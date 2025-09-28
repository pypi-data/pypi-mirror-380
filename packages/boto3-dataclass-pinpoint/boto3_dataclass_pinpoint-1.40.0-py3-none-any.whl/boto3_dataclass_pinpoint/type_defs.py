# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pinpoint import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ADMChannelRequest:
    boto3_raw_data: "type_defs.ADMChannelRequestTypeDef" = dataclasses.field()

    ClientId = field("ClientId")
    ClientSecret = field("ClientSecret")
    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ADMChannelRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ADMChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ADMChannelResponse:
    boto3_raw_data: "type_defs.ADMChannelResponseTypeDef" = dataclasses.field()

    Platform = field("Platform")
    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")
    Enabled = field("Enabled")
    HasCredential = field("HasCredential")
    Id = field("Id")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ADMChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ADMChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ADMMessage:
    boto3_raw_data: "type_defs.ADMMessageTypeDef" = dataclasses.field()

    Action = field("Action")
    Body = field("Body")
    ConsolidationKey = field("ConsolidationKey")
    Data = field("Data")
    ExpiresAfter = field("ExpiresAfter")
    IconReference = field("IconReference")
    ImageIconUrl = field("ImageIconUrl")
    ImageUrl = field("ImageUrl")
    MD5 = field("MD5")
    RawContent = field("RawContent")
    SilentPush = field("SilentPush")
    SmallImageIconUrl = field("SmallImageIconUrl")
    Sound = field("Sound")
    Substitutions = field("Substitutions")
    Title = field("Title")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ADMMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ADMMessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APNSChannelRequest:
    boto3_raw_data: "type_defs.APNSChannelRequestTypeDef" = dataclasses.field()

    BundleId = field("BundleId")
    Certificate = field("Certificate")
    DefaultAuthenticationMethod = field("DefaultAuthenticationMethod")
    Enabled = field("Enabled")
    PrivateKey = field("PrivateKey")
    TeamId = field("TeamId")
    TokenKey = field("TokenKey")
    TokenKeyId = field("TokenKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.APNSChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.APNSChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APNSChannelResponse:
    boto3_raw_data: "type_defs.APNSChannelResponseTypeDef" = dataclasses.field()

    Platform = field("Platform")
    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")
    DefaultAuthenticationMethod = field("DefaultAuthenticationMethod")
    Enabled = field("Enabled")
    HasCredential = field("HasCredential")
    HasTokenKey = field("HasTokenKey")
    Id = field("Id")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.APNSChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.APNSChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APNSMessage:
    boto3_raw_data: "type_defs.APNSMessageTypeDef" = dataclasses.field()

    APNSPushType = field("APNSPushType")
    Action = field("Action")
    Badge = field("Badge")
    Body = field("Body")
    Category = field("Category")
    CollapseId = field("CollapseId")
    Data = field("Data")
    MediaUrl = field("MediaUrl")
    PreferredAuthenticationMethod = field("PreferredAuthenticationMethod")
    Priority = field("Priority")
    RawContent = field("RawContent")
    SilentPush = field("SilentPush")
    Sound = field("Sound")
    Substitutions = field("Substitutions")
    ThreadId = field("ThreadId")
    TimeToLive = field("TimeToLive")
    Title = field("Title")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.APNSMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.APNSMessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APNSPushNotificationTemplate:
    boto3_raw_data: "type_defs.APNSPushNotificationTemplateTypeDef" = (
        dataclasses.field()
    )

    Action = field("Action")
    Body = field("Body")
    MediaUrl = field("MediaUrl")
    RawContent = field("RawContent")
    Sound = field("Sound")
    Title = field("Title")
    Url = field("Url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.APNSPushNotificationTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.APNSPushNotificationTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APNSSandboxChannelRequest:
    boto3_raw_data: "type_defs.APNSSandboxChannelRequestTypeDef" = dataclasses.field()

    BundleId = field("BundleId")
    Certificate = field("Certificate")
    DefaultAuthenticationMethod = field("DefaultAuthenticationMethod")
    Enabled = field("Enabled")
    PrivateKey = field("PrivateKey")
    TeamId = field("TeamId")
    TokenKey = field("TokenKey")
    TokenKeyId = field("TokenKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.APNSSandboxChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.APNSSandboxChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APNSSandboxChannelResponse:
    boto3_raw_data: "type_defs.APNSSandboxChannelResponseTypeDef" = dataclasses.field()

    Platform = field("Platform")
    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")
    DefaultAuthenticationMethod = field("DefaultAuthenticationMethod")
    Enabled = field("Enabled")
    HasCredential = field("HasCredential")
    HasTokenKey = field("HasTokenKey")
    Id = field("Id")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.APNSSandboxChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.APNSSandboxChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APNSVoipChannelRequest:
    boto3_raw_data: "type_defs.APNSVoipChannelRequestTypeDef" = dataclasses.field()

    BundleId = field("BundleId")
    Certificate = field("Certificate")
    DefaultAuthenticationMethod = field("DefaultAuthenticationMethod")
    Enabled = field("Enabled")
    PrivateKey = field("PrivateKey")
    TeamId = field("TeamId")
    TokenKey = field("TokenKey")
    TokenKeyId = field("TokenKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.APNSVoipChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.APNSVoipChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APNSVoipChannelResponse:
    boto3_raw_data: "type_defs.APNSVoipChannelResponseTypeDef" = dataclasses.field()

    Platform = field("Platform")
    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")
    DefaultAuthenticationMethod = field("DefaultAuthenticationMethod")
    Enabled = field("Enabled")
    HasCredential = field("HasCredential")
    HasTokenKey = field("HasTokenKey")
    Id = field("Id")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.APNSVoipChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.APNSVoipChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APNSVoipSandboxChannelRequest:
    boto3_raw_data: "type_defs.APNSVoipSandboxChannelRequestTypeDef" = (
        dataclasses.field()
    )

    BundleId = field("BundleId")
    Certificate = field("Certificate")
    DefaultAuthenticationMethod = field("DefaultAuthenticationMethod")
    Enabled = field("Enabled")
    PrivateKey = field("PrivateKey")
    TeamId = field("TeamId")
    TokenKey = field("TokenKey")
    TokenKeyId = field("TokenKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.APNSVoipSandboxChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.APNSVoipSandboxChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APNSVoipSandboxChannelResponse:
    boto3_raw_data: "type_defs.APNSVoipSandboxChannelResponseTypeDef" = (
        dataclasses.field()
    )

    Platform = field("Platform")
    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")
    DefaultAuthenticationMethod = field("DefaultAuthenticationMethod")
    Enabled = field("Enabled")
    HasCredential = field("HasCredential")
    HasTokenKey = field("HasTokenKey")
    Id = field("Id")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    Version = field("Version")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.APNSVoipSandboxChannelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.APNSVoipSandboxChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityResponse:
    boto3_raw_data: "type_defs.ActivityResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    CampaignId = field("CampaignId")
    Id = field("Id")
    End = field("End")
    Result = field("Result")
    ScheduledStart = field("ScheduledStart")
    Start = field("Start")
    State = field("State")
    SuccessfulEndpointCount = field("SuccessfulEndpointCount")
    TimezonesCompletedCount = field("TimezonesCompletedCount")
    TimezonesTotalCount = field("TimezonesTotalCount")
    TotalEndpointCount = field("TotalEndpointCount")
    TreatmentId = field("TreatmentId")
    ExecutionMetrics = field("ExecutionMetrics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactCenterActivity:
    boto3_raw_data: "type_defs.ContactCenterActivityTypeDef" = dataclasses.field()

    NextActivity = field("NextActivity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactCenterActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactCenterActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoldoutActivity:
    boto3_raw_data: "type_defs.HoldoutActivityTypeDef" = dataclasses.field()

    Percentage = field("Percentage")
    NextActivity = field("NextActivity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HoldoutActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HoldoutActivityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddressConfiguration:
    boto3_raw_data: "type_defs.AddressConfigurationTypeDef" = dataclasses.field()

    BodyOverride = field("BodyOverride")
    ChannelType = field("ChannelType")
    Context = field("Context")
    RawContent = field("RawContent")
    Substitutions = field("Substitutions")
    TitleOverride = field("TitleOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddressConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddressConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AndroidPushNotificationTemplate:
    boto3_raw_data: "type_defs.AndroidPushNotificationTemplateTypeDef" = (
        dataclasses.field()
    )

    Action = field("Action")
    Body = field("Body")
    ImageIconUrl = field("ImageIconUrl")
    ImageUrl = field("ImageUrl")
    RawContent = field("RawContent")
    SmallImageIconUrl = field("SmallImageIconUrl")
    Sound = field("Sound")
    Title = field("Title")
    Url = field("Url")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AndroidPushNotificationTemplateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AndroidPushNotificationTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationResponse:
    boto3_raw_data: "type_defs.ApplicationResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Name = field("Name")
    tags = field("tags")
    CreationDate = field("CreationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyTimeframeCap:
    boto3_raw_data: "type_defs.JourneyTimeframeCapTypeDef" = dataclasses.field()

    Cap = field("Cap")
    Days = field("Days")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JourneyTimeframeCapTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyTimeframeCapTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignHook:
    boto3_raw_data: "type_defs.CampaignHookTypeDef" = dataclasses.field()

    LambdaFunctionName = field("LambdaFunctionName")
    Mode = field("Mode")
    WebUrl = field("WebUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignHookTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignHookTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignLimits:
    boto3_raw_data: "type_defs.CampaignLimitsTypeDef" = dataclasses.field()

    Daily = field("Daily")
    MaximumDuration = field("MaximumDuration")
    MessagesPerSecond = field("MessagesPerSecond")
    Total = field("Total")
    Session = field("Session")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignLimitsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuietTime:
    boto3_raw_data: "type_defs.QuietTimeTypeDef" = dataclasses.field()

    End = field("End")
    Start = field("Start")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QuietTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QuietTimeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeDimensionOutput:
    boto3_raw_data: "type_defs.AttributeDimensionOutputTypeDef" = dataclasses.field()

    Values = field("Values")
    AttributeType = field("AttributeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeDimensionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeDimension:
    boto3_raw_data: "type_defs.AttributeDimensionTypeDef" = dataclasses.field()

    Values = field("Values")
    AttributeType = field("AttributeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeDimensionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributesResource:
    boto3_raw_data: "type_defs.AttributesResourceTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    AttributeType = field("AttributeType")
    Attributes = field("Attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributesResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributesResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaiduChannelRequest:
    boto3_raw_data: "type_defs.BaiduChannelRequestTypeDef" = dataclasses.field()

    ApiKey = field("ApiKey")
    SecretKey = field("SecretKey")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BaiduChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BaiduChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaiduChannelResponse:
    boto3_raw_data: "type_defs.BaiduChannelResponseTypeDef" = dataclasses.field()

    Credential = field("Credential")
    Platform = field("Platform")
    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")
    Enabled = field("Enabled")
    HasCredential = field("HasCredential")
    Id = field("Id")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BaiduChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BaiduChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaiduMessage:
    boto3_raw_data: "type_defs.BaiduMessageTypeDef" = dataclasses.field()

    Action = field("Action")
    Body = field("Body")
    Data = field("Data")
    IconReference = field("IconReference")
    ImageIconUrl = field("ImageIconUrl")
    ImageUrl = field("ImageUrl")
    RawContent = field("RawContent")
    SilentPush = field("SilentPush")
    SmallImageIconUrl = field("SmallImageIconUrl")
    Sound = field("Sound")
    Substitutions = field("Substitutions")
    TimeToLive = field("TimeToLive")
    Title = field("Title")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BaiduMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BaiduMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignCustomMessage:
    boto3_raw_data: "type_defs.CampaignCustomMessageTypeDef" = dataclasses.field()

    Data = field("Data")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignCustomMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignCustomMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageHeader:
    boto3_raw_data: "type_defs.MessageHeaderTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageHeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageHeaderTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignState:
    boto3_raw_data: "type_defs.CampaignStateTypeDef" = dataclasses.field()

    CampaignStatus = field("CampaignStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDeliveryConfigurationOutput:
    boto3_raw_data: "type_defs.CustomDeliveryConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    DeliveryUri = field("DeliveryUri")
    EndpointTypes = field("EndpointTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomDeliveryConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDeliveryConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignSmsMessage:
    boto3_raw_data: "type_defs.CampaignSmsMessageTypeDef" = dataclasses.field()

    Body = field("Body")
    MessageType = field("MessageType")
    OriginationNumber = field("OriginationNumber")
    SenderId = field("SenderId")
    EntityId = field("EntityId")
    TemplateId = field("TemplateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignSmsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignSmsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelResponse:
    boto3_raw_data: "type_defs.ChannelResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")
    Enabled = field("Enabled")
    HasCredential = field("HasCredential")
    Id = field("Id")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClosedDaysRule:
    boto3_raw_data: "type_defs.ClosedDaysRuleTypeDef" = dataclasses.field()

    Name = field("Name")
    StartDateTime = field("StartDateTime")
    EndDateTime = field("EndDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClosedDaysRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClosedDaysRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaitTime:
    boto3_raw_data: "type_defs.WaitTimeTypeDef" = dataclasses.field()

    WaitFor = field("WaitFor")
    WaitUntil = field("WaitUntil")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaitTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaitTimeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationRequest:
    boto3_raw_data: "type_defs.CreateApplicationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationRequestTypeDef"]
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
class CreateTemplateMessageBody:
    boto3_raw_data: "type_defs.CreateTemplateMessageBodyTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Message = field("Message")
    RequestID = field("RequestID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTemplateMessageBodyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateMessageBodyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportJobRequest:
    boto3_raw_data: "type_defs.ExportJobRequestTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    S3UrlPrefix = field("S3UrlPrefix")
    SegmentId = field("SegmentId")
    SegmentVersion = field("SegmentVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportJobRequest:
    boto3_raw_data: "type_defs.ImportJobRequestTypeDef" = dataclasses.field()

    Format = field("Format")
    RoleArn = field("RoleArn")
    S3Url = field("S3Url")
    DefineSegment = field("DefineSegment")
    ExternalId = field("ExternalId")
    RegisterEndpoints = field("RegisterEndpoints")
    SegmentId = field("SegmentId")
    SegmentName = field("SegmentName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateCreateMessageBody:
    boto3_raw_data: "type_defs.TemplateCreateMessageBodyTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Message = field("Message")
    RequestID = field("RequestID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateCreateMessageBodyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateCreateMessageBodyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRecommenderConfiguration:
    boto3_raw_data: "type_defs.CreateRecommenderConfigurationTypeDef" = (
        dataclasses.field()
    )

    RecommendationProviderRoleArn = field("RecommendationProviderRoleArn")
    RecommendationProviderUri = field("RecommendationProviderUri")
    Attributes = field("Attributes")
    Description = field("Description")
    Name = field("Name")
    RecommendationProviderIdType = field("RecommendationProviderIdType")
    RecommendationTransformerUri = field("RecommendationTransformerUri")
    RecommendationsDisplayName = field("RecommendationsDisplayName")
    RecommendationsPerMessage = field("RecommendationsPerMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRecommenderConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecommenderConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommenderConfigurationResponse:
    boto3_raw_data: "type_defs.RecommenderConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    CreationDate = field("CreationDate")
    Id = field("Id")
    LastModifiedDate = field("LastModifiedDate")
    RecommendationProviderRoleArn = field("RecommendationProviderRoleArn")
    RecommendationProviderUri = field("RecommendationProviderUri")
    Attributes = field("Attributes")
    Description = field("Description")
    Name = field("Name")
    RecommendationProviderIdType = field("RecommendationProviderIdType")
    RecommendationTransformerUri = field("RecommendationTransformerUri")
    RecommendationsDisplayName = field("RecommendationsDisplayName")
    RecommendationsPerMessage = field("RecommendationsPerMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RecommenderConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommenderConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSTemplateRequest:
    boto3_raw_data: "type_defs.SMSTemplateRequestTypeDef" = dataclasses.field()

    Body = field("Body")
    DefaultSubstitutions = field("DefaultSubstitutions")
    RecommenderId = field("RecommenderId")
    tags = field("tags")
    TemplateDescription = field("TemplateDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SMSTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMSTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceTemplateRequest:
    boto3_raw_data: "type_defs.VoiceTemplateRequestTypeDef" = dataclasses.field()

    Body = field("Body")
    DefaultSubstitutions = field("DefaultSubstitutions")
    LanguageCode = field("LanguageCode")
    tags = field("tags")
    TemplateDescription = field("TemplateDescription")
    VoiceId = field("VoiceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDeliveryConfiguration:
    boto3_raw_data: "type_defs.CustomDeliveryConfigurationTypeDef" = dataclasses.field()

    DeliveryUri = field("DeliveryUri")
    EndpointTypes = field("EndpointTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomDeliveryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDeliveryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyCustomMessage:
    boto3_raw_data: "type_defs.JourneyCustomMessageTypeDef" = dataclasses.field()

    Data = field("Data")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JourneyCustomMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyCustomMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultButtonConfiguration:
    boto3_raw_data: "type_defs.DefaultButtonConfigurationTypeDef" = dataclasses.field()

    ButtonAction = field("ButtonAction")
    Text = field("Text")
    BackgroundColor = field("BackgroundColor")
    BorderRadius = field("BorderRadius")
    Link = field("Link")
    TextColor = field("TextColor")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefaultButtonConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultButtonConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultMessage:
    boto3_raw_data: "type_defs.DefaultMessageTypeDef" = dataclasses.field()

    Body = field("Body")
    Substitutions = field("Substitutions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DefaultMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DefaultMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultPushNotificationMessage:
    boto3_raw_data: "type_defs.DefaultPushNotificationMessageTypeDef" = (
        dataclasses.field()
    )

    Action = field("Action")
    Body = field("Body")
    Data = field("Data")
    SilentPush = field("SilentPush")
    Substitutions = field("Substitutions")
    Title = field("Title")
    Url = field("Url")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DefaultPushNotificationMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultPushNotificationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultPushNotificationTemplate:
    boto3_raw_data: "type_defs.DefaultPushNotificationTemplateTypeDef" = (
        dataclasses.field()
    )

    Action = field("Action")
    Body = field("Body")
    Sound = field("Sound")
    Title = field("Title")
    Url = field("Url")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DefaultPushNotificationTemplateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultPushNotificationTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAdmChannelRequest:
    boto3_raw_data: "type_defs.DeleteAdmChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAdmChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAdmChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApnsChannelRequest:
    boto3_raw_data: "type_defs.DeleteApnsChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApnsChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApnsChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApnsSandboxChannelRequest:
    boto3_raw_data: "type_defs.DeleteApnsSandboxChannelRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApnsSandboxChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApnsSandboxChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApnsVoipChannelRequest:
    boto3_raw_data: "type_defs.DeleteApnsVoipChannelRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApnsVoipChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApnsVoipChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApnsVoipSandboxChannelRequest:
    boto3_raw_data: "type_defs.DeleteApnsVoipSandboxChannelRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApnsVoipSandboxChannelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApnsVoipSandboxChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppRequest:
    boto3_raw_data: "type_defs.DeleteAppRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBaiduChannelRequest:
    boto3_raw_data: "type_defs.DeleteBaiduChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBaiduChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBaiduChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCampaignRequest:
    boto3_raw_data: "type_defs.DeleteCampaignRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    CampaignId = field("CampaignId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEmailChannelRequest:
    boto3_raw_data: "type_defs.DeleteEmailChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEmailChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEmailChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailChannelResponse:
    boto3_raw_data: "type_defs.EmailChannelResponseTypeDef" = dataclasses.field()

    Platform = field("Platform")
    ApplicationId = field("ApplicationId")
    ConfigurationSet = field("ConfigurationSet")
    CreationDate = field("CreationDate")
    Enabled = field("Enabled")
    FromAddress = field("FromAddress")
    HasCredential = field("HasCredential")
    Id = field("Id")
    Identity = field("Identity")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    MessagesPerSecond = field("MessagesPerSecond")
    RoleArn = field("RoleArn")
    OrchestrationSendingRoleArn = field("OrchestrationSendingRoleArn")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEmailTemplateRequest:
    boto3_raw_data: "type_defs.DeleteEmailTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEmailTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEmailTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageBody:
    boto3_raw_data: "type_defs.MessageBodyTypeDef" = dataclasses.field()

    Message = field("Message")
    RequestID = field("RequestID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageBodyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageBodyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEndpointRequest:
    boto3_raw_data: "type_defs.DeleteEndpointRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EndpointId = field("EndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventStreamRequest:
    boto3_raw_data: "type_defs.DeleteEventStreamRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventStream:
    boto3_raw_data: "type_defs.EventStreamTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    DestinationStreamArn = field("DestinationStreamArn")
    RoleArn = field("RoleArn")
    ExternalId = field("ExternalId")
    LastModifiedDate = field("LastModifiedDate")
    LastUpdatedBy = field("LastUpdatedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventStreamTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGcmChannelRequest:
    boto3_raw_data: "type_defs.DeleteGcmChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGcmChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGcmChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GCMChannelResponse:
    boto3_raw_data: "type_defs.GCMChannelResponseTypeDef" = dataclasses.field()

    Platform = field("Platform")
    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")
    Credential = field("Credential")
    DefaultAuthenticationMethod = field("DefaultAuthenticationMethod")
    Enabled = field("Enabled")
    HasCredential = field("HasCredential")
    HasFcmServiceCredentials = field("HasFcmServiceCredentials")
    Id = field("Id")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GCMChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GCMChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInAppTemplateRequest:
    boto3_raw_data: "type_defs.DeleteInAppTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInAppTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInAppTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJourneyRequest:
    boto3_raw_data: "type_defs.DeleteJourneyRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    JourneyId = field("JourneyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteJourneyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJourneyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePushTemplateRequest:
    boto3_raw_data: "type_defs.DeletePushTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePushTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePushTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRecommenderConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteRecommenderConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    RecommenderId = field("RecommenderId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRecommenderConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecommenderConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSegmentRequest:
    boto3_raw_data: "type_defs.DeleteSegmentRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    SegmentId = field("SegmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSegmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSegmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSmsChannelRequest:
    boto3_raw_data: "type_defs.DeleteSmsChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSmsChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSmsChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSChannelResponse:
    boto3_raw_data: "type_defs.SMSChannelResponseTypeDef" = dataclasses.field()

    Platform = field("Platform")
    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")
    Enabled = field("Enabled")
    HasCredential = field("HasCredential")
    Id = field("Id")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    PromotionalMessagesPerSecond = field("PromotionalMessagesPerSecond")
    SenderId = field("SenderId")
    ShortCode = field("ShortCode")
    TransactionalMessagesPerSecond = field("TransactionalMessagesPerSecond")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SMSChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMSChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSmsTemplateRequest:
    boto3_raw_data: "type_defs.DeleteSmsTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSmsTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSmsTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserEndpointsRequest:
    boto3_raw_data: "type_defs.DeleteUserEndpointsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    UserId = field("UserId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceChannelRequest:
    boto3_raw_data: "type_defs.DeleteVoiceChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVoiceChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceChannelResponse:
    boto3_raw_data: "type_defs.VoiceChannelResponseTypeDef" = dataclasses.field()

    Platform = field("Platform")
    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")
    Enabled = field("Enabled")
    HasCredential = field("HasCredential")
    Id = field("Id")
    IsArchived = field("IsArchived")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceTemplateRequest:
    boto3_raw_data: "type_defs.DeleteVoiceTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVoiceTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GCMMessage:
    boto3_raw_data: "type_defs.GCMMessageTypeDef" = dataclasses.field()

    Action = field("Action")
    Body = field("Body")
    CollapseKey = field("CollapseKey")
    Data = field("Data")
    IconReference = field("IconReference")
    ImageIconUrl = field("ImageIconUrl")
    ImageUrl = field("ImageUrl")
    PreferredAuthenticationMethod = field("PreferredAuthenticationMethod")
    Priority = field("Priority")
    RawContent = field("RawContent")
    RestrictedPackageName = field("RestrictedPackageName")
    SilentPush = field("SilentPush")
    SmallImageIconUrl = field("SmallImageIconUrl")
    Sound = field("Sound")
    Substitutions = field("Substitutions")
    TimeToLive = field("TimeToLive")
    Title = field("Title")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GCMMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GCMMessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSMessage:
    boto3_raw_data: "type_defs.SMSMessageTypeDef" = dataclasses.field()

    Body = field("Body")
    Keyword = field("Keyword")
    MediaUrl = field("MediaUrl")
    MessageType = field("MessageType")
    OriginationNumber = field("OriginationNumber")
    SenderId = field("SenderId")
    Substitutions = field("Substitutions")
    EntityId = field("EntityId")
    TemplateId = field("TemplateId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SMSMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SMSMessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceMessage:
    boto3_raw_data: "type_defs.VoiceMessageTypeDef" = dataclasses.field()

    Body = field("Body")
    LanguageCode = field("LanguageCode")
    OriginationNumber = field("OriginationNumber")
    Substitutions = field("Substitutions")
    VoiceId = field("VoiceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VoiceMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VoiceMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailChannelRequest:
    boto3_raw_data: "type_defs.EmailChannelRequestTypeDef" = dataclasses.field()

    FromAddress = field("FromAddress")
    Identity = field("Identity")
    ConfigurationSet = field("ConfigurationSet")
    Enabled = field("Enabled")
    RoleArn = field("RoleArn")
    OrchestrationSendingRoleArn = field("OrchestrationSendingRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyEmailMessage:
    boto3_raw_data: "type_defs.JourneyEmailMessageTypeDef" = dataclasses.field()

    FromAddress = field("FromAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JourneyEmailMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyEmailMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointDemographic:
    boto3_raw_data: "type_defs.EndpointDemographicTypeDef" = dataclasses.field()

    AppVersion = field("AppVersion")
    Locale = field("Locale")
    Make = field("Make")
    Model = field("Model")
    ModelVersion = field("ModelVersion")
    Platform = field("Platform")
    PlatformVersion = field("PlatformVersion")
    Timezone = field("Timezone")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointDemographicTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointDemographicTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointLocation:
    boto3_raw_data: "type_defs.EndpointLocationTypeDef" = dataclasses.field()

    City = field("City")
    Country = field("Country")
    Latitude = field("Latitude")
    Longitude = field("Longitude")
    PostalCode = field("PostalCode")
    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointItemResponse:
    boto3_raw_data: "type_defs.EndpointItemResponseTypeDef" = dataclasses.field()

    Message = field("Message")
    StatusCode = field("StatusCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointItemResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointItemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointMessageResult:
    boto3_raw_data: "type_defs.EndpointMessageResultTypeDef" = dataclasses.field()

    DeliveryStatus = field("DeliveryStatus")
    StatusCode = field("StatusCode")
    Address = field("Address")
    MessageId = field("MessageId")
    StatusMessage = field("StatusMessage")
    UpdatedToken = field("UpdatedToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointMessageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointMessageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointUserOutput:
    boto3_raw_data: "type_defs.EndpointUserOutputTypeDef" = dataclasses.field()

    UserAttributes = field("UserAttributes")
    UserId = field("UserId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointUserOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointUserOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointSendConfiguration:
    boto3_raw_data: "type_defs.EndpointSendConfigurationTypeDef" = dataclasses.field()

    BodyOverride = field("BodyOverride")
    Context = field("Context")
    RawContent = field("RawContent")
    Substitutions = field("Substitutions")
    TitleOverride = field("TitleOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointSendConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointSendConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointUser:
    boto3_raw_data: "type_defs.EndpointUserTypeDef" = dataclasses.field()

    UserAttributes = field("UserAttributes")
    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointUserTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDimension:
    boto3_raw_data: "type_defs.MetricDimensionTypeDef" = dataclasses.field()

    ComparisonOperator = field("ComparisonOperator")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDimensionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDimensionOutput:
    boto3_raw_data: "type_defs.SetDimensionOutputTypeDef" = dataclasses.field()

    Values = field("Values")
    DimensionType = field("DimensionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetDimensionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventItemResponse:
    boto3_raw_data: "type_defs.EventItemResponseTypeDef" = dataclasses.field()

    Message = field("Message")
    StatusCode = field("StatusCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventItemResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventItemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Session:
    boto3_raw_data: "type_defs.SessionTypeDef" = dataclasses.field()

    Id = field("Id")
    StartTimestamp = field("StartTimestamp")
    Duration = field("Duration")
    StopTimestamp = field("StopTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportJobResource:
    boto3_raw_data: "type_defs.ExportJobResourceTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    S3UrlPrefix = field("S3UrlPrefix")
    SegmentId = field("SegmentId")
    SegmentVersion = field("SegmentVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportJobResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportJobResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GCMChannelRequest:
    boto3_raw_data: "type_defs.GCMChannelRequestTypeDef" = dataclasses.field()

    ApiKey = field("ApiKey")
    DefaultAuthenticationMethod = field("DefaultAuthenticationMethod")
    Enabled = field("Enabled")
    ServiceJson = field("ServiceJson")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GCMChannelRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GCMChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GPSCoordinates:
    boto3_raw_data: "type_defs.GPSCoordinatesTypeDef" = dataclasses.field()

    Latitude = field("Latitude")
    Longitude = field("Longitude")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GPSCoordinatesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GPSCoordinatesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAdmChannelRequest:
    boto3_raw_data: "type_defs.GetAdmChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAdmChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdmChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApnsChannelRequest:
    boto3_raw_data: "type_defs.GetApnsChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApnsChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApnsChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApnsSandboxChannelRequest:
    boto3_raw_data: "type_defs.GetApnsSandboxChannelRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApnsSandboxChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApnsSandboxChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApnsVoipChannelRequest:
    boto3_raw_data: "type_defs.GetApnsVoipChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApnsVoipChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApnsVoipChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApnsVoipSandboxChannelRequest:
    boto3_raw_data: "type_defs.GetApnsVoipSandboxChannelRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetApnsVoipSandboxChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApnsVoipSandboxChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppRequest:
    boto3_raw_data: "type_defs.GetAppRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAppRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationSettingsRequest:
    boto3_raw_data: "type_defs.GetApplicationSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetApplicationSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppsRequest:
    boto3_raw_data: "type_defs.GetAppsRequestTypeDef" = dataclasses.field()

    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAppsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAppsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBaiduChannelRequest:
    boto3_raw_data: "type_defs.GetBaiduChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBaiduChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBaiduChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignActivitiesRequest:
    boto3_raw_data: "type_defs.GetCampaignActivitiesRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    CampaignId = field("CampaignId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignActivitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignActivitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignRequest:
    boto3_raw_data: "type_defs.GetCampaignRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    CampaignId = field("CampaignId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignVersionRequest:
    boto3_raw_data: "type_defs.GetCampaignVersionRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    CampaignId = field("CampaignId")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignVersionsRequest:
    boto3_raw_data: "type_defs.GetCampaignVersionsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    CampaignId = field("CampaignId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignsRequest:
    boto3_raw_data: "type_defs.GetCampaignsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelsRequest:
    boto3_raw_data: "type_defs.GetChannelsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEmailChannelRequest:
    boto3_raw_data: "type_defs.GetEmailChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEmailChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEmailChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEmailTemplateRequest:
    boto3_raw_data: "type_defs.GetEmailTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEmailTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEmailTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEndpointRequest:
    boto3_raw_data: "type_defs.GetEndpointRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EndpointId = field("EndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventStreamRequest:
    boto3_raw_data: "type_defs.GetEventStreamRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportJobRequest:
    boto3_raw_data: "type_defs.GetExportJobRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportJobsRequest:
    boto3_raw_data: "type_defs.GetExportJobsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGcmChannelRequest:
    boto3_raw_data: "type_defs.GetGcmChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGcmChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGcmChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportJobRequest:
    boto3_raw_data: "type_defs.GetImportJobRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportJobsRequest:
    boto3_raw_data: "type_defs.GetImportJobsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInAppMessagesRequest:
    boto3_raw_data: "type_defs.GetInAppMessagesRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EndpointId = field("EndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInAppMessagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInAppMessagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInAppTemplateRequest:
    boto3_raw_data: "type_defs.GetInAppTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInAppTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInAppTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyExecutionActivityMetricsRequest:
    boto3_raw_data: "type_defs.GetJourneyExecutionActivityMetricsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    JourneyActivityId = field("JourneyActivityId")
    JourneyId = field("JourneyId")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetJourneyExecutionActivityMetricsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyExecutionActivityMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyExecutionActivityMetricsResponse:
    boto3_raw_data: "type_defs.JourneyExecutionActivityMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    ActivityType = field("ActivityType")
    ApplicationId = field("ApplicationId")
    JourneyActivityId = field("JourneyActivityId")
    JourneyId = field("JourneyId")
    LastEvaluatedTime = field("LastEvaluatedTime")
    Metrics = field("Metrics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.JourneyExecutionActivityMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyExecutionActivityMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyExecutionMetricsRequest:
    boto3_raw_data: "type_defs.GetJourneyExecutionMetricsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    JourneyId = field("JourneyId")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetJourneyExecutionMetricsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyExecutionMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyExecutionMetricsResponse:
    boto3_raw_data: "type_defs.JourneyExecutionMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    JourneyId = field("JourneyId")
    LastEvaluatedTime = field("LastEvaluatedTime")
    Metrics = field("Metrics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.JourneyExecutionMetricsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyExecutionMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyRequest:
    boto3_raw_data: "type_defs.GetJourneyRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    JourneyId = field("JourneyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJourneyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyRunExecutionActivityMetricsRequest:
    boto3_raw_data: "type_defs.GetJourneyRunExecutionActivityMetricsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    JourneyActivityId = field("JourneyActivityId")
    JourneyId = field("JourneyId")
    RunId = field("RunId")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetJourneyRunExecutionActivityMetricsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyRunExecutionActivityMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyRunExecutionActivityMetricsResponse:
    boto3_raw_data: "type_defs.JourneyRunExecutionActivityMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    ActivityType = field("ActivityType")
    ApplicationId = field("ApplicationId")
    JourneyActivityId = field("JourneyActivityId")
    JourneyId = field("JourneyId")
    LastEvaluatedTime = field("LastEvaluatedTime")
    Metrics = field("Metrics")
    RunId = field("RunId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.JourneyRunExecutionActivityMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyRunExecutionActivityMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyRunExecutionMetricsRequest:
    boto3_raw_data: "type_defs.GetJourneyRunExecutionMetricsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    JourneyId = field("JourneyId")
    RunId = field("RunId")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetJourneyRunExecutionMetricsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyRunExecutionMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyRunExecutionMetricsResponse:
    boto3_raw_data: "type_defs.JourneyRunExecutionMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    JourneyId = field("JourneyId")
    LastEvaluatedTime = field("LastEvaluatedTime")
    Metrics = field("Metrics")
    RunId = field("RunId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.JourneyRunExecutionMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyRunExecutionMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyRunsRequest:
    boto3_raw_data: "type_defs.GetJourneyRunsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    JourneyId = field("JourneyId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJourneyRunsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyRunsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPushTemplateRequest:
    boto3_raw_data: "type_defs.GetPushTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPushTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPushTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommenderConfigurationRequest:
    boto3_raw_data: "type_defs.GetRecommenderConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    RecommenderId = field("RecommenderId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommenderConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommenderConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommenderConfigurationsRequest:
    boto3_raw_data: "type_defs.GetRecommenderConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommenderConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommenderConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentExportJobsRequest:
    boto3_raw_data: "type_defs.GetSegmentExportJobsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    SegmentId = field("SegmentId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentExportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentImportJobsRequest:
    boto3_raw_data: "type_defs.GetSegmentImportJobsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    SegmentId = field("SegmentId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentRequest:
    boto3_raw_data: "type_defs.GetSegmentRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    SegmentId = field("SegmentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSegmentRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentVersionRequest:
    boto3_raw_data: "type_defs.GetSegmentVersionRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    SegmentId = field("SegmentId")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentVersionsRequest:
    boto3_raw_data: "type_defs.GetSegmentVersionsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    SegmentId = field("SegmentId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentsRequest:
    boto3_raw_data: "type_defs.GetSegmentsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSmsChannelRequest:
    boto3_raw_data: "type_defs.GetSmsChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSmsChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSmsChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSmsTemplateRequest:
    boto3_raw_data: "type_defs.GetSmsTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSmsTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSmsTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSTemplateResponse:
    boto3_raw_data: "type_defs.SMSTemplateResponseTypeDef" = dataclasses.field()

    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")
    TemplateName = field("TemplateName")
    TemplateType = field("TemplateType")
    Arn = field("Arn")
    Body = field("Body")
    DefaultSubstitutions = field("DefaultSubstitutions")
    RecommenderId = field("RecommenderId")
    tags = field("tags")
    TemplateDescription = field("TemplateDescription")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SMSTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMSTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserEndpointsRequest:
    boto3_raw_data: "type_defs.GetUserEndpointsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    UserId = field("UserId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceChannelRequest:
    boto3_raw_data: "type_defs.GetVoiceChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVoiceChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceTemplateRequest:
    boto3_raw_data: "type_defs.GetVoiceTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVoiceTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceTemplateResponse:
    boto3_raw_data: "type_defs.VoiceTemplateResponseTypeDef" = dataclasses.field()

    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")
    TemplateName = field("TemplateName")
    TemplateType = field("TemplateType")
    Arn = field("Arn")
    Body = field("Body")
    DefaultSubstitutions = field("DefaultSubstitutions")
    LanguageCode = field("LanguageCode")
    tags = field("tags")
    TemplateDescription = field("TemplateDescription")
    Version = field("Version")
    VoiceId = field("VoiceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportJobResource:
    boto3_raw_data: "type_defs.ImportJobResourceTypeDef" = dataclasses.field()

    Format = field("Format")
    RoleArn = field("RoleArn")
    S3Url = field("S3Url")
    DefineSegment = field("DefineSegment")
    ExternalId = field("ExternalId")
    RegisterEndpoints = field("RegisterEndpoints")
    SegmentId = field("SegmentId")
    SegmentName = field("SegmentName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportJobResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportJobResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InAppMessageBodyConfig:
    boto3_raw_data: "type_defs.InAppMessageBodyConfigTypeDef" = dataclasses.field()

    Alignment = field("Alignment")
    Body = field("Body")
    TextColor = field("TextColor")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InAppMessageBodyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InAppMessageBodyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverrideButtonConfiguration:
    boto3_raw_data: "type_defs.OverrideButtonConfigurationTypeDef" = dataclasses.field()

    ButtonAction = field("ButtonAction")
    Link = field("Link")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OverrideButtonConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OverrideButtonConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InAppMessageHeaderConfig:
    boto3_raw_data: "type_defs.InAppMessageHeaderConfigTypeDef" = dataclasses.field()

    Alignment = field("Alignment")
    Header = field("Header")
    TextColor = field("TextColor")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InAppMessageHeaderConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InAppMessageHeaderConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyChannelSettings:
    boto3_raw_data: "type_defs.JourneyChannelSettingsTypeDef" = dataclasses.field()

    ConnectCampaignArn = field("ConnectCampaignArn")
    ConnectCampaignExecutionRoleArn = field("ConnectCampaignExecutionRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JourneyChannelSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyChannelSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyPushMessage:
    boto3_raw_data: "type_defs.JourneyPushMessageTypeDef" = dataclasses.field()

    TimeToLive = field("TimeToLive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JourneyPushMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyPushMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyScheduleOutput:
    boto3_raw_data: "type_defs.JourneyScheduleOutputTypeDef" = dataclasses.field()

    EndTime = field("EndTime")
    StartTime = field("StartTime")
    Timezone = field("Timezone")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JourneyScheduleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyRunResponse:
    boto3_raw_data: "type_defs.JourneyRunResponseTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    LastUpdateTime = field("LastUpdateTime")
    RunId = field("RunId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JourneyRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneySMSMessage:
    boto3_raw_data: "type_defs.JourneySMSMessageTypeDef" = dataclasses.field()

    MessageType = field("MessageType")
    OriginationNumber = field("OriginationNumber")
    SenderId = field("SenderId")
    EntityId = field("EntityId")
    TemplateId = field("TemplateId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JourneySMSMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneySMSMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyStateRequest:
    boto3_raw_data: "type_defs.JourneyStateRequestTypeDef" = dataclasses.field()

    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JourneyStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJourneysRequest:
    boto3_raw_data: "type_defs.ListJourneysRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    PageSize = field("PageSize")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJourneysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJourneysRequestTypeDef"]
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
class TagsModelOutput:
    boto3_raw_data: "type_defs.TagsModelOutputTypeDef" = dataclasses.field()

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagsModelOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagsModelOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateVersionsRequest:
    boto3_raw_data: "type_defs.ListTemplateVersionsRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    TemplateType = field("TemplateType")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplateVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplatesRequest:
    boto3_raw_data: "type_defs.ListTemplatesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    PageSize = field("PageSize")
    Prefix = field("Prefix")
    TemplateType = field("TemplateType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Message:
    boto3_raw_data: "type_defs.MessageTypeDef" = dataclasses.field()

    Action = field("Action")
    Body = field("Body")
    ImageIconUrl = field("ImageIconUrl")
    ImageSmallIconUrl = field("ImageSmallIconUrl")
    ImageUrl = field("ImageUrl")
    JsonBody = field("JsonBody")
    MediaUrl = field("MediaUrl")
    RawContent = field("RawContent")
    SilentPush = field("SilentPush")
    TimeToLive = field("TimeToLive")
    Title = field("Title")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageResult:
    boto3_raw_data: "type_defs.MessageResultTypeDef" = dataclasses.field()

    DeliveryStatus = field("DeliveryStatus")
    StatusCode = field("StatusCode")
    MessageId = field("MessageId")
    StatusMessage = field("StatusMessage")
    UpdatedToken = field("UpdatedToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NumberValidateRequest:
    boto3_raw_data: "type_defs.NumberValidateRequestTypeDef" = dataclasses.field()

    IsoCountryCode = field("IsoCountryCode")
    PhoneNumber = field("PhoneNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NumberValidateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NumberValidateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NumberValidateResponse:
    boto3_raw_data: "type_defs.NumberValidateResponseTypeDef" = dataclasses.field()

    Carrier = field("Carrier")
    City = field("City")
    CleansedPhoneNumberE164 = field("CleansedPhoneNumberE164")
    CleansedPhoneNumberNational = field("CleansedPhoneNumberNational")
    Country = field("Country")
    CountryCodeIso2 = field("CountryCodeIso2")
    CountryCodeNumeric = field("CountryCodeNumeric")
    County = field("County")
    OriginalCountryCodeIso2 = field("OriginalCountryCodeIso2")
    OriginalPhoneNumber = field("OriginalPhoneNumber")
    PhoneType = field("PhoneType")
    PhoneTypeCode = field("PhoneTypeCode")
    Timezone = field("Timezone")
    ZipCode = field("ZipCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NumberValidateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NumberValidateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenHoursRule:
    boto3_raw_data: "type_defs.OpenHoursRuleTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpenHoursRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpenHoursRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteEventStream:
    boto3_raw_data: "type_defs.WriteEventStreamTypeDef" = dataclasses.field()

    DestinationStreamArn = field("DestinationStreamArn")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WriteEventStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteEventStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RandomSplitEntry:
    boto3_raw_data: "type_defs.RandomSplitEntryTypeDef" = dataclasses.field()

    NextActivity = field("NextActivity")
    Percentage = field("Percentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RandomSplitEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RandomSplitEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecencyDimension:
    boto3_raw_data: "type_defs.RecencyDimensionTypeDef" = dataclasses.field()

    Duration = field("Duration")
    RecencyType = field("RecencyType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecencyDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecencyDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAttributesRequest:
    boto3_raw_data: "type_defs.UpdateAttributesRequestTypeDef" = dataclasses.field()

    Blacklist = field("Blacklist")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultRowValue:
    boto3_raw_data: "type_defs.ResultRowValueTypeDef" = dataclasses.field()

    Key = field("Key")
    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultRowValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultRowValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSChannelRequest:
    boto3_raw_data: "type_defs.SMSChannelRequestTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SenderId = field("SenderId")
    ShortCode = field("ShortCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SMSChannelRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMSChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentCondition:
    boto3_raw_data: "type_defs.SegmentConditionTypeDef" = dataclasses.field()

    SegmentId = field("SegmentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentReference:
    boto3_raw_data: "type_defs.SegmentReferenceTypeDef" = dataclasses.field()

    Id = field("Id")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentImportResource:
    boto3_raw_data: "type_defs.SegmentImportResourceTypeDef" = dataclasses.field()

    ExternalId = field("ExternalId")
    Format = field("Format")
    RoleArn = field("RoleArn")
    S3Url = field("S3Url")
    Size = field("Size")
    ChannelCounts = field("ChannelCounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentImportResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentImportResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendOTPMessageRequestParameters:
    boto3_raw_data: "type_defs.SendOTPMessageRequestParametersTypeDef" = (
        dataclasses.field()
    )

    BrandName = field("BrandName")
    Channel = field("Channel")
    DestinationIdentity = field("DestinationIdentity")
    OriginationIdentity = field("OriginationIdentity")
    ReferenceId = field("ReferenceId")
    AllowedAttempts = field("AllowedAttempts")
    CodeLength = field("CodeLength")
    EntityId = field("EntityId")
    Language = field("Language")
    TemplateId = field("TemplateId")
    ValidityPeriod = field("ValidityPeriod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendOTPMessageRequestParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendOTPMessageRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDimension:
    boto3_raw_data: "type_defs.SetDimensionTypeDef" = dataclasses.field()

    Values = field("Values")
    DimensionType = field("DimensionType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SetDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SetDimensionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleEmailPart:
    boto3_raw_data: "type_defs.SimpleEmailPartTypeDef" = dataclasses.field()

    Charset = field("Charset")
    Data = field("Data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SimpleEmailPartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SimpleEmailPartTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagsModel:
    boto3_raw_data: "type_defs.TagsModelTypeDef" = dataclasses.field()

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagsModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagsModelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateActiveVersionRequest:
    boto3_raw_data: "type_defs.TemplateActiveVersionRequestTypeDef" = (
        dataclasses.field()
    )

    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateActiveVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateActiveVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Template:
    boto3_raw_data: "type_defs.TemplateTypeDef" = dataclasses.field()

    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateResponse:
    boto3_raw_data: "type_defs.TemplateResponseTypeDef" = dataclasses.field()

    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")
    TemplateName = field("TemplateName")
    TemplateType = field("TemplateType")
    Arn = field("Arn")
    DefaultSubstitutions = field("DefaultSubstitutions")
    tags = field("tags")
    TemplateDescription = field("TemplateDescription")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateVersionResponse:
    boto3_raw_data: "type_defs.TemplateVersionResponseTypeDef" = dataclasses.field()

    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")
    TemplateName = field("TemplateName")
    TemplateType = field("TemplateType")
    DefaultSubstitutions = field("DefaultSubstitutions")
    TemplateDescription = field("TemplateDescription")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateVersionResponseTypeDef"]
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
class UpdateRecommenderConfiguration:
    boto3_raw_data: "type_defs.UpdateRecommenderConfigurationTypeDef" = (
        dataclasses.field()
    )

    RecommendationProviderRoleArn = field("RecommendationProviderRoleArn")
    RecommendationProviderUri = field("RecommendationProviderUri")
    Attributes = field("Attributes")
    Description = field("Description")
    Name = field("Name")
    RecommendationProviderIdType = field("RecommendationProviderIdType")
    RecommendationTransformerUri = field("RecommendationTransformerUri")
    RecommendationsDisplayName = field("RecommendationsDisplayName")
    RecommendationsPerMessage = field("RecommendationsPerMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRecommenderConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecommenderConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceChannelRequest:
    boto3_raw_data: "type_defs.VoiceChannelRequestTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerificationResponse:
    boto3_raw_data: "type_defs.VerificationResponseTypeDef" = dataclasses.field()

    Valid = field("Valid")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerificationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerificationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyOTPMessageRequestParameters:
    boto3_raw_data: "type_defs.VerifyOTPMessageRequestParametersTypeDef" = (
        dataclasses.field()
    )

    DestinationIdentity = field("DestinationIdentity")
    Otp = field("Otp")
    ReferenceId = field("ReferenceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VerifyOTPMessageRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyOTPMessageRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAdmChannelRequest:
    boto3_raw_data: "type_defs.UpdateAdmChannelRequestTypeDef" = dataclasses.field()

    @cached_property
    def ADMChannelRequest(self):  # pragma: no cover
        return ADMChannelRequest.make_one(self.boto3_raw_data["ADMChannelRequest"])

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAdmChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAdmChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApnsChannelRequest:
    boto3_raw_data: "type_defs.UpdateApnsChannelRequestTypeDef" = dataclasses.field()

    @cached_property
    def APNSChannelRequest(self):  # pragma: no cover
        return APNSChannelRequest.make_one(self.boto3_raw_data["APNSChannelRequest"])

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApnsChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApnsChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApnsSandboxChannelRequest:
    boto3_raw_data: "type_defs.UpdateApnsSandboxChannelRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSSandboxChannelRequest(self):  # pragma: no cover
        return APNSSandboxChannelRequest.make_one(
            self.boto3_raw_data["APNSSandboxChannelRequest"]
        )

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateApnsSandboxChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApnsSandboxChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApnsVoipChannelRequest:
    boto3_raw_data: "type_defs.UpdateApnsVoipChannelRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSVoipChannelRequest(self):  # pragma: no cover
        return APNSVoipChannelRequest.make_one(
            self.boto3_raw_data["APNSVoipChannelRequest"]
        )

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApnsVoipChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApnsVoipChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApnsVoipSandboxChannelRequest:
    boto3_raw_data: "type_defs.UpdateApnsVoipSandboxChannelRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSVoipSandboxChannelRequest(self):  # pragma: no cover
        return APNSVoipSandboxChannelRequest.make_one(
            self.boto3_raw_data["APNSVoipSandboxChannelRequest"]
        )

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApnsVoipSandboxChannelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApnsVoipSandboxChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivitiesResponse:
    boto3_raw_data: "type_defs.ActivitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return ActivityResponse.make_many(self.boto3_raw_data["Item"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationsResponse:
    boto3_raw_data: "type_defs.ApplicationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return ApplicationResponse.make_many(self.boto3_raw_data["Item"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSettingsJourneyLimits:
    boto3_raw_data: "type_defs.ApplicationSettingsJourneyLimitsTypeDef" = (
        dataclasses.field()
    )

    DailyCap = field("DailyCap")

    @cached_property
    def TimeframeCap(self):  # pragma: no cover
        return JourneyTimeframeCap.make_one(self.boto3_raw_data["TimeframeCap"])

    TotalCap = field("TotalCap")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationSettingsJourneyLimitsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSettingsJourneyLimitsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyLimits:
    boto3_raw_data: "type_defs.JourneyLimitsTypeDef" = dataclasses.field()

    DailyCap = field("DailyCap")
    EndpointReentryCap = field("EndpointReentryCap")
    MessagesPerSecond = field("MessagesPerSecond")
    EndpointReentryInterval = field("EndpointReentryInterval")

    @cached_property
    def TimeframeCap(self):  # pragma: no cover
        return JourneyTimeframeCap.make_one(self.boto3_raw_data["TimeframeCap"])

    TotalCap = field("TotalCap")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JourneyLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JourneyLimitsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBaiduChannelRequest:
    boto3_raw_data: "type_defs.UpdateBaiduChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def BaiduChannelRequest(self):  # pragma: no cover
        return BaiduChannelRequest.make_one(self.boto3_raw_data["BaiduChannelRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBaiduChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBaiduChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RawEmail:
    boto3_raw_data: "type_defs.RawEmailTypeDef" = dataclasses.field()

    Data = field("Data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RawEmailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RawEmailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignEmailMessageOutput:
    boto3_raw_data: "type_defs.CampaignEmailMessageOutputTypeDef" = dataclasses.field()

    Body = field("Body")
    FromAddress = field("FromAddress")

    @cached_property
    def Headers(self):  # pragma: no cover
        return MessageHeader.make_many(self.boto3_raw_data["Headers"])

    HtmlBody = field("HtmlBody")
    Title = field("Title")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignEmailMessageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignEmailMessageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignEmailMessage:
    boto3_raw_data: "type_defs.CampaignEmailMessageTypeDef" = dataclasses.field()

    Body = field("Body")
    FromAddress = field("FromAddress")

    @cached_property
    def Headers(self):  # pragma: no cover
        return MessageHeader.make_many(self.boto3_raw_data["Headers"])

    HtmlBody = field("HtmlBody")
    Title = field("Title")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignEmailMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignEmailMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailTemplateRequest:
    boto3_raw_data: "type_defs.EmailTemplateRequestTypeDef" = dataclasses.field()

    DefaultSubstitutions = field("DefaultSubstitutions")
    HtmlPart = field("HtmlPart")
    RecommenderId = field("RecommenderId")
    Subject = field("Subject")

    @cached_property
    def Headers(self):  # pragma: no cover
        return MessageHeader.make_many(self.boto3_raw_data["Headers"])

    tags = field("tags")
    TemplateDescription = field("TemplateDescription")
    TextPart = field("TextPart")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailTemplateResponse:
    boto3_raw_data: "type_defs.EmailTemplateResponseTypeDef" = dataclasses.field()

    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")
    TemplateName = field("TemplateName")
    TemplateType = field("TemplateType")
    Arn = field("Arn")
    DefaultSubstitutions = field("DefaultSubstitutions")
    HtmlPart = field("HtmlPart")
    RecommenderId = field("RecommenderId")
    Subject = field("Subject")

    @cached_property
    def Headers(self):  # pragma: no cover
        return MessageHeader.make_many(self.boto3_raw_data["Headers"])

    tags = field("tags")
    TemplateDescription = field("TemplateDescription")
    TextPart = field("TextPart")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelsResponse:
    boto3_raw_data: "type_defs.ChannelsResponseTypeDef" = dataclasses.field()

    Channels = field("Channels")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClosedDaysOutput:
    boto3_raw_data: "type_defs.ClosedDaysOutputTypeDef" = dataclasses.field()

    @cached_property
    def EMAIL(self):  # pragma: no cover
        return ClosedDaysRule.make_many(self.boto3_raw_data["EMAIL"])

    @cached_property
    def SMS(self):  # pragma: no cover
        return ClosedDaysRule.make_many(self.boto3_raw_data["SMS"])

    @cached_property
    def PUSH(self):  # pragma: no cover
        return ClosedDaysRule.make_many(self.boto3_raw_data["PUSH"])

    @cached_property
    def VOICE(self):  # pragma: no cover
        return ClosedDaysRule.make_many(self.boto3_raw_data["VOICE"])

    @cached_property
    def CUSTOM(self):  # pragma: no cover
        return ClosedDaysRule.make_many(self.boto3_raw_data["CUSTOM"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClosedDaysOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClosedDaysOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClosedDays:
    boto3_raw_data: "type_defs.ClosedDaysTypeDef" = dataclasses.field()

    @cached_property
    def EMAIL(self):  # pragma: no cover
        return ClosedDaysRule.make_many(self.boto3_raw_data["EMAIL"])

    @cached_property
    def SMS(self):  # pragma: no cover
        return ClosedDaysRule.make_many(self.boto3_raw_data["SMS"])

    @cached_property
    def PUSH(self):  # pragma: no cover
        return ClosedDaysRule.make_many(self.boto3_raw_data["PUSH"])

    @cached_property
    def VOICE(self):  # pragma: no cover
        return ClosedDaysRule.make_many(self.boto3_raw_data["VOICE"])

    @cached_property
    def CUSTOM(self):  # pragma: no cover
        return ClosedDaysRule.make_many(self.boto3_raw_data["CUSTOM"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClosedDaysTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClosedDaysTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaitActivity:
    boto3_raw_data: "type_defs.WaitActivityTypeDef" = dataclasses.field()

    NextActivity = field("NextActivity")

    @cached_property
    def WaitTime(self):  # pragma: no cover
        return WaitTime.make_one(self.boto3_raw_data["WaitTime"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaitActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaitActivityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppRequest:
    boto3_raw_data: "type_defs.CreateAppRequestTypeDef" = dataclasses.field()

    @cached_property
    def CreateApplicationRequest(self):  # pragma: no cover
        return CreateApplicationRequest.make_one(
            self.boto3_raw_data["CreateApplicationRequest"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppResponse:
    boto3_raw_data: "type_defs.CreateAppResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationResponse(self):  # pragma: no cover
        return ApplicationResponse.make_one(self.boto3_raw_data["ApplicationResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAppResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAdmChannelResponse:
    boto3_raw_data: "type_defs.DeleteAdmChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def ADMChannelResponse(self):  # pragma: no cover
        return ADMChannelResponse.make_one(self.boto3_raw_data["ADMChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAdmChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAdmChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApnsChannelResponse:
    boto3_raw_data: "type_defs.DeleteApnsChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def APNSChannelResponse(self):  # pragma: no cover
        return APNSChannelResponse.make_one(self.boto3_raw_data["APNSChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApnsChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApnsChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApnsSandboxChannelResponse:
    boto3_raw_data: "type_defs.DeleteApnsSandboxChannelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSSandboxChannelResponse(self):  # pragma: no cover
        return APNSSandboxChannelResponse.make_one(
            self.boto3_raw_data["APNSSandboxChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApnsSandboxChannelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApnsSandboxChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApnsVoipChannelResponse:
    boto3_raw_data: "type_defs.DeleteApnsVoipChannelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSVoipChannelResponse(self):  # pragma: no cover
        return APNSVoipChannelResponse.make_one(
            self.boto3_raw_data["APNSVoipChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApnsVoipChannelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApnsVoipChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApnsVoipSandboxChannelResponse:
    boto3_raw_data: "type_defs.DeleteApnsVoipSandboxChannelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSVoipSandboxChannelResponse(self):  # pragma: no cover
        return APNSVoipSandboxChannelResponse.make_one(
            self.boto3_raw_data["APNSVoipSandboxChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApnsVoipSandboxChannelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApnsVoipSandboxChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppResponse:
    boto3_raw_data: "type_defs.DeleteAppResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationResponse(self):  # pragma: no cover
        return ApplicationResponse.make_one(self.boto3_raw_data["ApplicationResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAppResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBaiduChannelResponse:
    boto3_raw_data: "type_defs.DeleteBaiduChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def BaiduChannelResponse(self):  # pragma: no cover
        return BaiduChannelResponse.make_one(
            self.boto3_raw_data["BaiduChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBaiduChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBaiduChannelResponseTypeDef"]
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
class GetAdmChannelResponse:
    boto3_raw_data: "type_defs.GetAdmChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def ADMChannelResponse(self):  # pragma: no cover
        return ADMChannelResponse.make_one(self.boto3_raw_data["ADMChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAdmChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdmChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApnsChannelResponse:
    boto3_raw_data: "type_defs.GetApnsChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def APNSChannelResponse(self):  # pragma: no cover
        return APNSChannelResponse.make_one(self.boto3_raw_data["APNSChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApnsChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApnsChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApnsSandboxChannelResponse:
    boto3_raw_data: "type_defs.GetApnsSandboxChannelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSSandboxChannelResponse(self):  # pragma: no cover
        return APNSSandboxChannelResponse.make_one(
            self.boto3_raw_data["APNSSandboxChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetApnsSandboxChannelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApnsSandboxChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApnsVoipChannelResponse:
    boto3_raw_data: "type_defs.GetApnsVoipChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def APNSVoipChannelResponse(self):  # pragma: no cover
        return APNSVoipChannelResponse.make_one(
            self.boto3_raw_data["APNSVoipChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApnsVoipChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApnsVoipChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApnsVoipSandboxChannelResponse:
    boto3_raw_data: "type_defs.GetApnsVoipSandboxChannelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSVoipSandboxChannelResponse(self):  # pragma: no cover
        return APNSVoipSandboxChannelResponse.make_one(
            self.boto3_raw_data["APNSVoipSandboxChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApnsVoipSandboxChannelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApnsVoipSandboxChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppResponse:
    boto3_raw_data: "type_defs.GetAppResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationResponse(self):  # pragma: no cover
        return ApplicationResponse.make_one(self.boto3_raw_data["ApplicationResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAppResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAppResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBaiduChannelResponse:
    boto3_raw_data: "type_defs.GetBaiduChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def BaiduChannelResponse(self):  # pragma: no cover
        return BaiduChannelResponse.make_one(
            self.boto3_raw_data["BaiduChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBaiduChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBaiduChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAttributesResponse:
    boto3_raw_data: "type_defs.RemoveAttributesResponseTypeDef" = dataclasses.field()

    @cached_property
    def AttributesResource(self):  # pragma: no cover
        return AttributesResource.make_one(self.boto3_raw_data["AttributesResource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveAttributesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAdmChannelResponse:
    boto3_raw_data: "type_defs.UpdateAdmChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def ADMChannelResponse(self):  # pragma: no cover
        return ADMChannelResponse.make_one(self.boto3_raw_data["ADMChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAdmChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAdmChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApnsChannelResponse:
    boto3_raw_data: "type_defs.UpdateApnsChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def APNSChannelResponse(self):  # pragma: no cover
        return APNSChannelResponse.make_one(self.boto3_raw_data["APNSChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApnsChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApnsChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApnsSandboxChannelResponse:
    boto3_raw_data: "type_defs.UpdateApnsSandboxChannelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSSandboxChannelResponse(self):  # pragma: no cover
        return APNSSandboxChannelResponse.make_one(
            self.boto3_raw_data["APNSSandboxChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateApnsSandboxChannelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApnsSandboxChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApnsVoipChannelResponse:
    boto3_raw_data: "type_defs.UpdateApnsVoipChannelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSVoipChannelResponse(self):  # pragma: no cover
        return APNSVoipChannelResponse.make_one(
            self.boto3_raw_data["APNSVoipChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateApnsVoipChannelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApnsVoipChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApnsVoipSandboxChannelResponse:
    boto3_raw_data: "type_defs.UpdateApnsVoipSandboxChannelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def APNSVoipSandboxChannelResponse(self):  # pragma: no cover
        return APNSVoipSandboxChannelResponse.make_one(
            self.boto3_raw_data["APNSVoipSandboxChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApnsVoipSandboxChannelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApnsVoipSandboxChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBaiduChannelResponse:
    boto3_raw_data: "type_defs.UpdateBaiduChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def BaiduChannelResponse(self):  # pragma: no cover
        return BaiduChannelResponse.make_one(
            self.boto3_raw_data["BaiduChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBaiduChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBaiduChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEmailTemplateResponse:
    boto3_raw_data: "type_defs.CreateEmailTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def CreateTemplateMessageBody(self):  # pragma: no cover
        return CreateTemplateMessageBody.make_one(
            self.boto3_raw_data["CreateTemplateMessageBody"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEmailTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEmailTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePushTemplateResponse:
    boto3_raw_data: "type_defs.CreatePushTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def CreateTemplateMessageBody(self):  # pragma: no cover
        return CreateTemplateMessageBody.make_one(
            self.boto3_raw_data["CreateTemplateMessageBody"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePushTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePushTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSmsTemplateResponse:
    boto3_raw_data: "type_defs.CreateSmsTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def CreateTemplateMessageBody(self):  # pragma: no cover
        return CreateTemplateMessageBody.make_one(
            self.boto3_raw_data["CreateTemplateMessageBody"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSmsTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSmsTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVoiceTemplateResponse:
    boto3_raw_data: "type_defs.CreateVoiceTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def CreateTemplateMessageBody(self):  # pragma: no cover
        return CreateTemplateMessageBody.make_one(
            self.boto3_raw_data["CreateTemplateMessageBody"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVoiceTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVoiceTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExportJobRequest:
    boto3_raw_data: "type_defs.CreateExportJobRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def ExportJobRequest(self):  # pragma: no cover
        return ExportJobRequest.make_one(self.boto3_raw_data["ExportJobRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImportJobRequest:
    boto3_raw_data: "type_defs.CreateImportJobRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def ImportJobRequest(self):  # pragma: no cover
        return ImportJobRequest.make_one(self.boto3_raw_data["ImportJobRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInAppTemplateResponse:
    boto3_raw_data: "type_defs.CreateInAppTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def TemplateCreateMessageBody(self):  # pragma: no cover
        return TemplateCreateMessageBody.make_one(
            self.boto3_raw_data["TemplateCreateMessageBody"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInAppTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInAppTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRecommenderConfigurationRequest:
    boto3_raw_data: "type_defs.CreateRecommenderConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CreateRecommenderConfiguration(self):  # pragma: no cover
        return CreateRecommenderConfiguration.make_one(
            self.boto3_raw_data["CreateRecommenderConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRecommenderConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecommenderConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRecommenderConfigurationResponse:
    boto3_raw_data: "type_defs.CreateRecommenderConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecommenderConfigurationResponse(self):  # pragma: no cover
        return RecommenderConfigurationResponse.make_one(
            self.boto3_raw_data["RecommenderConfigurationResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRecommenderConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecommenderConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRecommenderConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteRecommenderConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecommenderConfigurationResponse(self):  # pragma: no cover
        return RecommenderConfigurationResponse.make_one(
            self.boto3_raw_data["RecommenderConfigurationResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRecommenderConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecommenderConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommenderConfigurationResponse:
    boto3_raw_data: "type_defs.GetRecommenderConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecommenderConfigurationResponse(self):  # pragma: no cover
        return RecommenderConfigurationResponse.make_one(
            self.boto3_raw_data["RecommenderConfigurationResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommenderConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommenderConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommenderConfigurationsResponse:
    boto3_raw_data: "type_defs.ListRecommenderConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Item(self):  # pragma: no cover
        return RecommenderConfigurationResponse.make_many(self.boto3_raw_data["Item"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommenderConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommenderConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecommenderConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateRecommenderConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecommenderConfigurationResponse(self):  # pragma: no cover
        return RecommenderConfigurationResponse.make_one(
            self.boto3_raw_data["RecommenderConfigurationResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRecommenderConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecommenderConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSmsTemplateRequest:
    boto3_raw_data: "type_defs.CreateSmsTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def SMSTemplateRequest(self):  # pragma: no cover
        return SMSTemplateRequest.make_one(self.boto3_raw_data["SMSTemplateRequest"])

    TemplateName = field("TemplateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSmsTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSmsTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSmsTemplateRequest:
    boto3_raw_data: "type_defs.UpdateSmsTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def SMSTemplateRequest(self):  # pragma: no cover
        return SMSTemplateRequest.make_one(self.boto3_raw_data["SMSTemplateRequest"])

    TemplateName = field("TemplateName")
    CreateNewVersion = field("CreateNewVersion")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSmsTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSmsTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVoiceTemplateRequest:
    boto3_raw_data: "type_defs.CreateVoiceTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")

    @cached_property
    def VoiceTemplateRequest(self):  # pragma: no cover
        return VoiceTemplateRequest.make_one(
            self.boto3_raw_data["VoiceTemplateRequest"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVoiceTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVoiceTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceTemplateRequest:
    boto3_raw_data: "type_defs.UpdateVoiceTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")

    @cached_property
    def VoiceTemplateRequest(self):  # pragma: no cover
        return VoiceTemplateRequest.make_one(
            self.boto3_raw_data["VoiceTemplateRequest"]
        )

    CreateNewVersion = field("CreateNewVersion")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVoiceTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomMessageActivityOutput:
    boto3_raw_data: "type_defs.CustomMessageActivityOutputTypeDef" = dataclasses.field()

    DeliveryUri = field("DeliveryUri")
    EndpointTypes = field("EndpointTypes")

    @cached_property
    def MessageConfig(self):  # pragma: no cover
        return JourneyCustomMessage.make_one(self.boto3_raw_data["MessageConfig"])

    NextActivity = field("NextActivity")
    TemplateName = field("TemplateName")
    TemplateVersion = field("TemplateVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomMessageActivityOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomMessageActivityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomMessageActivity:
    boto3_raw_data: "type_defs.CustomMessageActivityTypeDef" = dataclasses.field()

    DeliveryUri = field("DeliveryUri")
    EndpointTypes = field("EndpointTypes")

    @cached_property
    def MessageConfig(self):  # pragma: no cover
        return JourneyCustomMessage.make_one(self.boto3_raw_data["MessageConfig"])

    NextActivity = field("NextActivity")
    TemplateName = field("TemplateName")
    TemplateVersion = field("TemplateVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomMessageActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomMessageActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PushNotificationTemplateRequest:
    boto3_raw_data: "type_defs.PushNotificationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ADM(self):  # pragma: no cover
        return AndroidPushNotificationTemplate.make_one(self.boto3_raw_data["ADM"])

    @cached_property
    def APNS(self):  # pragma: no cover
        return APNSPushNotificationTemplate.make_one(self.boto3_raw_data["APNS"])

    @cached_property
    def Baidu(self):  # pragma: no cover
        return AndroidPushNotificationTemplate.make_one(self.boto3_raw_data["Baidu"])

    @cached_property
    def Default(self):  # pragma: no cover
        return DefaultPushNotificationTemplate.make_one(self.boto3_raw_data["Default"])

    DefaultSubstitutions = field("DefaultSubstitutions")

    @cached_property
    def GCM(self):  # pragma: no cover
        return AndroidPushNotificationTemplate.make_one(self.boto3_raw_data["GCM"])

    RecommenderId = field("RecommenderId")
    tags = field("tags")
    TemplateDescription = field("TemplateDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PushNotificationTemplateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PushNotificationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PushNotificationTemplateResponse:
    boto3_raw_data: "type_defs.PushNotificationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")
    TemplateName = field("TemplateName")
    TemplateType = field("TemplateType")

    @cached_property
    def ADM(self):  # pragma: no cover
        return AndroidPushNotificationTemplate.make_one(self.boto3_raw_data["ADM"])

    @cached_property
    def APNS(self):  # pragma: no cover
        return APNSPushNotificationTemplate.make_one(self.boto3_raw_data["APNS"])

    Arn = field("Arn")

    @cached_property
    def Baidu(self):  # pragma: no cover
        return AndroidPushNotificationTemplate.make_one(self.boto3_raw_data["Baidu"])

    @cached_property
    def Default(self):  # pragma: no cover
        return DefaultPushNotificationTemplate.make_one(self.boto3_raw_data["Default"])

    DefaultSubstitutions = field("DefaultSubstitutions")

    @cached_property
    def GCM(self):  # pragma: no cover
        return AndroidPushNotificationTemplate.make_one(self.boto3_raw_data["GCM"])

    RecommenderId = field("RecommenderId")
    tags = field("tags")
    TemplateDescription = field("TemplateDescription")
    Version = field("Version")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PushNotificationTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PushNotificationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEmailChannelResponse:
    boto3_raw_data: "type_defs.DeleteEmailChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def EmailChannelResponse(self):  # pragma: no cover
        return EmailChannelResponse.make_one(
            self.boto3_raw_data["EmailChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEmailChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEmailChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEmailChannelResponse:
    boto3_raw_data: "type_defs.GetEmailChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def EmailChannelResponse(self):  # pragma: no cover
        return EmailChannelResponse.make_one(
            self.boto3_raw_data["EmailChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEmailChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEmailChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEmailChannelResponse:
    boto3_raw_data: "type_defs.UpdateEmailChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def EmailChannelResponse(self):  # pragma: no cover
        return EmailChannelResponse.make_one(
            self.boto3_raw_data["EmailChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEmailChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEmailChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEmailTemplateResponse:
    boto3_raw_data: "type_defs.DeleteEmailTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEmailTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEmailTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInAppTemplateResponse:
    boto3_raw_data: "type_defs.DeleteInAppTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInAppTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInAppTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePushTemplateResponse:
    boto3_raw_data: "type_defs.DeletePushTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePushTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePushTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSmsTemplateResponse:
    boto3_raw_data: "type_defs.DeleteSmsTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSmsTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSmsTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceTemplateResponse:
    boto3_raw_data: "type_defs.DeleteVoiceTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVoiceTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEmailTemplateResponse:
    boto3_raw_data: "type_defs.UpdateEmailTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEmailTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEmailTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointResponse:
    boto3_raw_data: "type_defs.UpdateEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointsBatchResponse:
    boto3_raw_data: "type_defs.UpdateEndpointsBatchResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointsBatchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointsBatchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInAppTemplateResponse:
    boto3_raw_data: "type_defs.UpdateInAppTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInAppTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInAppTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePushTemplateResponse:
    boto3_raw_data: "type_defs.UpdatePushTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePushTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePushTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSmsTemplateResponse:
    boto3_raw_data: "type_defs.UpdateSmsTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSmsTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSmsTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTemplateActiveVersionResponse:
    boto3_raw_data: "type_defs.UpdateTemplateActiveVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTemplateActiveVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTemplateActiveVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceTemplateResponse:
    boto3_raw_data: "type_defs.UpdateVoiceTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageBody(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["MessageBody"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVoiceTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventStreamResponse:
    boto3_raw_data: "type_defs.DeleteEventStreamResponseTypeDef" = dataclasses.field()

    @cached_property
    def EventStream(self):  # pragma: no cover
        return EventStream.make_one(self.boto3_raw_data["EventStream"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventStreamResponse:
    boto3_raw_data: "type_defs.GetEventStreamResponseTypeDef" = dataclasses.field()

    @cached_property
    def EventStream(self):  # pragma: no cover
        return EventStream.make_one(self.boto3_raw_data["EventStream"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventStreamResponse:
    boto3_raw_data: "type_defs.PutEventStreamResponseTypeDef" = dataclasses.field()

    @cached_property
    def EventStream(self):  # pragma: no cover
        return EventStream.make_one(self.boto3_raw_data["EventStream"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEventStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGcmChannelResponse:
    boto3_raw_data: "type_defs.DeleteGcmChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def GCMChannelResponse(self):  # pragma: no cover
        return GCMChannelResponse.make_one(self.boto3_raw_data["GCMChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGcmChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGcmChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGcmChannelResponse:
    boto3_raw_data: "type_defs.GetGcmChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def GCMChannelResponse(self):  # pragma: no cover
        return GCMChannelResponse.make_one(self.boto3_raw_data["GCMChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGcmChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGcmChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGcmChannelResponse:
    boto3_raw_data: "type_defs.UpdateGcmChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def GCMChannelResponse(self):  # pragma: no cover
        return GCMChannelResponse.make_one(self.boto3_raw_data["GCMChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGcmChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGcmChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSmsChannelResponse:
    boto3_raw_data: "type_defs.DeleteSmsChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def SMSChannelResponse(self):  # pragma: no cover
        return SMSChannelResponse.make_one(self.boto3_raw_data["SMSChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSmsChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSmsChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSmsChannelResponse:
    boto3_raw_data: "type_defs.GetSmsChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def SMSChannelResponse(self):  # pragma: no cover
        return SMSChannelResponse.make_one(self.boto3_raw_data["SMSChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSmsChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSmsChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSmsChannelResponse:
    boto3_raw_data: "type_defs.UpdateSmsChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def SMSChannelResponse(self):  # pragma: no cover
        return SMSChannelResponse.make_one(self.boto3_raw_data["SMSChannelResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSmsChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSmsChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceChannelResponse:
    boto3_raw_data: "type_defs.DeleteVoiceChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceChannelResponse(self):  # pragma: no cover
        return VoiceChannelResponse.make_one(
            self.boto3_raw_data["VoiceChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVoiceChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceChannelResponse:
    boto3_raw_data: "type_defs.GetVoiceChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceChannelResponse(self):  # pragma: no cover
        return VoiceChannelResponse.make_one(
            self.boto3_raw_data["VoiceChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVoiceChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceChannelResponse:
    boto3_raw_data: "type_defs.UpdateVoiceChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceChannelResponse(self):  # pragma: no cover
        return VoiceChannelResponse.make_one(
            self.boto3_raw_data["VoiceChannelResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVoiceChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEmailChannelRequest:
    boto3_raw_data: "type_defs.UpdateEmailChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def EmailChannelRequest(self):  # pragma: no cover
        return EmailChannelRequest.make_one(self.boto3_raw_data["EmailChannelRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEmailChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEmailChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailMessageActivity:
    boto3_raw_data: "type_defs.EmailMessageActivityTypeDef" = dataclasses.field()

    @cached_property
    def MessageConfig(self):  # pragma: no cover
        return JourneyEmailMessage.make_one(self.boto3_raw_data["MessageConfig"])

    NextActivity = field("NextActivity")
    TemplateName = field("TemplateName")
    TemplateVersion = field("TemplateVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailMessageActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailMessageActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendUsersMessageResponse:
    boto3_raw_data: "type_defs.SendUsersMessageResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    RequestId = field("RequestId")
    Result = field("Result")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendUsersMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendUsersMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointResponse:
    boto3_raw_data: "type_defs.EndpointResponseTypeDef" = dataclasses.field()

    Address = field("Address")
    ApplicationId = field("ApplicationId")
    Attributes = field("Attributes")
    ChannelType = field("ChannelType")
    CohortId = field("CohortId")
    CreationDate = field("CreationDate")

    @cached_property
    def Demographic(self):  # pragma: no cover
        return EndpointDemographic.make_one(self.boto3_raw_data["Demographic"])

    EffectiveDate = field("EffectiveDate")
    EndpointStatus = field("EndpointStatus")
    Id = field("Id")

    @cached_property
    def Location(self):  # pragma: no cover
        return EndpointLocation.make_one(self.boto3_raw_data["Location"])

    Metrics = field("Metrics")
    OptOut = field("OptOut")
    RequestId = field("RequestId")

    @cached_property
    def User(self):  # pragma: no cover
        return EndpointUserOutput.make_one(self.boto3_raw_data["User"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDimensionsOutput:
    boto3_raw_data: "type_defs.EventDimensionsOutputTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def EventType(self):  # pragma: no cover
        return SetDimensionOutput.make_one(self.boto3_raw_data["EventType"])

    Metrics = field("Metrics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventDimensionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDimensionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentDemographicsOutput:
    boto3_raw_data: "type_defs.SegmentDemographicsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AppVersion(self):  # pragma: no cover
        return SetDimensionOutput.make_one(self.boto3_raw_data["AppVersion"])

    @cached_property
    def Channel(self):  # pragma: no cover
        return SetDimensionOutput.make_one(self.boto3_raw_data["Channel"])

    @cached_property
    def DeviceType(self):  # pragma: no cover
        return SetDimensionOutput.make_one(self.boto3_raw_data["DeviceType"])

    @cached_property
    def Make(self):  # pragma: no cover
        return SetDimensionOutput.make_one(self.boto3_raw_data["Make"])

    @cached_property
    def Model(self):  # pragma: no cover
        return SetDimensionOutput.make_one(self.boto3_raw_data["Model"])

    @cached_property
    def Platform(self):  # pragma: no cover
        return SetDimensionOutput.make_one(self.boto3_raw_data["Platform"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentDemographicsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentDemographicsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItemResponse:
    boto3_raw_data: "type_defs.ItemResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointItemResponse(self):  # pragma: no cover
        return EndpointItemResponse.make_one(
            self.boto3_raw_data["EndpointItemResponse"]
        )

    EventsItemResponse = field("EventsItemResponse")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ItemResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ItemResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    EventType = field("EventType")
    Timestamp = field("Timestamp")
    AppPackageName = field("AppPackageName")
    AppTitle = field("AppTitle")
    AppVersionCode = field("AppVersionCode")
    Attributes = field("Attributes")
    ClientSdkVersion = field("ClientSdkVersion")
    Metrics = field("Metrics")
    SdkName = field("SdkName")

    @cached_property
    def Session(self):  # pragma: no cover
        return Session.make_one(self.boto3_raw_data["Session"])

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
class ExportJobResponse:
    boto3_raw_data: "type_defs.ExportJobResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")

    @cached_property
    def Definition(self):  # pragma: no cover
        return ExportJobResource.make_one(self.boto3_raw_data["Definition"])

    Id = field("Id")
    JobStatus = field("JobStatus")
    Type = field("Type")
    CompletedPieces = field("CompletedPieces")
    CompletionDate = field("CompletionDate")
    FailedPieces = field("FailedPieces")
    Failures = field("Failures")
    TotalFailures = field("TotalFailures")
    TotalPieces = field("TotalPieces")
    TotalProcessed = field("TotalProcessed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGcmChannelRequest:
    boto3_raw_data: "type_defs.UpdateGcmChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def GCMChannelRequest(self):  # pragma: no cover
        return GCMChannelRequest.make_one(self.boto3_raw_data["GCMChannelRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGcmChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGcmChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GPSPointDimension:
    boto3_raw_data: "type_defs.GPSPointDimensionTypeDef" = dataclasses.field()

    @cached_property
    def Coordinates(self):  # pragma: no cover
        return GPSCoordinates.make_one(self.boto3_raw_data["Coordinates"])

    RangeInKilometers = field("RangeInKilometers")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GPSPointDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GPSPointDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationDateRangeKpiRequest:
    boto3_raw_data: "type_defs.GetApplicationDateRangeKpiRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    KpiName = field("KpiName")
    EndTime = field("EndTime")
    NextToken = field("NextToken")
    PageSize = field("PageSize")
    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationDateRangeKpiRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationDateRangeKpiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignDateRangeKpiRequest:
    boto3_raw_data: "type_defs.GetCampaignDateRangeKpiRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    CampaignId = field("CampaignId")
    KpiName = field("KpiName")
    EndTime = field("EndTime")
    NextToken = field("NextToken")
    PageSize = field("PageSize")
    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCampaignDateRangeKpiRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignDateRangeKpiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyDateRangeKpiRequest:
    boto3_raw_data: "type_defs.GetJourneyDateRangeKpiRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    JourneyId = field("JourneyId")
    KpiName = field("KpiName")
    EndTime = field("EndTime")
    NextToken = field("NextToken")
    PageSize = field("PageSize")
    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetJourneyDateRangeKpiRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyDateRangeKpiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneySchedule:
    boto3_raw_data: "type_defs.JourneyScheduleTypeDef" = dataclasses.field()

    EndTime = field("EndTime")
    StartTime = field("StartTime")
    Timezone = field("Timezone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JourneyScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JourneyScheduleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyExecutionActivityMetricsResponse:
    boto3_raw_data: "type_defs.GetJourneyExecutionActivityMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def JourneyExecutionActivityMetricsResponse(self):  # pragma: no cover
        return JourneyExecutionActivityMetricsResponse.make_one(
            self.boto3_raw_data["JourneyExecutionActivityMetricsResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetJourneyExecutionActivityMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyExecutionActivityMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyExecutionMetricsResponse:
    boto3_raw_data: "type_defs.GetJourneyExecutionMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def JourneyExecutionMetricsResponse(self):  # pragma: no cover
        return JourneyExecutionMetricsResponse.make_one(
            self.boto3_raw_data["JourneyExecutionMetricsResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetJourneyExecutionMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyExecutionMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyRunExecutionActivityMetricsResponse:
    boto3_raw_data: "type_defs.GetJourneyRunExecutionActivityMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def JourneyRunExecutionActivityMetricsResponse(self):  # pragma: no cover
        return JourneyRunExecutionActivityMetricsResponse.make_one(
            self.boto3_raw_data["JourneyRunExecutionActivityMetricsResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetJourneyRunExecutionActivityMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyRunExecutionActivityMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyRunExecutionMetricsResponse:
    boto3_raw_data: "type_defs.GetJourneyRunExecutionMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def JourneyRunExecutionMetricsResponse(self):  # pragma: no cover
        return JourneyRunExecutionMetricsResponse.make_one(
            self.boto3_raw_data["JourneyRunExecutionMetricsResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetJourneyRunExecutionMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyRunExecutionMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSmsTemplateResponse:
    boto3_raw_data: "type_defs.GetSmsTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def SMSTemplateResponse(self):  # pragma: no cover
        return SMSTemplateResponse.make_one(self.boto3_raw_data["SMSTemplateResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSmsTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSmsTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceTemplateResponse:
    boto3_raw_data: "type_defs.GetVoiceTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceTemplateResponse(self):  # pragma: no cover
        return VoiceTemplateResponse.make_one(
            self.boto3_raw_data["VoiceTemplateResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVoiceTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportJobResponse:
    boto3_raw_data: "type_defs.ImportJobResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    CreationDate = field("CreationDate")

    @cached_property
    def Definition(self):  # pragma: no cover
        return ImportJobResource.make_one(self.boto3_raw_data["Definition"])

    Id = field("Id")
    JobStatus = field("JobStatus")
    Type = field("Type")
    CompletedPieces = field("CompletedPieces")
    CompletionDate = field("CompletionDate")
    FailedPieces = field("FailedPieces")
    Failures = field("Failures")
    TotalFailures = field("TotalFailures")
    TotalPieces = field("TotalPieces")
    TotalProcessed = field("TotalProcessed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InAppMessageButton:
    boto3_raw_data: "type_defs.InAppMessageButtonTypeDef" = dataclasses.field()

    @cached_property
    def Android(self):  # pragma: no cover
        return OverrideButtonConfiguration.make_one(self.boto3_raw_data["Android"])

    @cached_property
    def DefaultConfig(self):  # pragma: no cover
        return DefaultButtonConfiguration.make_one(self.boto3_raw_data["DefaultConfig"])

    @cached_property
    def IOS(self):  # pragma: no cover
        return OverrideButtonConfiguration.make_one(self.boto3_raw_data["IOS"])

    @cached_property
    def Web(self):  # pragma: no cover
        return OverrideButtonConfiguration.make_one(self.boto3_raw_data["Web"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InAppMessageButtonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InAppMessageButtonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PushMessageActivity:
    boto3_raw_data: "type_defs.PushMessageActivityTypeDef" = dataclasses.field()

    @cached_property
    def MessageConfig(self):  # pragma: no cover
        return JourneyPushMessage.make_one(self.boto3_raw_data["MessageConfig"])

    NextActivity = field("NextActivity")
    TemplateName = field("TemplateName")
    TemplateVersion = field("TemplateVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PushMessageActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PushMessageActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyRunsResponse:
    boto3_raw_data: "type_defs.JourneyRunsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return JourneyRunResponse.make_many(self.boto3_raw_data["Item"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JourneyRunsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSMessageActivity:
    boto3_raw_data: "type_defs.SMSMessageActivityTypeDef" = dataclasses.field()

    @cached_property
    def MessageConfig(self):  # pragma: no cover
        return JourneySMSMessage.make_one(self.boto3_raw_data["MessageConfig"])

    NextActivity = field("NextActivity")
    TemplateName = field("TemplateName")
    TemplateVersion = field("TemplateVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SMSMessageActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMSMessageActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJourneyStateRequest:
    boto3_raw_data: "type_defs.UpdateJourneyStateRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    JourneyId = field("JourneyId")

    @cached_property
    def JourneyStateRequest(self):  # pragma: no cover
        return JourneyStateRequest.make_one(self.boto3_raw_data["JourneyStateRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJourneyStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJourneyStateRequestTypeDef"]
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

    @cached_property
    def TagsModel(self):  # pragma: no cover
        return TagsModelOutput.make_one(self.boto3_raw_data["TagsModel"])

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
class MessageResponse:
    boto3_raw_data: "type_defs.MessageResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EndpointResult = field("EndpointResult")
    RequestId = field("RequestId")
    Result = field("Result")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberValidateRequest:
    boto3_raw_data: "type_defs.PhoneNumberValidateRequestTypeDef" = dataclasses.field()

    @cached_property
    def NumberValidateRequest(self):  # pragma: no cover
        return NumberValidateRequest.make_one(
            self.boto3_raw_data["NumberValidateRequest"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberValidateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberValidateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberValidateResponse:
    boto3_raw_data: "type_defs.PhoneNumberValidateResponseTypeDef" = dataclasses.field()

    @cached_property
    def NumberValidateResponse(self):  # pragma: no cover
        return NumberValidateResponse.make_one(
            self.boto3_raw_data["NumberValidateResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberValidateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberValidateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenHoursOutput:
    boto3_raw_data: "type_defs.OpenHoursOutputTypeDef" = dataclasses.field()

    EMAIL = field("EMAIL")
    SMS = field("SMS")
    PUSH = field("PUSH")
    VOICE = field("VOICE")
    CUSTOM = field("CUSTOM")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpenHoursOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpenHoursOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenHours:
    boto3_raw_data: "type_defs.OpenHoursTypeDef" = dataclasses.field()

    EMAIL = field("EMAIL")
    SMS = field("SMS")
    PUSH = field("PUSH")
    VOICE = field("VOICE")
    CUSTOM = field("CUSTOM")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpenHoursTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpenHoursTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventStreamRequest:
    boto3_raw_data: "type_defs.PutEventStreamRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def WriteEventStream(self):  # pragma: no cover
        return WriteEventStream.make_one(self.boto3_raw_data["WriteEventStream"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEventStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RandomSplitActivityOutput:
    boto3_raw_data: "type_defs.RandomSplitActivityOutputTypeDef" = dataclasses.field()

    @cached_property
    def Branches(self):  # pragma: no cover
        return RandomSplitEntry.make_many(self.boto3_raw_data["Branches"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RandomSplitActivityOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RandomSplitActivityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RandomSplitActivity:
    boto3_raw_data: "type_defs.RandomSplitActivityTypeDef" = dataclasses.field()

    @cached_property
    def Branches(self):  # pragma: no cover
        return RandomSplitEntry.make_many(self.boto3_raw_data["Branches"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RandomSplitActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RandomSplitActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentBehaviors:
    boto3_raw_data: "type_defs.SegmentBehaviorsTypeDef" = dataclasses.field()

    @cached_property
    def Recency(self):  # pragma: no cover
        return RecencyDimension.make_one(self.boto3_raw_data["Recency"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentBehaviorsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentBehaviorsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAttributesRequest:
    boto3_raw_data: "type_defs.RemoveAttributesRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    AttributeType = field("AttributeType")

    @cached_property
    def UpdateAttributesRequest(self):  # pragma: no cover
        return UpdateAttributesRequest.make_one(
            self.boto3_raw_data["UpdateAttributesRequest"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultRow:
    boto3_raw_data: "type_defs.ResultRowTypeDef" = dataclasses.field()

    @cached_property
    def GroupedBys(self):  # pragma: no cover
        return ResultRowValue.make_many(self.boto3_raw_data["GroupedBys"])

    @cached_property
    def Values(self):  # pragma: no cover
        return ResultRowValue.make_many(self.boto3_raw_data["Values"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultRowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultRowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSmsChannelRequest:
    boto3_raw_data: "type_defs.UpdateSmsChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def SMSChannelRequest(self):  # pragma: no cover
        return SMSChannelRequest.make_one(self.boto3_raw_data["SMSChannelRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSmsChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSmsChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendOTPMessageRequest:
    boto3_raw_data: "type_defs.SendOTPMessageRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def SendOTPMessageRequestParameters(self):  # pragma: no cover
        return SendOTPMessageRequestParameters.make_one(
            self.boto3_raw_data["SendOTPMessageRequestParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendOTPMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendOTPMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleEmail:
    boto3_raw_data: "type_defs.SimpleEmailTypeDef" = dataclasses.field()

    @cached_property
    def HtmlPart(self):  # pragma: no cover
        return SimpleEmailPart.make_one(self.boto3_raw_data["HtmlPart"])

    @cached_property
    def Subject(self):  # pragma: no cover
        return SimpleEmailPart.make_one(self.boto3_raw_data["Subject"])

    @cached_property
    def TextPart(self):  # pragma: no cover
        return SimpleEmailPart.make_one(self.boto3_raw_data["TextPart"])

    @cached_property
    def Headers(self):  # pragma: no cover
        return MessageHeader.make_many(self.boto3_raw_data["Headers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SimpleEmailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SimpleEmailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTemplateActiveVersionRequest:
    boto3_raw_data: "type_defs.UpdateTemplateActiveVersionRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TemplateActiveVersionRequest(self):  # pragma: no cover
        return TemplateActiveVersionRequest.make_one(
            self.boto3_raw_data["TemplateActiveVersionRequest"]
        )

    TemplateName = field("TemplateName")
    TemplateType = field("TemplateType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTemplateActiveVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTemplateActiveVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateConfiguration:
    boto3_raw_data: "type_defs.TemplateConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def EmailTemplate(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["EmailTemplate"])

    @cached_property
    def PushTemplate(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["PushTemplate"])

    @cached_property
    def SMSTemplate(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["SMSTemplate"])

    @cached_property
    def VoiceTemplate(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["VoiceTemplate"])

    @cached_property
    def InAppTemplate(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["InAppTemplate"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplatesResponse:
    boto3_raw_data: "type_defs.TemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return TemplateResponse.make_many(self.boto3_raw_data["Item"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplatesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateVersionsResponse:
    boto3_raw_data: "type_defs.TemplateVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return TemplateVersionResponse.make_many(self.boto3_raw_data["Item"])

    Message = field("Message")
    NextToken = field("NextToken")
    RequestID = field("RequestID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecommenderConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateRecommenderConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    RecommenderId = field("RecommenderId")

    @cached_property
    def UpdateRecommenderConfiguration(self):  # pragma: no cover
        return UpdateRecommenderConfiguration.make_one(
            self.boto3_raw_data["UpdateRecommenderConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRecommenderConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecommenderConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceChannelRequest:
    boto3_raw_data: "type_defs.UpdateVoiceChannelRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def VoiceChannelRequest(self):  # pragma: no cover
        return VoiceChannelRequest.make_one(self.boto3_raw_data["VoiceChannelRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVoiceChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyOTPMessageResponse:
    boto3_raw_data: "type_defs.VerifyOTPMessageResponseTypeDef" = dataclasses.field()

    @cached_property
    def VerificationResponse(self):  # pragma: no cover
        return VerificationResponse.make_one(
            self.boto3_raw_data["VerificationResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyOTPMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyOTPMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyOTPMessageRequest:
    boto3_raw_data: "type_defs.VerifyOTPMessageRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def VerifyOTPMessageRequestParameters(self):  # pragma: no cover
        return VerifyOTPMessageRequestParameters.make_one(
            self.boto3_raw_data["VerifyOTPMessageRequestParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyOTPMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyOTPMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignActivitiesResponse:
    boto3_raw_data: "type_defs.GetCampaignActivitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ActivitiesResponse(self):  # pragma: no cover
        return ActivitiesResponse.make_one(self.boto3_raw_data["ActivitiesResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCampaignActivitiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignActivitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppsResponse:
    boto3_raw_data: "type_defs.GetAppsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationsResponse(self):  # pragma: no cover
        return ApplicationsResponse.make_one(
            self.boto3_raw_data["ApplicationsResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAppsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAppsResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSettingsResource:
    boto3_raw_data: "type_defs.ApplicationSettingsResourceTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def CampaignHook(self):  # pragma: no cover
        return CampaignHook.make_one(self.boto3_raw_data["CampaignHook"])

    LastModifiedDate = field("LastModifiedDate")

    @cached_property
    def Limits(self):  # pragma: no cover
        return CampaignLimits.make_one(self.boto3_raw_data["Limits"])

    @cached_property
    def QuietTime(self):  # pragma: no cover
        return QuietTime.make_one(self.boto3_raw_data["QuietTime"])

    @cached_property
    def JourneyLimits(self):  # pragma: no cover
        return ApplicationSettingsJourneyLimits.make_one(
            self.boto3_raw_data["JourneyLimits"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSettingsResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSettingsResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteApplicationSettingsRequest:
    boto3_raw_data: "type_defs.WriteApplicationSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CampaignHook(self):  # pragma: no cover
        return CampaignHook.make_one(self.boto3_raw_data["CampaignHook"])

    CloudWatchMetricsEnabled = field("CloudWatchMetricsEnabled")
    EventTaggingEnabled = field("EventTaggingEnabled")

    @cached_property
    def Limits(self):  # pragma: no cover
        return CampaignLimits.make_one(self.boto3_raw_data["Limits"])

    @cached_property
    def QuietTime(self):  # pragma: no cover
        return QuietTime.make_one(self.boto3_raw_data["QuietTime"])

    @cached_property
    def JourneyLimits(self):  # pragma: no cover
        return ApplicationSettingsJourneyLimits.make_one(
            self.boto3_raw_data["JourneyLimits"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WriteApplicationSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteApplicationSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEmailTemplateRequest:
    boto3_raw_data: "type_defs.CreateEmailTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def EmailTemplateRequest(self):  # pragma: no cover
        return EmailTemplateRequest.make_one(
            self.boto3_raw_data["EmailTemplateRequest"]
        )

    TemplateName = field("TemplateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEmailTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEmailTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEmailTemplateRequest:
    boto3_raw_data: "type_defs.UpdateEmailTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def EmailTemplateRequest(self):  # pragma: no cover
        return EmailTemplateRequest.make_one(
            self.boto3_raw_data["EmailTemplateRequest"]
        )

    TemplateName = field("TemplateName")
    CreateNewVersion = field("CreateNewVersion")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEmailTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEmailTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEmailTemplateResponse:
    boto3_raw_data: "type_defs.GetEmailTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def EmailTemplateResponse(self):  # pragma: no cover
        return EmailTemplateResponse.make_one(
            self.boto3_raw_data["EmailTemplateResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEmailTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEmailTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelsResponse:
    boto3_raw_data: "type_defs.GetChannelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChannelsResponse(self):  # pragma: no cover
        return ChannelsResponse.make_one(self.boto3_raw_data["ChannelsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommenderConfigurationsResponse:
    boto3_raw_data: "type_defs.GetRecommenderConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ListRecommenderConfigurationsResponse(self):  # pragma: no cover
        return ListRecommenderConfigurationsResponse.make_one(
            self.boto3_raw_data["ListRecommenderConfigurationsResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommenderConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommenderConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePushTemplateRequest:
    boto3_raw_data: "type_defs.CreatePushTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def PushNotificationTemplateRequest(self):  # pragma: no cover
        return PushNotificationTemplateRequest.make_one(
            self.boto3_raw_data["PushNotificationTemplateRequest"]
        )

    TemplateName = field("TemplateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePushTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePushTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePushTemplateRequest:
    boto3_raw_data: "type_defs.UpdatePushTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def PushNotificationTemplateRequest(self):  # pragma: no cover
        return PushNotificationTemplateRequest.make_one(
            self.boto3_raw_data["PushNotificationTemplateRequest"]
        )

    TemplateName = field("TemplateName")
    CreateNewVersion = field("CreateNewVersion")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePushTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePushTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPushTemplateResponse:
    boto3_raw_data: "type_defs.GetPushTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def PushNotificationTemplateResponse(self):  # pragma: no cover
        return PushNotificationTemplateResponse.make_one(
            self.boto3_raw_data["PushNotificationTemplateResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPushTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPushTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendUsersMessagesResponse:
    boto3_raw_data: "type_defs.SendUsersMessagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def SendUsersMessageResponse(self):  # pragma: no cover
        return SendUsersMessageResponse.make_one(
            self.boto3_raw_data["SendUsersMessageResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendUsersMessagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendUsersMessagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEndpointResponse:
    boto3_raw_data: "type_defs.DeleteEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointResponse(self):  # pragma: no cover
        return EndpointResponse.make_one(self.boto3_raw_data["EndpointResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointsResponse:
    boto3_raw_data: "type_defs.EndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return EndpointResponse.make_many(self.boto3_raw_data["Item"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEndpointResponse:
    boto3_raw_data: "type_defs.GetEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointResponse(self):  # pragma: no cover
        return EndpointResponse.make_one(self.boto3_raw_data["EndpointResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointBatchItem:
    boto3_raw_data: "type_defs.EndpointBatchItemTypeDef" = dataclasses.field()

    Address = field("Address")
    Attributes = field("Attributes")
    ChannelType = field("ChannelType")

    @cached_property
    def Demographic(self):  # pragma: no cover
        return EndpointDemographic.make_one(self.boto3_raw_data["Demographic"])

    EffectiveDate = field("EffectiveDate")
    EndpointStatus = field("EndpointStatus")
    Id = field("Id")

    @cached_property
    def Location(self):  # pragma: no cover
        return EndpointLocation.make_one(self.boto3_raw_data["Location"])

    Metrics = field("Metrics")
    OptOut = field("OptOut")
    RequestId = field("RequestId")
    User = field("User")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointBatchItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointBatchItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointRequest:
    boto3_raw_data: "type_defs.EndpointRequestTypeDef" = dataclasses.field()

    Address = field("Address")
    Attributes = field("Attributes")
    ChannelType = field("ChannelType")

    @cached_property
    def Demographic(self):  # pragma: no cover
        return EndpointDemographic.make_one(self.boto3_raw_data["Demographic"])

    EffectiveDate = field("EffectiveDate")
    EndpointStatus = field("EndpointStatus")

    @cached_property
    def Location(self):  # pragma: no cover
        return EndpointLocation.make_one(self.boto3_raw_data["Location"])

    Metrics = field("Metrics")
    OptOut = field("OptOut")
    RequestId = field("RequestId")
    User = field("User")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicEndpoint:
    boto3_raw_data: "type_defs.PublicEndpointTypeDef" = dataclasses.field()

    Address = field("Address")
    Attributes = field("Attributes")
    ChannelType = field("ChannelType")

    @cached_property
    def Demographic(self):  # pragma: no cover
        return EndpointDemographic.make_one(self.boto3_raw_data["Demographic"])

    EffectiveDate = field("EffectiveDate")
    EndpointStatus = field("EndpointStatus")

    @cached_property
    def Location(self):  # pragma: no cover
        return EndpointLocation.make_one(self.boto3_raw_data["Location"])

    Metrics = field("Metrics")
    OptOut = field("OptOut")
    RequestId = field("RequestId")
    User = field("User")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublicEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PublicEndpointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignEventFilterOutput:
    boto3_raw_data: "type_defs.CampaignEventFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return EventDimensionsOutput.make_one(self.boto3_raw_data["Dimensions"])

    FilterType = field("FilterType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignEventFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignEventFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventConditionOutput:
    boto3_raw_data: "type_defs.EventConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return EventDimensionsOutput.make_one(self.boto3_raw_data["Dimensions"])

    MessageActivity = field("MessageActivity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventFilterOutput:
    boto3_raw_data: "type_defs.EventFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return EventDimensionsOutput.make_one(self.boto3_raw_data["Dimensions"])

    FilterType = field("FilterType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventsResponse:
    boto3_raw_data: "type_defs.EventsResponseTypeDef" = dataclasses.field()

    Results = field("Results")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventsResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExportJobResponse:
    boto3_raw_data: "type_defs.CreateExportJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def ExportJobResponse(self):  # pragma: no cover
        return ExportJobResponse.make_one(self.boto3_raw_data["ExportJobResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportJobsResponse:
    boto3_raw_data: "type_defs.ExportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return ExportJobResponse.make_many(self.boto3_raw_data["Item"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportJobResponse:
    boto3_raw_data: "type_defs.GetExportJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def ExportJobResponse(self):  # pragma: no cover
        return ExportJobResponse.make_one(self.boto3_raw_data["ExportJobResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentLocationOutput:
    boto3_raw_data: "type_defs.SegmentLocationOutputTypeDef" = dataclasses.field()

    @cached_property
    def Country(self):  # pragma: no cover
        return SetDimensionOutput.make_one(self.boto3_raw_data["Country"])

    @cached_property
    def GPSPoint(self):  # pragma: no cover
        return GPSPointDimension.make_one(self.boto3_raw_data["GPSPoint"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentLocationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentLocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImportJobResponse:
    boto3_raw_data: "type_defs.CreateImportJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def ImportJobResponse(self):  # pragma: no cover
        return ImportJobResponse.make_one(self.boto3_raw_data["ImportJobResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportJobResponse:
    boto3_raw_data: "type_defs.GetImportJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def ImportJobResponse(self):  # pragma: no cover
        return ImportJobResponse.make_one(self.boto3_raw_data["ImportJobResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportJobsResponse:
    boto3_raw_data: "type_defs.ImportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return ImportJobResponse.make_many(self.boto3_raw_data["Item"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InAppMessageContent:
    boto3_raw_data: "type_defs.InAppMessageContentTypeDef" = dataclasses.field()

    BackgroundColor = field("BackgroundColor")

    @cached_property
    def BodyConfig(self):  # pragma: no cover
        return InAppMessageBodyConfig.make_one(self.boto3_raw_data["BodyConfig"])

    @cached_property
    def HeaderConfig(self):  # pragma: no cover
        return InAppMessageHeaderConfig.make_one(self.boto3_raw_data["HeaderConfig"])

    ImageUrl = field("ImageUrl")

    @cached_property
    def PrimaryBtn(self):  # pragma: no cover
        return InAppMessageButton.make_one(self.boto3_raw_data["PrimaryBtn"])

    @cached_property
    def SecondaryBtn(self):  # pragma: no cover
        return InAppMessageButton.make_one(self.boto3_raw_data["SecondaryBtn"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InAppMessageContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InAppMessageContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyRunsResponse:
    boto3_raw_data: "type_defs.GetJourneyRunsResponseTypeDef" = dataclasses.field()

    @cached_property
    def JourneyRunsResponse(self):  # pragma: no cover
        return JourneyRunsResponse.make_one(self.boto3_raw_data["JourneyRunsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJourneyRunsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessagesResponse:
    boto3_raw_data: "type_defs.SendMessagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageResponse(self):  # pragma: no cover
        return MessageResponse.make_one(self.boto3_raw_data["MessageResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendOTPMessageResponse:
    boto3_raw_data: "type_defs.SendOTPMessageResponseTypeDef" = dataclasses.field()

    @cached_property
    def MessageResponse(self):  # pragma: no cover
        return MessageResponse.make_one(self.boto3_raw_data["MessageResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendOTPMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendOTPMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaseKpiResult:
    boto3_raw_data: "type_defs.BaseKpiResultTypeDef" = dataclasses.field()

    @cached_property
    def Rows(self):  # pragma: no cover
        return ResultRow.make_many(self.boto3_raw_data["Rows"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BaseKpiResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BaseKpiResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDimensions:
    boto3_raw_data: "type_defs.EventDimensionsTypeDef" = dataclasses.field()

    Attributes = field("Attributes")
    EventType = field("EventType")
    Metrics = field("Metrics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventDimensionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventDimensionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentDemographics:
    boto3_raw_data: "type_defs.SegmentDemographicsTypeDef" = dataclasses.field()

    AppVersion = field("AppVersion")
    Channel = field("Channel")
    DeviceType = field("DeviceType")
    Make = field("Make")
    Model = field("Model")
    Platform = field("Platform")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentDemographicsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentDemographicsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentLocation:
    boto3_raw_data: "type_defs.SegmentLocationTypeDef" = dataclasses.field()

    Country = field("Country")

    @cached_property
    def GPSPoint(self):  # pragma: no cover
        return GPSPointDimension.make_one(self.boto3_raw_data["GPSPoint"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SegmentLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailMessage:
    boto3_raw_data: "type_defs.EmailMessageTypeDef" = dataclasses.field()

    Body = field("Body")
    FeedbackForwardingAddress = field("FeedbackForwardingAddress")
    FromAddress = field("FromAddress")

    @cached_property
    def RawEmail(self):  # pragma: no cover
        return RawEmail.make_one(self.boto3_raw_data["RawEmail"])

    ReplyToAddresses = field("ReplyToAddresses")

    @cached_property
    def SimpleEmail(self):  # pragma: no cover
        return SimpleEmail.make_one(self.boto3_raw_data["SimpleEmail"])

    Substitutions = field("Substitutions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailMessageTypeDef"]],
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
    TagsModel = field("TagsModel")

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
class ListTemplatesResponse:
    boto3_raw_data: "type_defs.ListTemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def TemplatesResponse(self):  # pragma: no cover
        return TemplatesResponse.make_one(self.boto3_raw_data["TemplatesResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateVersionsResponse:
    boto3_raw_data: "type_defs.ListTemplateVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TemplateVersionsResponse(self):  # pragma: no cover
        return TemplateVersionsResponse.make_one(
            self.boto3_raw_data["TemplateVersionsResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplateVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationSettingsResponse:
    boto3_raw_data: "type_defs.GetApplicationSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationSettingsResource(self):  # pragma: no cover
        return ApplicationSettingsResource.make_one(
            self.boto3_raw_data["ApplicationSettingsResource"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetApplicationSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationSettingsResponse:
    boto3_raw_data: "type_defs.UpdateApplicationSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationSettingsResource(self):  # pragma: no cover
        return ApplicationSettingsResource.make_one(
            self.boto3_raw_data["ApplicationSettingsResource"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApplicationSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationSettingsRequest:
    boto3_raw_data: "type_defs.UpdateApplicationSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")

    @cached_property
    def WriteApplicationSettingsRequest(self):  # pragma: no cover
        return WriteApplicationSettingsRequest.make_one(
            self.boto3_raw_data["WriteApplicationSettingsRequest"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateApplicationSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserEndpointsResponse:
    boto3_raw_data: "type_defs.DeleteUserEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointsResponse(self):  # pragma: no cover
        return EndpointsResponse.make_one(self.boto3_raw_data["EndpointsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserEndpointsResponse:
    boto3_raw_data: "type_defs.GetUserEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointsResponse(self):  # pragma: no cover
        return EndpointsResponse.make_one(self.boto3_raw_data["EndpointsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointBatchRequest:
    boto3_raw_data: "type_defs.EndpointBatchRequestTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return EndpointBatchItem.make_many(self.boto3_raw_data["Item"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointBatchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointRequest:
    boto3_raw_data: "type_defs.UpdateEndpointRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EndpointId = field("EndpointId")

    @cached_property
    def EndpointRequest(self):  # pragma: no cover
        return EndpointRequest.make_one(self.boto3_raw_data["EndpointRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventsBatch:
    boto3_raw_data: "type_defs.EventsBatchTypeDef" = dataclasses.field()

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return PublicEndpoint.make_one(self.boto3_raw_data["Endpoint"])

    Events = field("Events")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventsBatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventsBatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InAppCampaignSchedule:
    boto3_raw_data: "type_defs.InAppCampaignScheduleTypeDef" = dataclasses.field()

    EndDate = field("EndDate")

    @cached_property
    def EventFilter(self):  # pragma: no cover
        return CampaignEventFilterOutput.make_one(self.boto3_raw_data["EventFilter"])

    @cached_property
    def QuietTime(self):  # pragma: no cover
        return QuietTime.make_one(self.boto3_raw_data["QuietTime"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InAppCampaignScheduleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InAppCampaignScheduleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleOutput:
    boto3_raw_data: "type_defs.ScheduleOutputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def EventFilter(self):  # pragma: no cover
        return CampaignEventFilterOutput.make_one(self.boto3_raw_data["EventFilter"])

    Frequency = field("Frequency")
    IsLocalTime = field("IsLocalTime")

    @cached_property
    def QuietTime(self):  # pragma: no cover
        return QuietTime.make_one(self.boto3_raw_data["QuietTime"])

    Timezone = field("Timezone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventStartConditionOutput:
    boto3_raw_data: "type_defs.EventStartConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def EventFilter(self):  # pragma: no cover
        return EventFilterOutput.make_one(self.boto3_raw_data["EventFilter"])

    SegmentId = field("SegmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventStartConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventStartConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventsResponse:
    boto3_raw_data: "type_defs.PutEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EventsResponse(self):  # pragma: no cover
        return EventsResponse.make_one(self.boto3_raw_data["EventsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutEventsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportJobsResponse:
    boto3_raw_data: "type_defs.GetExportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ExportJobsResponse(self):  # pragma: no cover
        return ExportJobsResponse.make_one(self.boto3_raw_data["ExportJobsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentExportJobsResponse:
    boto3_raw_data: "type_defs.GetSegmentExportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ExportJobsResponse(self):  # pragma: no cover
        return ExportJobsResponse.make_one(self.boto3_raw_data["ExportJobsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentExportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentDimensionsOutput:
    boto3_raw_data: "type_defs.SegmentDimensionsOutputTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def Behavior(self):  # pragma: no cover
        return SegmentBehaviors.make_one(self.boto3_raw_data["Behavior"])

    @cached_property
    def Demographic(self):  # pragma: no cover
        return SegmentDemographicsOutput.make_one(self.boto3_raw_data["Demographic"])

    @cached_property
    def Location(self):  # pragma: no cover
        return SegmentLocationOutput.make_one(self.boto3_raw_data["Location"])

    Metrics = field("Metrics")
    UserAttributes = field("UserAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentDimensionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentDimensionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportJobsResponse:
    boto3_raw_data: "type_defs.GetImportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ImportJobsResponse(self):  # pragma: no cover
        return ImportJobsResponse.make_one(self.boto3_raw_data["ImportJobsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentImportJobsResponse:
    boto3_raw_data: "type_defs.GetSegmentImportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ImportJobsResponse(self):  # pragma: no cover
        return ImportJobsResponse.make_one(self.boto3_raw_data["ImportJobsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentImportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignInAppMessageOutput:
    boto3_raw_data: "type_defs.CampaignInAppMessageOutputTypeDef" = dataclasses.field()

    Body = field("Body")

    @cached_property
    def Content(self):  # pragma: no cover
        return InAppMessageContent.make_many(self.boto3_raw_data["Content"])

    CustomConfig = field("CustomConfig")
    Layout = field("Layout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignInAppMessageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignInAppMessageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignInAppMessage:
    boto3_raw_data: "type_defs.CampaignInAppMessageTypeDef" = dataclasses.field()

    Body = field("Body")

    @cached_property
    def Content(self):  # pragma: no cover
        return InAppMessageContent.make_many(self.boto3_raw_data["Content"])

    CustomConfig = field("CustomConfig")
    Layout = field("Layout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignInAppMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignInAppMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InAppMessage:
    boto3_raw_data: "type_defs.InAppMessageTypeDef" = dataclasses.field()

    @cached_property
    def Content(self):  # pragma: no cover
        return InAppMessageContent.make_many(self.boto3_raw_data["Content"])

    CustomConfig = field("CustomConfig")
    Layout = field("Layout")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InAppMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InAppMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InAppTemplateRequest:
    boto3_raw_data: "type_defs.InAppTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def Content(self):  # pragma: no cover
        return InAppMessageContent.make_many(self.boto3_raw_data["Content"])

    CustomConfig = field("CustomConfig")
    Layout = field("Layout")
    tags = field("tags")
    TemplateDescription = field("TemplateDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InAppTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InAppTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InAppTemplateResponse:
    boto3_raw_data: "type_defs.InAppTemplateResponseTypeDef" = dataclasses.field()

    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")
    TemplateName = field("TemplateName")
    TemplateType = field("TemplateType")
    Arn = field("Arn")

    @cached_property
    def Content(self):  # pragma: no cover
        return InAppMessageContent.make_many(self.boto3_raw_data["Content"])

    CustomConfig = field("CustomConfig")
    Layout = field("Layout")
    tags = field("tags")
    TemplateDescription = field("TemplateDescription")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InAppTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InAppTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationDateRangeKpiResponse:
    boto3_raw_data: "type_defs.ApplicationDateRangeKpiResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    EndTime = field("EndTime")
    KpiName = field("KpiName")

    @cached_property
    def KpiResult(self):  # pragma: no cover
        return BaseKpiResult.make_one(self.boto3_raw_data["KpiResult"])

    StartTime = field("StartTime")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationDateRangeKpiResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationDateRangeKpiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignDateRangeKpiResponse:
    boto3_raw_data: "type_defs.CampaignDateRangeKpiResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    CampaignId = field("CampaignId")
    EndTime = field("EndTime")
    KpiName = field("KpiName")

    @cached_property
    def KpiResult(self):  # pragma: no cover
        return BaseKpiResult.make_one(self.boto3_raw_data["KpiResult"])

    StartTime = field("StartTime")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignDateRangeKpiResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignDateRangeKpiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyDateRangeKpiResponse:
    boto3_raw_data: "type_defs.JourneyDateRangeKpiResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EndTime = field("EndTime")
    JourneyId = field("JourneyId")
    KpiName = field("KpiName")

    @cached_property
    def KpiResult(self):  # pragma: no cover
        return BaseKpiResult.make_one(self.boto3_raw_data["KpiResult"])

    StartTime = field("StartTime")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JourneyDateRangeKpiResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneyDateRangeKpiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectMessageConfiguration:
    boto3_raw_data: "type_defs.DirectMessageConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ADMMessage(self):  # pragma: no cover
        return ADMMessage.make_one(self.boto3_raw_data["ADMMessage"])

    @cached_property
    def APNSMessage(self):  # pragma: no cover
        return APNSMessage.make_one(self.boto3_raw_data["APNSMessage"])

    @cached_property
    def BaiduMessage(self):  # pragma: no cover
        return BaiduMessage.make_one(self.boto3_raw_data["BaiduMessage"])

    @cached_property
    def DefaultMessage(self):  # pragma: no cover
        return DefaultMessage.make_one(self.boto3_raw_data["DefaultMessage"])

    @cached_property
    def DefaultPushNotificationMessage(self):  # pragma: no cover
        return DefaultPushNotificationMessage.make_one(
            self.boto3_raw_data["DefaultPushNotificationMessage"]
        )

    @cached_property
    def EmailMessage(self):  # pragma: no cover
        return EmailMessage.make_one(self.boto3_raw_data["EmailMessage"])

    @cached_property
    def GCMMessage(self):  # pragma: no cover
        return GCMMessage.make_one(self.boto3_raw_data["GCMMessage"])

    @cached_property
    def SMSMessage(self):  # pragma: no cover
        return SMSMessage.make_one(self.boto3_raw_data["SMSMessage"])

    @cached_property
    def VoiceMessage(self):  # pragma: no cover
        return VoiceMessage.make_one(self.boto3_raw_data["VoiceMessage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectMessageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectMessageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointsBatchRequest:
    boto3_raw_data: "type_defs.UpdateEndpointsBatchRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def EndpointBatchRequest(self):  # pragma: no cover
        return EndpointBatchRequest.make_one(
            self.boto3_raw_data["EndpointBatchRequest"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointsBatchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointsBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventsRequest:
    boto3_raw_data: "type_defs.EventsRequestTypeDef" = dataclasses.field()

    BatchItem = field("BatchItem")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartConditionOutput:
    boto3_raw_data: "type_defs.StartConditionOutputTypeDef" = dataclasses.field()

    Description = field("Description")

    @cached_property
    def EventStartCondition(self):  # pragma: no cover
        return EventStartConditionOutput.make_one(
            self.boto3_raw_data["EventStartCondition"]
        )

    @cached_property
    def SegmentStartCondition(self):  # pragma: no cover
        return SegmentCondition.make_one(self.boto3_raw_data["SegmentStartCondition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentGroupOutput:
    boto3_raw_data: "type_defs.SegmentGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return SegmentDimensionsOutput.make_many(self.boto3_raw_data["Dimensions"])

    @cached_property
    def SourceSegments(self):  # pragma: no cover
        return SegmentReference.make_many(self.boto3_raw_data["SourceSegments"])

    SourceType = field("SourceType")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleConditionOutput:
    boto3_raw_data: "type_defs.SimpleConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def EventCondition(self):  # pragma: no cover
        return EventConditionOutput.make_one(self.boto3_raw_data["EventCondition"])

    @cached_property
    def SegmentCondition(self):  # pragma: no cover
        return SegmentCondition.make_one(self.boto3_raw_data["SegmentCondition"])

    @cached_property
    def SegmentDimensions(self):  # pragma: no cover
        return SegmentDimensionsOutput.make_one(
            self.boto3_raw_data["SegmentDimensions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimpleConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimpleConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageConfigurationOutput:
    boto3_raw_data: "type_defs.MessageConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def ADMMessage(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["ADMMessage"])

    @cached_property
    def APNSMessage(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["APNSMessage"])

    @cached_property
    def BaiduMessage(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["BaiduMessage"])

    @cached_property
    def CustomMessage(self):  # pragma: no cover
        return CampaignCustomMessage.make_one(self.boto3_raw_data["CustomMessage"])

    @cached_property
    def DefaultMessage(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["DefaultMessage"])

    @cached_property
    def EmailMessage(self):  # pragma: no cover
        return CampaignEmailMessageOutput.make_one(self.boto3_raw_data["EmailMessage"])

    @cached_property
    def GCMMessage(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["GCMMessage"])

    @cached_property
    def SMSMessage(self):  # pragma: no cover
        return CampaignSmsMessage.make_one(self.boto3_raw_data["SMSMessage"])

    @cached_property
    def InAppMessage(self):  # pragma: no cover
        return CampaignInAppMessageOutput.make_one(self.boto3_raw_data["InAppMessage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InAppMessageCampaign:
    boto3_raw_data: "type_defs.InAppMessageCampaignTypeDef" = dataclasses.field()

    CampaignId = field("CampaignId")
    DailyCap = field("DailyCap")

    @cached_property
    def InAppMessage(self):  # pragma: no cover
        return InAppMessage.make_one(self.boto3_raw_data["InAppMessage"])

    Priority = field("Priority")

    @cached_property
    def Schedule(self):  # pragma: no cover
        return InAppCampaignSchedule.make_one(self.boto3_raw_data["Schedule"])

    SessionCap = field("SessionCap")
    TotalCap = field("TotalCap")
    TreatmentId = field("TreatmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InAppMessageCampaignTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InAppMessageCampaignTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInAppTemplateRequest:
    boto3_raw_data: "type_defs.CreateInAppTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def InAppTemplateRequest(self):  # pragma: no cover
        return InAppTemplateRequest.make_one(
            self.boto3_raw_data["InAppTemplateRequest"]
        )

    TemplateName = field("TemplateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInAppTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInAppTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInAppTemplateRequest:
    boto3_raw_data: "type_defs.UpdateInAppTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def InAppTemplateRequest(self):  # pragma: no cover
        return InAppTemplateRequest.make_one(
            self.boto3_raw_data["InAppTemplateRequest"]
        )

    TemplateName = field("TemplateName")
    CreateNewVersion = field("CreateNewVersion")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInAppTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInAppTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInAppTemplateResponse:
    boto3_raw_data: "type_defs.GetInAppTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def InAppTemplateResponse(self):  # pragma: no cover
        return InAppTemplateResponse.make_one(
            self.boto3_raw_data["InAppTemplateResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInAppTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInAppTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationDateRangeKpiResponse:
    boto3_raw_data: "type_defs.GetApplicationDateRangeKpiResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationDateRangeKpiResponse(self):  # pragma: no cover
        return ApplicationDateRangeKpiResponse.make_one(
            self.boto3_raw_data["ApplicationDateRangeKpiResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationDateRangeKpiResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationDateRangeKpiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignDateRangeKpiResponse:
    boto3_raw_data: "type_defs.GetCampaignDateRangeKpiResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CampaignDateRangeKpiResponse(self):  # pragma: no cover
        return CampaignDateRangeKpiResponse.make_one(
            self.boto3_raw_data["CampaignDateRangeKpiResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCampaignDateRangeKpiResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignDateRangeKpiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyDateRangeKpiResponse:
    boto3_raw_data: "type_defs.GetJourneyDateRangeKpiResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def JourneyDateRangeKpiResponse(self):  # pragma: no cover
        return JourneyDateRangeKpiResponse.make_one(
            self.boto3_raw_data["JourneyDateRangeKpiResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetJourneyDateRangeKpiResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyDateRangeKpiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignEventFilter:
    boto3_raw_data: "type_defs.CampaignEventFilterTypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")
    FilterType = field("FilterType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignEventFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignEventFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventCondition:
    boto3_raw_data: "type_defs.EventConditionTypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")
    MessageActivity = field("MessageActivity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventFilter:
    boto3_raw_data: "type_defs.EventFilterTypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")
    FilterType = field("FilterType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentDimensions:
    boto3_raw_data: "type_defs.SegmentDimensionsTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def Behavior(self):  # pragma: no cover
        return SegmentBehaviors.make_one(self.boto3_raw_data["Behavior"])

    Demographic = field("Demographic")
    Location = field("Location")
    Metrics = field("Metrics")
    UserAttributes = field("UserAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentDimensionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentDimensionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageRequest:
    boto3_raw_data: "type_defs.MessageRequestTypeDef" = dataclasses.field()

    @cached_property
    def MessageConfiguration(self):  # pragma: no cover
        return DirectMessageConfiguration.make_one(
            self.boto3_raw_data["MessageConfiguration"]
        )

    Addresses = field("Addresses")
    Context = field("Context")
    Endpoints = field("Endpoints")

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfiguration.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    TraceId = field("TraceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendUsersMessageRequest:
    boto3_raw_data: "type_defs.SendUsersMessageRequestTypeDef" = dataclasses.field()

    @cached_property
    def MessageConfiguration(self):  # pragma: no cover
        return DirectMessageConfiguration.make_one(
            self.boto3_raw_data["MessageConfiguration"]
        )

    Users = field("Users")
    Context = field("Context")

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfiguration.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    TraceId = field("TraceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendUsersMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendUsersMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventsRequest:
    boto3_raw_data: "type_defs.PutEventsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def EventsRequest(self):  # pragma: no cover
        return EventsRequest.make_one(self.boto3_raw_data["EventsRequest"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutEventsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentGroupListOutput:
    boto3_raw_data: "type_defs.SegmentGroupListOutputTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return SegmentGroupOutput.make_many(self.boto3_raw_data["Groups"])

    Include = field("Include")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentGroupListOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentGroupListOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionOutput:
    boto3_raw_data: "type_defs.ConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Conditions(self):  # pragma: no cover
        return SimpleConditionOutput.make_many(self.boto3_raw_data["Conditions"])

    Operator = field("Operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiConditionalBranchOutput:
    boto3_raw_data: "type_defs.MultiConditionalBranchOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Condition(self):  # pragma: no cover
        return SimpleConditionOutput.make_one(self.boto3_raw_data["Condition"])

    NextActivity = field("NextActivity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiConditionalBranchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiConditionalBranchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TreatmentResource:
    boto3_raw_data: "type_defs.TreatmentResourceTypeDef" = dataclasses.field()

    Id = field("Id")
    SizePercent = field("SizePercent")

    @cached_property
    def CustomDeliveryConfiguration(self):  # pragma: no cover
        return CustomDeliveryConfigurationOutput.make_one(
            self.boto3_raw_data["CustomDeliveryConfiguration"]
        )

    @cached_property
    def MessageConfiguration(self):  # pragma: no cover
        return MessageConfigurationOutput.make_one(
            self.boto3_raw_data["MessageConfiguration"]
        )

    @cached_property
    def Schedule(self):  # pragma: no cover
        return ScheduleOutput.make_one(self.boto3_raw_data["Schedule"])

    @cached_property
    def State(self):  # pragma: no cover
        return CampaignState.make_one(self.boto3_raw_data["State"])

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfiguration.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    TreatmentDescription = field("TreatmentDescription")
    TreatmentName = field("TreatmentName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TreatmentResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TreatmentResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageConfiguration:
    boto3_raw_data: "type_defs.MessageConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ADMMessage(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["ADMMessage"])

    @cached_property
    def APNSMessage(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["APNSMessage"])

    @cached_property
    def BaiduMessage(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["BaiduMessage"])

    @cached_property
    def CustomMessage(self):  # pragma: no cover
        return CampaignCustomMessage.make_one(self.boto3_raw_data["CustomMessage"])

    @cached_property
    def DefaultMessage(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["DefaultMessage"])

    EmailMessage = field("EmailMessage")

    @cached_property
    def GCMMessage(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["GCMMessage"])

    @cached_property
    def SMSMessage(self):  # pragma: no cover
        return CampaignSmsMessage.make_one(self.boto3_raw_data["SMSMessage"])

    InAppMessage = field("InAppMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InAppMessagesResponse:
    boto3_raw_data: "type_defs.InAppMessagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def InAppMessageCampaigns(self):  # pragma: no cover
        return InAppMessageCampaign.make_many(
            self.boto3_raw_data["InAppMessageCampaigns"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InAppMessagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InAppMessagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessagesRequest:
    boto3_raw_data: "type_defs.SendMessagesRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def MessageRequest(self):  # pragma: no cover
        return MessageRequest.make_one(self.boto3_raw_data["MessageRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendUsersMessagesRequest:
    boto3_raw_data: "type_defs.SendUsersMessagesRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def SendUsersMessageRequest(self):  # pragma: no cover
        return SendUsersMessageRequest.make_one(
            self.boto3_raw_data["SendUsersMessageRequest"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendUsersMessagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendUsersMessagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentResponse:
    boto3_raw_data: "type_defs.SegmentResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreationDate = field("CreationDate")
    Id = field("Id")
    SegmentType = field("SegmentType")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return SegmentDimensionsOutput.make_one(self.boto3_raw_data["Dimensions"])

    @cached_property
    def ImportDefinition(self):  # pragma: no cover
        return SegmentImportResource.make_one(self.boto3_raw_data["ImportDefinition"])

    LastModifiedDate = field("LastModifiedDate")
    Name = field("Name")

    @cached_property
    def SegmentGroups(self):  # pragma: no cover
        return SegmentGroupListOutput.make_one(self.boto3_raw_data["SegmentGroups"])

    tags = field("tags")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SegmentResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionalSplitActivityOutput:
    boto3_raw_data: "type_defs.ConditionalSplitActivityOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Condition(self):  # pragma: no cover
        return ConditionOutput.make_one(self.boto3_raw_data["Condition"])

    @cached_property
    def EvaluationWaitTime(self):  # pragma: no cover
        return WaitTime.make_one(self.boto3_raw_data["EvaluationWaitTime"])

    FalseActivity = field("FalseActivity")
    TrueActivity = field("TrueActivity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConditionalSplitActivityOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionalSplitActivityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiConditionalSplitActivityOutput:
    boto3_raw_data: "type_defs.MultiConditionalSplitActivityOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Branches(self):  # pragma: no cover
        return MultiConditionalBranchOutput.make_many(self.boto3_raw_data["Branches"])

    DefaultActivity = field("DefaultActivity")

    @cached_property
    def EvaluationWaitTime(self):  # pragma: no cover
        return WaitTime.make_one(self.boto3_raw_data["EvaluationWaitTime"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultiConditionalSplitActivityOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiConditionalSplitActivityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignResponse:
    boto3_raw_data: "type_defs.CampaignResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreationDate = field("CreationDate")
    Id = field("Id")
    LastModifiedDate = field("LastModifiedDate")
    SegmentId = field("SegmentId")
    SegmentVersion = field("SegmentVersion")

    @cached_property
    def AdditionalTreatments(self):  # pragma: no cover
        return TreatmentResource.make_many(self.boto3_raw_data["AdditionalTreatments"])

    @cached_property
    def CustomDeliveryConfiguration(self):  # pragma: no cover
        return CustomDeliveryConfigurationOutput.make_one(
            self.boto3_raw_data["CustomDeliveryConfiguration"]
        )

    @cached_property
    def DefaultState(self):  # pragma: no cover
        return CampaignState.make_one(self.boto3_raw_data["DefaultState"])

    Description = field("Description")
    HoldoutPercent = field("HoldoutPercent")

    @cached_property
    def Hook(self):  # pragma: no cover
        return CampaignHook.make_one(self.boto3_raw_data["Hook"])

    IsPaused = field("IsPaused")

    @cached_property
    def Limits(self):  # pragma: no cover
        return CampaignLimits.make_one(self.boto3_raw_data["Limits"])

    @cached_property
    def MessageConfiguration(self):  # pragma: no cover
        return MessageConfigurationOutput.make_one(
            self.boto3_raw_data["MessageConfiguration"]
        )

    Name = field("Name")

    @cached_property
    def Schedule(self):  # pragma: no cover
        return ScheduleOutput.make_one(self.boto3_raw_data["Schedule"])

    @cached_property
    def State(self):  # pragma: no cover
        return CampaignState.make_one(self.boto3_raw_data["State"])

    tags = field("tags")

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfiguration.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    TreatmentDescription = field("TreatmentDescription")
    TreatmentName = field("TreatmentName")
    Version = field("Version")
    Priority = field("Priority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInAppMessagesResponse:
    boto3_raw_data: "type_defs.GetInAppMessagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def InAppMessagesResponse(self):  # pragma: no cover
        return InAppMessagesResponse.make_one(
            self.boto3_raw_data["InAppMessagesResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInAppMessagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInAppMessagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schedule:
    boto3_raw_data: "type_defs.ScheduleTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    EventFilter = field("EventFilter")
    Frequency = field("Frequency")
    IsLocalTime = field("IsLocalTime")

    @cached_property
    def QuietTime(self):  # pragma: no cover
        return QuietTime.make_one(self.boto3_raw_data["QuietTime"])

    Timezone = field("Timezone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventStartCondition:
    boto3_raw_data: "type_defs.EventStartConditionTypeDef" = dataclasses.field()

    EventFilter = field("EventFilter")
    SegmentId = field("SegmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventStartConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventStartConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentGroup:
    boto3_raw_data: "type_defs.SegmentGroupTypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")

    @cached_property
    def SourceSegments(self):  # pragma: no cover
        return SegmentReference.make_many(self.boto3_raw_data["SourceSegments"])

    SourceType = field("SourceType")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SegmentGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleCondition:
    boto3_raw_data: "type_defs.SimpleConditionTypeDef" = dataclasses.field()

    EventCondition = field("EventCondition")

    @cached_property
    def SegmentCondition(self):  # pragma: no cover
        return SegmentCondition.make_one(self.boto3_raw_data["SegmentCondition"])

    SegmentDimensions = field("SegmentDimensions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SimpleConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SimpleConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSegmentResponse:
    boto3_raw_data: "type_defs.CreateSegmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def SegmentResponse(self):  # pragma: no cover
        return SegmentResponse.make_one(self.boto3_raw_data["SegmentResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSegmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSegmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSegmentResponse:
    boto3_raw_data: "type_defs.DeleteSegmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def SegmentResponse(self):  # pragma: no cover
        return SegmentResponse.make_one(self.boto3_raw_data["SegmentResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSegmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSegmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentResponse:
    boto3_raw_data: "type_defs.GetSegmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def SegmentResponse(self):  # pragma: no cover
        return SegmentResponse.make_one(self.boto3_raw_data["SegmentResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentVersionResponse:
    boto3_raw_data: "type_defs.GetSegmentVersionResponseTypeDef" = dataclasses.field()

    @cached_property
    def SegmentResponse(self):  # pragma: no cover
        return SegmentResponse.make_one(self.boto3_raw_data["SegmentResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentsResponse:
    boto3_raw_data: "type_defs.SegmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return SegmentResponse.make_many(self.boto3_raw_data["Item"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSegmentResponse:
    boto3_raw_data: "type_defs.UpdateSegmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def SegmentResponse(self):  # pragma: no cover
        return SegmentResponse.make_one(self.boto3_raw_data["SegmentResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSegmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSegmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityOutput:
    boto3_raw_data: "type_defs.ActivityOutputTypeDef" = dataclasses.field()

    @cached_property
    def CUSTOM(self):  # pragma: no cover
        return CustomMessageActivityOutput.make_one(self.boto3_raw_data["CUSTOM"])

    @cached_property
    def ConditionalSplit(self):  # pragma: no cover
        return ConditionalSplitActivityOutput.make_one(
            self.boto3_raw_data["ConditionalSplit"]
        )

    Description = field("Description")

    @cached_property
    def EMAIL(self):  # pragma: no cover
        return EmailMessageActivity.make_one(self.boto3_raw_data["EMAIL"])

    @cached_property
    def Holdout(self):  # pragma: no cover
        return HoldoutActivity.make_one(self.boto3_raw_data["Holdout"])

    @cached_property
    def MultiCondition(self):  # pragma: no cover
        return MultiConditionalSplitActivityOutput.make_one(
            self.boto3_raw_data["MultiCondition"]
        )

    @cached_property
    def PUSH(self):  # pragma: no cover
        return PushMessageActivity.make_one(self.boto3_raw_data["PUSH"])

    @cached_property
    def RandomSplit(self):  # pragma: no cover
        return RandomSplitActivityOutput.make_one(self.boto3_raw_data["RandomSplit"])

    @cached_property
    def SMS(self):  # pragma: no cover
        return SMSMessageActivity.make_one(self.boto3_raw_data["SMS"])

    @cached_property
    def Wait(self):  # pragma: no cover
        return WaitActivity.make_one(self.boto3_raw_data["Wait"])

    @cached_property
    def ContactCenter(self):  # pragma: no cover
        return ContactCenterActivity.make_one(self.boto3_raw_data["ContactCenter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivityOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignsResponse:
    boto3_raw_data: "type_defs.CampaignsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return CampaignResponse.make_many(self.boto3_raw_data["Item"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCampaignResponse:
    boto3_raw_data: "type_defs.CreateCampaignResponseTypeDef" = dataclasses.field()

    @cached_property
    def CampaignResponse(self):  # pragma: no cover
        return CampaignResponse.make_one(self.boto3_raw_data["CampaignResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCampaignResponse:
    boto3_raw_data: "type_defs.DeleteCampaignResponseTypeDef" = dataclasses.field()

    @cached_property
    def CampaignResponse(self):  # pragma: no cover
        return CampaignResponse.make_one(self.boto3_raw_data["CampaignResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignResponse:
    boto3_raw_data: "type_defs.GetCampaignResponseTypeDef" = dataclasses.field()

    @cached_property
    def CampaignResponse(self):  # pragma: no cover
        return CampaignResponse.make_one(self.boto3_raw_data["CampaignResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignVersionResponse:
    boto3_raw_data: "type_defs.GetCampaignVersionResponseTypeDef" = dataclasses.field()

    @cached_property
    def CampaignResponse(self):  # pragma: no cover
        return CampaignResponse.make_one(self.boto3_raw_data["CampaignResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignResponse:
    boto3_raw_data: "type_defs.UpdateCampaignResponseTypeDef" = dataclasses.field()

    @cached_property
    def CampaignResponse(self):  # pragma: no cover
        return CampaignResponse.make_one(self.boto3_raw_data["CampaignResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentVersionsResponse:
    boto3_raw_data: "type_defs.GetSegmentVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def SegmentsResponse(self):  # pragma: no cover
        return SegmentsResponse.make_one(self.boto3_raw_data["SegmentsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentsResponse:
    boto3_raw_data: "type_defs.GetSegmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def SegmentsResponse(self):  # pragma: no cover
        return SegmentsResponse.make_one(self.boto3_raw_data["SegmentsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneyResponse:
    boto3_raw_data: "type_defs.JourneyResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Id = field("Id")
    Name = field("Name")
    Activities = field("Activities")
    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")

    @cached_property
    def Limits(self):  # pragma: no cover
        return JourneyLimits.make_one(self.boto3_raw_data["Limits"])

    LocalTime = field("LocalTime")

    @cached_property
    def QuietTime(self):  # pragma: no cover
        return QuietTime.make_one(self.boto3_raw_data["QuietTime"])

    RefreshFrequency = field("RefreshFrequency")

    @cached_property
    def Schedule(self):  # pragma: no cover
        return JourneyScheduleOutput.make_one(self.boto3_raw_data["Schedule"])

    StartActivity = field("StartActivity")

    @cached_property
    def StartCondition(self):  # pragma: no cover
        return StartConditionOutput.make_one(self.boto3_raw_data["StartCondition"])

    State = field("State")
    tags = field("tags")
    WaitForQuietTime = field("WaitForQuietTime")
    RefreshOnSegmentUpdate = field("RefreshOnSegmentUpdate")

    @cached_property
    def JourneyChannelSettings(self):  # pragma: no cover
        return JourneyChannelSettings.make_one(
            self.boto3_raw_data["JourneyChannelSettings"]
        )

    SendingSchedule = field("SendingSchedule")

    @cached_property
    def OpenHours(self):  # pragma: no cover
        return OpenHoursOutput.make_one(self.boto3_raw_data["OpenHours"])

    @cached_property
    def ClosedDays(self):  # pragma: no cover
        return ClosedDaysOutput.make_one(self.boto3_raw_data["ClosedDays"])

    TimezoneEstimationMethods = field("TimezoneEstimationMethods")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JourneyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JourneyResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignVersionsResponse:
    boto3_raw_data: "type_defs.GetCampaignVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def CampaignsResponse(self):  # pragma: no cover
        return CampaignsResponse.make_one(self.boto3_raw_data["CampaignsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignsResponse:
    boto3_raw_data: "type_defs.GetCampaignsResponseTypeDef" = dataclasses.field()

    @cached_property
    def CampaignsResponse(self):  # pragma: no cover
        return CampaignsResponse.make_one(self.boto3_raw_data["CampaignsResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteTreatmentResource:
    boto3_raw_data: "type_defs.WriteTreatmentResourceTypeDef" = dataclasses.field()

    SizePercent = field("SizePercent")
    CustomDeliveryConfiguration = field("CustomDeliveryConfiguration")
    MessageConfiguration = field("MessageConfiguration")
    Schedule = field("Schedule")

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfiguration.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    TreatmentDescription = field("TreatmentDescription")
    TreatmentName = field("TreatmentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WriteTreatmentResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteTreatmentResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCondition:
    boto3_raw_data: "type_defs.StartConditionTypeDef" = dataclasses.field()

    Description = field("Description")
    EventStartCondition = field("EventStartCondition")

    @cached_property
    def SegmentStartCondition(self):  # pragma: no cover
        return SegmentCondition.make_one(self.boto3_raw_data["SegmentStartCondition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentGroupList:
    boto3_raw_data: "type_defs.SegmentGroupListTypeDef" = dataclasses.field()

    Groups = field("Groups")
    Include = field("Include")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentGroupListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentGroupListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Condition:
    boto3_raw_data: "type_defs.ConditionTypeDef" = dataclasses.field()

    Conditions = field("Conditions")
    Operator = field("Operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiConditionalBranch:
    boto3_raw_data: "type_defs.MultiConditionalBranchTypeDef" = dataclasses.field()

    Condition = field("Condition")
    NextActivity = field("NextActivity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiConditionalBranchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiConditionalBranchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJourneyResponse:
    boto3_raw_data: "type_defs.CreateJourneyResponseTypeDef" = dataclasses.field()

    @cached_property
    def JourneyResponse(self):  # pragma: no cover
        return JourneyResponse.make_one(self.boto3_raw_data["JourneyResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJourneyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJourneyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJourneyResponse:
    boto3_raw_data: "type_defs.DeleteJourneyResponseTypeDef" = dataclasses.field()

    @cached_property
    def JourneyResponse(self):  # pragma: no cover
        return JourneyResponse.make_one(self.boto3_raw_data["JourneyResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteJourneyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJourneyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJourneyResponse:
    boto3_raw_data: "type_defs.GetJourneyResponseTypeDef" = dataclasses.field()

    @cached_property
    def JourneyResponse(self):  # pragma: no cover
        return JourneyResponse.make_one(self.boto3_raw_data["JourneyResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJourneyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJourneyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JourneysResponse:
    boto3_raw_data: "type_defs.JourneysResponseTypeDef" = dataclasses.field()

    @cached_property
    def Item(self):  # pragma: no cover
        return JourneyResponse.make_many(self.boto3_raw_data["Item"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JourneysResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JourneysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJourneyResponse:
    boto3_raw_data: "type_defs.UpdateJourneyResponseTypeDef" = dataclasses.field()

    @cached_property
    def JourneyResponse(self):  # pragma: no cover
        return JourneyResponse.make_one(self.boto3_raw_data["JourneyResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJourneyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJourneyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJourneyStateResponse:
    boto3_raw_data: "type_defs.UpdateJourneyStateResponseTypeDef" = dataclasses.field()

    @cached_property
    def JourneyResponse(self):  # pragma: no cover
        return JourneyResponse.make_one(self.boto3_raw_data["JourneyResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJourneyStateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJourneyStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteCampaignRequest:
    boto3_raw_data: "type_defs.WriteCampaignRequestTypeDef" = dataclasses.field()

    @cached_property
    def AdditionalTreatments(self):  # pragma: no cover
        return WriteTreatmentResource.make_many(
            self.boto3_raw_data["AdditionalTreatments"]
        )

    CustomDeliveryConfiguration = field("CustomDeliveryConfiguration")
    Description = field("Description")
    HoldoutPercent = field("HoldoutPercent")

    @cached_property
    def Hook(self):  # pragma: no cover
        return CampaignHook.make_one(self.boto3_raw_data["Hook"])

    IsPaused = field("IsPaused")

    @cached_property
    def Limits(self):  # pragma: no cover
        return CampaignLimits.make_one(self.boto3_raw_data["Limits"])

    MessageConfiguration = field("MessageConfiguration")
    Name = field("Name")
    Schedule = field("Schedule")
    SegmentId = field("SegmentId")
    SegmentVersion = field("SegmentVersion")
    tags = field("tags")

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfiguration.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    TreatmentDescription = field("TreatmentDescription")
    TreatmentName = field("TreatmentName")
    Priority = field("Priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WriteCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJourneysResponse:
    boto3_raw_data: "type_defs.ListJourneysResponseTypeDef" = dataclasses.field()

    @cached_property
    def JourneysResponse(self):  # pragma: no cover
        return JourneysResponse.make_one(self.boto3_raw_data["JourneysResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJourneysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJourneysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCampaignRequest:
    boto3_raw_data: "type_defs.CreateCampaignRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def WriteCampaignRequest(self):  # pragma: no cover
        return WriteCampaignRequest.make_one(
            self.boto3_raw_data["WriteCampaignRequest"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignRequest:
    boto3_raw_data: "type_defs.UpdateCampaignRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    CampaignId = field("CampaignId")

    @cached_property
    def WriteCampaignRequest(self):  # pragma: no cover
        return WriteCampaignRequest.make_one(
            self.boto3_raw_data["WriteCampaignRequest"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteSegmentRequest:
    boto3_raw_data: "type_defs.WriteSegmentRequestTypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")
    Name = field("Name")
    SegmentGroups = field("SegmentGroups")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WriteSegmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteSegmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionalSplitActivity:
    boto3_raw_data: "type_defs.ConditionalSplitActivityTypeDef" = dataclasses.field()

    Condition = field("Condition")

    @cached_property
    def EvaluationWaitTime(self):  # pragma: no cover
        return WaitTime.make_one(self.boto3_raw_data["EvaluationWaitTime"])

    FalseActivity = field("FalseActivity")
    TrueActivity = field("TrueActivity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConditionalSplitActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionalSplitActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiConditionalSplitActivity:
    boto3_raw_data: "type_defs.MultiConditionalSplitActivityTypeDef" = (
        dataclasses.field()
    )

    Branches = field("Branches")
    DefaultActivity = field("DefaultActivity")

    @cached_property
    def EvaluationWaitTime(self):  # pragma: no cover
        return WaitTime.make_one(self.boto3_raw_data["EvaluationWaitTime"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MultiConditionalSplitActivityTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiConditionalSplitActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSegmentRequest:
    boto3_raw_data: "type_defs.CreateSegmentRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def WriteSegmentRequest(self):  # pragma: no cover
        return WriteSegmentRequest.make_one(self.boto3_raw_data["WriteSegmentRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSegmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSegmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSegmentRequest:
    boto3_raw_data: "type_defs.UpdateSegmentRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    SegmentId = field("SegmentId")

    @cached_property
    def WriteSegmentRequest(self):  # pragma: no cover
        return WriteSegmentRequest.make_one(self.boto3_raw_data["WriteSegmentRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSegmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSegmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Activity:
    boto3_raw_data: "type_defs.ActivityTypeDef" = dataclasses.field()

    CUSTOM = field("CUSTOM")
    ConditionalSplit = field("ConditionalSplit")
    Description = field("Description")

    @cached_property
    def EMAIL(self):  # pragma: no cover
        return EmailMessageActivity.make_one(self.boto3_raw_data["EMAIL"])

    @cached_property
    def Holdout(self):  # pragma: no cover
        return HoldoutActivity.make_one(self.boto3_raw_data["Holdout"])

    MultiCondition = field("MultiCondition")

    @cached_property
    def PUSH(self):  # pragma: no cover
        return PushMessageActivity.make_one(self.boto3_raw_data["PUSH"])

    RandomSplit = field("RandomSplit")

    @cached_property
    def SMS(self):  # pragma: no cover
        return SMSMessageActivity.make_one(self.boto3_raw_data["SMS"])

    @cached_property
    def Wait(self):  # pragma: no cover
        return WaitActivity.make_one(self.boto3_raw_data["Wait"])

    @cached_property
    def ContactCenter(self):  # pragma: no cover
        return ContactCenterActivity.make_one(self.boto3_raw_data["ContactCenter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteJourneyRequest:
    boto3_raw_data: "type_defs.WriteJourneyRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Activities = field("Activities")
    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")

    @cached_property
    def Limits(self):  # pragma: no cover
        return JourneyLimits.make_one(self.boto3_raw_data["Limits"])

    LocalTime = field("LocalTime")

    @cached_property
    def QuietTime(self):  # pragma: no cover
        return QuietTime.make_one(self.boto3_raw_data["QuietTime"])

    RefreshFrequency = field("RefreshFrequency")
    Schedule = field("Schedule")
    StartActivity = field("StartActivity")
    StartCondition = field("StartCondition")
    State = field("State")
    WaitForQuietTime = field("WaitForQuietTime")
    RefreshOnSegmentUpdate = field("RefreshOnSegmentUpdate")

    @cached_property
    def JourneyChannelSettings(self):  # pragma: no cover
        return JourneyChannelSettings.make_one(
            self.boto3_raw_data["JourneyChannelSettings"]
        )

    SendingSchedule = field("SendingSchedule")
    OpenHours = field("OpenHours")
    ClosedDays = field("ClosedDays")
    TimezoneEstimationMethods = field("TimezoneEstimationMethods")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WriteJourneyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteJourneyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJourneyRequest:
    boto3_raw_data: "type_defs.CreateJourneyRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @cached_property
    def WriteJourneyRequest(self):  # pragma: no cover
        return WriteJourneyRequest.make_one(self.boto3_raw_data["WriteJourneyRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJourneyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJourneyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJourneyRequest:
    boto3_raw_data: "type_defs.UpdateJourneyRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    JourneyId = field("JourneyId")

    @cached_property
    def WriteJourneyRequest(self):  # pragma: no cover
        return WriteJourneyRequest.make_one(self.boto3_raw_data["WriteJourneyRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJourneyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJourneyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
