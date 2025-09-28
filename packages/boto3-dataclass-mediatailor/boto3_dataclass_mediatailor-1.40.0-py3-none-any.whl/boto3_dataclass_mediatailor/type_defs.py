# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediatailor import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class SecretsManagerAccessTokenConfiguration:
    boto3_raw_data: "type_defs.SecretsManagerAccessTokenConfigurationTypeDef" = (
        dataclasses.field()
    )

    HeaderName = field("HeaderName")
    SecretArn = field("SecretArn")
    SecretStringKey = field("SecretStringKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SecretsManagerAccessTokenConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecretsManagerAccessTokenConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdBreakOpportunity:
    boto3_raw_data: "type_defs.AdBreakOpportunityTypeDef" = dataclasses.field()

    OffsetMillis = field("OffsetMillis")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdBreakOpportunityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdBreakOpportunityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyValuePair:
    boto3_raw_data: "type_defs.KeyValuePairTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyValuePairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyValuePairTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlateSource:
    boto3_raw_data: "type_defs.SlateSourceTypeDef" = dataclasses.field()

    SourceLocationName = field("SourceLocationName")
    VodSourceName = field("VodSourceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlateSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlateSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpliceInsertMessage:
    boto3_raw_data: "type_defs.SpliceInsertMessageTypeDef" = dataclasses.field()

    AvailNum = field("AvailNum")
    AvailsExpected = field("AvailsExpected")
    SpliceEventId = field("SpliceEventId")
    UniqueProgramId = field("UniqueProgramId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpliceInsertMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpliceInsertMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdConditioningConfiguration:
    boto3_raw_data: "type_defs.AdConditioningConfigurationTypeDef" = dataclasses.field()

    StreamingMediaFileConditioning = field("StreamingMediaFileConditioning")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdConditioningConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdConditioningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdMarkerPassthrough:
    boto3_raw_data: "type_defs.AdMarkerPassthroughTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdMarkerPassthroughTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdMarkerPassthroughTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdsInteractionLogOutput:
    boto3_raw_data: "type_defs.AdsInteractionLogOutputTypeDef" = dataclasses.field()

    PublishOptInEventTypes = field("PublishOptInEventTypes")
    ExcludeEventTypes = field("ExcludeEventTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdsInteractionLogOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdsInteractionLogOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdsInteractionLog:
    boto3_raw_data: "type_defs.AdsInteractionLogTypeDef" = dataclasses.field()

    PublishOptInEventTypes = field("PublishOptInEventTypes")
    ExcludeEventTypes = field("ExcludeEventTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdsInteractionLogTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdsInteractionLogTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Alert:
    boto3_raw_data: "type_defs.AlertTypeDef" = dataclasses.field()

    AlertCode = field("AlertCode")
    AlertMessage = field("AlertMessage")
    LastModifiedTime = field("LastModifiedTime")
    RelatedResourceArns = field("RelatedResourceArns")
    ResourceArn = field("ResourceArn")
    Category = field("Category")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlertTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlertTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClipRange:
    boto3_raw_data: "type_defs.ClipRangeTypeDef" = dataclasses.field()

    EndOffsetMillis = field("EndOffsetMillis")
    StartOffsetMillis = field("StartOffsetMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClipRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClipRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailMatchingCriteria:
    boto3_raw_data: "type_defs.AvailMatchingCriteriaTypeDef" = dataclasses.field()

    DynamicVariable = field("DynamicVariable")
    Operator = field("Operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailMatchingCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailMatchingCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailSuppression:
    boto3_raw_data: "type_defs.AvailSuppressionTypeDef" = dataclasses.field()

    Mode = field("Mode")
    Value = field("Value")
    FillPolicy = field("FillPolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AvailSuppressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailSuppressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Bumper:
    boto3_raw_data: "type_defs.BumperTypeDef" = dataclasses.field()

    EndUrl = field("EndUrl")
    StartUrl = field("StartUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BumperTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BumperTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CdnConfiguration:
    boto3_raw_data: "type_defs.CdnConfigurationTypeDef" = dataclasses.field()

    AdSegmentUrlPrefix = field("AdSegmentUrlPrefix")
    ContentSegmentUrlPrefix = field("ContentSegmentUrlPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CdnConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CdnConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogConfigurationForChannel:
    boto3_raw_data: "type_defs.LogConfigurationForChannelTypeDef" = dataclasses.field()

    LogTypes = field("LogTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogConfigurationForChannelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogConfigurationForChannelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigureLogsForChannelRequest:
    boto3_raw_data: "type_defs.ConfigureLogsForChannelRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelName = field("ChannelName")
    LogTypes = field("LogTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfigureLogsForChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigureLogsForChannelRequestTypeDef"]
        ],
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
class ManifestServiceInteractionLogOutput:
    boto3_raw_data: "type_defs.ManifestServiceInteractionLogOutputTypeDef" = (
        dataclasses.field()
    )

    ExcludeEventTypes = field("ExcludeEventTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManifestServiceInteractionLogOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManifestServiceInteractionLogOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeShiftConfiguration:
    boto3_raw_data: "type_defs.TimeShiftConfigurationTypeDef" = dataclasses.field()

    MaxTimeDelaySeconds = field("MaxTimeDelaySeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeShiftConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeShiftConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpPackageConfiguration:
    boto3_raw_data: "type_defs.HttpPackageConfigurationTypeDef" = dataclasses.field()

    Path = field("Path")
    SourceGroup = field("SourceGroup")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpPackageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpPackageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultSegmentDeliveryConfiguration:
    boto3_raw_data: "type_defs.DefaultSegmentDeliveryConfigurationTypeDef" = (
        dataclasses.field()
    )

    BaseUrl = field("BaseUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DefaultSegmentDeliveryConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultSegmentDeliveryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpConfiguration:
    boto3_raw_data: "type_defs.HttpConfigurationTypeDef" = dataclasses.field()

    BaseUrl = field("BaseUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentDeliveryConfiguration:
    boto3_raw_data: "type_defs.SegmentDeliveryConfigurationTypeDef" = (
        dataclasses.field()
    )

    BaseUrl = field("BaseUrl")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentDeliveryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentDeliveryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashConfigurationForPut:
    boto3_raw_data: "type_defs.DashConfigurationForPutTypeDef" = dataclasses.field()

    MpdLocation = field("MpdLocation")
    OriginManifestType = field("OriginManifestType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashConfigurationForPutTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashConfigurationForPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashConfiguration:
    boto3_raw_data: "type_defs.DashConfigurationTypeDef" = dataclasses.field()

    ManifestEndpointPrefix = field("ManifestEndpointPrefix")
    MpdLocation = field("MpdLocation")
    OriginManifestType = field("OriginManifestType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashPlaylistSettings:
    boto3_raw_data: "type_defs.DashPlaylistSettingsTypeDef" = dataclasses.field()

    ManifestWindowSeconds = field("ManifestWindowSeconds")
    MinBufferTimeSeconds = field("MinBufferTimeSeconds")
    MinUpdatePeriodSeconds = field("MinUpdatePeriodSeconds")
    SuggestedPresentationDelaySeconds = field("SuggestedPresentationDelaySeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashPlaylistSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashPlaylistSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelPolicyRequest:
    boto3_raw_data: "type_defs.DeleteChannelPolicyRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelRequest:
    boto3_raw_data: "type_defs.DeleteChannelRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLiveSourceRequest:
    boto3_raw_data: "type_defs.DeleteLiveSourceRequestTypeDef" = dataclasses.field()

    LiveSourceName = field("LiveSourceName")
    SourceLocationName = field("SourceLocationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLiveSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLiveSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePlaybackConfigurationRequest:
    boto3_raw_data: "type_defs.DeletePlaybackConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePlaybackConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePlaybackConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePrefetchScheduleRequest:
    boto3_raw_data: "type_defs.DeletePrefetchScheduleRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    PlaybackConfigurationName = field("PlaybackConfigurationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePrefetchScheduleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePrefetchScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProgramRequest:
    boto3_raw_data: "type_defs.DeleteProgramRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")
    ProgramName = field("ProgramName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProgramRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProgramRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSourceLocationRequest:
    boto3_raw_data: "type_defs.DeleteSourceLocationRequestTypeDef" = dataclasses.field()

    SourceLocationName = field("SourceLocationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSourceLocationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSourceLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVodSourceRequest:
    boto3_raw_data: "type_defs.DeleteVodSourceRequestTypeDef" = dataclasses.field()

    SourceLocationName = field("SourceLocationName")
    VodSourceName = field("VodSourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVodSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVodSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelRequest:
    boto3_raw_data: "type_defs.DescribeChannelRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLiveSourceRequest:
    boto3_raw_data: "type_defs.DescribeLiveSourceRequestTypeDef" = dataclasses.field()

    LiveSourceName = field("LiveSourceName")
    SourceLocationName = field("SourceLocationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLiveSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLiveSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProgramRequest:
    boto3_raw_data: "type_defs.DescribeProgramRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")
    ProgramName = field("ProgramName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProgramRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProgramRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceLocationRequest:
    boto3_raw_data: "type_defs.DescribeSourceLocationRequestTypeDef" = (
        dataclasses.field()
    )

    SourceLocationName = field("SourceLocationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSourceLocationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVodSourceRequest:
    boto3_raw_data: "type_defs.DescribeVodSourceRequestTypeDef" = dataclasses.field()

    SourceLocationName = field("SourceLocationName")
    VodSourceName = field("VodSourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVodSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVodSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelPolicyRequest:
    boto3_raw_data: "type_defs.GetChannelPolicyRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelPolicyRequestTypeDef"]
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
class GetChannelScheduleRequest:
    boto3_raw_data: "type_defs.GetChannelScheduleRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")
    DurationMinutes = field("DurationMinutes")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Audience = field("Audience")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPlaybackConfigurationRequest:
    boto3_raw_data: "type_defs.GetPlaybackConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPlaybackConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPlaybackConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsConfiguration:
    boto3_raw_data: "type_defs.HlsConfigurationTypeDef" = dataclasses.field()

    ManifestEndpointPrefix = field("ManifestEndpointPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LivePreRollConfiguration:
    boto3_raw_data: "type_defs.LivePreRollConfigurationTypeDef" = dataclasses.field()

    AdDecisionServerUrl = field("AdDecisionServerUrl")
    MaxDurationSeconds = field("MaxDurationSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LivePreRollConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LivePreRollConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPrefetchScheduleRequest:
    boto3_raw_data: "type_defs.GetPrefetchScheduleRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    PlaybackConfigurationName = field("PlaybackConfigurationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPrefetchScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPrefetchScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsPlaylistSettingsOutput:
    boto3_raw_data: "type_defs.HlsPlaylistSettingsOutputTypeDef" = dataclasses.field()

    ManifestWindowSeconds = field("ManifestWindowSeconds")
    AdMarkupType = field("AdMarkupType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsPlaylistSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsPlaylistSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsPlaylistSettings:
    boto3_raw_data: "type_defs.HlsPlaylistSettingsTypeDef" = dataclasses.field()

    ManifestWindowSeconds = field("ManifestWindowSeconds")
    AdMarkupType = field("AdMarkupType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsPlaylistSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsPlaylistSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlertsRequest:
    boto3_raw_data: "type_defs.ListAlertsRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAlertsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlertsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsRequest:
    boto3_raw_data: "type_defs.ListChannelsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLiveSourcesRequest:
    boto3_raw_data: "type_defs.ListLiveSourcesRequestTypeDef" = dataclasses.field()

    SourceLocationName = field("SourceLocationName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLiveSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLiveSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlaybackConfigurationsRequest:
    boto3_raw_data: "type_defs.ListPlaybackConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPlaybackConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlaybackConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrefetchSchedulesRequest:
    boto3_raw_data: "type_defs.ListPrefetchSchedulesRequestTypeDef" = (
        dataclasses.field()
    )

    PlaybackConfigurationName = field("PlaybackConfigurationName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ScheduleType = field("ScheduleType")
    StreamId = field("StreamId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPrefetchSchedulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrefetchSchedulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSourceLocationsRequest:
    boto3_raw_data: "type_defs.ListSourceLocationsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSourceLocationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSourceLocationsRequestTypeDef"]
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
class ListVodSourcesRequest:
    boto3_raw_data: "type_defs.ListVodSourcesRequestTypeDef" = dataclasses.field()

    SourceLocationName = field("SourceLocationName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVodSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVodSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManifestServiceInteractionLog:
    boto3_raw_data: "type_defs.ManifestServiceInteractionLogTypeDef" = (
        dataclasses.field()
    )

    ExcludeEventTypes = field("ExcludeEventTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ManifestServiceInteractionLogTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManifestServiceInteractionLogTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficShapingRetrievalWindow:
    boto3_raw_data: "type_defs.TrafficShapingRetrievalWindowTypeDef" = (
        dataclasses.field()
    )

    RetrievalWindowDurationSeconds = field("RetrievalWindowDurationSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TrafficShapingRetrievalWindowTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrafficShapingRetrievalWindowTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutChannelPolicyRequest:
    boto3_raw_data: "type_defs.PutChannelPolicyRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutChannelPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutChannelPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleAdBreak:
    boto3_raw_data: "type_defs.ScheduleAdBreakTypeDef" = dataclasses.field()

    ApproximateDurationSeconds = field("ApproximateDurationSeconds")
    ApproximateStartTime = field("ApproximateStartTime")
    SourceLocationName = field("SourceLocationName")
    VodSourceName = field("VodSourceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleAdBreakTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleAdBreakTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Transition:
    boto3_raw_data: "type_defs.TransitionTypeDef" = dataclasses.field()

    RelativePosition = field("RelativePosition")
    Type = field("Type")
    DurationMillis = field("DurationMillis")
    RelativeProgram = field("RelativeProgram")
    ScheduledStartTimeMillis = field("ScheduledStartTimeMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransitionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentationDescriptor:
    boto3_raw_data: "type_defs.SegmentationDescriptorTypeDef" = dataclasses.field()

    SegmentationEventId = field("SegmentationEventId")
    SegmentationUpidType = field("SegmentationUpidType")
    SegmentationUpid = field("SegmentationUpid")
    SegmentationTypeId = field("SegmentationTypeId")
    SegmentNum = field("SegmentNum")
    SegmentsExpected = field("SegmentsExpected")
    SubSegmentNum = field("SubSegmentNum")
    SubSegmentsExpected = field("SubSegmentsExpected")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentationDescriptorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentationDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChannelRequest:
    boto3_raw_data: "type_defs.StartChannelRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopChannelRequest:
    boto3_raw_data: "type_defs.StopChannelRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopChannelRequestTypeDef"]
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
class UpdateProgramTransition:
    boto3_raw_data: "type_defs.UpdateProgramTransitionTypeDef" = dataclasses.field()

    ScheduledStartTimeMillis = field("ScheduledStartTimeMillis")
    DurationMillis = field("DurationMillis")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProgramTransitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProgramTransitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessConfiguration:
    boto3_raw_data: "type_defs.AccessConfigurationTypeDef" = dataclasses.field()

    AccessType = field("AccessType")

    @cached_property
    def SecretsManagerAccessTokenConfiguration(self):  # pragma: no cover
        return SecretsManagerAccessTokenConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerAccessTokenConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManifestProcessingRules:
    boto3_raw_data: "type_defs.ManifestProcessingRulesTypeDef" = dataclasses.field()

    @cached_property
    def AdMarkerPassthrough(self):  # pragma: no cover
        return AdMarkerPassthrough.make_one(self.boto3_raw_data["AdMarkerPassthrough"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManifestProcessingRulesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManifestProcessingRulesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrefetchConsumptionOutput:
    boto3_raw_data: "type_defs.PrefetchConsumptionOutputTypeDef" = dataclasses.field()

    EndTime = field("EndTime")

    @cached_property
    def AvailMatchingCriteria(self):  # pragma: no cover
        return AvailMatchingCriteria.make_many(
            self.boto3_raw_data["AvailMatchingCriteria"]
        )

    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrefetchConsumptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrefetchConsumptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurringConsumptionOutput:
    boto3_raw_data: "type_defs.RecurringConsumptionOutputTypeDef" = dataclasses.field()

    RetrievedAdExpirationSeconds = field("RetrievedAdExpirationSeconds")

    @cached_property
    def AvailMatchingCriteria(self):  # pragma: no cover
        return AvailMatchingCriteria.make_many(
            self.boto3_raw_data["AvailMatchingCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecurringConsumptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecurringConsumptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurringConsumption:
    boto3_raw_data: "type_defs.RecurringConsumptionTypeDef" = dataclasses.field()

    RetrievedAdExpirationSeconds = field("RetrievedAdExpirationSeconds")

    @cached_property
    def AvailMatchingCriteria(self):  # pragma: no cover
        return AvailMatchingCriteria.make_many(
            self.boto3_raw_data["AvailMatchingCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecurringConsumptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecurringConsumptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigureLogsForChannelResponse:
    boto3_raw_data: "type_defs.ConfigureLogsForChannelResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelName = field("ChannelName")
    LogTypes = field("LogTypes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfigureLogsForChannelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigureLogsForChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelPolicyResponse:
    boto3_raw_data: "type_defs.GetChannelPolicyResponseTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlertsResponse:
    boto3_raw_data: "type_defs.ListAlertsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Alert.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAlertsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlertsResponseTypeDef"]
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
class ConfigureLogsForPlaybackConfigurationResponse:
    boto3_raw_data: "type_defs.ConfigureLogsForPlaybackConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    PercentEnabled = field("PercentEnabled")
    PlaybackConfigurationName = field("PlaybackConfigurationName")
    EnabledLoggingStrategies = field("EnabledLoggingStrategies")

    @cached_property
    def AdsInteractionLog(self):  # pragma: no cover
        return AdsInteractionLogOutput.make_one(
            self.boto3_raw_data["AdsInteractionLog"]
        )

    @cached_property
    def ManifestServiceInteractionLog(self):  # pragma: no cover
        return ManifestServiceInteractionLogOutput.make_one(
            self.boto3_raw_data["ManifestServiceInteractionLog"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfigureLogsForPlaybackConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigureLogsForPlaybackConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogConfiguration:
    boto3_raw_data: "type_defs.LogConfigurationTypeDef" = dataclasses.field()

    PercentEnabled = field("PercentEnabled")
    EnabledLoggingStrategies = field("EnabledLoggingStrategies")

    @cached_property
    def AdsInteractionLog(self):  # pragma: no cover
        return AdsInteractionLogOutput.make_one(
            self.boto3_raw_data["AdsInteractionLog"]
        )

    @cached_property
    def ManifestServiceInteractionLog(self):  # pragma: no cover
        return ManifestServiceInteractionLogOutput.make_one(
            self.boto3_raw_data["ManifestServiceInteractionLog"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLiveSourceRequest:
    boto3_raw_data: "type_defs.CreateLiveSourceRequestTypeDef" = dataclasses.field()

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    LiveSourceName = field("LiveSourceName")
    SourceLocationName = field("SourceLocationName")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLiveSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLiveSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLiveSourceResponse:
    boto3_raw_data: "type_defs.CreateLiveSourceResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    LastModifiedTime = field("LastModifiedTime")
    LiveSourceName = field("LiveSourceName")
    SourceLocationName = field("SourceLocationName")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLiveSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLiveSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVodSourceRequest:
    boto3_raw_data: "type_defs.CreateVodSourceRequestTypeDef" = dataclasses.field()

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    SourceLocationName = field("SourceLocationName")
    VodSourceName = field("VodSourceName")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVodSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVodSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVodSourceResponse:
    boto3_raw_data: "type_defs.CreateVodSourceResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    LastModifiedTime = field("LastModifiedTime")
    SourceLocationName = field("SourceLocationName")
    Tags = field("Tags")
    VodSourceName = field("VodSourceName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVodSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVodSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLiveSourceResponse:
    boto3_raw_data: "type_defs.DescribeLiveSourceResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    LastModifiedTime = field("LastModifiedTime")
    LiveSourceName = field("LiveSourceName")
    SourceLocationName = field("SourceLocationName")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLiveSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLiveSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVodSourceResponse:
    boto3_raw_data: "type_defs.DescribeVodSourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def AdBreakOpportunities(self):  # pragma: no cover
        return AdBreakOpportunity.make_many(self.boto3_raw_data["AdBreakOpportunities"])

    Arn = field("Arn")
    CreationTime = field("CreationTime")

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    LastModifiedTime = field("LastModifiedTime")
    SourceLocationName = field("SourceLocationName")
    Tags = field("Tags")
    VodSourceName = field("VodSourceName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVodSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVodSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveSource:
    boto3_raw_data: "type_defs.LiveSourceTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    LiveSourceName = field("LiveSourceName")
    SourceLocationName = field("SourceLocationName")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LiveSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LiveSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLiveSourceRequest:
    boto3_raw_data: "type_defs.UpdateLiveSourceRequestTypeDef" = dataclasses.field()

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    LiveSourceName = field("LiveSourceName")
    SourceLocationName = field("SourceLocationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLiveSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLiveSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLiveSourceResponse:
    boto3_raw_data: "type_defs.UpdateLiveSourceResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    LastModifiedTime = field("LastModifiedTime")
    LiveSourceName = field("LiveSourceName")
    SourceLocationName = field("SourceLocationName")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLiveSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLiveSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVodSourceRequest:
    boto3_raw_data: "type_defs.UpdateVodSourceRequestTypeDef" = dataclasses.field()

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    SourceLocationName = field("SourceLocationName")
    VodSourceName = field("VodSourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVodSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVodSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVodSourceResponse:
    boto3_raw_data: "type_defs.UpdateVodSourceResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    LastModifiedTime = field("LastModifiedTime")
    SourceLocationName = field("SourceLocationName")
    Tags = field("Tags")
    VodSourceName = field("VodSourceName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVodSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVodSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VodSource:
    boto3_raw_data: "type_defs.VodSourceTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def HttpPackageConfigurations(self):  # pragma: no cover
        return HttpPackageConfiguration.make_many(
            self.boto3_raw_data["HttpPackageConfigurations"]
        )

    SourceLocationName = field("SourceLocationName")
    VodSourceName = field("VodSourceName")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VodSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VodSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelScheduleRequestPaginate:
    boto3_raw_data: "type_defs.GetChannelScheduleRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ChannelName = field("ChannelName")
    DurationMinutes = field("DurationMinutes")
    Audience = field("Audience")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetChannelScheduleRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelScheduleRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlertsRequestPaginate:
    boto3_raw_data: "type_defs.ListAlertsRequestPaginateTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAlertsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlertsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsRequestPaginate:
    boto3_raw_data: "type_defs.ListChannelsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLiveSourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListLiveSourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SourceLocationName = field("SourceLocationName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLiveSourcesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLiveSourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlaybackConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListPlaybackConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPlaybackConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlaybackConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrefetchSchedulesRequestPaginate:
    boto3_raw_data: "type_defs.ListPrefetchSchedulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PlaybackConfigurationName = field("PlaybackConfigurationName")
    ScheduleType = field("ScheduleType")
    StreamId = field("StreamId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPrefetchSchedulesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrefetchSchedulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSourceLocationsRequestPaginate:
    boto3_raw_data: "type_defs.ListSourceLocationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSourceLocationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSourceLocationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVodSourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListVodSourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SourceLocationName = field("SourceLocationName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVodSourcesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVodSourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseOutputItem:
    boto3_raw_data: "type_defs.ResponseOutputItemTypeDef" = dataclasses.field()

    ManifestName = field("ManifestName")
    PlaybackUrl = field("PlaybackUrl")
    SourceGroup = field("SourceGroup")

    @cached_property
    def DashPlaylistSettings(self):  # pragma: no cover
        return DashPlaylistSettings.make_one(
            self.boto3_raw_data["DashPlaylistSettings"]
        )

    @cached_property
    def HlsPlaylistSettings(self):  # pragma: no cover
        return HlsPlaylistSettingsOutput.make_one(
            self.boto3_raw_data["HlsPlaylistSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseOutputItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseOutputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrefetchConsumption:
    boto3_raw_data: "type_defs.PrefetchConsumptionTypeDef" = dataclasses.field()

    EndTime = field("EndTime")

    @cached_property
    def AvailMatchingCriteria(self):  # pragma: no cover
        return AvailMatchingCriteria.make_many(
            self.boto3_raw_data["AvailMatchingCriteria"]
        )

    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrefetchConsumptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrefetchConsumptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrefetchRetrievalOutput:
    boto3_raw_data: "type_defs.PrefetchRetrievalOutputTypeDef" = dataclasses.field()

    EndTime = field("EndTime")
    DynamicVariables = field("DynamicVariables")
    StartTime = field("StartTime")
    TrafficShapingType = field("TrafficShapingType")

    @cached_property
    def TrafficShapingRetrievalWindow(self):  # pragma: no cover
        return TrafficShapingRetrievalWindow.make_one(
            self.boto3_raw_data["TrafficShapingRetrievalWindow"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrefetchRetrievalOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrefetchRetrievalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrefetchRetrieval:
    boto3_raw_data: "type_defs.PrefetchRetrievalTypeDef" = dataclasses.field()

    EndTime = field("EndTime")
    DynamicVariables = field("DynamicVariables")
    StartTime = field("StartTime")
    TrafficShapingType = field("TrafficShapingType")

    @cached_property
    def TrafficShapingRetrievalWindow(self):  # pragma: no cover
        return TrafficShapingRetrievalWindow.make_one(
            self.boto3_raw_data["TrafficShapingRetrievalWindow"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrefetchRetrievalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrefetchRetrievalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurringRetrievalOutput:
    boto3_raw_data: "type_defs.RecurringRetrievalOutputTypeDef" = dataclasses.field()

    DynamicVariables = field("DynamicVariables")
    DelayAfterAvailEndSeconds = field("DelayAfterAvailEndSeconds")
    TrafficShapingType = field("TrafficShapingType")

    @cached_property
    def TrafficShapingRetrievalWindow(self):  # pragma: no cover
        return TrafficShapingRetrievalWindow.make_one(
            self.boto3_raw_data["TrafficShapingRetrievalWindow"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecurringRetrievalOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecurringRetrievalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurringRetrieval:
    boto3_raw_data: "type_defs.RecurringRetrievalTypeDef" = dataclasses.field()

    DynamicVariables = field("DynamicVariables")
    DelayAfterAvailEndSeconds = field("DelayAfterAvailEndSeconds")
    TrafficShapingType = field("TrafficShapingType")

    @cached_property
    def TrafficShapingRetrievalWindow(self):  # pragma: no cover
        return TrafficShapingRetrievalWindow.make_one(
            self.boto3_raw_data["TrafficShapingRetrievalWindow"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecurringRetrievalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecurringRetrievalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleEntry:
    boto3_raw_data: "type_defs.ScheduleEntryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    ProgramName = field("ProgramName")
    SourceLocationName = field("SourceLocationName")
    ApproximateDurationSeconds = field("ApproximateDurationSeconds")
    ApproximateStartTime = field("ApproximateStartTime")
    LiveSourceName = field("LiveSourceName")

    @cached_property
    def ScheduleAdBreaks(self):  # pragma: no cover
        return ScheduleAdBreak.make_many(self.boto3_raw_data["ScheduleAdBreaks"])

    ScheduleEntryType = field("ScheduleEntryType")
    VodSourceName = field("VodSourceName")
    Audiences = field("Audiences")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleConfiguration:
    boto3_raw_data: "type_defs.ScheduleConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def Transition(self):  # pragma: no cover
        return Transition.make_one(self.boto3_raw_data["Transition"])

    @cached_property
    def ClipRange(self):  # pragma: no cover
        return ClipRange.make_one(self.boto3_raw_data["ClipRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduleConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSignalMessageOutput:
    boto3_raw_data: "type_defs.TimeSignalMessageOutputTypeDef" = dataclasses.field()

    @cached_property
    def SegmentationDescriptors(self):  # pragma: no cover
        return SegmentationDescriptor.make_many(
            self.boto3_raw_data["SegmentationDescriptors"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSignalMessageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSignalMessageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSignalMessage:
    boto3_raw_data: "type_defs.TimeSignalMessageTypeDef" = dataclasses.field()

    @cached_property
    def SegmentationDescriptors(self):  # pragma: no cover
        return SegmentationDescriptor.make_many(
            self.boto3_raw_data["SegmentationDescriptors"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeSignalMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSignalMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProgramScheduleConfiguration:
    boto3_raw_data: "type_defs.UpdateProgramScheduleConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Transition(self):  # pragma: no cover
        return UpdateProgramTransition.make_one(self.boto3_raw_data["Transition"])

    @cached_property
    def ClipRange(self):  # pragma: no cover
        return ClipRange.make_one(self.boto3_raw_data["ClipRange"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateProgramScheduleConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProgramScheduleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSourceLocationRequest:
    boto3_raw_data: "type_defs.CreateSourceLocationRequestTypeDef" = dataclasses.field()

    @cached_property
    def HttpConfiguration(self):  # pragma: no cover
        return HttpConfiguration.make_one(self.boto3_raw_data["HttpConfiguration"])

    SourceLocationName = field("SourceLocationName")

    @cached_property
    def AccessConfiguration(self):  # pragma: no cover
        return AccessConfiguration.make_one(self.boto3_raw_data["AccessConfiguration"])

    @cached_property
    def DefaultSegmentDeliveryConfiguration(self):  # pragma: no cover
        return DefaultSegmentDeliveryConfiguration.make_one(
            self.boto3_raw_data["DefaultSegmentDeliveryConfiguration"]
        )

    @cached_property
    def SegmentDeliveryConfigurations(self):  # pragma: no cover
        return SegmentDeliveryConfiguration.make_many(
            self.boto3_raw_data["SegmentDeliveryConfigurations"]
        )

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSourceLocationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSourceLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSourceLocationResponse:
    boto3_raw_data: "type_defs.CreateSourceLocationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessConfiguration(self):  # pragma: no cover
        return AccessConfiguration.make_one(self.boto3_raw_data["AccessConfiguration"])

    Arn = field("Arn")
    CreationTime = field("CreationTime")

    @cached_property
    def DefaultSegmentDeliveryConfiguration(self):  # pragma: no cover
        return DefaultSegmentDeliveryConfiguration.make_one(
            self.boto3_raw_data["DefaultSegmentDeliveryConfiguration"]
        )

    @cached_property
    def HttpConfiguration(self):  # pragma: no cover
        return HttpConfiguration.make_one(self.boto3_raw_data["HttpConfiguration"])

    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def SegmentDeliveryConfigurations(self):  # pragma: no cover
        return SegmentDeliveryConfiguration.make_many(
            self.boto3_raw_data["SegmentDeliveryConfigurations"]
        )

    SourceLocationName = field("SourceLocationName")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSourceLocationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSourceLocationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceLocationResponse:
    boto3_raw_data: "type_defs.DescribeSourceLocationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessConfiguration(self):  # pragma: no cover
        return AccessConfiguration.make_one(self.boto3_raw_data["AccessConfiguration"])

    Arn = field("Arn")
    CreationTime = field("CreationTime")

    @cached_property
    def DefaultSegmentDeliveryConfiguration(self):  # pragma: no cover
        return DefaultSegmentDeliveryConfiguration.make_one(
            self.boto3_raw_data["DefaultSegmentDeliveryConfiguration"]
        )

    @cached_property
    def HttpConfiguration(self):  # pragma: no cover
        return HttpConfiguration.make_one(self.boto3_raw_data["HttpConfiguration"])

    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def SegmentDeliveryConfigurations(self):  # pragma: no cover
        return SegmentDeliveryConfiguration.make_many(
            self.boto3_raw_data["SegmentDeliveryConfigurations"]
        )

    SourceLocationName = field("SourceLocationName")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSourceLocationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceLocationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceLocation:
    boto3_raw_data: "type_defs.SourceLocationTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def HttpConfiguration(self):  # pragma: no cover
        return HttpConfiguration.make_one(self.boto3_raw_data["HttpConfiguration"])

    SourceLocationName = field("SourceLocationName")

    @cached_property
    def AccessConfiguration(self):  # pragma: no cover
        return AccessConfiguration.make_one(self.boto3_raw_data["AccessConfiguration"])

    CreationTime = field("CreationTime")

    @cached_property
    def DefaultSegmentDeliveryConfiguration(self):  # pragma: no cover
        return DefaultSegmentDeliveryConfiguration.make_one(
            self.boto3_raw_data["DefaultSegmentDeliveryConfiguration"]
        )

    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def SegmentDeliveryConfigurations(self):  # pragma: no cover
        return SegmentDeliveryConfiguration.make_many(
            self.boto3_raw_data["SegmentDeliveryConfigurations"]
        )

    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSourceLocationRequest:
    boto3_raw_data: "type_defs.UpdateSourceLocationRequestTypeDef" = dataclasses.field()

    @cached_property
    def HttpConfiguration(self):  # pragma: no cover
        return HttpConfiguration.make_one(self.boto3_raw_data["HttpConfiguration"])

    SourceLocationName = field("SourceLocationName")

    @cached_property
    def AccessConfiguration(self):  # pragma: no cover
        return AccessConfiguration.make_one(self.boto3_raw_data["AccessConfiguration"])

    @cached_property
    def DefaultSegmentDeliveryConfiguration(self):  # pragma: no cover
        return DefaultSegmentDeliveryConfiguration.make_one(
            self.boto3_raw_data["DefaultSegmentDeliveryConfiguration"]
        )

    @cached_property
    def SegmentDeliveryConfigurations(self):  # pragma: no cover
        return SegmentDeliveryConfiguration.make_many(
            self.boto3_raw_data["SegmentDeliveryConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSourceLocationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSourceLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSourceLocationResponse:
    boto3_raw_data: "type_defs.UpdateSourceLocationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessConfiguration(self):  # pragma: no cover
        return AccessConfiguration.make_one(self.boto3_raw_data["AccessConfiguration"])

    Arn = field("Arn")
    CreationTime = field("CreationTime")

    @cached_property
    def DefaultSegmentDeliveryConfiguration(self):  # pragma: no cover
        return DefaultSegmentDeliveryConfiguration.make_one(
            self.boto3_raw_data["DefaultSegmentDeliveryConfiguration"]
        )

    @cached_property
    def HttpConfiguration(self):  # pragma: no cover
        return HttpConfiguration.make_one(self.boto3_raw_data["HttpConfiguration"])

    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def SegmentDeliveryConfigurations(self):  # pragma: no cover
        return SegmentDeliveryConfiguration.make_many(
            self.boto3_raw_data["SegmentDeliveryConfigurations"]
        )

    SourceLocationName = field("SourceLocationName")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSourceLocationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSourceLocationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPlaybackConfigurationRequest:
    boto3_raw_data: "type_defs.PutPlaybackConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    AdDecisionServerUrl = field("AdDecisionServerUrl")

    @cached_property
    def AvailSuppression(self):  # pragma: no cover
        return AvailSuppression.make_one(self.boto3_raw_data["AvailSuppression"])

    @cached_property
    def Bumper(self):  # pragma: no cover
        return Bumper.make_one(self.boto3_raw_data["Bumper"])

    @cached_property
    def CdnConfiguration(self):  # pragma: no cover
        return CdnConfiguration.make_one(self.boto3_raw_data["CdnConfiguration"])

    ConfigurationAliases = field("ConfigurationAliases")

    @cached_property
    def DashConfiguration(self):  # pragma: no cover
        return DashConfigurationForPut.make_one(
            self.boto3_raw_data["DashConfiguration"]
        )

    InsertionMode = field("InsertionMode")

    @cached_property
    def LivePreRollConfiguration(self):  # pragma: no cover
        return LivePreRollConfiguration.make_one(
            self.boto3_raw_data["LivePreRollConfiguration"]
        )

    @cached_property
    def ManifestProcessingRules(self):  # pragma: no cover
        return ManifestProcessingRules.make_one(
            self.boto3_raw_data["ManifestProcessingRules"]
        )

    PersonalizationThresholdSeconds = field("PersonalizationThresholdSeconds")
    SlateAdUrl = field("SlateAdUrl")
    Tags = field("Tags")
    TranscodeProfileName = field("TranscodeProfileName")
    VideoContentSourceUrl = field("VideoContentSourceUrl")

    @cached_property
    def AdConditioningConfiguration(self):  # pragma: no cover
        return AdConditioningConfiguration.make_one(
            self.boto3_raw_data["AdConditioningConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutPlaybackConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPlaybackConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPlaybackConfigurationResponse:
    boto3_raw_data: "type_defs.GetPlaybackConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    AdDecisionServerUrl = field("AdDecisionServerUrl")

    @cached_property
    def AvailSuppression(self):  # pragma: no cover
        return AvailSuppression.make_one(self.boto3_raw_data["AvailSuppression"])

    @cached_property
    def Bumper(self):  # pragma: no cover
        return Bumper.make_one(self.boto3_raw_data["Bumper"])

    @cached_property
    def CdnConfiguration(self):  # pragma: no cover
        return CdnConfiguration.make_one(self.boto3_raw_data["CdnConfiguration"])

    ConfigurationAliases = field("ConfigurationAliases")

    @cached_property
    def DashConfiguration(self):  # pragma: no cover
        return DashConfiguration.make_one(self.boto3_raw_data["DashConfiguration"])

    @cached_property
    def HlsConfiguration(self):  # pragma: no cover
        return HlsConfiguration.make_one(self.boto3_raw_data["HlsConfiguration"])

    InsertionMode = field("InsertionMode")

    @cached_property
    def LivePreRollConfiguration(self):  # pragma: no cover
        return LivePreRollConfiguration.make_one(
            self.boto3_raw_data["LivePreRollConfiguration"]
        )

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["LogConfiguration"])

    @cached_property
    def ManifestProcessingRules(self):  # pragma: no cover
        return ManifestProcessingRules.make_one(
            self.boto3_raw_data["ManifestProcessingRules"]
        )

    Name = field("Name")
    PersonalizationThresholdSeconds = field("PersonalizationThresholdSeconds")
    PlaybackConfigurationArn = field("PlaybackConfigurationArn")
    PlaybackEndpointPrefix = field("PlaybackEndpointPrefix")
    SessionInitializationEndpointPrefix = field("SessionInitializationEndpointPrefix")
    SlateAdUrl = field("SlateAdUrl")
    Tags = field("Tags")
    TranscodeProfileName = field("TranscodeProfileName")
    VideoContentSourceUrl = field("VideoContentSourceUrl")

    @cached_property
    def AdConditioningConfiguration(self):  # pragma: no cover
        return AdConditioningConfiguration.make_one(
            self.boto3_raw_data["AdConditioningConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPlaybackConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPlaybackConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlaybackConfiguration:
    boto3_raw_data: "type_defs.PlaybackConfigurationTypeDef" = dataclasses.field()

    AdDecisionServerUrl = field("AdDecisionServerUrl")

    @cached_property
    def AvailSuppression(self):  # pragma: no cover
        return AvailSuppression.make_one(self.boto3_raw_data["AvailSuppression"])

    @cached_property
    def Bumper(self):  # pragma: no cover
        return Bumper.make_one(self.boto3_raw_data["Bumper"])

    @cached_property
    def CdnConfiguration(self):  # pragma: no cover
        return CdnConfiguration.make_one(self.boto3_raw_data["CdnConfiguration"])

    ConfigurationAliases = field("ConfigurationAliases")

    @cached_property
    def DashConfiguration(self):  # pragma: no cover
        return DashConfiguration.make_one(self.boto3_raw_data["DashConfiguration"])

    @cached_property
    def HlsConfiguration(self):  # pragma: no cover
        return HlsConfiguration.make_one(self.boto3_raw_data["HlsConfiguration"])

    InsertionMode = field("InsertionMode")

    @cached_property
    def LivePreRollConfiguration(self):  # pragma: no cover
        return LivePreRollConfiguration.make_one(
            self.boto3_raw_data["LivePreRollConfiguration"]
        )

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["LogConfiguration"])

    @cached_property
    def ManifestProcessingRules(self):  # pragma: no cover
        return ManifestProcessingRules.make_one(
            self.boto3_raw_data["ManifestProcessingRules"]
        )

    Name = field("Name")
    PersonalizationThresholdSeconds = field("PersonalizationThresholdSeconds")
    PlaybackConfigurationArn = field("PlaybackConfigurationArn")
    PlaybackEndpointPrefix = field("PlaybackEndpointPrefix")
    SessionInitializationEndpointPrefix = field("SessionInitializationEndpointPrefix")
    SlateAdUrl = field("SlateAdUrl")
    Tags = field("Tags")
    TranscodeProfileName = field("TranscodeProfileName")
    VideoContentSourceUrl = field("VideoContentSourceUrl")

    @cached_property
    def AdConditioningConfiguration(self):  # pragma: no cover
        return AdConditioningConfiguration.make_one(
            self.boto3_raw_data["AdConditioningConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlaybackConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlaybackConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPlaybackConfigurationResponse:
    boto3_raw_data: "type_defs.PutPlaybackConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    AdDecisionServerUrl = field("AdDecisionServerUrl")

    @cached_property
    def AvailSuppression(self):  # pragma: no cover
        return AvailSuppression.make_one(self.boto3_raw_data["AvailSuppression"])

    @cached_property
    def Bumper(self):  # pragma: no cover
        return Bumper.make_one(self.boto3_raw_data["Bumper"])

    @cached_property
    def CdnConfiguration(self):  # pragma: no cover
        return CdnConfiguration.make_one(self.boto3_raw_data["CdnConfiguration"])

    ConfigurationAliases = field("ConfigurationAliases")

    @cached_property
    def DashConfiguration(self):  # pragma: no cover
        return DashConfiguration.make_one(self.boto3_raw_data["DashConfiguration"])

    @cached_property
    def HlsConfiguration(self):  # pragma: no cover
        return HlsConfiguration.make_one(self.boto3_raw_data["HlsConfiguration"])

    InsertionMode = field("InsertionMode")

    @cached_property
    def LivePreRollConfiguration(self):  # pragma: no cover
        return LivePreRollConfiguration.make_one(
            self.boto3_raw_data["LivePreRollConfiguration"]
        )

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["LogConfiguration"])

    @cached_property
    def ManifestProcessingRules(self):  # pragma: no cover
        return ManifestProcessingRules.make_one(
            self.boto3_raw_data["ManifestProcessingRules"]
        )

    Name = field("Name")
    PersonalizationThresholdSeconds = field("PersonalizationThresholdSeconds")
    PlaybackConfigurationArn = field("PlaybackConfigurationArn")
    PlaybackEndpointPrefix = field("PlaybackEndpointPrefix")
    SessionInitializationEndpointPrefix = field("SessionInitializationEndpointPrefix")
    SlateAdUrl = field("SlateAdUrl")
    Tags = field("Tags")
    TranscodeProfileName = field("TranscodeProfileName")
    VideoContentSourceUrl = field("VideoContentSourceUrl")

    @cached_property
    def AdConditioningConfiguration(self):  # pragma: no cover
        return AdConditioningConfiguration.make_one(
            self.boto3_raw_data["AdConditioningConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutPlaybackConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPlaybackConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLiveSourcesResponse:
    boto3_raw_data: "type_defs.ListLiveSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return LiveSource.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLiveSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLiveSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVodSourcesResponse:
    boto3_raw_data: "type_defs.ListVodSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return VodSource.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVodSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVodSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Channel:
    boto3_raw_data: "type_defs.ChannelTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    ChannelState = field("ChannelState")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return ResponseOutputItem.make_many(self.boto3_raw_data["Outputs"])

    PlaybackMode = field("PlaybackMode")
    Tier = field("Tier")

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LogConfigurationForChannel.make_one(
            self.boto3_raw_data["LogConfiguration"]
        )

    CreationTime = field("CreationTime")

    @cached_property
    def FillerSlate(self):  # pragma: no cover
        return SlateSource.make_one(self.boto3_raw_data["FillerSlate"])

    LastModifiedTime = field("LastModifiedTime")
    Tags = field("Tags")
    Audiences = field("Audiences")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelResponse:
    boto3_raw_data: "type_defs.CreateChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    ChannelState = field("ChannelState")
    CreationTime = field("CreationTime")

    @cached_property
    def FillerSlate(self):  # pragma: no cover
        return SlateSource.make_one(self.boto3_raw_data["FillerSlate"])

    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return ResponseOutputItem.make_many(self.boto3_raw_data["Outputs"])

    PlaybackMode = field("PlaybackMode")
    Tags = field("Tags")
    Tier = field("Tier")

    @cached_property
    def TimeShiftConfiguration(self):  # pragma: no cover
        return TimeShiftConfiguration.make_one(
            self.boto3_raw_data["TimeShiftConfiguration"]
        )

    Audiences = field("Audiences")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelResponse:
    boto3_raw_data: "type_defs.DescribeChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    ChannelState = field("ChannelState")
    CreationTime = field("CreationTime")

    @cached_property
    def FillerSlate(self):  # pragma: no cover
        return SlateSource.make_one(self.boto3_raw_data["FillerSlate"])

    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return ResponseOutputItem.make_many(self.boto3_raw_data["Outputs"])

    PlaybackMode = field("PlaybackMode")
    Tags = field("Tags")
    Tier = field("Tier")

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LogConfigurationForChannel.make_one(
            self.boto3_raw_data["LogConfiguration"]
        )

    @cached_property
    def TimeShiftConfiguration(self):  # pragma: no cover
        return TimeShiftConfiguration.make_one(
            self.boto3_raw_data["TimeShiftConfiguration"]
        )

    Audiences = field("Audiences")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelResponse:
    boto3_raw_data: "type_defs.UpdateChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    ChannelState = field("ChannelState")
    CreationTime = field("CreationTime")

    @cached_property
    def FillerSlate(self):  # pragma: no cover
        return SlateSource.make_one(self.boto3_raw_data["FillerSlate"])

    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return ResponseOutputItem.make_many(self.boto3_raw_data["Outputs"])

    PlaybackMode = field("PlaybackMode")
    Tags = field("Tags")
    Tier = field("Tier")

    @cached_property
    def TimeShiftConfiguration(self):  # pragma: no cover
        return TimeShiftConfiguration.make_one(
            self.boto3_raw_data["TimeShiftConfiguration"]
        )

    Audiences = field("Audiences")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestOutputItem:
    boto3_raw_data: "type_defs.RequestOutputItemTypeDef" = dataclasses.field()

    ManifestName = field("ManifestName")
    SourceGroup = field("SourceGroup")

    @cached_property
    def DashPlaylistSettings(self):  # pragma: no cover
        return DashPlaylistSettings.make_one(
            self.boto3_raw_data["DashPlaylistSettings"]
        )

    HlsPlaylistSettings = field("HlsPlaylistSettings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequestOutputItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestOutputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigureLogsForPlaybackConfigurationRequest:
    boto3_raw_data: "type_defs.ConfigureLogsForPlaybackConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    PercentEnabled = field("PercentEnabled")
    PlaybackConfigurationName = field("PlaybackConfigurationName")
    EnabledLoggingStrategies = field("EnabledLoggingStrategies")
    AdsInteractionLog = field("AdsInteractionLog")
    ManifestServiceInteractionLog = field("ManifestServiceInteractionLog")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfigureLogsForPlaybackConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigureLogsForPlaybackConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurringPrefetchConfigurationOutput:
    boto3_raw_data: "type_defs.RecurringPrefetchConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    EndTime = field("EndTime")

    @cached_property
    def RecurringConsumption(self):  # pragma: no cover
        return RecurringConsumptionOutput.make_one(
            self.boto3_raw_data["RecurringConsumption"]
        )

    @cached_property
    def RecurringRetrieval(self):  # pragma: no cover
        return RecurringRetrievalOutput.make_one(
            self.boto3_raw_data["RecurringRetrieval"]
        )

    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecurringPrefetchConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecurringPrefetchConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurringPrefetchConfiguration:
    boto3_raw_data: "type_defs.RecurringPrefetchConfigurationTypeDef" = (
        dataclasses.field()
    )

    EndTime = field("EndTime")

    @cached_property
    def RecurringConsumption(self):  # pragma: no cover
        return RecurringConsumption.make_one(
            self.boto3_raw_data["RecurringConsumption"]
        )

    @cached_property
    def RecurringRetrieval(self):  # pragma: no cover
        return RecurringRetrieval.make_one(self.boto3_raw_data["RecurringRetrieval"])

    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RecurringPrefetchConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecurringPrefetchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelScheduleResponse:
    boto3_raw_data: "type_defs.GetChannelScheduleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ScheduleEntry.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelScheduleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelScheduleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdBreakOutput:
    boto3_raw_data: "type_defs.AdBreakOutputTypeDef" = dataclasses.field()

    OffsetMillis = field("OffsetMillis")
    MessageType = field("MessageType")

    @cached_property
    def Slate(self):  # pragma: no cover
        return SlateSource.make_one(self.boto3_raw_data["Slate"])

    @cached_property
    def SpliceInsertMessage(self):  # pragma: no cover
        return SpliceInsertMessage.make_one(self.boto3_raw_data["SpliceInsertMessage"])

    @cached_property
    def TimeSignalMessage(self):  # pragma: no cover
        return TimeSignalMessageOutput.make_one(
            self.boto3_raw_data["TimeSignalMessage"]
        )

    @cached_property
    def AdBreakMetadata(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["AdBreakMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdBreakOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdBreakOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSourceLocationsResponse:
    boto3_raw_data: "type_defs.ListSourceLocationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return SourceLocation.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSourceLocationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSourceLocationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlaybackConfigurationsResponse:
    boto3_raw_data: "type_defs.ListPlaybackConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return PlaybackConfiguration.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPlaybackConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlaybackConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsResponse:
    boto3_raw_data: "type_defs.ListChannelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Channel.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelRequest:
    boto3_raw_data: "type_defs.CreateChannelRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return RequestOutputItem.make_many(self.boto3_raw_data["Outputs"])

    PlaybackMode = field("PlaybackMode")

    @cached_property
    def FillerSlate(self):  # pragma: no cover
        return SlateSource.make_one(self.boto3_raw_data["FillerSlate"])

    Tags = field("Tags")
    Tier = field("Tier")

    @cached_property
    def TimeShiftConfiguration(self):  # pragma: no cover
        return TimeShiftConfiguration.make_one(
            self.boto3_raw_data["TimeShiftConfiguration"]
        )

    Audiences = field("Audiences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelRequest:
    boto3_raw_data: "type_defs.UpdateChannelRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return RequestOutputItem.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def FillerSlate(self):  # pragma: no cover
        return SlateSource.make_one(self.boto3_raw_data["FillerSlate"])

    @cached_property
    def TimeShiftConfiguration(self):  # pragma: no cover
        return TimeShiftConfiguration.make_one(
            self.boto3_raw_data["TimeShiftConfiguration"]
        )

    Audiences = field("Audiences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePrefetchScheduleResponse:
    boto3_raw_data: "type_defs.CreatePrefetchScheduleResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def Consumption(self):  # pragma: no cover
        return PrefetchConsumptionOutput.make_one(self.boto3_raw_data["Consumption"])

    Name = field("Name")
    PlaybackConfigurationName = field("PlaybackConfigurationName")

    @cached_property
    def Retrieval(self):  # pragma: no cover
        return PrefetchRetrievalOutput.make_one(self.boto3_raw_data["Retrieval"])

    @cached_property
    def RecurringPrefetchConfiguration(self):  # pragma: no cover
        return RecurringPrefetchConfigurationOutput.make_one(
            self.boto3_raw_data["RecurringPrefetchConfiguration"]
        )

    ScheduleType = field("ScheduleType")
    StreamId = field("StreamId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePrefetchScheduleResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePrefetchScheduleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPrefetchScheduleResponse:
    boto3_raw_data: "type_defs.GetPrefetchScheduleResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def Consumption(self):  # pragma: no cover
        return PrefetchConsumptionOutput.make_one(self.boto3_raw_data["Consumption"])

    Name = field("Name")
    PlaybackConfigurationName = field("PlaybackConfigurationName")

    @cached_property
    def Retrieval(self):  # pragma: no cover
        return PrefetchRetrievalOutput.make_one(self.boto3_raw_data["Retrieval"])

    ScheduleType = field("ScheduleType")

    @cached_property
    def RecurringPrefetchConfiguration(self):  # pragma: no cover
        return RecurringPrefetchConfigurationOutput.make_one(
            self.boto3_raw_data["RecurringPrefetchConfiguration"]
        )

    StreamId = field("StreamId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPrefetchScheduleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPrefetchScheduleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrefetchSchedule:
    boto3_raw_data: "type_defs.PrefetchScheduleTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    PlaybackConfigurationName = field("PlaybackConfigurationName")

    @cached_property
    def Consumption(self):  # pragma: no cover
        return PrefetchConsumptionOutput.make_one(self.boto3_raw_data["Consumption"])

    @cached_property
    def Retrieval(self):  # pragma: no cover
        return PrefetchRetrievalOutput.make_one(self.boto3_raw_data["Retrieval"])

    ScheduleType = field("ScheduleType")

    @cached_property
    def RecurringPrefetchConfiguration(self):  # pragma: no cover
        return RecurringPrefetchConfigurationOutput.make_one(
            self.boto3_raw_data["RecurringPrefetchConfiguration"]
        )

    StreamId = field("StreamId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrefetchScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrefetchScheduleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlternateMediaOutput:
    boto3_raw_data: "type_defs.AlternateMediaOutputTypeDef" = dataclasses.field()

    SourceLocationName = field("SourceLocationName")
    LiveSourceName = field("LiveSourceName")
    VodSourceName = field("VodSourceName")

    @cached_property
    def ClipRange(self):  # pragma: no cover
        return ClipRange.make_one(self.boto3_raw_data["ClipRange"])

    ScheduledStartTimeMillis = field("ScheduledStartTimeMillis")

    @cached_property
    def AdBreaks(self):  # pragma: no cover
        return AdBreakOutput.make_many(self.boto3_raw_data["AdBreaks"])

    DurationMillis = field("DurationMillis")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlternateMediaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlternateMediaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdBreak:
    boto3_raw_data: "type_defs.AdBreakTypeDef" = dataclasses.field()

    OffsetMillis = field("OffsetMillis")
    MessageType = field("MessageType")

    @cached_property
    def Slate(self):  # pragma: no cover
        return SlateSource.make_one(self.boto3_raw_data["Slate"])

    @cached_property
    def SpliceInsertMessage(self):  # pragma: no cover
        return SpliceInsertMessage.make_one(self.boto3_raw_data["SpliceInsertMessage"])

    TimeSignalMessage = field("TimeSignalMessage")

    @cached_property
    def AdBreakMetadata(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["AdBreakMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdBreakTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdBreakTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrefetchSchedulesResponse:
    boto3_raw_data: "type_defs.ListPrefetchSchedulesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return PrefetchSchedule.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPrefetchSchedulesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrefetchSchedulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePrefetchScheduleRequest:
    boto3_raw_data: "type_defs.CreatePrefetchScheduleRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    PlaybackConfigurationName = field("PlaybackConfigurationName")
    Consumption = field("Consumption")
    Retrieval = field("Retrieval")
    RecurringPrefetchConfiguration = field("RecurringPrefetchConfiguration")
    ScheduleType = field("ScheduleType")
    StreamId = field("StreamId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePrefetchScheduleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePrefetchScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceMediaOutput:
    boto3_raw_data: "type_defs.AudienceMediaOutputTypeDef" = dataclasses.field()

    Audience = field("Audience")

    @cached_property
    def AlternateMedia(self):  # pragma: no cover
        return AlternateMediaOutput.make_many(self.boto3_raw_data["AlternateMedia"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudienceMediaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudienceMediaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProgramResponse:
    boto3_raw_data: "type_defs.CreateProgramResponseTypeDef" = dataclasses.field()

    @cached_property
    def AdBreaks(self):  # pragma: no cover
        return AdBreakOutput.make_many(self.boto3_raw_data["AdBreaks"])

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    CreationTime = field("CreationTime")
    LiveSourceName = field("LiveSourceName")
    ProgramName = field("ProgramName")
    ScheduledStartTime = field("ScheduledStartTime")
    SourceLocationName = field("SourceLocationName")
    VodSourceName = field("VodSourceName")

    @cached_property
    def ClipRange(self):  # pragma: no cover
        return ClipRange.make_one(self.boto3_raw_data["ClipRange"])

    DurationMillis = field("DurationMillis")

    @cached_property
    def AudienceMedia(self):  # pragma: no cover
        return AudienceMediaOutput.make_many(self.boto3_raw_data["AudienceMedia"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProgramResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProgramResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProgramResponse:
    boto3_raw_data: "type_defs.DescribeProgramResponseTypeDef" = dataclasses.field()

    @cached_property
    def AdBreaks(self):  # pragma: no cover
        return AdBreakOutput.make_many(self.boto3_raw_data["AdBreaks"])

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    CreationTime = field("CreationTime")
    LiveSourceName = field("LiveSourceName")
    ProgramName = field("ProgramName")
    ScheduledStartTime = field("ScheduledStartTime")
    SourceLocationName = field("SourceLocationName")
    VodSourceName = field("VodSourceName")

    @cached_property
    def ClipRange(self):  # pragma: no cover
        return ClipRange.make_one(self.boto3_raw_data["ClipRange"])

    DurationMillis = field("DurationMillis")

    @cached_property
    def AudienceMedia(self):  # pragma: no cover
        return AudienceMediaOutput.make_many(self.boto3_raw_data["AudienceMedia"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProgramResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProgramResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProgramResponse:
    boto3_raw_data: "type_defs.UpdateProgramResponseTypeDef" = dataclasses.field()

    @cached_property
    def AdBreaks(self):  # pragma: no cover
        return AdBreakOutput.make_many(self.boto3_raw_data["AdBreaks"])

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    CreationTime = field("CreationTime")
    ProgramName = field("ProgramName")
    SourceLocationName = field("SourceLocationName")
    VodSourceName = field("VodSourceName")
    LiveSourceName = field("LiveSourceName")

    @cached_property
    def ClipRange(self):  # pragma: no cover
        return ClipRange.make_one(self.boto3_raw_data["ClipRange"])

    DurationMillis = field("DurationMillis")
    ScheduledStartTime = field("ScheduledStartTime")

    @cached_property
    def AudienceMedia(self):  # pragma: no cover
        return AudienceMediaOutput.make_many(self.boto3_raw_data["AudienceMedia"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProgramResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProgramResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlternateMedia:
    boto3_raw_data: "type_defs.AlternateMediaTypeDef" = dataclasses.field()

    SourceLocationName = field("SourceLocationName")
    LiveSourceName = field("LiveSourceName")
    VodSourceName = field("VodSourceName")

    @cached_property
    def ClipRange(self):  # pragma: no cover
        return ClipRange.make_one(self.boto3_raw_data["ClipRange"])

    ScheduledStartTimeMillis = field("ScheduledStartTimeMillis")
    AdBreaks = field("AdBreaks")
    DurationMillis = field("DurationMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlternateMediaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlternateMediaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceMedia:
    boto3_raw_data: "type_defs.AudienceMediaTypeDef" = dataclasses.field()

    Audience = field("Audience")
    AlternateMedia = field("AlternateMedia")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudienceMediaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudienceMediaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProgramRequest:
    boto3_raw_data: "type_defs.CreateProgramRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")
    ProgramName = field("ProgramName")

    @cached_property
    def ScheduleConfiguration(self):  # pragma: no cover
        return ScheduleConfiguration.make_one(
            self.boto3_raw_data["ScheduleConfiguration"]
        )

    SourceLocationName = field("SourceLocationName")
    AdBreaks = field("AdBreaks")
    LiveSourceName = field("LiveSourceName")
    VodSourceName = field("VodSourceName")
    AudienceMedia = field("AudienceMedia")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProgramRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProgramRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProgramRequest:
    boto3_raw_data: "type_defs.UpdateProgramRequestTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")
    ProgramName = field("ProgramName")

    @cached_property
    def ScheduleConfiguration(self):  # pragma: no cover
        return UpdateProgramScheduleConfiguration.make_one(
            self.boto3_raw_data["ScheduleConfiguration"]
        )

    AdBreaks = field("AdBreaks")
    AudienceMedia = field("AudienceMedia")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProgramRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProgramRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
