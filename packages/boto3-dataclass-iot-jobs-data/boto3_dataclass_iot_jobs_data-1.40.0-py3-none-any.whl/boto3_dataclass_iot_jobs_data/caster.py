# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iot_jobs_data import type_defs as bs_td


class IOT_JOBS_DATACaster:

    def describe_job_execution(
        self,
        res: "bs_td.DescribeJobExecutionResponseTypeDef",
    ) -> "dc_td.DescribeJobExecutionResponse":
        return dc_td.DescribeJobExecutionResponse.make_one(res)

    def get_pending_job_executions(
        self,
        res: "bs_td.GetPendingJobExecutionsResponseTypeDef",
    ) -> "dc_td.GetPendingJobExecutionsResponse":
        return dc_td.GetPendingJobExecutionsResponse.make_one(res)

    def start_command_execution(
        self,
        res: "bs_td.StartCommandExecutionResponseTypeDef",
    ) -> "dc_td.StartCommandExecutionResponse":
        return dc_td.StartCommandExecutionResponse.make_one(res)

    def start_next_pending_job_execution(
        self,
        res: "bs_td.StartNextPendingJobExecutionResponseTypeDef",
    ) -> "dc_td.StartNextPendingJobExecutionResponse":
        return dc_td.StartNextPendingJobExecutionResponse.make_one(res)

    def update_job_execution(
        self,
        res: "bs_td.UpdateJobExecutionResponseTypeDef",
    ) -> "dc_td.UpdateJobExecutionResponse":
        return dc_td.UpdateJobExecutionResponse.make_one(res)


iot_jobs_data_caster = IOT_JOBS_DATACaster()
