# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_timestream_query import type_defs as bs_td


class TIMESTREAM_QUERYCaster:

    def cancel_query(
        self,
        res: "bs_td.CancelQueryResponseTypeDef",
    ) -> "dc_td.CancelQueryResponse":
        return dc_td.CancelQueryResponse.make_one(res)

    def create_scheduled_query(
        self,
        res: "bs_td.CreateScheduledQueryResponseTypeDef",
    ) -> "dc_td.CreateScheduledQueryResponse":
        return dc_td.CreateScheduledQueryResponse.make_one(res)

    def delete_scheduled_query(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_account_settings(
        self,
        res: "bs_td.DescribeAccountSettingsResponseTypeDef",
    ) -> "dc_td.DescribeAccountSettingsResponse":
        return dc_td.DescribeAccountSettingsResponse.make_one(res)

    def describe_endpoints(
        self,
        res: "bs_td.DescribeEndpointsResponseTypeDef",
    ) -> "dc_td.DescribeEndpointsResponse":
        return dc_td.DescribeEndpointsResponse.make_one(res)

    def describe_scheduled_query(
        self,
        res: "bs_td.DescribeScheduledQueryResponseTypeDef",
    ) -> "dc_td.DescribeScheduledQueryResponse":
        return dc_td.DescribeScheduledQueryResponse.make_one(res)

    def execute_scheduled_query(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def list_scheduled_queries(
        self,
        res: "bs_td.ListScheduledQueriesResponseTypeDef",
    ) -> "dc_td.ListScheduledQueriesResponse":
        return dc_td.ListScheduledQueriesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def prepare_query(
        self,
        res: "bs_td.PrepareQueryResponseTypeDef",
    ) -> "dc_td.PrepareQueryResponse":
        return dc_td.PrepareQueryResponse.make_one(res)

    def query(
        self,
        res: "bs_td.QueryResponseTypeDef",
    ) -> "dc_td.QueryResponse":
        return dc_td.QueryResponse.make_one(res)

    def update_account_settings(
        self,
        res: "bs_td.UpdateAccountSettingsResponseTypeDef",
    ) -> "dc_td.UpdateAccountSettingsResponse":
        return dc_td.UpdateAccountSettingsResponse.make_one(res)

    def update_scheduled_query(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


timestream_query_caster = TIMESTREAM_QUERYCaster()
