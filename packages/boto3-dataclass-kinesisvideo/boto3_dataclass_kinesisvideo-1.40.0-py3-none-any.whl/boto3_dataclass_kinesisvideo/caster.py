# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesisvideo import type_defs as bs_td


class KINESISVIDEOCaster:

    def create_signaling_channel(
        self,
        res: "bs_td.CreateSignalingChannelOutputTypeDef",
    ) -> "dc_td.CreateSignalingChannelOutput":
        return dc_td.CreateSignalingChannelOutput.make_one(res)

    def create_stream(
        self,
        res: "bs_td.CreateStreamOutputTypeDef",
    ) -> "dc_td.CreateStreamOutput":
        return dc_td.CreateStreamOutput.make_one(res)

    def describe_edge_configuration(
        self,
        res: "bs_td.DescribeEdgeConfigurationOutputTypeDef",
    ) -> "dc_td.DescribeEdgeConfigurationOutput":
        return dc_td.DescribeEdgeConfigurationOutput.make_one(res)

    def describe_image_generation_configuration(
        self,
        res: "bs_td.DescribeImageGenerationConfigurationOutputTypeDef",
    ) -> "dc_td.DescribeImageGenerationConfigurationOutput":
        return dc_td.DescribeImageGenerationConfigurationOutput.make_one(res)

    def describe_mapped_resource_configuration(
        self,
        res: "bs_td.DescribeMappedResourceConfigurationOutputTypeDef",
    ) -> "dc_td.DescribeMappedResourceConfigurationOutput":
        return dc_td.DescribeMappedResourceConfigurationOutput.make_one(res)

    def describe_media_storage_configuration(
        self,
        res: "bs_td.DescribeMediaStorageConfigurationOutputTypeDef",
    ) -> "dc_td.DescribeMediaStorageConfigurationOutput":
        return dc_td.DescribeMediaStorageConfigurationOutput.make_one(res)

    def describe_notification_configuration(
        self,
        res: "bs_td.DescribeNotificationConfigurationOutputTypeDef",
    ) -> "dc_td.DescribeNotificationConfigurationOutput":
        return dc_td.DescribeNotificationConfigurationOutput.make_one(res)

    def describe_signaling_channel(
        self,
        res: "bs_td.DescribeSignalingChannelOutputTypeDef",
    ) -> "dc_td.DescribeSignalingChannelOutput":
        return dc_td.DescribeSignalingChannelOutput.make_one(res)

    def describe_stream(
        self,
        res: "bs_td.DescribeStreamOutputTypeDef",
    ) -> "dc_td.DescribeStreamOutput":
        return dc_td.DescribeStreamOutput.make_one(res)

    def get_data_endpoint(
        self,
        res: "bs_td.GetDataEndpointOutputTypeDef",
    ) -> "dc_td.GetDataEndpointOutput":
        return dc_td.GetDataEndpointOutput.make_one(res)

    def get_signaling_channel_endpoint(
        self,
        res: "bs_td.GetSignalingChannelEndpointOutputTypeDef",
    ) -> "dc_td.GetSignalingChannelEndpointOutput":
        return dc_td.GetSignalingChannelEndpointOutput.make_one(res)

    def list_edge_agent_configurations(
        self,
        res: "bs_td.ListEdgeAgentConfigurationsOutputTypeDef",
    ) -> "dc_td.ListEdgeAgentConfigurationsOutput":
        return dc_td.ListEdgeAgentConfigurationsOutput.make_one(res)

    def list_signaling_channels(
        self,
        res: "bs_td.ListSignalingChannelsOutputTypeDef",
    ) -> "dc_td.ListSignalingChannelsOutput":
        return dc_td.ListSignalingChannelsOutput.make_one(res)

    def list_streams(
        self,
        res: "bs_td.ListStreamsOutputTypeDef",
    ) -> "dc_td.ListStreamsOutput":
        return dc_td.ListStreamsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_tags_for_stream(
        self,
        res: "bs_td.ListTagsForStreamOutputTypeDef",
    ) -> "dc_td.ListTagsForStreamOutput":
        return dc_td.ListTagsForStreamOutput.make_one(res)

    def start_edge_configuration_update(
        self,
        res: "bs_td.StartEdgeConfigurationUpdateOutputTypeDef",
    ) -> "dc_td.StartEdgeConfigurationUpdateOutput":
        return dc_td.StartEdgeConfigurationUpdateOutput.make_one(res)


kinesisvideo_caster = KINESISVIDEOCaster()
