# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_stepfunctions import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActivityFailedEventDetails:
    boto3_raw_data: "type_defs.ActivityFailedEventDetailsTypeDef" = dataclasses.field()

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivityFailedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityListItem:
    boto3_raw_data: "type_defs.ActivityListItemTypeDef" = dataclasses.field()

    activityArn = field("activityArn")
    name = field("name")
    creationDate = field("creationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityScheduleFailedEventDetails:
    boto3_raw_data: "type_defs.ActivityScheduleFailedEventDetailsTypeDef" = (
        dataclasses.field()
    )

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActivityScheduleFailedEventDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityScheduleFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HistoryEventExecutionDataDetails:
    boto3_raw_data: "type_defs.HistoryEventExecutionDataDetailsTypeDef" = (
        dataclasses.field()
    )

    truncated = field("truncated")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HistoryEventExecutionDataDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HistoryEventExecutionDataDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityStartedEventDetails:
    boto3_raw_data: "type_defs.ActivityStartedEventDetailsTypeDef" = dataclasses.field()

    workerName = field("workerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivityStartedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityStartedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTimedOutEventDetails:
    boto3_raw_data: "type_defs.ActivityTimedOutEventDetailsTypeDef" = (
        dataclasses.field()
    )

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivityTimedOutEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTimedOutEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignedVariablesDetails:
    boto3_raw_data: "type_defs.AssignedVariablesDetailsTypeDef" = dataclasses.field()

    truncated = field("truncated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssignedVariablesDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignedVariablesDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillingDetails:
    boto3_raw_data: "type_defs.BillingDetailsTypeDef" = dataclasses.field()

    billedMemoryUsedInMB = field("billedMemoryUsedInMB")
    billedDurationInMilliseconds = field("billedDurationInMilliseconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BillingDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BillingDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchEventsExecutionDataDetails:
    boto3_raw_data: "type_defs.CloudWatchEventsExecutionDataDetailsTypeDef" = (
        dataclasses.field()
    )

    included = field("included")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudWatchEventsExecutionDataDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchEventsExecutionDataDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsLogGroup:
    boto3_raw_data: "type_defs.CloudWatchLogsLogGroupTypeDef" = dataclasses.field()

    logGroupArn = field("logGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogsLogGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsLogGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    type = field("type")
    kmsKeyId = field("kmsKeyId")
    kmsDataKeyReusePeriodSeconds = field("kmsDataKeyReusePeriodSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
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
class RoutingConfigurationListItem:
    boto3_raw_data: "type_defs.RoutingConfigurationListItemTypeDef" = (
        dataclasses.field()
    )

    stateMachineVersionArn = field("stateMachineVersionArn")
    weight = field("weight")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingConfigurationListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingConfigurationListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TracingConfiguration:
    boto3_raw_data: "type_defs.TracingConfigurationTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TracingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TracingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteActivityInput:
    boto3_raw_data: "type_defs.DeleteActivityInputTypeDef" = dataclasses.field()

    activityArn = field("activityArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteActivityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteActivityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStateMachineAliasInput:
    boto3_raw_data: "type_defs.DeleteStateMachineAliasInputTypeDef" = (
        dataclasses.field()
    )

    stateMachineAliasArn = field("stateMachineAliasArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStateMachineAliasInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStateMachineAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStateMachineInput:
    boto3_raw_data: "type_defs.DeleteStateMachineInputTypeDef" = dataclasses.field()

    stateMachineArn = field("stateMachineArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStateMachineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStateMachineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStateMachineVersionInput:
    boto3_raw_data: "type_defs.DeleteStateMachineVersionInputTypeDef" = (
        dataclasses.field()
    )

    stateMachineVersionArn = field("stateMachineVersionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteStateMachineVersionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStateMachineVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActivityInput:
    boto3_raw_data: "type_defs.DescribeActivityInputTypeDef" = dataclasses.field()

    activityArn = field("activityArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeActivityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActivityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExecutionInput:
    boto3_raw_data: "type_defs.DescribeExecutionInputTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    includedData = field("includedData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMapRunInput:
    boto3_raw_data: "type_defs.DescribeMapRunInputTypeDef" = dataclasses.field()

    mapRunArn = field("mapRunArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMapRunInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMapRunInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapRunExecutionCounts:
    boto3_raw_data: "type_defs.MapRunExecutionCountsTypeDef" = dataclasses.field()

    pending = field("pending")
    running = field("running")
    succeeded = field("succeeded")
    failed = field("failed")
    timedOut = field("timedOut")
    aborted = field("aborted")
    total = field("total")
    resultsWritten = field("resultsWritten")
    failuresNotRedrivable = field("failuresNotRedrivable")
    pendingRedrive = field("pendingRedrive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MapRunExecutionCountsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapRunExecutionCountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapRunItemCounts:
    boto3_raw_data: "type_defs.MapRunItemCountsTypeDef" = dataclasses.field()

    pending = field("pending")
    running = field("running")
    succeeded = field("succeeded")
    failed = field("failed")
    timedOut = field("timedOut")
    aborted = field("aborted")
    total = field("total")
    resultsWritten = field("resultsWritten")
    failuresNotRedrivable = field("failuresNotRedrivable")
    pendingRedrive = field("pendingRedrive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MapRunItemCountsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapRunItemCountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStateMachineAliasInput:
    boto3_raw_data: "type_defs.DescribeStateMachineAliasInputTypeDef" = (
        dataclasses.field()
    )

    stateMachineAliasArn = field("stateMachineAliasArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStateMachineAliasInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStateMachineAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStateMachineForExecutionInput:
    boto3_raw_data: "type_defs.DescribeStateMachineForExecutionInputTypeDef" = (
        dataclasses.field()
    )

    executionArn = field("executionArn")
    includedData = field("includedData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStateMachineForExecutionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStateMachineForExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStateMachineInput:
    boto3_raw_data: "type_defs.DescribeStateMachineInputTypeDef" = dataclasses.field()

    stateMachineArn = field("stateMachineArn")
    includedData = field("includedData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStateMachineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStateMachineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFailedEventDetails:
    boto3_raw_data: "type_defs.EvaluationFailedEventDetailsTypeDef" = (
        dataclasses.field()
    )

    state = field("state")
    error = field("error")
    cause = field("cause")
    location = field("location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationFailedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionAbortedEventDetails:
    boto3_raw_data: "type_defs.ExecutionAbortedEventDetailsTypeDef" = (
        dataclasses.field()
    )

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutionAbortedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionAbortedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionFailedEventDetails:
    boto3_raw_data: "type_defs.ExecutionFailedEventDetailsTypeDef" = dataclasses.field()

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutionFailedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionListItem:
    boto3_raw_data: "type_defs.ExecutionListItemTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    stateMachineArn = field("stateMachineArn")
    name = field("name")
    status = field("status")
    startDate = field("startDate")
    stopDate = field("stopDate")
    mapRunArn = field("mapRunArn")
    itemCount = field("itemCount")
    stateMachineVersionArn = field("stateMachineVersionArn")
    stateMachineAliasArn = field("stateMachineAliasArn")
    redriveCount = field("redriveCount")
    redriveDate = field("redriveDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionRedrivenEventDetails:
    boto3_raw_data: "type_defs.ExecutionRedrivenEventDetailsTypeDef" = (
        dataclasses.field()
    )

    redriveCount = field("redriveCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExecutionRedrivenEventDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionRedrivenEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionTimedOutEventDetails:
    boto3_raw_data: "type_defs.ExecutionTimedOutEventDetailsTypeDef" = (
        dataclasses.field()
    )

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExecutionTimedOutEventDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionTimedOutEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetActivityTaskInput:
    boto3_raw_data: "type_defs.GetActivityTaskInputTypeDef" = dataclasses.field()

    activityArn = field("activityArn")
    workerName = field("workerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetActivityTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActivityTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExecutionHistoryInput:
    boto3_raw_data: "type_defs.GetExecutionHistoryInputTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    maxResults = field("maxResults")
    reverseOrder = field("reverseOrder")
    nextToken = field("nextToken")
    includeExecutionData = field("includeExecutionData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExecutionHistoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExecutionHistoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionFailedEventDetails:
    boto3_raw_data: "type_defs.LambdaFunctionFailedEventDetailsTypeDef" = (
        dataclasses.field()
    )

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LambdaFunctionFailedEventDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionScheduleFailedEventDetails:
    boto3_raw_data: "type_defs.LambdaFunctionScheduleFailedEventDetailsTypeDef" = (
        dataclasses.field()
    )

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionScheduleFailedEventDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionScheduleFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionStartFailedEventDetails:
    boto3_raw_data: "type_defs.LambdaFunctionStartFailedEventDetailsTypeDef" = (
        dataclasses.field()
    )

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionStartFailedEventDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionStartFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionTimedOutEventDetails:
    boto3_raw_data: "type_defs.LambdaFunctionTimedOutEventDetailsTypeDef" = (
        dataclasses.field()
    )

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionTimedOutEventDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionTimedOutEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapIterationEventDetails:
    boto3_raw_data: "type_defs.MapIterationEventDetailsTypeDef" = dataclasses.field()

    name = field("name")
    index = field("index")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MapIterationEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapIterationEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapRunFailedEventDetails:
    boto3_raw_data: "type_defs.MapRunFailedEventDetailsTypeDef" = dataclasses.field()

    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MapRunFailedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapRunFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapRunRedrivenEventDetails:
    boto3_raw_data: "type_defs.MapRunRedrivenEventDetailsTypeDef" = dataclasses.field()

    mapRunArn = field("mapRunArn")
    redriveCount = field("redriveCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MapRunRedrivenEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapRunRedrivenEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapRunStartedEventDetails:
    boto3_raw_data: "type_defs.MapRunStartedEventDetailsTypeDef" = dataclasses.field()

    mapRunArn = field("mapRunArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MapRunStartedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapRunStartedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapStateStartedEventDetails:
    boto3_raw_data: "type_defs.MapStateStartedEventDetailsTypeDef" = dataclasses.field()

    length = field("length")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MapStateStartedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapStateStartedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskFailedEventDetails:
    boto3_raw_data: "type_defs.TaskFailedEventDetailsTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resource = field("resource")
    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskFailedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskStartFailedEventDetails:
    boto3_raw_data: "type_defs.TaskStartFailedEventDetailsTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resource = field("resource")
    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskStartFailedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskStartFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskStartedEventDetails:
    boto3_raw_data: "type_defs.TaskStartedEventDetailsTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resource = field("resource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskStartedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskStartedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskSubmitFailedEventDetails:
    boto3_raw_data: "type_defs.TaskSubmitFailedEventDetailsTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    resource = field("resource")
    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskSubmitFailedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskSubmitFailedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskTimedOutEventDetails:
    boto3_raw_data: "type_defs.TaskTimedOutEventDetailsTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resource = field("resource")
    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskTimedOutEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskTimedOutEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InspectionDataRequest:
    boto3_raw_data: "type_defs.InspectionDataRequestTypeDef" = dataclasses.field()

    protocol = field("protocol")
    method = field("method")
    url = field("url")
    headers = field("headers")
    body = field("body")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InspectionDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InspectionDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InspectionDataResponse:
    boto3_raw_data: "type_defs.InspectionDataResponseTypeDef" = dataclasses.field()

    protocol = field("protocol")
    statusCode = field("statusCode")
    statusMessage = field("statusMessage")
    headers = field("headers")
    body = field("body")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InspectionDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InspectionDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskCredentials:
    boto3_raw_data: "type_defs.TaskCredentialsTypeDef" = dataclasses.field()

    roleArn = field("roleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskCredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskCredentialsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActivitiesInput:
    boto3_raw_data: "type_defs.ListActivitiesInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActivitiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActivitiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExecutionsInput:
    boto3_raw_data: "type_defs.ListExecutionsInputTypeDef" = dataclasses.field()

    stateMachineArn = field("stateMachineArn")
    statusFilter = field("statusFilter")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    mapRunArn = field("mapRunArn")
    redriveFilter = field("redriveFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExecutionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMapRunsInput:
    boto3_raw_data: "type_defs.ListMapRunsInputTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMapRunsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMapRunsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapRunListItem:
    boto3_raw_data: "type_defs.MapRunListItemTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    mapRunArn = field("mapRunArn")
    stateMachineArn = field("stateMachineArn")
    startDate = field("startDate")
    stopDate = field("stopDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MapRunListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MapRunListItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStateMachineAliasesInput:
    boto3_raw_data: "type_defs.ListStateMachineAliasesInputTypeDef" = (
        dataclasses.field()
    )

    stateMachineArn = field("stateMachineArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStateMachineAliasesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStateMachineAliasesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateMachineAliasListItem:
    boto3_raw_data: "type_defs.StateMachineAliasListItemTypeDef" = dataclasses.field()

    stateMachineAliasArn = field("stateMachineAliasArn")
    creationDate = field("creationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StateMachineAliasListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateMachineAliasListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStateMachineVersionsInput:
    boto3_raw_data: "type_defs.ListStateMachineVersionsInputTypeDef" = (
        dataclasses.field()
    )

    stateMachineArn = field("stateMachineArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStateMachineVersionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStateMachineVersionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateMachineVersionListItem:
    boto3_raw_data: "type_defs.StateMachineVersionListItemTypeDef" = dataclasses.field()

    stateMachineVersionArn = field("stateMachineVersionArn")
    creationDate = field("creationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StateMachineVersionListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateMachineVersionListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStateMachinesInput:
    boto3_raw_data: "type_defs.ListStateMachinesInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStateMachinesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStateMachinesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateMachineListItem:
    boto3_raw_data: "type_defs.StateMachineListItemTypeDef" = dataclasses.field()

    stateMachineArn = field("stateMachineArn")
    name = field("name")
    type = field("type")
    creationDate = field("creationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StateMachineListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateMachineListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishStateMachineVersionInput:
    boto3_raw_data: "type_defs.PublishStateMachineVersionInputTypeDef" = (
        dataclasses.field()
    )

    stateMachineArn = field("stateMachineArn")
    revisionId = field("revisionId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PublishStateMachineVersionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishStateMachineVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedriveExecutionInput:
    boto3_raw_data: "type_defs.RedriveExecutionInputTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedriveExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedriveExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendTaskFailureInput:
    boto3_raw_data: "type_defs.SendTaskFailureInputTypeDef" = dataclasses.field()

    taskToken = field("taskToken")
    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendTaskFailureInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendTaskFailureInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendTaskHeartbeatInput:
    boto3_raw_data: "type_defs.SendTaskHeartbeatInputTypeDef" = dataclasses.field()

    taskToken = field("taskToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendTaskHeartbeatInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendTaskHeartbeatInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendTaskSuccessInput:
    boto3_raw_data: "type_defs.SendTaskSuccessInputTypeDef" = dataclasses.field()

    taskToken = field("taskToken")
    output = field("output")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendTaskSuccessInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendTaskSuccessInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExecutionInput:
    boto3_raw_data: "type_defs.StartExecutionInputTypeDef" = dataclasses.field()

    stateMachineArn = field("stateMachineArn")
    name = field("name")
    input = field("input")
    traceHeader = field("traceHeader")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSyncExecutionInput:
    boto3_raw_data: "type_defs.StartSyncExecutionInputTypeDef" = dataclasses.field()

    stateMachineArn = field("stateMachineArn")
    name = field("name")
    input = field("input")
    traceHeader = field("traceHeader")
    includedData = field("includedData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSyncExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSyncExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopExecutionInput:
    boto3_raw_data: "type_defs.StopExecutionInputTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    error = field("error")
    cause = field("cause")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestStateInput:
    boto3_raw_data: "type_defs.TestStateInputTypeDef" = dataclasses.field()

    definition = field("definition")
    roleArn = field("roleArn")
    input = field("input")
    inspectionLevel = field("inspectionLevel")
    revealSecrets = field("revealSecrets")
    variables = field("variables")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestStateInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestStateInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMapRunInput:
    boto3_raw_data: "type_defs.UpdateMapRunInputTypeDef" = dataclasses.field()

    mapRunArn = field("mapRunArn")
    maxConcurrency = field("maxConcurrency")
    toleratedFailurePercentage = field("toleratedFailurePercentage")
    toleratedFailureCount = field("toleratedFailureCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateMapRunInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMapRunInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateStateMachineDefinitionDiagnostic:
    boto3_raw_data: "type_defs.ValidateStateMachineDefinitionDiagnosticTypeDef" = (
        dataclasses.field()
    )

    severity = field("severity")
    code = field("code")
    message = field("message")
    location = field("location")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateStateMachineDefinitionDiagnosticTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateStateMachineDefinitionDiagnosticTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateStateMachineDefinitionInput:
    boto3_raw_data: "type_defs.ValidateStateMachineDefinitionInputTypeDef" = (
        dataclasses.field()
    )

    definition = field("definition")
    type = field("type")
    severity = field("severity")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateStateMachineDefinitionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateStateMachineDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityScheduledEventDetails:
    boto3_raw_data: "type_defs.ActivityScheduledEventDetailsTypeDef" = (
        dataclasses.field()
    )

    resource = field("resource")
    input = field("input")

    @cached_property
    def inputDetails(self):  # pragma: no cover
        return HistoryEventExecutionDataDetails.make_one(
            self.boto3_raw_data["inputDetails"]
        )

    timeoutInSeconds = field("timeoutInSeconds")
    heartbeatInSeconds = field("heartbeatInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActivityScheduledEventDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityScheduledEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivitySucceededEventDetails:
    boto3_raw_data: "type_defs.ActivitySucceededEventDetailsTypeDef" = (
        dataclasses.field()
    )

    output = field("output")

    @cached_property
    def outputDetails(self):  # pragma: no cover
        return HistoryEventExecutionDataDetails.make_one(
            self.boto3_raw_data["outputDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActivitySucceededEventDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivitySucceededEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionStartedEventDetails:
    boto3_raw_data: "type_defs.ExecutionStartedEventDetailsTypeDef" = (
        dataclasses.field()
    )

    input = field("input")

    @cached_property
    def inputDetails(self):  # pragma: no cover
        return HistoryEventExecutionDataDetails.make_one(
            self.boto3_raw_data["inputDetails"]
        )

    roleArn = field("roleArn")
    stateMachineAliasArn = field("stateMachineAliasArn")
    stateMachineVersionArn = field("stateMachineVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutionStartedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionStartedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionSucceededEventDetails:
    boto3_raw_data: "type_defs.ExecutionSucceededEventDetailsTypeDef" = (
        dataclasses.field()
    )

    output = field("output")

    @cached_property
    def outputDetails(self):  # pragma: no cover
        return HistoryEventExecutionDataDetails.make_one(
            self.boto3_raw_data["outputDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExecutionSucceededEventDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionSucceededEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionSucceededEventDetails:
    boto3_raw_data: "type_defs.LambdaFunctionSucceededEventDetailsTypeDef" = (
        dataclasses.field()
    )

    output = field("output")

    @cached_property
    def outputDetails(self):  # pragma: no cover
        return HistoryEventExecutionDataDetails.make_one(
            self.boto3_raw_data["outputDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionSucceededEventDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionSucceededEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateEnteredEventDetails:
    boto3_raw_data: "type_defs.StateEnteredEventDetailsTypeDef" = dataclasses.field()

    name = field("name")
    input = field("input")

    @cached_property
    def inputDetails(self):  # pragma: no cover
        return HistoryEventExecutionDataDetails.make_one(
            self.boto3_raw_data["inputDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StateEnteredEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateEnteredEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskSubmittedEventDetails:
    boto3_raw_data: "type_defs.TaskSubmittedEventDetailsTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resource = field("resource")
    output = field("output")

    @cached_property
    def outputDetails(self):  # pragma: no cover
        return HistoryEventExecutionDataDetails.make_one(
            self.boto3_raw_data["outputDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskSubmittedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskSubmittedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskSucceededEventDetails:
    boto3_raw_data: "type_defs.TaskSucceededEventDetailsTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resource = field("resource")
    output = field("output")

    @cached_property
    def outputDetails(self):  # pragma: no cover
        return HistoryEventExecutionDataDetails.make_one(
            self.boto3_raw_data["outputDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskSucceededEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskSucceededEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateExitedEventDetails:
    boto3_raw_data: "type_defs.StateExitedEventDetailsTypeDef" = dataclasses.field()

    name = field("name")
    output = field("output")

    @cached_property
    def outputDetails(self):  # pragma: no cover
        return HistoryEventExecutionDataDetails.make_one(
            self.boto3_raw_data["outputDetails"]
        )

    assignedVariables = field("assignedVariables")

    @cached_property
    def assignedVariablesDetails(self):  # pragma: no cover
        return AssignedVariablesDetails.make_one(
            self.boto3_raw_data["assignedVariablesDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StateExitedEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateExitedEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogDestination:
    boto3_raw_data: "type_defs.LogDestinationTypeDef" = dataclasses.field()

    @cached_property
    def cloudWatchLogsLogGroup(self):  # pragma: no cover
        return CloudWatchLogsLogGroup.make_one(
            self.boto3_raw_data["cloudWatchLogsLogGroup"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogDestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateActivityInput:
    boto3_raw_data: "type_defs.CreateActivityInputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateActivityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateActivityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateActivityOutput:
    boto3_raw_data: "type_defs.CreateActivityOutputTypeDef" = dataclasses.field()

    activityArn = field("activityArn")
    creationDate = field("creationDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateActivityOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateActivityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStateMachineAliasOutput:
    boto3_raw_data: "type_defs.CreateStateMachineAliasOutputTypeDef" = (
        dataclasses.field()
    )

    stateMachineAliasArn = field("stateMachineAliasArn")
    creationDate = field("creationDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateStateMachineAliasOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStateMachineAliasOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStateMachineOutput:
    boto3_raw_data: "type_defs.CreateStateMachineOutputTypeDef" = dataclasses.field()

    stateMachineArn = field("stateMachineArn")
    creationDate = field("creationDate")
    stateMachineVersionArn = field("stateMachineVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStateMachineOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStateMachineOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActivityOutput:
    boto3_raw_data: "type_defs.DescribeActivityOutputTypeDef" = dataclasses.field()

    activityArn = field("activityArn")
    name = field("name")
    creationDate = field("creationDate")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeActivityOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActivityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExecutionOutput:
    boto3_raw_data: "type_defs.DescribeExecutionOutputTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    stateMachineArn = field("stateMachineArn")
    name = field("name")
    status = field("status")
    startDate = field("startDate")
    input = field("input")

    @cached_property
    def inputDetails(self):  # pragma: no cover
        return CloudWatchEventsExecutionDataDetails.make_one(
            self.boto3_raw_data["inputDetails"]
        )

    redriveCount = field("redriveCount")
    redriveStatus = field("redriveStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    stopDate = field("stopDate")
    output = field("output")

    @cached_property
    def outputDetails(self):  # pragma: no cover
        return CloudWatchEventsExecutionDataDetails.make_one(
            self.boto3_raw_data["outputDetails"]
        )

    traceHeader = field("traceHeader")
    mapRunArn = field("mapRunArn")
    error = field("error")
    cause = field("cause")
    stateMachineVersionArn = field("stateMachineVersionArn")
    stateMachineAliasArn = field("stateMachineAliasArn")
    redriveDate = field("redriveDate")
    redriveStatusReason = field("redriveStatusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetActivityTaskOutput:
    boto3_raw_data: "type_defs.GetActivityTaskOutputTypeDef" = dataclasses.field()

    taskToken = field("taskToken")
    input = field("input")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetActivityTaskOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActivityTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActivitiesOutput:
    boto3_raw_data: "type_defs.ListActivitiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def activities(self):  # pragma: no cover
        return ActivityListItem.make_many(self.boto3_raw_data["activities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActivitiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActivitiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishStateMachineVersionOutput:
    boto3_raw_data: "type_defs.PublishStateMachineVersionOutputTypeDef" = (
        dataclasses.field()
    )

    creationDate = field("creationDate")
    stateMachineVersionArn = field("stateMachineVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PublishStateMachineVersionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishStateMachineVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedriveExecutionOutput:
    boto3_raw_data: "type_defs.RedriveExecutionOutputTypeDef" = dataclasses.field()

    redriveDate = field("redriveDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedriveExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedriveExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExecutionOutput:
    boto3_raw_data: "type_defs.StartExecutionOutputTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    startDate = field("startDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSyncExecutionOutput:
    boto3_raw_data: "type_defs.StartSyncExecutionOutputTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    stateMachineArn = field("stateMachineArn")
    name = field("name")
    startDate = field("startDate")
    stopDate = field("stopDate")
    status = field("status")
    error = field("error")
    cause = field("cause")
    input = field("input")

    @cached_property
    def inputDetails(self):  # pragma: no cover
        return CloudWatchEventsExecutionDataDetails.make_one(
            self.boto3_raw_data["inputDetails"]
        )

    output = field("output")

    @cached_property
    def outputDetails(self):  # pragma: no cover
        return CloudWatchEventsExecutionDataDetails.make_one(
            self.boto3_raw_data["outputDetails"]
        )

    traceHeader = field("traceHeader")

    @cached_property
    def billingDetails(self):  # pragma: no cover
        return BillingDetails.make_one(self.boto3_raw_data["billingDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSyncExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSyncExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopExecutionOutput:
    boto3_raw_data: "type_defs.StopExecutionOutputTypeDef" = dataclasses.field()

    stopDate = field("stopDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStateMachineAliasOutput:
    boto3_raw_data: "type_defs.UpdateStateMachineAliasOutputTypeDef" = (
        dataclasses.field()
    )

    updateDate = field("updateDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateStateMachineAliasOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStateMachineAliasOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStateMachineOutput:
    boto3_raw_data: "type_defs.UpdateStateMachineOutputTypeDef" = dataclasses.field()

    updateDate = field("updateDate")
    revisionId = field("revisionId")
    stateMachineVersionArn = field("stateMachineVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStateMachineOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStateMachineOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStateMachineAliasInput:
    boto3_raw_data: "type_defs.CreateStateMachineAliasInputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return RoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStateMachineAliasInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStateMachineAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStateMachineAliasOutput:
    boto3_raw_data: "type_defs.DescribeStateMachineAliasOutputTypeDef" = (
        dataclasses.field()
    )

    stateMachineAliasArn = field("stateMachineAliasArn")
    name = field("name")
    description = field("description")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return RoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    creationDate = field("creationDate")
    updateDate = field("updateDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStateMachineAliasOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStateMachineAliasOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStateMachineAliasInput:
    boto3_raw_data: "type_defs.UpdateStateMachineAliasInputTypeDef" = (
        dataclasses.field()
    )

    stateMachineAliasArn = field("stateMachineAliasArn")
    description = field("description")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return RoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStateMachineAliasInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStateMachineAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMapRunOutput:
    boto3_raw_data: "type_defs.DescribeMapRunOutputTypeDef" = dataclasses.field()

    mapRunArn = field("mapRunArn")
    executionArn = field("executionArn")
    status = field("status")
    startDate = field("startDate")
    stopDate = field("stopDate")
    maxConcurrency = field("maxConcurrency")
    toleratedFailurePercentage = field("toleratedFailurePercentage")
    toleratedFailureCount = field("toleratedFailureCount")

    @cached_property
    def itemCounts(self):  # pragma: no cover
        return MapRunItemCounts.make_one(self.boto3_raw_data["itemCounts"])

    @cached_property
    def executionCounts(self):  # pragma: no cover
        return MapRunExecutionCounts.make_one(self.boto3_raw_data["executionCounts"])

    redriveCount = field("redriveCount")
    redriveDate = field("redriveDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMapRunOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMapRunOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExecutionsOutput:
    boto3_raw_data: "type_defs.ListExecutionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def executions(self):  # pragma: no cover
        return ExecutionListItem.make_many(self.boto3_raw_data["executions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExecutionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExecutionHistoryInputPaginate:
    boto3_raw_data: "type_defs.GetExecutionHistoryInputPaginateTypeDef" = (
        dataclasses.field()
    )

    executionArn = field("executionArn")
    reverseOrder = field("reverseOrder")
    includeExecutionData = field("includeExecutionData")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetExecutionHistoryInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExecutionHistoryInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActivitiesInputPaginate:
    boto3_raw_data: "type_defs.ListActivitiesInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActivitiesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActivitiesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExecutionsInputPaginate:
    boto3_raw_data: "type_defs.ListExecutionsInputPaginateTypeDef" = dataclasses.field()

    stateMachineArn = field("stateMachineArn")
    statusFilter = field("statusFilter")
    mapRunArn = field("mapRunArn")
    redriveFilter = field("redriveFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExecutionsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMapRunsInputPaginate:
    boto3_raw_data: "type_defs.ListMapRunsInputPaginateTypeDef" = dataclasses.field()

    executionArn = field("executionArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMapRunsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMapRunsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStateMachinesInputPaginate:
    boto3_raw_data: "type_defs.ListStateMachinesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStateMachinesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStateMachinesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InspectionData:
    boto3_raw_data: "type_defs.InspectionDataTypeDef" = dataclasses.field()

    input = field("input")
    afterArguments = field("afterArguments")
    afterInputPath = field("afterInputPath")
    afterParameters = field("afterParameters")
    result = field("result")
    afterResultSelector = field("afterResultSelector")
    afterResultPath = field("afterResultPath")

    @cached_property
    def request(self):  # pragma: no cover
        return InspectionDataRequest.make_one(self.boto3_raw_data["request"])

    @cached_property
    def response(self):  # pragma: no cover
        return InspectionDataResponse.make_one(self.boto3_raw_data["response"])

    variables = field("variables")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InspectionDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InspectionDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionScheduledEventDetails:
    boto3_raw_data: "type_defs.LambdaFunctionScheduledEventDetailsTypeDef" = (
        dataclasses.field()
    )

    resource = field("resource")
    input = field("input")

    @cached_property
    def inputDetails(self):  # pragma: no cover
        return HistoryEventExecutionDataDetails.make_one(
            self.boto3_raw_data["inputDetails"]
        )

    timeoutInSeconds = field("timeoutInSeconds")

    @cached_property
    def taskCredentials(self):  # pragma: no cover
        return TaskCredentials.make_one(self.boto3_raw_data["taskCredentials"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionScheduledEventDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionScheduledEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskScheduledEventDetails:
    boto3_raw_data: "type_defs.TaskScheduledEventDetailsTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resource = field("resource")
    region = field("region")
    parameters = field("parameters")
    timeoutInSeconds = field("timeoutInSeconds")
    heartbeatInSeconds = field("heartbeatInSeconds")

    @cached_property
    def taskCredentials(self):  # pragma: no cover
        return TaskCredentials.make_one(self.boto3_raw_data["taskCredentials"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskScheduledEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskScheduledEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMapRunsOutput:
    boto3_raw_data: "type_defs.ListMapRunsOutputTypeDef" = dataclasses.field()

    @cached_property
    def mapRuns(self):  # pragma: no cover
        return MapRunListItem.make_many(self.boto3_raw_data["mapRuns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMapRunsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMapRunsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStateMachineAliasesOutput:
    boto3_raw_data: "type_defs.ListStateMachineAliasesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def stateMachineAliases(self):  # pragma: no cover
        return StateMachineAliasListItem.make_many(
            self.boto3_raw_data["stateMachineAliases"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStateMachineAliasesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStateMachineAliasesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStateMachineVersionsOutput:
    boto3_raw_data: "type_defs.ListStateMachineVersionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def stateMachineVersions(self):  # pragma: no cover
        return StateMachineVersionListItem.make_many(
            self.boto3_raw_data["stateMachineVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStateMachineVersionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStateMachineVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStateMachinesOutput:
    boto3_raw_data: "type_defs.ListStateMachinesOutputTypeDef" = dataclasses.field()

    @cached_property
    def stateMachines(self):  # pragma: no cover
        return StateMachineListItem.make_many(self.boto3_raw_data["stateMachines"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStateMachinesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStateMachinesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateStateMachineDefinitionOutput:
    boto3_raw_data: "type_defs.ValidateStateMachineDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    result = field("result")

    @cached_property
    def diagnostics(self):  # pragma: no cover
        return ValidateStateMachineDefinitionDiagnostic.make_many(
            self.boto3_raw_data["diagnostics"]
        )

    truncated = field("truncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateStateMachineDefinitionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateStateMachineDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfigurationOutput:
    boto3_raw_data: "type_defs.LoggingConfigurationOutputTypeDef" = dataclasses.field()

    level = field("level")
    includeExecutionData = field("includeExecutionData")

    @cached_property
    def destinations(self):  # pragma: no cover
        return LogDestination.make_many(self.boto3_raw_data["destinations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfiguration:
    boto3_raw_data: "type_defs.LoggingConfigurationTypeDef" = dataclasses.field()

    level = field("level")
    includeExecutionData = field("includeExecutionData")

    @cached_property
    def destinations(self):  # pragma: no cover
        return LogDestination.make_many(self.boto3_raw_data["destinations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestStateOutput:
    boto3_raw_data: "type_defs.TestStateOutputTypeDef" = dataclasses.field()

    output = field("output")
    error = field("error")
    cause = field("cause")

    @cached_property
    def inspectionData(self):  # pragma: no cover
        return InspectionData.make_one(self.boto3_raw_data["inspectionData"])

    nextState = field("nextState")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestStateOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestStateOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HistoryEvent:
    boto3_raw_data: "type_defs.HistoryEventTypeDef" = dataclasses.field()

    timestamp = field("timestamp")
    type = field("type")
    id = field("id")
    previousEventId = field("previousEventId")

    @cached_property
    def activityFailedEventDetails(self):  # pragma: no cover
        return ActivityFailedEventDetails.make_one(
            self.boto3_raw_data["activityFailedEventDetails"]
        )

    @cached_property
    def activityScheduleFailedEventDetails(self):  # pragma: no cover
        return ActivityScheduleFailedEventDetails.make_one(
            self.boto3_raw_data["activityScheduleFailedEventDetails"]
        )

    @cached_property
    def activityScheduledEventDetails(self):  # pragma: no cover
        return ActivityScheduledEventDetails.make_one(
            self.boto3_raw_data["activityScheduledEventDetails"]
        )

    @cached_property
    def activityStartedEventDetails(self):  # pragma: no cover
        return ActivityStartedEventDetails.make_one(
            self.boto3_raw_data["activityStartedEventDetails"]
        )

    @cached_property
    def activitySucceededEventDetails(self):  # pragma: no cover
        return ActivitySucceededEventDetails.make_one(
            self.boto3_raw_data["activitySucceededEventDetails"]
        )

    @cached_property
    def activityTimedOutEventDetails(self):  # pragma: no cover
        return ActivityTimedOutEventDetails.make_one(
            self.boto3_raw_data["activityTimedOutEventDetails"]
        )

    @cached_property
    def taskFailedEventDetails(self):  # pragma: no cover
        return TaskFailedEventDetails.make_one(
            self.boto3_raw_data["taskFailedEventDetails"]
        )

    @cached_property
    def taskScheduledEventDetails(self):  # pragma: no cover
        return TaskScheduledEventDetails.make_one(
            self.boto3_raw_data["taskScheduledEventDetails"]
        )

    @cached_property
    def taskStartFailedEventDetails(self):  # pragma: no cover
        return TaskStartFailedEventDetails.make_one(
            self.boto3_raw_data["taskStartFailedEventDetails"]
        )

    @cached_property
    def taskStartedEventDetails(self):  # pragma: no cover
        return TaskStartedEventDetails.make_one(
            self.boto3_raw_data["taskStartedEventDetails"]
        )

    @cached_property
    def taskSubmitFailedEventDetails(self):  # pragma: no cover
        return TaskSubmitFailedEventDetails.make_one(
            self.boto3_raw_data["taskSubmitFailedEventDetails"]
        )

    @cached_property
    def taskSubmittedEventDetails(self):  # pragma: no cover
        return TaskSubmittedEventDetails.make_one(
            self.boto3_raw_data["taskSubmittedEventDetails"]
        )

    @cached_property
    def taskSucceededEventDetails(self):  # pragma: no cover
        return TaskSucceededEventDetails.make_one(
            self.boto3_raw_data["taskSucceededEventDetails"]
        )

    @cached_property
    def taskTimedOutEventDetails(self):  # pragma: no cover
        return TaskTimedOutEventDetails.make_one(
            self.boto3_raw_data["taskTimedOutEventDetails"]
        )

    @cached_property
    def executionFailedEventDetails(self):  # pragma: no cover
        return ExecutionFailedEventDetails.make_one(
            self.boto3_raw_data["executionFailedEventDetails"]
        )

    @cached_property
    def executionStartedEventDetails(self):  # pragma: no cover
        return ExecutionStartedEventDetails.make_one(
            self.boto3_raw_data["executionStartedEventDetails"]
        )

    @cached_property
    def executionSucceededEventDetails(self):  # pragma: no cover
        return ExecutionSucceededEventDetails.make_one(
            self.boto3_raw_data["executionSucceededEventDetails"]
        )

    @cached_property
    def executionAbortedEventDetails(self):  # pragma: no cover
        return ExecutionAbortedEventDetails.make_one(
            self.boto3_raw_data["executionAbortedEventDetails"]
        )

    @cached_property
    def executionTimedOutEventDetails(self):  # pragma: no cover
        return ExecutionTimedOutEventDetails.make_one(
            self.boto3_raw_data["executionTimedOutEventDetails"]
        )

    @cached_property
    def executionRedrivenEventDetails(self):  # pragma: no cover
        return ExecutionRedrivenEventDetails.make_one(
            self.boto3_raw_data["executionRedrivenEventDetails"]
        )

    @cached_property
    def mapStateStartedEventDetails(self):  # pragma: no cover
        return MapStateStartedEventDetails.make_one(
            self.boto3_raw_data["mapStateStartedEventDetails"]
        )

    @cached_property
    def mapIterationStartedEventDetails(self):  # pragma: no cover
        return MapIterationEventDetails.make_one(
            self.boto3_raw_data["mapIterationStartedEventDetails"]
        )

    @cached_property
    def mapIterationSucceededEventDetails(self):  # pragma: no cover
        return MapIterationEventDetails.make_one(
            self.boto3_raw_data["mapIterationSucceededEventDetails"]
        )

    @cached_property
    def mapIterationFailedEventDetails(self):  # pragma: no cover
        return MapIterationEventDetails.make_one(
            self.boto3_raw_data["mapIterationFailedEventDetails"]
        )

    @cached_property
    def mapIterationAbortedEventDetails(self):  # pragma: no cover
        return MapIterationEventDetails.make_one(
            self.boto3_raw_data["mapIterationAbortedEventDetails"]
        )

    @cached_property
    def lambdaFunctionFailedEventDetails(self):  # pragma: no cover
        return LambdaFunctionFailedEventDetails.make_one(
            self.boto3_raw_data["lambdaFunctionFailedEventDetails"]
        )

    @cached_property
    def lambdaFunctionScheduleFailedEventDetails(self):  # pragma: no cover
        return LambdaFunctionScheduleFailedEventDetails.make_one(
            self.boto3_raw_data["lambdaFunctionScheduleFailedEventDetails"]
        )

    @cached_property
    def lambdaFunctionScheduledEventDetails(self):  # pragma: no cover
        return LambdaFunctionScheduledEventDetails.make_one(
            self.boto3_raw_data["lambdaFunctionScheduledEventDetails"]
        )

    @cached_property
    def lambdaFunctionStartFailedEventDetails(self):  # pragma: no cover
        return LambdaFunctionStartFailedEventDetails.make_one(
            self.boto3_raw_data["lambdaFunctionStartFailedEventDetails"]
        )

    @cached_property
    def lambdaFunctionSucceededEventDetails(self):  # pragma: no cover
        return LambdaFunctionSucceededEventDetails.make_one(
            self.boto3_raw_data["lambdaFunctionSucceededEventDetails"]
        )

    @cached_property
    def lambdaFunctionTimedOutEventDetails(self):  # pragma: no cover
        return LambdaFunctionTimedOutEventDetails.make_one(
            self.boto3_raw_data["lambdaFunctionTimedOutEventDetails"]
        )

    @cached_property
    def stateEnteredEventDetails(self):  # pragma: no cover
        return StateEnteredEventDetails.make_one(
            self.boto3_raw_data["stateEnteredEventDetails"]
        )

    @cached_property
    def stateExitedEventDetails(self):  # pragma: no cover
        return StateExitedEventDetails.make_one(
            self.boto3_raw_data["stateExitedEventDetails"]
        )

    @cached_property
    def mapRunStartedEventDetails(self):  # pragma: no cover
        return MapRunStartedEventDetails.make_one(
            self.boto3_raw_data["mapRunStartedEventDetails"]
        )

    @cached_property
    def mapRunFailedEventDetails(self):  # pragma: no cover
        return MapRunFailedEventDetails.make_one(
            self.boto3_raw_data["mapRunFailedEventDetails"]
        )

    @cached_property
    def mapRunRedrivenEventDetails(self):  # pragma: no cover
        return MapRunRedrivenEventDetails.make_one(
            self.boto3_raw_data["mapRunRedrivenEventDetails"]
        )

    @cached_property
    def evaluationFailedEventDetails(self):  # pragma: no cover
        return EvaluationFailedEventDetails.make_one(
            self.boto3_raw_data["evaluationFailedEventDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HistoryEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HistoryEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStateMachineForExecutionOutput:
    boto3_raw_data: "type_defs.DescribeStateMachineForExecutionOutputTypeDef" = (
        dataclasses.field()
    )

    stateMachineArn = field("stateMachineArn")
    name = field("name")
    definition = field("definition")
    roleArn = field("roleArn")
    updateDate = field("updateDate")

    @cached_property
    def loggingConfiguration(self):  # pragma: no cover
        return LoggingConfigurationOutput.make_one(
            self.boto3_raw_data["loggingConfiguration"]
        )

    @cached_property
    def tracingConfiguration(self):  # pragma: no cover
        return TracingConfiguration.make_one(
            self.boto3_raw_data["tracingConfiguration"]
        )

    mapRunArn = field("mapRunArn")
    label = field("label")
    revisionId = field("revisionId")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    variableReferences = field("variableReferences")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStateMachineForExecutionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStateMachineForExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStateMachineOutput:
    boto3_raw_data: "type_defs.DescribeStateMachineOutputTypeDef" = dataclasses.field()

    stateMachineArn = field("stateMachineArn")
    name = field("name")
    status = field("status")
    definition = field("definition")
    roleArn = field("roleArn")
    type = field("type")
    creationDate = field("creationDate")

    @cached_property
    def loggingConfiguration(self):  # pragma: no cover
        return LoggingConfigurationOutput.make_one(
            self.boto3_raw_data["loggingConfiguration"]
        )

    @cached_property
    def tracingConfiguration(self):  # pragma: no cover
        return TracingConfiguration.make_one(
            self.boto3_raw_data["tracingConfiguration"]
        )

    label = field("label")
    revisionId = field("revisionId")
    description = field("description")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    variableReferences = field("variableReferences")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStateMachineOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStateMachineOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExecutionHistoryOutput:
    boto3_raw_data: "type_defs.GetExecutionHistoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return HistoryEvent.make_many(self.boto3_raw_data["events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExecutionHistoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExecutionHistoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStateMachineInput:
    boto3_raw_data: "type_defs.CreateStateMachineInputTypeDef" = dataclasses.field()

    name = field("name")
    definition = field("definition")
    roleArn = field("roleArn")
    type = field("type")
    loggingConfiguration = field("loggingConfiguration")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def tracingConfiguration(self):  # pragma: no cover
        return TracingConfiguration.make_one(
            self.boto3_raw_data["tracingConfiguration"]
        )

    publish = field("publish")
    versionDescription = field("versionDescription")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStateMachineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStateMachineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStateMachineInput:
    boto3_raw_data: "type_defs.UpdateStateMachineInputTypeDef" = dataclasses.field()

    stateMachineArn = field("stateMachineArn")
    definition = field("definition")
    roleArn = field("roleArn")
    loggingConfiguration = field("loggingConfiguration")

    @cached_property
    def tracingConfiguration(self):  # pragma: no cover
        return TracingConfiguration.make_one(
            self.boto3_raw_data["tracingConfiguration"]
        )

    publish = field("publish")
    versionDescription = field("versionDescription")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStateMachineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStateMachineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
