# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotanalytics import type_defs as bs_td


class IOTANALYTICSCaster:

    def batch_put_message(
        self,
        res: "bs_td.BatchPutMessageResponseTypeDef",
    ) -> "dc_td.BatchPutMessageResponse":
        return dc_td.BatchPutMessageResponse.make_one(res)

    def create_channel(
        self,
        res: "bs_td.CreateChannelResponseTypeDef",
    ) -> "dc_td.CreateChannelResponse":
        return dc_td.CreateChannelResponse.make_one(res)

    def create_dataset(
        self,
        res: "bs_td.CreateDatasetResponseTypeDef",
    ) -> "dc_td.CreateDatasetResponse":
        return dc_td.CreateDatasetResponse.make_one(res)

    def create_dataset_content(
        self,
        res: "bs_td.CreateDatasetContentResponseTypeDef",
    ) -> "dc_td.CreateDatasetContentResponse":
        return dc_td.CreateDatasetContentResponse.make_one(res)

    def create_datastore(
        self,
        res: "bs_td.CreateDatastoreResponseTypeDef",
    ) -> "dc_td.CreateDatastoreResponse":
        return dc_td.CreateDatastoreResponse.make_one(res)

    def create_pipeline(
        self,
        res: "bs_td.CreatePipelineResponseTypeDef",
    ) -> "dc_td.CreatePipelineResponse":
        return dc_td.CreatePipelineResponse.make_one(res)

    def delete_channel(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_dataset(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_dataset_content(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_datastore(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_pipeline(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_channel(
        self,
        res: "bs_td.DescribeChannelResponseTypeDef",
    ) -> "dc_td.DescribeChannelResponse":
        return dc_td.DescribeChannelResponse.make_one(res)

    def describe_dataset(
        self,
        res: "bs_td.DescribeDatasetResponseTypeDef",
    ) -> "dc_td.DescribeDatasetResponse":
        return dc_td.DescribeDatasetResponse.make_one(res)

    def describe_datastore(
        self,
        res: "bs_td.DescribeDatastoreResponseTypeDef",
    ) -> "dc_td.DescribeDatastoreResponse":
        return dc_td.DescribeDatastoreResponse.make_one(res)

    def describe_logging_options(
        self,
        res: "bs_td.DescribeLoggingOptionsResponseTypeDef",
    ) -> "dc_td.DescribeLoggingOptionsResponse":
        return dc_td.DescribeLoggingOptionsResponse.make_one(res)

    def describe_pipeline(
        self,
        res: "bs_td.DescribePipelineResponseTypeDef",
    ) -> "dc_td.DescribePipelineResponse":
        return dc_td.DescribePipelineResponse.make_one(res)

    def get_dataset_content(
        self,
        res: "bs_td.GetDatasetContentResponseTypeDef",
    ) -> "dc_td.GetDatasetContentResponse":
        return dc_td.GetDatasetContentResponse.make_one(res)

    def list_channels(
        self,
        res: "bs_td.ListChannelsResponseTypeDef",
    ) -> "dc_td.ListChannelsResponse":
        return dc_td.ListChannelsResponse.make_one(res)

    def list_dataset_contents(
        self,
        res: "bs_td.ListDatasetContentsResponseTypeDef",
    ) -> "dc_td.ListDatasetContentsResponse":
        return dc_td.ListDatasetContentsResponse.make_one(res)

    def list_datasets(
        self,
        res: "bs_td.ListDatasetsResponseTypeDef",
    ) -> "dc_td.ListDatasetsResponse":
        return dc_td.ListDatasetsResponse.make_one(res)

    def list_datastores(
        self,
        res: "bs_td.ListDatastoresResponseTypeDef",
    ) -> "dc_td.ListDatastoresResponse":
        return dc_td.ListDatastoresResponse.make_one(res)

    def list_pipelines(
        self,
        res: "bs_td.ListPipelinesResponseTypeDef",
    ) -> "dc_td.ListPipelinesResponse":
        return dc_td.ListPipelinesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_logging_options(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def run_pipeline_activity(
        self,
        res: "bs_td.RunPipelineActivityResponseTypeDef",
    ) -> "dc_td.RunPipelineActivityResponse":
        return dc_td.RunPipelineActivityResponse.make_one(res)

    def sample_channel_data(
        self,
        res: "bs_td.SampleChannelDataResponseTypeDef",
    ) -> "dc_td.SampleChannelDataResponse":
        return dc_td.SampleChannelDataResponse.make_one(res)

    def start_pipeline_reprocessing(
        self,
        res: "bs_td.StartPipelineReprocessingResponseTypeDef",
    ) -> "dc_td.StartPipelineReprocessingResponse":
        return dc_td.StartPipelineReprocessingResponse.make_one(res)

    def update_channel(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_dataset(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_datastore(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_pipeline(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


iotanalytics_caster = IOTANALYTICSCaster()
