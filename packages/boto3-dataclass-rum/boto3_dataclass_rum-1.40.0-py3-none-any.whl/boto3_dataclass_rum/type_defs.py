# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rum import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AppMonitorConfigurationOutput:
    boto3_raw_data: "type_defs.AppMonitorConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    AllowCookies = field("AllowCookies")
    EnableXRay = field("EnableXRay")
    ExcludedPages = field("ExcludedPages")
    FavoritePages = field("FavoritePages")
    GuestRoleArn = field("GuestRoleArn")
    IdentityPoolId = field("IdentityPoolId")
    IncludedPages = field("IncludedPages")
    SessionSampleRate = field("SessionSampleRate")
    Telemetries = field("Telemetries")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AppMonitorConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppMonitorConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppMonitorConfiguration:
    boto3_raw_data: "type_defs.AppMonitorConfigurationTypeDef" = dataclasses.field()

    AllowCookies = field("AllowCookies")
    EnableXRay = field("EnableXRay")
    ExcludedPages = field("ExcludedPages")
    FavoritePages = field("FavoritePages")
    GuestRoleArn = field("GuestRoleArn")
    IdentityPoolId = field("IdentityPoolId")
    IncludedPages = field("IncludedPages")
    SessionSampleRate = field("SessionSampleRate")
    Telemetries = field("Telemetries")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppMonitorConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppMonitorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppMonitorDetails:
    boto3_raw_data: "type_defs.AppMonitorDetailsTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppMonitorDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppMonitorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppMonitorSummary:
    boto3_raw_data: "type_defs.AppMonitorSummaryTypeDef" = dataclasses.field()

    Created = field("Created")
    Id = field("Id")
    LastModified = field("LastModified")
    Name = field("Name")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppMonitorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppMonitorSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomEvents:
    boto3_raw_data: "type_defs.CustomEventsTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomEventsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomEventsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDefinitionRequestOutput:
    boto3_raw_data: "type_defs.MetricDefinitionRequestOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    DimensionKeys = field("DimensionKeys")
    EventPattern = field("EventPattern")
    Namespace = field("Namespace")
    UnitLabel = field("UnitLabel")
    ValueKey = field("ValueKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MetricDefinitionRequestOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDefinitionRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDefinition:
    boto3_raw_data: "type_defs.MetricDefinitionTypeDef" = dataclasses.field()

    MetricDefinitionId = field("MetricDefinitionId")
    Name = field("Name")
    DimensionKeys = field("DimensionKeys")
    EventPattern = field("EventPattern")
    Namespace = field("Namespace")
    UnitLabel = field("UnitLabel")
    ValueKey = field("ValueKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDefinitionTypeDef"]
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
class BatchDeleteRumMetricDefinitionsError:
    boto3_raw_data: "type_defs.BatchDeleteRumMetricDefinitionsErrorTypeDef" = (
        dataclasses.field()
    )

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    MetricDefinitionId = field("MetricDefinitionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteRumMetricDefinitionsErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteRumMetricDefinitionsErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteRumMetricDefinitionsRequest:
    boto3_raw_data: "type_defs.BatchDeleteRumMetricDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    AppMonitorName = field("AppMonitorName")
    Destination = field("Destination")
    MetricDefinitionIds = field("MetricDefinitionIds")
    DestinationArn = field("DestinationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteRumMetricDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteRumMetricDefinitionsRequestTypeDef"]
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
class BatchGetRumMetricDefinitionsRequest:
    boto3_raw_data: "type_defs.BatchGetRumMetricDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    AppMonitorName = field("AppMonitorName")
    Destination = field("Destination")
    DestinationArn = field("DestinationArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetRumMetricDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRumMetricDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CwLog:
    boto3_raw_data: "type_defs.CwLogTypeDef" = dataclasses.field()

    CwLogEnabled = field("CwLogEnabled")
    CwLogGroup = field("CwLogGroup")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CwLogTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CwLogTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppMonitorRequest:
    boto3_raw_data: "type_defs.DeleteAppMonitorRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAppMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppMonitorRequestTypeDef"]
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

    Name = field("Name")
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
class DeleteRumMetricsDestinationRequest:
    boto3_raw_data: "type_defs.DeleteRumMetricsDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    AppMonitorName = field("AppMonitorName")
    Destination = field("Destination")
    DestinationArn = field("DestinationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRumMetricsDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRumMetricsDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JavaScriptSourceMaps:
    boto3_raw_data: "type_defs.JavaScriptSourceMapsTypeDef" = dataclasses.field()

    Status = field("Status")
    S3Uri = field("S3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JavaScriptSourceMapsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JavaScriptSourceMapsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryFilter:
    boto3_raw_data: "type_defs.QueryFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeRange:
    boto3_raw_data: "type_defs.TimeRangeTypeDef" = dataclasses.field()

    After = field("After")
    Before = field("Before")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppMonitorRequest:
    boto3_raw_data: "type_defs.GetAppMonitorRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAppMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyRequest:
    boto3_raw_data: "type_defs.GetResourcePolicyRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppMonitorsRequest:
    boto3_raw_data: "type_defs.ListAppMonitorsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppMonitorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppMonitorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRumMetricsDestinationsRequest:
    boto3_raw_data: "type_defs.ListRumMetricsDestinationsRequestTypeDef" = (
        dataclasses.field()
    )

    AppMonitorName = field("AppMonitorName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRumMetricsDestinationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRumMetricsDestinationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDestinationSummary:
    boto3_raw_data: "type_defs.MetricDestinationSummaryTypeDef" = dataclasses.field()

    Destination = field("Destination")
    DestinationArn = field("DestinationArn")
    IamRoleArn = field("IamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricDestinationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDestinationSummaryTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class MetricDefinitionRequest:
    boto3_raw_data: "type_defs.MetricDefinitionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    DimensionKeys = field("DimensionKeys")
    EventPattern = field("EventPattern")
    Namespace = field("Namespace")
    UnitLabel = field("UnitLabel")
    ValueKey = field("ValueKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDefinitionRequestTypeDef"]
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

    Name = field("Name")
    PolicyDocument = field("PolicyDocument")
    PolicyRevisionId = field("PolicyRevisionId")

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
class UserDetails:
    boto3_raw_data: "type_defs.UserDetailsTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    userId = field("userId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRumMetricsDestinationRequest:
    boto3_raw_data: "type_defs.PutRumMetricsDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    AppMonitorName = field("AppMonitorName")
    Destination = field("Destination")
    DestinationArn = field("DestinationArn")
    IamRoleArn = field("IamRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutRumMetricsDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRumMetricsDestinationRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
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
class BatchCreateRumMetricDefinitionsError:
    boto3_raw_data: "type_defs.BatchCreateRumMetricDefinitionsErrorTypeDef" = (
        dataclasses.field()
    )

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @cached_property
    def MetricDefinition(self):  # pragma: no cover
        return MetricDefinitionRequestOutput.make_one(
            self.boto3_raw_data["MetricDefinition"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateRumMetricDefinitionsErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateRumMetricDefinitionsErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRumMetricDefinitionsResponse:
    boto3_raw_data: "type_defs.BatchGetRumMetricDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricDefinitions(self):  # pragma: no cover
        return MetricDefinition.make_many(self.boto3_raw_data["MetricDefinitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetRumMetricDefinitionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRumMetricDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppMonitorResponse:
    boto3_raw_data: "type_defs.CreateAppMonitorResponseTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAppMonitorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppMonitorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyResponse:
    boto3_raw_data: "type_defs.DeleteResourcePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    PolicyRevisionId = field("PolicyRevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppMonitorDataResponse:
    boto3_raw_data: "type_defs.GetAppMonitorDataResponseTypeDef" = dataclasses.field()

    Events = field("Events")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAppMonitorDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppMonitorDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyResponse:
    boto3_raw_data: "type_defs.GetResourcePolicyResponseTypeDef" = dataclasses.field()

    PolicyDocument = field("PolicyDocument")
    PolicyRevisionId = field("PolicyRevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppMonitorsResponse:
    boto3_raw_data: "type_defs.ListAppMonitorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def AppMonitorSummaries(self):  # pragma: no cover
        return AppMonitorSummary.make_many(self.boto3_raw_data["AppMonitorSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppMonitorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppMonitorsResponseTypeDef"]
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

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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
class PutResourcePolicyResponse:
    boto3_raw_data: "type_defs.PutResourcePolicyResponseTypeDef" = dataclasses.field()

    PolicyDocument = field("PolicyDocument")
    PolicyRevisionId = field("PolicyRevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteRumMetricDefinitionsResponse:
    boto3_raw_data: "type_defs.BatchDeleteRumMetricDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchDeleteRumMetricDefinitionsError.make_many(
            self.boto3_raw_data["Errors"]
        )

    MetricDefinitionIds = field("MetricDefinitionIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteRumMetricDefinitionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteRumMetricDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRumMetricDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.BatchGetRumMetricDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AppMonitorName = field("AppMonitorName")
    Destination = field("Destination")
    DestinationArn = field("DestinationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetRumMetricDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRumMetricDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppMonitorsRequestPaginate:
    boto3_raw_data: "type_defs.ListAppMonitorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAppMonitorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppMonitorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRumMetricsDestinationsRequestPaginate:
    boto3_raw_data: "type_defs.ListRumMetricsDestinationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AppMonitorName = field("AppMonitorName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRumMetricsDestinationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRumMetricsDestinationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataStorage:
    boto3_raw_data: "type_defs.DataStorageTypeDef" = dataclasses.field()

    @cached_property
    def CwLog(self):  # pragma: no cover
        return CwLog.make_one(self.boto3_raw_data["CwLog"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataStorageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataStorageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeobfuscationConfiguration:
    boto3_raw_data: "type_defs.DeobfuscationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def JavaScriptSourceMaps(self):  # pragma: no cover
        return JavaScriptSourceMaps.make_one(
            self.boto3_raw_data["JavaScriptSourceMaps"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeobfuscationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeobfuscationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppMonitorDataRequestPaginate:
    boto3_raw_data: "type_defs.GetAppMonitorDataRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def TimeRange(self):  # pragma: no cover
        return TimeRange.make_one(self.boto3_raw_data["TimeRange"])

    @cached_property
    def Filters(self):  # pragma: no cover
        return QueryFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAppMonitorDataRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppMonitorDataRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppMonitorDataRequest:
    boto3_raw_data: "type_defs.GetAppMonitorDataRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def TimeRange(self):  # pragma: no cover
        return TimeRange.make_one(self.boto3_raw_data["TimeRange"])

    @cached_property
    def Filters(self):  # pragma: no cover
        return QueryFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAppMonitorDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppMonitorDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRumMetricsDestinationsResponse:
    boto3_raw_data: "type_defs.ListRumMetricsDestinationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Destinations(self):  # pragma: no cover
        return MetricDestinationSummary.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRumMetricsDestinationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRumMetricsDestinationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RumEvent:
    boto3_raw_data: "type_defs.RumEventTypeDef" = dataclasses.field()

    details = field("details")
    id = field("id")
    timestamp = field("timestamp")
    type = field("type")
    metadata = field("metadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RumEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RumEventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateRumMetricDefinitionsResponse:
    boto3_raw_data: "type_defs.BatchCreateRumMetricDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchCreateRumMetricDefinitionsError.make_many(
            self.boto3_raw_data["Errors"]
        )

    @cached_property
    def MetricDefinitions(self):  # pragma: no cover
        return MetricDefinition.make_many(self.boto3_raw_data["MetricDefinitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateRumMetricDefinitionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateRumMetricDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppMonitor:
    boto3_raw_data: "type_defs.AppMonitorTypeDef" = dataclasses.field()

    @cached_property
    def AppMonitorConfiguration(self):  # pragma: no cover
        return AppMonitorConfigurationOutput.make_one(
            self.boto3_raw_data["AppMonitorConfiguration"]
        )

    Created = field("Created")

    @cached_property
    def CustomEvents(self):  # pragma: no cover
        return CustomEvents.make_one(self.boto3_raw_data["CustomEvents"])

    @cached_property
    def DataStorage(self):  # pragma: no cover
        return DataStorage.make_one(self.boto3_raw_data["DataStorage"])

    @cached_property
    def DeobfuscationConfiguration(self):  # pragma: no cover
        return DeobfuscationConfiguration.make_one(
            self.boto3_raw_data["DeobfuscationConfiguration"]
        )

    Domain = field("Domain")
    DomainList = field("DomainList")
    Id = field("Id")
    LastModified = field("LastModified")
    Name = field("Name")
    State = field("State")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppMonitorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppMonitorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppMonitorRequest:
    boto3_raw_data: "type_defs.CreateAppMonitorRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    AppMonitorConfiguration = field("AppMonitorConfiguration")

    @cached_property
    def CustomEvents(self):  # pragma: no cover
        return CustomEvents.make_one(self.boto3_raw_data["CustomEvents"])

    CwLogEnabled = field("CwLogEnabled")

    @cached_property
    def DeobfuscationConfiguration(self):  # pragma: no cover
        return DeobfuscationConfiguration.make_one(
            self.boto3_raw_data["DeobfuscationConfiguration"]
        )

    Domain = field("Domain")
    DomainList = field("DomainList")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAppMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppMonitorRequest:
    boto3_raw_data: "type_defs.UpdateAppMonitorRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    AppMonitorConfiguration = field("AppMonitorConfiguration")

    @cached_property
    def CustomEvents(self):  # pragma: no cover
        return CustomEvents.make_one(self.boto3_raw_data["CustomEvents"])

    CwLogEnabled = field("CwLogEnabled")

    @cached_property
    def DeobfuscationConfiguration(self):  # pragma: no cover
        return DeobfuscationConfiguration.make_one(
            self.boto3_raw_data["DeobfuscationConfiguration"]
        )

    Domain = field("Domain")
    DomainList = field("DomainList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAppMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateRumMetricDefinitionsRequest:
    boto3_raw_data: "type_defs.BatchCreateRumMetricDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    AppMonitorName = field("AppMonitorName")
    Destination = field("Destination")
    MetricDefinitions = field("MetricDefinitions")
    DestinationArn = field("DestinationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateRumMetricDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateRumMetricDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRumMetricDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateRumMetricDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    AppMonitorName = field("AppMonitorName")
    Destination = field("Destination")
    MetricDefinition = field("MetricDefinition")
    MetricDefinitionId = field("MetricDefinitionId")
    DestinationArn = field("DestinationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRumMetricDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRumMetricDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRumEventsRequest:
    boto3_raw_data: "type_defs.PutRumEventsRequestTypeDef" = dataclasses.field()

    @cached_property
    def AppMonitorDetails(self):  # pragma: no cover
        return AppMonitorDetails.make_one(self.boto3_raw_data["AppMonitorDetails"])

    BatchId = field("BatchId")
    Id = field("Id")

    @cached_property
    def RumEvents(self):  # pragma: no cover
        return RumEvent.make_many(self.boto3_raw_data["RumEvents"])

    @cached_property
    def UserDetails(self):  # pragma: no cover
        return UserDetails.make_one(self.boto3_raw_data["UserDetails"])

    Alias = field("Alias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRumEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRumEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppMonitorResponse:
    boto3_raw_data: "type_defs.GetAppMonitorResponseTypeDef" = dataclasses.field()

    @cached_property
    def AppMonitor(self):  # pragma: no cover
        return AppMonitor.make_one(self.boto3_raw_data["AppMonitor"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAppMonitorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppMonitorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
