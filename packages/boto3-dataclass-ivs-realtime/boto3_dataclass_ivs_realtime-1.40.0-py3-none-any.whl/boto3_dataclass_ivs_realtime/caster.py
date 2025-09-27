# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ivs_realtime import type_defs as bs_td


class IVS_REALTIMECaster:

    def create_encoder_configuration(
        self,
        res: "bs_td.CreateEncoderConfigurationResponseTypeDef",
    ) -> "dc_td.CreateEncoderConfigurationResponse":
        return dc_td.CreateEncoderConfigurationResponse.make_one(res)

    def create_ingest_configuration(
        self,
        res: "bs_td.CreateIngestConfigurationResponseTypeDef",
    ) -> "dc_td.CreateIngestConfigurationResponse":
        return dc_td.CreateIngestConfigurationResponse.make_one(res)

    def create_participant_token(
        self,
        res: "bs_td.CreateParticipantTokenResponseTypeDef",
    ) -> "dc_td.CreateParticipantTokenResponse":
        return dc_td.CreateParticipantTokenResponse.make_one(res)

    def create_stage(
        self,
        res: "bs_td.CreateStageResponseTypeDef",
    ) -> "dc_td.CreateStageResponse":
        return dc_td.CreateStageResponse.make_one(res)

    def create_storage_configuration(
        self,
        res: "bs_td.CreateStorageConfigurationResponseTypeDef",
    ) -> "dc_td.CreateStorageConfigurationResponse":
        return dc_td.CreateStorageConfigurationResponse.make_one(res)

    def get_composition(
        self,
        res: "bs_td.GetCompositionResponseTypeDef",
    ) -> "dc_td.GetCompositionResponse":
        return dc_td.GetCompositionResponse.make_one(res)

    def get_encoder_configuration(
        self,
        res: "bs_td.GetEncoderConfigurationResponseTypeDef",
    ) -> "dc_td.GetEncoderConfigurationResponse":
        return dc_td.GetEncoderConfigurationResponse.make_one(res)

    def get_ingest_configuration(
        self,
        res: "bs_td.GetIngestConfigurationResponseTypeDef",
    ) -> "dc_td.GetIngestConfigurationResponse":
        return dc_td.GetIngestConfigurationResponse.make_one(res)

    def get_participant(
        self,
        res: "bs_td.GetParticipantResponseTypeDef",
    ) -> "dc_td.GetParticipantResponse":
        return dc_td.GetParticipantResponse.make_one(res)

    def get_public_key(
        self,
        res: "bs_td.GetPublicKeyResponseTypeDef",
    ) -> "dc_td.GetPublicKeyResponse":
        return dc_td.GetPublicKeyResponse.make_one(res)

    def get_stage(
        self,
        res: "bs_td.GetStageResponseTypeDef",
    ) -> "dc_td.GetStageResponse":
        return dc_td.GetStageResponse.make_one(res)

    def get_stage_session(
        self,
        res: "bs_td.GetStageSessionResponseTypeDef",
    ) -> "dc_td.GetStageSessionResponse":
        return dc_td.GetStageSessionResponse.make_one(res)

    def get_storage_configuration(
        self,
        res: "bs_td.GetStorageConfigurationResponseTypeDef",
    ) -> "dc_td.GetStorageConfigurationResponse":
        return dc_td.GetStorageConfigurationResponse.make_one(res)

    def import_public_key(
        self,
        res: "bs_td.ImportPublicKeyResponseTypeDef",
    ) -> "dc_td.ImportPublicKeyResponse":
        return dc_td.ImportPublicKeyResponse.make_one(res)

    def list_compositions(
        self,
        res: "bs_td.ListCompositionsResponseTypeDef",
    ) -> "dc_td.ListCompositionsResponse":
        return dc_td.ListCompositionsResponse.make_one(res)

    def list_encoder_configurations(
        self,
        res: "bs_td.ListEncoderConfigurationsResponseTypeDef",
    ) -> "dc_td.ListEncoderConfigurationsResponse":
        return dc_td.ListEncoderConfigurationsResponse.make_one(res)

    def list_ingest_configurations(
        self,
        res: "bs_td.ListIngestConfigurationsResponseTypeDef",
    ) -> "dc_td.ListIngestConfigurationsResponse":
        return dc_td.ListIngestConfigurationsResponse.make_one(res)

    def list_participant_events(
        self,
        res: "bs_td.ListParticipantEventsResponseTypeDef",
    ) -> "dc_td.ListParticipantEventsResponse":
        return dc_td.ListParticipantEventsResponse.make_one(res)

    def list_participant_replicas(
        self,
        res: "bs_td.ListParticipantReplicasResponseTypeDef",
    ) -> "dc_td.ListParticipantReplicasResponse":
        return dc_td.ListParticipantReplicasResponse.make_one(res)

    def list_participants(
        self,
        res: "bs_td.ListParticipantsResponseTypeDef",
    ) -> "dc_td.ListParticipantsResponse":
        return dc_td.ListParticipantsResponse.make_one(res)

    def list_public_keys(
        self,
        res: "bs_td.ListPublicKeysResponseTypeDef",
    ) -> "dc_td.ListPublicKeysResponse":
        return dc_td.ListPublicKeysResponse.make_one(res)

    def list_stage_sessions(
        self,
        res: "bs_td.ListStageSessionsResponseTypeDef",
    ) -> "dc_td.ListStageSessionsResponse":
        return dc_td.ListStageSessionsResponse.make_one(res)

    def list_stages(
        self,
        res: "bs_td.ListStagesResponseTypeDef",
    ) -> "dc_td.ListStagesResponse":
        return dc_td.ListStagesResponse.make_one(res)

    def list_storage_configurations(
        self,
        res: "bs_td.ListStorageConfigurationsResponseTypeDef",
    ) -> "dc_td.ListStorageConfigurationsResponse":
        return dc_td.ListStorageConfigurationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_composition(
        self,
        res: "bs_td.StartCompositionResponseTypeDef",
    ) -> "dc_td.StartCompositionResponse":
        return dc_td.StartCompositionResponse.make_one(res)

    def start_participant_replication(
        self,
        res: "bs_td.StartParticipantReplicationResponseTypeDef",
    ) -> "dc_td.StartParticipantReplicationResponse":
        return dc_td.StartParticipantReplicationResponse.make_one(res)

    def stop_participant_replication(
        self,
        res: "bs_td.StopParticipantReplicationResponseTypeDef",
    ) -> "dc_td.StopParticipantReplicationResponse":
        return dc_td.StopParticipantReplicationResponse.make_one(res)

    def update_ingest_configuration(
        self,
        res: "bs_td.UpdateIngestConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateIngestConfigurationResponse":
        return dc_td.UpdateIngestConfigurationResponse.make_one(res)

    def update_stage(
        self,
        res: "bs_td.UpdateStageResponseTypeDef",
    ) -> "dc_td.UpdateStageResponse":
        return dc_td.UpdateStageResponse.make_one(res)


ivs_realtime_caster = IVS_REALTIMECaster()
