# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_personalize import type_defs as bs_td


class PERSONALIZECaster:

    def create_batch_inference_job(
        self,
        res: "bs_td.CreateBatchInferenceJobResponseTypeDef",
    ) -> "dc_td.CreateBatchInferenceJobResponse":
        return dc_td.CreateBatchInferenceJobResponse.make_one(res)

    def create_batch_segment_job(
        self,
        res: "bs_td.CreateBatchSegmentJobResponseTypeDef",
    ) -> "dc_td.CreateBatchSegmentJobResponse":
        return dc_td.CreateBatchSegmentJobResponse.make_one(res)

    def create_campaign(
        self,
        res: "bs_td.CreateCampaignResponseTypeDef",
    ) -> "dc_td.CreateCampaignResponse":
        return dc_td.CreateCampaignResponse.make_one(res)

    def create_data_deletion_job(
        self,
        res: "bs_td.CreateDataDeletionJobResponseTypeDef",
    ) -> "dc_td.CreateDataDeletionJobResponse":
        return dc_td.CreateDataDeletionJobResponse.make_one(res)

    def create_dataset(
        self,
        res: "bs_td.CreateDatasetResponseTypeDef",
    ) -> "dc_td.CreateDatasetResponse":
        return dc_td.CreateDatasetResponse.make_one(res)

    def create_dataset_export_job(
        self,
        res: "bs_td.CreateDatasetExportJobResponseTypeDef",
    ) -> "dc_td.CreateDatasetExportJobResponse":
        return dc_td.CreateDatasetExportJobResponse.make_one(res)

    def create_dataset_group(
        self,
        res: "bs_td.CreateDatasetGroupResponseTypeDef",
    ) -> "dc_td.CreateDatasetGroupResponse":
        return dc_td.CreateDatasetGroupResponse.make_one(res)

    def create_dataset_import_job(
        self,
        res: "bs_td.CreateDatasetImportJobResponseTypeDef",
    ) -> "dc_td.CreateDatasetImportJobResponse":
        return dc_td.CreateDatasetImportJobResponse.make_one(res)

    def create_event_tracker(
        self,
        res: "bs_td.CreateEventTrackerResponseTypeDef",
    ) -> "dc_td.CreateEventTrackerResponse":
        return dc_td.CreateEventTrackerResponse.make_one(res)

    def create_filter(
        self,
        res: "bs_td.CreateFilterResponseTypeDef",
    ) -> "dc_td.CreateFilterResponse":
        return dc_td.CreateFilterResponse.make_one(res)

    def create_metric_attribution(
        self,
        res: "bs_td.CreateMetricAttributionResponseTypeDef",
    ) -> "dc_td.CreateMetricAttributionResponse":
        return dc_td.CreateMetricAttributionResponse.make_one(res)

    def create_recommender(
        self,
        res: "bs_td.CreateRecommenderResponseTypeDef",
    ) -> "dc_td.CreateRecommenderResponse":
        return dc_td.CreateRecommenderResponse.make_one(res)

    def create_schema(
        self,
        res: "bs_td.CreateSchemaResponseTypeDef",
    ) -> "dc_td.CreateSchemaResponse":
        return dc_td.CreateSchemaResponse.make_one(res)

    def create_solution(
        self,
        res: "bs_td.CreateSolutionResponseTypeDef",
    ) -> "dc_td.CreateSolutionResponse":
        return dc_td.CreateSolutionResponse.make_one(res)

    def create_solution_version(
        self,
        res: "bs_td.CreateSolutionVersionResponseTypeDef",
    ) -> "dc_td.CreateSolutionVersionResponse":
        return dc_td.CreateSolutionVersionResponse.make_one(res)

    def delete_campaign(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_dataset(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_dataset_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_event_tracker(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_filter(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_metric_attribution(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_recommender(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_schema(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_solution(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_algorithm(
        self,
        res: "bs_td.DescribeAlgorithmResponseTypeDef",
    ) -> "dc_td.DescribeAlgorithmResponse":
        return dc_td.DescribeAlgorithmResponse.make_one(res)

    def describe_batch_inference_job(
        self,
        res: "bs_td.DescribeBatchInferenceJobResponseTypeDef",
    ) -> "dc_td.DescribeBatchInferenceJobResponse":
        return dc_td.DescribeBatchInferenceJobResponse.make_one(res)

    def describe_batch_segment_job(
        self,
        res: "bs_td.DescribeBatchSegmentJobResponseTypeDef",
    ) -> "dc_td.DescribeBatchSegmentJobResponse":
        return dc_td.DescribeBatchSegmentJobResponse.make_one(res)

    def describe_campaign(
        self,
        res: "bs_td.DescribeCampaignResponseTypeDef",
    ) -> "dc_td.DescribeCampaignResponse":
        return dc_td.DescribeCampaignResponse.make_one(res)

    def describe_data_deletion_job(
        self,
        res: "bs_td.DescribeDataDeletionJobResponseTypeDef",
    ) -> "dc_td.DescribeDataDeletionJobResponse":
        return dc_td.DescribeDataDeletionJobResponse.make_one(res)

    def describe_dataset(
        self,
        res: "bs_td.DescribeDatasetResponseTypeDef",
    ) -> "dc_td.DescribeDatasetResponse":
        return dc_td.DescribeDatasetResponse.make_one(res)

    def describe_dataset_export_job(
        self,
        res: "bs_td.DescribeDatasetExportJobResponseTypeDef",
    ) -> "dc_td.DescribeDatasetExportJobResponse":
        return dc_td.DescribeDatasetExportJobResponse.make_one(res)

    def describe_dataset_group(
        self,
        res: "bs_td.DescribeDatasetGroupResponseTypeDef",
    ) -> "dc_td.DescribeDatasetGroupResponse":
        return dc_td.DescribeDatasetGroupResponse.make_one(res)

    def describe_dataset_import_job(
        self,
        res: "bs_td.DescribeDatasetImportJobResponseTypeDef",
    ) -> "dc_td.DescribeDatasetImportJobResponse":
        return dc_td.DescribeDatasetImportJobResponse.make_one(res)

    def describe_event_tracker(
        self,
        res: "bs_td.DescribeEventTrackerResponseTypeDef",
    ) -> "dc_td.DescribeEventTrackerResponse":
        return dc_td.DescribeEventTrackerResponse.make_one(res)

    def describe_feature_transformation(
        self,
        res: "bs_td.DescribeFeatureTransformationResponseTypeDef",
    ) -> "dc_td.DescribeFeatureTransformationResponse":
        return dc_td.DescribeFeatureTransformationResponse.make_one(res)

    def describe_filter(
        self,
        res: "bs_td.DescribeFilterResponseTypeDef",
    ) -> "dc_td.DescribeFilterResponse":
        return dc_td.DescribeFilterResponse.make_one(res)

    def describe_metric_attribution(
        self,
        res: "bs_td.DescribeMetricAttributionResponseTypeDef",
    ) -> "dc_td.DescribeMetricAttributionResponse":
        return dc_td.DescribeMetricAttributionResponse.make_one(res)

    def describe_recipe(
        self,
        res: "bs_td.DescribeRecipeResponseTypeDef",
    ) -> "dc_td.DescribeRecipeResponse":
        return dc_td.DescribeRecipeResponse.make_one(res)

    def describe_recommender(
        self,
        res: "bs_td.DescribeRecommenderResponseTypeDef",
    ) -> "dc_td.DescribeRecommenderResponse":
        return dc_td.DescribeRecommenderResponse.make_one(res)

    def describe_schema(
        self,
        res: "bs_td.DescribeSchemaResponseTypeDef",
    ) -> "dc_td.DescribeSchemaResponse":
        return dc_td.DescribeSchemaResponse.make_one(res)

    def describe_solution(
        self,
        res: "bs_td.DescribeSolutionResponseTypeDef",
    ) -> "dc_td.DescribeSolutionResponse":
        return dc_td.DescribeSolutionResponse.make_one(res)

    def describe_solution_version(
        self,
        res: "bs_td.DescribeSolutionVersionResponseTypeDef",
    ) -> "dc_td.DescribeSolutionVersionResponse":
        return dc_td.DescribeSolutionVersionResponse.make_one(res)

    def get_solution_metrics(
        self,
        res: "bs_td.GetSolutionMetricsResponseTypeDef",
    ) -> "dc_td.GetSolutionMetricsResponse":
        return dc_td.GetSolutionMetricsResponse.make_one(res)

    def list_batch_inference_jobs(
        self,
        res: "bs_td.ListBatchInferenceJobsResponseTypeDef",
    ) -> "dc_td.ListBatchInferenceJobsResponse":
        return dc_td.ListBatchInferenceJobsResponse.make_one(res)

    def list_batch_segment_jobs(
        self,
        res: "bs_td.ListBatchSegmentJobsResponseTypeDef",
    ) -> "dc_td.ListBatchSegmentJobsResponse":
        return dc_td.ListBatchSegmentJobsResponse.make_one(res)

    def list_campaigns(
        self,
        res: "bs_td.ListCampaignsResponseTypeDef",
    ) -> "dc_td.ListCampaignsResponse":
        return dc_td.ListCampaignsResponse.make_one(res)

    def list_data_deletion_jobs(
        self,
        res: "bs_td.ListDataDeletionJobsResponseTypeDef",
    ) -> "dc_td.ListDataDeletionJobsResponse":
        return dc_td.ListDataDeletionJobsResponse.make_one(res)

    def list_dataset_export_jobs(
        self,
        res: "bs_td.ListDatasetExportJobsResponseTypeDef",
    ) -> "dc_td.ListDatasetExportJobsResponse":
        return dc_td.ListDatasetExportJobsResponse.make_one(res)

    def list_dataset_groups(
        self,
        res: "bs_td.ListDatasetGroupsResponseTypeDef",
    ) -> "dc_td.ListDatasetGroupsResponse":
        return dc_td.ListDatasetGroupsResponse.make_one(res)

    def list_dataset_import_jobs(
        self,
        res: "bs_td.ListDatasetImportJobsResponseTypeDef",
    ) -> "dc_td.ListDatasetImportJobsResponse":
        return dc_td.ListDatasetImportJobsResponse.make_one(res)

    def list_datasets(
        self,
        res: "bs_td.ListDatasetsResponseTypeDef",
    ) -> "dc_td.ListDatasetsResponse":
        return dc_td.ListDatasetsResponse.make_one(res)

    def list_event_trackers(
        self,
        res: "bs_td.ListEventTrackersResponseTypeDef",
    ) -> "dc_td.ListEventTrackersResponse":
        return dc_td.ListEventTrackersResponse.make_one(res)

    def list_filters(
        self,
        res: "bs_td.ListFiltersResponseTypeDef",
    ) -> "dc_td.ListFiltersResponse":
        return dc_td.ListFiltersResponse.make_one(res)

    def list_metric_attribution_metrics(
        self,
        res: "bs_td.ListMetricAttributionMetricsResponseTypeDef",
    ) -> "dc_td.ListMetricAttributionMetricsResponse":
        return dc_td.ListMetricAttributionMetricsResponse.make_one(res)

    def list_metric_attributions(
        self,
        res: "bs_td.ListMetricAttributionsResponseTypeDef",
    ) -> "dc_td.ListMetricAttributionsResponse":
        return dc_td.ListMetricAttributionsResponse.make_one(res)

    def list_recipes(
        self,
        res: "bs_td.ListRecipesResponseTypeDef",
    ) -> "dc_td.ListRecipesResponse":
        return dc_td.ListRecipesResponse.make_one(res)

    def list_recommenders(
        self,
        res: "bs_td.ListRecommendersResponseTypeDef",
    ) -> "dc_td.ListRecommendersResponse":
        return dc_td.ListRecommendersResponse.make_one(res)

    def list_schemas(
        self,
        res: "bs_td.ListSchemasResponseTypeDef",
    ) -> "dc_td.ListSchemasResponse":
        return dc_td.ListSchemasResponse.make_one(res)

    def list_solution_versions(
        self,
        res: "bs_td.ListSolutionVersionsResponseTypeDef",
    ) -> "dc_td.ListSolutionVersionsResponse":
        return dc_td.ListSolutionVersionsResponse.make_one(res)

    def list_solutions(
        self,
        res: "bs_td.ListSolutionsResponseTypeDef",
    ) -> "dc_td.ListSolutionsResponse":
        return dc_td.ListSolutionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_recommender(
        self,
        res: "bs_td.StartRecommenderResponseTypeDef",
    ) -> "dc_td.StartRecommenderResponse":
        return dc_td.StartRecommenderResponse.make_one(res)

    def stop_recommender(
        self,
        res: "bs_td.StopRecommenderResponseTypeDef",
    ) -> "dc_td.StopRecommenderResponse":
        return dc_td.StopRecommenderResponse.make_one(res)

    def stop_solution_version_creation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_campaign(
        self,
        res: "bs_td.UpdateCampaignResponseTypeDef",
    ) -> "dc_td.UpdateCampaignResponse":
        return dc_td.UpdateCampaignResponse.make_one(res)

    def update_dataset(
        self,
        res: "bs_td.UpdateDatasetResponseTypeDef",
    ) -> "dc_td.UpdateDatasetResponse":
        return dc_td.UpdateDatasetResponse.make_one(res)

    def update_metric_attribution(
        self,
        res: "bs_td.UpdateMetricAttributionResponseTypeDef",
    ) -> "dc_td.UpdateMetricAttributionResponse":
        return dc_td.UpdateMetricAttributionResponse.make_one(res)

    def update_recommender(
        self,
        res: "bs_td.UpdateRecommenderResponseTypeDef",
    ) -> "dc_td.UpdateRecommenderResponse":
        return dc_td.UpdateRecommenderResponse.make_one(res)

    def update_solution(
        self,
        res: "bs_td.UpdateSolutionResponseTypeDef",
    ) -> "dc_td.UpdateSolutionResponse":
        return dc_td.UpdateSolutionResponse.make_one(res)


personalize_caster = PERSONALIZECaster()
