# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lookoutequipment import type_defs as bs_td


class LOOKOUTEQUIPMENTCaster:

    def create_dataset(
        self,
        res: "bs_td.CreateDatasetResponseTypeDef",
    ) -> "dc_td.CreateDatasetResponse":
        return dc_td.CreateDatasetResponse.make_one(res)

    def create_inference_scheduler(
        self,
        res: "bs_td.CreateInferenceSchedulerResponseTypeDef",
    ) -> "dc_td.CreateInferenceSchedulerResponse":
        return dc_td.CreateInferenceSchedulerResponse.make_one(res)

    def create_label(
        self,
        res: "bs_td.CreateLabelResponseTypeDef",
    ) -> "dc_td.CreateLabelResponse":
        return dc_td.CreateLabelResponse.make_one(res)

    def create_label_group(
        self,
        res: "bs_td.CreateLabelGroupResponseTypeDef",
    ) -> "dc_td.CreateLabelGroupResponse":
        return dc_td.CreateLabelGroupResponse.make_one(res)

    def create_model(
        self,
        res: "bs_td.CreateModelResponseTypeDef",
    ) -> "dc_td.CreateModelResponse":
        return dc_td.CreateModelResponse.make_one(res)

    def create_retraining_scheduler(
        self,
        res: "bs_td.CreateRetrainingSchedulerResponseTypeDef",
    ) -> "dc_td.CreateRetrainingSchedulerResponse":
        return dc_td.CreateRetrainingSchedulerResponse.make_one(res)

    def delete_dataset(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_inference_scheduler(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_label(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_label_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_model(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_retraining_scheduler(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_data_ingestion_job(
        self,
        res: "bs_td.DescribeDataIngestionJobResponseTypeDef",
    ) -> "dc_td.DescribeDataIngestionJobResponse":
        return dc_td.DescribeDataIngestionJobResponse.make_one(res)

    def describe_dataset(
        self,
        res: "bs_td.DescribeDatasetResponseTypeDef",
    ) -> "dc_td.DescribeDatasetResponse":
        return dc_td.DescribeDatasetResponse.make_one(res)

    def describe_inference_scheduler(
        self,
        res: "bs_td.DescribeInferenceSchedulerResponseTypeDef",
    ) -> "dc_td.DescribeInferenceSchedulerResponse":
        return dc_td.DescribeInferenceSchedulerResponse.make_one(res)

    def describe_label(
        self,
        res: "bs_td.DescribeLabelResponseTypeDef",
    ) -> "dc_td.DescribeLabelResponse":
        return dc_td.DescribeLabelResponse.make_one(res)

    def describe_label_group(
        self,
        res: "bs_td.DescribeLabelGroupResponseTypeDef",
    ) -> "dc_td.DescribeLabelGroupResponse":
        return dc_td.DescribeLabelGroupResponse.make_one(res)

    def describe_model(
        self,
        res: "bs_td.DescribeModelResponseTypeDef",
    ) -> "dc_td.DescribeModelResponse":
        return dc_td.DescribeModelResponse.make_one(res)

    def describe_model_version(
        self,
        res: "bs_td.DescribeModelVersionResponseTypeDef",
    ) -> "dc_td.DescribeModelVersionResponse":
        return dc_td.DescribeModelVersionResponse.make_one(res)

    def describe_resource_policy(
        self,
        res: "bs_td.DescribeResourcePolicyResponseTypeDef",
    ) -> "dc_td.DescribeResourcePolicyResponse":
        return dc_td.DescribeResourcePolicyResponse.make_one(res)

    def describe_retraining_scheduler(
        self,
        res: "bs_td.DescribeRetrainingSchedulerResponseTypeDef",
    ) -> "dc_td.DescribeRetrainingSchedulerResponse":
        return dc_td.DescribeRetrainingSchedulerResponse.make_one(res)

    def import_dataset(
        self,
        res: "bs_td.ImportDatasetResponseTypeDef",
    ) -> "dc_td.ImportDatasetResponse":
        return dc_td.ImportDatasetResponse.make_one(res)

    def import_model_version(
        self,
        res: "bs_td.ImportModelVersionResponseTypeDef",
    ) -> "dc_td.ImportModelVersionResponse":
        return dc_td.ImportModelVersionResponse.make_one(res)

    def list_data_ingestion_jobs(
        self,
        res: "bs_td.ListDataIngestionJobsResponseTypeDef",
    ) -> "dc_td.ListDataIngestionJobsResponse":
        return dc_td.ListDataIngestionJobsResponse.make_one(res)

    def list_datasets(
        self,
        res: "bs_td.ListDatasetsResponseTypeDef",
    ) -> "dc_td.ListDatasetsResponse":
        return dc_td.ListDatasetsResponse.make_one(res)

    def list_inference_events(
        self,
        res: "bs_td.ListInferenceEventsResponseTypeDef",
    ) -> "dc_td.ListInferenceEventsResponse":
        return dc_td.ListInferenceEventsResponse.make_one(res)

    def list_inference_executions(
        self,
        res: "bs_td.ListInferenceExecutionsResponseTypeDef",
    ) -> "dc_td.ListInferenceExecutionsResponse":
        return dc_td.ListInferenceExecutionsResponse.make_one(res)

    def list_inference_schedulers(
        self,
        res: "bs_td.ListInferenceSchedulersResponseTypeDef",
    ) -> "dc_td.ListInferenceSchedulersResponse":
        return dc_td.ListInferenceSchedulersResponse.make_one(res)

    def list_label_groups(
        self,
        res: "bs_td.ListLabelGroupsResponseTypeDef",
    ) -> "dc_td.ListLabelGroupsResponse":
        return dc_td.ListLabelGroupsResponse.make_one(res)

    def list_labels(
        self,
        res: "bs_td.ListLabelsResponseTypeDef",
    ) -> "dc_td.ListLabelsResponse":
        return dc_td.ListLabelsResponse.make_one(res)

    def list_model_versions(
        self,
        res: "bs_td.ListModelVersionsResponseTypeDef",
    ) -> "dc_td.ListModelVersionsResponse":
        return dc_td.ListModelVersionsResponse.make_one(res)

    def list_models(
        self,
        res: "bs_td.ListModelsResponseTypeDef",
    ) -> "dc_td.ListModelsResponse":
        return dc_td.ListModelsResponse.make_one(res)

    def list_retraining_schedulers(
        self,
        res: "bs_td.ListRetrainingSchedulersResponseTypeDef",
    ) -> "dc_td.ListRetrainingSchedulersResponse":
        return dc_td.ListRetrainingSchedulersResponse.make_one(res)

    def list_sensor_statistics(
        self,
        res: "bs_td.ListSensorStatisticsResponseTypeDef",
    ) -> "dc_td.ListSensorStatisticsResponse":
        return dc_td.ListSensorStatisticsResponse.make_one(res)

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

    def start_data_ingestion_job(
        self,
        res: "bs_td.StartDataIngestionJobResponseTypeDef",
    ) -> "dc_td.StartDataIngestionJobResponse":
        return dc_td.StartDataIngestionJobResponse.make_one(res)

    def start_inference_scheduler(
        self,
        res: "bs_td.StartInferenceSchedulerResponseTypeDef",
    ) -> "dc_td.StartInferenceSchedulerResponse":
        return dc_td.StartInferenceSchedulerResponse.make_one(res)

    def start_retraining_scheduler(
        self,
        res: "bs_td.StartRetrainingSchedulerResponseTypeDef",
    ) -> "dc_td.StartRetrainingSchedulerResponse":
        return dc_td.StartRetrainingSchedulerResponse.make_one(res)

    def stop_inference_scheduler(
        self,
        res: "bs_td.StopInferenceSchedulerResponseTypeDef",
    ) -> "dc_td.StopInferenceSchedulerResponse":
        return dc_td.StopInferenceSchedulerResponse.make_one(res)

    def stop_retraining_scheduler(
        self,
        res: "bs_td.StopRetrainingSchedulerResponseTypeDef",
    ) -> "dc_td.StopRetrainingSchedulerResponse":
        return dc_td.StopRetrainingSchedulerResponse.make_one(res)

    def update_active_model_version(
        self,
        res: "bs_td.UpdateActiveModelVersionResponseTypeDef",
    ) -> "dc_td.UpdateActiveModelVersionResponse":
        return dc_td.UpdateActiveModelVersionResponse.make_one(res)

    def update_inference_scheduler(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_label_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_model(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_retraining_scheduler(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


lookoutequipment_caster = LOOKOUTEQUIPMENTCaster()
