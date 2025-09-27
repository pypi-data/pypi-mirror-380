# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ivs import type_defs as bs_td


class IVSCaster:

    def batch_get_channel(
        self,
        res: "bs_td.BatchGetChannelResponseTypeDef",
    ) -> "dc_td.BatchGetChannelResponse":
        return dc_td.BatchGetChannelResponse.make_one(res)

    def batch_get_stream_key(
        self,
        res: "bs_td.BatchGetStreamKeyResponseTypeDef",
    ) -> "dc_td.BatchGetStreamKeyResponse":
        return dc_td.BatchGetStreamKeyResponse.make_one(res)

    def batch_start_viewer_session_revocation(
        self,
        res: "bs_td.BatchStartViewerSessionRevocationResponseTypeDef",
    ) -> "dc_td.BatchStartViewerSessionRevocationResponse":
        return dc_td.BatchStartViewerSessionRevocationResponse.make_one(res)

    def create_channel(
        self,
        res: "bs_td.CreateChannelResponseTypeDef",
    ) -> "dc_td.CreateChannelResponse":
        return dc_td.CreateChannelResponse.make_one(res)

    def create_playback_restriction_policy(
        self,
        res: "bs_td.CreatePlaybackRestrictionPolicyResponseTypeDef",
    ) -> "dc_td.CreatePlaybackRestrictionPolicyResponse":
        return dc_td.CreatePlaybackRestrictionPolicyResponse.make_one(res)

    def create_recording_configuration(
        self,
        res: "bs_td.CreateRecordingConfigurationResponseTypeDef",
    ) -> "dc_td.CreateRecordingConfigurationResponse":
        return dc_td.CreateRecordingConfigurationResponse.make_one(res)

    def create_stream_key(
        self,
        res: "bs_td.CreateStreamKeyResponseTypeDef",
    ) -> "dc_td.CreateStreamKeyResponse":
        return dc_td.CreateStreamKeyResponse.make_one(res)

    def delete_channel(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_playback_restriction_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_recording_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_stream_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_channel(
        self,
        res: "bs_td.GetChannelResponseTypeDef",
    ) -> "dc_td.GetChannelResponse":
        return dc_td.GetChannelResponse.make_one(res)

    def get_playback_key_pair(
        self,
        res: "bs_td.GetPlaybackKeyPairResponseTypeDef",
    ) -> "dc_td.GetPlaybackKeyPairResponse":
        return dc_td.GetPlaybackKeyPairResponse.make_one(res)

    def get_playback_restriction_policy(
        self,
        res: "bs_td.GetPlaybackRestrictionPolicyResponseTypeDef",
    ) -> "dc_td.GetPlaybackRestrictionPolicyResponse":
        return dc_td.GetPlaybackRestrictionPolicyResponse.make_one(res)

    def get_recording_configuration(
        self,
        res: "bs_td.GetRecordingConfigurationResponseTypeDef",
    ) -> "dc_td.GetRecordingConfigurationResponse":
        return dc_td.GetRecordingConfigurationResponse.make_one(res)

    def get_stream(
        self,
        res: "bs_td.GetStreamResponseTypeDef",
    ) -> "dc_td.GetStreamResponse":
        return dc_td.GetStreamResponse.make_one(res)

    def get_stream_key(
        self,
        res: "bs_td.GetStreamKeyResponseTypeDef",
    ) -> "dc_td.GetStreamKeyResponse":
        return dc_td.GetStreamKeyResponse.make_one(res)

    def get_stream_session(
        self,
        res: "bs_td.GetStreamSessionResponseTypeDef",
    ) -> "dc_td.GetStreamSessionResponse":
        return dc_td.GetStreamSessionResponse.make_one(res)

    def import_playback_key_pair(
        self,
        res: "bs_td.ImportPlaybackKeyPairResponseTypeDef",
    ) -> "dc_td.ImportPlaybackKeyPairResponse":
        return dc_td.ImportPlaybackKeyPairResponse.make_one(res)

    def list_channels(
        self,
        res: "bs_td.ListChannelsResponseTypeDef",
    ) -> "dc_td.ListChannelsResponse":
        return dc_td.ListChannelsResponse.make_one(res)

    def list_playback_key_pairs(
        self,
        res: "bs_td.ListPlaybackKeyPairsResponseTypeDef",
    ) -> "dc_td.ListPlaybackKeyPairsResponse":
        return dc_td.ListPlaybackKeyPairsResponse.make_one(res)

    def list_playback_restriction_policies(
        self,
        res: "bs_td.ListPlaybackRestrictionPoliciesResponseTypeDef",
    ) -> "dc_td.ListPlaybackRestrictionPoliciesResponse":
        return dc_td.ListPlaybackRestrictionPoliciesResponse.make_one(res)

    def list_recording_configurations(
        self,
        res: "bs_td.ListRecordingConfigurationsResponseTypeDef",
    ) -> "dc_td.ListRecordingConfigurationsResponse":
        return dc_td.ListRecordingConfigurationsResponse.make_one(res)

    def list_stream_keys(
        self,
        res: "bs_td.ListStreamKeysResponseTypeDef",
    ) -> "dc_td.ListStreamKeysResponse":
        return dc_td.ListStreamKeysResponse.make_one(res)

    def list_stream_sessions(
        self,
        res: "bs_td.ListStreamSessionsResponseTypeDef",
    ) -> "dc_td.ListStreamSessionsResponse":
        return dc_td.ListStreamSessionsResponse.make_one(res)

    def list_streams(
        self,
        res: "bs_td.ListStreamsResponseTypeDef",
    ) -> "dc_td.ListStreamsResponse":
        return dc_td.ListStreamsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_metadata(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_channel(
        self,
        res: "bs_td.UpdateChannelResponseTypeDef",
    ) -> "dc_td.UpdateChannelResponse":
        return dc_td.UpdateChannelResponse.make_one(res)

    def update_playback_restriction_policy(
        self,
        res: "bs_td.UpdatePlaybackRestrictionPolicyResponseTypeDef",
    ) -> "dc_td.UpdatePlaybackRestrictionPolicyResponse":
        return dc_td.UpdatePlaybackRestrictionPolicyResponse.make_one(res)


ivs_caster = IVSCaster()
