# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_internetmonitor import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AvailabilityMeasurement:
    boto3_raw_data: "type_defs.AvailabilityMeasurementTypeDef" = dataclasses.field()

    ExperienceScore = field("ExperienceScore")
    PercentOfTotalTrafficImpacted = field("PercentOfTotalTrafficImpacted")
    PercentOfClientLocationImpacted = field("PercentOfClientLocationImpacted")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailabilityMeasurementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityMeasurementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientLocation:
    boto3_raw_data: "type_defs.ClientLocationTypeDef" = dataclasses.field()

    ASName = field("ASName")
    ASNumber = field("ASNumber")
    Country = field("Country")
    City = field("City")
    Latitude = field("Latitude")
    Longitude = field("Longitude")
    Subdivision = field("Subdivision")
    Metro = field("Metro")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClientLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClientLocationTypeDef"]],
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
class DeleteMonitorInput:
    boto3_raw_data: "type_defs.DeleteMonitorInputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMonitorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMonitorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterParameter:
    boto3_raw_data: "type_defs.FilterParameterTypeDef" = dataclasses.field()

    Field = field("Field")
    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterParameterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHealthEventInput:
    boto3_raw_data: "type_defs.GetHealthEventInputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    EventId = field("EventId")
    LinkedAccountId = field("LinkedAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHealthEventInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHealthEventInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInternetEventInput:
    boto3_raw_data: "type_defs.GetInternetEventInputTypeDef" = dataclasses.field()

    EventId = field("EventId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInternetEventInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInternetEventInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMonitorInput:
    boto3_raw_data: "type_defs.GetMonitorInputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    LinkedAccountId = field("LinkedAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMonitorInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetMonitorInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsInput:
    boto3_raw_data: "type_defs.GetQueryResultsInputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    QueryId = field("QueryId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryResultsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryField:
    boto3_raw_data: "type_defs.QueryFieldTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryFieldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStatusInput:
    boto3_raw_data: "type_defs.GetQueryStatusInputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    QueryId = field("QueryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryStatusInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalHealthEventsConfig:
    boto3_raw_data: "type_defs.LocalHealthEventsConfigTypeDef" = dataclasses.field()

    Status = field("Status")
    HealthScoreThreshold = field("HealthScoreThreshold")
    MinTrafficImpact = field("MinTrafficImpact")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LocalHealthEventsConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocalHealthEventsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Config:
    boto3_raw_data: "type_defs.S3ConfigTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    BucketPrefix = field("BucketPrefix")
    LogDeliveryStatus = field("LogDeliveryStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigTypeDef"]]
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
class ListMonitorsInput:
    boto3_raw_data: "type_defs.ListMonitorsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    MonitorStatus = field("MonitorStatus")
    IncludeLinkedAccounts = field("IncludeLinkedAccounts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Monitor:
    boto3_raw_data: "type_defs.MonitorTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    MonitorArn = field("MonitorArn")
    Status = field("Status")
    ProcessingStatus = field("ProcessingStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonitorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonitorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

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
class Network:
    boto3_raw_data: "type_defs.NetworkTypeDef" = dataclasses.field()

    ASName = field("ASName")
    ASNumber = field("ASNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoundTripTime:
    boto3_raw_data: "type_defs.RoundTripTimeTypeDef" = dataclasses.field()

    P50 = field("P50")
    P90 = field("P90")
    P95 = field("P95")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoundTripTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoundTripTimeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopQueryInput:
    boto3_raw_data: "type_defs.StopQueryInputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    QueryId = field("QueryId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopQueryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopQueryInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class InternetEventSummary:
    boto3_raw_data: "type_defs.InternetEventSummaryTypeDef" = dataclasses.field()

    EventId = field("EventId")
    EventArn = field("EventArn")
    StartedAt = field("StartedAt")

    @cached_property
    def ClientLocation(self):  # pragma: no cover
        return ClientLocation.make_one(self.boto3_raw_data["ClientLocation"])

    EventType = field("EventType")
    EventStatus = field("EventStatus")
    EndedAt = field("EndedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InternetEventSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternetEventSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMonitorOutput:
    boto3_raw_data: "type_defs.CreateMonitorOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMonitorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMonitorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInternetEventOutput:
    boto3_raw_data: "type_defs.GetInternetEventOutputTypeDef" = dataclasses.field()

    EventId = field("EventId")
    EventArn = field("EventArn")
    StartedAt = field("StartedAt")
    EndedAt = field("EndedAt")

    @cached_property
    def ClientLocation(self):  # pragma: no cover
        return ClientLocation.make_one(self.boto3_raw_data["ClientLocation"])

    EventType = field("EventType")
    EventStatus = field("EventStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInternetEventOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInternetEventOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStatusOutput:
    boto3_raw_data: "type_defs.GetQueryStatusOutputTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryStatusOutputTypeDef"]
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

    Tags = field("Tags")

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
class StartQueryOutput:
    boto3_raw_data: "type_defs.StartQueryOutputTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartQueryOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMonitorOutput:
    boto3_raw_data: "type_defs.UpdateMonitorOutputTypeDef" = dataclasses.field()

    MonitorArn = field("MonitorArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMonitorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMonitorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsOutput:
    boto3_raw_data: "type_defs.GetQueryResultsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Fields(self):  # pragma: no cover
        return QueryField.make_many(self.boto3_raw_data["Fields"])

    Data = field("Data")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryResultsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthEventsConfig:
    boto3_raw_data: "type_defs.HealthEventsConfigTypeDef" = dataclasses.field()

    AvailabilityScoreThreshold = field("AvailabilityScoreThreshold")
    PerformanceScoreThreshold = field("PerformanceScoreThreshold")

    @cached_property
    def AvailabilityLocalHealthEventsConfig(self):  # pragma: no cover
        return LocalHealthEventsConfig.make_one(
            self.boto3_raw_data["AvailabilityLocalHealthEventsConfig"]
        )

    @cached_property
    def PerformanceLocalHealthEventsConfig(self):  # pragma: no cover
        return LocalHealthEventsConfig.make_one(
            self.boto3_raw_data["PerformanceLocalHealthEventsConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HealthEventsConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HealthEventsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternetMeasurementsLogDelivery:
    boto3_raw_data: "type_defs.InternetMeasurementsLogDeliveryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["S3Config"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InternetMeasurementsLogDeliveryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternetMeasurementsLogDeliveryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsInputPaginate:
    boto3_raw_data: "type_defs.ListMonitorsInputPaginateTypeDef" = dataclasses.field()

    MonitorStatus = field("MonitorStatus")
    IncludeLinkedAccounts = field("IncludeLinkedAccounts")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHealthEventsInputPaginate:
    boto3_raw_data: "type_defs.ListHealthEventsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    MonitorName = field("MonitorName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    EventStatus = field("EventStatus")
    LinkedAccountId = field("LinkedAccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListHealthEventsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHealthEventsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHealthEventsInput:
    boto3_raw_data: "type_defs.ListHealthEventsInputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    EventStatus = field("EventStatus")
    LinkedAccountId = field("LinkedAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHealthEventsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHealthEventsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInternetEventsInputPaginate:
    boto3_raw_data: "type_defs.ListInternetEventsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    EventStatus = field("EventStatus")
    EventType = field("EventType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInternetEventsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInternetEventsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInternetEventsInput:
    boto3_raw_data: "type_defs.ListInternetEventsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    EventStatus = field("EventStatus")
    EventType = field("EventType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInternetEventsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInternetEventsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryInput:
    boto3_raw_data: "type_defs.StartQueryInputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    QueryType = field("QueryType")

    @cached_property
    def FilterParameters(self):  # pragma: no cover
        return FilterParameter.make_many(self.boto3_raw_data["FilterParameters"])

    LinkedAccountId = field("LinkedAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartQueryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartQueryInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsOutput:
    boto3_raw_data: "type_defs.ListMonitorsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Monitors(self):  # pragma: no cover
        return Monitor.make_many(self.boto3_raw_data["Monitors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkImpairment:
    boto3_raw_data: "type_defs.NetworkImpairmentTypeDef" = dataclasses.field()

    @cached_property
    def Networks(self):  # pragma: no cover
        return Network.make_many(self.boto3_raw_data["Networks"])

    @cached_property
    def AsPath(self):  # pragma: no cover
        return Network.make_many(self.boto3_raw_data["AsPath"])

    NetworkEventType = field("NetworkEventType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkImpairmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkImpairmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceMeasurement:
    boto3_raw_data: "type_defs.PerformanceMeasurementTypeDef" = dataclasses.field()

    ExperienceScore = field("ExperienceScore")
    PercentOfTotalTrafficImpacted = field("PercentOfTotalTrafficImpacted")
    PercentOfClientLocationImpacted = field("PercentOfClientLocationImpacted")

    @cached_property
    def RoundTripTime(self):  # pragma: no cover
        return RoundTripTime.make_one(self.boto3_raw_data["RoundTripTime"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PerformanceMeasurementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceMeasurementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInternetEventsOutput:
    boto3_raw_data: "type_defs.ListInternetEventsOutputTypeDef" = dataclasses.field()

    @cached_property
    def InternetEvents(self):  # pragma: no cover
        return InternetEventSummary.make_many(self.boto3_raw_data["InternetEvents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInternetEventsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInternetEventsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMonitorInput:
    boto3_raw_data: "type_defs.CreateMonitorInputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    Resources = field("Resources")
    ClientToken = field("ClientToken")
    Tags = field("Tags")
    MaxCityNetworksToMonitor = field("MaxCityNetworksToMonitor")

    @cached_property
    def InternetMeasurementsLogDelivery(self):  # pragma: no cover
        return InternetMeasurementsLogDelivery.make_one(
            self.boto3_raw_data["InternetMeasurementsLogDelivery"]
        )

    TrafficPercentageToMonitor = field("TrafficPercentageToMonitor")

    @cached_property
    def HealthEventsConfig(self):  # pragma: no cover
        return HealthEventsConfig.make_one(self.boto3_raw_data["HealthEventsConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMonitorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMonitorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMonitorOutput:
    boto3_raw_data: "type_defs.GetMonitorOutputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    MonitorArn = field("MonitorArn")
    Resources = field("Resources")
    Status = field("Status")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    ProcessingStatus = field("ProcessingStatus")
    ProcessingStatusInfo = field("ProcessingStatusInfo")
    Tags = field("Tags")
    MaxCityNetworksToMonitor = field("MaxCityNetworksToMonitor")

    @cached_property
    def InternetMeasurementsLogDelivery(self):  # pragma: no cover
        return InternetMeasurementsLogDelivery.make_one(
            self.boto3_raw_data["InternetMeasurementsLogDelivery"]
        )

    TrafficPercentageToMonitor = field("TrafficPercentageToMonitor")

    @cached_property
    def HealthEventsConfig(self):  # pragma: no cover
        return HealthEventsConfig.make_one(self.boto3_raw_data["HealthEventsConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMonitorOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMonitorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMonitorInput:
    boto3_raw_data: "type_defs.UpdateMonitorInputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    ResourcesToAdd = field("ResourcesToAdd")
    ResourcesToRemove = field("ResourcesToRemove")
    Status = field("Status")
    ClientToken = field("ClientToken")
    MaxCityNetworksToMonitor = field("MaxCityNetworksToMonitor")

    @cached_property
    def InternetMeasurementsLogDelivery(self):  # pragma: no cover
        return InternetMeasurementsLogDelivery.make_one(
            self.boto3_raw_data["InternetMeasurementsLogDelivery"]
        )

    TrafficPercentageToMonitor = field("TrafficPercentageToMonitor")

    @cached_property
    def HealthEventsConfig(self):  # pragma: no cover
        return HealthEventsConfig.make_one(self.boto3_raw_data["HealthEventsConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMonitorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMonitorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternetHealth:
    boto3_raw_data: "type_defs.InternetHealthTypeDef" = dataclasses.field()

    @cached_property
    def Availability(self):  # pragma: no cover
        return AvailabilityMeasurement.make_one(self.boto3_raw_data["Availability"])

    @cached_property
    def Performance(self):  # pragma: no cover
        return PerformanceMeasurement.make_one(self.boto3_raw_data["Performance"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InternetHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InternetHealthTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImpactedLocation:
    boto3_raw_data: "type_defs.ImpactedLocationTypeDef" = dataclasses.field()

    ASName = field("ASName")
    ASNumber = field("ASNumber")
    Country = field("Country")
    Status = field("Status")
    Subdivision = field("Subdivision")
    Metro = field("Metro")
    City = field("City")
    Latitude = field("Latitude")
    Longitude = field("Longitude")
    CountryCode = field("CountryCode")
    SubdivisionCode = field("SubdivisionCode")
    ServiceLocation = field("ServiceLocation")

    @cached_property
    def CausedBy(self):  # pragma: no cover
        return NetworkImpairment.make_one(self.boto3_raw_data["CausedBy"])

    @cached_property
    def InternetHealth(self):  # pragma: no cover
        return InternetHealth.make_one(self.boto3_raw_data["InternetHealth"])

    Ipv4Prefixes = field("Ipv4Prefixes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImpactedLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImpactedLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHealthEventOutput:
    boto3_raw_data: "type_defs.GetHealthEventOutputTypeDef" = dataclasses.field()

    EventArn = field("EventArn")
    EventId = field("EventId")
    StartedAt = field("StartedAt")
    EndedAt = field("EndedAt")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")

    @cached_property
    def ImpactedLocations(self):  # pragma: no cover
        return ImpactedLocation.make_many(self.boto3_raw_data["ImpactedLocations"])

    Status = field("Status")
    PercentOfTotalTrafficImpacted = field("PercentOfTotalTrafficImpacted")
    ImpactType = field("ImpactType")
    HealthScoreThreshold = field("HealthScoreThreshold")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHealthEventOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHealthEventOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthEvent:
    boto3_raw_data: "type_defs.HealthEventTypeDef" = dataclasses.field()

    EventArn = field("EventArn")
    EventId = field("EventId")
    StartedAt = field("StartedAt")
    LastUpdatedAt = field("LastUpdatedAt")

    @cached_property
    def ImpactedLocations(self):  # pragma: no cover
        return ImpactedLocation.make_many(self.boto3_raw_data["ImpactedLocations"])

    Status = field("Status")
    ImpactType = field("ImpactType")
    EndedAt = field("EndedAt")
    CreatedAt = field("CreatedAt")
    PercentOfTotalTrafficImpacted = field("PercentOfTotalTrafficImpacted")
    HealthScoreThreshold = field("HealthScoreThreshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HealthEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HealthEventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHealthEventsOutput:
    boto3_raw_data: "type_defs.ListHealthEventsOutputTypeDef" = dataclasses.field()

    @cached_property
    def HealthEvents(self):  # pragma: no cover
        return HealthEvent.make_many(self.boto3_raw_data["HealthEvents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHealthEventsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHealthEventsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
