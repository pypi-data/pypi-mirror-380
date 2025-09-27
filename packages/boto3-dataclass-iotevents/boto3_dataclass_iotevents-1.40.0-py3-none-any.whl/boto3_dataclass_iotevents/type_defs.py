# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotevents import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcknowledgeFlow:
    boto3_raw_data: "type_defs.AcknowledgeFlowTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AcknowledgeFlowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AcknowledgeFlowTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClearTimerAction:
    boto3_raw_data: "type_defs.ClearTimerActionTypeDef" = dataclasses.field()

    timerName = field("timerName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClearTimerActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClearTimerActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetTimerAction:
    boto3_raw_data: "type_defs.ResetTimerActionTypeDef" = dataclasses.field()

    timerName = field("timerName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResetTimerActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetTimerActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTimerAction:
    boto3_raw_data: "type_defs.SetTimerActionTypeDef" = dataclasses.field()

    timerName = field("timerName")
    seconds = field("seconds")
    durationExpression = field("durationExpression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SetTimerActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SetTimerActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetVariableAction:
    boto3_raw_data: "type_defs.SetVariableActionTypeDef" = dataclasses.field()

    variableName = field("variableName")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SetVariableActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetVariableActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitializationConfiguration:
    boto3_raw_data: "type_defs.InitializationConfigurationTypeDef" = dataclasses.field()

    disabledOnInitialization = field("disabledOnInitialization")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitializationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitializationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmModelSummary:
    boto3_raw_data: "type_defs.AlarmModelSummaryTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    alarmModelDescription = field("alarmModelDescription")
    alarmModelName = field("alarmModelName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmModelSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmModelVersionSummary:
    boto3_raw_data: "type_defs.AlarmModelVersionSummaryTypeDef" = dataclasses.field()

    alarmModelName = field("alarmModelName")
    alarmModelArn = field("alarmModelArn")
    alarmModelVersion = field("alarmModelVersion")
    roleArn = field("roleArn")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    status = field("status")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlarmModelVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmModelVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleRule:
    boto3_raw_data: "type_defs.SimpleRuleTypeDef" = dataclasses.field()

    inputProperty = field("inputProperty")
    comparisonOperator = field("comparisonOperator")
    threshold = field("threshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SimpleRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SimpleRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisResultLocation:
    boto3_raw_data: "type_defs.AnalysisResultLocationTypeDef" = dataclasses.field()

    path = field("path")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisResultLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisResultLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertyTimestamp:
    boto3_raw_data: "type_defs.AssetPropertyTimestampTypeDef" = dataclasses.field()

    timeInSeconds = field("timeInSeconds")
    offsetInNanos = field("offsetInNanos")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetPropertyTimestampTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertyTimestampTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertyVariant:
    boto3_raw_data: "type_defs.AssetPropertyVariantTypeDef" = dataclasses.field()

    stringValue = field("stringValue")
    integerValue = field("integerValue")
    doubleValue = field("doubleValue")
    booleanValue = field("booleanValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetPropertyVariantTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertyVariantTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attribute:
    boto3_raw_data: "type_defs.AttributeTypeDef" = dataclasses.field()

    jsonPath = field("jsonPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeTypeDef"]]
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
class DetectorModelConfiguration:
    boto3_raw_data: "type_defs.DetectorModelConfigurationTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")
    detectorModelVersion = field("detectorModelVersion")
    detectorModelDescription = field("detectorModelDescription")
    detectorModelArn = field("detectorModelArn")
    roleArn = field("roleArn")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    status = field("status")
    key = field("key")
    evaluationMethod = field("evaluationMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectorModelConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorModelConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputConfiguration:
    boto3_raw_data: "type_defs.InputConfigurationTypeDef" = dataclasses.field()

    inputName = field("inputName")
    inputArn = field("inputArn")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    status = field("status")
    inputDescription = field("inputDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAlarmModelRequest:
    boto3_raw_data: "type_defs.DeleteAlarmModelRequestTypeDef" = dataclasses.field()

    alarmModelName = field("alarmModelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAlarmModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAlarmModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDetectorModelRequest:
    boto3_raw_data: "type_defs.DeleteDetectorModelRequestTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDetectorModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDetectorModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInputRequest:
    boto3_raw_data: "type_defs.DeleteInputRequestTypeDef" = dataclasses.field()

    inputName = field("inputName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmModelRequest:
    boto3_raw_data: "type_defs.DescribeAlarmModelRequestTypeDef" = dataclasses.field()

    alarmModelName = field("alarmModelName")
    alarmModelVersion = field("alarmModelVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDetectorModelAnalysisRequest:
    boto3_raw_data: "type_defs.DescribeDetectorModelAnalysisRequestTypeDef" = (
        dataclasses.field()
    )

    analysisId = field("analysisId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDetectorModelAnalysisRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDetectorModelAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDetectorModelRequest:
    boto3_raw_data: "type_defs.DescribeDetectorModelRequestTypeDef" = (
        dataclasses.field()
    )

    detectorModelName = field("detectorModelName")
    detectorModelVersion = field("detectorModelVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDetectorModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDetectorModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputRequest:
    boto3_raw_data: "type_defs.DescribeInputRequestTypeDef" = dataclasses.field()

    inputName = field("inputName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorDebugOption:
    boto3_raw_data: "type_defs.DetectorDebugOptionTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")
    keyValue = field("keyValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectorDebugOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorDebugOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorModelSummary:
    boto3_raw_data: "type_defs.DetectorModelSummaryTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")
    detectorModelDescription = field("detectorModelDescription")
    creationTime = field("creationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectorModelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorModelVersionSummary:
    boto3_raw_data: "type_defs.DetectorModelVersionSummaryTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")
    detectorModelVersion = field("detectorModelVersion")
    detectorModelArn = field("detectorModelArn")
    roleArn = field("roleArn")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    status = field("status")
    evaluationMethod = field("evaluationMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectorModelVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorModelVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Payload:
    boto3_raw_data: "type_defs.PayloadTypeDef" = dataclasses.field()

    contentExpression = field("contentExpression")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PayloadTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailContent:
    boto3_raw_data: "type_defs.EmailContentTypeDef" = dataclasses.field()

    subject = field("subject")
    additionalMessage = field("additionalMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDetectorModelAnalysisResultsRequest:
    boto3_raw_data: "type_defs.GetDetectorModelAnalysisResultsRequestTypeDef" = (
        dataclasses.field()
    )

    analysisId = field("analysisId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDetectorModelAnalysisResultsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDetectorModelAnalysisResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotEventsInputIdentifier:
    boto3_raw_data: "type_defs.IotEventsInputIdentifierTypeDef" = dataclasses.field()

    inputName = field("inputName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IotEventsInputIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotEventsInputIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSummary:
    boto3_raw_data: "type_defs.InputSummaryTypeDef" = dataclasses.field()

    inputName = field("inputName")
    inputDescription = field("inputDescription")
    inputArn = field("inputArn")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotSiteWiseAssetModelPropertyIdentifier:
    boto3_raw_data: "type_defs.IotSiteWiseAssetModelPropertyIdentifierTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    propertyId = field("propertyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IotSiteWiseAssetModelPropertyIdentifierTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotSiteWiseAssetModelPropertyIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlarmModelVersionsRequest:
    boto3_raw_data: "type_defs.ListAlarmModelVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    alarmModelName = field("alarmModelName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAlarmModelVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlarmModelVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlarmModelsRequest:
    boto3_raw_data: "type_defs.ListAlarmModelsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAlarmModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlarmModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectorModelVersionsRequest:
    boto3_raw_data: "type_defs.ListDetectorModelVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    detectorModelName = field("detectorModelName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDetectorModelVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectorModelVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectorModelsRequest:
    boto3_raw_data: "type_defs.ListDetectorModelsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDetectorModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectorModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutedResource:
    boto3_raw_data: "type_defs.RoutedResourceTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoutedResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoutedResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputsRequest:
    boto3_raw_data: "type_defs.ListInputsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListInputsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSOIdentity:
    boto3_raw_data: "type_defs.SSOIdentityTypeDef" = dataclasses.field()

    identityStoreId = field("identityStoreId")
    userId = field("userId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSOIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SSOIdentityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmCapabilities:
    boto3_raw_data: "type_defs.AlarmCapabilitiesTypeDef" = dataclasses.field()

    @cached_property
    def initializationConfiguration(self):  # pragma: no cover
        return InitializationConfiguration.make_one(
            self.boto3_raw_data["initializationConfiguration"]
        )

    @cached_property
    def acknowledgeFlow(self):  # pragma: no cover
        return AcknowledgeFlow.make_one(self.boto3_raw_data["acknowledgeFlow"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmCapabilitiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmRule:
    boto3_raw_data: "type_defs.AlarmRuleTypeDef" = dataclasses.field()

    @cached_property
    def simpleRule(self):  # pragma: no cover
        return SimpleRule.make_one(self.boto3_raw_data["simpleRule"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisResult:
    boto3_raw_data: "type_defs.AnalysisResultTypeDef" = dataclasses.field()

    type = field("type")
    level = field("level")
    message = field("message")

    @cached_property
    def locations(self):  # pragma: no cover
        return AnalysisResultLocation.make_many(self.boto3_raw_data["locations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertyValue:
    boto3_raw_data: "type_defs.AssetPropertyValueTypeDef" = dataclasses.field()

    @cached_property
    def value(self):  # pragma: no cover
        return AssetPropertyVariant.make_one(self.boto3_raw_data["value"])

    @cached_property
    def timestamp(self):  # pragma: no cover
        return AssetPropertyTimestamp.make_one(self.boto3_raw_data["timestamp"])

    quality = field("quality")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetPropertyValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertyValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDefinitionOutput:
    boto3_raw_data: "type_defs.InputDefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDefinition:
    boto3_raw_data: "type_defs.InputDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAlarmModelResponse:
    boto3_raw_data: "type_defs.CreateAlarmModelResponseTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    alarmModelArn = field("alarmModelArn")
    alarmModelVersion = field("alarmModelVersion")
    lastUpdateTime = field("lastUpdateTime")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAlarmModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAlarmModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDetectorModelAnalysisResponse:
    boto3_raw_data: "type_defs.DescribeDetectorModelAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDetectorModelAnalysisResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDetectorModelAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlarmModelVersionsResponse:
    boto3_raw_data: "type_defs.ListAlarmModelVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def alarmModelVersionSummaries(self):  # pragma: no cover
        return AlarmModelVersionSummary.make_many(
            self.boto3_raw_data["alarmModelVersionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAlarmModelVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlarmModelVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlarmModelsResponse:
    boto3_raw_data: "type_defs.ListAlarmModelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def alarmModelSummaries(self):  # pragma: no cover
        return AlarmModelSummary.make_many(self.boto3_raw_data["alarmModelSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAlarmModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlarmModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDetectorModelAnalysisResponse:
    boto3_raw_data: "type_defs.StartDetectorModelAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    analysisId = field("analysisId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDetectorModelAnalysisResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDetectorModelAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAlarmModelResponse:
    boto3_raw_data: "type_defs.UpdateAlarmModelResponseTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    alarmModelArn = field("alarmModelArn")
    alarmModelVersion = field("alarmModelVersion")
    lastUpdateTime = field("lastUpdateTime")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAlarmModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAlarmModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDetectorModelResponse:
    boto3_raw_data: "type_defs.CreateDetectorModelResponseTypeDef" = dataclasses.field()

    @cached_property
    def detectorModelConfiguration(self):  # pragma: no cover
        return DetectorModelConfiguration.make_one(
            self.boto3_raw_data["detectorModelConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDetectorModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDetectorModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDetectorModelResponse:
    boto3_raw_data: "type_defs.UpdateDetectorModelResponseTypeDef" = dataclasses.field()

    @cached_property
    def detectorModelConfiguration(self):  # pragma: no cover
        return DetectorModelConfiguration.make_one(
            self.boto3_raw_data["detectorModelConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDetectorModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDetectorModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInputResponse:
    boto3_raw_data: "type_defs.CreateInputResponseTypeDef" = dataclasses.field()

    @cached_property
    def inputConfiguration(self):  # pragma: no cover
        return InputConfiguration.make_one(self.boto3_raw_data["inputConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInputResponse:
    boto3_raw_data: "type_defs.UpdateInputResponseTypeDef" = dataclasses.field()

    @cached_property
    def inputConfiguration(self):  # pragma: no cover
        return InputConfiguration.make_one(self.boto3_raw_data["inputConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingOptionsOutput:
    boto3_raw_data: "type_defs.LoggingOptionsOutputTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    level = field("level")
    enabled = field("enabled")

    @cached_property
    def detectorDebugOptions(self):  # pragma: no cover
        return DetectorDebugOption.make_many(
            self.boto3_raw_data["detectorDebugOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingOptions:
    boto3_raw_data: "type_defs.LoggingOptionsTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    level = field("level")
    enabled = field("enabled")

    @cached_property
    def detectorDebugOptions(self):  # pragma: no cover
        return DetectorDebugOption.make_many(
            self.boto3_raw_data["detectorDebugOptions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectorModelsResponse:
    boto3_raw_data: "type_defs.ListDetectorModelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def detectorModelSummaries(self):  # pragma: no cover
        return DetectorModelSummary.make_many(
            self.boto3_raw_data["detectorModelSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDetectorModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectorModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectorModelVersionsResponse:
    boto3_raw_data: "type_defs.ListDetectorModelVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def detectorModelVersionSummaries(self):  # pragma: no cover
        return DetectorModelVersionSummary.make_many(
            self.boto3_raw_data["detectorModelVersionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDetectorModelVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectorModelVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamoDBAction:
    boto3_raw_data: "type_defs.DynamoDBActionTypeDef" = dataclasses.field()

    hashKeyField = field("hashKeyField")
    hashKeyValue = field("hashKeyValue")
    tableName = field("tableName")
    hashKeyType = field("hashKeyType")
    rangeKeyType = field("rangeKeyType")
    rangeKeyField = field("rangeKeyField")
    rangeKeyValue = field("rangeKeyValue")
    operation = field("operation")
    payloadField = field("payloadField")

    @cached_property
    def payload(self):  # pragma: no cover
        return Payload.make_one(self.boto3_raw_data["payload"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DynamoDBActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DynamoDBActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamoDBv2Action:
    boto3_raw_data: "type_defs.DynamoDBv2ActionTypeDef" = dataclasses.field()

    tableName = field("tableName")

    @cached_property
    def payload(self):  # pragma: no cover
        return Payload.make_one(self.boto3_raw_data["payload"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DynamoDBv2ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamoDBv2ActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirehoseAction:
    boto3_raw_data: "type_defs.FirehoseActionTypeDef" = dataclasses.field()

    deliveryStreamName = field("deliveryStreamName")
    separator = field("separator")

    @cached_property
    def payload(self):  # pragma: no cover
        return Payload.make_one(self.boto3_raw_data["payload"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FirehoseActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FirehoseActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotEventsAction:
    boto3_raw_data: "type_defs.IotEventsActionTypeDef" = dataclasses.field()

    inputName = field("inputName")

    @cached_property
    def payload(self):  # pragma: no cover
        return Payload.make_one(self.boto3_raw_data["payload"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IotEventsActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IotEventsActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotTopicPublishAction:
    boto3_raw_data: "type_defs.IotTopicPublishActionTypeDef" = dataclasses.field()

    mqttTopic = field("mqttTopic")

    @cached_property
    def payload(self):  # pragma: no cover
        return Payload.make_one(self.boto3_raw_data["payload"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IotTopicPublishActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotTopicPublishActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaAction:
    boto3_raw_data: "type_defs.LambdaActionTypeDef" = dataclasses.field()

    functionArn = field("functionArn")

    @cached_property
    def payload(self):  # pragma: no cover
        return Payload.make_one(self.boto3_raw_data["payload"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SNSTopicPublishAction:
    boto3_raw_data: "type_defs.SNSTopicPublishActionTypeDef" = dataclasses.field()

    targetArn = field("targetArn")

    @cached_property
    def payload(self):  # pragma: no cover
        return Payload.make_one(self.boto3_raw_data["payload"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SNSTopicPublishActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SNSTopicPublishActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqsAction:
    boto3_raw_data: "type_defs.SqsActionTypeDef" = dataclasses.field()

    queueUrl = field("queueUrl")
    useBase64 = field("useBase64")

    @cached_property
    def payload(self):  # pragma: no cover
        return Payload.make_one(self.boto3_raw_data["payload"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SqsActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SqsActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputsResponse:
    boto3_raw_data: "type_defs.ListInputsResponseTypeDef" = dataclasses.field()

    @cached_property
    def inputSummaries(self):  # pragma: no cover
        return InputSummary.make_many(self.boto3_raw_data["inputSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInputsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotSiteWiseInputIdentifier:
    boto3_raw_data: "type_defs.IotSiteWiseInputIdentifierTypeDef" = dataclasses.field()

    @cached_property
    def iotSiteWiseAssetModelPropertyIdentifier(self):  # pragma: no cover
        return IotSiteWiseAssetModelPropertyIdentifier.make_one(
            self.boto3_raw_data["iotSiteWiseAssetModelPropertyIdentifier"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IotSiteWiseInputIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotSiteWiseInputIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputRoutingsResponse:
    boto3_raw_data: "type_defs.ListInputRoutingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def routedResources(self):  # pragma: no cover
        return RoutedResource.make_many(self.boto3_raw_data["routedResources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInputRoutingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputRoutingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipientDetail:
    boto3_raw_data: "type_defs.RecipientDetailTypeDef" = dataclasses.field()

    @cached_property
    def ssoIdentity(self):  # pragma: no cover
        return SSOIdentity.make_one(self.boto3_raw_data["ssoIdentity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipientDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecipientDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDetectorModelAnalysisResultsResponse:
    boto3_raw_data: "type_defs.GetDetectorModelAnalysisResultsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def analysisResults(self):  # pragma: no cover
        return AnalysisResult.make_many(self.boto3_raw_data["analysisResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDetectorModelAnalysisResultsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDetectorModelAnalysisResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotSiteWiseAction:
    boto3_raw_data: "type_defs.IotSiteWiseActionTypeDef" = dataclasses.field()

    entryId = field("entryId")
    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")

    @cached_property
    def propertyValue(self):  # pragma: no cover
        return AssetPropertyValue.make_one(self.boto3_raw_data["propertyValue"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IotSiteWiseActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotSiteWiseActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Input:
    boto3_raw_data: "type_defs.InputTypeDef" = dataclasses.field()

    @cached_property
    def inputConfiguration(self):  # pragma: no cover
        return InputConfiguration.make_one(self.boto3_raw_data["inputConfiguration"])

    @cached_property
    def inputDefinition(self):  # pragma: no cover
        return InputDefinitionOutput.make_one(self.boto3_raw_data["inputDefinition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoggingOptionsResponse:
    boto3_raw_data: "type_defs.DescribeLoggingOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def loggingOptions(self):  # pragma: no cover
        return LoggingOptionsOutput.make_one(self.boto3_raw_data["loggingOptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLoggingOptionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoggingOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationTargetActions:
    boto3_raw_data: "type_defs.NotificationTargetActionsTypeDef" = dataclasses.field()

    @cached_property
    def lambdaAction(self):  # pragma: no cover
        return LambdaAction.make_one(self.boto3_raw_data["lambdaAction"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationTargetActionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationTargetActionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputIdentifier:
    boto3_raw_data: "type_defs.InputIdentifierTypeDef" = dataclasses.field()

    @cached_property
    def iotEventsInputIdentifier(self):  # pragma: no cover
        return IotEventsInputIdentifier.make_one(
            self.boto3_raw_data["iotEventsInputIdentifier"]
        )

    @cached_property
    def iotSiteWiseInputIdentifier(self):  # pragma: no cover
        return IotSiteWiseInputIdentifier.make_one(
            self.boto3_raw_data["iotSiteWiseInputIdentifier"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputIdentifierTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailRecipientsOutput:
    boto3_raw_data: "type_defs.EmailRecipientsOutputTypeDef" = dataclasses.field()

    @cached_property
    def to(self):  # pragma: no cover
        return RecipientDetail.make_many(self.boto3_raw_data["to"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailRecipientsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailRecipientsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailRecipients:
    boto3_raw_data: "type_defs.EmailRecipientsTypeDef" = dataclasses.field()

    @cached_property
    def to(self):  # pragma: no cover
        return RecipientDetail.make_many(self.boto3_raw_data["to"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailRecipientsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailRecipientsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSConfigurationOutput:
    boto3_raw_data: "type_defs.SMSConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def recipients(self):  # pragma: no cover
        return RecipientDetail.make_many(self.boto3_raw_data["recipients"])

    senderId = field("senderId")
    additionalMessage = field("additionalMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SMSConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMSConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSConfiguration:
    boto3_raw_data: "type_defs.SMSConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def recipients(self):  # pragma: no cover
        return RecipientDetail.make_many(self.boto3_raw_data["recipients"])

    senderId = field("senderId")
    additionalMessage = field("additionalMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SMSConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMSConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Action:
    boto3_raw_data: "type_defs.ActionTypeDef" = dataclasses.field()

    @cached_property
    def setVariable(self):  # pragma: no cover
        return SetVariableAction.make_one(self.boto3_raw_data["setVariable"])

    @cached_property
    def sns(self):  # pragma: no cover
        return SNSTopicPublishAction.make_one(self.boto3_raw_data["sns"])

    @cached_property
    def iotTopicPublish(self):  # pragma: no cover
        return IotTopicPublishAction.make_one(self.boto3_raw_data["iotTopicPublish"])

    @cached_property
    def setTimer(self):  # pragma: no cover
        return SetTimerAction.make_one(self.boto3_raw_data["setTimer"])

    @cached_property
    def clearTimer(self):  # pragma: no cover
        return ClearTimerAction.make_one(self.boto3_raw_data["clearTimer"])

    @cached_property
    def resetTimer(self):  # pragma: no cover
        return ResetTimerAction.make_one(self.boto3_raw_data["resetTimer"])

    @cached_property
    def lambda_(self):  # pragma: no cover
        return LambdaAction.make_one(self.boto3_raw_data["lambda"])

    @cached_property
    def iotEvents(self):  # pragma: no cover
        return IotEventsAction.make_one(self.boto3_raw_data["iotEvents"])

    @cached_property
    def sqs(self):  # pragma: no cover
        return SqsAction.make_one(self.boto3_raw_data["sqs"])

    @cached_property
    def firehose(self):  # pragma: no cover
        return FirehoseAction.make_one(self.boto3_raw_data["firehose"])

    @cached_property
    def dynamoDB(self):  # pragma: no cover
        return DynamoDBAction.make_one(self.boto3_raw_data["dynamoDB"])

    @cached_property
    def dynamoDBv2(self):  # pragma: no cover
        return DynamoDBv2Action.make_one(self.boto3_raw_data["dynamoDBv2"])

    @cached_property
    def iotSiteWise(self):  # pragma: no cover
        return IotSiteWiseAction.make_one(self.boto3_raw_data["iotSiteWise"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmAction:
    boto3_raw_data: "type_defs.AlarmActionTypeDef" = dataclasses.field()

    @cached_property
    def sns(self):  # pragma: no cover
        return SNSTopicPublishAction.make_one(self.boto3_raw_data["sns"])

    @cached_property
    def iotTopicPublish(self):  # pragma: no cover
        return IotTopicPublishAction.make_one(self.boto3_raw_data["iotTopicPublish"])

    @cached_property
    def lambda_(self):  # pragma: no cover
        return LambdaAction.make_one(self.boto3_raw_data["lambda"])

    @cached_property
    def iotEvents(self):  # pragma: no cover
        return IotEventsAction.make_one(self.boto3_raw_data["iotEvents"])

    @cached_property
    def sqs(self):  # pragma: no cover
        return SqsAction.make_one(self.boto3_raw_data["sqs"])

    @cached_property
    def firehose(self):  # pragma: no cover
        return FirehoseAction.make_one(self.boto3_raw_data["firehose"])

    @cached_property
    def dynamoDB(self):  # pragma: no cover
        return DynamoDBAction.make_one(self.boto3_raw_data["dynamoDB"])

    @cached_property
    def dynamoDBv2(self):  # pragma: no cover
        return DynamoDBv2Action.make_one(self.boto3_raw_data["dynamoDBv2"])

    @cached_property
    def iotSiteWise(self):  # pragma: no cover
        return IotSiteWiseAction.make_one(self.boto3_raw_data["iotSiteWise"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputResponse:
    boto3_raw_data: "type_defs.DescribeInputResponseTypeDef" = dataclasses.field()

    @cached_property
    def input(self):  # pragma: no cover
        return Input.make_one(self.boto3_raw_data["input"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInputRequest:
    boto3_raw_data: "type_defs.CreateInputRequestTypeDef" = dataclasses.field()

    inputName = field("inputName")
    inputDefinition = field("inputDefinition")
    inputDescription = field("inputDescription")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInputRequest:
    boto3_raw_data: "type_defs.UpdateInputRequestTypeDef" = dataclasses.field()

    inputName = field("inputName")
    inputDefinition = field("inputDefinition")
    inputDescription = field("inputDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLoggingOptionsRequest:
    boto3_raw_data: "type_defs.PutLoggingOptionsRequestTypeDef" = dataclasses.field()

    loggingOptions = field("loggingOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLoggingOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLoggingOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputRoutingsRequest:
    boto3_raw_data: "type_defs.ListInputRoutingsRequestTypeDef" = dataclasses.field()

    @cached_property
    def inputIdentifier(self):  # pragma: no cover
        return InputIdentifier.make_one(self.boto3_raw_data["inputIdentifier"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInputRoutingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputRoutingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailConfigurationOutput:
    boto3_raw_data: "type_defs.EmailConfigurationOutputTypeDef" = dataclasses.field()

    from_ = field("from")

    @cached_property
    def recipients(self):  # pragma: no cover
        return EmailRecipientsOutput.make_one(self.boto3_raw_data["recipients"])

    @cached_property
    def content(self):  # pragma: no cover
        return EmailContent.make_one(self.boto3_raw_data["content"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailConfiguration:
    boto3_raw_data: "type_defs.EmailConfigurationTypeDef" = dataclasses.field()

    from_ = field("from")

    @cached_property
    def recipients(self):  # pragma: no cover
        return EmailRecipients.make_one(self.boto3_raw_data["recipients"])

    @cached_property
    def content(self):  # pragma: no cover
        return EmailContent.make_one(self.boto3_raw_data["content"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventOutput:
    boto3_raw_data: "type_defs.EventOutputTypeDef" = dataclasses.field()

    eventName = field("eventName")
    condition = field("condition")

    @cached_property
    def actions(self):  # pragma: no cover
        return Action.make_many(self.boto3_raw_data["actions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    eventName = field("eventName")
    condition = field("condition")

    @cached_property
    def actions(self):  # pragma: no cover
        return Action.make_many(self.boto3_raw_data["actions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitionEventOutput:
    boto3_raw_data: "type_defs.TransitionEventOutputTypeDef" = dataclasses.field()

    eventName = field("eventName")
    condition = field("condition")
    nextState = field("nextState")

    @cached_property
    def actions(self):  # pragma: no cover
        return Action.make_many(self.boto3_raw_data["actions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransitionEventOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitionEventOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitionEvent:
    boto3_raw_data: "type_defs.TransitionEventTypeDef" = dataclasses.field()

    eventName = field("eventName")
    condition = field("condition")
    nextState = field("nextState")

    @cached_property
    def actions(self):  # pragma: no cover
        return Action.make_many(self.boto3_raw_data["actions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransitionEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransitionEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmEventActionsOutput:
    boto3_raw_data: "type_defs.AlarmEventActionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def alarmActions(self):  # pragma: no cover
        return AlarmAction.make_many(self.boto3_raw_data["alarmActions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlarmEventActionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmEventActionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmEventActions:
    boto3_raw_data: "type_defs.AlarmEventActionsTypeDef" = dataclasses.field()

    @cached_property
    def alarmActions(self):  # pragma: no cover
        return AlarmAction.make_many(self.boto3_raw_data["alarmActions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmEventActionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmEventActionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationActionOutput:
    boto3_raw_data: "type_defs.NotificationActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return NotificationTargetActions.make_one(self.boto3_raw_data["action"])

    @cached_property
    def smsConfigurations(self):  # pragma: no cover
        return SMSConfigurationOutput.make_many(
            self.boto3_raw_data["smsConfigurations"]
        )

    @cached_property
    def emailConfigurations(self):  # pragma: no cover
        return EmailConfigurationOutput.make_many(
            self.boto3_raw_data["emailConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationAction:
    boto3_raw_data: "type_defs.NotificationActionTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return NotificationTargetActions.make_one(self.boto3_raw_data["action"])

    @cached_property
    def smsConfigurations(self):  # pragma: no cover
        return SMSConfiguration.make_many(self.boto3_raw_data["smsConfigurations"])

    @cached_property
    def emailConfigurations(self):  # pragma: no cover
        return EmailConfiguration.make_many(self.boto3_raw_data["emailConfigurations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnEnterLifecycleOutput:
    boto3_raw_data: "type_defs.OnEnterLifecycleOutputTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return EventOutput.make_many(self.boto3_raw_data["events"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OnEnterLifecycleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnEnterLifecycleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnExitLifecycleOutput:
    boto3_raw_data: "type_defs.OnExitLifecycleOutputTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return EventOutput.make_many(self.boto3_raw_data["events"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OnExitLifecycleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnExitLifecycleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnEnterLifecycle:
    boto3_raw_data: "type_defs.OnEnterLifecycleTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["events"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OnEnterLifecycleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnEnterLifecycleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnExitLifecycle:
    boto3_raw_data: "type_defs.OnExitLifecycleTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["events"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OnExitLifecycleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OnExitLifecycleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnInputLifecycleOutput:
    boto3_raw_data: "type_defs.OnInputLifecycleOutputTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return EventOutput.make_many(self.boto3_raw_data["events"])

    @cached_property
    def transitionEvents(self):  # pragma: no cover
        return TransitionEventOutput.make_many(self.boto3_raw_data["transitionEvents"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OnInputLifecycleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnInputLifecycleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnInputLifecycle:
    boto3_raw_data: "type_defs.OnInputLifecycleTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["events"])

    @cached_property
    def transitionEvents(self):  # pragma: no cover
        return TransitionEvent.make_many(self.boto3_raw_data["transitionEvents"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OnInputLifecycleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnInputLifecycleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmNotificationOutput:
    boto3_raw_data: "type_defs.AlarmNotificationOutputTypeDef" = dataclasses.field()

    @cached_property
    def notificationActions(self):  # pragma: no cover
        return NotificationActionOutput.make_many(
            self.boto3_raw_data["notificationActions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlarmNotificationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmNotificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmNotification:
    boto3_raw_data: "type_defs.AlarmNotificationTypeDef" = dataclasses.field()

    @cached_property
    def notificationActions(self):  # pragma: no cover
        return NotificationAction.make_many(self.boto3_raw_data["notificationActions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmNotificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmNotificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateOutput:
    boto3_raw_data: "type_defs.StateOutputTypeDef" = dataclasses.field()

    stateName = field("stateName")

    @cached_property
    def onInput(self):  # pragma: no cover
        return OnInputLifecycleOutput.make_one(self.boto3_raw_data["onInput"])

    @cached_property
    def onEnter(self):  # pragma: no cover
        return OnEnterLifecycleOutput.make_one(self.boto3_raw_data["onEnter"])

    @cached_property
    def onExit(self):  # pragma: no cover
        return OnExitLifecycleOutput.make_one(self.boto3_raw_data["onExit"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StateOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StateOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class State:
    boto3_raw_data: "type_defs.StateTypeDef" = dataclasses.field()

    stateName = field("stateName")

    @cached_property
    def onInput(self):  # pragma: no cover
        return OnInputLifecycle.make_one(self.boto3_raw_data["onInput"])

    @cached_property
    def onEnter(self):  # pragma: no cover
        return OnEnterLifecycle.make_one(self.boto3_raw_data["onEnter"])

    @cached_property
    def onExit(self):  # pragma: no cover
        return OnExitLifecycle.make_one(self.boto3_raw_data["onExit"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmModelResponse:
    boto3_raw_data: "type_defs.DescribeAlarmModelResponseTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    alarmModelArn = field("alarmModelArn")
    alarmModelVersion = field("alarmModelVersion")
    lastUpdateTime = field("lastUpdateTime")
    status = field("status")
    statusMessage = field("statusMessage")
    alarmModelName = field("alarmModelName")
    alarmModelDescription = field("alarmModelDescription")
    roleArn = field("roleArn")
    key = field("key")
    severity = field("severity")

    @cached_property
    def alarmRule(self):  # pragma: no cover
        return AlarmRule.make_one(self.boto3_raw_data["alarmRule"])

    @cached_property
    def alarmNotification(self):  # pragma: no cover
        return AlarmNotificationOutput.make_one(
            self.boto3_raw_data["alarmNotification"]
        )

    @cached_property
    def alarmEventActions(self):  # pragma: no cover
        return AlarmEventActionsOutput.make_one(
            self.boto3_raw_data["alarmEventActions"]
        )

    @cached_property
    def alarmCapabilities(self):  # pragma: no cover
        return AlarmCapabilities.make_one(self.boto3_raw_data["alarmCapabilities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorModelDefinitionOutput:
    boto3_raw_data: "type_defs.DetectorModelDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def states(self):  # pragma: no cover
        return StateOutput.make_many(self.boto3_raw_data["states"])

    initialStateName = field("initialStateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectorModelDefinitionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorModelDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorModelDefinition:
    boto3_raw_data: "type_defs.DetectorModelDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def states(self):  # pragma: no cover
        return State.make_many(self.boto3_raw_data["states"])

    initialStateName = field("initialStateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectorModelDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorModelDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAlarmModelRequest:
    boto3_raw_data: "type_defs.CreateAlarmModelRequestTypeDef" = dataclasses.field()

    alarmModelName = field("alarmModelName")
    roleArn = field("roleArn")

    @cached_property
    def alarmRule(self):  # pragma: no cover
        return AlarmRule.make_one(self.boto3_raw_data["alarmRule"])

    alarmModelDescription = field("alarmModelDescription")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    key = field("key")
    severity = field("severity")
    alarmNotification = field("alarmNotification")
    alarmEventActions = field("alarmEventActions")

    @cached_property
    def alarmCapabilities(self):  # pragma: no cover
        return AlarmCapabilities.make_one(self.boto3_raw_data["alarmCapabilities"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAlarmModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAlarmModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAlarmModelRequest:
    boto3_raw_data: "type_defs.UpdateAlarmModelRequestTypeDef" = dataclasses.field()

    alarmModelName = field("alarmModelName")
    roleArn = field("roleArn")

    @cached_property
    def alarmRule(self):  # pragma: no cover
        return AlarmRule.make_one(self.boto3_raw_data["alarmRule"])

    alarmModelDescription = field("alarmModelDescription")
    severity = field("severity")
    alarmNotification = field("alarmNotification")
    alarmEventActions = field("alarmEventActions")

    @cached_property
    def alarmCapabilities(self):  # pragma: no cover
        return AlarmCapabilities.make_one(self.boto3_raw_data["alarmCapabilities"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAlarmModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAlarmModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorModel:
    boto3_raw_data: "type_defs.DetectorModelTypeDef" = dataclasses.field()

    @cached_property
    def detectorModelDefinition(self):  # pragma: no cover
        return DetectorModelDefinitionOutput.make_one(
            self.boto3_raw_data["detectorModelDefinition"]
        )

    @cached_property
    def detectorModelConfiguration(self):  # pragma: no cover
        return DetectorModelConfiguration.make_one(
            self.boto3_raw_data["detectorModelConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectorModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetectorModelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDetectorModelResponse:
    boto3_raw_data: "type_defs.DescribeDetectorModelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def detectorModel(self):  # pragma: no cover
        return DetectorModel.make_one(self.boto3_raw_data["detectorModel"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDetectorModelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDetectorModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDetectorModelRequest:
    boto3_raw_data: "type_defs.CreateDetectorModelRequestTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")
    detectorModelDefinition = field("detectorModelDefinition")
    roleArn = field("roleArn")
    detectorModelDescription = field("detectorModelDescription")
    key = field("key")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    evaluationMethod = field("evaluationMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDetectorModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDetectorModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDetectorModelAnalysisRequest:
    boto3_raw_data: "type_defs.StartDetectorModelAnalysisRequestTypeDef" = (
        dataclasses.field()
    )

    detectorModelDefinition = field("detectorModelDefinition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDetectorModelAnalysisRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDetectorModelAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDetectorModelRequest:
    boto3_raw_data: "type_defs.UpdateDetectorModelRequestTypeDef" = dataclasses.field()

    detectorModelName = field("detectorModelName")
    detectorModelDefinition = field("detectorModelDefinition")
    roleArn = field("roleArn")
    detectorModelDescription = field("detectorModelDescription")
    evaluationMethod = field("evaluationMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDetectorModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDetectorModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
