# Copyright (c) 2024-2025, Huawei Technologies Co., Ltd.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0  (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import threading
import sys
from collections import OrderedDict

import torch
from torch.utils.hooks import BackwardHook, RemovableHandle

from msprobe.core.common.const import Const
from msprobe.core.common.runtime import Runtime
from msprobe.core.common.utils import ModuleQueue, ThreadSafe
from msprobe.core.common.megatron_utils import wrap_megatron_step, get_micro_step, is_megatron
from msprobe.core.data_dump.scope import BaseScope, ModuleRangeScope, MixRangeScope
from msprobe.pytorch.common.log import logger
from msprobe.pytorch.common.utils import is_torch_nn_module, register_forward_pre_hook
from msprobe.pytorch.dump.module_dump.hook_wrapper import wrap_setup_input_output_hook

torch_version_above_or_equal_2 = torch.__version__.split('+')[0] >= '2.0'
torch_version_above_or_equal_21 = torch.__version__.split('+')[0] >= '2.1'
if torch_version_above_or_equal_21:
    from torch.utils.checkpoint import _StopRecomputationError


def wrap_megatron_deallocate(func):
    def wrapper_func(out, deallocate_pipeline_outputs=False):
        if deallocate_pipeline_outputs and isinstance(out, torch.Tensor) and getattr(out, "_base") is not None:
            out_clone = out.clone()
            out.data = torch.empty((1,), device=out.device, dtype=out.dtype, )
            return func(out_clone, deallocate_pipeline_outputs)
        return func(out, deallocate_pipeline_outputs)

    return wrapper_func


def wrap_forward_with_hook_safety(module):
    """
    包装模块的forward方法，确保异常时也执行forward_hook。
    """
    original_forward = module.forward

    def wrapped_forward(*args, **kwargs):
        try:
            output = original_forward(*args, **kwargs)
            return output
        except _StopRecomputationError as e:
            exception_output = None
            if len(module._forward_hooks.values()) > 0:
                # msprobe的forward_hook会出现在第一个，仅执行msprobe的forward_hook
                hook_fn = list(module._forward_hooks.values())[0]
                hook_fn(module, args, kwargs, exception_output)
            raise e
    if torch_version_above_or_equal_21:
        module.forward = wrapped_forward


