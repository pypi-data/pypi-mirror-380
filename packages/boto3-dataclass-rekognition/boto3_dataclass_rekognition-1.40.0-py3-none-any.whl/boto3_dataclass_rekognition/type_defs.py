# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rekognition import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AgeRange:
    boto3_raw_data: "type_defs.AgeRangeTypeDef" = dataclasses.field()

    Low = field("Low")
    High = field("High")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgeRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFacesRequest:
    boto3_raw_data: "type_defs.AssociateFacesRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    UserId = field("UserId")
    FaceIds = field("FaceIds")
    UserMatchThreshold = field("UserMatchThreshold")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateFacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedFace:
    boto3_raw_data: "type_defs.AssociatedFaceTypeDef" = dataclasses.field()

    FaceId = field("FaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssociatedFaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssociatedFaceTypeDef"]],
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
class UnsuccessfulFaceAssociation:
    boto3_raw_data: "type_defs.UnsuccessfulFaceAssociationTypeDef" = dataclasses.field()

    FaceId = field("FaceId")
    UserId = field("UserId")
    Confidence = field("Confidence")
    Reasons = field("Reasons")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnsuccessfulFaceAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnsuccessfulFaceAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioMetadata:
    boto3_raw_data: "type_defs.AudioMetadataTypeDef" = dataclasses.field()

    Codec = field("Codec")
    DurationMillis = field("DurationMillis")
    SampleRate = field("SampleRate")
    NumberOfChannels = field("NumberOfChannels")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudioMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BoundingBox:
    boto3_raw_data: "type_defs.BoundingBoxTypeDef" = dataclasses.field()

    Width = field("Width")
    Height = field("Height")
    Left = field("Left")
    Top = field("Top")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BoundingBoxTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BoundingBoxTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Object:
    boto3_raw_data: "type_defs.S3ObjectTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Beard:
    boto3_raw_data: "type_defs.BeardTypeDef" = dataclasses.field()

    Value = field("Value")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BeardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BeardTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlackFrame:
    boto3_raw_data: "type_defs.BlackFrameTypeDef" = dataclasses.field()

    MaxPixelThreshold = field("MaxPixelThreshold")
    MinCoveragePercentage = field("MinCoveragePercentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlackFrameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlackFrameTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnownGender:
    boto3_raw_data: "type_defs.KnownGenderTypeDef" = dataclasses.field()

    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KnownGenderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KnownGenderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Versions:
    boto3_raw_data: "type_defs.VersionsTypeDef" = dataclasses.field()

    Minimum = field("Minimum")
    Maximum = field("Maximum")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VersionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VersionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Challenge:
    boto3_raw_data: "type_defs.ChallengeTypeDef" = dataclasses.field()

    Type = field("Type")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChallengeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChallengeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Emotion:
    boto3_raw_data: "type_defs.EmotionTypeDef" = dataclasses.field()

    Type = field("Type")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmotionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmotionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageQuality:
    boto3_raw_data: "type_defs.ImageQualityTypeDef" = dataclasses.field()

    Brightness = field("Brightness")
    Sharpness = field("Sharpness")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageQualityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageQualityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Landmark:
    boto3_raw_data: "type_defs.LandmarkTypeDef" = dataclasses.field()

    Type = field("Type")
    X = field("X")
    Y = field("Y")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LandmarkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LandmarkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Pose:
    boto3_raw_data: "type_defs.PoseTypeDef" = dataclasses.field()

    Roll = field("Roll")
    Yaw = field("Yaw")
    Pitch = field("Pitch")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PoseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PoseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Smile:
    boto3_raw_data: "type_defs.SmileTypeDef" = dataclasses.field()

    Value = field("Value")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SmileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SmileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectedHomeSettingsForUpdate:
    boto3_raw_data: "type_defs.ConnectedHomeSettingsForUpdateTypeDef" = (
        dataclasses.field()
    )

    Labels = field("Labels")
    MinConfidence = field("MinConfidence")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConnectedHomeSettingsForUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectedHomeSettingsForUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectedHomeSettingsOutput:
    boto3_raw_data: "type_defs.ConnectedHomeSettingsOutputTypeDef" = dataclasses.field()

    Labels = field("Labels")
    MinConfidence = field("MinConfidence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectedHomeSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectedHomeSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectedHomeSettings:
    boto3_raw_data: "type_defs.ConnectedHomeSettingsTypeDef" = dataclasses.field()

    Labels = field("Labels")
    MinConfidence = field("MinConfidence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectedHomeSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectedHomeSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentType:
    boto3_raw_data: "type_defs.ContentTypeTypeDef" = dataclasses.field()

    Confidence = field("Confidence")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContentTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModerationLabel:
    boto3_raw_data: "type_defs.ModerationLabelTypeDef" = dataclasses.field()

    Confidence = field("Confidence")
    Name = field("Name")
    ParentName = field("ParentName")
    TaxonomyLevel = field("TaxonomyLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModerationLabelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModerationLabelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputConfig:
    boto3_raw_data: "type_defs.OutputConfigTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3KeyPrefix = field("S3KeyPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoversBodyPart:
    boto3_raw_data: "type_defs.CoversBodyPartTypeDef" = dataclasses.field()

    Confidence = field("Confidence")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoversBodyPartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoversBodyPartTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCollectionRequest:
    boto3_raw_data: "type_defs.CreateCollectionRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LivenessOutputConfig:
    boto3_raw_data: "type_defs.LivenessOutputConfigTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3KeyPrefix = field("S3KeyPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LivenessOutputConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LivenessOutputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectRequest:
    boto3_raw_data: "type_defs.CreateProjectRequestTypeDef" = dataclasses.field()

    ProjectName = field("ProjectName")
    Feature = field("Feature")
    AutoUpdate = field("AutoUpdate")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamProcessorDataSharingPreference:
    boto3_raw_data: "type_defs.StreamProcessorDataSharingPreferenceTypeDef" = (
        dataclasses.field()
    )

    OptIn = field("OptIn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StreamProcessorDataSharingPreferenceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamProcessorDataSharingPreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamProcessorNotificationChannel:
    boto3_raw_data: "type_defs.StreamProcessorNotificationChannelTypeDef" = (
        dataclasses.field()
    )

    SNSTopicArn = field("SNSTopicArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StreamProcessorNotificationChannelTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamProcessorNotificationChannelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserRequest:
    boto3_raw_data: "type_defs.CreateUserRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    UserId = field("UserId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizationFeatureContentModerationConfig:
    boto3_raw_data: "type_defs.CustomizationFeatureContentModerationConfigTypeDef" = (
        dataclasses.field()
    )

    ConfidenceThreshold = field("ConfidenceThreshold")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomizationFeatureContentModerationConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizationFeatureContentModerationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetStats:
    boto3_raw_data: "type_defs.DatasetStatsTypeDef" = dataclasses.field()

    LabeledEntries = field("LabeledEntries")
    TotalEntries = field("TotalEntries")
    TotalLabels = field("TotalLabels")
    ErrorEntries = field("ErrorEntries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetStatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetStatsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetLabelStats:
    boto3_raw_data: "type_defs.DatasetLabelStatsTypeDef" = dataclasses.field()

    EntryCount = field("EntryCount")
    BoundingBoxCount = field("BoundingBoxCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetLabelStatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetLabelStatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetMetadata:
    boto3_raw_data: "type_defs.DatasetMetadataTypeDef" = dataclasses.field()

    CreationTimestamp = field("CreationTimestamp")
    DatasetType = field("DatasetType")
    DatasetArn = field("DatasetArn")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    StatusMessageCode = field("StatusMessageCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCollectionRequest:
    boto3_raw_data: "type_defs.DeleteCollectionRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetRequest:
    boto3_raw_data: "type_defs.DeleteDatasetRequestTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFacesRequest:
    boto3_raw_data: "type_defs.DeleteFacesRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    FaceIds = field("FaceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnsuccessfulFaceDeletion:
    boto3_raw_data: "type_defs.UnsuccessfulFaceDeletionTypeDef" = dataclasses.field()

    FaceId = field("FaceId")
    UserId = field("UserId")
    Reasons = field("Reasons")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnsuccessfulFaceDeletionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnsuccessfulFaceDeletionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectPolicyRequest:
    boto3_raw_data: "type_defs.DeleteProjectPolicyRequestTypeDef" = dataclasses.field()

    ProjectArn = field("ProjectArn")
    PolicyName = field("PolicyName")
    PolicyRevisionId = field("PolicyRevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectRequest:
    boto3_raw_data: "type_defs.DeleteProjectRequestTypeDef" = dataclasses.field()

    ProjectArn = field("ProjectArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectVersionRequest:
    boto3_raw_data: "type_defs.DeleteProjectVersionRequestTypeDef" = dataclasses.field()

    ProjectVersionArn = field("ProjectVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStreamProcessorRequest:
    boto3_raw_data: "type_defs.DeleteStreamProcessorRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStreamProcessorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStreamProcessorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserRequest:
    boto3_raw_data: "type_defs.DeleteUserRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    UserId = field("UserId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCollectionRequest:
    boto3_raw_data: "type_defs.DescribeCollectionRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetRequest:
    boto3_raw_data: "type_defs.DescribeDatasetRequestTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetRequestTypeDef"]
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
class DescribeProjectVersionsRequest:
    boto3_raw_data: "type_defs.DescribeProjectVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    ProjectArn = field("ProjectArn")
    VersionNames = field("VersionNames")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeProjectVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProjectsRequest:
    boto3_raw_data: "type_defs.DescribeProjectsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ProjectNames = field("ProjectNames")
    Features = field("Features")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProjectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamProcessorRequest:
    boto3_raw_data: "type_defs.DescribeStreamProcessorRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStreamProcessorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamProcessorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectLabelsImageQuality:
    boto3_raw_data: "type_defs.DetectLabelsImageQualityTypeDef" = dataclasses.field()

    Brightness = field("Brightness")
    Sharpness = field("Sharpness")
    Contrast = field("Contrast")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectLabelsImageQualityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectLabelsImageQualityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DominantColor:
    boto3_raw_data: "type_defs.DominantColorTypeDef" = dataclasses.field()

    Red = field("Red")
    Blue = field("Blue")
    Green = field("Green")
    HexCode = field("HexCode")
    CSSColor = field("CSSColor")
    SimplifiedColor = field("SimplifiedColor")
    PixelPercent = field("PixelPercent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DominantColorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DominantColorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectLabelsImagePropertiesSettings:
    boto3_raw_data: "type_defs.DetectLabelsImagePropertiesSettingsTypeDef" = (
        dataclasses.field()
    )

    MaxDominantColors = field("MaxDominantColors")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetectLabelsImagePropertiesSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectLabelsImagePropertiesSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneralLabelsSettings:
    boto3_raw_data: "type_defs.GeneralLabelsSettingsTypeDef" = dataclasses.field()

    LabelInclusionFilters = field("LabelInclusionFilters")
    LabelExclusionFilters = field("LabelExclusionFilters")
    LabelCategoryInclusionFilters = field("LabelCategoryInclusionFilters")
    LabelCategoryExclusionFilters = field("LabelCategoryExclusionFilters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeneralLabelsSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeneralLabelsSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HumanLoopActivationOutput:
    boto3_raw_data: "type_defs.HumanLoopActivationOutputTypeDef" = dataclasses.field()

    HumanLoopArn = field("HumanLoopArn")
    HumanLoopActivationReasons = field("HumanLoopActivationReasons")
    HumanLoopActivationConditionsEvaluationResults = field(
        "HumanLoopActivationConditionsEvaluationResults"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HumanLoopActivationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HumanLoopActivationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectiveEquipmentSummarizationAttributes:
    boto3_raw_data: "type_defs.ProtectiveEquipmentSummarizationAttributesTypeDef" = (
        dataclasses.field()
    )

    MinConfidence = field("MinConfidence")
    RequiredEquipmentTypes = field("RequiredEquipmentTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectiveEquipmentSummarizationAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectiveEquipmentSummarizationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectiveEquipmentSummary:
    boto3_raw_data: "type_defs.ProtectiveEquipmentSummaryTypeDef" = dataclasses.field()

    PersonsWithRequiredEquipment = field("PersonsWithRequiredEquipment")
    PersonsWithoutRequiredEquipment = field("PersonsWithoutRequiredEquipment")
    PersonsIndeterminate = field("PersonsIndeterminate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectiveEquipmentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectiveEquipmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectionFilter:
    boto3_raw_data: "type_defs.DetectionFilterTypeDef" = dataclasses.field()

    MinConfidence = field("MinConfidence")
    MinBoundingBoxHeight = field("MinBoundingBoxHeight")
    MinBoundingBoxWidth = field("MinBoundingBoxWidth")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectionFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetectionFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFacesRequest:
    boto3_raw_data: "type_defs.DisassociateFacesRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    UserId = field("UserId")
    FaceIds = field("FaceIds")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateFacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatedFace:
    boto3_raw_data: "type_defs.DisassociatedFaceTypeDef" = dataclasses.field()

    FaceId = field("FaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DisassociatedFaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociatedFaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnsuccessfulFaceDisassociation:
    boto3_raw_data: "type_defs.UnsuccessfulFaceDisassociationTypeDef" = (
        dataclasses.field()
    )

    FaceId = field("FaceId")
    UserId = field("UserId")
    Reasons = field("Reasons")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UnsuccessfulFaceDisassociationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnsuccessfulFaceDisassociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributeDataset:
    boto3_raw_data: "type_defs.DistributeDatasetTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DistributeDatasetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributeDatasetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EyeDirection:
    boto3_raw_data: "type_defs.EyeDirectionTypeDef" = dataclasses.field()

    Yaw = field("Yaw")
    Pitch = field("Pitch")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EyeDirectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EyeDirectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EyeOpen:
    boto3_raw_data: "type_defs.EyeOpenTypeDef" = dataclasses.field()

    Value = field("Value")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EyeOpenTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EyeOpenTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Eyeglasses:
    boto3_raw_data: "type_defs.EyeglassesTypeDef" = dataclasses.field()

    Value = field("Value")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EyeglassesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EyeglassesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaceOccluded:
    boto3_raw_data: "type_defs.FaceOccludedTypeDef" = dataclasses.field()

    Value = field("Value")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FaceOccludedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FaceOccludedTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Gender:
    boto3_raw_data: "type_defs.GenderTypeDef" = dataclasses.field()

    Value = field("Value")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GenderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GenderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MouthOpen:
    boto3_raw_data: "type_defs.MouthOpenTypeDef" = dataclasses.field()

    Value = field("Value")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MouthOpenTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MouthOpenTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Mustache:
    boto3_raw_data: "type_defs.MustacheTypeDef" = dataclasses.field()

    Value = field("Value")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MustacheTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MustacheTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sunglasses:
    boto3_raw_data: "type_defs.SunglassesTypeDef" = dataclasses.field()

    Value = field("Value")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SunglassesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SunglassesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaceSearchSettings:
    boto3_raw_data: "type_defs.FaceSearchSettingsTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    FaceMatchThreshold = field("FaceMatchThreshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FaceSearchSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FaceSearchSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Point:
    boto3_raw_data: "type_defs.PointTypeDef" = dataclasses.field()

    X = field("X")
    Y = field("Y")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCelebrityInfoRequest:
    boto3_raw_data: "type_defs.GetCelebrityInfoRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCelebrityInfoRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCelebrityInfoRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCelebrityRecognitionRequest:
    boto3_raw_data: "type_defs.GetCelebrityRecognitionRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SortBy = field("SortBy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCelebrityRecognitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCelebrityRecognitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoMetadata:
    boto3_raw_data: "type_defs.VideoMetadataTypeDef" = dataclasses.field()

    Codec = field("Codec")
    DurationMillis = field("DurationMillis")
    Format = field("Format")
    FrameRate = field("FrameRate")
    FrameHeight = field("FrameHeight")
    FrameWidth = field("FrameWidth")
    ColorRange = field("ColorRange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContentModerationRequestMetadata:
    boto3_raw_data: "type_defs.GetContentModerationRequestMetadataTypeDef" = (
        dataclasses.field()
    )

    SortBy = field("SortBy")
    AggregateBy = field("AggregateBy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContentModerationRequestMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContentModerationRequestMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContentModerationRequest:
    boto3_raw_data: "type_defs.GetContentModerationRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SortBy = field("SortBy")
    AggregateBy = field("AggregateBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContentModerationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContentModerationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFaceDetectionRequest:
    boto3_raw_data: "type_defs.GetFaceDetectionRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFaceDetectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFaceDetectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFaceLivenessSessionResultsRequest:
    boto3_raw_data: "type_defs.GetFaceLivenessSessionResultsRequestTypeDef" = (
        dataclasses.field()
    )

    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFaceLivenessSessionResultsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFaceLivenessSessionResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFaceSearchRequest:
    boto3_raw_data: "type_defs.GetFaceSearchRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SortBy = field("SortBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFaceSearchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFaceSearchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLabelDetectionRequestMetadata:
    boto3_raw_data: "type_defs.GetLabelDetectionRequestMetadataTypeDef" = (
        dataclasses.field()
    )

    SortBy = field("SortBy")
    AggregateBy = field("AggregateBy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLabelDetectionRequestMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLabelDetectionRequestMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLabelDetectionRequest:
    boto3_raw_data: "type_defs.GetLabelDetectionRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SortBy = field("SortBy")
    AggregateBy = field("AggregateBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLabelDetectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLabelDetectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaAnalysisJobRequest:
    boto3_raw_data: "type_defs.GetMediaAnalysisJobRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMediaAnalysisJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaAnalysisJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaAnalysisJobFailureDetails:
    boto3_raw_data: "type_defs.MediaAnalysisJobFailureDetailsTypeDef" = (
        dataclasses.field()
    )

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MediaAnalysisJobFailureDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaAnalysisJobFailureDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaAnalysisOutputConfig:
    boto3_raw_data: "type_defs.MediaAnalysisOutputConfigTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3KeyPrefix = field("S3KeyPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaAnalysisOutputConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaAnalysisOutputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPersonTrackingRequest:
    boto3_raw_data: "type_defs.GetPersonTrackingRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SortBy = field("SortBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPersonTrackingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPersonTrackingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentDetectionRequest:
    boto3_raw_data: "type_defs.GetSegmentDetectionRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentDetectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentDetectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentTypeInfo:
    boto3_raw_data: "type_defs.SegmentTypeInfoTypeDef" = dataclasses.field()

    Type = field("Type")
    ModelVersion = field("ModelVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentTypeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SegmentTypeInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTextDetectionRequest:
    boto3_raw_data: "type_defs.GetTextDetectionRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTextDetectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTextDetectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HumanLoopDataAttributes:
    boto3_raw_data: "type_defs.HumanLoopDataAttributesTypeDef" = dataclasses.field()

    ContentClassifiers = field("ContentClassifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HumanLoopDataAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HumanLoopDataAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisDataStream:
    boto3_raw_data: "type_defs.KinesisDataStreamTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KinesisDataStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisDataStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamStartSelector:
    boto3_raw_data: "type_defs.KinesisVideoStreamStartSelectorTypeDef" = (
        dataclasses.field()
    )

    ProducerTimestamp = field("ProducerTimestamp")
    FragmentNumber = field("FragmentNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisVideoStreamStartSelectorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisVideoStreamStartSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStream:
    boto3_raw_data: "type_defs.KinesisVideoStreamTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisVideoStreamTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisVideoStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelAlias:
    boto3_raw_data: "type_defs.LabelAliasTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelAliasTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LabelAliasTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelCategory:
    boto3_raw_data: "type_defs.LabelCategoryTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelCategoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LabelCategoryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Parent:
    boto3_raw_data: "type_defs.ParentTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollectionsRequest:
    boto3_raw_data: "type_defs.ListCollectionsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCollectionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetEntriesRequest:
    boto3_raw_data: "type_defs.ListDatasetEntriesRequestTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")
    ContainsLabels = field("ContainsLabels")
    Labeled = field("Labeled")
    SourceRefContains = field("SourceRefContains")
    HasErrors = field("HasErrors")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetEntriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetEntriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetLabelsRequest:
    boto3_raw_data: "type_defs.ListDatasetLabelsRequestTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetLabelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetLabelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFacesRequest:
    boto3_raw_data: "type_defs.ListFacesRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    UserId = field("UserId")
    FaceIds = field("FaceIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFacesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMediaAnalysisJobsRequest:
    boto3_raw_data: "type_defs.ListMediaAnalysisJobsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMediaAnalysisJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMediaAnalysisJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectPoliciesRequest:
    boto3_raw_data: "type_defs.ListProjectPoliciesRequestTypeDef" = dataclasses.field()

    ProjectArn = field("ProjectArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectPolicy:
    boto3_raw_data: "type_defs.ProjectPolicyTypeDef" = dataclasses.field()

    ProjectArn = field("ProjectArn")
    PolicyName = field("PolicyName")
    PolicyRevisionId = field("PolicyRevisionId")
    PolicyDocument = field("PolicyDocument")
    CreationTimestamp = field("CreationTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamProcessorsRequest:
    boto3_raw_data: "type_defs.ListStreamProcessorsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStreamProcessorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamProcessorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamProcessor:
    boto3_raw_data: "type_defs.StreamProcessorTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamProcessorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamProcessorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

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
class ListUsersRequest:
    boto3_raw_data: "type_defs.ListUsersRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    UserId = field("UserId")
    UserStatus = field("UserStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchedUser:
    boto3_raw_data: "type_defs.MatchedUserTypeDef" = dataclasses.field()

    UserId = field("UserId")
    UserStatus = field("UserStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchedUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchedUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaAnalysisDetectModerationLabelsConfig:
    boto3_raw_data: "type_defs.MediaAnalysisDetectModerationLabelsConfigTypeDef" = (
        dataclasses.field()
    )

    MinConfidence = field("MinConfidence")
    ProjectVersion = field("ProjectVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaAnalysisDetectModerationLabelsConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaAnalysisDetectModerationLabelsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaAnalysisModelVersions:
    boto3_raw_data: "type_defs.MediaAnalysisModelVersionsTypeDef" = dataclasses.field()

    Moderation = field("Moderation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaAnalysisModelVersionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaAnalysisModelVersionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationChannel:
    boto3_raw_data: "type_defs.NotificationChannelTypeDef" = dataclasses.field()

    SNSTopicArn = field("SNSTopicArn")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationChannelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationChannelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProjectPolicyRequest:
    boto3_raw_data: "type_defs.PutProjectPolicyRequestTypeDef" = dataclasses.field()

    ProjectArn = field("ProjectArn")
    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")
    PolicyRevisionId = field("PolicyRevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProjectPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProjectPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Destination:
    boto3_raw_data: "type_defs.S3DestinationTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    KeyPrefix = field("KeyPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchFacesRequest:
    boto3_raw_data: "type_defs.SearchFacesRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    FaceId = field("FaceId")
    MaxFaces = field("MaxFaces")
    FaceMatchThreshold = field("FaceMatchThreshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchFacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchFacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUsersRequest:
    boto3_raw_data: "type_defs.SearchUsersRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    UserId = field("UserId")
    FaceId = field("FaceId")
    UserMatchThreshold = field("UserMatchThreshold")
    MaxUsers = field("MaxUsers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUsersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchedFace:
    boto3_raw_data: "type_defs.SearchedFaceTypeDef" = dataclasses.field()

    FaceId = field("FaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchedFaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchedFaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchedUser:
    boto3_raw_data: "type_defs.SearchedUserTypeDef" = dataclasses.field()

    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchedUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchedUserTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShotSegment:
    boto3_raw_data: "type_defs.ShotSegmentTypeDef" = dataclasses.field()

    Index = field("Index")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShotSegmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShotSegmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TechnicalCueSegment:
    boto3_raw_data: "type_defs.TechnicalCueSegmentTypeDef" = dataclasses.field()

    Type = field("Type")
    Confidence = field("Confidence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TechnicalCueSegmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TechnicalCueSegmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartProjectVersionRequest:
    boto3_raw_data: "type_defs.StartProjectVersionRequestTypeDef" = dataclasses.field()

    ProjectVersionArn = field("ProjectVersionArn")
    MinInferenceUnits = field("MinInferenceUnits")
    MaxInferenceUnits = field("MaxInferenceUnits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartProjectVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartProjectVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartShotDetectionFilter:
    boto3_raw_data: "type_defs.StartShotDetectionFilterTypeDef" = dataclasses.field()

    MinSegmentConfidence = field("MinSegmentConfidence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartShotDetectionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartShotDetectionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamProcessingStopSelector:
    boto3_raw_data: "type_defs.StreamProcessingStopSelectorTypeDef" = (
        dataclasses.field()
    )

    MaxDurationInSeconds = field("MaxDurationInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamProcessingStopSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamProcessingStopSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopProjectVersionRequest:
    boto3_raw_data: "type_defs.StopProjectVersionRequestTypeDef" = dataclasses.field()

    ProjectVersionArn = field("ProjectVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopProjectVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopProjectVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopStreamProcessorRequest:
    boto3_raw_data: "type_defs.StopStreamProcessorRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopStreamProcessorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopStreamProcessorRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class CopyProjectVersionResponse:
    boto3_raw_data: "type_defs.CopyProjectVersionResponseTypeDef" = dataclasses.field()

    ProjectVersionArn = field("ProjectVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyProjectVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyProjectVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCollectionResponse:
    boto3_raw_data: "type_defs.CreateCollectionResponseTypeDef" = dataclasses.field()

    StatusCode = field("StatusCode")
    CollectionArn = field("CollectionArn")
    FaceModelVersion = field("FaceModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCollectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetResponse:
    boto3_raw_data: "type_defs.CreateDatasetResponseTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFaceLivenessSessionResponse:
    boto3_raw_data: "type_defs.CreateFaceLivenessSessionResponseTypeDef" = (
        dataclasses.field()
    )

    SessionId = field("SessionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFaceLivenessSessionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFaceLivenessSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectResponse:
    boto3_raw_data: "type_defs.CreateProjectResponseTypeDef" = dataclasses.field()

    ProjectArn = field("ProjectArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectVersionResponse:
    boto3_raw_data: "type_defs.CreateProjectVersionResponseTypeDef" = (
        dataclasses.field()
    )

    ProjectVersionArn = field("ProjectVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamProcessorResponse:
    boto3_raw_data: "type_defs.CreateStreamProcessorResponseTypeDef" = (
        dataclasses.field()
    )

    StreamProcessorArn = field("StreamProcessorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateStreamProcessorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamProcessorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCollectionResponse:
    boto3_raw_data: "type_defs.DeleteCollectionResponseTypeDef" = dataclasses.field()

    StatusCode = field("StatusCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCollectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectResponse:
    boto3_raw_data: "type_defs.DeleteProjectResponseTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectVersionResponse:
    boto3_raw_data: "type_defs.DeleteProjectVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCollectionResponse:
    boto3_raw_data: "type_defs.DescribeCollectionResponseTypeDef" = dataclasses.field()

    FaceCount = field("FaceCount")
    FaceModelVersion = field("FaceModelVersion")
    CollectionARN = field("CollectionARN")
    CreationTimestamp = field("CreationTimestamp")
    UserCount = field("UserCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCollectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollectionsResponse:
    boto3_raw_data: "type_defs.ListCollectionsResponseTypeDef" = dataclasses.field()

    CollectionIds = field("CollectionIds")
    FaceModelVersions = field("FaceModelVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCollectionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetEntriesResponse:
    boto3_raw_data: "type_defs.ListDatasetEntriesResponseTypeDef" = dataclasses.field()

    DatasetEntries = field("DatasetEntries")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetEntriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetEntriesResponseTypeDef"]
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

    Tags = field("Tags")

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
class PutProjectPolicyResponse:
    boto3_raw_data: "type_defs.PutProjectPolicyResponseTypeDef" = dataclasses.field()

    PolicyRevisionId = field("PolicyRevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProjectPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProjectPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCelebrityRecognitionResponse:
    boto3_raw_data: "type_defs.StartCelebrityRecognitionResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartCelebrityRecognitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCelebrityRecognitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartContentModerationResponse:
    boto3_raw_data: "type_defs.StartContentModerationResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartContentModerationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartContentModerationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFaceDetectionResponse:
    boto3_raw_data: "type_defs.StartFaceDetectionResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFaceDetectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFaceDetectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFaceSearchResponse:
    boto3_raw_data: "type_defs.StartFaceSearchResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFaceSearchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFaceSearchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLabelDetectionResponse:
    boto3_raw_data: "type_defs.StartLabelDetectionResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLabelDetectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLabelDetectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMediaAnalysisJobResponse:
    boto3_raw_data: "type_defs.StartMediaAnalysisJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMediaAnalysisJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMediaAnalysisJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPersonTrackingResponse:
    boto3_raw_data: "type_defs.StartPersonTrackingResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPersonTrackingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPersonTrackingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartProjectVersionResponse:
    boto3_raw_data: "type_defs.StartProjectVersionResponseTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartProjectVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartProjectVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSegmentDetectionResponse:
    boto3_raw_data: "type_defs.StartSegmentDetectionResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSegmentDetectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSegmentDetectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartStreamProcessorResponse:
    boto3_raw_data: "type_defs.StartStreamProcessorResponseTypeDef" = (
        dataclasses.field()
    )

    SessionId = field("SessionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartStreamProcessorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartStreamProcessorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTextDetectionResponse:
    boto3_raw_data: "type_defs.StartTextDetectionResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTextDetectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTextDetectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopProjectVersionResponse:
    boto3_raw_data: "type_defs.StopProjectVersionResponseTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopProjectVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopProjectVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFacesResponse:
    boto3_raw_data: "type_defs.AssociateFacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def AssociatedFaces(self):  # pragma: no cover
        return AssociatedFace.make_many(self.boto3_raw_data["AssociatedFaces"])

    @cached_property
    def UnsuccessfulFaceAssociations(self):  # pragma: no cover
        return UnsuccessfulFaceAssociation.make_many(
            self.boto3_raw_data["UnsuccessfulFaceAssociations"]
        )

    UserStatus = field("UserStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateFacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComparedSourceImageFace:
    boto3_raw_data: "type_defs.ComparedSourceImageFaceTypeDef" = dataclasses.field()

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    Confidence = field("Confidence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComparedSourceImageFaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComparedSourceImageFaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Face:
    boto3_raw_data: "type_defs.FaceTypeDef" = dataclasses.field()

    FaceId = field("FaceId")

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    ImageId = field("ImageId")
    ExternalImageId = field("ExternalImageId")
    Confidence = field("Confidence")
    IndexFacesModelVersion = field("IndexFacesModelVersion")
    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FaceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditImage:
    boto3_raw_data: "type_defs.AuditImageTypeDef" = dataclasses.field()

    Bytes = field("Bytes")

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuditImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuditImageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroundTruthManifest:
    boto3_raw_data: "type_defs.GroundTruthManifestTypeDef" = dataclasses.field()

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GroundTruthManifestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroundTruthManifestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaAnalysisInput:
    boto3_raw_data: "type_defs.MediaAnalysisInputTypeDef" = dataclasses.field()

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaAnalysisInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaAnalysisInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaAnalysisManifestSummary:
    boto3_raw_data: "type_defs.MediaAnalysisManifestSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaAnalysisManifestSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaAnalysisManifestSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Summary:
    boto3_raw_data: "type_defs.SummaryTypeDef" = dataclasses.field()

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Video:
    boto3_raw_data: "type_defs.VideoTypeDef" = dataclasses.field()

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

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
class StartTechnicalCueDetectionFilter:
    boto3_raw_data: "type_defs.StartTechnicalCueDetectionFilterTypeDef" = (
        dataclasses.field()
    )

    MinSegmentConfidence = field("MinSegmentConfidence")

    @cached_property
    def BlackFrame(self):  # pragma: no cover
        return BlackFrame.make_one(self.boto3_raw_data["BlackFrame"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartTechnicalCueDetectionFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTechnicalCueDetectionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetChanges:
    boto3_raw_data: "type_defs.DatasetChangesTypeDef" = dataclasses.field()

    GroundTruth = field("GroundTruth")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetChangesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetChangesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Image:
    boto3_raw_data: "type_defs.ImageTypeDef" = dataclasses.field()

    Bytes = field("Bytes")

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCelebrityInfoResponse:
    boto3_raw_data: "type_defs.GetCelebrityInfoResponseTypeDef" = dataclasses.field()

    Urls = field("Urls")
    Name = field("Name")

    @cached_property
    def KnownGender(self):  # pragma: no cover
        return KnownGender.make_one(self.boto3_raw_data["KnownGender"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCelebrityInfoResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCelebrityInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChallengePreference:
    boto3_raw_data: "type_defs.ChallengePreferenceTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Versions(self):  # pragma: no cover
        return Versions.make_one(self.boto3_raw_data["Versions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChallengePreferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChallengePreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComparedFace:
    boto3_raw_data: "type_defs.ComparedFaceTypeDef" = dataclasses.field()

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    Confidence = field("Confidence")

    @cached_property
    def Landmarks(self):  # pragma: no cover
        return Landmark.make_many(self.boto3_raw_data["Landmarks"])

    @cached_property
    def Pose(self):  # pragma: no cover
        return Pose.make_one(self.boto3_raw_data["Pose"])

    @cached_property
    def Quality(self):  # pragma: no cover
        return ImageQuality.make_one(self.boto3_raw_data["Quality"])

    @cached_property
    def Emotions(self):  # pragma: no cover
        return Emotion.make_many(self.boto3_raw_data["Emotions"])

    @cached_property
    def Smile(self):  # pragma: no cover
        return Smile.make_one(self.boto3_raw_data["Smile"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComparedFaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComparedFaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamProcessorSettingsForUpdate:
    boto3_raw_data: "type_defs.StreamProcessorSettingsForUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConnectedHomeForUpdate(self):  # pragma: no cover
        return ConnectedHomeSettingsForUpdate.make_one(
            self.boto3_raw_data["ConnectedHomeForUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StreamProcessorSettingsForUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamProcessorSettingsForUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentModerationDetection:
    boto3_raw_data: "type_defs.ContentModerationDetectionTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")

    @cached_property
    def ModerationLabel(self):  # pragma: no cover
        return ModerationLabel.make_one(self.boto3_raw_data["ModerationLabel"])

    StartTimestampMillis = field("StartTimestampMillis")
    EndTimestampMillis = field("EndTimestampMillis")
    DurationMillis = field("DurationMillis")

    @cached_property
    def ContentTypes(self):  # pragma: no cover
        return ContentType.make_many(self.boto3_raw_data["ContentTypes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentModerationDetectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentModerationDetectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyProjectVersionRequest:
    boto3_raw_data: "type_defs.CopyProjectVersionRequestTypeDef" = dataclasses.field()

    SourceProjectArn = field("SourceProjectArn")
    SourceProjectVersionArn = field("SourceProjectVersionArn")
    DestinationProjectArn = field("DestinationProjectArn")
    VersionName = field("VersionName")

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    Tags = field("Tags")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyProjectVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyProjectVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EquipmentDetection:
    boto3_raw_data: "type_defs.EquipmentDetectionTypeDef" = dataclasses.field()

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    Confidence = field("Confidence")
    Type = field("Type")

    @cached_property
    def CoversBodyPart(self):  # pragma: no cover
        return CoversBodyPart.make_one(self.boto3_raw_data["CoversBodyPart"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EquipmentDetectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EquipmentDetectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizationFeatureConfig:
    boto3_raw_data: "type_defs.CustomizationFeatureConfigTypeDef" = dataclasses.field()

    @cached_property
    def ContentModeration(self):  # pragma: no cover
        return CustomizationFeatureContentModerationConfig.make_one(
            self.boto3_raw_data["ContentModeration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomizationFeatureConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizationFeatureConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetDescription:
    boto3_raw_data: "type_defs.DatasetDescriptionTypeDef" = dataclasses.field()

    CreationTimestamp = field("CreationTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    StatusMessageCode = field("StatusMessageCode")

    @cached_property
    def DatasetStats(self):  # pragma: no cover
        return DatasetStats.make_one(self.boto3_raw_data["DatasetStats"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetLabelDescription:
    boto3_raw_data: "type_defs.DatasetLabelDescriptionTypeDef" = dataclasses.field()

    LabelName = field("LabelName")

    @cached_property
    def LabelStats(self):  # pragma: no cover
        return DatasetLabelStats.make_one(self.boto3_raw_data["LabelStats"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetLabelDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetLabelDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectDescription:
    boto3_raw_data: "type_defs.ProjectDescriptionTypeDef" = dataclasses.field()

    ProjectArn = field("ProjectArn")
    CreationTimestamp = field("CreationTimestamp")
    Status = field("Status")

    @cached_property
    def Datasets(self):  # pragma: no cover
        return DatasetMetadata.make_many(self.boto3_raw_data["Datasets"])

    Feature = field("Feature")
    AutoUpdate = field("AutoUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFacesResponse:
    boto3_raw_data: "type_defs.DeleteFacesResponseTypeDef" = dataclasses.field()

    DeletedFaces = field("DeletedFaces")

    @cached_property
    def UnsuccessfulFaceDeletions(self):  # pragma: no cover
        return UnsuccessfulFaceDeletion.make_many(
            self.boto3_raw_data["UnsuccessfulFaceDeletions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProjectVersionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeProjectVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ProjectArn = field("ProjectArn")
    VersionNames = field("VersionNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProjectVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProjectsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeProjectsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ProjectNames = field("ProjectNames")
    Features = field("Features")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeProjectsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollectionsRequestPaginate:
    boto3_raw_data: "type_defs.ListCollectionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCollectionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollectionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetEntriesRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetEntriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DatasetArn = field("DatasetArn")
    ContainsLabels = field("ContainsLabels")
    Labeled = field("Labeled")
    SourceRefContains = field("SourceRefContains")
    HasErrors = field("HasErrors")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDatasetEntriesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetEntriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetLabelsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetLabelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DatasetArn = field("DatasetArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDatasetLabelsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetLabelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFacesRequestPaginate:
    boto3_raw_data: "type_defs.ListFacesRequestPaginateTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    UserId = field("UserId")
    FaceIds = field("FaceIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFacesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFacesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListProjectPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ProjectArn = field("ProjectArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProjectPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamProcessorsRequestPaginate:
    boto3_raw_data: "type_defs.ListStreamProcessorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStreamProcessorsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamProcessorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequestPaginate:
    boto3_raw_data: "type_defs.ListUsersRequestPaginateTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProjectVersionsRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeProjectVersionsRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    ProjectArn = field("ProjectArn")
    VersionNames = field("VersionNames")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProjectVersionsRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectVersionsRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProjectVersionsRequestWait:
    boto3_raw_data: "type_defs.DescribeProjectVersionsRequestWaitTypeDef" = (
        dataclasses.field()
    )

    ProjectArn = field("ProjectArn")
    VersionNames = field("VersionNames")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProjectVersionsRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectVersionsRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectLabelsImageBackground:
    boto3_raw_data: "type_defs.DetectLabelsImageBackgroundTypeDef" = dataclasses.field()

    @cached_property
    def Quality(self):  # pragma: no cover
        return DetectLabelsImageQuality.make_one(self.boto3_raw_data["Quality"])

    @cached_property
    def DominantColors(self):  # pragma: no cover
        return DominantColor.make_many(self.boto3_raw_data["DominantColors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectLabelsImageBackgroundTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectLabelsImageBackgroundTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectLabelsImageForeground:
    boto3_raw_data: "type_defs.DetectLabelsImageForegroundTypeDef" = dataclasses.field()

    @cached_property
    def Quality(self):  # pragma: no cover
        return DetectLabelsImageQuality.make_one(self.boto3_raw_data["Quality"])

    @cached_property
    def DominantColors(self):  # pragma: no cover
        return DominantColor.make_many(self.boto3_raw_data["DominantColors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectLabelsImageForegroundTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectLabelsImageForegroundTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Instance:
    boto3_raw_data: "type_defs.InstanceTypeDef" = dataclasses.field()

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    Confidence = field("Confidence")

    @cached_property
    def DominantColors(self):  # pragma: no cover
        return DominantColor.make_many(self.boto3_raw_data["DominantColors"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectLabelsSettings:
    boto3_raw_data: "type_defs.DetectLabelsSettingsTypeDef" = dataclasses.field()

    @cached_property
    def GeneralLabels(self):  # pragma: no cover
        return GeneralLabelsSettings.make_one(self.boto3_raw_data["GeneralLabels"])

    @cached_property
    def ImageProperties(self):  # pragma: no cover
        return DetectLabelsImagePropertiesSettings.make_one(
            self.boto3_raw_data["ImageProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectLabelsSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectLabelsSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelDetectionSettings:
    boto3_raw_data: "type_defs.LabelDetectionSettingsTypeDef" = dataclasses.field()

    @cached_property
    def GeneralLabels(self):  # pragma: no cover
        return GeneralLabelsSettings.make_one(self.boto3_raw_data["GeneralLabels"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LabelDetectionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LabelDetectionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectModerationLabelsResponse:
    boto3_raw_data: "type_defs.DetectModerationLabelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ModerationLabels(self):  # pragma: no cover
        return ModerationLabel.make_many(self.boto3_raw_data["ModerationLabels"])

    ModerationModelVersion = field("ModerationModelVersion")

    @cached_property
    def HumanLoopActivationOutput(self):  # pragma: no cover
        return HumanLoopActivationOutput.make_one(
            self.boto3_raw_data["HumanLoopActivationOutput"]
        )

    ProjectVersion = field("ProjectVersion")

    @cached_property
    def ContentTypes(self):  # pragma: no cover
        return ContentType.make_many(self.boto3_raw_data["ContentTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectModerationLabelsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectModerationLabelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFacesResponse:
    boto3_raw_data: "type_defs.DisassociateFacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DisassociatedFaces(self):  # pragma: no cover
        return DisassociatedFace.make_many(self.boto3_raw_data["DisassociatedFaces"])

    @cached_property
    def UnsuccessfulFaceDisassociations(self):  # pragma: no cover
        return UnsuccessfulFaceDisassociation.make_many(
            self.boto3_raw_data["UnsuccessfulFaceDisassociations"]
        )

    UserStatus = field("UserStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateFacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributeDatasetEntriesRequest:
    boto3_raw_data: "type_defs.DistributeDatasetEntriesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Datasets(self):  # pragma: no cover
        return DistributeDataset.make_many(self.boto3_raw_data["Datasets"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DistributeDatasetEntriesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributeDatasetEntriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaceDetail:
    boto3_raw_data: "type_defs.FaceDetailTypeDef" = dataclasses.field()

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    @cached_property
    def AgeRange(self):  # pragma: no cover
        return AgeRange.make_one(self.boto3_raw_data["AgeRange"])

    @cached_property
    def Smile(self):  # pragma: no cover
        return Smile.make_one(self.boto3_raw_data["Smile"])

    @cached_property
    def Eyeglasses(self):  # pragma: no cover
        return Eyeglasses.make_one(self.boto3_raw_data["Eyeglasses"])

    @cached_property
    def Sunglasses(self):  # pragma: no cover
        return Sunglasses.make_one(self.boto3_raw_data["Sunglasses"])

    @cached_property
    def Gender(self):  # pragma: no cover
        return Gender.make_one(self.boto3_raw_data["Gender"])

    @cached_property
    def Beard(self):  # pragma: no cover
        return Beard.make_one(self.boto3_raw_data["Beard"])

    @cached_property
    def Mustache(self):  # pragma: no cover
        return Mustache.make_one(self.boto3_raw_data["Mustache"])

    @cached_property
    def EyesOpen(self):  # pragma: no cover
        return EyeOpen.make_one(self.boto3_raw_data["EyesOpen"])

    @cached_property
    def MouthOpen(self):  # pragma: no cover
        return MouthOpen.make_one(self.boto3_raw_data["MouthOpen"])

    @cached_property
    def Emotions(self):  # pragma: no cover
        return Emotion.make_many(self.boto3_raw_data["Emotions"])

    @cached_property
    def Landmarks(self):  # pragma: no cover
        return Landmark.make_many(self.boto3_raw_data["Landmarks"])

    @cached_property
    def Pose(self):  # pragma: no cover
        return Pose.make_one(self.boto3_raw_data["Pose"])

    @cached_property
    def Quality(self):  # pragma: no cover
        return ImageQuality.make_one(self.boto3_raw_data["Quality"])

    Confidence = field("Confidence")

    @cached_property
    def FaceOccluded(self):  # pragma: no cover
        return FaceOccluded.make_one(self.boto3_raw_data["FaceOccluded"])

    @cached_property
    def EyeDirection(self):  # pragma: no cover
        return EyeDirection.make_one(self.boto3_raw_data["EyeDirection"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FaceDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FaceDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamProcessorSettingsOutput:
    boto3_raw_data: "type_defs.StreamProcessorSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FaceSearch(self):  # pragma: no cover
        return FaceSearchSettings.make_one(self.boto3_raw_data["FaceSearch"])

    @cached_property
    def ConnectedHome(self):  # pragma: no cover
        return ConnectedHomeSettingsOutput.make_one(
            self.boto3_raw_data["ConnectedHome"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StreamProcessorSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamProcessorSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamProcessorSettings:
    boto3_raw_data: "type_defs.StreamProcessorSettingsTypeDef" = dataclasses.field()

    @cached_property
    def FaceSearch(self):  # pragma: no cover
        return FaceSearchSettings.make_one(self.boto3_raw_data["FaceSearch"])

    @cached_property
    def ConnectedHome(self):  # pragma: no cover
        return ConnectedHomeSettings.make_one(self.boto3_raw_data["ConnectedHome"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamProcessorSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamProcessorSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Geometry:
    boto3_raw_data: "type_defs.GeometryTypeDef" = dataclasses.field()

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    @cached_property
    def Polygon(self):  # pragma: no cover
        return Point.make_many(self.boto3_raw_data["Polygon"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeometryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeometryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionOfInterestOutput:
    boto3_raw_data: "type_defs.RegionOfInterestOutputTypeDef" = dataclasses.field()

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    @cached_property
    def Polygon(self):  # pragma: no cover
        return Point.make_many(self.boto3_raw_data["Polygon"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegionOfInterestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegionOfInterestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionOfInterest:
    boto3_raw_data: "type_defs.RegionOfInterestTypeDef" = dataclasses.field()

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    @cached_property
    def Polygon(self):  # pragma: no cover
        return Point.make_many(self.boto3_raw_data["Polygon"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionOfInterestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegionOfInterestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HumanLoopConfig:
    boto3_raw_data: "type_defs.HumanLoopConfigTypeDef" = dataclasses.field()

    HumanLoopName = field("HumanLoopName")
    FlowDefinitionArn = field("FlowDefinitionArn")

    @cached_property
    def DataAttributes(self):  # pragma: no cover
        return HumanLoopDataAttributes.make_one(self.boto3_raw_data["DataAttributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HumanLoopConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HumanLoopConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamProcessingStartSelector:
    boto3_raw_data: "type_defs.StreamProcessingStartSelectorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def KVSStreamStartSelector(self):  # pragma: no cover
        return KinesisVideoStreamStartSelector.make_one(
            self.boto3_raw_data["KVSStreamStartSelector"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StreamProcessingStartSelectorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamProcessingStartSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamProcessorInput:
    boto3_raw_data: "type_defs.StreamProcessorInputTypeDef" = dataclasses.field()

    @cached_property
    def KinesisVideoStream(self):  # pragma: no cover
        return KinesisVideoStream.make_one(self.boto3_raw_data["KinesisVideoStream"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamProcessorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamProcessorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectPoliciesResponse:
    boto3_raw_data: "type_defs.ListProjectPoliciesResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProjectPolicies(self):  # pragma: no cover
        return ProjectPolicy.make_many(self.boto3_raw_data["ProjectPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamProcessorsResponse:
    boto3_raw_data: "type_defs.ListStreamProcessorsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StreamProcessors(self):  # pragma: no cover
        return StreamProcessor.make_many(self.boto3_raw_data["StreamProcessors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStreamProcessorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamProcessorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersResponse:
    boto3_raw_data: "type_defs.ListUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserMatch:
    boto3_raw_data: "type_defs.UserMatchTypeDef" = dataclasses.field()

    Similarity = field("Similarity")

    @cached_property
    def User(self):  # pragma: no cover
        return MatchedUser.make_one(self.boto3_raw_data["User"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserMatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaAnalysisOperationsConfig:
    boto3_raw_data: "type_defs.MediaAnalysisOperationsConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DetectModerationLabels(self):  # pragma: no cover
        return MediaAnalysisDetectModerationLabelsConfig.make_one(
            self.boto3_raw_data["DetectModerationLabels"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MediaAnalysisOperationsConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaAnalysisOperationsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaAnalysisResults:
    boto3_raw_data: "type_defs.MediaAnalysisResultsTypeDef" = dataclasses.field()

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

    @cached_property
    def ModelVersions(self):  # pragma: no cover
        return MediaAnalysisModelVersions.make_one(self.boto3_raw_data["ModelVersions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaAnalysisResultsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaAnalysisResultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamProcessorOutput:
    boto3_raw_data: "type_defs.StreamProcessorOutputTypeDef" = dataclasses.field()

    @cached_property
    def KinesisDataStream(self):  # pragma: no cover
        return KinesisDataStream.make_one(self.boto3_raw_data["KinesisDataStream"])

    @cached_property
    def S3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["S3Destination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamProcessorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamProcessorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentDetection:
    boto3_raw_data: "type_defs.SegmentDetectionTypeDef" = dataclasses.field()

    Type = field("Type")
    StartTimestampMillis = field("StartTimestampMillis")
    EndTimestampMillis = field("EndTimestampMillis")
    DurationMillis = field("DurationMillis")
    StartTimecodeSMPTE = field("StartTimecodeSMPTE")
    EndTimecodeSMPTE = field("EndTimecodeSMPTE")
    DurationSMPTE = field("DurationSMPTE")

    @cached_property
    def TechnicalCueSegment(self):  # pragma: no cover
        return TechnicalCueSegment.make_one(self.boto3_raw_data["TechnicalCueSegment"])

    @cached_property
    def ShotSegment(self):  # pragma: no cover
        return ShotSegment.make_one(self.boto3_raw_data["ShotSegment"])

    StartFrameNumber = field("StartFrameNumber")
    EndFrameNumber = field("EndFrameNumber")
    DurationFrames = field("DurationFrames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentDetectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaceMatch:
    boto3_raw_data: "type_defs.FaceMatchTypeDef" = dataclasses.field()

    Similarity = field("Similarity")

    @cached_property
    def Face(self):  # pragma: no cover
        return Face.make_one(self.boto3_raw_data["Face"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FaceMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FaceMatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFacesResponse:
    boto3_raw_data: "type_defs.ListFacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Faces(self):  # pragma: no cover
        return Face.make_many(self.boto3_raw_data["Faces"])

    FaceModelVersion = field("FaceModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFacesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFaceLivenessSessionResultsResponse:
    boto3_raw_data: "type_defs.GetFaceLivenessSessionResultsResponseTypeDef" = (
        dataclasses.field()
    )

    SessionId = field("SessionId")
    Status = field("Status")
    Confidence = field("Confidence")

    @cached_property
    def ReferenceImage(self):  # pragma: no cover
        return AuditImage.make_one(self.boto3_raw_data["ReferenceImage"])

    @cached_property
    def AuditImages(self):  # pragma: no cover
        return AuditImage.make_many(self.boto3_raw_data["AuditImages"])

    @cached_property
    def Challenge(self):  # pragma: no cover
        return Challenge.make_one(self.boto3_raw_data["Challenge"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFaceLivenessSessionResultsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFaceLivenessSessionResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Asset:
    boto3_raw_data: "type_defs.AssetTypeDef" = dataclasses.field()

    @cached_property
    def GroundTruthManifest(self):  # pragma: no cover
        return GroundTruthManifest.make_one(self.boto3_raw_data["GroundTruthManifest"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetSource:
    boto3_raw_data: "type_defs.DatasetSourceTypeDef" = dataclasses.field()

    @cached_property
    def GroundTruthManifest(self):  # pragma: no cover
        return GroundTruthManifest.make_one(self.boto3_raw_data["GroundTruthManifest"])

    DatasetArn = field("DatasetArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationResult:
    boto3_raw_data: "type_defs.EvaluationResultTypeDef" = dataclasses.field()

    F1Score = field("F1Score")

    @cached_property
    def Summary(self):  # pragma: no cover
        return Summary.make_one(self.boto3_raw_data["Summary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCelebrityRecognitionRequest:
    boto3_raw_data: "type_defs.StartCelebrityRecognitionRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    JobTag = field("JobTag")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartCelebrityRecognitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCelebrityRecognitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartContentModerationRequest:
    boto3_raw_data: "type_defs.StartContentModerationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    MinConfidence = field("MinConfidence")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    JobTag = field("JobTag")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartContentModerationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartContentModerationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFaceDetectionRequest:
    boto3_raw_data: "type_defs.StartFaceDetectionRequestTypeDef" = dataclasses.field()

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    FaceAttributes = field("FaceAttributes")
    JobTag = field("JobTag")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFaceDetectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFaceDetectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFaceSearchRequest:
    boto3_raw_data: "type_defs.StartFaceSearchRequestTypeDef" = dataclasses.field()

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    CollectionId = field("CollectionId")
    ClientRequestToken = field("ClientRequestToken")
    FaceMatchThreshold = field("FaceMatchThreshold")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    JobTag = field("JobTag")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFaceSearchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFaceSearchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPersonTrackingRequest:
    boto3_raw_data: "type_defs.StartPersonTrackingRequestTypeDef" = dataclasses.field()

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    JobTag = field("JobTag")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPersonTrackingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPersonTrackingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSegmentDetectionFilters:
    boto3_raw_data: "type_defs.StartSegmentDetectionFiltersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TechnicalCueFilter(self):  # pragma: no cover
        return StartTechnicalCueDetectionFilter.make_one(
            self.boto3_raw_data["TechnicalCueFilter"]
        )

    @cached_property
    def ShotFilter(self):  # pragma: no cover
        return StartShotDetectionFilter.make_one(self.boto3_raw_data["ShotFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSegmentDetectionFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSegmentDetectionFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDatasetEntriesRequest:
    boto3_raw_data: "type_defs.UpdateDatasetEntriesRequestTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")

    @cached_property
    def Changes(self):  # pragma: no cover
        return DatasetChanges.make_one(self.boto3_raw_data["Changes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatasetEntriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatasetEntriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareFacesRequest:
    boto3_raw_data: "type_defs.CompareFacesRequestTypeDef" = dataclasses.field()

    @cached_property
    def SourceImage(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["SourceImage"])

    @cached_property
    def TargetImage(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["TargetImage"])

    SimilarityThreshold = field("SimilarityThreshold")
    QualityFilter = field("QualityFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompareFacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareFacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectCustomLabelsRequest:
    boto3_raw_data: "type_defs.DetectCustomLabelsRequestTypeDef" = dataclasses.field()

    ProjectVersionArn = field("ProjectVersionArn")

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    MaxResults = field("MaxResults")
    MinConfidence = field("MinConfidence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectCustomLabelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectCustomLabelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectFacesRequest:
    boto3_raw_data: "type_defs.DetectFacesRequestTypeDef" = dataclasses.field()

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    Attributes = field("Attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectFacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectFacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectProtectiveEquipmentRequest:
    boto3_raw_data: "type_defs.DetectProtectiveEquipmentRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    @cached_property
    def SummarizationAttributes(self):  # pragma: no cover
        return ProtectiveEquipmentSummarizationAttributes.make_one(
            self.boto3_raw_data["SummarizationAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectProtectiveEquipmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectProtectiveEquipmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexFacesRequest:
    boto3_raw_data: "type_defs.IndexFacesRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    ExternalImageId = field("ExternalImageId")
    DetectionAttributes = field("DetectionAttributes")
    MaxFaces = field("MaxFaces")
    QualityFilter = field("QualityFilter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexFacesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexFacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecognizeCelebritiesRequest:
    boto3_raw_data: "type_defs.RecognizeCelebritiesRequestTypeDef" = dataclasses.field()

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecognizeCelebritiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecognizeCelebritiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchFacesByImageRequest:
    boto3_raw_data: "type_defs.SearchFacesByImageRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    MaxFaces = field("MaxFaces")
    FaceMatchThreshold = field("FaceMatchThreshold")
    QualityFilter = field("QualityFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchFacesByImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchFacesByImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUsersByImageRequest:
    boto3_raw_data: "type_defs.SearchUsersByImageRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    UserMatchThreshold = field("UserMatchThreshold")
    MaxUsers = field("MaxUsers")
    QualityFilter = field("QualityFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUsersByImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUsersByImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFaceLivenessSessionRequestSettings:
    boto3_raw_data: "type_defs.CreateFaceLivenessSessionRequestSettingsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return LivenessOutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    AuditImagesLimit = field("AuditImagesLimit")

    @cached_property
    def ChallengePreferences(self):  # pragma: no cover
        return ChallengePreference.make_many(
            self.boto3_raw_data["ChallengePreferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFaceLivenessSessionRequestSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFaceLivenessSessionRequestSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Celebrity:
    boto3_raw_data: "type_defs.CelebrityTypeDef" = dataclasses.field()

    Urls = field("Urls")
    Name = field("Name")
    Id = field("Id")

    @cached_property
    def Face(self):  # pragma: no cover
        return ComparedFace.make_one(self.boto3_raw_data["Face"])

    MatchConfidence = field("MatchConfidence")

    @cached_property
    def KnownGender(self):  # pragma: no cover
        return KnownGender.make_one(self.boto3_raw_data["KnownGender"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CelebrityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CelebrityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareFacesMatch:
    boto3_raw_data: "type_defs.CompareFacesMatchTypeDef" = dataclasses.field()

    Similarity = field("Similarity")

    @cached_property
    def Face(self):  # pragma: no cover
        return ComparedFace.make_one(self.boto3_raw_data["Face"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CompareFacesMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareFacesMatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContentModerationResponse:
    boto3_raw_data: "type_defs.GetContentModerationResponseTypeDef" = (
        dataclasses.field()
    )

    JobStatus = field("JobStatus")
    StatusMessage = field("StatusMessage")

    @cached_property
    def VideoMetadata(self):  # pragma: no cover
        return VideoMetadata.make_one(self.boto3_raw_data["VideoMetadata"])

    @cached_property
    def ModerationLabels(self):  # pragma: no cover
        return ContentModerationDetection.make_many(
            self.boto3_raw_data["ModerationLabels"]
        )

    ModerationModelVersion = field("ModerationModelVersion")
    JobId = field("JobId")

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    JobTag = field("JobTag")

    @cached_property
    def GetRequestMetadata(self):  # pragma: no cover
        return GetContentModerationRequestMetadata.make_one(
            self.boto3_raw_data["GetRequestMetadata"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContentModerationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContentModerationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectiveEquipmentBodyPart:
    boto3_raw_data: "type_defs.ProtectiveEquipmentBodyPartTypeDef" = dataclasses.field()

    Name = field("Name")
    Confidence = field("Confidence")

    @cached_property
    def EquipmentDetections(self):  # pragma: no cover
        return EquipmentDetection.make_many(self.boto3_raw_data["EquipmentDetections"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectiveEquipmentBodyPartTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectiveEquipmentBodyPartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetResponse:
    boto3_raw_data: "type_defs.DescribeDatasetResponseTypeDef" = dataclasses.field()

    @cached_property
    def DatasetDescription(self):  # pragma: no cover
        return DatasetDescription.make_one(self.boto3_raw_data["DatasetDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetLabelsResponse:
    boto3_raw_data: "type_defs.ListDatasetLabelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DatasetLabelDescriptions(self):  # pragma: no cover
        return DatasetLabelDescription.make_many(
            self.boto3_raw_data["DatasetLabelDescriptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetLabelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetLabelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProjectsResponse:
    boto3_raw_data: "type_defs.DescribeProjectsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProjectDescriptions(self):  # pragma: no cover
        return ProjectDescription.make_many(self.boto3_raw_data["ProjectDescriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProjectsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectLabelsImageProperties:
    boto3_raw_data: "type_defs.DetectLabelsImagePropertiesTypeDef" = dataclasses.field()

    @cached_property
    def Quality(self):  # pragma: no cover
        return DetectLabelsImageQuality.make_one(self.boto3_raw_data["Quality"])

    @cached_property
    def DominantColors(self):  # pragma: no cover
        return DominantColor.make_many(self.boto3_raw_data["DominantColors"])

    @cached_property
    def Foreground(self):  # pragma: no cover
        return DetectLabelsImageForeground.make_one(self.boto3_raw_data["Foreground"])

    @cached_property
    def Background(self):  # pragma: no cover
        return DetectLabelsImageBackground.make_one(self.boto3_raw_data["Background"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectLabelsImagePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectLabelsImagePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Label:
    boto3_raw_data: "type_defs.LabelTypeDef" = dataclasses.field()

    Name = field("Name")
    Confidence = field("Confidence")

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def Parents(self):  # pragma: no cover
        return Parent.make_many(self.boto3_raw_data["Parents"])

    @cached_property
    def Aliases(self):  # pragma: no cover
        return LabelAlias.make_many(self.boto3_raw_data["Aliases"])

    @cached_property
    def Categories(self):  # pragma: no cover
        return LabelCategory.make_many(self.boto3_raw_data["Categories"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LabelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectLabelsRequest:
    boto3_raw_data: "type_defs.DetectLabelsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    MaxLabels = field("MaxLabels")
    MinConfidence = field("MinConfidence")
    Features = field("Features")

    @cached_property
    def Settings(self):  # pragma: no cover
        return DetectLabelsSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectLabelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectLabelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLabelDetectionRequest:
    boto3_raw_data: "type_defs.StartLabelDetectionRequestTypeDef" = dataclasses.field()

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    ClientRequestToken = field("ClientRequestToken")
    MinConfidence = field("MinConfidence")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    JobTag = field("JobTag")
    Features = field("Features")

    @cached_property
    def Settings(self):  # pragma: no cover
        return LabelDetectionSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLabelDetectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLabelDetectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CelebrityDetail:
    boto3_raw_data: "type_defs.CelebrityDetailTypeDef" = dataclasses.field()

    Urls = field("Urls")
    Name = field("Name")
    Id = field("Id")
    Confidence = field("Confidence")

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    @cached_property
    def Face(self):  # pragma: no cover
        return FaceDetail.make_one(self.boto3_raw_data["Face"])

    @cached_property
    def KnownGender(self):  # pragma: no cover
        return KnownGender.make_one(self.boto3_raw_data["KnownGender"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CelebrityDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CelebrityDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectFacesResponse:
    boto3_raw_data: "type_defs.DetectFacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def FaceDetails(self):  # pragma: no cover
        return FaceDetail.make_many(self.boto3_raw_data["FaceDetails"])

    OrientationCorrection = field("OrientationCorrection")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectFacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectFacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaceDetection:
    boto3_raw_data: "type_defs.FaceDetectionTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")

    @cached_property
    def Face(self):  # pragma: no cover
        return FaceDetail.make_one(self.boto3_raw_data["Face"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FaceDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FaceDetectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaceRecord:
    boto3_raw_data: "type_defs.FaceRecordTypeDef" = dataclasses.field()

    @cached_property
    def Face(self):  # pragma: no cover
        return Face.make_one(self.boto3_raw_data["Face"])

    @cached_property
    def FaceDetail(self):  # pragma: no cover
        return FaceDetail.make_one(self.boto3_raw_data["FaceDetail"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FaceRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FaceRecordTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PersonDetail:
    boto3_raw_data: "type_defs.PersonDetailTypeDef" = dataclasses.field()

    Index = field("Index")

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    @cached_property
    def Face(self):  # pragma: no cover
        return FaceDetail.make_one(self.boto3_raw_data["Face"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PersonDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PersonDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchedFaceDetails:
    boto3_raw_data: "type_defs.SearchedFaceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def FaceDetail(self):  # pragma: no cover
        return FaceDetail.make_one(self.boto3_raw_data["FaceDetail"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchedFaceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchedFaceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnindexedFace:
    boto3_raw_data: "type_defs.UnindexedFaceTypeDef" = dataclasses.field()

    Reasons = field("Reasons")

    @cached_property
    def FaceDetail(self):  # pragma: no cover
        return FaceDetail.make_one(self.boto3_raw_data["FaceDetail"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UnindexedFaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UnindexedFaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnsearchedFace:
    boto3_raw_data: "type_defs.UnsearchedFaceTypeDef" = dataclasses.field()

    @cached_property
    def FaceDetails(self):  # pragma: no cover
        return FaceDetail.make_one(self.boto3_raw_data["FaceDetails"])

    Reasons = field("Reasons")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UnsearchedFaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UnsearchedFaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLabel:
    boto3_raw_data: "type_defs.CustomLabelTypeDef" = dataclasses.field()

    Name = field("Name")
    Confidence = field("Confidence")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return Geometry.make_one(self.boto3_raw_data["Geometry"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomLabelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomLabelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextDetection:
    boto3_raw_data: "type_defs.TextDetectionTypeDef" = dataclasses.field()

    DetectedText = field("DetectedText")
    Type = field("Type")
    Id = field("Id")
    ParentId = field("ParentId")
    Confidence = field("Confidence")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return Geometry.make_one(self.boto3_raw_data["Geometry"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextDetectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectModerationLabelsRequest:
    boto3_raw_data: "type_defs.DetectModerationLabelsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    MinConfidence = field("MinConfidence")

    @cached_property
    def HumanLoopConfig(self):  # pragma: no cover
        return HumanLoopConfig.make_one(self.boto3_raw_data["HumanLoopConfig"])

    ProjectVersion = field("ProjectVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectModerationLabelsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectModerationLabelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartStreamProcessorRequest:
    boto3_raw_data: "type_defs.StartStreamProcessorRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def StartSelector(self):  # pragma: no cover
        return StreamProcessingStartSelector.make_one(
            self.boto3_raw_data["StartSelector"]
        )

    @cached_property
    def StopSelector(self):  # pragma: no cover
        return StreamProcessingStopSelector.make_one(
            self.boto3_raw_data["StopSelector"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartStreamProcessorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartStreamProcessorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUsersResponse:
    boto3_raw_data: "type_defs.SearchUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserMatches(self):  # pragma: no cover
        return UserMatch.make_many(self.boto3_raw_data["UserMatches"])

    FaceModelVersion = field("FaceModelVersion")

    @cached_property
    def SearchedFace(self):  # pragma: no cover
        return SearchedFace.make_one(self.boto3_raw_data["SearchedFace"])

    @cached_property
    def SearchedUser(self):  # pragma: no cover
        return SearchedUser.make_one(self.boto3_raw_data["SearchedUser"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUsersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMediaAnalysisJobRequest:
    boto3_raw_data: "type_defs.StartMediaAnalysisJobRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OperationsConfig(self):  # pragma: no cover
        return MediaAnalysisOperationsConfig.make_one(
            self.boto3_raw_data["OperationsConfig"]
        )

    @cached_property
    def Input(self):  # pragma: no cover
        return MediaAnalysisInput.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return MediaAnalysisOutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    ClientRequestToken = field("ClientRequestToken")
    JobName = field("JobName")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMediaAnalysisJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMediaAnalysisJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaAnalysisJobResponse:
    boto3_raw_data: "type_defs.GetMediaAnalysisJobResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")
    JobName = field("JobName")

    @cached_property
    def OperationsConfig(self):  # pragma: no cover
        return MediaAnalysisOperationsConfig.make_one(
            self.boto3_raw_data["OperationsConfig"]
        )

    Status = field("Status")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return MediaAnalysisJobFailureDetails.make_one(
            self.boto3_raw_data["FailureDetails"]
        )

    CreationTimestamp = field("CreationTimestamp")
    CompletionTimestamp = field("CompletionTimestamp")

    @cached_property
    def Input(self):  # pragma: no cover
        return MediaAnalysisInput.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return MediaAnalysisOutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Results(self):  # pragma: no cover
        return MediaAnalysisResults.make_one(self.boto3_raw_data["Results"])

    @cached_property
    def ManifestSummary(self):  # pragma: no cover
        return MediaAnalysisManifestSummary.make_one(
            self.boto3_raw_data["ManifestSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMediaAnalysisJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaAnalysisJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaAnalysisJobDescription:
    boto3_raw_data: "type_defs.MediaAnalysisJobDescriptionTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def OperationsConfig(self):  # pragma: no cover
        return MediaAnalysisOperationsConfig.make_one(
            self.boto3_raw_data["OperationsConfig"]
        )

    Status = field("Status")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def Input(self):  # pragma: no cover
        return MediaAnalysisInput.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return MediaAnalysisOutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    JobName = field("JobName")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return MediaAnalysisJobFailureDetails.make_one(
            self.boto3_raw_data["FailureDetails"]
        )

    CompletionTimestamp = field("CompletionTimestamp")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Results(self):  # pragma: no cover
        return MediaAnalysisResults.make_one(self.boto3_raw_data["Results"])

    @cached_property
    def ManifestSummary(self):  # pragma: no cover
        return MediaAnalysisManifestSummary.make_one(
            self.boto3_raw_data["ManifestSummary"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaAnalysisJobDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaAnalysisJobDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamProcessorResponse:
    boto3_raw_data: "type_defs.DescribeStreamProcessorResponseTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    StreamProcessorArn = field("StreamProcessorArn")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreationTimestamp = field("CreationTimestamp")
    LastUpdateTimestamp = field("LastUpdateTimestamp")

    @cached_property
    def Input(self):  # pragma: no cover
        return StreamProcessorInput.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def Output(self):  # pragma: no cover
        return StreamProcessorOutput.make_one(self.boto3_raw_data["Output"])

    RoleArn = field("RoleArn")

    @cached_property
    def Settings(self):  # pragma: no cover
        return StreamProcessorSettingsOutput.make_one(self.boto3_raw_data["Settings"])

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return StreamProcessorNotificationChannel.make_one(
            self.boto3_raw_data["NotificationChannel"]
        )

    KmsKeyId = field("KmsKeyId")

    @cached_property
    def RegionsOfInterest(self):  # pragma: no cover
        return RegionOfInterestOutput.make_many(
            self.boto3_raw_data["RegionsOfInterest"]
        )

    @cached_property
    def DataSharingPreference(self):  # pragma: no cover
        return StreamProcessorDataSharingPreference.make_one(
            self.boto3_raw_data["DataSharingPreference"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStreamProcessorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamProcessorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentDetectionResponse:
    boto3_raw_data: "type_defs.GetSegmentDetectionResponseTypeDef" = dataclasses.field()

    JobStatus = field("JobStatus")
    StatusMessage = field("StatusMessage")

    @cached_property
    def VideoMetadata(self):  # pragma: no cover
        return VideoMetadata.make_many(self.boto3_raw_data["VideoMetadata"])

    @cached_property
    def AudioMetadata(self):  # pragma: no cover
        return AudioMetadata.make_many(self.boto3_raw_data["AudioMetadata"])

    @cached_property
    def Segments(self):  # pragma: no cover
        return SegmentDetection.make_many(self.boto3_raw_data["Segments"])

    @cached_property
    def SelectedSegmentTypes(self):  # pragma: no cover
        return SegmentTypeInfo.make_many(self.boto3_raw_data["SelectedSegmentTypes"])

    JobId = field("JobId")

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    JobTag = field("JobTag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentDetectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentDetectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchFacesByImageResponse:
    boto3_raw_data: "type_defs.SearchFacesByImageResponseTypeDef" = dataclasses.field()

    @cached_property
    def SearchedFaceBoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["SearchedFaceBoundingBox"])

    SearchedFaceConfidence = field("SearchedFaceConfidence")

    @cached_property
    def FaceMatches(self):  # pragma: no cover
        return FaceMatch.make_many(self.boto3_raw_data["FaceMatches"])

    FaceModelVersion = field("FaceModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchFacesByImageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchFacesByImageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchFacesResponse:
    boto3_raw_data: "type_defs.SearchFacesResponseTypeDef" = dataclasses.field()

    SearchedFaceId = field("SearchedFaceId")

    @cached_property
    def FaceMatches(self):  # pragma: no cover
        return FaceMatch.make_many(self.boto3_raw_data["FaceMatches"])

    FaceModelVersion = field("FaceModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchFacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchFacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestingDataOutput:
    boto3_raw_data: "type_defs.TestingDataOutputTypeDef" = dataclasses.field()

    @cached_property
    def Assets(self):  # pragma: no cover
        return Asset.make_many(self.boto3_raw_data["Assets"])

    AutoCreate = field("AutoCreate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestingDataOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestingDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestingData:
    boto3_raw_data: "type_defs.TestingDataTypeDef" = dataclasses.field()

    @cached_property
    def Assets(self):  # pragma: no cover
        return Asset.make_many(self.boto3_raw_data["Assets"])

    AutoCreate = field("AutoCreate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestingDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestingDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingDataOutput:
    boto3_raw_data: "type_defs.TrainingDataOutputTypeDef" = dataclasses.field()

    @cached_property
    def Assets(self):  # pragma: no cover
        return Asset.make_many(self.boto3_raw_data["Assets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainingDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingData:
    boto3_raw_data: "type_defs.TrainingDataTypeDef" = dataclasses.field()

    @cached_property
    def Assets(self):  # pragma: no cover
        return Asset.make_many(self.boto3_raw_data["Assets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrainingDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrainingDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationData:
    boto3_raw_data: "type_defs.ValidationDataTypeDef" = dataclasses.field()

    @cached_property
    def Assets(self):  # pragma: no cover
        return Asset.make_many(self.boto3_raw_data["Assets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidationDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValidationDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetRequest:
    boto3_raw_data: "type_defs.CreateDatasetRequestTypeDef" = dataclasses.field()

    DatasetType = field("DatasetType")
    ProjectArn = field("ProjectArn")

    @cached_property
    def DatasetSource(self):  # pragma: no cover
        return DatasetSource.make_one(self.boto3_raw_data["DatasetSource"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSegmentDetectionRequest:
    boto3_raw_data: "type_defs.StartSegmentDetectionRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    SegmentTypes = field("SegmentTypes")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    JobTag = field("JobTag")

    @cached_property
    def Filters(self):  # pragma: no cover
        return StartSegmentDetectionFilters.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSegmentDetectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSegmentDetectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFaceLivenessSessionRequest:
    boto3_raw_data: "type_defs.CreateFaceLivenessSessionRequestTypeDef" = (
        dataclasses.field()
    )

    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Settings(self):  # pragma: no cover
        return CreateFaceLivenessSessionRequestSettings.make_one(
            self.boto3_raw_data["Settings"]
        )

    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFaceLivenessSessionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFaceLivenessSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecognizeCelebritiesResponse:
    boto3_raw_data: "type_defs.RecognizeCelebritiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CelebrityFaces(self):  # pragma: no cover
        return Celebrity.make_many(self.boto3_raw_data["CelebrityFaces"])

    @cached_property
    def UnrecognizedFaces(self):  # pragma: no cover
        return ComparedFace.make_many(self.boto3_raw_data["UnrecognizedFaces"])

    OrientationCorrection = field("OrientationCorrection")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecognizeCelebritiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecognizeCelebritiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareFacesResponse:
    boto3_raw_data: "type_defs.CompareFacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def SourceImageFace(self):  # pragma: no cover
        return ComparedSourceImageFace.make_one(self.boto3_raw_data["SourceImageFace"])

    @cached_property
    def FaceMatches(self):  # pragma: no cover
        return CompareFacesMatch.make_many(self.boto3_raw_data["FaceMatches"])

    @cached_property
    def UnmatchedFaces(self):  # pragma: no cover
        return ComparedFace.make_many(self.boto3_raw_data["UnmatchedFaces"])

    SourceImageOrientationCorrection = field("SourceImageOrientationCorrection")
    TargetImageOrientationCorrection = field("TargetImageOrientationCorrection")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompareFacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareFacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectiveEquipmentPerson:
    boto3_raw_data: "type_defs.ProtectiveEquipmentPersonTypeDef" = dataclasses.field()

    @cached_property
    def BodyParts(self):  # pragma: no cover
        return ProtectiveEquipmentBodyPart.make_many(self.boto3_raw_data["BodyParts"])

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    Confidence = field("Confidence")
    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectiveEquipmentPersonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectiveEquipmentPersonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectLabelsResponse:
    boto3_raw_data: "type_defs.DetectLabelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Labels(self):  # pragma: no cover
        return Label.make_many(self.boto3_raw_data["Labels"])

    OrientationCorrection = field("OrientationCorrection")
    LabelModelVersion = field("LabelModelVersion")

    @cached_property
    def ImageProperties(self):  # pragma: no cover
        return DetectLabelsImageProperties.make_one(
            self.boto3_raw_data["ImageProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectLabelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectLabelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelDetection:
    boto3_raw_data: "type_defs.LabelDetectionTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")

    @cached_property
    def Label(self):  # pragma: no cover
        return Label.make_one(self.boto3_raw_data["Label"])

    StartTimestampMillis = field("StartTimestampMillis")
    EndTimestampMillis = field("EndTimestampMillis")
    DurationMillis = field("DurationMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LabelDetectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CelebrityRecognition:
    boto3_raw_data: "type_defs.CelebrityRecognitionTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")

    @cached_property
    def Celebrity(self):  # pragma: no cover
        return CelebrityDetail.make_one(self.boto3_raw_data["Celebrity"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CelebrityRecognitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CelebrityRecognitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFaceDetectionResponse:
    boto3_raw_data: "type_defs.GetFaceDetectionResponseTypeDef" = dataclasses.field()

    JobStatus = field("JobStatus")
    StatusMessage = field("StatusMessage")

    @cached_property
    def VideoMetadata(self):  # pragma: no cover
        return VideoMetadata.make_one(self.boto3_raw_data["VideoMetadata"])

    @cached_property
    def Faces(self):  # pragma: no cover
        return FaceDetection.make_many(self.boto3_raw_data["Faces"])

    JobId = field("JobId")

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    JobTag = field("JobTag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFaceDetectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFaceDetectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PersonDetection:
    boto3_raw_data: "type_defs.PersonDetectionTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")

    @cached_property
    def Person(self):  # pragma: no cover
        return PersonDetail.make_one(self.boto3_raw_data["Person"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PersonDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PersonDetectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PersonMatch:
    boto3_raw_data: "type_defs.PersonMatchTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")

    @cached_property
    def Person(self):  # pragma: no cover
        return PersonDetail.make_one(self.boto3_raw_data["Person"])

    @cached_property
    def FaceMatches(self):  # pragma: no cover
        return FaceMatch.make_many(self.boto3_raw_data["FaceMatches"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PersonMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PersonMatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexFacesResponse:
    boto3_raw_data: "type_defs.IndexFacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def FaceRecords(self):  # pragma: no cover
        return FaceRecord.make_many(self.boto3_raw_data["FaceRecords"])

    OrientationCorrection = field("OrientationCorrection")
    FaceModelVersion = field("FaceModelVersion")

    @cached_property
    def UnindexedFaces(self):  # pragma: no cover
        return UnindexedFace.make_many(self.boto3_raw_data["UnindexedFaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IndexFacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexFacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUsersByImageResponse:
    boto3_raw_data: "type_defs.SearchUsersByImageResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserMatches(self):  # pragma: no cover
        return UserMatch.make_many(self.boto3_raw_data["UserMatches"])

    FaceModelVersion = field("FaceModelVersion")

    @cached_property
    def SearchedFace(self):  # pragma: no cover
        return SearchedFaceDetails.make_one(self.boto3_raw_data["SearchedFace"])

    @cached_property
    def UnsearchedFaces(self):  # pragma: no cover
        return UnsearchedFace.make_many(self.boto3_raw_data["UnsearchedFaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUsersByImageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUsersByImageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectCustomLabelsResponse:
    boto3_raw_data: "type_defs.DetectCustomLabelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def CustomLabels(self):  # pragma: no cover
        return CustomLabel.make_many(self.boto3_raw_data["CustomLabels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectCustomLabelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectCustomLabelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectTextResponse:
    boto3_raw_data: "type_defs.DetectTextResponseTypeDef" = dataclasses.field()

    @cached_property
    def TextDetections(self):  # pragma: no cover
        return TextDetection.make_many(self.boto3_raw_data["TextDetections"])

    TextModelVersion = field("TextModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectTextResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectTextResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextDetectionResult:
    boto3_raw_data: "type_defs.TextDetectionResultTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")

    @cached_property
    def TextDetection(self):  # pragma: no cover
        return TextDetection.make_one(self.boto3_raw_data["TextDetection"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextDetectionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextDetectionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamProcessorRequest:
    boto3_raw_data: "type_defs.CreateStreamProcessorRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Input(self):  # pragma: no cover
        return StreamProcessorInput.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def Output(self):  # pragma: no cover
        return StreamProcessorOutput.make_one(self.boto3_raw_data["Output"])

    Name = field("Name")
    Settings = field("Settings")
    RoleArn = field("RoleArn")
    Tags = field("Tags")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return StreamProcessorNotificationChannel.make_one(
            self.boto3_raw_data["NotificationChannel"]
        )

    KmsKeyId = field("KmsKeyId")
    RegionsOfInterest = field("RegionsOfInterest")

    @cached_property
    def DataSharingPreference(self):  # pragma: no cover
        return StreamProcessorDataSharingPreference.make_one(
            self.boto3_raw_data["DataSharingPreference"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStreamProcessorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamProcessorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectTextFilters:
    boto3_raw_data: "type_defs.DetectTextFiltersTypeDef" = dataclasses.field()

    @cached_property
    def WordFilter(self):  # pragma: no cover
        return DetectionFilter.make_one(self.boto3_raw_data["WordFilter"])

    RegionsOfInterest = field("RegionsOfInterest")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectTextFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectTextFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTextDetectionFilters:
    boto3_raw_data: "type_defs.StartTextDetectionFiltersTypeDef" = dataclasses.field()

    @cached_property
    def WordFilter(self):  # pragma: no cover
        return DetectionFilter.make_one(self.boto3_raw_data["WordFilter"])

    RegionsOfInterest = field("RegionsOfInterest")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTextDetectionFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTextDetectionFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStreamProcessorRequest:
    boto3_raw_data: "type_defs.UpdateStreamProcessorRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def SettingsForUpdate(self):  # pragma: no cover
        return StreamProcessorSettingsForUpdate.make_one(
            self.boto3_raw_data["SettingsForUpdate"]
        )

    RegionsOfInterestForUpdate = field("RegionsOfInterestForUpdate")

    @cached_property
    def DataSharingPreferenceForUpdate(self):  # pragma: no cover
        return StreamProcessorDataSharingPreference.make_one(
            self.boto3_raw_data["DataSharingPreferenceForUpdate"]
        )

    ParametersToDelete = field("ParametersToDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStreamProcessorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStreamProcessorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMediaAnalysisJobsResponse:
    boto3_raw_data: "type_defs.ListMediaAnalysisJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MediaAnalysisJobs(self):  # pragma: no cover
        return MediaAnalysisJobDescription.make_many(
            self.boto3_raw_data["MediaAnalysisJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMediaAnalysisJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMediaAnalysisJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestingDataResult:
    boto3_raw_data: "type_defs.TestingDataResultTypeDef" = dataclasses.field()

    @cached_property
    def Input(self):  # pragma: no cover
        return TestingDataOutput.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def Output(self):  # pragma: no cover
        return TestingDataOutput.make_one(self.boto3_raw_data["Output"])

    @cached_property
    def Validation(self):  # pragma: no cover
        return ValidationData.make_one(self.boto3_raw_data["Validation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestingDataResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestingDataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingDataResult:
    boto3_raw_data: "type_defs.TrainingDataResultTypeDef" = dataclasses.field()

    @cached_property
    def Input(self):  # pragma: no cover
        return TrainingDataOutput.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def Output(self):  # pragma: no cover
        return TrainingDataOutput.make_one(self.boto3_raw_data["Output"])

    @cached_property
    def Validation(self):  # pragma: no cover
        return ValidationData.make_one(self.boto3_raw_data["Validation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainingDataResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingDataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectProtectiveEquipmentResponse:
    boto3_raw_data: "type_defs.DetectProtectiveEquipmentResponseTypeDef" = (
        dataclasses.field()
    )

    ProtectiveEquipmentModelVersion = field("ProtectiveEquipmentModelVersion")

    @cached_property
    def Persons(self):  # pragma: no cover
        return ProtectiveEquipmentPerson.make_many(self.boto3_raw_data["Persons"])

    @cached_property
    def Summary(self):  # pragma: no cover
        return ProtectiveEquipmentSummary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetectProtectiveEquipmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectProtectiveEquipmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLabelDetectionResponse:
    boto3_raw_data: "type_defs.GetLabelDetectionResponseTypeDef" = dataclasses.field()

    JobStatus = field("JobStatus")
    StatusMessage = field("StatusMessage")

    @cached_property
    def VideoMetadata(self):  # pragma: no cover
        return VideoMetadata.make_one(self.boto3_raw_data["VideoMetadata"])

    @cached_property
    def Labels(self):  # pragma: no cover
        return LabelDetection.make_many(self.boto3_raw_data["Labels"])

    LabelModelVersion = field("LabelModelVersion")
    JobId = field("JobId")

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    JobTag = field("JobTag")

    @cached_property
    def GetRequestMetadata(self):  # pragma: no cover
        return GetLabelDetectionRequestMetadata.make_one(
            self.boto3_raw_data["GetRequestMetadata"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLabelDetectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLabelDetectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCelebrityRecognitionResponse:
    boto3_raw_data: "type_defs.GetCelebrityRecognitionResponseTypeDef" = (
        dataclasses.field()
    )

    JobStatus = field("JobStatus")
    StatusMessage = field("StatusMessage")

    @cached_property
    def VideoMetadata(self):  # pragma: no cover
        return VideoMetadata.make_one(self.boto3_raw_data["VideoMetadata"])

    @cached_property
    def Celebrities(self):  # pragma: no cover
        return CelebrityRecognition.make_many(self.boto3_raw_data["Celebrities"])

    JobId = field("JobId")

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    JobTag = field("JobTag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCelebrityRecognitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCelebrityRecognitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPersonTrackingResponse:
    boto3_raw_data: "type_defs.GetPersonTrackingResponseTypeDef" = dataclasses.field()

    JobStatus = field("JobStatus")
    StatusMessage = field("StatusMessage")

    @cached_property
    def VideoMetadata(self):  # pragma: no cover
        return VideoMetadata.make_one(self.boto3_raw_data["VideoMetadata"])

    @cached_property
    def Persons(self):  # pragma: no cover
        return PersonDetection.make_many(self.boto3_raw_data["Persons"])

    JobId = field("JobId")

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    JobTag = field("JobTag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPersonTrackingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPersonTrackingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFaceSearchResponse:
    boto3_raw_data: "type_defs.GetFaceSearchResponseTypeDef" = dataclasses.field()

    JobStatus = field("JobStatus")
    StatusMessage = field("StatusMessage")

    @cached_property
    def VideoMetadata(self):  # pragma: no cover
        return VideoMetadata.make_one(self.boto3_raw_data["VideoMetadata"])

    @cached_property
    def Persons(self):  # pragma: no cover
        return PersonMatch.make_many(self.boto3_raw_data["Persons"])

    JobId = field("JobId")

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    JobTag = field("JobTag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFaceSearchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFaceSearchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTextDetectionResponse:
    boto3_raw_data: "type_defs.GetTextDetectionResponseTypeDef" = dataclasses.field()

    JobStatus = field("JobStatus")
    StatusMessage = field("StatusMessage")

    @cached_property
    def VideoMetadata(self):  # pragma: no cover
        return VideoMetadata.make_one(self.boto3_raw_data["VideoMetadata"])

    @cached_property
    def TextDetections(self):  # pragma: no cover
        return TextDetectionResult.make_many(self.boto3_raw_data["TextDetections"])

    TextModelVersion = field("TextModelVersion")
    JobId = field("JobId")

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    JobTag = field("JobTag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTextDetectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTextDetectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectTextRequest:
    boto3_raw_data: "type_defs.DetectTextRequestTypeDef" = dataclasses.field()

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    @cached_property
    def Filters(self):  # pragma: no cover
        return DetectTextFilters.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectTextRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectTextRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTextDetectionRequest:
    boto3_raw_data: "type_defs.StartTextDetectionRequestTypeDef" = dataclasses.field()

    @cached_property
    def Video(self):  # pragma: no cover
        return Video.make_one(self.boto3_raw_data["Video"])

    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    JobTag = field("JobTag")

    @cached_property
    def Filters(self):  # pragma: no cover
        return StartTextDetectionFilters.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTextDetectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTextDetectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectVersionRequest:
    boto3_raw_data: "type_defs.CreateProjectVersionRequestTypeDef" = dataclasses.field()

    ProjectArn = field("ProjectArn")
    VersionName = field("VersionName")

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    TrainingData = field("TrainingData")
    TestingData = field("TestingData")
    Tags = field("Tags")
    KmsKeyId = field("KmsKeyId")
    VersionDescription = field("VersionDescription")

    @cached_property
    def FeatureConfig(self):  # pragma: no cover
        return CustomizationFeatureConfig.make_one(self.boto3_raw_data["FeatureConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectVersionDescription:
    boto3_raw_data: "type_defs.ProjectVersionDescriptionTypeDef" = dataclasses.field()

    ProjectVersionArn = field("ProjectVersionArn")
    CreationTimestamp = field("CreationTimestamp")
    MinInferenceUnits = field("MinInferenceUnits")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    BillableTrainingTimeInSeconds = field("BillableTrainingTimeInSeconds")
    TrainingEndTimestamp = field("TrainingEndTimestamp")

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    @cached_property
    def TrainingDataResult(self):  # pragma: no cover
        return TrainingDataResult.make_one(self.boto3_raw_data["TrainingDataResult"])

    @cached_property
    def TestingDataResult(self):  # pragma: no cover
        return TestingDataResult.make_one(self.boto3_raw_data["TestingDataResult"])

    @cached_property
    def EvaluationResult(self):  # pragma: no cover
        return EvaluationResult.make_one(self.boto3_raw_data["EvaluationResult"])

    @cached_property
    def ManifestSummary(self):  # pragma: no cover
        return GroundTruthManifest.make_one(self.boto3_raw_data["ManifestSummary"])

    KmsKeyId = field("KmsKeyId")
    MaxInferenceUnits = field("MaxInferenceUnits")
    SourceProjectVersionArn = field("SourceProjectVersionArn")
    VersionDescription = field("VersionDescription")
    Feature = field("Feature")
    BaseModelVersion = field("BaseModelVersion")

    @cached_property
    def FeatureConfig(self):  # pragma: no cover
        return CustomizationFeatureConfig.make_one(self.boto3_raw_data["FeatureConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectVersionDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectVersionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProjectVersionsResponse:
    boto3_raw_data: "type_defs.DescribeProjectVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProjectVersionDescriptions(self):  # pragma: no cover
        return ProjectVersionDescription.make_many(
            self.boto3_raw_data["ProjectVersionDescriptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeProjectVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
