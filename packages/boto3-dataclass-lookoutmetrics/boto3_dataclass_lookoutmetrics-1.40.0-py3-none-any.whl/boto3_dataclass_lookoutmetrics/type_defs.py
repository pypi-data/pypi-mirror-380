# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lookoutmetrics import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class LambdaConfiguration:
    boto3_raw_data: "type_defs.LambdaConfigurationTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    LambdaArn = field("LambdaArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SNSConfiguration:
    boto3_raw_data: "type_defs.SNSConfigurationTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    SnsTopicArn = field("SnsTopicArn")
    SnsFormat = field("SnsFormat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SNSConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SNSConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.ActivateAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActivateAnomalyDetectorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateAnomalyDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionFilterOutput:
    boto3_raw_data: "type_defs.DimensionFilterOutputTypeDef" = dataclasses.field()

    DimensionName = field("DimensionName")
    DimensionValueList = field("DimensionValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DimensionFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionFilter:
    boto3_raw_data: "type_defs.DimensionFilterTypeDef" = dataclasses.field()

    DimensionName = field("DimensionName")
    DimensionValueList = field("DimensionValueList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlertSummary:
    boto3_raw_data: "type_defs.AlertSummaryTypeDef" = dataclasses.field()

    AlertArn = field("AlertArn")
    AnomalyDetectorArn = field("AnomalyDetectorArn")
    AlertName = field("AlertName")
    AlertSensitivityThreshold = field("AlertSensitivityThreshold")
    AlertType = field("AlertType")
    AlertStatus = field("AlertStatus")
    LastModificationTime = field("LastModificationTime")
    CreationTime = field("CreationTime")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlertSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlertSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyDetectorConfigSummary:
    boto3_raw_data: "type_defs.AnomalyDetectorConfigSummaryTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorFrequency = field("AnomalyDetectorFrequency")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyDetectorConfigSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyDetectorConfigSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyDetectorConfig:
    boto3_raw_data: "type_defs.AnomalyDetectorConfigTypeDef" = dataclasses.field()

    AnomalyDetectorFrequency = field("AnomalyDetectorFrequency")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyDetectorConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyDetectorConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyDetectorSummary:
    boto3_raw_data: "type_defs.AnomalyDetectorSummaryTypeDef" = dataclasses.field()

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    AnomalyDetectorName = field("AnomalyDetectorName")
    AnomalyDetectorDescription = field("AnomalyDetectorDescription")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    Status = field("Status")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyDetectorSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyDetectorSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItemizedMetricStats:
    boto3_raw_data: "type_defs.ItemizedMetricStatsTypeDef" = dataclasses.field()

    MetricName = field("MetricName")
    OccurrenceCount = field("OccurrenceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ItemizedMetricStatsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ItemizedMetricStatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyGroupSummary:
    boto3_raw_data: "type_defs.AnomalyGroupSummaryTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    AnomalyGroupId = field("AnomalyGroupId")
    AnomalyGroupScore = field("AnomalyGroupScore")
    PrimaryMetricName = field("PrimaryMetricName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyGroupTimeSeriesFeedback:
    boto3_raw_data: "type_defs.AnomalyGroupTimeSeriesFeedbackTypeDef" = (
        dataclasses.field()
    )

    AnomalyGroupId = field("AnomalyGroupId")
    TimeSeriesId = field("TimeSeriesId")
    IsAnomaly = field("IsAnomaly")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AnomalyGroupTimeSeriesFeedbackTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyGroupTimeSeriesFeedbackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyGroupTimeSeries:
    boto3_raw_data: "type_defs.AnomalyGroupTimeSeriesTypeDef" = dataclasses.field()

    AnomalyGroupId = field("AnomalyGroupId")
    TimeSeriesId = field("TimeSeriesId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyGroupTimeSeriesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyGroupTimeSeriesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppFlowConfig:
    boto3_raw_data: "type_defs.AppFlowConfigTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    FlowName = field("FlowName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppFlowConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppFlowConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackTestConfiguration:
    boto3_raw_data: "type_defs.BackTestConfigurationTypeDef" = dataclasses.field()

    RunBackTestMode = field("RunBackTestMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackTestConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackTestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValue:
    boto3_raw_data: "type_defs.AttributeValueTypeDef" = dataclasses.field()

    S = field("S")
    N = field("N")
    B = field("B")
    SS = field("SS")
    NS = field("NS")
    BS = field("BS")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoDetectionS3SourceConfig:
    boto3_raw_data: "type_defs.AutoDetectionS3SourceConfigTypeDef" = dataclasses.field()

    TemplatedPathList = field("TemplatedPathList")
    HistoricalDataPathList = field("HistoricalDataPathList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoDetectionS3SourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoDetectionS3SourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackTestAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.BackTestAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BackTestAnomalyDetectorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackTestAnomalyDetectorRequestTypeDef"]
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
class Metric:
    boto3_raw_data: "type_defs.MetricTypeDef" = dataclasses.field()

    MetricName = field("MetricName")
    AggregationFunction = field("AggregationFunction")
    Namespace = field("Namespace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestampColumn:
    boto3_raw_data: "type_defs.TimestampColumnTypeDef" = dataclasses.field()

    ColumnName = field("ColumnName")
    ColumnFormat = field("ColumnFormat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimestampColumnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimestampColumnTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CsvFormatDescriptorOutput:
    boto3_raw_data: "type_defs.CsvFormatDescriptorOutputTypeDef" = dataclasses.field()

    FileCompression = field("FileCompression")
    Charset = field("Charset")
    ContainsHeader = field("ContainsHeader")
    Delimiter = field("Delimiter")
    HeaderList = field("HeaderList")
    QuoteSymbol = field("QuoteSymbol")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CsvFormatDescriptorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CsvFormatDescriptorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CsvFormatDescriptor:
    boto3_raw_data: "type_defs.CsvFormatDescriptorTypeDef" = dataclasses.field()

    FileCompression = field("FileCompression")
    Charset = field("Charset")
    ContainsHeader = field("ContainsHeader")
    Delimiter = field("Delimiter")
    HeaderList = field("HeaderList")
    QuoteSymbol = field("QuoteSymbol")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CsvFormatDescriptorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CsvFormatDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataQualityMetric:
    boto3_raw_data: "type_defs.DataQualityMetricTypeDef" = dataclasses.field()

    MetricType = field("MetricType")
    MetricDescription = field("MetricDescription")
    RelatedColumnName = field("RelatedColumnName")
    MetricValue = field("MetricValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataQualityMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataQualityMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.DeactivateAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeactivateAnomalyDetectorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateAnomalyDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAlertRequest:
    boto3_raw_data: "type_defs.DeleteAlertRequestTypeDef" = dataclasses.field()

    AlertArn = field("AlertArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAlertRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAlertRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.DeleteAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAnomalyDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnomalyDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlertRequest:
    boto3_raw_data: "type_defs.DescribeAlertRequestTypeDef" = dataclasses.field()

    AlertArn = field("AlertArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlertRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlertRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnomalyDetectionExecutionsRequest:
    boto3_raw_data: "type_defs.DescribeAnomalyDetectionExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    Timestamp = field("Timestamp")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAnomalyDetectionExecutionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnomalyDetectionExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionStatus:
    boto3_raw_data: "type_defs.ExecutionStatusTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    Status = field("Status")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExecutionStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.DescribeAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAnomalyDetectorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnomalyDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetricSetRequest:
    boto3_raw_data: "type_defs.DescribeMetricSetRequestTypeDef" = dataclasses.field()

    MetricSetArn = field("MetricSetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMetricSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetricSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionValueContribution:
    boto3_raw_data: "type_defs.DimensionValueContributionTypeDef" = dataclasses.field()

    DimensionValue = field("DimensionValue")
    ContributionScore = field("ContributionScore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DimensionValueContributionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionValueContributionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionNameValue:
    boto3_raw_data: "type_defs.DimensionNameValueTypeDef" = dataclasses.field()

    DimensionName = field("DimensionName")
    DimensionValue = field("DimensionValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DimensionNameValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionNameValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JsonFormatDescriptor:
    boto3_raw_data: "type_defs.JsonFormatDescriptorTypeDef" = dataclasses.field()

    FileCompression = field("FileCompression")
    Charset = field("Charset")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JsonFormatDescriptorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JsonFormatDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    DimensionValue = field("DimensionValue")
    FilterOperation = field("FilterOperation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomalyGroupRequest:
    boto3_raw_data: "type_defs.GetAnomalyGroupRequestTypeDef" = dataclasses.field()

    AnomalyGroupId = field("AnomalyGroupId")
    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnomalyGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomalyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataQualityMetricsRequest:
    boto3_raw_data: "type_defs.GetDataQualityMetricsRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    MetricSetArn = field("MetricSetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataQualityMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataQualityMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesFeedback:
    boto3_raw_data: "type_defs.TimeSeriesFeedbackTypeDef" = dataclasses.field()

    TimeSeriesId = field("TimeSeriesId")
    IsAnomaly = field("IsAnomaly")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesFeedbackTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesFeedbackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterMetricImpactDetails:
    boto3_raw_data: "type_defs.InterMetricImpactDetailsTypeDef" = dataclasses.field()

    MetricName = field("MetricName")
    AnomalyGroupId = field("AnomalyGroupId")
    RelationshipType = field("RelationshipType")
    ContributionPercentage = field("ContributionPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InterMetricImpactDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterMetricImpactDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlertsRequest:
    boto3_raw_data: "type_defs.ListAlertsRequestTypeDef" = dataclasses.field()

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAlertsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlertsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalyDetectorsRequest:
    boto3_raw_data: "type_defs.ListAnomalyDetectorsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnomalyDetectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalyDetectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalyGroupRelatedMetricsRequest:
    boto3_raw_data: "type_defs.ListAnomalyGroupRelatedMetricsRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    AnomalyGroupId = field("AnomalyGroupId")
    RelationshipTypeFilter = field("RelationshipTypeFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnomalyGroupRelatedMetricsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalyGroupRelatedMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalyGroupSummariesRequest:
    boto3_raw_data: "type_defs.ListAnomalyGroupSummariesRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    SensitivityThreshold = field("SensitivityThreshold")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnomalyGroupSummariesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalyGroupSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalyGroupTimeSeriesRequest:
    boto3_raw_data: "type_defs.ListAnomalyGroupTimeSeriesRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    AnomalyGroupId = field("AnomalyGroupId")
    MetricName = field("MetricName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnomalyGroupTimeSeriesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalyGroupTimeSeriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricSetsRequest:
    boto3_raw_data: "type_defs.ListMetricSetsRequestTypeDef" = dataclasses.field()

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMetricSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricSetSummary:
    boto3_raw_data: "type_defs.MetricSetSummaryTypeDef" = dataclasses.field()

    MetricSetArn = field("MetricSetArn")
    AnomalyDetectorArn = field("AnomalyDetectorArn")
    MetricSetDescription = field("MetricSetDescription")
    MetricSetName = field("MetricSetName")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricSetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricSetSummaryTypeDef"]
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
class VpcConfigurationOutput:
    boto3_raw_data: "type_defs.VpcConfigurationOutputTypeDef" = dataclasses.field()

    SubnetIdList = field("SubnetIdList")
    SecurityGroupIdList = field("SecurityGroupIdList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfiguration:
    boto3_raw_data: "type_defs.VpcConfigurationTypeDef" = dataclasses.field()

    SubnetIdList = field("SubnetIdList")
    SecurityGroupIdList = field("SecurityGroupIdList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationTypeDef"]
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
class Action:
    boto3_raw_data: "type_defs.ActionTypeDef" = dataclasses.field()

    @cached_property
    def SNSConfiguration(self):  # pragma: no cover
        return SNSConfiguration.make_one(self.boto3_raw_data["SNSConfiguration"])

    @cached_property
    def LambdaConfiguration(self):  # pragma: no cover
        return LambdaConfiguration.make_one(self.boto3_raw_data["LambdaConfiguration"])

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
class AlertFiltersOutput:
    boto3_raw_data: "type_defs.AlertFiltersOutputTypeDef" = dataclasses.field()

    MetricList = field("MetricList")

    @cached_property
    def DimensionFilterList(self):  # pragma: no cover
        return DimensionFilterOutput.make_many(
            self.boto3_raw_data["DimensionFilterList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlertFiltersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlertFiltersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlertFilters:
    boto3_raw_data: "type_defs.AlertFiltersTypeDef" = dataclasses.field()

    MetricList = field("MetricList")

    @cached_property
    def DimensionFilterList(self):  # pragma: no cover
        return DimensionFilter.make_many(self.boto3_raw_data["DimensionFilterList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlertFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlertFiltersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.CreateAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorName = field("AnomalyDetectorName")

    @cached_property
    def AnomalyDetectorConfig(self):  # pragma: no cover
        return AnomalyDetectorConfig.make_one(
            self.boto3_raw_data["AnomalyDetectorConfig"]
        )

    AnomalyDetectorDescription = field("AnomalyDetectorDescription")
    KmsKeyArn = field("KmsKeyArn")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAnomalyDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnomalyDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.UpdateAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    KmsKeyArn = field("KmsKeyArn")
    AnomalyDetectorDescription = field("AnomalyDetectorDescription")

    @cached_property
    def AnomalyDetectorConfig(self):  # pragma: no cover
        return AnomalyDetectorConfig.make_one(
            self.boto3_raw_data["AnomalyDetectorConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAnomalyDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnomalyDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyGroupStatistics:
    boto3_raw_data: "type_defs.AnomalyGroupStatisticsTypeDef" = dataclasses.field()

    EvaluationStartDate = field("EvaluationStartDate")
    TotalCount = field("TotalCount")

    @cached_property
    def ItemizedMetricStatsList(self):  # pragma: no cover
        return ItemizedMetricStats.make_many(
            self.boto3_raw_data["ItemizedMetricStatsList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyGroupStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyGroupStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFeedbackRequest:
    boto3_raw_data: "type_defs.PutFeedbackRequestTypeDef" = dataclasses.field()

    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @cached_property
    def AnomalyGroupTimeSeriesFeedback(self):  # pragma: no cover
        return AnomalyGroupTimeSeriesFeedback.make_one(
            self.boto3_raw_data["AnomalyGroupTimeSeriesFeedback"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutFeedbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFeedbackRequest:
    boto3_raw_data: "type_defs.GetFeedbackRequestTypeDef" = dataclasses.field()

    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @cached_property
    def AnomalyGroupTimeSeriesFeedback(self):  # pragma: no cover
        return AnomalyGroupTimeSeries.make_one(
            self.boto3_raw_data["AnomalyGroupTimeSeriesFeedback"]
        )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFeedbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AthenaSourceConfig:
    boto3_raw_data: "type_defs.AthenaSourceConfigTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    DatabaseName = field("DatabaseName")
    DataCatalog = field("DataCatalog")
    TableName = field("TableName")
    WorkGroupName = field("WorkGroupName")
    S3ResultsPath = field("S3ResultsPath")

    @cached_property
    def BackTestConfiguration(self):  # pragma: no cover
        return BackTestConfiguration.make_one(
            self.boto3_raw_data["BackTestConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AthenaSourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AthenaSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchConfig:
    boto3_raw_data: "type_defs.CloudWatchConfigTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")

    @cached_property
    def BackTestConfiguration(self):  # pragma: no cover
        return BackTestConfiguration.make_one(
            self.boto3_raw_data["BackTestConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloudWatchConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedField:
    boto3_raw_data: "type_defs.DetectedFieldTypeDef" = dataclasses.field()

    @cached_property
    def Value(self):  # pragma: no cover
        return AttributeValue.make_one(self.boto3_raw_data["Value"])

    Confidence = field("Confidence")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectedFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetectedFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoDetectionMetricSource:
    boto3_raw_data: "type_defs.AutoDetectionMetricSourceTypeDef" = dataclasses.field()

    @cached_property
    def S3SourceConfig(self):  # pragma: no cover
        return AutoDetectionS3SourceConfig.make_one(
            self.boto3_raw_data["S3SourceConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoDetectionMetricSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoDetectionMetricSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAlertResponse:
    boto3_raw_data: "type_defs.CreateAlertResponseTypeDef" = dataclasses.field()

    AlertArn = field("AlertArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAlertResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAlertResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnomalyDetectorResponse:
    boto3_raw_data: "type_defs.CreateAnomalyDetectorResponseTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAnomalyDetectorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnomalyDetectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMetricSetResponse:
    boto3_raw_data: "type_defs.CreateMetricSetResponseTypeDef" = dataclasses.field()

    MetricSetArn = field("MetricSetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMetricSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMetricSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnomalyDetectorResponse:
    boto3_raw_data: "type_defs.DescribeAnomalyDetectorResponseTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    AnomalyDetectorName = field("AnomalyDetectorName")
    AnomalyDetectorDescription = field("AnomalyDetectorDescription")

    @cached_property
    def AnomalyDetectorConfig(self):  # pragma: no cover
        return AnomalyDetectorConfigSummary.make_one(
            self.boto3_raw_data["AnomalyDetectorConfig"]
        )

    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    Status = field("Status")
    FailureReason = field("FailureReason")
    KmsKeyArn = field("KmsKeyArn")
    FailureType = field("FailureType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAnomalyDetectorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnomalyDetectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSampleDataResponse:
    boto3_raw_data: "type_defs.GetSampleDataResponseTypeDef" = dataclasses.field()

    HeaderValues = field("HeaderValues")
    SampleRows = field("SampleRows")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSampleDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSampleDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlertsResponse:
    boto3_raw_data: "type_defs.ListAlertsResponseTypeDef" = dataclasses.field()

    @cached_property
    def AlertSummaryList(self):  # pragma: no cover
        return AlertSummary.make_many(self.boto3_raw_data["AlertSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAlertsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlertsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalyDetectorsResponse:
    boto3_raw_data: "type_defs.ListAnomalyDetectorsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnomalyDetectorSummaryList(self):  # pragma: no cover
        return AnomalyDetectorSummary.make_many(
            self.boto3_raw_data["AnomalyDetectorSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnomalyDetectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalyDetectorsResponseTypeDef"]
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
class UpdateAlertResponse:
    boto3_raw_data: "type_defs.UpdateAlertResponseTypeDef" = dataclasses.field()

    AlertArn = field("AlertArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAlertResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAlertResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnomalyDetectorResponse:
    boto3_raw_data: "type_defs.UpdateAnomalyDetectorResponseTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAnomalyDetectorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnomalyDetectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMetricSetResponse:
    boto3_raw_data: "type_defs.UpdateMetricSetResponseTypeDef" = dataclasses.field()

    MetricSetArn = field("MetricSetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMetricSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMetricSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricSetDataQualityMetric:
    boto3_raw_data: "type_defs.MetricSetDataQualityMetricTypeDef" = dataclasses.field()

    MetricSetArn = field("MetricSetArn")

    @cached_property
    def DataQualityMetricList(self):  # pragma: no cover
        return DataQualityMetric.make_many(self.boto3_raw_data["DataQualityMetricList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricSetDataQualityMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricSetDataQualityMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnomalyDetectionExecutionsResponse:
    boto3_raw_data: "type_defs.DescribeAnomalyDetectionExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ExecutionList(self):  # pragma: no cover
        return ExecutionStatus.make_many(self.boto3_raw_data["ExecutionList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAnomalyDetectionExecutionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnomalyDetectionExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionContribution:
    boto3_raw_data: "type_defs.DimensionContributionTypeDef" = dataclasses.field()

    DimensionName = field("DimensionName")

    @cached_property
    def DimensionValueContributionList(self):  # pragma: no cover
        return DimensionValueContribution.make_many(
            self.boto3_raw_data["DimensionValueContributionList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DimensionContributionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionContributionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeries:
    boto3_raw_data: "type_defs.TimeSeriesTypeDef" = dataclasses.field()

    TimeSeriesId = field("TimeSeriesId")

    @cached_property
    def DimensionList(self):  # pragma: no cover
        return DimensionNameValue.make_many(self.boto3_raw_data["DimensionList"])

    MetricValueList = field("MetricValueList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeSeriesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileFormatDescriptorOutput:
    boto3_raw_data: "type_defs.FileFormatDescriptorOutputTypeDef" = dataclasses.field()

    @cached_property
    def CsvFormatDescriptor(self):  # pragma: no cover
        return CsvFormatDescriptorOutput.make_one(
            self.boto3_raw_data["CsvFormatDescriptor"]
        )

    @cached_property
    def JsonFormatDescriptor(self):  # pragma: no cover
        return JsonFormatDescriptor.make_one(
            self.boto3_raw_data["JsonFormatDescriptor"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileFormatDescriptorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileFormatDescriptorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricSetDimensionFilterOutput:
    boto3_raw_data: "type_defs.MetricSetDimensionFilterOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def FilterList(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["FilterList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MetricSetDimensionFilterOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricSetDimensionFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricSetDimensionFilter:
    boto3_raw_data: "type_defs.MetricSetDimensionFilterTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def FilterList(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["FilterList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricSetDimensionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricSetDimensionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFeedbackResponse:
    boto3_raw_data: "type_defs.GetFeedbackResponseTypeDef" = dataclasses.field()

    @cached_property
    def AnomalyGroupTimeSeriesFeedback(self):  # pragma: no cover
        return TimeSeriesFeedback.make_many(
            self.boto3_raw_data["AnomalyGroupTimeSeriesFeedback"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFeedbackResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFeedbackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalyGroupRelatedMetricsResponse:
    boto3_raw_data: "type_defs.ListAnomalyGroupRelatedMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InterMetricImpactList(self):  # pragma: no cover
        return InterMetricImpactDetails.make_many(
            self.boto3_raw_data["InterMetricImpactList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnomalyGroupRelatedMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalyGroupRelatedMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricSetsResponse:
    boto3_raw_data: "type_defs.ListMetricSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def MetricSetSummaryList(self):  # pragma: no cover
        return MetricSetSummary.make_many(self.boto3_raw_data["MetricSetSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMetricSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSSourceConfigOutput:
    boto3_raw_data: "type_defs.RDSSourceConfigOutputTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DatabaseHost = field("DatabaseHost")
    DatabasePort = field("DatabasePort")
    SecretManagerArn = field("SecretManagerArn")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    RoleArn = field("RoleArn")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfigurationOutput.make_one(self.boto3_raw_data["VpcConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RDSSourceConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSSourceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftSourceConfigOutput:
    boto3_raw_data: "type_defs.RedshiftSourceConfigOutputTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    DatabaseHost = field("DatabaseHost")
    DatabasePort = field("DatabasePort")
    SecretManagerArn = field("SecretManagerArn")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    RoleArn = field("RoleArn")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfigurationOutput.make_one(self.boto3_raw_data["VpcConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftSourceConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftSourceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSSourceConfig:
    boto3_raw_data: "type_defs.RDSSourceConfigTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DatabaseHost = field("DatabaseHost")
    DatabasePort = field("DatabasePort")
    SecretManagerArn = field("SecretManagerArn")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    RoleArn = field("RoleArn")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["VpcConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RDSSourceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RDSSourceConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftSourceConfig:
    boto3_raw_data: "type_defs.RedshiftSourceConfigTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    DatabaseHost = field("DatabaseHost")
    DatabasePort = field("DatabasePort")
    SecretManagerArn = field("SecretManagerArn")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    RoleArn = field("RoleArn")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["VpcConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftSourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Alert:
    boto3_raw_data: "type_defs.AlertTypeDef" = dataclasses.field()

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    AlertDescription = field("AlertDescription")
    AlertArn = field("AlertArn")
    AnomalyDetectorArn = field("AnomalyDetectorArn")
    AlertName = field("AlertName")
    AlertSensitivityThreshold = field("AlertSensitivityThreshold")
    AlertType = field("AlertType")
    AlertStatus = field("AlertStatus")
    LastModificationTime = field("LastModificationTime")
    CreationTime = field("CreationTime")

    @cached_property
    def AlertFilters(self):  # pragma: no cover
        return AlertFiltersOutput.make_one(self.boto3_raw_data["AlertFilters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlertTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlertTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalyGroupSummariesResponse:
    boto3_raw_data: "type_defs.ListAnomalyGroupSummariesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnomalyGroupSummaryList(self):  # pragma: no cover
        return AnomalyGroupSummary.make_many(
            self.boto3_raw_data["AnomalyGroupSummaryList"]
        )

    @cached_property
    def AnomalyGroupStatistics(self):  # pragma: no cover
        return AnomalyGroupStatistics.make_one(
            self.boto3_raw_data["AnomalyGroupStatistics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnomalyGroupSummariesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalyGroupSummariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedCsvFormatDescriptor:
    boto3_raw_data: "type_defs.DetectedCsvFormatDescriptorTypeDef" = dataclasses.field()

    @cached_property
    def FileCompression(self):  # pragma: no cover
        return DetectedField.make_one(self.boto3_raw_data["FileCompression"])

    @cached_property
    def Charset(self):  # pragma: no cover
        return DetectedField.make_one(self.boto3_raw_data["Charset"])

    @cached_property
    def ContainsHeader(self):  # pragma: no cover
        return DetectedField.make_one(self.boto3_raw_data["ContainsHeader"])

    @cached_property
    def Delimiter(self):  # pragma: no cover
        return DetectedField.make_one(self.boto3_raw_data["Delimiter"])

    @cached_property
    def HeaderList(self):  # pragma: no cover
        return DetectedField.make_one(self.boto3_raw_data["HeaderList"])

    @cached_property
    def QuoteSymbol(self):  # pragma: no cover
        return DetectedField.make_one(self.boto3_raw_data["QuoteSymbol"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectedCsvFormatDescriptorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectedCsvFormatDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedJsonFormatDescriptor:
    boto3_raw_data: "type_defs.DetectedJsonFormatDescriptorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FileCompression(self):  # pragma: no cover
        return DetectedField.make_one(self.boto3_raw_data["FileCompression"])

    @cached_property
    def Charset(self):  # pragma: no cover
        return DetectedField.make_one(self.boto3_raw_data["Charset"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectedJsonFormatDescriptorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectedJsonFormatDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectMetricSetConfigRequest:
    boto3_raw_data: "type_defs.DetectMetricSetConfigRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @cached_property
    def AutoDetectionMetricSource(self):  # pragma: no cover
        return AutoDetectionMetricSource.make_one(
            self.boto3_raw_data["AutoDetectionMetricSource"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectMetricSetConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectMetricSetConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileFormatDescriptor:
    boto3_raw_data: "type_defs.FileFormatDescriptorTypeDef" = dataclasses.field()

    CsvFormatDescriptor = field("CsvFormatDescriptor")

    @cached_property
    def JsonFormatDescriptor(self):  # pragma: no cover
        return JsonFormatDescriptor.make_one(
            self.boto3_raw_data["JsonFormatDescriptor"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileFormatDescriptorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileFormatDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyDetectorDataQualityMetric:
    boto3_raw_data: "type_defs.AnomalyDetectorDataQualityMetricTypeDef" = (
        dataclasses.field()
    )

    StartTimestamp = field("StartTimestamp")

    @cached_property
    def MetricSetDataQualityMetricList(self):  # pragma: no cover
        return MetricSetDataQualityMetric.make_many(
            self.boto3_raw_data["MetricSetDataQualityMetricList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AnomalyDetectorDataQualityMetricTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyDetectorDataQualityMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContributionMatrix:
    boto3_raw_data: "type_defs.ContributionMatrixTypeDef" = dataclasses.field()

    @cached_property
    def DimensionContributionList(self):  # pragma: no cover
        return DimensionContribution.make_many(
            self.boto3_raw_data["DimensionContributionList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContributionMatrixTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContributionMatrixTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalyGroupTimeSeriesResponse:
    boto3_raw_data: "type_defs.ListAnomalyGroupTimeSeriesResponseTypeDef" = (
        dataclasses.field()
    )

    AnomalyGroupId = field("AnomalyGroupId")
    MetricName = field("MetricName")
    TimestampList = field("TimestampList")

    @cached_property
    def TimeSeriesList(self):  # pragma: no cover
        return TimeSeries.make_many(self.boto3_raw_data["TimeSeriesList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnomalyGroupTimeSeriesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalyGroupTimeSeriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SourceConfigOutput:
    boto3_raw_data: "type_defs.S3SourceConfigOutputTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    TemplatedPathList = field("TemplatedPathList")
    HistoricalDataPathList = field("HistoricalDataPathList")

    @cached_property
    def FileFormatDescriptor(self):  # pragma: no cover
        return FileFormatDescriptorOutput.make_one(
            self.boto3_raw_data["FileFormatDescriptor"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3SourceConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3SourceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlertResponse:
    boto3_raw_data: "type_defs.DescribeAlertResponseTypeDef" = dataclasses.field()

    @cached_property
    def Alert(self):  # pragma: no cover
        return Alert.make_one(self.boto3_raw_data["Alert"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlertResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlertResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAlertRequest:
    boto3_raw_data: "type_defs.CreateAlertRequestTypeDef" = dataclasses.field()

    AlertName = field("AlertName")
    AnomalyDetectorArn = field("AnomalyDetectorArn")

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    AlertSensitivityThreshold = field("AlertSensitivityThreshold")
    AlertDescription = field("AlertDescription")
    Tags = field("Tags")
    AlertFilters = field("AlertFilters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAlertRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAlertRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAlertRequest:
    boto3_raw_data: "type_defs.UpdateAlertRequestTypeDef" = dataclasses.field()

    AlertArn = field("AlertArn")
    AlertDescription = field("AlertDescription")
    AlertSensitivityThreshold = field("AlertSensitivityThreshold")

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    AlertFilters = field("AlertFilters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAlertRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAlertRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedFileFormatDescriptor:
    boto3_raw_data: "type_defs.DetectedFileFormatDescriptorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CsvFormatDescriptor(self):  # pragma: no cover
        return DetectedCsvFormatDescriptor.make_one(
            self.boto3_raw_data["CsvFormatDescriptor"]
        )

    @cached_property
    def JsonFormatDescriptor(self):  # pragma: no cover
        return DetectedJsonFormatDescriptor.make_one(
            self.boto3_raw_data["JsonFormatDescriptor"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectedFileFormatDescriptorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectedFileFormatDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SourceConfig:
    boto3_raw_data: "type_defs.S3SourceConfigTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    TemplatedPathList = field("TemplatedPathList")
    HistoricalDataPathList = field("HistoricalDataPathList")

    @cached_property
    def FileFormatDescriptor(self):  # pragma: no cover
        return FileFormatDescriptor.make_one(
            self.boto3_raw_data["FileFormatDescriptor"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3SourceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3SourceConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataQualityMetricsResponse:
    boto3_raw_data: "type_defs.GetDataQualityMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnomalyDetectorDataQualityMetricList(self):  # pragma: no cover
        return AnomalyDetectorDataQualityMetric.make_many(
            self.boto3_raw_data["AnomalyDetectorDataQualityMetricList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataQualityMetricsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataQualityMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricLevelImpact:
    boto3_raw_data: "type_defs.MetricLevelImpactTypeDef" = dataclasses.field()

    MetricName = field("MetricName")
    NumTimeSeries = field("NumTimeSeries")

    @cached_property
    def ContributionMatrix(self):  # pragma: no cover
        return ContributionMatrix.make_one(self.boto3_raw_data["ContributionMatrix"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricLevelImpactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricLevelImpactTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricSourceOutput:
    boto3_raw_data: "type_defs.MetricSourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def S3SourceConfig(self):  # pragma: no cover
        return S3SourceConfigOutput.make_one(self.boto3_raw_data["S3SourceConfig"])

    @cached_property
    def AppFlowConfig(self):  # pragma: no cover
        return AppFlowConfig.make_one(self.boto3_raw_data["AppFlowConfig"])

    @cached_property
    def CloudWatchConfig(self):  # pragma: no cover
        return CloudWatchConfig.make_one(self.boto3_raw_data["CloudWatchConfig"])

    @cached_property
    def RDSSourceConfig(self):  # pragma: no cover
        return RDSSourceConfigOutput.make_one(self.boto3_raw_data["RDSSourceConfig"])

    @cached_property
    def RedshiftSourceConfig(self):  # pragma: no cover
        return RedshiftSourceConfigOutput.make_one(
            self.boto3_raw_data["RedshiftSourceConfig"]
        )

    @cached_property
    def AthenaSourceConfig(self):  # pragma: no cover
        return AthenaSourceConfig.make_one(self.boto3_raw_data["AthenaSourceConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedS3SourceConfig:
    boto3_raw_data: "type_defs.DetectedS3SourceConfigTypeDef" = dataclasses.field()

    @cached_property
    def FileFormatDescriptor(self):  # pragma: no cover
        return DetectedFileFormatDescriptor.make_one(
            self.boto3_raw_data["FileFormatDescriptor"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectedS3SourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectedS3SourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SampleDataS3SourceConfig:
    boto3_raw_data: "type_defs.SampleDataS3SourceConfigTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    FileFormatDescriptor = field("FileFormatDescriptor")
    TemplatedPathList = field("TemplatedPathList")
    HistoricalDataPathList = field("HistoricalDataPathList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SampleDataS3SourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SampleDataS3SourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricSource:
    boto3_raw_data: "type_defs.MetricSourceTypeDef" = dataclasses.field()

    @cached_property
    def S3SourceConfig(self):  # pragma: no cover
        return S3SourceConfig.make_one(self.boto3_raw_data["S3SourceConfig"])

    @cached_property
    def AppFlowConfig(self):  # pragma: no cover
        return AppFlowConfig.make_one(self.boto3_raw_data["AppFlowConfig"])

    @cached_property
    def CloudWatchConfig(self):  # pragma: no cover
        return CloudWatchConfig.make_one(self.boto3_raw_data["CloudWatchConfig"])

    @cached_property
    def RDSSourceConfig(self):  # pragma: no cover
        return RDSSourceConfig.make_one(self.boto3_raw_data["RDSSourceConfig"])

    @cached_property
    def RedshiftSourceConfig(self):  # pragma: no cover
        return RedshiftSourceConfig.make_one(
            self.boto3_raw_data["RedshiftSourceConfig"]
        )

    @cached_property
    def AthenaSourceConfig(self):  # pragma: no cover
        return AthenaSourceConfig.make_one(self.boto3_raw_data["AthenaSourceConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyGroup:
    boto3_raw_data: "type_defs.AnomalyGroupTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    AnomalyGroupId = field("AnomalyGroupId")
    AnomalyGroupScore = field("AnomalyGroupScore")
    PrimaryMetricName = field("PrimaryMetricName")

    @cached_property
    def MetricLevelImpactList(self):  # pragma: no cover
        return MetricLevelImpact.make_many(self.boto3_raw_data["MetricLevelImpactList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetricSetResponse:
    boto3_raw_data: "type_defs.DescribeMetricSetResponseTypeDef" = dataclasses.field()

    MetricSetArn = field("MetricSetArn")
    AnomalyDetectorArn = field("AnomalyDetectorArn")
    MetricSetName = field("MetricSetName")
    MetricSetDescription = field("MetricSetDescription")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    Offset = field("Offset")

    @cached_property
    def MetricList(self):  # pragma: no cover
        return Metric.make_many(self.boto3_raw_data["MetricList"])

    @cached_property
    def TimestampColumn(self):  # pragma: no cover
        return TimestampColumn.make_one(self.boto3_raw_data["TimestampColumn"])

    DimensionList = field("DimensionList")
    MetricSetFrequency = field("MetricSetFrequency")
    Timezone = field("Timezone")

    @cached_property
    def MetricSource(self):  # pragma: no cover
        return MetricSourceOutput.make_one(self.boto3_raw_data["MetricSource"])

    @cached_property
    def DimensionFilterList(self):  # pragma: no cover
        return MetricSetDimensionFilterOutput.make_many(
            self.boto3_raw_data["DimensionFilterList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMetricSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetricSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedMetricSource:
    boto3_raw_data: "type_defs.DetectedMetricSourceTypeDef" = dataclasses.field()

    @cached_property
    def S3SourceConfig(self):  # pragma: no cover
        return DetectedS3SourceConfig.make_one(self.boto3_raw_data["S3SourceConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectedMetricSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectedMetricSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSampleDataRequest:
    boto3_raw_data: "type_defs.GetSampleDataRequestTypeDef" = dataclasses.field()

    @cached_property
    def S3SourceConfig(self):  # pragma: no cover
        return SampleDataS3SourceConfig.make_one(self.boto3_raw_data["S3SourceConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSampleDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSampleDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomalyGroupResponse:
    boto3_raw_data: "type_defs.GetAnomalyGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def AnomalyGroup(self):  # pragma: no cover
        return AnomalyGroup.make_one(self.boto3_raw_data["AnomalyGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnomalyGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomalyGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedMetricSetConfig:
    boto3_raw_data: "type_defs.DetectedMetricSetConfigTypeDef" = dataclasses.field()

    @cached_property
    def Offset(self):  # pragma: no cover
        return DetectedField.make_one(self.boto3_raw_data["Offset"])

    @cached_property
    def MetricSetFrequency(self):  # pragma: no cover
        return DetectedField.make_one(self.boto3_raw_data["MetricSetFrequency"])

    @cached_property
    def MetricSource(self):  # pragma: no cover
        return DetectedMetricSource.make_one(self.boto3_raw_data["MetricSource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectedMetricSetConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectedMetricSetConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMetricSetRequest:
    boto3_raw_data: "type_defs.CreateMetricSetRequestTypeDef" = dataclasses.field()

    AnomalyDetectorArn = field("AnomalyDetectorArn")
    MetricSetName = field("MetricSetName")

    @cached_property
    def MetricList(self):  # pragma: no cover
        return Metric.make_many(self.boto3_raw_data["MetricList"])

    MetricSource = field("MetricSource")
    MetricSetDescription = field("MetricSetDescription")
    Offset = field("Offset")

    @cached_property
    def TimestampColumn(self):  # pragma: no cover
        return TimestampColumn.make_one(self.boto3_raw_data["TimestampColumn"])

    DimensionList = field("DimensionList")
    MetricSetFrequency = field("MetricSetFrequency")
    Timezone = field("Timezone")
    Tags = field("Tags")
    DimensionFilterList = field("DimensionFilterList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMetricSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMetricSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMetricSetRequest:
    boto3_raw_data: "type_defs.UpdateMetricSetRequestTypeDef" = dataclasses.field()

    MetricSetArn = field("MetricSetArn")
    MetricSetDescription = field("MetricSetDescription")

    @cached_property
    def MetricList(self):  # pragma: no cover
        return Metric.make_many(self.boto3_raw_data["MetricList"])

    Offset = field("Offset")

    @cached_property
    def TimestampColumn(self):  # pragma: no cover
        return TimestampColumn.make_one(self.boto3_raw_data["TimestampColumn"])

    DimensionList = field("DimensionList")
    MetricSetFrequency = field("MetricSetFrequency")
    MetricSource = field("MetricSource")
    DimensionFilterList = field("DimensionFilterList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMetricSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMetricSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectMetricSetConfigResponse:
    boto3_raw_data: "type_defs.DetectMetricSetConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DetectedMetricSetConfig(self):  # pragma: no cover
        return DetectedMetricSetConfig.make_one(
            self.boto3_raw_data["DetectedMetricSetConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectMetricSetConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectMetricSetConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
