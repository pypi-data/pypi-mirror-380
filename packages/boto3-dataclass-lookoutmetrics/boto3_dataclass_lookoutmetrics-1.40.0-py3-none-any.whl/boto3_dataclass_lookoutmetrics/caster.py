# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lookoutmetrics import type_defs as bs_td


class LOOKOUTMETRICSCaster:

    def create_alert(
        self,
        res: "bs_td.CreateAlertResponseTypeDef",
    ) -> "dc_td.CreateAlertResponse":
        return dc_td.CreateAlertResponse.make_one(res)

    def create_anomaly_detector(
        self,
        res: "bs_td.CreateAnomalyDetectorResponseTypeDef",
    ) -> "dc_td.CreateAnomalyDetectorResponse":
        return dc_td.CreateAnomalyDetectorResponse.make_one(res)

    def create_metric_set(
        self,
        res: "bs_td.CreateMetricSetResponseTypeDef",
    ) -> "dc_td.CreateMetricSetResponse":
        return dc_td.CreateMetricSetResponse.make_one(res)

    def describe_alert(
        self,
        res: "bs_td.DescribeAlertResponseTypeDef",
    ) -> "dc_td.DescribeAlertResponse":
        return dc_td.DescribeAlertResponse.make_one(res)

    def describe_anomaly_detection_executions(
        self,
        res: "bs_td.DescribeAnomalyDetectionExecutionsResponseTypeDef",
    ) -> "dc_td.DescribeAnomalyDetectionExecutionsResponse":
        return dc_td.DescribeAnomalyDetectionExecutionsResponse.make_one(res)

    def describe_anomaly_detector(
        self,
        res: "bs_td.DescribeAnomalyDetectorResponseTypeDef",
    ) -> "dc_td.DescribeAnomalyDetectorResponse":
        return dc_td.DescribeAnomalyDetectorResponse.make_one(res)

    def describe_metric_set(
        self,
        res: "bs_td.DescribeMetricSetResponseTypeDef",
    ) -> "dc_td.DescribeMetricSetResponse":
        return dc_td.DescribeMetricSetResponse.make_one(res)

    def detect_metric_set_config(
        self,
        res: "bs_td.DetectMetricSetConfigResponseTypeDef",
    ) -> "dc_td.DetectMetricSetConfigResponse":
        return dc_td.DetectMetricSetConfigResponse.make_one(res)

    def get_anomaly_group(
        self,
        res: "bs_td.GetAnomalyGroupResponseTypeDef",
    ) -> "dc_td.GetAnomalyGroupResponse":
        return dc_td.GetAnomalyGroupResponse.make_one(res)

    def get_data_quality_metrics(
        self,
        res: "bs_td.GetDataQualityMetricsResponseTypeDef",
    ) -> "dc_td.GetDataQualityMetricsResponse":
        return dc_td.GetDataQualityMetricsResponse.make_one(res)

    def get_feedback(
        self,
        res: "bs_td.GetFeedbackResponseTypeDef",
    ) -> "dc_td.GetFeedbackResponse":
        return dc_td.GetFeedbackResponse.make_one(res)

    def get_sample_data(
        self,
        res: "bs_td.GetSampleDataResponseTypeDef",
    ) -> "dc_td.GetSampleDataResponse":
        return dc_td.GetSampleDataResponse.make_one(res)

    def list_alerts(
        self,
        res: "bs_td.ListAlertsResponseTypeDef",
    ) -> "dc_td.ListAlertsResponse":
        return dc_td.ListAlertsResponse.make_one(res)

    def list_anomaly_detectors(
        self,
        res: "bs_td.ListAnomalyDetectorsResponseTypeDef",
    ) -> "dc_td.ListAnomalyDetectorsResponse":
        return dc_td.ListAnomalyDetectorsResponse.make_one(res)

    def list_anomaly_group_related_metrics(
        self,
        res: "bs_td.ListAnomalyGroupRelatedMetricsResponseTypeDef",
    ) -> "dc_td.ListAnomalyGroupRelatedMetricsResponse":
        return dc_td.ListAnomalyGroupRelatedMetricsResponse.make_one(res)

    def list_anomaly_group_summaries(
        self,
        res: "bs_td.ListAnomalyGroupSummariesResponseTypeDef",
    ) -> "dc_td.ListAnomalyGroupSummariesResponse":
        return dc_td.ListAnomalyGroupSummariesResponse.make_one(res)

    def list_anomaly_group_time_series(
        self,
        res: "bs_td.ListAnomalyGroupTimeSeriesResponseTypeDef",
    ) -> "dc_td.ListAnomalyGroupTimeSeriesResponse":
        return dc_td.ListAnomalyGroupTimeSeriesResponse.make_one(res)

    def list_metric_sets(
        self,
        res: "bs_td.ListMetricSetsResponseTypeDef",
    ) -> "dc_td.ListMetricSetsResponse":
        return dc_td.ListMetricSetsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_alert(
        self,
        res: "bs_td.UpdateAlertResponseTypeDef",
    ) -> "dc_td.UpdateAlertResponse":
        return dc_td.UpdateAlertResponse.make_one(res)

    def update_anomaly_detector(
        self,
        res: "bs_td.UpdateAnomalyDetectorResponseTypeDef",
    ) -> "dc_td.UpdateAnomalyDetectorResponse":
        return dc_td.UpdateAnomalyDetectorResponse.make_one(res)

    def update_metric_set(
        self,
        res: "bs_td.UpdateMetricSetResponseTypeDef",
    ) -> "dc_td.UpdateMetricSetResponse":
        return dc_td.UpdateMetricSetResponse.make_one(res)


lookoutmetrics_caster = LOOKOUTMETRICSCaster()
