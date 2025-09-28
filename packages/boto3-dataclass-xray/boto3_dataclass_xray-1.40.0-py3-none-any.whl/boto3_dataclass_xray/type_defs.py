# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_xray import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Alias:
    boto3_raw_data: "type_defs.AliasTypeDef" = dataclasses.field()

    Name = field("Name")
    Names = field("Names")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AliasTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AliasTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnnotationValue:
    boto3_raw_data: "type_defs.AnnotationValueTypeDef" = dataclasses.field()

    NumberValue = field("NumberValue")
    BooleanValue = field("BooleanValue")
    StringValue = field("StringValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnnotationValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnnotationValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceId:
    boto3_raw_data: "type_defs.ServiceIdTypeDef" = dataclasses.field()

    Name = field("Name")
    Names = field("Names")
    AccountId = field("AccountId")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceIdTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityZoneDetail:
    boto3_raw_data: "type_defs.AvailabilityZoneDetailTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendConnectionErrors:
    boto3_raw_data: "type_defs.BackendConnectionErrorsTypeDef" = dataclasses.field()

    TimeoutCount = field("TimeoutCount")
    ConnectionRefusedCount = field("ConnectionRefusedCount")
    HTTPCode4XXCount = field("HTTPCode4XXCount")
    HTTPCode5XXCount = field("HTTPCode5XXCount")
    UnknownHostCount = field("UnknownHostCount")
    OtherCount = field("OtherCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackendConnectionErrorsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendConnectionErrorsTypeDef"]
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
class BatchGetTracesRequest:
    boto3_raw_data: "type_defs.BatchGetTracesRequestTypeDef" = dataclasses.field()

    TraceIds = field("TraceIds")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetTracesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetTracesRequestTypeDef"]
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
class CancelTraceRetrievalRequest:
    boto3_raw_data: "type_defs.CancelTraceRetrievalRequestTypeDef" = dataclasses.field()

    RetrievalToken = field("RetrievalToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelTraceRetrievalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelTraceRetrievalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightsConfiguration:
    boto3_raw_data: "type_defs.InsightsConfigurationTypeDef" = dataclasses.field()

    InsightsEnabled = field("InsightsEnabled")
    NotificationsEnabled = field("NotificationsEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InsightsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsightsConfigurationTypeDef"]
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

    Key = field("Key")
    Value = field("Value")

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
class DeleteGroupRequest:
    boto3_raw_data: "type_defs.DeleteGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    GroupARN = field("GroupARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyRequestTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyRevisionId = field("PolicyRevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSamplingRuleRequest:
    boto3_raw_data: "type_defs.DeleteSamplingRuleRequestTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    RuleARN = field("RuleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSamplingRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSamplingRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorStatistics:
    boto3_raw_data: "type_defs.ErrorStatisticsTypeDef" = dataclasses.field()

    ThrottleCount = field("ThrottleCount")
    OtherCount = field("OtherCount")
    TotalCount = field("TotalCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaultStatistics:
    boto3_raw_data: "type_defs.FaultStatisticsTypeDef" = dataclasses.field()

    OtherCount = field("OtherCount")
    TotalCount = field("TotalCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FaultStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FaultStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HistogramEntry:
    boto3_raw_data: "type_defs.HistogramEntryTypeDef" = dataclasses.field()

    Value = field("Value")
    Count = field("Count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HistogramEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HistogramEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfig:
    boto3_raw_data: "type_defs.EncryptionConfigTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Status = field("Status")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RootCauseException:
    boto3_raw_data: "type_defs.RootCauseExceptionTypeDef" = dataclasses.field()

    Name = field("Name")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RootCauseExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RootCauseExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForecastStatistics:
    boto3_raw_data: "type_defs.ForecastStatisticsTypeDef" = dataclasses.field()

    FaultCountHigh = field("FaultCountHigh")
    FaultCountLow = field("FaultCountLow")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ForecastStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForecastStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupRequest:
    boto3_raw_data: "type_defs.GetGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    GroupARN = field("GroupARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetGroupRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupsRequest:
    boto3_raw_data: "type_defs.GetGroupsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIndexingRulesRequest:
    boto3_raw_data: "type_defs.GetIndexingRulesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIndexingRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIndexingRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightEventsRequest:
    boto3_raw_data: "type_defs.GetInsightEventsRequestTypeDef" = dataclasses.field()

    InsightId = field("InsightId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightRequest:
    boto3_raw_data: "type_defs.GetInsightRequestTypeDef" = dataclasses.field()

    InsightId = field("InsightId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetInsightRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRetrievedTracesGraphRequest:
    boto3_raw_data: "type_defs.GetRetrievedTracesGraphRequestTypeDef" = (
        dataclasses.field()
    )

    RetrievalToken = field("RetrievalToken")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRetrievedTracesGraphRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRetrievedTracesGraphRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSamplingRulesRequest:
    boto3_raw_data: "type_defs.GetSamplingRulesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSamplingRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSamplingRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSamplingStatisticSummariesRequest:
    boto3_raw_data: "type_defs.GetSamplingStatisticSummariesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSamplingStatisticSummariesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSamplingStatisticSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingStatisticSummary:
    boto3_raw_data: "type_defs.SamplingStatisticSummaryTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    Timestamp = field("Timestamp")
    RequestCount = field("RequestCount")
    BorrowCount = field("BorrowCount")
    SampledCount = field("SampledCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SamplingStatisticSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamplingStatisticSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnprocessedStatistics:
    boto3_raw_data: "type_defs.UnprocessedStatisticsTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    ErrorCode = field("ErrorCode")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTraceGraphRequest:
    boto3_raw_data: "type_defs.GetTraceGraphRequestTypeDef" = dataclasses.field()

    TraceIds = field("TraceIds")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTraceGraphRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTraceGraphRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingStrategy:
    boto3_raw_data: "type_defs.SamplingStrategyTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SamplingStrategyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamplingStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GraphLink:
    boto3_raw_data: "type_defs.GraphLinkTypeDef" = dataclasses.field()

    ReferenceType = field("ReferenceType")
    SourceTraceId = field("SourceTraceId")
    DestinationTraceIds = field("DestinationTraceIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GraphLinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GraphLinkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Http:
    boto3_raw_data: "type_defs.HttpTypeDef" = dataclasses.field()

    HttpURL = field("HttpURL")
    HttpStatus = field("HttpStatus")
    HttpMethod = field("HttpMethod")
    UserAgent = field("UserAgent")
    ClientIp = field("ClientIp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProbabilisticRuleValue:
    boto3_raw_data: "type_defs.ProbabilisticRuleValueTypeDef" = dataclasses.field()

    DesiredSamplingPercentage = field("DesiredSamplingPercentage")
    ActualSamplingPercentage = field("ActualSamplingPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProbabilisticRuleValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProbabilisticRuleValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProbabilisticRuleValueUpdate:
    boto3_raw_data: "type_defs.ProbabilisticRuleValueUpdateTypeDef" = (
        dataclasses.field()
    )

    DesiredSamplingPercentage = field("DesiredSamplingPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProbabilisticRuleValueUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProbabilisticRuleValueUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestImpactStatistics:
    boto3_raw_data: "type_defs.RequestImpactStatisticsTypeDef" = dataclasses.field()

    FaultCount = field("FaultCount")
    OkCount = field("OkCount")
    TotalCount = field("TotalCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestImpactStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestImpactStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightImpactGraphEdge:
    boto3_raw_data: "type_defs.InsightImpactGraphEdgeTypeDef" = dataclasses.field()

    ReferenceId = field("ReferenceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InsightImpactGraphEdgeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsightImpactGraphEdgeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceIdDetail:
    boto3_raw_data: "type_defs.InstanceIdDetailTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceIdDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceIdDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcePoliciesRequest:
    boto3_raw_data: "type_defs.ListResourcePoliciesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourcePoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcePoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourcePolicy:
    boto3_raw_data: "type_defs.ResourcePolicyTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")
    PolicyRevisionId = field("PolicyRevisionId")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourcePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourcePolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRetrievedTracesRequest:
    boto3_raw_data: "type_defs.ListRetrievedTracesRequestTypeDef" = dataclasses.field()

    RetrievalToken = field("RetrievalToken")
    TraceFormat = field("TraceFormat")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRetrievedTracesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRetrievedTracesRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")
    NextToken = field("NextToken")

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
class PutEncryptionConfigRequest:
    boto3_raw_data: "type_defs.PutEncryptionConfigRequestTypeDef" = dataclasses.field()

    Type = field("Type")
    KeyId = field("KeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEncryptionConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEncryptionConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")
    PolicyRevisionId = field("PolicyRevisionId")
    BypassPolicyLockoutCheck = field("BypassPolicyLockoutCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTraceSegmentsRequest:
    boto3_raw_data: "type_defs.PutTraceSegmentsRequestTypeDef" = dataclasses.field()

    TraceSegmentDocuments = field("TraceSegmentDocuments")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTraceSegmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTraceSegmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnprocessedTraceSegment:
    boto3_raw_data: "type_defs.UnprocessedTraceSegmentTypeDef" = dataclasses.field()

    Id = field("Id")
    ErrorCode = field("ErrorCode")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedTraceSegmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedTraceSegmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceARNDetail:
    boto3_raw_data: "type_defs.ResourceARNDetailTypeDef" = dataclasses.field()

    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceARNDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceARNDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseTimeRootCauseEntity:
    boto3_raw_data: "type_defs.ResponseTimeRootCauseEntityTypeDef" = dataclasses.field()

    Name = field("Name")
    Coverage = field("Coverage")
    Remote = field("Remote")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseTimeRootCauseEntityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseTimeRootCauseEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Span:
    boto3_raw_data: "type_defs.SpanTypeDef" = dataclasses.field()

    Id = field("Id")
    Document = field("Document")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SpanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingBoost:
    boto3_raw_data: "type_defs.SamplingBoostTypeDef" = dataclasses.field()

    BoostRate = field("BoostRate")
    BoostRateTTL = field("BoostRateTTL")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SamplingBoostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SamplingBoostTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingRateBoost:
    boto3_raw_data: "type_defs.SamplingRateBoostTypeDef" = dataclasses.field()

    MaxRate = field("MaxRate")
    CooldownWindowMinutes = field("CooldownWindowMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SamplingRateBoostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamplingRateBoostTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Segment:
    boto3_raw_data: "type_defs.SegmentTypeDef" = dataclasses.field()

    Id = field("Id")
    Document = field("Document")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SegmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    TagKeys = field("TagKeys")

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
class UpdateTraceSegmentDestinationRequest:
    boto3_raw_data: "type_defs.UpdateTraceSegmentDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    Destination = field("Destination")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTraceSegmentDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTraceSegmentDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalousService:
    boto3_raw_data: "type_defs.AnomalousServiceTypeDef" = dataclasses.field()

    @cached_property
    def ServiceId(self):  # pragma: no cover
        return ServiceId.make_one(self.boto3_raw_data["ServiceId"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalousServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalousServiceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TraceUser:
    boto3_raw_data: "type_defs.TraceUserTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @cached_property
    def ServiceIds(self):  # pragma: no cover
        return ServiceId.make_many(self.boto3_raw_data["ServiceIds"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TraceUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TraceUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueWithServiceIds:
    boto3_raw_data: "type_defs.ValueWithServiceIdsTypeDef" = dataclasses.field()

    @cached_property
    def AnnotationValue(self):  # pragma: no cover
        return AnnotationValue.make_one(self.boto3_raw_data["AnnotationValue"])

    @cached_property
    def ServiceIds(self):  # pragma: no cover
        return ServiceId.make_many(self.boto3_raw_data["ServiceIds"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValueWithServiceIdsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValueWithServiceIdsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetTracesRequestPaginate:
    boto3_raw_data: "type_defs.BatchGetTracesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TraceIds = field("TraceIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetTracesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetTracesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupsRequestPaginate:
    boto3_raw_data: "type_defs.GetGroupsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSamplingRulesRequestPaginate:
    boto3_raw_data: "type_defs.GetSamplingRulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSamplingRulesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSamplingRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSamplingStatisticSummariesRequestPaginate:
    boto3_raw_data: "type_defs.GetSamplingStatisticSummariesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSamplingStatisticSummariesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSamplingStatisticSummariesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTraceGraphRequestPaginate:
    boto3_raw_data: "type_defs.GetTraceGraphRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TraceIds = field("TraceIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTraceGraphRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTraceGraphRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcePoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListResourcePoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourcePoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcePoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTagsForResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTraceSegmentDestinationResult:
    boto3_raw_data: "type_defs.GetTraceSegmentDestinationResultTypeDef" = (
        dataclasses.field()
    )

    Destination = field("Destination")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTraceSegmentDestinationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTraceSegmentDestinationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTraceRetrievalResult:
    boto3_raw_data: "type_defs.StartTraceRetrievalResultTypeDef" = dataclasses.field()

    RetrievalToken = field("RetrievalToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTraceRetrievalResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTraceRetrievalResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTraceSegmentDestinationResult:
    boto3_raw_data: "type_defs.UpdateTraceSegmentDestinationResultTypeDef" = (
        dataclasses.field()
    )

    Destination = field("Destination")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTraceSegmentDestinationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTraceSegmentDestinationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupSummary:
    boto3_raw_data: "type_defs.GroupSummaryTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    GroupARN = field("GroupARN")
    FilterExpression = field("FilterExpression")

    @cached_property
    def InsightsConfiguration(self):  # pragma: no cover
        return InsightsConfiguration.make_one(
            self.boto3_raw_data["InsightsConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Group:
    boto3_raw_data: "type_defs.GroupTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    GroupARN = field("GroupARN")
    FilterExpression = field("FilterExpression")

    @cached_property
    def InsightsConfiguration(self):  # pragma: no cover
        return InsightsConfiguration.make_one(
            self.boto3_raw_data["InsightsConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupRequest:
    boto3_raw_data: "type_defs.UpdateGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    GroupARN = field("GroupARN")
    FilterExpression = field("FilterExpression")

    @cached_property
    def InsightsConfiguration(self):  # pragma: no cover
        return InsightsConfiguration.make_one(
            self.boto3_raw_data["InsightsConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupRequest:
    boto3_raw_data: "type_defs.CreateGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    FilterExpression = field("FilterExpression")

    @cached_property
    def InsightsConfiguration(self):  # pragma: no cover
        return InsightsConfiguration.make_one(
            self.boto3_raw_data["InsightsConfiguration"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupRequestTypeDef"]
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
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class EdgeStatistics:
    boto3_raw_data: "type_defs.EdgeStatisticsTypeDef" = dataclasses.field()

    OkCount = field("OkCount")

    @cached_property
    def ErrorStatistics(self):  # pragma: no cover
        return ErrorStatistics.make_one(self.boto3_raw_data["ErrorStatistics"])

    @cached_property
    def FaultStatistics(self):  # pragma: no cover
        return FaultStatistics.make_one(self.boto3_raw_data["FaultStatistics"])

    TotalCount = field("TotalCount")
    TotalResponseTime = field("TotalResponseTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdgeStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdgeStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceStatistics:
    boto3_raw_data: "type_defs.ServiceStatisticsTypeDef" = dataclasses.field()

    OkCount = field("OkCount")

    @cached_property
    def ErrorStatistics(self):  # pragma: no cover
        return ErrorStatistics.make_one(self.boto3_raw_data["ErrorStatistics"])

    @cached_property
    def FaultStatistics(self):  # pragma: no cover
        return FaultStatistics.make_one(self.boto3_raw_data["FaultStatistics"])

    TotalCount = field("TotalCount")
    TotalResponseTime = field("TotalResponseTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEncryptionConfigResult:
    boto3_raw_data: "type_defs.GetEncryptionConfigResultTypeDef" = dataclasses.field()

    @cached_property
    def EncryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["EncryptionConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEncryptionConfigResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEncryptionConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEncryptionConfigResult:
    boto3_raw_data: "type_defs.PutEncryptionConfigResultTypeDef" = dataclasses.field()

    @cached_property
    def EncryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["EncryptionConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEncryptionConfigResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEncryptionConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorRootCauseEntity:
    boto3_raw_data: "type_defs.ErrorRootCauseEntityTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Exceptions(self):  # pragma: no cover
        return RootCauseException.make_many(self.boto3_raw_data["Exceptions"])

    Remote = field("Remote")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ErrorRootCauseEntityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ErrorRootCauseEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaultRootCauseEntity:
    boto3_raw_data: "type_defs.FaultRootCauseEntityTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Exceptions(self):  # pragma: no cover
        return RootCauseException.make_many(self.boto3_raw_data["Exceptions"])

    Remote = field("Remote")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FaultRootCauseEntityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FaultRootCauseEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightImpactGraphRequest:
    boto3_raw_data: "type_defs.GetInsightImpactGraphRequestTypeDef" = (
        dataclasses.field()
    )

    InsightId = field("InsightId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightImpactGraphRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightImpactGraphRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightSummariesRequest:
    boto3_raw_data: "type_defs.GetInsightSummariesRequestTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    States = field("States")
    GroupARN = field("GroupARN")
    GroupName = field("GroupName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightSummariesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceGraphRequestPaginate:
    boto3_raw_data: "type_defs.GetServiceGraphRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    GroupName = field("GroupName")
    GroupARN = field("GroupARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetServiceGraphRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceGraphRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceGraphRequest:
    boto3_raw_data: "type_defs.GetServiceGraphRequestTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    GroupName = field("GroupName")
    GroupARN = field("GroupARN")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceGraphRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceGraphRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTimeSeriesServiceStatisticsRequestPaginate:
    boto3_raw_data: "type_defs.GetTimeSeriesServiceStatisticsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    GroupName = field("GroupName")
    GroupARN = field("GroupARN")
    EntitySelectorExpression = field("EntitySelectorExpression")
    Period = field("Period")
    ForecastStatistics = field("ForecastStatistics")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTimeSeriesServiceStatisticsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTimeSeriesServiceStatisticsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTimeSeriesServiceStatisticsRequest:
    boto3_raw_data: "type_defs.GetTimeSeriesServiceStatisticsRequestTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    GroupName = field("GroupName")
    GroupARN = field("GroupARN")
    EntitySelectorExpression = field("EntitySelectorExpression")
    Period = field("Period")
    ForecastStatistics = field("ForecastStatistics")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTimeSeriesServiceStatisticsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTimeSeriesServiceStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingBoostStatisticsDocument:
    boto3_raw_data: "type_defs.SamplingBoostStatisticsDocumentTypeDef" = (
        dataclasses.field()
    )

    RuleName = field("RuleName")
    ServiceName = field("ServiceName")
    Timestamp = field("Timestamp")
    AnomalyCount = field("AnomalyCount")
    TotalCount = field("TotalCount")
    SampledAnomalyCount = field("SampledAnomalyCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SamplingBoostStatisticsDocumentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamplingBoostStatisticsDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingStatisticsDocument:
    boto3_raw_data: "type_defs.SamplingStatisticsDocumentTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    ClientID = field("ClientID")
    Timestamp = field("Timestamp")
    RequestCount = field("RequestCount")
    SampledCount = field("SampledCount")
    BorrowCount = field("BorrowCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SamplingStatisticsDocumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamplingStatisticsDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTraceRetrievalRequest:
    boto3_raw_data: "type_defs.StartTraceRetrievalRequestTypeDef" = dataclasses.field()

    TraceIds = field("TraceIds")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTraceRetrievalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTraceRetrievalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelemetryRecord:
    boto3_raw_data: "type_defs.TelemetryRecordTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    SegmentsReceivedCount = field("SegmentsReceivedCount")
    SegmentsSentCount = field("SegmentsSentCount")
    SegmentsSpilloverCount = field("SegmentsSpilloverCount")
    SegmentsRejectedCount = field("SegmentsRejectedCount")

    @cached_property
    def BackendConnectionErrors(self):  # pragma: no cover
        return BackendConnectionErrors.make_one(
            self.boto3_raw_data["BackendConnectionErrors"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TelemetryRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TelemetryRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSamplingStatisticSummariesResult:
    boto3_raw_data: "type_defs.GetSamplingStatisticSummariesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SamplingStatisticSummaries(self):  # pragma: no cover
        return SamplingStatisticSummary.make_many(
            self.boto3_raw_data["SamplingStatisticSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSamplingStatisticSummariesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSamplingStatisticSummariesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTraceSummariesRequestPaginate:
    boto3_raw_data: "type_defs.GetTraceSummariesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    TimeRangeType = field("TimeRangeType")
    Sampling = field("Sampling")

    @cached_property
    def SamplingStrategy(self):  # pragma: no cover
        return SamplingStrategy.make_one(self.boto3_raw_data["SamplingStrategy"])

    FilterExpression = field("FilterExpression")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTraceSummariesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTraceSummariesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTraceSummariesRequest:
    boto3_raw_data: "type_defs.GetTraceSummariesRequestTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    TimeRangeType = field("TimeRangeType")
    Sampling = field("Sampling")

    @cached_property
    def SamplingStrategy(self):  # pragma: no cover
        return SamplingStrategy.make_one(self.boto3_raw_data["SamplingStrategy"])

    FilterExpression = field("FilterExpression")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTraceSummariesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTraceSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexingRuleValue:
    boto3_raw_data: "type_defs.IndexingRuleValueTypeDef" = dataclasses.field()

    @cached_property
    def Probabilistic(self):  # pragma: no cover
        return ProbabilisticRuleValue.make_one(self.boto3_raw_data["Probabilistic"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexingRuleValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexingRuleValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexingRuleValueUpdate:
    boto3_raw_data: "type_defs.IndexingRuleValueUpdateTypeDef" = dataclasses.field()

    @cached_property
    def Probabilistic(self):  # pragma: no cover
        return ProbabilisticRuleValueUpdate.make_one(
            self.boto3_raw_data["Probabilistic"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IndexingRuleValueUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexingRuleValueUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightImpactGraphService:
    boto3_raw_data: "type_defs.InsightImpactGraphServiceTypeDef" = dataclasses.field()

    ReferenceId = field("ReferenceId")
    Type = field("Type")
    Name = field("Name")
    Names = field("Names")
    AccountId = field("AccountId")

    @cached_property
    def Edges(self):  # pragma: no cover
        return InsightImpactGraphEdge.make_many(self.boto3_raw_data["Edges"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InsightImpactGraphServiceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsightImpactGraphServiceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcePoliciesResult:
    boto3_raw_data: "type_defs.ListResourcePoliciesResultTypeDef" = dataclasses.field()

    @cached_property
    def ResourcePolicies(self):  # pragma: no cover
        return ResourcePolicy.make_many(self.boto3_raw_data["ResourcePolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourcePoliciesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcePoliciesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyResult:
    boto3_raw_data: "type_defs.PutResourcePolicyResultTypeDef" = dataclasses.field()

    @cached_property
    def ResourcePolicy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["ResourcePolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTraceSegmentsResult:
    boto3_raw_data: "type_defs.PutTraceSegmentsResultTypeDef" = dataclasses.field()

    @cached_property
    def UnprocessedTraceSegments(self):  # pragma: no cover
        return UnprocessedTraceSegment.make_many(
            self.boto3_raw_data["UnprocessedTraceSegments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTraceSegmentsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTraceSegmentsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseTimeRootCauseService:
    boto3_raw_data: "type_defs.ResponseTimeRootCauseServiceTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Names = field("Names")
    Type = field("Type")
    AccountId = field("AccountId")

    @cached_property
    def EntityPath(self):  # pragma: no cover
        return ResponseTimeRootCauseEntity.make_many(self.boto3_raw_data["EntityPath"])

    Inferred = field("Inferred")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseTimeRootCauseServiceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseTimeRootCauseServiceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievedTrace:
    boto3_raw_data: "type_defs.RetrievedTraceTypeDef" = dataclasses.field()

    Id = field("Id")
    Duration = field("Duration")

    @cached_property
    def Spans(self):  # pragma: no cover
        return Span.make_many(self.boto3_raw_data["Spans"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetrievedTraceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetrievedTraceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingTargetDocument:
    boto3_raw_data: "type_defs.SamplingTargetDocumentTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    FixedRate = field("FixedRate")
    ReservoirQuota = field("ReservoirQuota")
    ReservoirQuotaTTL = field("ReservoirQuotaTTL")
    Interval = field("Interval")

    @cached_property
    def SamplingBoost(self):  # pragma: no cover
        return SamplingBoost.make_one(self.boto3_raw_data["SamplingBoost"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SamplingTargetDocumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamplingTargetDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingRuleOutput:
    boto3_raw_data: "type_defs.SamplingRuleOutputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    Priority = field("Priority")
    FixedRate = field("FixedRate")
    ReservoirSize = field("ReservoirSize")
    ServiceName = field("ServiceName")
    ServiceType = field("ServiceType")
    Host = field("Host")
    HTTPMethod = field("HTTPMethod")
    URLPath = field("URLPath")
    Version = field("Version")
    RuleName = field("RuleName")
    RuleARN = field("RuleARN")
    Attributes = field("Attributes")

    @cached_property
    def SamplingRateBoost(self):  # pragma: no cover
        return SamplingRateBoost.make_one(self.boto3_raw_data["SamplingRateBoost"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SamplingRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamplingRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingRule:
    boto3_raw_data: "type_defs.SamplingRuleTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    Priority = field("Priority")
    FixedRate = field("FixedRate")
    ReservoirSize = field("ReservoirSize")
    ServiceName = field("ServiceName")
    ServiceType = field("ServiceType")
    Host = field("Host")
    HTTPMethod = field("HTTPMethod")
    URLPath = field("URLPath")
    Version = field("Version")
    RuleName = field("RuleName")
    RuleARN = field("RuleARN")
    Attributes = field("Attributes")

    @cached_property
    def SamplingRateBoost(self):  # pragma: no cover
        return SamplingRateBoost.make_one(self.boto3_raw_data["SamplingRateBoost"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SamplingRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SamplingRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingRuleUpdate:
    boto3_raw_data: "type_defs.SamplingRuleUpdateTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    RuleARN = field("RuleARN")
    ResourceARN = field("ResourceARN")
    Priority = field("Priority")
    FixedRate = field("FixedRate")
    ReservoirSize = field("ReservoirSize")
    Host = field("Host")
    ServiceName = field("ServiceName")
    ServiceType = field("ServiceType")
    HTTPMethod = field("HTTPMethod")
    URLPath = field("URLPath")
    Attributes = field("Attributes")

    @cached_property
    def SamplingRateBoost(self):  # pragma: no cover
        return SamplingRateBoost.make_one(self.boto3_raw_data["SamplingRateBoost"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SamplingRuleUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamplingRuleUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Trace:
    boto3_raw_data: "type_defs.TraceTypeDef" = dataclasses.field()

    Id = field("Id")
    Duration = field("Duration")
    LimitExceeded = field("LimitExceeded")

    @cached_property
    def Segments(self):  # pragma: no cover
        return Segment.make_many(self.boto3_raw_data["Segments"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TraceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TraceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightEvent:
    boto3_raw_data: "type_defs.InsightEventTypeDef" = dataclasses.field()

    Summary = field("Summary")
    EventTime = field("EventTime")

    @cached_property
    def ClientRequestImpactStatistics(self):  # pragma: no cover
        return RequestImpactStatistics.make_one(
            self.boto3_raw_data["ClientRequestImpactStatistics"]
        )

    @cached_property
    def RootCauseServiceRequestImpactStatistics(self):  # pragma: no cover
        return RequestImpactStatistics.make_one(
            self.boto3_raw_data["RootCauseServiceRequestImpactStatistics"]
        )

    @cached_property
    def TopAnomalousServices(self):  # pragma: no cover
        return AnomalousService.make_many(self.boto3_raw_data["TopAnomalousServices"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightSummary:
    boto3_raw_data: "type_defs.InsightSummaryTypeDef" = dataclasses.field()

    InsightId = field("InsightId")
    GroupARN = field("GroupARN")
    GroupName = field("GroupName")

    @cached_property
    def RootCauseServiceId(self):  # pragma: no cover
        return ServiceId.make_one(self.boto3_raw_data["RootCauseServiceId"])

    Categories = field("Categories")
    State = field("State")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Summary = field("Summary")

    @cached_property
    def ClientRequestImpactStatistics(self):  # pragma: no cover
        return RequestImpactStatistics.make_one(
            self.boto3_raw_data["ClientRequestImpactStatistics"]
        )

    @cached_property
    def RootCauseServiceRequestImpactStatistics(self):  # pragma: no cover
        return RequestImpactStatistics.make_one(
            self.boto3_raw_data["RootCauseServiceRequestImpactStatistics"]
        )

    @cached_property
    def TopAnomalousServices(self):  # pragma: no cover
        return AnomalousService.make_many(self.boto3_raw_data["TopAnomalousServices"])

    LastUpdateTime = field("LastUpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Insight:
    boto3_raw_data: "type_defs.InsightTypeDef" = dataclasses.field()

    InsightId = field("InsightId")
    GroupARN = field("GroupARN")
    GroupName = field("GroupName")

    @cached_property
    def RootCauseServiceId(self):  # pragma: no cover
        return ServiceId.make_one(self.boto3_raw_data["RootCauseServiceId"])

    Categories = field("Categories")
    State = field("State")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Summary = field("Summary")

    @cached_property
    def ClientRequestImpactStatistics(self):  # pragma: no cover
        return RequestImpactStatistics.make_one(
            self.boto3_raw_data["ClientRequestImpactStatistics"]
        )

    @cached_property
    def RootCauseServiceRequestImpactStatistics(self):  # pragma: no cover
        return RequestImpactStatistics.make_one(
            self.boto3_raw_data["RootCauseServiceRequestImpactStatistics"]
        )

    @cached_property
    def TopAnomalousServices(self):  # pragma: no cover
        return AnomalousService.make_many(self.boto3_raw_data["TopAnomalousServices"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupsResult:
    boto3_raw_data: "type_defs.GetGroupsResultTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupSummary.make_many(self.boto3_raw_data["Groups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetGroupsResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupResult:
    boto3_raw_data: "type_defs.CreateGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def Group(self):  # pragma: no cover
        return Group.make_one(self.boto3_raw_data["Group"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateGroupResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupResult:
    boto3_raw_data: "type_defs.GetGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def Group(self):  # pragma: no cover
        return Group.make_one(self.boto3_raw_data["Group"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetGroupResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupResult:
    boto3_raw_data: "type_defs.UpdateGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def Group(self):  # pragma: no cover
        return Group.make_one(self.boto3_raw_data["Group"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateGroupResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Edge:
    boto3_raw_data: "type_defs.EdgeTypeDef" = dataclasses.field()

    ReferenceId = field("ReferenceId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def SummaryStatistics(self):  # pragma: no cover
        return EdgeStatistics.make_one(self.boto3_raw_data["SummaryStatistics"])

    @cached_property
    def ResponseTimeHistogram(self):  # pragma: no cover
        return HistogramEntry.make_many(self.boto3_raw_data["ResponseTimeHistogram"])

    @cached_property
    def Aliases(self):  # pragma: no cover
        return Alias.make_many(self.boto3_raw_data["Aliases"])

    EdgeType = field("EdgeType")

    @cached_property
    def ReceivedEventAgeHistogram(self):  # pragma: no cover
        return HistogramEntry.make_many(
            self.boto3_raw_data["ReceivedEventAgeHistogram"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdgeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdgeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesServiceStatistics:
    boto3_raw_data: "type_defs.TimeSeriesServiceStatisticsTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")

    @cached_property
    def EdgeSummaryStatistics(self):  # pragma: no cover
        return EdgeStatistics.make_one(self.boto3_raw_data["EdgeSummaryStatistics"])

    @cached_property
    def ServiceSummaryStatistics(self):  # pragma: no cover
        return ServiceStatistics.make_one(
            self.boto3_raw_data["ServiceSummaryStatistics"]
        )

    @cached_property
    def ServiceForecastStatistics(self):  # pragma: no cover
        return ForecastStatistics.make_one(
            self.boto3_raw_data["ServiceForecastStatistics"]
        )

    @cached_property
    def ResponseTimeHistogram(self):  # pragma: no cover
        return HistogramEntry.make_many(self.boto3_raw_data["ResponseTimeHistogram"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesServiceStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesServiceStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorRootCauseService:
    boto3_raw_data: "type_defs.ErrorRootCauseServiceTypeDef" = dataclasses.field()

    Name = field("Name")
    Names = field("Names")
    Type = field("Type")
    AccountId = field("AccountId")

    @cached_property
    def EntityPath(self):  # pragma: no cover
        return ErrorRootCauseEntity.make_many(self.boto3_raw_data["EntityPath"])

    Inferred = field("Inferred")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ErrorRootCauseServiceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ErrorRootCauseServiceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaultRootCauseService:
    boto3_raw_data: "type_defs.FaultRootCauseServiceTypeDef" = dataclasses.field()

    Name = field("Name")
    Names = field("Names")
    Type = field("Type")
    AccountId = field("AccountId")

    @cached_property
    def EntityPath(self):  # pragma: no cover
        return FaultRootCauseEntity.make_many(self.boto3_raw_data["EntityPath"])

    Inferred = field("Inferred")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FaultRootCauseServiceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FaultRootCauseServiceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSamplingTargetsRequest:
    boto3_raw_data: "type_defs.GetSamplingTargetsRequestTypeDef" = dataclasses.field()

    @cached_property
    def SamplingStatisticsDocuments(self):  # pragma: no cover
        return SamplingStatisticsDocument.make_many(
            self.boto3_raw_data["SamplingStatisticsDocuments"]
        )

    @cached_property
    def SamplingBoostStatisticsDocuments(self):  # pragma: no cover
        return SamplingBoostStatisticsDocument.make_many(
            self.boto3_raw_data["SamplingBoostStatisticsDocuments"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSamplingTargetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSamplingTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTelemetryRecordsRequest:
    boto3_raw_data: "type_defs.PutTelemetryRecordsRequestTypeDef" = dataclasses.field()

    @cached_property
    def TelemetryRecords(self):  # pragma: no cover
        return TelemetryRecord.make_many(self.boto3_raw_data["TelemetryRecords"])

    EC2InstanceId = field("EC2InstanceId")
    Hostname = field("Hostname")
    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTelemetryRecordsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTelemetryRecordsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexingRule:
    boto3_raw_data: "type_defs.IndexingRuleTypeDef" = dataclasses.field()

    Name = field("Name")
    ModifiedAt = field("ModifiedAt")

    @cached_property
    def Rule(self):  # pragma: no cover
        return IndexingRuleValue.make_one(self.boto3_raw_data["Rule"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexingRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexingRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIndexingRuleRequest:
    boto3_raw_data: "type_defs.UpdateIndexingRuleRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Rule(self):  # pragma: no cover
        return IndexingRuleValueUpdate.make_one(self.boto3_raw_data["Rule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIndexingRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIndexingRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightImpactGraphResult:
    boto3_raw_data: "type_defs.GetInsightImpactGraphResultTypeDef" = dataclasses.field()

    InsightId = field("InsightId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    ServiceGraphStartTime = field("ServiceGraphStartTime")
    ServiceGraphEndTime = field("ServiceGraphEndTime")

    @cached_property
    def Services(self):  # pragma: no cover
        return InsightImpactGraphService.make_many(self.boto3_raw_data["Services"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightImpactGraphResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightImpactGraphResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseTimeRootCause:
    boto3_raw_data: "type_defs.ResponseTimeRootCauseTypeDef" = dataclasses.field()

    @cached_property
    def Services(self):  # pragma: no cover
        return ResponseTimeRootCauseService.make_many(self.boto3_raw_data["Services"])

    ClientImpacting = field("ClientImpacting")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseTimeRootCauseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseTimeRootCauseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRetrievedTracesResult:
    boto3_raw_data: "type_defs.ListRetrievedTracesResultTypeDef" = dataclasses.field()

    RetrievalStatus = field("RetrievalStatus")
    TraceFormat = field("TraceFormat")

    @cached_property
    def Traces(self):  # pragma: no cover
        return RetrievedTrace.make_many(self.boto3_raw_data["Traces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRetrievedTracesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRetrievedTracesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSamplingTargetsResult:
    boto3_raw_data: "type_defs.GetSamplingTargetsResultTypeDef" = dataclasses.field()

    @cached_property
    def SamplingTargetDocuments(self):  # pragma: no cover
        return SamplingTargetDocument.make_many(
            self.boto3_raw_data["SamplingTargetDocuments"]
        )

    LastRuleModification = field("LastRuleModification")

    @cached_property
    def UnprocessedStatistics(self):  # pragma: no cover
        return UnprocessedStatistics.make_many(
            self.boto3_raw_data["UnprocessedStatistics"]
        )

    @cached_property
    def UnprocessedBoostStatistics(self):  # pragma: no cover
        return UnprocessedStatistics.make_many(
            self.boto3_raw_data["UnprocessedBoostStatistics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSamplingTargetsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSamplingTargetsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamplingRuleRecord:
    boto3_raw_data: "type_defs.SamplingRuleRecordTypeDef" = dataclasses.field()

    @cached_property
    def SamplingRule(self):  # pragma: no cover
        return SamplingRuleOutput.make_one(self.boto3_raw_data["SamplingRule"])

    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SamplingRuleRecordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamplingRuleRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSamplingRuleRequest:
    boto3_raw_data: "type_defs.UpdateSamplingRuleRequestTypeDef" = dataclasses.field()

    @cached_property
    def SamplingRuleUpdate(self):  # pragma: no cover
        return SamplingRuleUpdate.make_one(self.boto3_raw_data["SamplingRuleUpdate"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSamplingRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSamplingRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetTracesResult:
    boto3_raw_data: "type_defs.BatchGetTracesResultTypeDef" = dataclasses.field()

    @cached_property
    def Traces(self):  # pragma: no cover
        return Trace.make_many(self.boto3_raw_data["Traces"])

    UnprocessedTraceIds = field("UnprocessedTraceIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetTracesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetTracesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightEventsResult:
    boto3_raw_data: "type_defs.GetInsightEventsResultTypeDef" = dataclasses.field()

    @cached_property
    def InsightEvents(self):  # pragma: no cover
        return InsightEvent.make_many(self.boto3_raw_data["InsightEvents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightEventsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightEventsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightSummariesResult:
    boto3_raw_data: "type_defs.GetInsightSummariesResultTypeDef" = dataclasses.field()

    @cached_property
    def InsightSummaries(self):  # pragma: no cover
        return InsightSummary.make_many(self.boto3_raw_data["InsightSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightSummariesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightSummariesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightResult:
    boto3_raw_data: "type_defs.GetInsightResultTypeDef" = dataclasses.field()

    @cached_property
    def Insight(self):  # pragma: no cover
        return Insight.make_one(self.boto3_raw_data["Insight"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetInsightResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Service:
    boto3_raw_data: "type_defs.ServiceTypeDef" = dataclasses.field()

    ReferenceId = field("ReferenceId")
    Name = field("Name")
    Names = field("Names")
    Root = field("Root")
    AccountId = field("AccountId")
    Type = field("Type")
    State = field("State")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def Edges(self):  # pragma: no cover
        return Edge.make_many(self.boto3_raw_data["Edges"])

    @cached_property
    def SummaryStatistics(self):  # pragma: no cover
        return ServiceStatistics.make_one(self.boto3_raw_data["SummaryStatistics"])

    @cached_property
    def DurationHistogram(self):  # pragma: no cover
        return HistogramEntry.make_many(self.boto3_raw_data["DurationHistogram"])

    @cached_property
    def ResponseTimeHistogram(self):  # pragma: no cover
        return HistogramEntry.make_many(self.boto3_raw_data["ResponseTimeHistogram"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTimeSeriesServiceStatisticsResult:
    boto3_raw_data: "type_defs.GetTimeSeriesServiceStatisticsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimeSeriesServiceStatistics(self):  # pragma: no cover
        return TimeSeriesServiceStatistics.make_many(
            self.boto3_raw_data["TimeSeriesServiceStatistics"]
        )

    ContainsOldGroupVersions = field("ContainsOldGroupVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTimeSeriesServiceStatisticsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTimeSeriesServiceStatisticsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorRootCause:
    boto3_raw_data: "type_defs.ErrorRootCauseTypeDef" = dataclasses.field()

    @cached_property
    def Services(self):  # pragma: no cover
        return ErrorRootCauseService.make_many(self.boto3_raw_data["Services"])

    ClientImpacting = field("ClientImpacting")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorRootCauseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorRootCauseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaultRootCause:
    boto3_raw_data: "type_defs.FaultRootCauseTypeDef" = dataclasses.field()

    @cached_property
    def Services(self):  # pragma: no cover
        return FaultRootCauseService.make_many(self.boto3_raw_data["Services"])

    ClientImpacting = field("ClientImpacting")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FaultRootCauseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FaultRootCauseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIndexingRulesResult:
    boto3_raw_data: "type_defs.GetIndexingRulesResultTypeDef" = dataclasses.field()

    @cached_property
    def IndexingRules(self):  # pragma: no cover
        return IndexingRule.make_many(self.boto3_raw_data["IndexingRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIndexingRulesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIndexingRulesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIndexingRuleResult:
    boto3_raw_data: "type_defs.UpdateIndexingRuleResultTypeDef" = dataclasses.field()

    @cached_property
    def IndexingRule(self):  # pragma: no cover
        return IndexingRule.make_one(self.boto3_raw_data["IndexingRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIndexingRuleResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIndexingRuleResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSamplingRuleResult:
    boto3_raw_data: "type_defs.CreateSamplingRuleResultTypeDef" = dataclasses.field()

    @cached_property
    def SamplingRuleRecord(self):  # pragma: no cover
        return SamplingRuleRecord.make_one(self.boto3_raw_data["SamplingRuleRecord"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSamplingRuleResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSamplingRuleResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSamplingRuleResult:
    boto3_raw_data: "type_defs.DeleteSamplingRuleResultTypeDef" = dataclasses.field()

    @cached_property
    def SamplingRuleRecord(self):  # pragma: no cover
        return SamplingRuleRecord.make_one(self.boto3_raw_data["SamplingRuleRecord"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSamplingRuleResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSamplingRuleResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSamplingRulesResult:
    boto3_raw_data: "type_defs.GetSamplingRulesResultTypeDef" = dataclasses.field()

    @cached_property
    def SamplingRuleRecords(self):  # pragma: no cover
        return SamplingRuleRecord.make_many(self.boto3_raw_data["SamplingRuleRecords"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSamplingRulesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSamplingRulesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSamplingRuleResult:
    boto3_raw_data: "type_defs.UpdateSamplingRuleResultTypeDef" = dataclasses.field()

    @cached_property
    def SamplingRuleRecord(self):  # pragma: no cover
        return SamplingRuleRecord.make_one(self.boto3_raw_data["SamplingRuleRecord"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSamplingRuleResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSamplingRuleResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSamplingRuleRequest:
    boto3_raw_data: "type_defs.CreateSamplingRuleRequestTypeDef" = dataclasses.field()

    SamplingRule = field("SamplingRule")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSamplingRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSamplingRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceGraphResult:
    boto3_raw_data: "type_defs.GetServiceGraphResultTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def Services(self):  # pragma: no cover
        return Service.make_many(self.boto3_raw_data["Services"])

    ContainsOldGroupVersions = field("ContainsOldGroupVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceGraphResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceGraphResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTraceGraphResult:
    boto3_raw_data: "type_defs.GetTraceGraphResultTypeDef" = dataclasses.field()

    @cached_property
    def Services(self):  # pragma: no cover
        return Service.make_many(self.boto3_raw_data["Services"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTraceGraphResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTraceGraphResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievedService:
    boto3_raw_data: "type_defs.RetrievedServiceTypeDef" = dataclasses.field()

    @cached_property
    def Service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["Service"])

    @cached_property
    def Links(self):  # pragma: no cover
        return GraphLink.make_many(self.boto3_raw_data["Links"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetrievedServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievedServiceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TraceSummary:
    boto3_raw_data: "type_defs.TraceSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    StartTime = field("StartTime")
    Duration = field("Duration")
    ResponseTime = field("ResponseTime")
    HasFault = field("HasFault")
    HasError = field("HasError")
    HasThrottle = field("HasThrottle")
    IsPartial = field("IsPartial")

    @cached_property
    def Http(self):  # pragma: no cover
        return Http.make_one(self.boto3_raw_data["Http"])

    Annotations = field("Annotations")

    @cached_property
    def Users(self):  # pragma: no cover
        return TraceUser.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ServiceIds(self):  # pragma: no cover
        return ServiceId.make_many(self.boto3_raw_data["ServiceIds"])

    @cached_property
    def ResourceARNs(self):  # pragma: no cover
        return ResourceARNDetail.make_many(self.boto3_raw_data["ResourceARNs"])

    @cached_property
    def InstanceIds(self):  # pragma: no cover
        return InstanceIdDetail.make_many(self.boto3_raw_data["InstanceIds"])

    @cached_property
    def AvailabilityZones(self):  # pragma: no cover
        return AvailabilityZoneDetail.make_many(
            self.boto3_raw_data["AvailabilityZones"]
        )

    @cached_property
    def EntryPoint(self):  # pragma: no cover
        return ServiceId.make_one(self.boto3_raw_data["EntryPoint"])

    @cached_property
    def FaultRootCauses(self):  # pragma: no cover
        return FaultRootCause.make_many(self.boto3_raw_data["FaultRootCauses"])

    @cached_property
    def ErrorRootCauses(self):  # pragma: no cover
        return ErrorRootCause.make_many(self.boto3_raw_data["ErrorRootCauses"])

    @cached_property
    def ResponseTimeRootCauses(self):  # pragma: no cover
        return ResponseTimeRootCause.make_many(
            self.boto3_raw_data["ResponseTimeRootCauses"]
        )

    Revision = field("Revision")
    MatchedEventTime = field("MatchedEventTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TraceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TraceSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRetrievedTracesGraphResult:
    boto3_raw_data: "type_defs.GetRetrievedTracesGraphResultTypeDef" = (
        dataclasses.field()
    )

    RetrievalStatus = field("RetrievalStatus")

    @cached_property
    def Services(self):  # pragma: no cover
        return RetrievedService.make_many(self.boto3_raw_data["Services"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRetrievedTracesGraphResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRetrievedTracesGraphResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTraceSummariesResult:
    boto3_raw_data: "type_defs.GetTraceSummariesResultTypeDef" = dataclasses.field()

    @cached_property
    def TraceSummaries(self):  # pragma: no cover
        return TraceSummary.make_many(self.boto3_raw_data["TraceSummaries"])

    ApproximateTime = field("ApproximateTime")
    TracesProcessedCount = field("TracesProcessedCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTraceSummariesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTraceSummariesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
