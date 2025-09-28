# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lookoutequipment import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CategoricalValues:
    boto3_raw_data: "type_defs.CategoricalValuesTypeDef" = dataclasses.field()

    Status = field("Status")
    NumberOfCategory = field("NumberOfCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CategoricalValuesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CategoricalValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountPercent:
    boto3_raw_data: "type_defs.CountPercentTypeDef" = dataclasses.field()

    Count = field("Count")
    Percentage = field("Percentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CountPercentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CountPercentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetSchema:
    boto3_raw_data: "type_defs.DatasetSchemaTypeDef" = dataclasses.field()

    InlineDataSchema = field("InlineDataSchema")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetSchemaTypeDef"]],
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
class DataPreProcessingConfiguration:
    boto3_raw_data: "type_defs.DataPreProcessingConfigurationTypeDef" = (
        dataclasses.field()
    )

    TargetSamplingRate = field("TargetSamplingRate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataPreProcessingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataPreProcessingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DuplicateTimestamps:
    boto3_raw_data: "type_defs.DuplicateTimestampsTypeDef" = dataclasses.field()

    TotalNumberOfDuplicateTimestamps = field("TotalNumberOfDuplicateTimestamps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DuplicateTimestampsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DuplicateTimestampsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvalidSensorData:
    boto3_raw_data: "type_defs.InvalidSensorDataTypeDef" = dataclasses.field()

    AffectedSensorCount = field("AffectedSensorCount")
    TotalNumberOfInvalidValues = field("TotalNumberOfInvalidValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvalidSensorDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvalidSensorDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MissingSensorData:
    boto3_raw_data: "type_defs.MissingSensorDataTypeDef" = dataclasses.field()

    AffectedSensorCount = field("AffectedSensorCount")
    TotalNumberOfMissingValues = field("TotalNumberOfMissingValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MissingSensorDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MissingSensorDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnsupportedTimestamps:
    boto3_raw_data: "type_defs.UnsupportedTimestampsTypeDef" = dataclasses.field()

    TotalNumberOfUnsupportedTimestamps = field("TotalNumberOfUnsupportedTimestamps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnsupportedTimestampsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnsupportedTimestampsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetSummary:
    boto3_raw_data: "type_defs.DatasetSummaryTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    DatasetArn = field("DatasetArn")
    Status = field("Status")
    CreatedAt = field("CreatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetRequest:
    boto3_raw_data: "type_defs.DeleteDatasetRequestTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInferenceSchedulerRequest:
    boto3_raw_data: "type_defs.DeleteInferenceSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    InferenceSchedulerName = field("InferenceSchedulerName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteInferenceSchedulerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInferenceSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLabelGroupRequest:
    boto3_raw_data: "type_defs.DeleteLabelGroupRequestTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLabelGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLabelGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLabelRequest:
    boto3_raw_data: "type_defs.DeleteLabelRequestTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    LabelId = field("LabelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLabelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLabelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteModelRequest:
    boto3_raw_data: "type_defs.DeleteModelRequestTypeDef" = dataclasses.field()

    ModelName = field("ModelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteModelRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class DeleteRetrainingSchedulerRequest:
    boto3_raw_data: "type_defs.DeleteRetrainingSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRetrainingSchedulerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRetrainingSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataIngestionJobRequest:
    boto3_raw_data: "type_defs.DescribeDataIngestionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDataIngestionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataIngestionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetRequest:
    boto3_raw_data: "type_defs.DescribeDatasetRequestTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInferenceSchedulerRequest:
    boto3_raw_data: "type_defs.DescribeInferenceSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    InferenceSchedulerName = field("InferenceSchedulerName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInferenceSchedulerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInferenceSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLabelGroupRequest:
    boto3_raw_data: "type_defs.DescribeLabelGroupRequestTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLabelGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLabelGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLabelRequest:
    boto3_raw_data: "type_defs.DescribeLabelRequestTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    LabelId = field("LabelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLabelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLabelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeModelRequest:
    boto3_raw_data: "type_defs.DescribeModelRequestTypeDef" = dataclasses.field()

    ModelName = field("ModelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeModelVersionRequest:
    boto3_raw_data: "type_defs.DescribeModelVersionRequestTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    ModelVersion = field("ModelVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeModelVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeModelVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Object:
    boto3_raw_data: "type_defs.S3ObjectTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePolicyRequest:
    boto3_raw_data: "type_defs.DescribeResourcePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourcePolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRetrainingSchedulerRequest:
    boto3_raw_data: "type_defs.DescribeRetrainingSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRetrainingSchedulerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRetrainingSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceEventSummary:
    boto3_raw_data: "type_defs.InferenceEventSummaryTypeDef" = dataclasses.field()

    InferenceSchedulerArn = field("InferenceSchedulerArn")
    InferenceSchedulerName = field("InferenceSchedulerName")
    EventStartTime = field("EventStartTime")
    EventEndTime = field("EventEndTime")
    Diagnostics = field("Diagnostics")
    EventDurationInSeconds = field("EventDurationInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceEventSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceEventSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceInputNameConfiguration:
    boto3_raw_data: "type_defs.InferenceInputNameConfigurationTypeDef" = (
        dataclasses.field()
    )

    TimestampFormat = field("TimestampFormat")
    ComponentTimestampDelimiter = field("ComponentTimestampDelimiter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InferenceInputNameConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceInputNameConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceS3InputConfiguration:
    boto3_raw_data: "type_defs.InferenceS3InputConfigurationTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Prefix = field("Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InferenceS3InputConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceS3InputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceS3OutputConfiguration:
    boto3_raw_data: "type_defs.InferenceS3OutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Prefix = field("Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InferenceS3OutputConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceS3OutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceSchedulerSummary:
    boto3_raw_data: "type_defs.InferenceSchedulerSummaryTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    InferenceSchedulerName = field("InferenceSchedulerName")
    InferenceSchedulerArn = field("InferenceSchedulerArn")
    Status = field("Status")
    DataDelayOffsetInMinutes = field("DataDelayOffsetInMinutes")
    DataUploadFrequency = field("DataUploadFrequency")
    LatestInferenceResult = field("LatestInferenceResult")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceSchedulerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceSchedulerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestionS3InputConfiguration:
    boto3_raw_data: "type_defs.IngestionS3InputConfigurationTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Prefix = field("Prefix")
    KeyPattern = field("KeyPattern")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IngestionS3InputConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestionS3InputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MissingCompleteSensorData:
    boto3_raw_data: "type_defs.MissingCompleteSensorDataTypeDef" = dataclasses.field()

    AffectedSensorCount = field("AffectedSensorCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MissingCompleteSensorDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MissingCompleteSensorDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SensorsWithShortDateRange:
    boto3_raw_data: "type_defs.SensorsWithShortDateRangeTypeDef" = dataclasses.field()

    AffectedSensorCount = field("AffectedSensorCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SensorsWithShortDateRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SensorsWithShortDateRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelGroupSummary:
    boto3_raw_data: "type_defs.LabelGroupSummaryTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    LabelGroupArn = field("LabelGroupArn")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelGroupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LabelGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelSummary:
    boto3_raw_data: "type_defs.LabelSummaryTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    LabelId = field("LabelId")
    LabelGroupArn = field("LabelGroupArn")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Rating = field("Rating")
    FaultCode = field("FaultCode")
    Equipment = field("Equipment")
    CreatedAt = field("CreatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LabelSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelsS3InputConfiguration:
    boto3_raw_data: "type_defs.LabelsS3InputConfigurationTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Prefix = field("Prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LabelsS3InputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LabelsS3InputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LargeTimestampGaps:
    boto3_raw_data: "type_defs.LargeTimestampGapsTypeDef" = dataclasses.field()

    Status = field("Status")
    NumberOfLargeTimestampGaps = field("NumberOfLargeTimestampGaps")
    MaxTimestampGapInDays = field("MaxTimestampGapInDays")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LargeTimestampGapsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LargeTimestampGapsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataIngestionJobsRequest:
    boto3_raw_data: "type_defs.ListDataIngestionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    DatasetName = field("DatasetName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataIngestionJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataIngestionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsRequest:
    boto3_raw_data: "type_defs.ListDatasetsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    DatasetNameBeginsWith = field("DatasetNameBeginsWith")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInferenceSchedulersRequest:
    boto3_raw_data: "type_defs.ListInferenceSchedulersRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    InferenceSchedulerNameBeginsWith = field("InferenceSchedulerNameBeginsWith")
    ModelName = field("ModelName")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInferenceSchedulersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInferenceSchedulersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLabelGroupsRequest:
    boto3_raw_data: "type_defs.ListLabelGroupsRequestTypeDef" = dataclasses.field()

    LabelGroupNameBeginsWith = field("LabelGroupNameBeginsWith")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLabelGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLabelGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelVersionSummary:
    boto3_raw_data: "type_defs.ModelVersionSummaryTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    ModelVersion = field("ModelVersion")
    ModelVersionArn = field("ModelVersionArn")
    CreatedAt = field("CreatedAt")
    Status = field("Status")
    SourceType = field("SourceType")
    ModelQuality = field("ModelQuality")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelsRequest:
    boto3_raw_data: "type_defs.ListModelsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Status = field("Status")
    ModelNameBeginsWith = field("ModelNameBeginsWith")
    DatasetNameBeginsWith = field("DatasetNameBeginsWith")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListModelsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRetrainingSchedulersRequest:
    boto3_raw_data: "type_defs.ListRetrainingSchedulersRequestTypeDef" = (
        dataclasses.field()
    )

    ModelNameBeginsWith = field("ModelNameBeginsWith")
    Status = field("Status")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRetrainingSchedulersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRetrainingSchedulersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrainingSchedulerSummary:
    boto3_raw_data: "type_defs.RetrainingSchedulerSummaryTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    Status = field("Status")
    RetrainingStartDate = field("RetrainingStartDate")
    RetrainingFrequency = field("RetrainingFrequency")
    LookbackWindow = field("LookbackWindow")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrainingSchedulerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrainingSchedulerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSensorStatisticsRequest:
    boto3_raw_data: "type_defs.ListSensorStatisticsRequestTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    IngestionJobId = field("IngestionJobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSensorStatisticsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSensorStatisticsRequestTypeDef"]
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
class ModelDiagnosticsS3OutputConfiguration:
    boto3_raw_data: "type_defs.ModelDiagnosticsS3OutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Prefix = field("Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModelDiagnosticsS3OutputConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelDiagnosticsS3OutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonotonicValues:
    boto3_raw_data: "type_defs.MonotonicValuesTypeDef" = dataclasses.field()

    Status = field("Status")
    Monotonicity = field("Monotonicity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonotonicValuesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonotonicValuesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultipleOperatingModes:
    boto3_raw_data: "type_defs.MultipleOperatingModesTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultipleOperatingModesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultipleOperatingModesTypeDef"]
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

    ResourceArn = field("ResourceArn")
    ResourcePolicy = field("ResourcePolicy")
    ClientToken = field("ClientToken")
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
class StartInferenceSchedulerRequest:
    boto3_raw_data: "type_defs.StartInferenceSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    InferenceSchedulerName = field("InferenceSchedulerName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartInferenceSchedulerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInferenceSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRetrainingSchedulerRequest:
    boto3_raw_data: "type_defs.StartRetrainingSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartRetrainingSchedulerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRetrainingSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopInferenceSchedulerRequest:
    boto3_raw_data: "type_defs.StopInferenceSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    InferenceSchedulerName = field("InferenceSchedulerName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopInferenceSchedulerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopInferenceSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopRetrainingSchedulerRequest:
    boto3_raw_data: "type_defs.StopRetrainingSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopRetrainingSchedulerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopRetrainingSchedulerRequestTypeDef"]
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
class UpdateActiveModelVersionRequest:
    boto3_raw_data: "type_defs.UpdateActiveModelVersionRequestTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")
    ModelVersion = field("ModelVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateActiveModelVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateActiveModelVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLabelGroupRequest:
    boto3_raw_data: "type_defs.UpdateLabelGroupRequestTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    FaultCodes = field("FaultCodes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLabelGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLabelGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetRequest:
    boto3_raw_data: "type_defs.CreateDatasetRequestTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    ClientToken = field("ClientToken")

    @cached_property
    def DatasetSchema(self):  # pragma: no cover
        return DatasetSchema.make_one(self.boto3_raw_data["DatasetSchema"])

    ServerSideKmsKeyId = field("ServerSideKmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLabelGroupRequest:
    boto3_raw_data: "type_defs.CreateLabelGroupRequestTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    ClientToken = field("ClientToken")
    FaultCodes = field("FaultCodes")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLabelGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLabelGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportDatasetRequest:
    boto3_raw_data: "type_defs.ImportDatasetRequestTypeDef" = dataclasses.field()

    SourceDatasetArn = field("SourceDatasetArn")
    ClientToken = field("ClientToken")
    DatasetName = field("DatasetName")
    ServerSideKmsKeyId = field("ServerSideKmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDatasetRequestTypeDef"]
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
class CreateDatasetResponse:
    boto3_raw_data: "type_defs.CreateDatasetResponseTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    DatasetArn = field("DatasetArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInferenceSchedulerResponse:
    boto3_raw_data: "type_defs.CreateInferenceSchedulerResponseTypeDef" = (
        dataclasses.field()
    )

    InferenceSchedulerArn = field("InferenceSchedulerArn")
    InferenceSchedulerName = field("InferenceSchedulerName")
    Status = field("Status")
    ModelQuality = field("ModelQuality")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateInferenceSchedulerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInferenceSchedulerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLabelGroupResponse:
    boto3_raw_data: "type_defs.CreateLabelGroupResponseTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    LabelGroupArn = field("LabelGroupArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLabelGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLabelGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLabelResponse:
    boto3_raw_data: "type_defs.CreateLabelResponseTypeDef" = dataclasses.field()

    LabelId = field("LabelId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLabelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLabelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelResponse:
    boto3_raw_data: "type_defs.CreateModelResponseTypeDef" = dataclasses.field()

    ModelArn = field("ModelArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRetrainingSchedulerResponse:
    boto3_raw_data: "type_defs.CreateRetrainingSchedulerResponseTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRetrainingSchedulerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRetrainingSchedulerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLabelGroupResponse:
    boto3_raw_data: "type_defs.DescribeLabelGroupResponseTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    LabelGroupArn = field("LabelGroupArn")
    FaultCodes = field("FaultCodes")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLabelGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLabelGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLabelResponse:
    boto3_raw_data: "type_defs.DescribeLabelResponseTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    LabelGroupArn = field("LabelGroupArn")
    LabelId = field("LabelId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Rating = field("Rating")
    FaultCode = field("FaultCode")
    Notes = field("Notes")
    Equipment = field("Equipment")
    CreatedAt = field("CreatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLabelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLabelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePolicyResponse:
    boto3_raw_data: "type_defs.DescribeResourcePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    PolicyRevisionId = field("PolicyRevisionId")
    ResourcePolicy = field("ResourcePolicy")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourcePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRetrainingSchedulerResponse:
    boto3_raw_data: "type_defs.DescribeRetrainingSchedulerResponseTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    RetrainingStartDate = field("RetrainingStartDate")
    RetrainingFrequency = field("RetrainingFrequency")
    LookbackWindow = field("LookbackWindow")
    Status = field("Status")
    PromoteMode = field("PromoteMode")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRetrainingSchedulerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRetrainingSchedulerResponseTypeDef"]
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
class ImportDatasetResponse:
    boto3_raw_data: "type_defs.ImportDatasetResponseTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    DatasetArn = field("DatasetArn")
    Status = field("Status")
    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportModelVersionResponse:
    boto3_raw_data: "type_defs.ImportModelVersionResponseTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    ModelVersionArn = field("ModelVersionArn")
    ModelVersion = field("ModelVersion")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportModelVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportModelVersionResponseTypeDef"]
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
class PutResourcePolicyResponse:
    boto3_raw_data: "type_defs.PutResourcePolicyResponseTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
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
class StartDataIngestionJobResponse:
    boto3_raw_data: "type_defs.StartDataIngestionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDataIngestionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataIngestionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInferenceSchedulerResponse:
    boto3_raw_data: "type_defs.StartInferenceSchedulerResponseTypeDef" = (
        dataclasses.field()
    )

    ModelArn = field("ModelArn")
    ModelName = field("ModelName")
    InferenceSchedulerName = field("InferenceSchedulerName")
    InferenceSchedulerArn = field("InferenceSchedulerArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartInferenceSchedulerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInferenceSchedulerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRetrainingSchedulerResponse:
    boto3_raw_data: "type_defs.StartRetrainingSchedulerResponseTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartRetrainingSchedulerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRetrainingSchedulerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopInferenceSchedulerResponse:
    boto3_raw_data: "type_defs.StopInferenceSchedulerResponseTypeDef" = (
        dataclasses.field()
    )

    ModelArn = field("ModelArn")
    ModelName = field("ModelName")
    InferenceSchedulerName = field("InferenceSchedulerName")
    InferenceSchedulerArn = field("InferenceSchedulerArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopInferenceSchedulerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopInferenceSchedulerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopRetrainingSchedulerResponse:
    boto3_raw_data: "type_defs.StopRetrainingSchedulerResponseTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopRetrainingSchedulerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopRetrainingSchedulerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateActiveModelVersionResponse:
    boto3_raw_data: "type_defs.UpdateActiveModelVersionResponseTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    CurrentActiveVersion = field("CurrentActiveVersion")
    PreviousActiveVersion = field("PreviousActiveVersion")
    CurrentActiveVersionArn = field("CurrentActiveVersionArn")
    PreviousActiveVersionArn = field("PreviousActiveVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateActiveModelVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateActiveModelVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLabelRequest:
    boto3_raw_data: "type_defs.CreateLabelRequestTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Rating = field("Rating")
    ClientToken = field("ClientToken")
    FaultCode = field("FaultCode")
    Notes = field("Notes")
    Equipment = field("Equipment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLabelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLabelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRetrainingSchedulerRequest:
    boto3_raw_data: "type_defs.CreateRetrainingSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")
    RetrainingFrequency = field("RetrainingFrequency")
    LookbackWindow = field("LookbackWindow")
    ClientToken = field("ClientToken")
    RetrainingStartDate = field("RetrainingStartDate")
    PromoteMode = field("PromoteMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRetrainingSchedulerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRetrainingSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInferenceEventsRequest:
    boto3_raw_data: "type_defs.ListInferenceEventsRequestTypeDef" = dataclasses.field()

    InferenceSchedulerName = field("InferenceSchedulerName")
    IntervalStartTime = field("IntervalStartTime")
    IntervalEndTime = field("IntervalEndTime")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInferenceEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInferenceEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInferenceExecutionsRequest:
    boto3_raw_data: "type_defs.ListInferenceExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    InferenceSchedulerName = field("InferenceSchedulerName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    DataStartTimeAfter = field("DataStartTimeAfter")
    DataEndTimeBefore = field("DataEndTimeBefore")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInferenceExecutionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInferenceExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLabelsRequest:
    boto3_raw_data: "type_defs.ListLabelsRequestTypeDef" = dataclasses.field()

    LabelGroupName = field("LabelGroupName")
    IntervalStartTime = field("IntervalStartTime")
    IntervalEndTime = field("IntervalEndTime")
    FaultCode = field("FaultCode")
    Equipment = field("Equipment")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListLabelsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLabelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelVersionsRequest:
    boto3_raw_data: "type_defs.ListModelVersionsRequestTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Status = field("Status")
    SourceType = field("SourceType")
    CreatedAtEndTime = field("CreatedAtEndTime")
    CreatedAtStartTime = field("CreatedAtStartTime")
    MaxModelVersion = field("MaxModelVersion")
    MinModelVersion = field("MinModelVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListModelVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRetrainingSchedulerRequest:
    boto3_raw_data: "type_defs.UpdateRetrainingSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")
    RetrainingStartDate = field("RetrainingStartDate")
    RetrainingFrequency = field("RetrainingFrequency")
    LookbackWindow = field("LookbackWindow")
    PromoteMode = field("PromoteMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRetrainingSchedulerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRetrainingSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsResponse:
    boto3_raw_data: "type_defs.ListDatasetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DatasetSummaries(self):  # pragma: no cover
        return DatasetSummary.make_many(self.boto3_raw_data["DatasetSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestedFilesSummary:
    boto3_raw_data: "type_defs.IngestedFilesSummaryTypeDef" = dataclasses.field()

    TotalNumberOfFiles = field("TotalNumberOfFiles")
    IngestedNumberOfFiles = field("IngestedNumberOfFiles")

    @cached_property
    def DiscardedFiles(self):  # pragma: no cover
        return S3Object.make_many(self.boto3_raw_data["DiscardedFiles"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestedFilesSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestedFilesSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInferenceEventsResponse:
    boto3_raw_data: "type_defs.ListInferenceEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def InferenceEventSummaries(self):  # pragma: no cover
        return InferenceEventSummary.make_many(
            self.boto3_raw_data["InferenceEventSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInferenceEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInferenceEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceInputConfiguration:
    boto3_raw_data: "type_defs.InferenceInputConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def S3InputConfiguration(self):  # pragma: no cover
        return InferenceS3InputConfiguration.make_one(
            self.boto3_raw_data["S3InputConfiguration"]
        )

    InputTimeZoneOffset = field("InputTimeZoneOffset")

    @cached_property
    def InferenceInputNameConfiguration(self):  # pragma: no cover
        return InferenceInputNameConfiguration.make_one(
            self.boto3_raw_data["InferenceInputNameConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceInputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceInputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceOutputConfiguration:
    boto3_raw_data: "type_defs.InferenceOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3OutputConfiguration(self):  # pragma: no cover
        return InferenceS3OutputConfiguration.make_one(
            self.boto3_raw_data["S3OutputConfiguration"]
        )

    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceOutputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInferenceSchedulersResponse:
    boto3_raw_data: "type_defs.ListInferenceSchedulersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InferenceSchedulerSummaries(self):  # pragma: no cover
        return InferenceSchedulerSummary.make_many(
            self.boto3_raw_data["InferenceSchedulerSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInferenceSchedulersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInferenceSchedulersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestionInputConfiguration:
    boto3_raw_data: "type_defs.IngestionInputConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def S3InputConfiguration(self):  # pragma: no cover
        return IngestionS3InputConfiguration.make_one(
            self.boto3_raw_data["S3InputConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestionInputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestionInputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsufficientSensorData:
    boto3_raw_data: "type_defs.InsufficientSensorDataTypeDef" = dataclasses.field()

    @cached_property
    def MissingCompleteSensorData(self):  # pragma: no cover
        return MissingCompleteSensorData.make_one(
            self.boto3_raw_data["MissingCompleteSensorData"]
        )

    @cached_property
    def SensorsWithShortDateRange(self):  # pragma: no cover
        return SensorsWithShortDateRange.make_one(
            self.boto3_raw_data["SensorsWithShortDateRange"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InsufficientSensorDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsufficientSensorDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLabelGroupsResponse:
    boto3_raw_data: "type_defs.ListLabelGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def LabelGroupSummaries(self):  # pragma: no cover
        return LabelGroupSummary.make_many(self.boto3_raw_data["LabelGroupSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLabelGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLabelGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLabelsResponse:
    boto3_raw_data: "type_defs.ListLabelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def LabelSummaries(self):  # pragma: no cover
        return LabelSummary.make_many(self.boto3_raw_data["LabelSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLabelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLabelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelsInputConfiguration:
    boto3_raw_data: "type_defs.LabelsInputConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def S3InputConfiguration(self):  # pragma: no cover
        return LabelsS3InputConfiguration.make_one(
            self.boto3_raw_data["S3InputConfiguration"]
        )

    LabelGroupName = field("LabelGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LabelsInputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LabelsInputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelVersionsResponse:
    boto3_raw_data: "type_defs.ListModelVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ModelVersionSummaries(self):  # pragma: no cover
        return ModelVersionSummary.make_many(
            self.boto3_raw_data["ModelVersionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListModelVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRetrainingSchedulersResponse:
    boto3_raw_data: "type_defs.ListRetrainingSchedulersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RetrainingSchedulerSummaries(self):  # pragma: no cover
        return RetrainingSchedulerSummary.make_many(
            self.boto3_raw_data["RetrainingSchedulerSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRetrainingSchedulersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRetrainingSchedulersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelDiagnosticsOutputConfiguration:
    boto3_raw_data: "type_defs.ModelDiagnosticsOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3OutputConfiguration(self):  # pragma: no cover
        return ModelDiagnosticsS3OutputConfiguration.make_one(
            self.boto3_raw_data["S3OutputConfiguration"]
        )

    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModelDiagnosticsOutputConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelDiagnosticsOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SensorStatisticsSummary:
    boto3_raw_data: "type_defs.SensorStatisticsSummaryTypeDef" = dataclasses.field()

    ComponentName = field("ComponentName")
    SensorName = field("SensorName")
    DataExists = field("DataExists")

    @cached_property
    def MissingValues(self):  # pragma: no cover
        return CountPercent.make_one(self.boto3_raw_data["MissingValues"])

    @cached_property
    def InvalidValues(self):  # pragma: no cover
        return CountPercent.make_one(self.boto3_raw_data["InvalidValues"])

    @cached_property
    def InvalidDateEntries(self):  # pragma: no cover
        return CountPercent.make_one(self.boto3_raw_data["InvalidDateEntries"])

    @cached_property
    def DuplicateTimestamps(self):  # pragma: no cover
        return CountPercent.make_one(self.boto3_raw_data["DuplicateTimestamps"])

    @cached_property
    def CategoricalValues(self):  # pragma: no cover
        return CategoricalValues.make_one(self.boto3_raw_data["CategoricalValues"])

    @cached_property
    def MultipleOperatingModes(self):  # pragma: no cover
        return MultipleOperatingModes.make_one(
            self.boto3_raw_data["MultipleOperatingModes"]
        )

    @cached_property
    def LargeTimestampGaps(self):  # pragma: no cover
        return LargeTimestampGaps.make_one(self.boto3_raw_data["LargeTimestampGaps"])

    @cached_property
    def MonotonicValues(self):  # pragma: no cover
        return MonotonicValues.make_one(self.boto3_raw_data["MonotonicValues"])

    DataStartTime = field("DataStartTime")
    DataEndTime = field("DataEndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SensorStatisticsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SensorStatisticsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInferenceSchedulerRequest:
    boto3_raw_data: "type_defs.CreateInferenceSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")
    InferenceSchedulerName = field("InferenceSchedulerName")
    DataUploadFrequency = field("DataUploadFrequency")

    @cached_property
    def DataInputConfiguration(self):  # pragma: no cover
        return InferenceInputConfiguration.make_one(
            self.boto3_raw_data["DataInputConfiguration"]
        )

    @cached_property
    def DataOutputConfiguration(self):  # pragma: no cover
        return InferenceOutputConfiguration.make_one(
            self.boto3_raw_data["DataOutputConfiguration"]
        )

    RoleArn = field("RoleArn")
    ClientToken = field("ClientToken")
    DataDelayOffsetInMinutes = field("DataDelayOffsetInMinutes")
    ServerSideKmsKeyId = field("ServerSideKmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateInferenceSchedulerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInferenceSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInferenceSchedulerResponse:
    boto3_raw_data: "type_defs.DescribeInferenceSchedulerResponseTypeDef" = (
        dataclasses.field()
    )

    ModelArn = field("ModelArn")
    ModelName = field("ModelName")
    InferenceSchedulerName = field("InferenceSchedulerName")
    InferenceSchedulerArn = field("InferenceSchedulerArn")
    Status = field("Status")
    DataDelayOffsetInMinutes = field("DataDelayOffsetInMinutes")
    DataUploadFrequency = field("DataUploadFrequency")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def DataInputConfiguration(self):  # pragma: no cover
        return InferenceInputConfiguration.make_one(
            self.boto3_raw_data["DataInputConfiguration"]
        )

    @cached_property
    def DataOutputConfiguration(self):  # pragma: no cover
        return InferenceOutputConfiguration.make_one(
            self.boto3_raw_data["DataOutputConfiguration"]
        )

    RoleArn = field("RoleArn")
    ServerSideKmsKeyId = field("ServerSideKmsKeyId")
    LatestInferenceResult = field("LatestInferenceResult")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInferenceSchedulerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInferenceSchedulerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceExecutionSummary:
    boto3_raw_data: "type_defs.InferenceExecutionSummaryTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    InferenceSchedulerName = field("InferenceSchedulerName")
    InferenceSchedulerArn = field("InferenceSchedulerArn")
    ScheduledStartTime = field("ScheduledStartTime")
    DataStartTime = field("DataStartTime")
    DataEndTime = field("DataEndTime")

    @cached_property
    def DataInputConfiguration(self):  # pragma: no cover
        return InferenceInputConfiguration.make_one(
            self.boto3_raw_data["DataInputConfiguration"]
        )

    @cached_property
    def DataOutputConfiguration(self):  # pragma: no cover
        return InferenceOutputConfiguration.make_one(
            self.boto3_raw_data["DataOutputConfiguration"]
        )

    @cached_property
    def CustomerResultObject(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["CustomerResultObject"])

    Status = field("Status")
    FailedReason = field("FailedReason")
    ModelVersion = field("ModelVersion")
    ModelVersionArn = field("ModelVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceExecutionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInferenceSchedulerRequest:
    boto3_raw_data: "type_defs.UpdateInferenceSchedulerRequestTypeDef" = (
        dataclasses.field()
    )

    InferenceSchedulerName = field("InferenceSchedulerName")
    DataDelayOffsetInMinutes = field("DataDelayOffsetInMinutes")
    DataUploadFrequency = field("DataUploadFrequency")

    @cached_property
    def DataInputConfiguration(self):  # pragma: no cover
        return InferenceInputConfiguration.make_one(
            self.boto3_raw_data["DataInputConfiguration"]
        )

    @cached_property
    def DataOutputConfiguration(self):  # pragma: no cover
        return InferenceOutputConfiguration.make_one(
            self.boto3_raw_data["DataOutputConfiguration"]
        )

    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateInferenceSchedulerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInferenceSchedulerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIngestionJobSummary:
    boto3_raw_data: "type_defs.DataIngestionJobSummaryTypeDef" = dataclasses.field()

    JobId = field("JobId")
    DatasetName = field("DatasetName")
    DatasetArn = field("DatasetArn")

    @cached_property
    def IngestionInputConfiguration(self):  # pragma: no cover
        return IngestionInputConfiguration.make_one(
            self.boto3_raw_data["IngestionInputConfiguration"]
        )

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataIngestionJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIngestionJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataIngestionJobRequest:
    boto3_raw_data: "type_defs.StartDataIngestionJobRequestTypeDef" = (
        dataclasses.field()
    )

    DatasetName = field("DatasetName")

    @cached_property
    def IngestionInputConfiguration(self):  # pragma: no cover
        return IngestionInputConfiguration.make_one(
            self.boto3_raw_data["IngestionInputConfiguration"]
        )

    RoleArn = field("RoleArn")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDataIngestionJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataIngestionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataQualitySummary:
    boto3_raw_data: "type_defs.DataQualitySummaryTypeDef" = dataclasses.field()

    @cached_property
    def InsufficientSensorData(self):  # pragma: no cover
        return InsufficientSensorData.make_one(
            self.boto3_raw_data["InsufficientSensorData"]
        )

    @cached_property
    def MissingSensorData(self):  # pragma: no cover
        return MissingSensorData.make_one(self.boto3_raw_data["MissingSensorData"])

    @cached_property
    def InvalidSensorData(self):  # pragma: no cover
        return InvalidSensorData.make_one(self.boto3_raw_data["InvalidSensorData"])

    @cached_property
    def UnsupportedTimestamps(self):  # pragma: no cover
        return UnsupportedTimestamps.make_one(
            self.boto3_raw_data["UnsupportedTimestamps"]
        )

    @cached_property
    def DuplicateTimestamps(self):  # pragma: no cover
        return DuplicateTimestamps.make_one(self.boto3_raw_data["DuplicateTimestamps"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataQualitySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataQualitySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportModelVersionRequest:
    boto3_raw_data: "type_defs.ImportModelVersionRequestTypeDef" = dataclasses.field()

    SourceModelVersionArn = field("SourceModelVersionArn")
    DatasetName = field("DatasetName")
    ClientToken = field("ClientToken")
    ModelName = field("ModelName")

    @cached_property
    def LabelsInputConfiguration(self):  # pragma: no cover
        return LabelsInputConfiguration.make_one(
            self.boto3_raw_data["LabelsInputConfiguration"]
        )

    RoleArn = field("RoleArn")
    ServerSideKmsKeyId = field("ServerSideKmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    InferenceDataImportStrategy = field("InferenceDataImportStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportModelVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportModelVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelRequest:
    boto3_raw_data: "type_defs.CreateModelRequestTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    DatasetName = field("DatasetName")
    ClientToken = field("ClientToken")

    @cached_property
    def DatasetSchema(self):  # pragma: no cover
        return DatasetSchema.make_one(self.boto3_raw_data["DatasetSchema"])

    @cached_property
    def LabelsInputConfiguration(self):  # pragma: no cover
        return LabelsInputConfiguration.make_one(
            self.boto3_raw_data["LabelsInputConfiguration"]
        )

    TrainingDataStartTime = field("TrainingDataStartTime")
    TrainingDataEndTime = field("TrainingDataEndTime")
    EvaluationDataStartTime = field("EvaluationDataStartTime")
    EvaluationDataEndTime = field("EvaluationDataEndTime")
    RoleArn = field("RoleArn")

    @cached_property
    def DataPreProcessingConfiguration(self):  # pragma: no cover
        return DataPreProcessingConfiguration.make_one(
            self.boto3_raw_data["DataPreProcessingConfiguration"]
        )

    ServerSideKmsKeyId = field("ServerSideKmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    OffCondition = field("OffCondition")

    @cached_property
    def ModelDiagnosticsOutputConfiguration(self):  # pragma: no cover
        return ModelDiagnosticsOutputConfiguration.make_one(
            self.boto3_raw_data["ModelDiagnosticsOutputConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeModelResponse:
    boto3_raw_data: "type_defs.DescribeModelResponseTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    DatasetName = field("DatasetName")
    DatasetArn = field("DatasetArn")
    Schema = field("Schema")

    @cached_property
    def LabelsInputConfiguration(self):  # pragma: no cover
        return LabelsInputConfiguration.make_one(
            self.boto3_raw_data["LabelsInputConfiguration"]
        )

    TrainingDataStartTime = field("TrainingDataStartTime")
    TrainingDataEndTime = field("TrainingDataEndTime")
    EvaluationDataStartTime = field("EvaluationDataStartTime")
    EvaluationDataEndTime = field("EvaluationDataEndTime")
    RoleArn = field("RoleArn")

    @cached_property
    def DataPreProcessingConfiguration(self):  # pragma: no cover
        return DataPreProcessingConfiguration.make_one(
            self.boto3_raw_data["DataPreProcessingConfiguration"]
        )

    Status = field("Status")
    TrainingExecutionStartTime = field("TrainingExecutionStartTime")
    TrainingExecutionEndTime = field("TrainingExecutionEndTime")
    FailedReason = field("FailedReason")
    ModelMetrics = field("ModelMetrics")
    LastUpdatedTime = field("LastUpdatedTime")
    CreatedAt = field("CreatedAt")
    ServerSideKmsKeyId = field("ServerSideKmsKeyId")
    OffCondition = field("OffCondition")
    SourceModelVersionArn = field("SourceModelVersionArn")
    ImportJobStartTime = field("ImportJobStartTime")
    ImportJobEndTime = field("ImportJobEndTime")
    ActiveModelVersion = field("ActiveModelVersion")
    ActiveModelVersionArn = field("ActiveModelVersionArn")
    ModelVersionActivatedAt = field("ModelVersionActivatedAt")
    PreviousActiveModelVersion = field("PreviousActiveModelVersion")
    PreviousActiveModelVersionArn = field("PreviousActiveModelVersionArn")
    PreviousModelVersionActivatedAt = field("PreviousModelVersionActivatedAt")
    PriorModelMetrics = field("PriorModelMetrics")
    LatestScheduledRetrainingFailedReason = field(
        "LatestScheduledRetrainingFailedReason"
    )
    LatestScheduledRetrainingStatus = field("LatestScheduledRetrainingStatus")
    LatestScheduledRetrainingModelVersion = field(
        "LatestScheduledRetrainingModelVersion"
    )
    LatestScheduledRetrainingStartTime = field("LatestScheduledRetrainingStartTime")
    LatestScheduledRetrainingAvailableDataInDays = field(
        "LatestScheduledRetrainingAvailableDataInDays"
    )
    NextScheduledRetrainingStartDate = field("NextScheduledRetrainingStartDate")
    AccumulatedInferenceDataStartTime = field("AccumulatedInferenceDataStartTime")
    AccumulatedInferenceDataEndTime = field("AccumulatedInferenceDataEndTime")
    RetrainingSchedulerStatus = field("RetrainingSchedulerStatus")

    @cached_property
    def ModelDiagnosticsOutputConfiguration(self):  # pragma: no cover
        return ModelDiagnosticsOutputConfiguration.make_one(
            self.boto3_raw_data["ModelDiagnosticsOutputConfiguration"]
        )

    ModelQuality = field("ModelQuality")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeModelVersionResponse:
    boto3_raw_data: "type_defs.DescribeModelVersionResponseTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    ModelVersion = field("ModelVersion")
    ModelVersionArn = field("ModelVersionArn")
    Status = field("Status")
    SourceType = field("SourceType")
    DatasetName = field("DatasetName")
    DatasetArn = field("DatasetArn")
    Schema = field("Schema")

    @cached_property
    def LabelsInputConfiguration(self):  # pragma: no cover
        return LabelsInputConfiguration.make_one(
            self.boto3_raw_data["LabelsInputConfiguration"]
        )

    TrainingDataStartTime = field("TrainingDataStartTime")
    TrainingDataEndTime = field("TrainingDataEndTime")
    EvaluationDataStartTime = field("EvaluationDataStartTime")
    EvaluationDataEndTime = field("EvaluationDataEndTime")
    RoleArn = field("RoleArn")

    @cached_property
    def DataPreProcessingConfiguration(self):  # pragma: no cover
        return DataPreProcessingConfiguration.make_one(
            self.boto3_raw_data["DataPreProcessingConfiguration"]
        )

    TrainingExecutionStartTime = field("TrainingExecutionStartTime")
    TrainingExecutionEndTime = field("TrainingExecutionEndTime")
    FailedReason = field("FailedReason")
    ModelMetrics = field("ModelMetrics")
    LastUpdatedTime = field("LastUpdatedTime")
    CreatedAt = field("CreatedAt")
    ServerSideKmsKeyId = field("ServerSideKmsKeyId")
    OffCondition = field("OffCondition")
    SourceModelVersionArn = field("SourceModelVersionArn")
    ImportJobStartTime = field("ImportJobStartTime")
    ImportJobEndTime = field("ImportJobEndTime")
    ImportedDataSizeInBytes = field("ImportedDataSizeInBytes")
    PriorModelMetrics = field("PriorModelMetrics")
    RetrainingAvailableDataInDays = field("RetrainingAvailableDataInDays")
    AutoPromotionResult = field("AutoPromotionResult")
    AutoPromotionResultReason = field("AutoPromotionResultReason")

    @cached_property
    def ModelDiagnosticsOutputConfiguration(self):  # pragma: no cover
        return ModelDiagnosticsOutputConfiguration.make_one(
            self.boto3_raw_data["ModelDiagnosticsOutputConfiguration"]
        )

    @cached_property
    def ModelDiagnosticsResultsObject(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["ModelDiagnosticsResultsObject"])

    ModelQuality = field("ModelQuality")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeModelVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeModelVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelSummary:
    boto3_raw_data: "type_defs.ModelSummaryTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    ModelArn = field("ModelArn")
    DatasetName = field("DatasetName")
    DatasetArn = field("DatasetArn")
    Status = field("Status")
    CreatedAt = field("CreatedAt")
    ActiveModelVersion = field("ActiveModelVersion")
    ActiveModelVersionArn = field("ActiveModelVersionArn")
    LatestScheduledRetrainingStatus = field("LatestScheduledRetrainingStatus")
    LatestScheduledRetrainingModelVersion = field(
        "LatestScheduledRetrainingModelVersion"
    )
    LatestScheduledRetrainingStartTime = field("LatestScheduledRetrainingStartTime")
    NextScheduledRetrainingStartDate = field("NextScheduledRetrainingStartDate")
    RetrainingSchedulerStatus = field("RetrainingSchedulerStatus")

    @cached_property
    def ModelDiagnosticsOutputConfiguration(self):  # pragma: no cover
        return ModelDiagnosticsOutputConfiguration.make_one(
            self.boto3_raw_data["ModelDiagnosticsOutputConfiguration"]
        )

    ModelQuality = field("ModelQuality")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateModelRequest:
    boto3_raw_data: "type_defs.UpdateModelRequestTypeDef" = dataclasses.field()

    ModelName = field("ModelName")

    @cached_property
    def LabelsInputConfiguration(self):  # pragma: no cover
        return LabelsInputConfiguration.make_one(
            self.boto3_raw_data["LabelsInputConfiguration"]
        )

    RoleArn = field("RoleArn")

    @cached_property
    def ModelDiagnosticsOutputConfiguration(self):  # pragma: no cover
        return ModelDiagnosticsOutputConfiguration.make_one(
            self.boto3_raw_data["ModelDiagnosticsOutputConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSensorStatisticsResponse:
    boto3_raw_data: "type_defs.ListSensorStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SensorStatisticsSummaries(self):  # pragma: no cover
        return SensorStatisticsSummary.make_many(
            self.boto3_raw_data["SensorStatisticsSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSensorStatisticsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSensorStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInferenceExecutionsResponse:
    boto3_raw_data: "type_defs.ListInferenceExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InferenceExecutionSummaries(self):  # pragma: no cover
        return InferenceExecutionSummary.make_many(
            self.boto3_raw_data["InferenceExecutionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInferenceExecutionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInferenceExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataIngestionJobsResponse:
    boto3_raw_data: "type_defs.ListDataIngestionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DataIngestionJobSummaries(self):  # pragma: no cover
        return DataIngestionJobSummary.make_many(
            self.boto3_raw_data["DataIngestionJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataIngestionJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataIngestionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataIngestionJobResponse:
    boto3_raw_data: "type_defs.DescribeDataIngestionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    DatasetArn = field("DatasetArn")

    @cached_property
    def IngestionInputConfiguration(self):  # pragma: no cover
        return IngestionInputConfiguration.make_one(
            self.boto3_raw_data["IngestionInputConfiguration"]
        )

    RoleArn = field("RoleArn")
    CreatedAt = field("CreatedAt")
    Status = field("Status")
    FailedReason = field("FailedReason")

    @cached_property
    def DataQualitySummary(self):  # pragma: no cover
        return DataQualitySummary.make_one(self.boto3_raw_data["DataQualitySummary"])

    @cached_property
    def IngestedFilesSummary(self):  # pragma: no cover
        return IngestedFilesSummary.make_one(
            self.boto3_raw_data["IngestedFilesSummary"]
        )

    StatusDetail = field("StatusDetail")
    IngestedDataSize = field("IngestedDataSize")
    DataStartTime = field("DataStartTime")
    DataEndTime = field("DataEndTime")
    SourceDatasetArn = field("SourceDatasetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDataIngestionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataIngestionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetResponse:
    boto3_raw_data: "type_defs.DescribeDatasetResponseTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    DatasetArn = field("DatasetArn")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Status = field("Status")
    Schema = field("Schema")
    ServerSideKmsKeyId = field("ServerSideKmsKeyId")

    @cached_property
    def IngestionInputConfiguration(self):  # pragma: no cover
        return IngestionInputConfiguration.make_one(
            self.boto3_raw_data["IngestionInputConfiguration"]
        )

    @cached_property
    def DataQualitySummary(self):  # pragma: no cover
        return DataQualitySummary.make_one(self.boto3_raw_data["DataQualitySummary"])

    @cached_property
    def IngestedFilesSummary(self):  # pragma: no cover
        return IngestedFilesSummary.make_one(
            self.boto3_raw_data["IngestedFilesSummary"]
        )

    RoleArn = field("RoleArn")
    DataStartTime = field("DataStartTime")
    DataEndTime = field("DataEndTime")
    SourceDatasetArn = field("SourceDatasetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelsResponse:
    boto3_raw_data: "type_defs.ListModelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ModelSummaries(self):  # pragma: no cover
        return ModelSummary.make_many(self.boto3_raw_data["ModelSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
