# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediapackage import type_defs as bs_td


class MEDIAPACKAGECaster:

    def configure_logs(
        self,
        res: "bs_td.ConfigureLogsResponseTypeDef",
    ) -> "dc_td.ConfigureLogsResponse":
        return dc_td.ConfigureLogsResponse.make_one(res)

    def create_channel(
        self,
        res: "bs_td.CreateChannelResponseTypeDef",
    ) -> "dc_td.CreateChannelResponse":
        return dc_td.CreateChannelResponse.make_one(res)

    def create_harvest_job(
        self,
        res: "bs_td.CreateHarvestJobResponseTypeDef",
    ) -> "dc_td.CreateHarvestJobResponse":
        return dc_td.CreateHarvestJobResponse.make_one(res)

    def create_origin_endpoint(
        self,
        res: "bs_td.CreateOriginEndpointResponseTypeDef",
    ) -> "dc_td.CreateOriginEndpointResponse":
        return dc_td.CreateOriginEndpointResponse.make_one(res)

    def describe_channel(
        self,
        res: "bs_td.DescribeChannelResponseTypeDef",
    ) -> "dc_td.DescribeChannelResponse":
        return dc_td.DescribeChannelResponse.make_one(res)

    def describe_harvest_job(
        self,
        res: "bs_td.DescribeHarvestJobResponseTypeDef",
    ) -> "dc_td.DescribeHarvestJobResponse":
        return dc_td.DescribeHarvestJobResponse.make_one(res)

    def describe_origin_endpoint(
        self,
        res: "bs_td.DescribeOriginEndpointResponseTypeDef",
    ) -> "dc_td.DescribeOriginEndpointResponse":
        return dc_td.DescribeOriginEndpointResponse.make_one(res)

    def list_channels(
        self,
        res: "bs_td.ListChannelsResponseTypeDef",
    ) -> "dc_td.ListChannelsResponse":
        return dc_td.ListChannelsResponse.make_one(res)

    def list_harvest_jobs(
        self,
        res: "bs_td.ListHarvestJobsResponseTypeDef",
    ) -> "dc_td.ListHarvestJobsResponse":
        return dc_td.ListHarvestJobsResponse.make_one(res)

    def list_origin_endpoints(
        self,
        res: "bs_td.ListOriginEndpointsResponseTypeDef",
    ) -> "dc_td.ListOriginEndpointsResponse":
        return dc_td.ListOriginEndpointsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def rotate_channel_credentials(
        self,
        res: "bs_td.RotateChannelCredentialsResponseTypeDef",
    ) -> "dc_td.RotateChannelCredentialsResponse":
        return dc_td.RotateChannelCredentialsResponse.make_one(res)

    def rotate_ingest_endpoint_credentials(
        self,
        res: "bs_td.RotateIngestEndpointCredentialsResponseTypeDef",
    ) -> "dc_td.RotateIngestEndpointCredentialsResponse":
        return dc_td.RotateIngestEndpointCredentialsResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_channel(
        self,
        res: "bs_td.UpdateChannelResponseTypeDef",
    ) -> "dc_td.UpdateChannelResponse":
        return dc_td.UpdateChannelResponse.make_one(res)

    def update_origin_endpoint(
        self,
        res: "bs_td.UpdateOriginEndpointResponseTypeDef",
    ) -> "dc_td.UpdateOriginEndpointResponse":
        return dc_td.UpdateOriginEndpointResponse.make_one(res)


mediapackage_caster = MEDIAPACKAGECaster()
