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

import itertools
import os
from dataclasses import dataclass
from collections import defaultdict

import pandas as pd
from mindspore import ops
from mindspore import Tensor
from mindspore import _no_grad

from msprobe.core.common.log import logger
from msprobe.core.common.file_utils import change_mode, create_directory, write_df_to_csv
from msprobe.core.monitor.anomaly_processor import AnomalyDataFactory, AnomalyTurbulence, AnomalyScanner
from msprobe.core.common.const import FileCheckConst, MonitorConst


class BCOLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@dataclass
class WriterInput:
    path: str
    ad_rules: list
    job_id: str
    anomaly_factory: AnomalyDataFactory = None
    ndigits: int = 6
    step_count_per_record: int = 1


class BaseWriterWithAD:
    def __init__(self, writer_input: WriterInput):
        self.tag2scalars = {}
        self.ad_rules = writer_input.ad_rules
        self.job_id = writer_input.job_id
        self.anomaly_factory = writer_input.anomaly_factory
        self.anomalies = []
        self.ndigits = writer_input.ndigits
        self.beta = 0.99

    @staticmethod
    def stack_tensors(tensor_list):
        """
        Torch not support stack cpu and xpu tensors. Group the tensors into cpu_group and xpu_group,
        stack them separately, migrate xpu_group to cpu, and then restore in the order of input.

        :param tensor_list: [tensor(-1.6165), tensor(-1.0985), tensor(-1.7777), tensor(-1.8408, device='npu:0')]
        :return: result: list of float
        """
        cpu_tensors = []
        xpu_tensors = []

        for tensor in tensor_list:
            if isinstance(tensor, Tensor):
                # 将device上的tensor先stack后to cpu
                xpu_tensors.append(tensor)
            else:
                cpu_tensors.append(tensor)

        xpu_stack = ops.stack(xpu_tensors).tolist() if xpu_tensors else ops.tensor([])

        # 按照输入的顺序恢复
        result = []
        cpu_tensors_idx, xpu_tensors_idx = 0, 0
        for tensor in tensor_list:
            if isinstance(tensor, Tensor):
                result.append(xpu_stack[xpu_tensors_idx])
                xpu_tensors_idx += 1
            else:
                result.append(cpu_tensors[cpu_tensors_idx])
                cpu_tensors_idx += 1

        return result

    def get_anomalies(self):
        """返回已检测到的异常列表
        """
        return self.anomalies

    def clear_anomalies(self):
        self.anomalies.clear()

    def add_scalar(self, tag, scalar_value, global_step=None, need_explain=False):
        """If an anomaly is detected, the anomaly information is recorded and added to self.anomalies.
        Args:
            tag (tuple): tuple of tag_name and tag like ('0:1.post_attention_norm.weight/rank0/pre_grad', 'min').
            scalar_value (float): scalar_value.
            global_step (int): global_step.
        Returns:
            None
        """
        if not self.ad_rules or tag[-1] in ["shape", "dtype"]:
            return
        if isinstance(scalar_value, Tensor):
            scalar_value = scalar_value.item()
        avg = self._update_tag2scalars(tag, scalar_value)
        detected, rule_name = self._ad(scalar_value, history=avg)
        if detected:
            if rule_name == AnomalyTurbulence.name and tag[-1] not in ["norm", "mean"]:
                return
            exception_message = (f"Rule {rule_name} reports anomaly signal in {tag} at step {global_step}, "
                                 f"current value {scalar_value}, history mean {avg}.")
            logger.info(f"{BCOLORS.WARNING}> {exception_message}{BCOLORS.ENDC}")
            # append to self.anomalies for dump
            if self.anomaly_factory:
                self.anomalies.append(self.anomaly_factory.create(tag, exception_message, global_step))

    def write_metrics(self, op_list, metric_value, step, prefix='', need_explain=False):
        if not metric_value:
            return
        tensors = []
        tags = list(itertools.product(metric_value.keys(), op_list))
        for op2tensor in metric_value.values():
            tensors.extend(op2tensor.values())

        if not tensors:
            return

        with _no_grad():
            metric_list = self.stack_tensors(tensors)
        for tag, metric in zip(tags, metric_list):
            self.add_scalar(tag, metric, step, need_explain)

    def _ad(self, scalar_value, history):
        return AnomalyScanner.scan(self.ad_rules, history, cur=scalar_value)

    def _update_tag2scalars(self, tag, scalar_value):
        """Update the average and count of a scalar value associated with a tag.

        This method is used to maintain a running average of scalar values for each tag.


        Args:
            tag (str): The tag identifier.
            scalar_value (float): The scalar value to be added.

        Returns:
            float: The average value before update.
        """
        abs_scalar_value = abs(scalar_value)
        if tag not in self.tag2scalars:
            self.tag2scalars[tag] = {'avg': abs_scalar_value, 'count': 0}
        avg = self.tag2scalars[tag]['avg']
        self.tag2scalars[tag]['avg'] = self.beta * avg + (1 - self.beta) * abs_scalar_value
        self.tag2scalars[tag]['count'] += 1
        return avg


class CSVWriterWithAD(BaseWriterWithAD):
    def __init__(self, writer_input: WriterInput):
        super().__init__(writer_input)

        path = writer_input.path
        self.log_dir = path
        create_directory(path)
        change_mode(path, FileCheckConst.DATA_DIR_AUTHORITY)
        self.context_dict = defaultdict(list)
        self.header = []
        self.step_count_per_record = writer_input.step_count_per_record

    def get_step_interval(self, step):
        count = step // self.step_count_per_record
        return count * self.step_count_per_record, (count + 1) * self.step_count_per_record - 1

    def write_csv(self, prefix, step):
        """
        Args:
            prefix[str]: prefix of output csv file e.g. grad_unreduced
            step[int]
        """
        if len(self.context_dict) == 0:
            return

        ster_start, step_end = self.get_step_interval(step)
        filepath = os.path.join(self.log_dir, f'{prefix}_{ster_start}-{step_end}.csv')
        if not os.path.exists(filepath):
            data_frame = pd.DataFrame(columns=self.header)
            write_df_to_csv(data_frame, filepath)

        new_data = []
        for name, metric_value in self.context_dict.items():
            new_line = name.split(MonitorConst.NAME_SEP) + metric_value
            new_line.insert(2, step)
            new_data.append(new_line)
        new_data = pd.DataFrame(new_data).round(self.ndigits).fillna("nan")
        write_df_to_csv(new_data, filepath, mode='a+', header=False)
        self.context_dict = defaultdict(list)

    def add_scalar(self, tag, scalar_value, global_step, need_explain=False):
        """
        ('0:1.post_attention_norm.weight/rank0/pre_grad', 'min')
        """
        super().add_scalar(tag, scalar_value, global_step, need_explain=False)
        split_name = tag[0].split('/')
        name = split_name[0]
        if need_explain:
            if 'pre' in split_name[-1]:
                name += '.input'
            if 'post' in split_name[-1]:
                name += '.output'
        self.context_dict[name].append(scalar_value)

    def write_metrics(self, op_list, metric_value, step, prefix='', need_explain=False, **kwargs):
        need_explain = prefix == 'other'
        super().write_metrics(op_list, metric_value, step, prefix='', need_explain=need_explain)

        if prefix in [MonitorConst.ACTV, MonitorConst.ACTVGRAD] or kwargs.get("use_micro_step"):
            self.header = MonitorConst.CSV_HEADER_MICRO_STEP + op_list
        else:
            self.header = MonitorConst.CSV_HEADER + op_list
        self.write_csv(prefix, step)

    def close(self):
        pass
