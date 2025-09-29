# Copyright (c) 2025, Huawei Technologies Co., Ltd.
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
from collections import OrderedDict

import mindspore as ms
from mindspore import Tensor
from mindspore.common.api import _no_grad, _pynative_executor
from mindspore.ops.operations import _inner_ops as inner

from msprobe.core.common.const import Const
from msprobe.core.common.log import logger
from msprobe.core.common.utils import replace_last_occurrence, ThreadSafe
from msprobe.core.data_dump.data_processor.base import ModuleBackwardInputs
from msprobe.core.hook_manager import BaseHookManager, HookSet
from msprobe.mindspore.common.const import Const as MsConst
from msprobe.mindspore.common.utils import (
    has_kwargs_in_forward_hook,
    is_mindtorch,
    is_backward_hook_output_a_view
)
from msprobe.mindspore.dump.hook_cell.hook_cell import HOOKCell

ms_version = ms.__version__


class MindsporeHookManager(BaseHookManager):
    cell_bw_hook_kernels = {}
    cell_backward_pre_hook = []
    cell_backward_hook = []

    @property
    def _is_recompute(self):
        return None

    @staticmethod
    def reset_status():
        BaseHookManager.reset_status()
        MindsporeHookManager.cell_bw_hook_kernels.clear()
        MindsporeHookManager.cell_backward_pre_hook.clear()
        MindsporeHookManager.cell_backward_hook.clear()

    @staticmethod
    def _no_grad_context():
        return _no_grad()

    @staticmethod
    def _add_count(name):
        HOOKCell.add_cell_count(name)

    @staticmethod
    def _get_count(name):
        return HOOKCell.get_cell_count(name)

    @staticmethod
    def _process_kwargs_and_output(module, tid, hook_type, kwargs_or_output, output_or_kwargs):
        if not has_kwargs_in_forward_hook() or hook_type == Const.API:
            kwargs = module.msprobe_input_kwargs.get(tid, {}) if hasattr(module, 'msprobe_input_kwargs') else {}
            output = kwargs_or_output
        else:
            kwargs = kwargs_or_output
            output = output_or_kwargs
        return kwargs, output

    def build_hook(self, hook_type, name):
        if hook_type == Const.API:
            hook_set = HookSet(
                forward_pre_hook=self._build_forward_pre_hook(hook_type, name)
            )
        else:
            full_backward_name = replace_last_occurrence(name, Const.FORWARD, Const.BACKWARD)
            hook_set = HookSet(
                forward_hook=self._build_forward_hook(hook_type, name),
                backward_pre_hook=self._build_backward_pre_hook(hook_type, full_backward_name),
                backward_hook=self._build_backward_hook(hook_type, full_backward_name)
            )
        return hook_set

    def _register_forward_hook(self, module, api_name):
        if not hasattr(module, 'msprobe_forward_hook'):
            forward_hook = self._build_forward_hook(Const.API, api_name)
            if ms_version < "2.6.0" and not is_mindtorch():
                getattr(module, "_forward_hook", {})[id(module)] = forward_hook
            else:
                module.register_forward_hook(forward_hook)
            setattr(module, 'msprobe_forward_hook', True)

    def _register_backward_hook(self, module, full_backward_name, args):
        if not _pynative_executor.requires_grad():
            return args

        enable_hooked = sum(
            [isinstance(ele, Tensor) and ele.dtype not in MsConst.NonDifferentiableType for ele in args]
        )

        if enable_hooked:
            backward_hook_dict = OrderedDict()
            backward_hook_dict[full_backward_name] = self._build_backward_hook(Const.API, full_backward_name)
            MindsporeHookManager.cell_backward_hook.append(backward_hook_dict)
            bw_hook = inner.CellBackwardHook(full_backward_name, module, MindsporeHookManager.cell_backward_hook[-1])
            bw_hook.register_backward_hook()
            MindsporeHookManager.cell_bw_hook_kernels[full_backward_name] = bw_hook
            args = bw_hook(args) if is_backward_hook_output_a_view() else bw_hook(*args)
        return args

    def _register_backward_pre_hook(self, module, full_backward_name, output):
        if not _pynative_executor.requires_grad():
            return output

        bw_hook = MindsporeHookManager.cell_bw_hook_kernels.get(full_backward_name)
        if bw_hook:
            if not isinstance(output, (Tensor, tuple)):
                logger.debug("For backward hooks to be called, "
                             "cell output should be a Tensor or a tuple of Tensors "
                             f"but received {type(output)}")
            if is_backward_hook_output_a_view():
                new_outputs = bw_hook(output)
            else:
                if isinstance(output, tuple):
                    new_outputs = bw_hook(*output)
                else:
                    new_outputs = bw_hook(output)
                if isinstance(output, tuple) and len(output) == 1:
                    new_outputs = (new_outputs,)
            output = new_outputs

        def get_backward_pre_hook(backward_pre_hook, backward_post_hook):
            @ThreadSafe.synchronized
            def backward_pre_hook_fn(cell, grad_output):
                backward_pre_hook(cell, grad_output)
                if backward_post_hook:
                    backward_post_hook(cell, (), grad_output)

            return backward_pre_hook_fn

        backward_pre_hook = self._build_backward_pre_hook(Const.API, full_backward_name)
        backward_post_hook = None if bw_hook else self._build_backward_hook(Const.API, full_backward_name)

        backward_pre_hook_dict = OrderedDict()
        backward_pre_hook_dict[full_backward_name] = get_backward_pre_hook(
            backward_pre_hook,
            backward_post_hook
        )
        MindsporeHookManager.cell_backward_pre_hook.append(backward_pre_hook_dict)
        bw_pre_hook = inner.CellBackwardHook(
            full_backward_name,
            module,
            MindsporeHookManager.cell_backward_pre_hook[-1]
        )
        bw_pre_hook.register_backward_pre_hook()

        if is_backward_hook_output_a_view():
            result = bw_pre_hook(output)
        else:
            if isinstance(output, tuple):
                result = bw_pre_hook(*output)
            else:
                result = bw_pre_hook(output)
            if isinstance(output, tuple):
                if len(output) == 1:
                    result = (result,)
                if len(result) != len(output):
                    raise TypeError(
                        f"The backward pre hook return value size is {len(result)} "
                        f"not equal to output size {len(output)}"
                    )
        return result

    def _need_exchange(self, module):
        if not hasattr(module, 'has_pre_hook_called') or not module.has_pre_hook_called:
            return False
        else:
            return True

    def _get_params_dict(self, module):
        params_dict = {}
        if self.config.task != Const.STRUCTURE:
            params_dict = {
                key.split(Const.SEP)[-1]: value
                for key, value in module.parameters_dict(recurse=False).items()
            }
        return params_dict

    def _build_backward_pre_hook(self, hook_type, full_name):
        def backward_pre_hook(module, grad_input):
            if self.config.level != Const.LEVEL_L2:
                return
            tid = threading.get_ident()
            if not self._should_execute_hook(tid):
                return

            with ThreadSafe():
                original_state = self.ensure_gc_enabled()
                BaseHookManager.inner_switch[tid] = True
                module_input = ModuleBackwardInputs(grad_input=grad_input)
                self.data_collector.update_api_or_module_name(full_name)
                self.data_collector.backward_input_data_collect(full_name, module, self._pid, module_input)
                BaseHookManager.inner_switch[tid] = False
                self.restore_gc_state(original_state)

        return backward_pre_hook