class ModuleProcesser:
    module_queue = ModuleQueue()
    module_count = {}
    module_stack = {}
    api_parent_node = {}
    module_node = {}
    module_bw_hook_kernels = {}
    module_with_backward_hook = {}
    enable_module_dump = False

    def __init__(self, scope):
        self.scope = scope if isinstance(scope, (ModuleRangeScope, MixRangeScope)) else None
        wrap_setup_input_output_hook()
        try:
            from megatron.core.pipeline_parallel import schedules
            origin_func_id = id(schedules.deallocate_output_tensor)
            schedules.deallocate_output_tensor = wrap_megatron_deallocate(schedules.deallocate_output_tensor)
            schedules.forward_step = wrap_megatron_step(schedules.forward_step)
            schedules.backward_step = wrap_megatron_step(schedules.backward_step, is_forward=False)
            for module in list(sys.modules.values()):
                if module.__name__ == 'schedules':
                    continue
                for func in module.__dict__:
                    if id(module.__dict__[func]) == origin_func_id:
                        module.__setattr__(func, schedules.deallocate_output_tensor)
                        logger.debug(f'patch {module.__name__}.{func}.')
            logger.info_on_rank_0("Patch megatron method success.")
        except ImportError:
            logger.info_on_rank_0("No megatron find.")
        except Exception as e:
            logger.info_on_rank_0(f"Patch megatron method failed, detail:{str(e)}")

    @staticmethod
    def set_and_get_calls_number(module_name):
        if module_name not in ModuleProcesser.module_count:
            ModuleProcesser.module_count[module_name] = 0
        else:
            ModuleProcesser.module_count[module_name] += 1
        return ModuleProcesser.module_count[module_name]

    @staticmethod
    def has_register_backward_hook(module):
        return hasattr(module, '_backward_hooks') and \
            len(module._backward_hooks) > 0 and \
            module._is_full_backward_hook is False

    @staticmethod
    def get_modules_and_names(models, recursive, module_names):
        modules_and_names_with_index = {}
        if isinstance(models, (list, tuple)):
            if not recursive and len(module_names) != len(models):
                return modules_and_names_with_index
            for index, model in enumerate(models):
                modules_and_names_with_index[str(index)] = model.named_modules() if recursive else \
                    [(module_names[index], model)]
        else:
            if not recursive and len(module_names) != 1:
                return modules_and_names_with_index
            modules_and_names_with_index["-1"] = models.named_modules() if recursive else \
                [(module_names[0], models)]
        return modules_and_names_with_index

    @classmethod
    def reset_module_stats(cls):
        cls.module_queue = ModuleQueue()
        cls.module_count = {}
        cls.module_stack = {}
        cls.api_parent_node = {}
        cls.module_node = {}
        cls.module_bw_hook_kernels = {}
        cls.enable_module_dump = False

    def register_module_hook(self, models, build_hook, recursive=True, module_names=None):
        if module_names is None:
            module_names = []

        modules_and_names_with_index = self.get_modules_and_names(models, recursive, module_names)
        for index, modules_and_names in modules_and_names_with_index.items():
            model = models if index == "-1" else models[int(index)]
            for name, module in modules_and_names:
                if recursive and module == model:
                    continue
                if not is_torch_nn_module(module):
                    logger.warning(
                        f"The module dump does not support {type(module)} type. "
                        f"The data dump for this module will be skipped."
                    )
                    continue
                if module.__class__.__name__ == "FullyShardedDataParallel":
                    continue
                setattr(module, 'msprobe_hook', True)
                module_index = (index + Const.SEP) if index != "-1" else ""
                prefix_name = f'{BaseScope.Module_Type_Module}{Const.SEP}{module_index}{name}{Const.SEP}' + \
                              f'{module.__class__.__name__}{Const.SEP}'

                forward_pre_hook = self.build_module_hook(prefix_name, build_hook)

                if self.has_register_backward_hook(module):
                    logger.warning(
                        f"The {prefix_name[:-1]} has registered deprecated register_backward_hook,"
                        f"which may cause abnormal data dump. The backward data dump for this module will be skipped."
                    )
                    ModuleProcesser.module_with_backward_hook[prefix_name] = True
                wrap_forward_with_hook_safety(module)
                register_forward_pre_hook(module, forward_pre_hook)

    def build_module_hook(self, module_name, build_data_hook):
        @ThreadSafe.synchronized
        def forward_pre_hook(module, args, kwargs=None):
            if kwargs is None:
                kwargs = {}

            if not Runtime.is_running:
                return (args, kwargs) if torch_version_above_or_equal_2 else args

            if hasattr(module, 'msprobe_module_dump') and not self.enable_module_dump:
                return (args, kwargs) if torch_version_above_or_equal_2 else args

            index = ModuleProcesser.set_and_get_calls_number(module_name)
            full_forward_name = f'{module_name}{Const.FORWARD}{Const.SEP}{index}'
            full_backward_name = f'{module_name}{Const.BACKWARD}{Const.SEP}{index}'

            self.set_construct_info_in_pre_hook(full_forward_name)

            if not hasattr(module, 'msprobe_forward_hook'):
                forward_hooks_dict = getattr(module, '_forward_hooks', OrderedDict())
                handle = RemovableHandle(forward_hooks_dict)
                forward_hooks_dict[handle.id] = forward_hook
                forward_hooks_dict.move_to_end(handle.id, last=False)
                if torch_version_above_or_equal_2:
                    forward_hooks_with_kwargs_dict = getattr(module, '_forward_hooks_with_kwargs', OrderedDict())
                    forward_hooks_with_kwargs_dict[handle.id] = True

                setattr(module, 'msprobe_forward_hook', True)

            hook_set = build_data_hook(BaseScope.Module_Type_Module, full_forward_name)

            def get_backward_pre_hook(full_backward_name):
                @ThreadSafe.synchronized
                def backward_pre_hook_fn(module, grad_output):
                    self.set_construct_info_in_pre_hook(full_backward_name)

                return backward_pre_hook_fn

            def get_backward_hook(backward_data_hook, full_backward_name):
                @ThreadSafe.synchronized
                def backward_hook_fn(module, grad_input, grad_output):
                    new_output = backward_data_hook(module, grad_input, grad_output)
                    self.set_construct_info_in_hook(full_backward_name, is_forward=False)
                    return new_output

                return backward_hook_fn

            if not ModuleProcesser.module_with_backward_hook.get(module_name):
                backward_pre_hook = get_backward_pre_hook(full_backward_name)
                backward_hook = get_backward_hook(hook_set.backward_hook, full_backward_name)
                if torch_version_above_or_equal_2:
                    bw_hook = BackwardHook(module, [backward_hook], [backward_pre_hook])
                else:
                    bw_hook = BackwardHook(module, [backward_hook])
                ModuleProcesser.module_bw_hook_kernels[full_forward_name] = bw_hook
                args = bw_hook.setup_input_hook(args)
            return (args, kwargs) if torch_version_above_or_equal_2 else args

        @ThreadSafe.synchronized
        def forward_hook(module, args, kwargs_or_output, output_or_kwargs=None):
            if hasattr(module, 'msprobe_module_dump') and not self.enable_module_dump:
                return output_or_kwargs if torch_version_above_or_equal_2 else kwargs_or_output

            index = ModuleProcesser.module_count.get(module_name)
            full_name = f'{module_name}{Const.FORWARD}{Const.SEP}{index}'

            hook_set = build_data_hook(BaseScope.Module_Type_Module, full_name)
            hook_result = hook_set.forward_hook(module, args, kwargs_or_output, output_or_kwargs)
            self.set_construct_info_in_hook(full_name)

            if hook_result is not None:
                result = hook_result
            else:
                result = output_or_kwargs if torch_version_above_or_equal_2 else kwargs_or_output

            bw_hook = ModuleProcesser.module_bw_hook_kernels.get(full_name)
            if bw_hook:
                result = bw_hook.setup_output_hook(result)

            return result

        return forward_pre_hook

    def set_construct_info_in_pre_hook(self, full_name):
        tid = threading.get_ident()
        if tid not in self.module_stack:
            ModuleProcesser.module_stack[tid] = []

        if self.module_stack[tid]:
            ModuleProcesser.module_node[full_name] = self.module_stack[tid][-1] if not is_megatron() \
                else [self.module_stack[tid][-1], get_micro_step()]
        else:
            parent_name = ModuleProcesser.module_queue.find_last(full_name)
            ModuleProcesser.module_node[full_name] = parent_name if not is_megatron() \
                else [parent_name, get_micro_step()]

        ModuleProcesser.module_queue.add_name(full_name)
        ModuleProcesser.module_stack[tid].append(full_name)
        ModuleProcesser.api_parent_node[tid] = full_name if not is_megatron() else [full_name, get_micro_step()]
        if self.scope:
            self.scope.begin_module(full_name)

    def set_construct_info_in_hook(self, full_name, is_forward=True):
        tid = threading.get_ident()
        if torch_version_above_or_equal_2 or is_forward:
            ModuleProcesser.module_queue.remove_name(full_name)
            ModuleProcesser.api_parent_node[tid] = None if not is_megatron() else [None, get_micro_step()]
            if self.module_stack.get(tid):
                ModuleProcesser.module_stack[tid].pop()
            if self.module_stack.get(tid):
                ModuleProcesser.api_parent_node[tid] = ModuleProcesser.module_stack[tid][-1] if not is_megatron() \
                    else [ModuleProcesser.module_stack[tid][-1], get_micro_step()]
            if self.scope:
                self.scope.end_module(full_name)
        else:
            if self.scope:
                self.scope.begin_module(full_name)
            ModuleProcesser.api_parent_node[tid] = full_name if not is_megatron() else [full_name, get_micro_step()]
