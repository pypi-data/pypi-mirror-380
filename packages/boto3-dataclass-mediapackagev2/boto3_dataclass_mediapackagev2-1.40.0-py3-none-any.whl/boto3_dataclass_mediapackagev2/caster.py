# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediapackagev2 import type_defs as bs_td


class MEDIAPACKAGEV2Caster:

    def create_channel(
        self,
        res: "bs_td.CreateChannelResponseTypeDef",
    ) -> "dc_td.CreateChannelResponse":
        return dc_td.CreateChannelResponse.make_one(res)

    def create_channel_group(
        self,
        res: "bs_td.CreateChannelGroupResponseTypeDef",
    ) -> "dc_td.CreateChannelGroupResponse":
        return dc_td.CreateChannelGroupResponse.make_one(res)

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

    def get_channel(
        self,
        res: "bs_td.GetChannelResponseTypeDef",
    ) -> "dc_td.GetChannelResponse":
        return dc_td.GetChannelResponse.make_one(res)

    def get_channel_group(
        self,
        res: "bs_td.GetChannelGroupResponseTypeDef",
    ) -> "dc_td.GetChannelGroupResponse":
        return dc_td.GetChannelGroupResponse.make_one(res)

    def get_channel_policy(
        self,
        res: "bs_td.GetChannelPolicyResponseTypeDef",
    ) -> "dc_td.GetChannelPolicyResponse":
        return dc_td.GetChannelPolicyResponse.make_one(res)

    def get_harvest_job(
        self,
        res: "bs_td.GetHarvestJobResponseTypeDef",
    ) -> "dc_td.GetHarvestJobResponse":
        return dc_td.GetHarvestJobResponse.make_one(res)

    def get_origin_endpoint(
        self,
        res: "bs_td.GetOriginEndpointResponseTypeDef",
    ) -> "dc_td.GetOriginEndpointResponse":
        return dc_td.GetOriginEndpointResponse.make_one(res)

    def get_origin_endpoint_policy(
        self,
        res: "bs_td.GetOriginEndpointPolicyResponseTypeDef",
    ) -> "dc_td.GetOriginEndpointPolicyResponse":
        return dc_td.GetOriginEndpointPolicyResponse.make_one(res)

    def list_channel_groups(
        self,
        res: "bs_td.ListChannelGroupsResponseTypeDef",
    ) -> "dc_td.ListChannelGroupsResponse":
        return dc_td.ListChannelGroupsResponse.make_one(res)

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

    def reset_channel_state(
        self,
        res: "bs_td.ResetChannelStateResponseTypeDef",
    ) -> "dc_td.ResetChannelStateResponse":
        return dc_td.ResetChannelStateResponse.make_one(res)

    def reset_origin_endpoint_state(
        self,
        res: "bs_td.ResetOriginEndpointStateResponseTypeDef",
    ) -> "dc_td.ResetOriginEndpointStateResponse":
        return dc_td.ResetOriginEndpointStateResponse.make_one(res)

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

    def update_channel_group(
        self,
        res: "bs_td.UpdateChannelGroupResponseTypeDef",
    ) -> "dc_td.UpdateChannelGroupResponse":
        return dc_td.UpdateChannelGroupResponse.make_one(res)

    def update_origin_endpoint(
        self,
        res: "bs_td.UpdateOriginEndpointResponseTypeDef",
    ) -> "dc_td.UpdateOriginEndpointResponse":
        return dc_td.UpdateOriginEndpointResponse.make_one(res)


mediapackagev2_caster = MEDIAPACKAGEV2Caster()
