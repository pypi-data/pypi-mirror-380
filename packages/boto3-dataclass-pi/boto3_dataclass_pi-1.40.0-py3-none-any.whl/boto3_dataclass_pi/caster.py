# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pi import type_defs as bs_td


class PICaster:

    def create_performance_analysis_report(
        self,
        res: "bs_td.CreatePerformanceAnalysisReportResponseTypeDef",
    ) -> "dc_td.CreatePerformanceAnalysisReportResponse":
        return dc_td.CreatePerformanceAnalysisReportResponse.make_one(res)

    def describe_dimension_keys(
        self,
        res: "bs_td.DescribeDimensionKeysResponseTypeDef",
    ) -> "dc_td.DescribeDimensionKeysResponse":
        return dc_td.DescribeDimensionKeysResponse.make_one(res)

    def get_dimension_key_details(
        self,
        res: "bs_td.GetDimensionKeyDetailsResponseTypeDef",
    ) -> "dc_td.GetDimensionKeyDetailsResponse":
        return dc_td.GetDimensionKeyDetailsResponse.make_one(res)

    def get_performance_analysis_report(
        self,
        res: "bs_td.GetPerformanceAnalysisReportResponseTypeDef",
    ) -> "dc_td.GetPerformanceAnalysisReportResponse":
        return dc_td.GetPerformanceAnalysisReportResponse.make_one(res)

    def get_resource_metadata(
        self,
        res: "bs_td.GetResourceMetadataResponseTypeDef",
    ) -> "dc_td.GetResourceMetadataResponse":
        return dc_td.GetResourceMetadataResponse.make_one(res)

    def get_resource_metrics(
        self,
        res: "bs_td.GetResourceMetricsResponseTypeDef",
    ) -> "dc_td.GetResourceMetricsResponse":
        return dc_td.GetResourceMetricsResponse.make_one(res)

    def list_available_resource_dimensions(
        self,
        res: "bs_td.ListAvailableResourceDimensionsResponseTypeDef",
    ) -> "dc_td.ListAvailableResourceDimensionsResponse":
        return dc_td.ListAvailableResourceDimensionsResponse.make_one(res)

    def list_available_resource_metrics(
        self,
        res: "bs_td.ListAvailableResourceMetricsResponseTypeDef",
    ) -> "dc_td.ListAvailableResourceMetricsResponse":
        return dc_td.ListAvailableResourceMetricsResponse.make_one(res)

    def list_performance_analysis_reports(
        self,
        res: "bs_td.ListPerformanceAnalysisReportsResponseTypeDef",
    ) -> "dc_td.ListPerformanceAnalysisReportsResponse":
        return dc_td.ListPerformanceAnalysisReportsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)


pi_caster = PICaster()
