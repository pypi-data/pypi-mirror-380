# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediatailor import type_defs as bs_td


class MEDIATAILORCaster:

    def configure_logs_for_channel(
        self,
        res: "bs_td.ConfigureLogsForChannelResponseTypeDef",
    ) -> "dc_td.ConfigureLogsForChannelResponse":
        return dc_td.ConfigureLogsForChannelResponse.make_one(res)

    def configure_logs_for_playback_configuration(
        self,
        res: "bs_td.ConfigureLogsForPlaybackConfigurationResponseTypeDef",
    ) -> "dc_td.ConfigureLogsForPlaybackConfigurationResponse":
        return dc_td.ConfigureLogsForPlaybackConfigurationResponse.make_one(res)

    def create_channel(
        self,
        res: "bs_td.CreateChannelResponseTypeDef",
    ) -> "dc_td.CreateChannelResponse":
        return dc_td.CreateChannelResponse.make_one(res)

    def create_live_source(
        self,
        res: "bs_td.CreateLiveSourceResponseTypeDef",
    ) -> "dc_td.CreateLiveSourceResponse":
        return dc_td.CreateLiveSourceResponse.make_one(res)

    def create_prefetch_schedule(
        self,
        res: "bs_td.CreatePrefetchScheduleResponseTypeDef",
    ) -> "dc_td.CreatePrefetchScheduleResponse":
        return dc_td.CreatePrefetchScheduleResponse.make_one(res)

    def create_program(
        self,
        res: "bs_td.CreateProgramResponseTypeDef",
    ) -> "dc_td.CreateProgramResponse":
        return dc_td.CreateProgramResponse.make_one(res)

    def create_source_location(
        self,
        res: "bs_td.CreateSourceLocationResponseTypeDef",
    ) -> "dc_td.CreateSourceLocationResponse":
        return dc_td.CreateSourceLocationResponse.make_one(res)

    def create_vod_source(
        self,
        res: "bs_td.CreateVodSourceResponseTypeDef",
    ) -> "dc_td.CreateVodSourceResponse":
        return dc_td.CreateVodSourceResponse.make_one(res)

    def describe_channel(
        self,
        res: "bs_td.DescribeChannelResponseTypeDef",
    ) -> "dc_td.DescribeChannelResponse":
        return dc_td.DescribeChannelResponse.make_one(res)

    def describe_live_source(
        self,
        res: "bs_td.DescribeLiveSourceResponseTypeDef",
    ) -> "dc_td.DescribeLiveSourceResponse":
        return dc_td.DescribeLiveSourceResponse.make_one(res)

    def describe_program(
        self,
        res: "bs_td.DescribeProgramResponseTypeDef",
    ) -> "dc_td.DescribeProgramResponse":
        return dc_td.DescribeProgramResponse.make_one(res)

    def describe_source_location(
        self,
        res: "bs_td.DescribeSourceLocationResponseTypeDef",
    ) -> "dc_td.DescribeSourceLocationResponse":
        return dc_td.DescribeSourceLocationResponse.make_one(res)

    def describe_vod_source(
        self,
        res: "bs_td.DescribeVodSourceResponseTypeDef",
    ) -> "dc_td.DescribeVodSourceResponse":
        return dc_td.DescribeVodSourceResponse.make_one(res)

    def get_channel_policy(
        self,
        res: "bs_td.GetChannelPolicyResponseTypeDef",
    ) -> "dc_td.GetChannelPolicyResponse":
        return dc_td.GetChannelPolicyResponse.make_one(res)

    def get_channel_schedule(
        self,
        res: "bs_td.GetChannelScheduleResponseTypeDef",
    ) -> "dc_td.GetChannelScheduleResponse":
        return dc_td.GetChannelScheduleResponse.make_one(res)

    def get_playback_configuration(
        self,
        res: "bs_td.GetPlaybackConfigurationResponseTypeDef",
    ) -> "dc_td.GetPlaybackConfigurationResponse":
        return dc_td.GetPlaybackConfigurationResponse.make_one(res)

    def get_prefetch_schedule(
        self,
        res: "bs_td.GetPrefetchScheduleResponseTypeDef",
    ) -> "dc_td.GetPrefetchScheduleResponse":
        return dc_td.GetPrefetchScheduleResponse.make_one(res)

    def list_alerts(
        self,
        res: "bs_td.ListAlertsResponseTypeDef",
    ) -> "dc_td.ListAlertsResponse":
        return dc_td.ListAlertsResponse.make_one(res)

    def list_channels(
        self,
        res: "bs_td.ListChannelsResponseTypeDef",
    ) -> "dc_td.ListChannelsResponse":
        return dc_td.ListChannelsResponse.make_one(res)

    def list_live_sources(
        self,
        res: "bs_td.ListLiveSourcesResponseTypeDef",
    ) -> "dc_td.ListLiveSourcesResponse":
        return dc_td.ListLiveSourcesResponse.make_one(res)

    def list_playback_configurations(
        self,
        res: "bs_td.ListPlaybackConfigurationsResponseTypeDef",
    ) -> "dc_td.ListPlaybackConfigurationsResponse":
        return dc_td.ListPlaybackConfigurationsResponse.make_one(res)

    def list_prefetch_schedules(
        self,
        res: "bs_td.ListPrefetchSchedulesResponseTypeDef",
    ) -> "dc_td.ListPrefetchSchedulesResponse":
        return dc_td.ListPrefetchSchedulesResponse.make_one(res)

    def list_source_locations(
        self,
        res: "bs_td.ListSourceLocationsResponseTypeDef",
    ) -> "dc_td.ListSourceLocationsResponse":
        return dc_td.ListSourceLocationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_vod_sources(
        self,
        res: "bs_td.ListVodSourcesResponseTypeDef",
    ) -> "dc_td.ListVodSourcesResponse":
        return dc_td.ListVodSourcesResponse.make_one(res)

    def put_playback_configuration(
        self,
        res: "bs_td.PutPlaybackConfigurationResponseTypeDef",
    ) -> "dc_td.PutPlaybackConfigurationResponse":
        return dc_td.PutPlaybackConfigurationResponse.make_one(res)

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

    def update_live_source(
        self,
        res: "bs_td.UpdateLiveSourceResponseTypeDef",
    ) -> "dc_td.UpdateLiveSourceResponse":
        return dc_td.UpdateLiveSourceResponse.make_one(res)

    def update_program(
        self,
        res: "bs_td.UpdateProgramResponseTypeDef",
    ) -> "dc_td.UpdateProgramResponse":
        return dc_td.UpdateProgramResponse.make_one(res)

    def update_source_location(
        self,
        res: "bs_td.UpdateSourceLocationResponseTypeDef",
    ) -> "dc_td.UpdateSourceLocationResponse":
        return dc_td.UpdateSourceLocationResponse.make_one(res)

    def update_vod_source(
        self,
        res: "bs_td.UpdateVodSourceResponseTypeDef",
    ) -> "dc_td.UpdateVodSourceResponse":
        return dc_td.UpdateVodSourceResponse.make_one(res)


mediatailor_caster = MEDIATAILORCaster()
