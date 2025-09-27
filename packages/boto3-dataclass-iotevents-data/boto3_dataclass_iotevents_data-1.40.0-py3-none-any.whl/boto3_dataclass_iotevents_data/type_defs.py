# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotevents_data import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcknowledgeActionConfiguration:
    boto3_raw_data: "type_defs.AcknowledgeActionConfigurationTypeDef" = (
        dataclasses.field()
    )

    note = field("note")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcknowledgeActionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcknowledgeActionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcknowledgeAlarmActionRequest:
    boto3_raw_data: "type_defs.AcknowledgeAlarmActionRequestTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    alarmModelName = field("alarmModelName")
    keyValue = field("keyValue")
    note = field("note")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcknowledgeAlarmActionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcknowledgeAlarmActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmSummary:
    boto3_raw_data: "type_defs.AlarmSummaryTypeDef" = dataclasses.field()

    alarmModelName = field("alarmModelName")
    alarmModelVersion = field("alarmModelVersion")
    keyValue = field("keyValue")
    stateName = field("stateName")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAlarmActionErrorEntry:
    boto3_raw_data: "type_defs.BatchAlarmActionErrorEntryTypeDef" = dataclasses.field()

    requestId = field("requestId")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchAlarmActionErrorEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAlarmActionErrorEntryTypeDef"]
        ],
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
class BatchDeleteDetectorErrorEntry:
    boto3_raw_data: "type_defs.BatchDeleteDetectorErrorEntryTypeDef" = (
        dataclasses.field()
    )

    messageId = field("messageId")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeleteDetectorErrorEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDetectorErrorEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDetectorRequest:
    boto3_raw_data: "type_defs.DeleteDetectorRequestTypeDef" = dataclasses.field()

    messageId = field("messageId")
    detectorModelName = field("detectorModelName")
    keyValue = field("keyValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableAlarmActionRequest:
    boto3_raw_data: "type_defs.DisableAlarmActionRequestTypeDef" = dataclasses.field()

    requestId = field("requestId")
    alarmModelName = field("alarmModelName")
    keyValue = field("keyValue")
    note = field("note")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableAlarmActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableAlarmActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableAlarmActionRequest:
    boto3_raw_data: "type_defs.EnableAlarmActionRequestTypeDef" = dataclasses.field()

    requestId = field("requestId")
    alarmModelName = field("alarmModelName")
    keyValue = field("keyValue")
    note = field("note")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableAlarmActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableAlarmActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutMessageErrorEntry:
    boto3_raw_data: "type_defs.BatchPutMessageErrorEntryTypeDef" = dataclasses.field()

    messageId = field("messageId")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutMessageErrorEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutMessageErrorEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetAlarmActionRequest:
    boto3_raw_data: "type_defs.ResetAlarmActionRequestTypeDef" = dataclasses.field()

    requestId = field("requestId")
    alarmModelName = field("alarmModelName")
    keyValue = field("keyValue")
    note = field("note")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetAlarmActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetAlarmActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnoozeAlarmActionRequest:
    boto3_raw_data: "type_defs.SnoozeAlarmActionRequestTypeDef" = dataclasses.field()

    requestId = field("requestId")
    alarmModelName = field("alarmModelName")
    snoozeDuration = field("snoozeDuration")
    keyValue = field("keyValue")
    note = field("note")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnoozeAlarmActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnoozeAlarmActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateDetectorErrorEntry:
    boto3_raw_data: "type_defs.BatchUpdateDetectorErrorEntryTypeDef" = (
        dataclasses.field()
    )

    messageId = field("messageId")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchUpdateDetectorErrorEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateDetectorErrorEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableActionConfiguration:
    boto3_raw_data: "type_defs.DisableActionConfigurationTypeDef" = dataclasses.field()

    note = field("note")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableActionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableActionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableActionConfiguration:
    boto3_raw_data: "type_defs.EnableActionConfigurationTypeDef" = dataclasses.field()

    note = field("note")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableActionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableActionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetActionConfiguration:
    boto3_raw_data: "type_defs.ResetActionConfigurationTypeDef" = dataclasses.field()

    note = field("note")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetActionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetActionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnoozeActionConfiguration:
    boto3_raw_data: "type_defs.SnoozeActionConfigurationTypeDef" = dataclasses.field()

    snoozeDuration = field("snoozeDuration")
    note = field("note")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnoozeActionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnoozeActionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmRequest:
    boto3_raw_data: "type_defs.DescribeAlarmRequestTypeDef" = dataclasses.field()

    alarmModelName = field("alarmModelName")
    keyValue = field("keyValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDetectorRequest:
    boto3_raw_data: "type_defs.DescribeDetectorRequestTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")
    keyValue = field("keyValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimerDefinition:
    boto3_raw_data: "type_defs.TimerDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    seconds = field("seconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimerDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimerDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariableDefinition:
    boto3_raw_data: "type_defs.VariableDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VariableDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VariableDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorStateSummary:
    boto3_raw_data: "type_defs.DetectorStateSummaryTypeDef" = dataclasses.field()

    stateName = field("stateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectorStateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorStateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Timer:
    boto3_raw_data: "type_defs.TimerTypeDef" = dataclasses.field()

    name = field("name")
    timestamp = field("timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Variable:
    boto3_raw_data: "type_defs.VariableTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VariableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VariableTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlarmsRequest:
    boto3_raw_data: "type_defs.ListAlarmsRequestTypeDef" = dataclasses.field()

    alarmModelName = field("alarmModelName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAlarmsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlarmsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectorsRequest:
    boto3_raw_data: "type_defs.ListDetectorsRequestTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")
    stateName = field("stateName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDetectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestampValue:
    boto3_raw_data: "type_defs.TimestampValueTypeDef" = dataclasses.field()

    timeInMillis = field("timeInMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimestampValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimestampValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleRuleEvaluation:
    boto3_raw_data: "type_defs.SimpleRuleEvaluationTypeDef" = dataclasses.field()

    inputPropertyValue = field("inputPropertyValue")
    operator = field("operator")
    thresholdValue = field("thresholdValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimpleRuleEvaluationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimpleRuleEvaluationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateChangeConfiguration:
    boto3_raw_data: "type_defs.StateChangeConfigurationTypeDef" = dataclasses.field()

    triggerType = field("triggerType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StateChangeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateChangeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAcknowledgeAlarmRequest:
    boto3_raw_data: "type_defs.BatchAcknowledgeAlarmRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def acknowledgeActionRequests(self):  # pragma: no cover
        return AcknowledgeAlarmActionRequest.make_many(
            self.boto3_raw_data["acknowledgeActionRequests"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchAcknowledgeAlarmRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAcknowledgeAlarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAcknowledgeAlarmResponse:
    boto3_raw_data: "type_defs.BatchAcknowledgeAlarmResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return BatchAlarmActionErrorEntry.make_many(self.boto3_raw_data["errorEntries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchAcknowledgeAlarmResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAcknowledgeAlarmResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisableAlarmResponse:
    boto3_raw_data: "type_defs.BatchDisableAlarmResponseTypeDef" = dataclasses.field()

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return BatchAlarmActionErrorEntry.make_many(self.boto3_raw_data["errorEntries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDisableAlarmResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisableAlarmResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchEnableAlarmResponse:
    boto3_raw_data: "type_defs.BatchEnableAlarmResponseTypeDef" = dataclasses.field()

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return BatchAlarmActionErrorEntry.make_many(self.boto3_raw_data["errorEntries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchEnableAlarmResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchEnableAlarmResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchResetAlarmResponse:
    boto3_raw_data: "type_defs.BatchResetAlarmResponseTypeDef" = dataclasses.field()

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return BatchAlarmActionErrorEntry.make_many(self.boto3_raw_data["errorEntries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchResetAlarmResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchResetAlarmResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchSnoozeAlarmResponse:
    boto3_raw_data: "type_defs.BatchSnoozeAlarmResponseTypeDef" = dataclasses.field()

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return BatchAlarmActionErrorEntry.make_many(self.boto3_raw_data["errorEntries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchSnoozeAlarmResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchSnoozeAlarmResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlarmsResponse:
    boto3_raw_data: "type_defs.ListAlarmsResponseTypeDef" = dataclasses.field()

    @cached_property
    def alarmSummaries(self):  # pragma: no cover
        return AlarmSummary.make_many(self.boto3_raw_data["alarmSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAlarmsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlarmsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDetectorResponse:
    boto3_raw_data: "type_defs.BatchDeleteDetectorResponseTypeDef" = dataclasses.field()

    @cached_property
    def batchDeleteDetectorErrorEntries(self):  # pragma: no cover
        return BatchDeleteDetectorErrorEntry.make_many(
            self.boto3_raw_data["batchDeleteDetectorErrorEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteDetectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDetectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDetectorRequest:
    boto3_raw_data: "type_defs.BatchDeleteDetectorRequestTypeDef" = dataclasses.field()

    @cached_property
    def detectors(self):  # pragma: no cover
        return DeleteDetectorRequest.make_many(self.boto3_raw_data["detectors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisableAlarmRequest:
    boto3_raw_data: "type_defs.BatchDisableAlarmRequestTypeDef" = dataclasses.field()

    @cached_property
    def disableActionRequests(self):  # pragma: no cover
        return DisableAlarmActionRequest.make_many(
            self.boto3_raw_data["disableActionRequests"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDisableAlarmRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisableAlarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchEnableAlarmRequest:
    boto3_raw_data: "type_defs.BatchEnableAlarmRequestTypeDef" = dataclasses.field()

    @cached_property
    def enableActionRequests(self):  # pragma: no cover
        return EnableAlarmActionRequest.make_many(
            self.boto3_raw_data["enableActionRequests"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchEnableAlarmRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchEnableAlarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutMessageResponse:
    boto3_raw_data: "type_defs.BatchPutMessageResponseTypeDef" = dataclasses.field()

    @cached_property
    def BatchPutMessageErrorEntries(self):  # pragma: no cover
        return BatchPutMessageErrorEntry.make_many(
            self.boto3_raw_data["BatchPutMessageErrorEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchResetAlarmRequest:
    boto3_raw_data: "type_defs.BatchResetAlarmRequestTypeDef" = dataclasses.field()

    @cached_property
    def resetActionRequests(self):  # pragma: no cover
        return ResetAlarmActionRequest.make_many(
            self.boto3_raw_data["resetActionRequests"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchResetAlarmRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchResetAlarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchSnoozeAlarmRequest:
    boto3_raw_data: "type_defs.BatchSnoozeAlarmRequestTypeDef" = dataclasses.field()

    @cached_property
    def snoozeActionRequests(self):  # pragma: no cover
        return SnoozeAlarmActionRequest.make_many(
            self.boto3_raw_data["snoozeActionRequests"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchSnoozeAlarmRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchSnoozeAlarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateDetectorResponse:
    boto3_raw_data: "type_defs.BatchUpdateDetectorResponseTypeDef" = dataclasses.field()

    @cached_property
    def batchUpdateDetectorErrorEntries(self):  # pragma: no cover
        return BatchUpdateDetectorErrorEntry.make_many(
            self.boto3_raw_data["batchUpdateDetectorErrorEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateDetectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateDetectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerAction:
    boto3_raw_data: "type_defs.CustomerActionTypeDef" = dataclasses.field()

    actionName = field("actionName")

    @cached_property
    def snoozeActionConfiguration(self):  # pragma: no cover
        return SnoozeActionConfiguration.make_one(
            self.boto3_raw_data["snoozeActionConfiguration"]
        )

    @cached_property
    def enableActionConfiguration(self):  # pragma: no cover
        return EnableActionConfiguration.make_one(
            self.boto3_raw_data["enableActionConfiguration"]
        )

    @cached_property
    def disableActionConfiguration(self):  # pragma: no cover
        return DisableActionConfiguration.make_one(
            self.boto3_raw_data["disableActionConfiguration"]
        )

    @cached_property
    def acknowledgeActionConfiguration(self):  # pragma: no cover
        return AcknowledgeActionConfiguration.make_one(
            self.boto3_raw_data["acknowledgeActionConfiguration"]
        )

    @cached_property
    def resetActionConfiguration(self):  # pragma: no cover
        return ResetActionConfiguration.make_one(
            self.boto3_raw_data["resetActionConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomerActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomerActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorStateDefinition:
    boto3_raw_data: "type_defs.DetectorStateDefinitionTypeDef" = dataclasses.field()

    stateName = field("stateName")

    @cached_property
    def variables(self):  # pragma: no cover
        return VariableDefinition.make_many(self.boto3_raw_data["variables"])

    @cached_property
    def timers(self):  # pragma: no cover
        return TimerDefinition.make_many(self.boto3_raw_data["timers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectorStateDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorStateDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorSummary:
    boto3_raw_data: "type_defs.DetectorSummaryTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")
    keyValue = field("keyValue")
    detectorModelVersion = field("detectorModelVersion")

    @cached_property
    def state(self):  # pragma: no cover
        return DetectorStateSummary.make_one(self.boto3_raw_data["state"])

    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetectorSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorState:
    boto3_raw_data: "type_defs.DetectorStateTypeDef" = dataclasses.field()

    stateName = field("stateName")

    @cached_property
    def variables(self):  # pragma: no cover
        return Variable.make_many(self.boto3_raw_data["variables"])

    @cached_property
    def timers(self):  # pragma: no cover
        return Timer.make_many(self.boto3_raw_data["timers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectorStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetectorStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Message:
    boto3_raw_data: "type_defs.MessageTypeDef" = dataclasses.field()

    messageId = field("messageId")
    inputName = field("inputName")
    payload = field("payload")

    @cached_property
    def timestamp(self):  # pragma: no cover
        return TimestampValue.make_one(self.boto3_raw_data["timestamp"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleEvaluation:
    boto3_raw_data: "type_defs.RuleEvaluationTypeDef" = dataclasses.field()

    @cached_property
    def simpleRuleEvaluation(self):  # pragma: no cover
        return SimpleRuleEvaluation.make_one(
            self.boto3_raw_data["simpleRuleEvaluation"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleEvaluationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleEvaluationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SystemEvent:
    boto3_raw_data: "type_defs.SystemEventTypeDef" = dataclasses.field()

    eventType = field("eventType")

    @cached_property
    def stateChangeConfiguration(self):  # pragma: no cover
        return StateChangeConfiguration.make_one(
            self.boto3_raw_data["stateChangeConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SystemEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SystemEventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDetectorRequest:
    boto3_raw_data: "type_defs.UpdateDetectorRequestTypeDef" = dataclasses.field()

    messageId = field("messageId")
    detectorModelName = field("detectorModelName")

    @cached_property
    def state(self):  # pragma: no cover
        return DetectorStateDefinition.make_one(self.boto3_raw_data["state"])

    keyValue = field("keyValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectorsResponse:
    boto3_raw_data: "type_defs.ListDetectorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def detectorSummaries(self):  # pragma: no cover
        return DetectorSummary.make_many(self.boto3_raw_data["detectorSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDetectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Detector:
    boto3_raw_data: "type_defs.DetectorTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")
    keyValue = field("keyValue")
    detectorModelVersion = field("detectorModelVersion")

    @cached_property
    def state(self):  # pragma: no cover
        return DetectorState.make_one(self.boto3_raw_data["state"])

    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetectorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutMessageRequest:
    boto3_raw_data: "type_defs.BatchPutMessageRequestTypeDef" = dataclasses.field()

    @cached_property
    def messages(self):  # pragma: no cover
        return Message.make_many(self.boto3_raw_data["messages"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmState:
    boto3_raw_data: "type_defs.AlarmStateTypeDef" = dataclasses.field()

    stateName = field("stateName")

    @cached_property
    def ruleEvaluation(self):  # pragma: no cover
        return RuleEvaluation.make_one(self.boto3_raw_data["ruleEvaluation"])

    @cached_property
    def customerAction(self):  # pragma: no cover
        return CustomerAction.make_one(self.boto3_raw_data["customerAction"])

    @cached_property
    def systemEvent(self):  # pragma: no cover
        return SystemEvent.make_one(self.boto3_raw_data["systemEvent"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmStateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateDetectorRequest:
    boto3_raw_data: "type_defs.BatchUpdateDetectorRequestTypeDef" = dataclasses.field()

    @cached_property
    def detectors(self):  # pragma: no cover
        return UpdateDetectorRequest.make_many(self.boto3_raw_data["detectors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDetectorResponse:
    boto3_raw_data: "type_defs.DescribeDetectorResponseTypeDef" = dataclasses.field()

    @cached_property
    def detector(self):  # pragma: no cover
        return Detector.make_one(self.boto3_raw_data["detector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDetectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDetectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Alarm:
    boto3_raw_data: "type_defs.AlarmTypeDef" = dataclasses.field()

    alarmModelName = field("alarmModelName")
    alarmModelVersion = field("alarmModelVersion")
    keyValue = field("keyValue")

    @cached_property
    def alarmState(self):  # pragma: no cover
        return AlarmState.make_one(self.boto3_raw_data["alarmState"])

    severity = field("severity")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmResponse:
    boto3_raw_data: "type_defs.DescribeAlarmResponseTypeDef" = dataclasses.field()

    @cached_property
    def alarm(self):  # pragma: no cover
        return Alarm.make_one(self.boto3_raw_data["alarm"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
