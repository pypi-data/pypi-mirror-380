# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ivs_realtime import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ParticipantRecordingHlsConfiguration:
    boto3_raw_data: "type_defs.ParticipantRecordingHlsConfigurationTypeDef" = (
        dataclasses.field()
    )

    targetSegmentDurationSeconds = field("targetSegmentDurationSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParticipantRecordingHlsConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantRecordingHlsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantThumbnailConfigurationOutput:
    boto3_raw_data: "type_defs.ParticipantThumbnailConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    targetIntervalSeconds = field("targetIntervalSeconds")
    storage = field("storage")
    recordingMode = field("recordingMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParticipantThumbnailConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantThumbnailConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantThumbnailConfiguration:
    boto3_raw_data: "type_defs.ParticipantThumbnailConfigurationTypeDef" = (
        dataclasses.field()
    )

    targetIntervalSeconds = field("targetIntervalSeconds")
    storage = field("storage")
    recordingMode = field("recordingMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParticipantThumbnailConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantThumbnailConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelDestinationConfiguration:
    boto3_raw_data: "type_defs.ChannelDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    channelArn = field("channelArn")
    encoderConfigurationArn = field("encoderConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ChannelDestinationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositionRecordingHlsConfiguration:
    boto3_raw_data: "type_defs.CompositionRecordingHlsConfigurationTypeDef" = (
        dataclasses.field()
    )

    targetSegmentDurationSeconds = field("targetSegmentDurationSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompositionRecordingHlsConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositionRecordingHlsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationSummary:
    boto3_raw_data: "type_defs.DestinationSummaryTypeDef" = dataclasses.field()

    id = field("id")
    state = field("state")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositionThumbnailConfigurationOutput:
    boto3_raw_data: "type_defs.CompositionThumbnailConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    targetIntervalSeconds = field("targetIntervalSeconds")
    storage = field("storage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompositionThumbnailConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositionThumbnailConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositionThumbnailConfiguration:
    boto3_raw_data: "type_defs.CompositionThumbnailConfigurationTypeDef" = (
        dataclasses.field()
    )

    targetIntervalSeconds = field("targetIntervalSeconds")
    storage = field("storage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompositionThumbnailConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositionThumbnailConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Video:
    boto3_raw_data: "type_defs.VideoTypeDef" = dataclasses.field()

    width = field("width")
    height = field("height")
    framerate = field("framerate")
    bitrate = field("bitrate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoTypeDef"]]
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
class CreateIngestConfigurationRequest:
    boto3_raw_data: "type_defs.CreateIngestConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ingestProtocol = field("ingestProtocol")
    name = field("name")
    stageArn = field("stageArn")
    userId = field("userId")
    attributes = field("attributes")
    insecureIngest = field("insecureIngest")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateIngestConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIngestConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestConfiguration:
    boto3_raw_data: "type_defs.IngestConfigurationTypeDef" = dataclasses.field()

    arn = field("arn")
    ingestProtocol = field("ingestProtocol")
    streamKey = field("streamKey")
    stageArn = field("stageArn")
    participantId = field("participantId")
    state = field("state")
    name = field("name")
    userId = field("userId")
    attributes = field("attributes")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateParticipantTokenRequest:
    boto3_raw_data: "type_defs.CreateParticipantTokenRequestTypeDef" = (
        dataclasses.field()
    )

    stageArn = field("stageArn")
    duration = field("duration")
    userId = field("userId")
    attributes = field("attributes")
    capabilities = field("capabilities")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateParticipantTokenRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateParticipantTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantToken:
    boto3_raw_data: "type_defs.ParticipantTokenTypeDef" = dataclasses.field()

    participantId = field("participantId")
    token = field("token")
    userId = field("userId")
    attributes = field("attributes")
    duration = field("duration")
    capabilities = field("capabilities")
    expirationTime = field("expirationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParticipantTokenTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantTokenTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantTokenConfiguration:
    boto3_raw_data: "type_defs.ParticipantTokenConfigurationTypeDef" = (
        dataclasses.field()
    )

    duration = field("duration")
    userId = field("userId")
    attributes = field("attributes")
    capabilities = field("capabilities")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ParticipantTokenConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantTokenConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3StorageConfiguration:
    boto3_raw_data: "type_defs.S3StorageConfigurationTypeDef" = dataclasses.field()

    bucketName = field("bucketName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3StorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3StorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEncoderConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteEncoderConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEncoderConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEncoderConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIngestConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteIngestConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    force = field("force")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteIngestConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIngestConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePublicKeyRequest:
    boto3_raw_data: "type_defs.DeletePublicKeyRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStageRequest:
    boto3_raw_data: "type_defs.DeleteStageRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStorageConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteStorageConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteStorageConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStorageConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Detail:
    boto3_raw_data: "type_defs.S3DetailTypeDef" = dataclasses.field()

    recordingPrefix = field("recordingPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisconnectParticipantRequest:
    boto3_raw_data: "type_defs.DisconnectParticipantRequestTypeDef" = (
        dataclasses.field()
    )

    stageArn = field("stageArn")
    participantId = field("participantId")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisconnectParticipantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisconnectParticipantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncoderConfigurationSummary:
    boto3_raw_data: "type_defs.EncoderConfigurationSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncoderConfigurationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncoderConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    name = field("name")
    participantId = field("participantId")
    eventTime = field("eventTime")
    remoteParticipantId = field("remoteParticipantId")
    errorCode = field("errorCode")
    destinationStageArn = field("destinationStageArn")
    destinationSessionId = field("destinationSessionId")
    replica = field("replica")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCompositionRequest:
    boto3_raw_data: "type_defs.GetCompositionRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCompositionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCompositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEncoderConfigurationRequest:
    boto3_raw_data: "type_defs.GetEncoderConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEncoderConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEncoderConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIngestConfigurationRequest:
    boto3_raw_data: "type_defs.GetIngestConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIngestConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIngestConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParticipantRequest:
    boto3_raw_data: "type_defs.GetParticipantRequestTypeDef" = dataclasses.field()

    stageArn = field("stageArn")
    sessionId = field("sessionId")
    participantId = field("participantId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParticipantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParticipantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Participant:
    boto3_raw_data: "type_defs.ParticipantTypeDef" = dataclasses.field()

    participantId = field("participantId")
    userId = field("userId")
    state = field("state")
    firstJoinTime = field("firstJoinTime")
    attributes = field("attributes")
    published = field("published")
    ispName = field("ispName")
    osName = field("osName")
    osVersion = field("osVersion")
    browserName = field("browserName")
    browserVersion = field("browserVersion")
    sdkVersion = field("sdkVersion")
    recordingS3BucketName = field("recordingS3BucketName")
    recordingS3Prefix = field("recordingS3Prefix")
    recordingState = field("recordingState")
    protocol = field("protocol")
    replicationType = field("replicationType")
    replicationState = field("replicationState")
    sourceStageArn = field("sourceStageArn")
    sourceSessionId = field("sourceSessionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParticipantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParticipantTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicKeyRequest:
    boto3_raw_data: "type_defs.GetPublicKeyRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicKey:
    boto3_raw_data: "type_defs.PublicKeyTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    publicKeyMaterial = field("publicKeyMaterial")
    fingerprint = field("fingerprint")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublicKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PublicKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStageRequest:
    boto3_raw_data: "type_defs.GetStageRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetStageRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStageSessionRequest:
    boto3_raw_data: "type_defs.GetStageSessionRequestTypeDef" = dataclasses.field()

    stageArn = field("stageArn")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStageSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStageSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageSession:
    boto3_raw_data: "type_defs.StageSessionTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageSessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageSessionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageConfigurationRequest:
    boto3_raw_data: "type_defs.GetStorageConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetStorageConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GridConfiguration:
    boto3_raw_data: "type_defs.GridConfigurationTypeDef" = dataclasses.field()

    featuredParticipantAttribute = field("featuredParticipantAttribute")
    omitStoppedVideo = field("omitStoppedVideo")
    videoAspectRatio = field("videoAspectRatio")
    videoFillMode = field("videoFillMode")
    gridGap = field("gridGap")
    participantOrderAttribute = field("participantOrderAttribute")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GridConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GridConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportPublicKeyRequest:
    boto3_raw_data: "type_defs.ImportPublicKeyRequestTypeDef" = dataclasses.field()

    publicKeyMaterial = field("publicKeyMaterial")
    name = field("name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportPublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportPublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestConfigurationSummary:
    boto3_raw_data: "type_defs.IngestConfigurationSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    ingestProtocol = field("ingestProtocol")
    stageArn = field("stageArn")
    participantId = field("participantId")
    state = field("state")
    name = field("name")
    userId = field("userId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestConfigurationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipConfiguration:
    boto3_raw_data: "type_defs.PipConfigurationTypeDef" = dataclasses.field()

    featuredParticipantAttribute = field("featuredParticipantAttribute")
    omitStoppedVideo = field("omitStoppedVideo")
    videoFillMode = field("videoFillMode")
    gridGap = field("gridGap")
    pipParticipantAttribute = field("pipParticipantAttribute")
    pipBehavior = field("pipBehavior")
    pipOffset = field("pipOffset")
    pipPosition = field("pipPosition")
    pipWidth = field("pipWidth")
    pipHeight = field("pipHeight")
    participantOrderAttribute = field("participantOrderAttribute")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCompositionsRequest:
    boto3_raw_data: "type_defs.ListCompositionsRequestTypeDef" = dataclasses.field()

    filterByStageArn = field("filterByStageArn")
    filterByEncoderConfigurationArn = field("filterByEncoderConfigurationArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCompositionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCompositionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEncoderConfigurationsRequest:
    boto3_raw_data: "type_defs.ListEncoderConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEncoderConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEncoderConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIngestConfigurationsRequest:
    boto3_raw_data: "type_defs.ListIngestConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    filterByStageArn = field("filterByStageArn")
    filterByState = field("filterByState")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIngestConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIngestConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListParticipantEventsRequest:
    boto3_raw_data: "type_defs.ListParticipantEventsRequestTypeDef" = (
        dataclasses.field()
    )

    stageArn = field("stageArn")
    sessionId = field("sessionId")
    participantId = field("participantId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListParticipantEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListParticipantEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListParticipantReplicasRequest:
    boto3_raw_data: "type_defs.ListParticipantReplicasRequestTypeDef" = (
        dataclasses.field()
    )

    sourceStageArn = field("sourceStageArn")
    participantId = field("participantId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListParticipantReplicasRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListParticipantReplicasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantReplica:
    boto3_raw_data: "type_defs.ParticipantReplicaTypeDef" = dataclasses.field()

    sourceStageArn = field("sourceStageArn")
    participantId = field("participantId")
    sourceSessionId = field("sourceSessionId")
    destinationStageArn = field("destinationStageArn")
    destinationSessionId = field("destinationSessionId")
    replicationState = field("replicationState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipantReplicaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantReplicaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListParticipantsRequest:
    boto3_raw_data: "type_defs.ListParticipantsRequestTypeDef" = dataclasses.field()

    stageArn = field("stageArn")
    sessionId = field("sessionId")
    filterByUserId = field("filterByUserId")
    filterByPublished = field("filterByPublished")
    filterByState = field("filterByState")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    filterByRecordingState = field("filterByRecordingState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListParticipantsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListParticipantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantSummary:
    boto3_raw_data: "type_defs.ParticipantSummaryTypeDef" = dataclasses.field()

    participantId = field("participantId")
    userId = field("userId")
    state = field("state")
    firstJoinTime = field("firstJoinTime")
    published = field("published")
    recordingState = field("recordingState")
    replicationType = field("replicationType")
    replicationState = field("replicationState")
    sourceStageArn = field("sourceStageArn")
    sourceSessionId = field("sourceSessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipantSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublicKeysRequest:
    boto3_raw_data: "type_defs.ListPublicKeysRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPublicKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublicKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicKeySummary:
    boto3_raw_data: "type_defs.PublicKeySummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublicKeySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublicKeySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStageSessionsRequest:
    boto3_raw_data: "type_defs.ListStageSessionsRequestTypeDef" = dataclasses.field()

    stageArn = field("stageArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStageSessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStageSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageSessionSummary:
    boto3_raw_data: "type_defs.StageSessionSummaryTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StageSessionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StageSessionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStagesRequest:
    boto3_raw_data: "type_defs.ListStagesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStagesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageSummary:
    boto3_raw_data: "type_defs.StageSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    activeSessionId = field("activeSessionId")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageConfigurationsRequest:
    boto3_raw_data: "type_defs.ListStorageConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStorageConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageConfigurationsRequestTypeDef"]
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

    resourceArn = field("resourceArn")

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
class StageEndpoints:
    boto3_raw_data: "type_defs.StageEndpointsTypeDef" = dataclasses.field()

    events = field("events")
    whip = field("whip")
    rtmp = field("rtmp")
    rtmps = field("rtmps")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageEndpointsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageEndpointsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartParticipantReplicationRequest:
    boto3_raw_data: "type_defs.StartParticipantReplicationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceStageArn = field("sourceStageArn")
    destinationStageArn = field("destinationStageArn")
    participantId = field("participantId")
    reconnectWindowSeconds = field("reconnectWindowSeconds")
    attributes = field("attributes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartParticipantReplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartParticipantReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopCompositionRequest:
    boto3_raw_data: "type_defs.StopCompositionRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopCompositionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopCompositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopParticipantReplicationRequest:
    boto3_raw_data: "type_defs.StopParticipantReplicationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceStageArn = field("sourceStageArn")
    destinationStageArn = field("destinationStageArn")
    participantId = field("participantId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopParticipantReplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopParticipantReplicationRequestTypeDef"]
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

    resourceArn = field("resourceArn")
    tags = field("tags")

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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class UpdateIngestConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateIngestConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    stageArn = field("stageArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateIngestConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIngestConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoParticipantRecordingConfigurationOutput:
    boto3_raw_data: "type_defs.AutoParticipantRecordingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    storageConfigurationArn = field("storageConfigurationArn")
    mediaTypes = field("mediaTypes")

    @cached_property
    def thumbnailConfiguration(self):  # pragma: no cover
        return ParticipantThumbnailConfigurationOutput.make_one(
            self.boto3_raw_data["thumbnailConfiguration"]
        )

    recordingReconnectWindowSeconds = field("recordingReconnectWindowSeconds")

    @cached_property
    def hlsConfiguration(self):  # pragma: no cover
        return ParticipantRecordingHlsConfiguration.make_one(
            self.boto3_raw_data["hlsConfiguration"]
        )

    recordParticipantReplicas = field("recordParticipantReplicas")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoParticipantRecordingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoParticipantRecordingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoParticipantRecordingConfiguration:
    boto3_raw_data: "type_defs.AutoParticipantRecordingConfigurationTypeDef" = (
        dataclasses.field()
    )

    storageConfigurationArn = field("storageConfigurationArn")
    mediaTypes = field("mediaTypes")

    @cached_property
    def thumbnailConfiguration(self):  # pragma: no cover
        return ParticipantThumbnailConfiguration.make_one(
            self.boto3_raw_data["thumbnailConfiguration"]
        )

    recordingReconnectWindowSeconds = field("recordingReconnectWindowSeconds")

    @cached_property
    def hlsConfiguration(self):  # pragma: no cover
        return ParticipantRecordingHlsConfiguration.make_one(
            self.boto3_raw_data["hlsConfiguration"]
        )

    recordParticipantReplicas = field("recordParticipantReplicas")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoParticipantRecordingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoParticipantRecordingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingConfiguration:
    boto3_raw_data: "type_defs.RecordingConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def hlsConfiguration(self):  # pragma: no cover
        return CompositionRecordingHlsConfiguration.make_one(
            self.boto3_raw_data["hlsConfiguration"]
        )

    format = field("format")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecordingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositionSummary:
    boto3_raw_data: "type_defs.CompositionSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    stageArn = field("stageArn")

    @cached_property
    def destinations(self):  # pragma: no cover
        return DestinationSummary.make_many(self.boto3_raw_data["destinations"])

    state = field("state")
    tags = field("tags")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompositionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEncoderConfigurationRequest:
    boto3_raw_data: "type_defs.CreateEncoderConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["video"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEncoderConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEncoderConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncoderConfiguration:
    boto3_raw_data: "type_defs.EncoderConfigurationTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")

    @cached_property
    def video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["video"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncoderConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncoderConfigurationTypeDef"]
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

    tags = field("tags")

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
class StartParticipantReplicationResponse:
    boto3_raw_data: "type_defs.StartParticipantReplicationResponseTypeDef" = (
        dataclasses.field()
    )

    accessControlAllowOrigin = field("accessControlAllowOrigin")
    accessControlExposeHeaders = field("accessControlExposeHeaders")
    cacheControl = field("cacheControl")
    contentSecurityPolicy = field("contentSecurityPolicy")
    strictTransportSecurity = field("strictTransportSecurity")
    xContentTypeOptions = field("xContentTypeOptions")
    xFrameOptions = field("xFrameOptions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartParticipantReplicationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartParticipantReplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopParticipantReplicationResponse:
    boto3_raw_data: "type_defs.StopParticipantReplicationResponseTypeDef" = (
        dataclasses.field()
    )

    accessControlAllowOrigin = field("accessControlAllowOrigin")
    accessControlExposeHeaders = field("accessControlExposeHeaders")
    cacheControl = field("cacheControl")
    contentSecurityPolicy = field("contentSecurityPolicy")
    strictTransportSecurity = field("strictTransportSecurity")
    xContentTypeOptions = field("xContentTypeOptions")
    xFrameOptions = field("xFrameOptions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopParticipantReplicationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopParticipantReplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIngestConfigurationResponse:
    boto3_raw_data: "type_defs.CreateIngestConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ingestConfiguration(self):  # pragma: no cover
        return IngestConfiguration.make_one(self.boto3_raw_data["ingestConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateIngestConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIngestConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIngestConfigurationResponse:
    boto3_raw_data: "type_defs.GetIngestConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ingestConfiguration(self):  # pragma: no cover
        return IngestConfiguration.make_one(self.boto3_raw_data["ingestConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIngestConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIngestConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIngestConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateIngestConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ingestConfiguration(self):  # pragma: no cover
        return IngestConfiguration.make_one(self.boto3_raw_data["ingestConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateIngestConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIngestConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateParticipantTokenResponse:
    boto3_raw_data: "type_defs.CreateParticipantTokenResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def participantToken(self):  # pragma: no cover
        return ParticipantToken.make_one(self.boto3_raw_data["participantToken"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateParticipantTokenResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateParticipantTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStorageConfigurationRequest:
    boto3_raw_data: "type_defs.CreateStorageConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3(self):  # pragma: no cover
        return S3StorageConfiguration.make_one(self.boto3_raw_data["s3"])

    name = field("name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStorageConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStorageConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageConfigurationSummary:
    boto3_raw_data: "type_defs.StorageConfigurationSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")

    @cached_property
    def s3(self):  # pragma: no cover
        return S3StorageConfiguration.make_one(self.boto3_raw_data["s3"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageConfigurationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageConfiguration:
    boto3_raw_data: "type_defs.StorageConfigurationTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")

    @cached_property
    def s3(self):  # pragma: no cover
        return S3StorageConfiguration.make_one(self.boto3_raw_data["s3"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationDetail:
    boto3_raw_data: "type_defs.DestinationDetailTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Detail.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEncoderConfigurationsResponse:
    boto3_raw_data: "type_defs.ListEncoderConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def encoderConfigurations(self):  # pragma: no cover
        return EncoderConfigurationSummary.make_many(
            self.boto3_raw_data["encoderConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEncoderConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEncoderConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListParticipantEventsResponse:
    boto3_raw_data: "type_defs.ListParticipantEventsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListParticipantEventsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListParticipantEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParticipantResponse:
    boto3_raw_data: "type_defs.GetParticipantResponseTypeDef" = dataclasses.field()

    @cached_property
    def participant(self):  # pragma: no cover
        return Participant.make_one(self.boto3_raw_data["participant"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParticipantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParticipantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicKeyResponse:
    boto3_raw_data: "type_defs.GetPublicKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def publicKey(self):  # pragma: no cover
        return PublicKey.make_one(self.boto3_raw_data["publicKey"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportPublicKeyResponse:
    boto3_raw_data: "type_defs.ImportPublicKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def publicKey(self):  # pragma: no cover
        return PublicKey.make_one(self.boto3_raw_data["publicKey"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportPublicKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportPublicKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStageSessionResponse:
    boto3_raw_data: "type_defs.GetStageSessionResponseTypeDef" = dataclasses.field()

    @cached_property
    def stageSession(self):  # pragma: no cover
        return StageSession.make_one(self.boto3_raw_data["stageSession"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStageSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStageSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIngestConfigurationsResponse:
    boto3_raw_data: "type_defs.ListIngestConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ingestConfigurations(self):  # pragma: no cover
        return IngestConfigurationSummary.make_many(
            self.boto3_raw_data["ingestConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIngestConfigurationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIngestConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayoutConfiguration:
    boto3_raw_data: "type_defs.LayoutConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def grid(self):  # pragma: no cover
        return GridConfiguration.make_one(self.boto3_raw_data["grid"])

    @cached_property
    def pip(self):  # pragma: no cover
        return PipConfiguration.make_one(self.boto3_raw_data["pip"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LayoutConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LayoutConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIngestConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListIngestConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    filterByStageArn = field("filterByStageArn")
    filterByState = field("filterByState")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIngestConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIngestConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListParticipantReplicasRequestPaginate:
    boto3_raw_data: "type_defs.ListParticipantReplicasRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sourceStageArn = field("sourceStageArn")
    participantId = field("participantId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListParticipantReplicasRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListParticipantReplicasRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublicKeysRequestPaginate:
    boto3_raw_data: "type_defs.ListPublicKeysRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPublicKeysRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublicKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListParticipantReplicasResponse:
    boto3_raw_data: "type_defs.ListParticipantReplicasResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def replicas(self):  # pragma: no cover
        return ParticipantReplica.make_many(self.boto3_raw_data["replicas"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListParticipantReplicasResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListParticipantReplicasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListParticipantsResponse:
    boto3_raw_data: "type_defs.ListParticipantsResponseTypeDef" = dataclasses.field()

    @cached_property
    def participants(self):  # pragma: no cover
        return ParticipantSummary.make_many(self.boto3_raw_data["participants"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListParticipantsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListParticipantsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublicKeysResponse:
    boto3_raw_data: "type_defs.ListPublicKeysResponseTypeDef" = dataclasses.field()

    @cached_property
    def publicKeys(self):  # pragma: no cover
        return PublicKeySummary.make_many(self.boto3_raw_data["publicKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPublicKeysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublicKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStageSessionsResponse:
    boto3_raw_data: "type_defs.ListStageSessionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def stageSessions(self):  # pragma: no cover
        return StageSessionSummary.make_many(self.boto3_raw_data["stageSessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStageSessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStageSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStagesResponse:
    boto3_raw_data: "type_defs.ListStagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def stages(self):  # pragma: no cover
        return StageSummary.make_many(self.boto3_raw_data["stages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stage:
    boto3_raw_data: "type_defs.StageTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    activeSessionId = field("activeSessionId")
    tags = field("tags")

    @cached_property
    def autoParticipantRecordingConfiguration(self):  # pragma: no cover
        return AutoParticipantRecordingConfigurationOutput.make_one(
            self.boto3_raw_data["autoParticipantRecordingConfiguration"]
        )

    @cached_property
    def endpoints(self):  # pragma: no cover
        return StageEndpoints.make_one(self.boto3_raw_data["endpoints"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationConfigurationOutput:
    boto3_raw_data: "type_defs.S3DestinationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    storageConfigurationArn = field("storageConfigurationArn")
    encoderConfigurationArns = field("encoderConfigurationArns")

    @cached_property
    def recordingConfiguration(self):  # pragma: no cover
        return RecordingConfiguration.make_one(
            self.boto3_raw_data["recordingConfiguration"]
        )

    @cached_property
    def thumbnailConfigurations(self):  # pragma: no cover
        return CompositionThumbnailConfigurationOutput.make_many(
            self.boto3_raw_data["thumbnailConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3DestinationConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCompositionsResponse:
    boto3_raw_data: "type_defs.ListCompositionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def compositions(self):  # pragma: no cover
        return CompositionSummary.make_many(self.boto3_raw_data["compositions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCompositionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCompositionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationConfiguration:
    boto3_raw_data: "type_defs.S3DestinationConfigurationTypeDef" = dataclasses.field()

    storageConfigurationArn = field("storageConfigurationArn")
    encoderConfigurationArns = field("encoderConfigurationArns")

    @cached_property
    def recordingConfiguration(self):  # pragma: no cover
        return RecordingConfiguration.make_one(
            self.boto3_raw_data["recordingConfiguration"]
        )

    thumbnailConfigurations = field("thumbnailConfigurations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEncoderConfigurationResponse:
    boto3_raw_data: "type_defs.CreateEncoderConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def encoderConfiguration(self):  # pragma: no cover
        return EncoderConfiguration.make_one(
            self.boto3_raw_data["encoderConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEncoderConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEncoderConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEncoderConfigurationResponse:
    boto3_raw_data: "type_defs.GetEncoderConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def encoderConfiguration(self):  # pragma: no cover
        return EncoderConfiguration.make_one(
            self.boto3_raw_data["encoderConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEncoderConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEncoderConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageConfigurationsResponse:
    boto3_raw_data: "type_defs.ListStorageConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def storageConfigurations(self):  # pragma: no cover
        return StorageConfigurationSummary.make_many(
            self.boto3_raw_data["storageConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStorageConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStorageConfigurationResponse:
    boto3_raw_data: "type_defs.CreateStorageConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def storageConfiguration(self):  # pragma: no cover
        return StorageConfiguration.make_one(
            self.boto3_raw_data["storageConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStorageConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStorageConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageConfigurationResponse:
    boto3_raw_data: "type_defs.GetStorageConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def storageConfiguration(self):  # pragma: no cover
        return StorageConfiguration.make_one(
            self.boto3_raw_data["storageConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetStorageConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStageResponse:
    boto3_raw_data: "type_defs.CreateStageResponseTypeDef" = dataclasses.field()

    @cached_property
    def stage(self):  # pragma: no cover
        return Stage.make_one(self.boto3_raw_data["stage"])

    @cached_property
    def participantTokens(self):  # pragma: no cover
        return ParticipantToken.make_many(self.boto3_raw_data["participantTokens"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStageResponse:
    boto3_raw_data: "type_defs.GetStageResponseTypeDef" = dataclasses.field()

    @cached_property
    def stage(self):  # pragma: no cover
        return Stage.make_one(self.boto3_raw_data["stage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStageResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStageResponse:
    boto3_raw_data: "type_defs.UpdateStageResponseTypeDef" = dataclasses.field()

    @cached_property
    def stage(self):  # pragma: no cover
        return Stage.make_one(self.boto3_raw_data["stage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStageRequest:
    boto3_raw_data: "type_defs.CreateStageRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def participantTokenConfigurations(self):  # pragma: no cover
        return ParticipantTokenConfiguration.make_many(
            self.boto3_raw_data["participantTokenConfigurations"]
        )

    tags = field("tags")
    autoParticipantRecordingConfiguration = field(
        "autoParticipantRecordingConfiguration"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStageRequest:
    boto3_raw_data: "type_defs.UpdateStageRequestTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    autoParticipantRecordingConfiguration = field(
        "autoParticipantRecordingConfiguration"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationConfigurationOutput:
    boto3_raw_data: "type_defs.DestinationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def channel(self):  # pragma: no cover
        return ChannelDestinationConfiguration.make_one(self.boto3_raw_data["channel"])

    @cached_property
    def s3(self):  # pragma: no cover
        return S3DestinationConfigurationOutput.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DestinationConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Destination:
    boto3_raw_data: "type_defs.DestinationTypeDef" = dataclasses.field()

    id = field("id")
    state = field("state")

    @cached_property
    def configuration(self):  # pragma: no cover
        return DestinationConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def detail(self):  # pragma: no cover
        return DestinationDetail.make_one(self.boto3_raw_data["detail"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationConfiguration:
    boto3_raw_data: "type_defs.DestinationConfigurationTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def channel(self):  # pragma: no cover
        return ChannelDestinationConfiguration.make_one(self.boto3_raw_data["channel"])

    s3 = field("s3")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Composition:
    boto3_raw_data: "type_defs.CompositionTypeDef" = dataclasses.field()

    arn = field("arn")
    stageArn = field("stageArn")
    state = field("state")

    @cached_property
    def layout(self):  # pragma: no cover
        return LayoutConfiguration.make_one(self.boto3_raw_data["layout"])

    @cached_property
    def destinations(self):  # pragma: no cover
        return Destination.make_many(self.boto3_raw_data["destinations"])

    tags = field("tags")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CompositionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CompositionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCompositionResponse:
    boto3_raw_data: "type_defs.GetCompositionResponseTypeDef" = dataclasses.field()

    @cached_property
    def composition(self):  # pragma: no cover
        return Composition.make_one(self.boto3_raw_data["composition"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCompositionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCompositionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCompositionResponse:
    boto3_raw_data: "type_defs.StartCompositionResponseTypeDef" = dataclasses.field()

    @cached_property
    def composition(self):  # pragma: no cover
        return Composition.make_one(self.boto3_raw_data["composition"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCompositionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCompositionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCompositionRequest:
    boto3_raw_data: "type_defs.StartCompositionRequestTypeDef" = dataclasses.field()

    stageArn = field("stageArn")
    destinations = field("destinations")
    idempotencyToken = field("idempotencyToken")

    @cached_property
    def layout(self):  # pragma: no cover
        return LayoutConfiguration.make_one(self.boto3_raw_data["layout"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCompositionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCompositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
