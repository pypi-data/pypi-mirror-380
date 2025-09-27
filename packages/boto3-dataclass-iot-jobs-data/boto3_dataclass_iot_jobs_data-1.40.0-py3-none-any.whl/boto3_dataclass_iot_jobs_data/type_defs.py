# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iot_jobs_data import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class DescribeJobExecutionRequest:
    boto3_raw_data: "type_defs.DescribeJobExecutionRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    thingName = field("thingName")
    includeJobDocument = field("includeJobDocument")
    executionNumber = field("executionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecution:
    boto3_raw_data: "type_defs.JobExecutionTypeDef" = dataclasses.field()

    jobId = field("jobId")
    thingName = field("thingName")
    status = field("status")
    statusDetails = field("statusDetails")
    queuedAt = field("queuedAt")
    startedAt = field("startedAt")
    lastUpdatedAt = field("lastUpdatedAt")
    approximateSecondsBeforeTimedOut = field("approximateSecondsBeforeTimedOut")
    versionNumber = field("versionNumber")
    executionNumber = field("executionNumber")
    jobDocument = field("jobDocument")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobExecutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPendingJobExecutionsRequest:
    boto3_raw_data: "type_defs.GetPendingJobExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPendingJobExecutionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPendingJobExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecutionSummary:
    boto3_raw_data: "type_defs.JobExecutionSummaryTypeDef" = dataclasses.field()

    jobId = field("jobId")
    queuedAt = field("queuedAt")
    startedAt = field("startedAt")
    lastUpdatedAt = field("lastUpdatedAt")
    versionNumber = field("versionNumber")
    executionNumber = field("executionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobExecutionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecutionState:
    boto3_raw_data: "type_defs.JobExecutionStateTypeDef" = dataclasses.field()

    status = field("status")
    statusDetails = field("statusDetails")
    versionNumber = field("versionNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobExecutionStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobExecutionStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartNextPendingJobExecutionRequest:
    boto3_raw_data: "type_defs.StartNextPendingJobExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    statusDetails = field("statusDetails")
    stepTimeoutInMinutes = field("stepTimeoutInMinutes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartNextPendingJobExecutionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartNextPendingJobExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobExecutionRequest:
    boto3_raw_data: "type_defs.UpdateJobExecutionRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    thingName = field("thingName")
    status = field("status")
    statusDetails = field("statusDetails")
    stepTimeoutInMinutes = field("stepTimeoutInMinutes")
    expectedVersion = field("expectedVersion")
    includeJobExecutionState = field("includeJobExecutionState")
    includeJobDocument = field("includeJobDocument")
    executionNumber = field("executionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJobExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandParameterValue:
    boto3_raw_data: "type_defs.CommandParameterValueTypeDef" = dataclasses.field()

    S = field("S")
    B = field("B")
    I = field("I")
    L = field("L")
    D = field("D")
    BIN = field("BIN")
    UL = field("UL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommandParameterValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommandParameterValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobExecutionResponse:
    boto3_raw_data: "type_defs.DescribeJobExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def execution(self):  # pragma: no cover
        return JobExecution.make_one(self.boto3_raw_data["execution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCommandExecutionResponse:
    boto3_raw_data: "type_defs.StartCommandExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    executionId = field("executionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartCommandExecutionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCommandExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartNextPendingJobExecutionResponse:
    boto3_raw_data: "type_defs.StartNextPendingJobExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def execution(self):  # pragma: no cover
        return JobExecution.make_one(self.boto3_raw_data["execution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartNextPendingJobExecutionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartNextPendingJobExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPendingJobExecutionsResponse:
    boto3_raw_data: "type_defs.GetPendingJobExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def inProgressJobs(self):  # pragma: no cover
        return JobExecutionSummary.make_many(self.boto3_raw_data["inProgressJobs"])

    @cached_property
    def queuedJobs(self):  # pragma: no cover
        return JobExecutionSummary.make_many(self.boto3_raw_data["queuedJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPendingJobExecutionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPendingJobExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobExecutionResponse:
    boto3_raw_data: "type_defs.UpdateJobExecutionResponseTypeDef" = dataclasses.field()

    @cached_property
    def executionState(self):  # pragma: no cover
        return JobExecutionState.make_one(self.boto3_raw_data["executionState"])

    jobDocument = field("jobDocument")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJobExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCommandExecutionRequest:
    boto3_raw_data: "type_defs.StartCommandExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    targetArn = field("targetArn")
    commandArn = field("commandArn")
    parameters = field("parameters")
    executionTimeoutSeconds = field("executionTimeoutSeconds")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCommandExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCommandExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
