# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pi import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class DataPoint:
    boto3_raw_data: "type_defs.DataPointTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataPointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsMetric:
    boto3_raw_data: "type_defs.PerformanceInsightsMetricTypeDef" = dataclasses.field()

    Metric = field("Metric")
    DisplayName = field("DisplayName")
    Dimensions = field("Dimensions")
    Filter = field("Filter")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PerformanceInsightsMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePerformanceAnalysisReportRequest:
    boto3_raw_data: "type_defs.DeletePerformanceAnalysisReportRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceType = field("ServiceType")
    Identifier = field("Identifier")
    AnalysisReportId = field("AnalysisReportId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePerformanceAnalysisReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePerformanceAnalysisReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionGroup:
    boto3_raw_data: "type_defs.DimensionGroupTypeDef" = dataclasses.field()

    Group = field("Group")
    Dimensions = field("Dimensions")
    Limit = field("Limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionKeyDescription:
    boto3_raw_data: "type_defs.DimensionKeyDescriptionTypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")
    Total = field("Total")
    AdditionalMetrics = field("AdditionalMetrics")
    Partitions = field("Partitions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DimensionKeyDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionKeyDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponsePartitionKey:
    boto3_raw_data: "type_defs.ResponsePartitionKeyTypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponsePartitionKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponsePartitionKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionDetail:
    boto3_raw_data: "type_defs.DimensionDetailTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionKeyDetail:
    boto3_raw_data: "type_defs.DimensionKeyDetailTypeDef" = dataclasses.field()

    Value = field("Value")
    Dimension = field("Dimension")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DimensionKeyDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionKeyDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeatureMetadata:
    boto3_raw_data: "type_defs.FeatureMetadataTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FeatureMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FeatureMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDimensionKeyDetailsRequest:
    boto3_raw_data: "type_defs.GetDimensionKeyDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceType = field("ServiceType")
    Identifier = field("Identifier")
    Group = field("Group")
    GroupIdentifier = field("GroupIdentifier")
    RequestedDimensions = field("RequestedDimensions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDimensionKeyDetailsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDimensionKeyDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPerformanceAnalysisReportRequest:
    boto3_raw_data: "type_defs.GetPerformanceAnalysisReportRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceType = field("ServiceType")
    Identifier = field("Identifier")
    AnalysisReportId = field("AnalysisReportId")
    TextFormat = field("TextFormat")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPerformanceAnalysisReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPerformanceAnalysisReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceMetadataRequest:
    boto3_raw_data: "type_defs.GetResourceMetadataRequestTypeDef" = dataclasses.field()

    ServiceType = field("ServiceType")
    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recommendation:
    boto3_raw_data: "type_defs.RecommendationTypeDef" = dataclasses.field()

    RecommendationId = field("RecommendationId")
    RecommendationDescription = field("RecommendationDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecommendationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableResourceDimensionsRequest:
    boto3_raw_data: "type_defs.ListAvailableResourceDimensionsRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceType = field("ServiceType")
    Identifier = field("Identifier")
    Metrics = field("Metrics")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AuthorizedActions = field("AuthorizedActions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableResourceDimensionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableResourceDimensionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableResourceMetricsRequest:
    boto3_raw_data: "type_defs.ListAvailableResourceMetricsRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceType = field("ServiceType")
    Identifier = field("Identifier")
    MetricTypes = field("MetricTypes")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableResourceMetricsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableResourceMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseResourceMetric:
    boto3_raw_data: "type_defs.ResponseResourceMetricTypeDef" = dataclasses.field()

    Metric = field("Metric")
    Description = field("Description")
    Unit = field("Unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseResourceMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseResourceMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPerformanceAnalysisReportsRequest:
    boto3_raw_data: "type_defs.ListPerformanceAnalysisReportsRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceType = field("ServiceType")
    Identifier = field("Identifier")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ListTags = field("ListTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPerformanceAnalysisReportsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPerformanceAnalysisReportsRequestTypeDef"]
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

    ServiceType = field("ServiceType")
    ResourceARN = field("ResourceARN")

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
class ResponseResourceMetricKey:
    boto3_raw_data: "type_defs.ResponseResourceMetricKeyTypeDef" = dataclasses.field()

    Metric = field("Metric")
    Dimensions = field("Dimensions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseResourceMetricKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseResourceMetricKeyTypeDef"]
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

    ServiceType = field("ServiceType")
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
class AnalysisReportSummary:
    boto3_raw_data: "type_defs.AnalysisReportSummaryTypeDef" = dataclasses.field()

    AnalysisReportId = field("AnalysisReportId")
    CreateTime = field("CreateTime")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Status = field("Status")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisReportSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisReportSummaryTypeDef"]
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

    ServiceType = field("ServiceType")
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
class CreatePerformanceAnalysisReportRequest:
    boto3_raw_data: "type_defs.CreatePerformanceAnalysisReportRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceType = field("ServiceType")
    Identifier = field("Identifier")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePerformanceAnalysisReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePerformanceAnalysisReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePerformanceAnalysisReportResponse:
    boto3_raw_data: "type_defs.CreatePerformanceAnalysisReportResponseTypeDef" = (
        dataclasses.field()
    )

    AnalysisReportId = field("AnalysisReportId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePerformanceAnalysisReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePerformanceAnalysisReportResponseTypeDef"]
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
class Data:
    boto3_raw_data: "type_defs.DataTypeDef" = dataclasses.field()

    @cached_property
    def PerformanceInsightsMetric(self):  # pragma: no cover
        return PerformanceInsightsMetric.make_one(
            self.boto3_raw_data["PerformanceInsightsMetric"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDimensionKeysRequest:
    boto3_raw_data: "type_defs.DescribeDimensionKeysRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceType = field("ServiceType")
    Identifier = field("Identifier")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Metric = field("Metric")

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return DimensionGroup.make_one(self.boto3_raw_data["GroupBy"])

    PeriodInSeconds = field("PeriodInSeconds")
    AdditionalMetrics = field("AdditionalMetrics")

    @cached_property
    def PartitionBy(self):  # pragma: no cover
        return DimensionGroup.make_one(self.boto3_raw_data["PartitionBy"])

    Filter = field("Filter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDimensionKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDimensionKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricQuery:
    boto3_raw_data: "type_defs.MetricQueryTypeDef" = dataclasses.field()

    Metric = field("Metric")

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return DimensionGroup.make_one(self.boto3_raw_data["GroupBy"])

    Filter = field("Filter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricQueryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDimensionKeysResponse:
    boto3_raw_data: "type_defs.DescribeDimensionKeysResponseTypeDef" = (
        dataclasses.field()
    )

    AlignedStartTime = field("AlignedStartTime")
    AlignedEndTime = field("AlignedEndTime")

    @cached_property
    def PartitionKeys(self):  # pragma: no cover
        return ResponsePartitionKey.make_many(self.boto3_raw_data["PartitionKeys"])

    @cached_property
    def Keys(self):  # pragma: no cover
        return DimensionKeyDescription.make_many(self.boto3_raw_data["Keys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDimensionKeysResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDimensionKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionGroupDetail:
    boto3_raw_data: "type_defs.DimensionGroupDetailTypeDef" = dataclasses.field()

    Group = field("Group")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return DimensionDetail.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DimensionGroupDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionGroupDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDimensionKeyDetailsResponse:
    boto3_raw_data: "type_defs.GetDimensionKeyDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return DimensionKeyDetail.make_many(self.boto3_raw_data["Dimensions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDimensionKeyDetailsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDimensionKeyDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceMetadataResponse:
    boto3_raw_data: "type_defs.GetResourceMetadataResponseTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    Features = field("Features")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceMetadataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableResourceMetricsResponse:
    boto3_raw_data: "type_defs.ListAvailableResourceMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metrics(self):  # pragma: no cover
        return ResponseResourceMetric.make_many(self.boto3_raw_data["Metrics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableResourceMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableResourceMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricKeyDataPoints:
    boto3_raw_data: "type_defs.MetricKeyDataPointsTypeDef" = dataclasses.field()

    @cached_property
    def Key(self):  # pragma: no cover
        return ResponseResourceMetricKey.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def DataPoints(self):  # pragma: no cover
        return DataPoint.make_many(self.boto3_raw_data["DataPoints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricKeyDataPointsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricKeyDataPointsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPerformanceAnalysisReportsResponse:
    boto3_raw_data: "type_defs.ListPerformanceAnalysisReportsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnalysisReports(self):  # pragma: no cover
        return AnalysisReportSummary.make_many(self.boto3_raw_data["AnalysisReports"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPerformanceAnalysisReportsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPerformanceAnalysisReportsResponseTypeDef"]
        ],
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
    InsightType = field("InsightType")
    Context = field("Context")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Severity = field("Severity")
    SupportingInsights = field("SupportingInsights")
    Description = field("Description")

    @cached_property
    def Recommendations(self):  # pragma: no cover
        return Recommendation.make_many(self.boto3_raw_data["Recommendations"])

    @cached_property
    def InsightData(self):  # pragma: no cover
        return Data.make_many(self.boto3_raw_data["InsightData"])

    @cached_property
    def BaselineData(self):  # pragma: no cover
        return Data.make_many(self.boto3_raw_data["BaselineData"])

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
class GetResourceMetricsRequest:
    boto3_raw_data: "type_defs.GetResourceMetricsRequestTypeDef" = dataclasses.field()

    ServiceType = field("ServiceType")
    Identifier = field("Identifier")

    @cached_property
    def MetricQueries(self):  # pragma: no cover
        return MetricQuery.make_many(self.boto3_raw_data["MetricQueries"])

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    PeriodInSeconds = field("PeriodInSeconds")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    PeriodAlignment = field("PeriodAlignment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDimensionGroups:
    boto3_raw_data: "type_defs.MetricDimensionGroupsTypeDef" = dataclasses.field()

    Metric = field("Metric")

    @cached_property
    def Groups(self):  # pragma: no cover
        return DimensionGroupDetail.make_many(self.boto3_raw_data["Groups"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricDimensionGroupsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDimensionGroupsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceMetricsResponse:
    boto3_raw_data: "type_defs.GetResourceMetricsResponseTypeDef" = dataclasses.field()

    AlignedStartTime = field("AlignedStartTime")
    AlignedEndTime = field("AlignedEndTime")
    Identifier = field("Identifier")

    @cached_property
    def MetricList(self):  # pragma: no cover
        return MetricKeyDataPoints.make_many(self.boto3_raw_data["MetricList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisReport:
    boto3_raw_data: "type_defs.AnalysisReportTypeDef" = dataclasses.field()

    AnalysisReportId = field("AnalysisReportId")
    Identifier = field("Identifier")
    ServiceType = field("ServiceType")
    CreateTime = field("CreateTime")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Status = field("Status")

    @cached_property
    def Insights(self):  # pragma: no cover
        return Insight.make_many(self.boto3_raw_data["Insights"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisReportTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableResourceDimensionsResponse:
    boto3_raw_data: "type_defs.ListAvailableResourceDimensionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricDimensions(self):  # pragma: no cover
        return MetricDimensionGroups.make_many(self.boto3_raw_data["MetricDimensions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableResourceDimensionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableResourceDimensionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPerformanceAnalysisReportResponse:
    boto3_raw_data: "type_defs.GetPerformanceAnalysisReportResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnalysisReport(self):  # pragma: no cover
        return AnalysisReport.make_one(self.boto3_raw_data["AnalysisReport"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPerformanceAnalysisReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPerformanceAnalysisReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
