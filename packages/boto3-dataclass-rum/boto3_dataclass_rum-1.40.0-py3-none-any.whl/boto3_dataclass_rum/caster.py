# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rum import type_defs as bs_td


class RUMCaster:

    def batch_create_rum_metric_definitions(
        self,
        res: "bs_td.BatchCreateRumMetricDefinitionsResponseTypeDef",
    ) -> "dc_td.BatchCreateRumMetricDefinitionsResponse":
        return dc_td.BatchCreateRumMetricDefinitionsResponse.make_one(res)

    def batch_delete_rum_metric_definitions(
        self,
        res: "bs_td.BatchDeleteRumMetricDefinitionsResponseTypeDef",
    ) -> "dc_td.BatchDeleteRumMetricDefinitionsResponse":
        return dc_td.BatchDeleteRumMetricDefinitionsResponse.make_one(res)

    def batch_get_rum_metric_definitions(
        self,
        res: "bs_td.BatchGetRumMetricDefinitionsResponseTypeDef",
    ) -> "dc_td.BatchGetRumMetricDefinitionsResponse":
        return dc_td.BatchGetRumMetricDefinitionsResponse.make_one(res)

    def create_app_monitor(
        self,
        res: "bs_td.CreateAppMonitorResponseTypeDef",
    ) -> "dc_td.CreateAppMonitorResponse":
        return dc_td.CreateAppMonitorResponse.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.DeleteResourcePolicyResponseTypeDef",
    ) -> "dc_td.DeleteResourcePolicyResponse":
        return dc_td.DeleteResourcePolicyResponse.make_one(res)

    def get_app_monitor(
        self,
        res: "bs_td.GetAppMonitorResponseTypeDef",
    ) -> "dc_td.GetAppMonitorResponse":
        return dc_td.GetAppMonitorResponse.make_one(res)

    def get_app_monitor_data(
        self,
        res: "bs_td.GetAppMonitorDataResponseTypeDef",
    ) -> "dc_td.GetAppMonitorDataResponse":
        return dc_td.GetAppMonitorDataResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def list_app_monitors(
        self,
        res: "bs_td.ListAppMonitorsResponseTypeDef",
    ) -> "dc_td.ListAppMonitorsResponse":
        return dc_td.ListAppMonitorsResponse.make_one(res)

    def list_rum_metrics_destinations(
        self,
        res: "bs_td.ListRumMetricsDestinationsResponseTypeDef",
    ) -> "dc_td.ListRumMetricsDestinationsResponse":
        return dc_td.ListRumMetricsDestinationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)


rum_caster = RUMCaster()
