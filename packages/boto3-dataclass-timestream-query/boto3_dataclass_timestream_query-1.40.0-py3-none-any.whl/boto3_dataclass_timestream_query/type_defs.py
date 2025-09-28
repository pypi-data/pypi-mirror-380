# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_timestream_query import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class SnsConfiguration:
    boto3_raw_data: "type_defs.SnsConfigurationTypeDef" = dataclasses.field()

    TopicArn = field("TopicArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnsConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelQueryRequest:
    boto3_raw_data: "type_defs.CancelQueryRequestTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelQueryRequestTypeDef"]
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
class TypePaginator:
    boto3_raw_data: "type_defs.TypePaginatorTypeDef" = dataclasses.field()

    ScalarType = field("ScalarType")
    ArrayColumnInfo = field("ArrayColumnInfo")
    TimeSeriesMeasureValueColumnInfo = field("TimeSeriesMeasureValueColumnInfo")
    RowColumnInfo = field("RowColumnInfo")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TypePaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TypePaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnInfo:
    boto3_raw_data: "type_defs.ColumnInfoTypeDef" = dataclasses.field()

    Type = field("Type")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleConfiguration:
    boto3_raw_data: "type_defs.ScheduleConfigurationTypeDef" = dataclasses.field()

    ScheduleExpression = field("ScheduleExpression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduleConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleConfigurationTypeDef"]
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
class TimeSeriesDataPointPaginator:
    boto3_raw_data: "type_defs.TimeSeriesDataPointPaginatorTypeDef" = (
        dataclasses.field()
    )

    Time = field("Time")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesDataPointPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesDataPointPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesDataPoint:
    boto3_raw_data: "type_defs.TimeSeriesDataPointTypeDef" = dataclasses.field()

    Time = field("Time")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesDataPointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesDataPointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScheduledQueryRequest:
    boto3_raw_data: "type_defs.DeleteScheduledQueryRequestTypeDef" = dataclasses.field()

    ScheduledQueryArn = field("ScheduledQueryArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduledQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduledQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Endpoint:
    boto3_raw_data: "type_defs.EndpointTypeDef" = dataclasses.field()

    Address = field("Address")
    CachePeriodInMinutes = field("CachePeriodInMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledQueryRequest:
    boto3_raw_data: "type_defs.DescribeScheduledQueryRequestTypeDef" = (
        dataclasses.field()
    )

    ScheduledQueryArn = field("ScheduledQueryArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScheduledQueryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionMapping:
    boto3_raw_data: "type_defs.DimensionMappingTypeDef" = dataclasses.field()

    Name = field("Name")
    DimensionValueType = field("DimensionValueType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Configuration:
    boto3_raw_data: "type_defs.S3ConfigurationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectKeyPrefix = field("ObjectKeyPrefix")
    EncryptionOption = field("EncryptionOption")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ReportLocation:
    boto3_raw_data: "type_defs.S3ReportLocationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectKey = field("ObjectKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ReportLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ReportLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledQueryInsights:
    boto3_raw_data: "type_defs.ScheduledQueryInsightsTypeDef" = dataclasses.field()

    Mode = field("Mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledQueryInsightsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledQueryInsightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionStats:
    boto3_raw_data: "type_defs.ExecutionStatsTypeDef" = dataclasses.field()

    ExecutionTimeInMillis = field("ExecutionTimeInMillis")
    DataWrites = field("DataWrites")
    BytesMetered = field("BytesMetered")
    CumulativeBytesScanned = field("CumulativeBytesScanned")
    RecordsIngested = field("RecordsIngested")
    QueryResultRows = field("QueryResultRows")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionStatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExecutionStatsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LastUpdate:
    boto3_raw_data: "type_defs.LastUpdateTypeDef" = dataclasses.field()

    TargetQueryTCU = field("TargetQueryTCU")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LastUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LastUpdateTypeDef"]]
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
class ListScheduledQueriesRequest:
    boto3_raw_data: "type_defs.ListScheduledQueriesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScheduledQueriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduledQueriesRequestTypeDef"]
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
    MaxResults = field("MaxResults")
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
class MultiMeasureAttributeMapping:
    boto3_raw_data: "type_defs.MultiMeasureAttributeMappingTypeDef" = (
        dataclasses.field()
    )

    SourceColumn = field("SourceColumn")
    MeasureValueType = field("MeasureValueType")
    TargetMultiMeasureAttributeName = field("TargetMultiMeasureAttributeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiMeasureAttributeMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiMeasureAttributeMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrepareQueryRequest:
    boto3_raw_data: "type_defs.PrepareQueryRequestTypeDef" = dataclasses.field()

    QueryString = field("QueryString")
    ValidateOnly = field("ValidateOnly")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrepareQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrepareQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryInsights:
    boto3_raw_data: "type_defs.QueryInsightsTypeDef" = dataclasses.field()

    Mode = field("Mode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryInsightsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryInsightsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStatus:
    boto3_raw_data: "type_defs.QueryStatusTypeDef" = dataclasses.field()

    ProgressPercentage = field("ProgressPercentage")
    CumulativeBytesScanned = field("CumulativeBytesScanned")
    CumulativeBytesMetered = field("CumulativeBytesMetered")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuerySpatialCoverageMax:
    boto3_raw_data: "type_defs.QuerySpatialCoverageMaxTypeDef" = dataclasses.field()

    Value = field("Value")
    TableArn = field("TableArn")
    PartitionKey = field("PartitionKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuerySpatialCoverageMaxTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuerySpatialCoverageMaxTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryTemporalRangeMax:
    boto3_raw_data: "type_defs.QueryTemporalRangeMaxTypeDef" = dataclasses.field()

    Value = field("Value")
    TableArn = field("TableArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryTemporalRangeMaxTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryTemporalRangeMaxTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamDestination:
    boto3_raw_data: "type_defs.TimestreamDestinationTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestreamDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamDestinationTypeDef"]
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
class UpdateScheduledQueryRequest:
    boto3_raw_data: "type_defs.UpdateScheduledQueryRequestTypeDef" = dataclasses.field()

    ScheduledQueryArn = field("ScheduledQueryArn")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateScheduledQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScheduledQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountSettingsNotificationConfiguration:
    boto3_raw_data: "type_defs.AccountSettingsNotificationConfigurationTypeDef" = (
        dataclasses.field()
    )

    RoleArn = field("RoleArn")

    @cached_property
    def SnsConfiguration(self):  # pragma: no cover
        return SnsConfiguration.make_one(self.boto3_raw_data["SnsConfiguration"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AccountSettingsNotificationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountSettingsNotificationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfiguration:
    boto3_raw_data: "type_defs.NotificationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def SnsConfiguration(self):  # pragma: no cover
        return SnsConfiguration.make_one(self.boto3_raw_data["SnsConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelQueryResponse:
    boto3_raw_data: "type_defs.CancelQueryResponseTypeDef" = dataclasses.field()

    CancellationMessage = field("CancellationMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScheduledQueryResponse:
    boto3_raw_data: "type_defs.CreateScheduledQueryResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduledQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduledQueryResponseTypeDef"]
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
class ColumnInfoPaginator:
    boto3_raw_data: "type_defs.ColumnInfoPaginatorTypeDef" = dataclasses.field()

    @cached_property
    def Type(self):  # pragma: no cover
        return TypePaginator.make_one(self.boto3_raw_data["Type"])

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ColumnInfoPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnInfoPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Type:
    boto3_raw_data: "type_defs.TypeTypeDef" = dataclasses.field()

    ScalarType = field("ScalarType")
    ArrayColumnInfo = field("ArrayColumnInfo")
    TimeSeriesMeasureValueColumnInfo = field("TimeSeriesMeasureValueColumnInfo")

    @cached_property
    def RowColumnInfo(self):  # pragma: no cover
        return ColumnInfo.make_many(self.boto3_raw_data["RowColumnInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TypeTypeDef"]]
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
class DatumPaginator:
    boto3_raw_data: "type_defs.DatumPaginatorTypeDef" = dataclasses.field()

    ScalarValue = field("ScalarValue")

    @cached_property
    def TimeSeriesValue(self):  # pragma: no cover
        return TimeSeriesDataPointPaginator.make_many(
            self.boto3_raw_data["TimeSeriesValue"]
        )

    ArrayValue = field("ArrayValue")
    RowValue = field("RowValue")
    NullValue = field("NullValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatumPaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatumPaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Datum:
    boto3_raw_data: "type_defs.DatumTypeDef" = dataclasses.field()

    ScalarValue = field("ScalarValue")

    @cached_property
    def TimeSeriesValue(self):  # pragma: no cover
        return TimeSeriesDataPoint.make_many(self.boto3_raw_data["TimeSeriesValue"])

    ArrayValue = field("ArrayValue")
    RowValue = field("RowValue")
    NullValue = field("NullValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatumTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatumTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointsResponse:
    boto3_raw_data: "type_defs.DescribeEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return Endpoint.make_many(self.boto3_raw_data["Endpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorReportConfiguration:
    boto3_raw_data: "type_defs.ErrorReportConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3Configuration.make_one(self.boto3_raw_data["S3Configuration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ErrorReportConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ErrorReportConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorReportLocation:
    boto3_raw_data: "type_defs.ErrorReportLocationTypeDef" = dataclasses.field()

    @cached_property
    def S3ReportLocation(self):  # pragma: no cover
        return S3ReportLocation.make_one(self.boto3_raw_data["S3ReportLocation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ErrorReportLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ErrorReportLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteScheduledQueryRequest:
    boto3_raw_data: "type_defs.ExecuteScheduledQueryRequestTypeDef" = (
        dataclasses.field()
    )

    ScheduledQueryArn = field("ScheduledQueryArn")
    InvocationTime = field("InvocationTime")
    ClientToken = field("ClientToken")

    @cached_property
    def QueryInsights(self):  # pragma: no cover
        return ScheduledQueryInsights.make_one(self.boto3_raw_data["QueryInsights"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteScheduledQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteScheduledQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScheduledQueriesRequestPaginate:
    boto3_raw_data: "type_defs.ListScheduledQueriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListScheduledQueriesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduledQueriesRequestPaginateTypeDef"]
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
class MixedMeasureMappingOutput:
    boto3_raw_data: "type_defs.MixedMeasureMappingOutputTypeDef" = dataclasses.field()

    MeasureValueType = field("MeasureValueType")
    MeasureName = field("MeasureName")
    SourceColumn = field("SourceColumn")
    TargetMeasureName = field("TargetMeasureName")

    @cached_property
    def MultiMeasureAttributeMappings(self):  # pragma: no cover
        return MultiMeasureAttributeMapping.make_many(
            self.boto3_raw_data["MultiMeasureAttributeMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MixedMeasureMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MixedMeasureMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MixedMeasureMapping:
    boto3_raw_data: "type_defs.MixedMeasureMappingTypeDef" = dataclasses.field()

    MeasureValueType = field("MeasureValueType")
    MeasureName = field("MeasureName")
    SourceColumn = field("SourceColumn")
    TargetMeasureName = field("TargetMeasureName")

    @cached_property
    def MultiMeasureAttributeMappings(self):  # pragma: no cover
        return MultiMeasureAttributeMapping.make_many(
            self.boto3_raw_data["MultiMeasureAttributeMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MixedMeasureMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MixedMeasureMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiMeasureMappingsOutput:
    boto3_raw_data: "type_defs.MultiMeasureMappingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def MultiMeasureAttributeMappings(self):  # pragma: no cover
        return MultiMeasureAttributeMapping.make_many(
            self.boto3_raw_data["MultiMeasureAttributeMappings"]
        )

    TargetMultiMeasureName = field("TargetMultiMeasureName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiMeasureMappingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiMeasureMappingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiMeasureMappings:
    boto3_raw_data: "type_defs.MultiMeasureMappingsTypeDef" = dataclasses.field()

    @cached_property
    def MultiMeasureAttributeMappings(self):  # pragma: no cover
        return MultiMeasureAttributeMapping.make_many(
            self.boto3_raw_data["MultiMeasureAttributeMappings"]
        )

    TargetMultiMeasureName = field("TargetMultiMeasureName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiMeasureMappingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiMeasureMappingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryRequestPaginate:
    boto3_raw_data: "type_defs.QueryRequestPaginateTypeDef" = dataclasses.field()

    QueryString = field("QueryString")
    ClientToken = field("ClientToken")

    @cached_property
    def QueryInsights(self):  # pragma: no cover
        return QueryInsights.make_one(self.boto3_raw_data["QueryInsights"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryRequest:
    boto3_raw_data: "type_defs.QueryRequestTypeDef" = dataclasses.field()

    QueryString = field("QueryString")
    ClientToken = field("ClientToken")
    NextToken = field("NextToken")
    MaxRows = field("MaxRows")

    @cached_property
    def QueryInsights(self):  # pragma: no cover
        return QueryInsights.make_one(self.boto3_raw_data["QueryInsights"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuerySpatialCoverage:
    boto3_raw_data: "type_defs.QuerySpatialCoverageTypeDef" = dataclasses.field()

    @cached_property
    def Max(self):  # pragma: no cover
        return QuerySpatialCoverageMax.make_one(self.boto3_raw_data["Max"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuerySpatialCoverageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuerySpatialCoverageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryTemporalRange:
    boto3_raw_data: "type_defs.QueryTemporalRangeTypeDef" = dataclasses.field()

    @cached_property
    def Max(self):  # pragma: no cover
        return QueryTemporalRangeMax.make_one(self.boto3_raw_data["Max"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryTemporalRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryTemporalRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetDestination:
    boto3_raw_data: "type_defs.TargetDestinationTypeDef" = dataclasses.field()

    @cached_property
    def TimestreamDestination(self):  # pragma: no cover
        return TimestreamDestination.make_one(
            self.boto3_raw_data["TimestreamDestination"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedCapacityRequest:
    boto3_raw_data: "type_defs.ProvisionedCapacityRequestTypeDef" = dataclasses.field()

    TargetQueryTCU = field("TargetQueryTCU")

    @cached_property
    def NotificationConfiguration(self):  # pragma: no cover
        return AccountSettingsNotificationConfiguration.make_one(
            self.boto3_raw_data["NotificationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedCapacityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedCapacityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedCapacityResponse:
    boto3_raw_data: "type_defs.ProvisionedCapacityResponseTypeDef" = dataclasses.field()

    ActiveQueryTCU = field("ActiveQueryTCU")

    @cached_property
    def NotificationConfiguration(self):  # pragma: no cover
        return AccountSettingsNotificationConfiguration.make_one(
            self.boto3_raw_data["NotificationConfiguration"]
        )

    @cached_property
    def LastUpdate(self):  # pragma: no cover
        return LastUpdate.make_one(self.boto3_raw_data["LastUpdate"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedCapacityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedCapacityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterMapping:
    boto3_raw_data: "type_defs.ParameterMappingTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Type(self):  # pragma: no cover
        return Type.make_one(self.boto3_raw_data["Type"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectColumn:
    boto3_raw_data: "type_defs.SelectColumnTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Type(self):  # pragma: no cover
        return Type.make_one(self.boto3_raw_data["Type"])

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    Aliased = field("Aliased")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SelectColumnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SelectColumnTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RowPaginator:
    boto3_raw_data: "type_defs.RowPaginatorTypeDef" = dataclasses.field()

    @cached_property
    def Data(self):  # pragma: no cover
        return DatumPaginator.make_many(self.boto3_raw_data["Data"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowPaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowPaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Row:
    boto3_raw_data: "type_defs.RowTypeDef" = dataclasses.field()

    @cached_property
    def Data(self):  # pragma: no cover
        return Datum.make_many(self.boto3_raw_data["Data"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamConfigurationOutput:
    boto3_raw_data: "type_defs.TimestreamConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    TimeColumn = field("TimeColumn")

    @cached_property
    def DimensionMappings(self):  # pragma: no cover
        return DimensionMapping.make_many(self.boto3_raw_data["DimensionMappings"])

    @cached_property
    def MultiMeasureMappings(self):  # pragma: no cover
        return MultiMeasureMappingsOutput.make_one(
            self.boto3_raw_data["MultiMeasureMappings"]
        )

    @cached_property
    def MixedMeasureMappings(self):  # pragma: no cover
        return MixedMeasureMappingOutput.make_many(
            self.boto3_raw_data["MixedMeasureMappings"]
        )

    MeasureNameColumn = field("MeasureNameColumn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TimestreamConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamConfiguration:
    boto3_raw_data: "type_defs.TimestreamConfigurationTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    TimeColumn = field("TimeColumn")

    @cached_property
    def DimensionMappings(self):  # pragma: no cover
        return DimensionMapping.make_many(self.boto3_raw_data["DimensionMappings"])

    @cached_property
    def MultiMeasureMappings(self):  # pragma: no cover
        return MultiMeasureMappings.make_one(
            self.boto3_raw_data["MultiMeasureMappings"]
        )

    @cached_property
    def MixedMeasureMappings(self):  # pragma: no cover
        return MixedMeasureMapping.make_many(
            self.boto3_raw_data["MixedMeasureMappings"]
        )

    MeasureNameColumn = field("MeasureNameColumn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestreamConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryInsightsResponse:
    boto3_raw_data: "type_defs.QueryInsightsResponseTypeDef" = dataclasses.field()

    @cached_property
    def QuerySpatialCoverage(self):  # pragma: no cover
        return QuerySpatialCoverage.make_one(
            self.boto3_raw_data["QuerySpatialCoverage"]
        )

    @cached_property
    def QueryTemporalRange(self):  # pragma: no cover
        return QueryTemporalRange.make_one(self.boto3_raw_data["QueryTemporalRange"])

    QueryTableCount = field("QueryTableCount")
    OutputRows = field("OutputRows")
    OutputBytes = field("OutputBytes")
    UnloadPartitionCount = field("UnloadPartitionCount")
    UnloadWrittenRows = field("UnloadWrittenRows")
    UnloadWrittenBytes = field("UnloadWrittenBytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryInsightsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryInsightsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledQueryInsightsResponse:
    boto3_raw_data: "type_defs.ScheduledQueryInsightsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QuerySpatialCoverage(self):  # pragma: no cover
        return QuerySpatialCoverage.make_one(
            self.boto3_raw_data["QuerySpatialCoverage"]
        )

    @cached_property
    def QueryTemporalRange(self):  # pragma: no cover
        return QueryTemporalRange.make_one(self.boto3_raw_data["QueryTemporalRange"])

    QueryTableCount = field("QueryTableCount")
    OutputRows = field("OutputRows")
    OutputBytes = field("OutputBytes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ScheduledQueryInsightsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledQueryInsightsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledQuery:
    boto3_raw_data: "type_defs.ScheduledQueryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    State = field("State")
    CreationTime = field("CreationTime")
    PreviousInvocationTime = field("PreviousInvocationTime")
    NextInvocationTime = field("NextInvocationTime")

    @cached_property
    def ErrorReportConfiguration(self):  # pragma: no cover
        return ErrorReportConfiguration.make_one(
            self.boto3_raw_data["ErrorReportConfiguration"]
        )

    @cached_property
    def TargetDestination(self):  # pragma: no cover
        return TargetDestination.make_one(self.boto3_raw_data["TargetDestination"])

    LastRunStatus = field("LastRunStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduledQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduledQueryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryComputeRequest:
    boto3_raw_data: "type_defs.QueryComputeRequestTypeDef" = dataclasses.field()

    ComputeMode = field("ComputeMode")

    @cached_property
    def ProvisionedCapacity(self):  # pragma: no cover
        return ProvisionedCapacityRequest.make_one(
            self.boto3_raw_data["ProvisionedCapacity"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryComputeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryComputeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryComputeResponse:
    boto3_raw_data: "type_defs.QueryComputeResponseTypeDef" = dataclasses.field()

    ComputeMode = field("ComputeMode")

    @cached_property
    def ProvisionedCapacity(self):  # pragma: no cover
        return ProvisionedCapacityResponse.make_one(
            self.boto3_raw_data["ProvisionedCapacity"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryComputeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryComputeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrepareQueryResponse:
    boto3_raw_data: "type_defs.PrepareQueryResponseTypeDef" = dataclasses.field()

    QueryString = field("QueryString")

    @cached_property
    def Columns(self):  # pragma: no cover
        return SelectColumn.make_many(self.boto3_raw_data["Columns"])

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ParameterMapping.make_many(self.boto3_raw_data["Parameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrepareQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrepareQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetConfigurationOutput:
    boto3_raw_data: "type_defs.TargetConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def TimestreamConfiguration(self):  # pragma: no cover
        return TimestreamConfigurationOutput.make_one(
            self.boto3_raw_data["TimestreamConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetConfiguration:
    boto3_raw_data: "type_defs.TargetConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def TimestreamConfiguration(self):  # pragma: no cover
        return TimestreamConfiguration.make_one(
            self.boto3_raw_data["TimestreamConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryResponsePaginator:
    boto3_raw_data: "type_defs.QueryResponsePaginatorTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @cached_property
    def Rows(self):  # pragma: no cover
        return RowPaginator.make_many(self.boto3_raw_data["Rows"])

    @cached_property
    def ColumnInfo(self):  # pragma: no cover
        return ColumnInfoPaginator.make_many(self.boto3_raw_data["ColumnInfo"])

    @cached_property
    def QueryStatus(self):  # pragma: no cover
        return QueryStatus.make_one(self.boto3_raw_data["QueryStatus"])

    @cached_property
    def QueryInsightsResponse(self):  # pragma: no cover
        return QueryInsightsResponse.make_one(
            self.boto3_raw_data["QueryInsightsResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryResponsePaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryResponse:
    boto3_raw_data: "type_defs.QueryResponseTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @cached_property
    def Rows(self):  # pragma: no cover
        return Row.make_many(self.boto3_raw_data["Rows"])

    @cached_property
    def ColumnInfo(self):  # pragma: no cover
        return ColumnInfo.make_many(self.boto3_raw_data["ColumnInfo"])

    @cached_property
    def QueryStatus(self):  # pragma: no cover
        return QueryStatus.make_one(self.boto3_raw_data["QueryStatus"])

    @cached_property
    def QueryInsightsResponse(self):  # pragma: no cover
        return QueryInsightsResponse.make_one(
            self.boto3_raw_data["QueryInsightsResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledQueryRunSummary:
    boto3_raw_data: "type_defs.ScheduledQueryRunSummaryTypeDef" = dataclasses.field()

    InvocationTime = field("InvocationTime")
    TriggerTime = field("TriggerTime")
    RunStatus = field("RunStatus")

    @cached_property
    def ExecutionStats(self):  # pragma: no cover
        return ExecutionStats.make_one(self.boto3_raw_data["ExecutionStats"])

    @cached_property
    def QueryInsightsResponse(self):  # pragma: no cover
        return ScheduledQueryInsightsResponse.make_one(
            self.boto3_raw_data["QueryInsightsResponse"]
        )

    @cached_property
    def ErrorReportLocation(self):  # pragma: no cover
        return ErrorReportLocation.make_one(self.boto3_raw_data["ErrorReportLocation"])

    FailureReason = field("FailureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledQueryRunSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledQueryRunSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScheduledQueriesResponse:
    boto3_raw_data: "type_defs.ListScheduledQueriesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScheduledQueries(self):  # pragma: no cover
        return ScheduledQuery.make_many(self.boto3_raw_data["ScheduledQueries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScheduledQueriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduledQueriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountSettingsRequest:
    boto3_raw_data: "type_defs.UpdateAccountSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxQueryTCU = field("MaxQueryTCU")
    QueryPricingModel = field("QueryPricingModel")

    @cached_property
    def QueryCompute(self):  # pragma: no cover
        return QueryComputeRequest.make_one(self.boto3_raw_data["QueryCompute"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccountSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountSettingsResponse:
    boto3_raw_data: "type_defs.DescribeAccountSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    MaxQueryTCU = field("MaxQueryTCU")
    QueryPricingModel = field("QueryPricingModel")

    @cached_property
    def QueryCompute(self):  # pragma: no cover
        return QueryComputeResponse.make_one(self.boto3_raw_data["QueryCompute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAccountSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountSettingsResponse:
    boto3_raw_data: "type_defs.UpdateAccountSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    MaxQueryTCU = field("MaxQueryTCU")
    QueryPricingModel = field("QueryPricingModel")

    @cached_property
    def QueryCompute(self):  # pragma: no cover
        return QueryComputeResponse.make_one(self.boto3_raw_data["QueryCompute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAccountSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledQueryDescription:
    boto3_raw_data: "type_defs.ScheduledQueryDescriptionTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    QueryString = field("QueryString")
    State = field("State")

    @cached_property
    def ScheduleConfiguration(self):  # pragma: no cover
        return ScheduleConfiguration.make_one(
            self.boto3_raw_data["ScheduleConfiguration"]
        )

    @cached_property
    def NotificationConfiguration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(
            self.boto3_raw_data["NotificationConfiguration"]
        )

    CreationTime = field("CreationTime")
    PreviousInvocationTime = field("PreviousInvocationTime")
    NextInvocationTime = field("NextInvocationTime")

    @cached_property
    def TargetConfiguration(self):  # pragma: no cover
        return TargetConfigurationOutput.make_one(
            self.boto3_raw_data["TargetConfiguration"]
        )

    ScheduledQueryExecutionRoleArn = field("ScheduledQueryExecutionRoleArn")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def ErrorReportConfiguration(self):  # pragma: no cover
        return ErrorReportConfiguration.make_one(
            self.boto3_raw_data["ErrorReportConfiguration"]
        )

    @cached_property
    def LastRunSummary(self):  # pragma: no cover
        return ScheduledQueryRunSummary.make_one(self.boto3_raw_data["LastRunSummary"])

    @cached_property
    def RecentlyFailedRuns(self):  # pragma: no cover
        return ScheduledQueryRunSummary.make_many(
            self.boto3_raw_data["RecentlyFailedRuns"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledQueryDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledQueryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScheduledQueryRequest:
    boto3_raw_data: "type_defs.CreateScheduledQueryRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    QueryString = field("QueryString")

    @cached_property
    def ScheduleConfiguration(self):  # pragma: no cover
        return ScheduleConfiguration.make_one(
            self.boto3_raw_data["ScheduleConfiguration"]
        )

    @cached_property
    def NotificationConfiguration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(
            self.boto3_raw_data["NotificationConfiguration"]
        )

    ScheduledQueryExecutionRoleArn = field("ScheduledQueryExecutionRoleArn")

    @cached_property
    def ErrorReportConfiguration(self):  # pragma: no cover
        return ErrorReportConfiguration.make_one(
            self.boto3_raw_data["ErrorReportConfiguration"]
        )

    TargetConfiguration = field("TargetConfiguration")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduledQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduledQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledQueryResponse:
    boto3_raw_data: "type_defs.DescribeScheduledQueryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScheduledQuery(self):  # pragma: no cover
        return ScheduledQueryDescription.make_one(self.boto3_raw_data["ScheduledQuery"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScheduledQueryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
