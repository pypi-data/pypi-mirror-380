# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pinpoint_email import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BlacklistEntry:
    boto3_raw_data: "type_defs.BlacklistEntryTypeDef" = dataclasses.field()

    RblName = field("RblName")
    ListingTime = field("ListingTime")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlacklistEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlacklistEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Content:
    boto3_raw_data: "type_defs.ContentTypeDef" = dataclasses.field()

    Data = field("Data")
    Charset = field("Charset")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchDimensionConfiguration:
    boto3_raw_data: "type_defs.CloudWatchDimensionConfigurationTypeDef" = (
        dataclasses.field()
    )

    DimensionName = field("DimensionName")
    DimensionValueSource = field("DimensionValueSource")
    DefaultDimensionValue = field("DefaultDimensionValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchDimensionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchDimensionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliveryOptions:
    boto3_raw_data: "type_defs.DeliveryOptionsTypeDef" = dataclasses.field()

    TlsPolicy = field("TlsPolicy")
    SendingPoolName = field("SendingPoolName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeliveryOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeliveryOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendingOptions:
    boto3_raw_data: "type_defs.SendingOptionsTypeDef" = dataclasses.field()

    SendingEnabled = field("SendingEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendingOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SendingOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrackingOptions:
    boto3_raw_data: "type_defs.TrackingOptionsTypeDef" = dataclasses.field()

    CustomRedirectDomain = field("CustomRedirectDomain")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrackingOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrackingOptionsTypeDef"]],
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
class DkimAttributes:
    boto3_raw_data: "type_defs.DkimAttributesTypeDef" = dataclasses.field()

    SigningEnabled = field("SigningEnabled")
    Status = field("Status")
    Tokens = field("Tokens")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DkimAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DkimAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainIspPlacement:
    boto3_raw_data: "type_defs.DomainIspPlacementTypeDef" = dataclasses.field()

    IspName = field("IspName")
    InboxRawCount = field("InboxRawCount")
    SpamRawCount = field("SpamRawCount")
    InboxPercentage = field("InboxPercentage")
    SpamPercentage = field("SpamPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainIspPlacementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainIspPlacementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeStatistics:
    boto3_raw_data: "type_defs.VolumeStatisticsTypeDef" = dataclasses.field()

    InboxRawCount = field("InboxRawCount")
    SpamRawCount = field("SpamRawCount")
    ProjectedInbox = field("ProjectedInbox")
    ProjectedSpam = field("ProjectedSpam")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VolumeStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DedicatedIp:
    boto3_raw_data: "type_defs.DedicatedIpTypeDef" = dataclasses.field()

    Ip = field("Ip")
    WarmupStatus = field("WarmupStatus")
    WarmupPercentage = field("WarmupPercentage")
    PoolName = field("PoolName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DedicatedIpTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DedicatedIpTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationSetEventDestinationRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationSetEventDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    EventDestinationName = field("EventDestinationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfigurationSetEventDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationSetEventDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationSetRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationSetRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteConfigurationSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDedicatedIpPoolRequest:
    boto3_raw_data: "type_defs.DeleteDedicatedIpPoolRequestTypeDef" = (
        dataclasses.field()
    )

    PoolName = field("PoolName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDedicatedIpPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDedicatedIpPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEmailIdentityRequest:
    boto3_raw_data: "type_defs.DeleteEmailIdentityRequestTypeDef" = dataclasses.field()

    EmailIdentity = field("EmailIdentity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEmailIdentityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEmailIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliverabilityTestReport:
    boto3_raw_data: "type_defs.DeliverabilityTestReportTypeDef" = dataclasses.field()

    ReportId = field("ReportId")
    ReportName = field("ReportName")
    Subject = field("Subject")
    FromEmailAddress = field("FromEmailAddress")
    CreateDate = field("CreateDate")
    DeliverabilityTestStatus = field("DeliverabilityTestStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeliverabilityTestReportTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliverabilityTestReportTypeDef"]
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

    ToAddresses = field("ToAddresses")
    CcAddresses = field("CcAddresses")
    BccAddresses = field("BccAddresses")

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
class DomainDeliverabilityCampaign:
    boto3_raw_data: "type_defs.DomainDeliverabilityCampaignTypeDef" = (
        dataclasses.field()
    )

    CampaignId = field("CampaignId")
    ImageUrl = field("ImageUrl")
    Subject = field("Subject")
    FromAddress = field("FromAddress")
    SendingIps = field("SendingIps")
    FirstSeenDateTime = field("FirstSeenDateTime")
    LastSeenDateTime = field("LastSeenDateTime")
    InboxCount = field("InboxCount")
    SpamCount = field("SpamCount")
    ReadRate = field("ReadRate")
    DeleteRate = field("DeleteRate")
    ReadDeleteRate = field("ReadDeleteRate")
    ProjectedVolume = field("ProjectedVolume")
    Esps = field("Esps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainDeliverabilityCampaignTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainDeliverabilityCampaignTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InboxPlacementTrackingOptionOutput:
    boto3_raw_data: "type_defs.InboxPlacementTrackingOptionOutputTypeDef" = (
        dataclasses.field()
    )

    Global = field("Global")
    TrackedIsps = field("TrackedIsps")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InboxPlacementTrackingOptionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboxPlacementTrackingOptionOutputTypeDef"]
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

    TemplateArn = field("TemplateArn")
    TemplateData = field("TemplateData")

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
class KinesisFirehoseDestination:
    boto3_raw_data: "type_defs.KinesisFirehoseDestinationTypeDef" = dataclasses.field()

    IamRoleArn = field("IamRoleArn")
    DeliveryStreamArn = field("DeliveryStreamArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PinpointDestination:
    boto3_raw_data: "type_defs.PinpointDestinationTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PinpointDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PinpointDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnsDestination:
    boto3_raw_data: "type_defs.SnsDestinationTypeDef" = dataclasses.field()

    TopicArn = field("TopicArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnsDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnsDestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendQuota:
    boto3_raw_data: "type_defs.SendQuotaTypeDef" = dataclasses.field()

    Max24HourSend = field("Max24HourSend")
    MaxSendRate = field("MaxSendRate")
    SentLast24Hours = field("SentLast24Hours")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendQuotaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SendQuotaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBlacklistReportsRequest:
    boto3_raw_data: "type_defs.GetBlacklistReportsRequestTypeDef" = dataclasses.field()

    BlacklistItemNames = field("BlacklistItemNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBlacklistReportsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBlacklistReportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigurationSetEventDestinationsRequest:
    boto3_raw_data: "type_defs.GetConfigurationSetEventDestinationsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfigurationSetEventDestinationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigurationSetEventDestinationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigurationSetRequest:
    boto3_raw_data: "type_defs.GetConfigurationSetRequestTypeDef" = dataclasses.field()

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConfigurationSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigurationSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReputationOptionsOutput:
    boto3_raw_data: "type_defs.ReputationOptionsOutputTypeDef" = dataclasses.field()

    ReputationMetricsEnabled = field("ReputationMetricsEnabled")
    LastFreshStart = field("LastFreshStart")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReputationOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReputationOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDedicatedIpRequest:
    boto3_raw_data: "type_defs.GetDedicatedIpRequestTypeDef" = dataclasses.field()

    Ip = field("Ip")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDedicatedIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDedicatedIpRequestTypeDef"]
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
class GetDedicatedIpsRequest:
    boto3_raw_data: "type_defs.GetDedicatedIpsRequestTypeDef" = dataclasses.field()

    PoolName = field("PoolName")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDedicatedIpsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDedicatedIpsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliverabilityTestReportRequest:
    boto3_raw_data: "type_defs.GetDeliverabilityTestReportRequestTypeDef" = (
        dataclasses.field()
    )

    ReportId = field("ReportId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeliverabilityTestReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliverabilityTestReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlacementStatistics:
    boto3_raw_data: "type_defs.PlacementStatisticsTypeDef" = dataclasses.field()

    InboxPercentage = field("InboxPercentage")
    SpamPercentage = field("SpamPercentage")
    MissingPercentage = field("MissingPercentage")
    SpfPercentage = field("SpfPercentage")
    DkimPercentage = field("DkimPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlacementStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlacementStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainDeliverabilityCampaignRequest:
    boto3_raw_data: "type_defs.GetDomainDeliverabilityCampaignRequestTypeDef" = (
        dataclasses.field()
    )

    CampaignId = field("CampaignId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDomainDeliverabilityCampaignRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainDeliverabilityCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEmailIdentityRequest:
    boto3_raw_data: "type_defs.GetEmailIdentityRequestTypeDef" = dataclasses.field()

    EmailIdentity = field("EmailIdentity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEmailIdentityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEmailIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MailFromAttributes:
    boto3_raw_data: "type_defs.MailFromAttributesTypeDef" = dataclasses.field()

    MailFromDomain = field("MailFromDomain")
    MailFromDomainStatus = field("MailFromDomainStatus")
    BehaviorOnMxFailure = field("BehaviorOnMxFailure")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MailFromAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MailFromAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityInfo:
    boto3_raw_data: "type_defs.IdentityInfoTypeDef" = dataclasses.field()

    IdentityType = field("IdentityType")
    IdentityName = field("IdentityName")
    SendingEnabled = field("SendingEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdentityInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InboxPlacementTrackingOption:
    boto3_raw_data: "type_defs.InboxPlacementTrackingOptionTypeDef" = (
        dataclasses.field()
    )

    Global = field("Global")
    TrackedIsps = field("TrackedIsps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InboxPlacementTrackingOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboxPlacementTrackingOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationSetsRequest:
    boto3_raw_data: "type_defs.ListConfigurationSetsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfigurationSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDedicatedIpPoolsRequest:
    boto3_raw_data: "type_defs.ListDedicatedIpPoolsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDedicatedIpPoolsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDedicatedIpPoolsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeliverabilityTestReportsRequest:
    boto3_raw_data: "type_defs.ListDeliverabilityTestReportsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeliverabilityTestReportsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeliverabilityTestReportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEmailIdentitiesRequest:
    boto3_raw_data: "type_defs.ListEmailIdentitiesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEmailIdentitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEmailIdentitiesRequestTypeDef"]
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
class MessageTag:
    boto3_raw_data: "type_defs.MessageTagTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountDedicatedIpWarmupAttributesRequest:
    boto3_raw_data: "type_defs.PutAccountDedicatedIpWarmupAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    AutoWarmupEnabled = field("AutoWarmupEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAccountDedicatedIpWarmupAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountDedicatedIpWarmupAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountSendingAttributesRequest:
    boto3_raw_data: "type_defs.PutAccountSendingAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    SendingEnabled = field("SendingEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAccountSendingAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountSendingAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConfigurationSetDeliveryOptionsRequest:
    boto3_raw_data: "type_defs.PutConfigurationSetDeliveryOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    TlsPolicy = field("TlsPolicy")
    SendingPoolName = field("SendingPoolName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfigurationSetDeliveryOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigurationSetDeliveryOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConfigurationSetReputationOptionsRequest:
    boto3_raw_data: "type_defs.PutConfigurationSetReputationOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    ReputationMetricsEnabled = field("ReputationMetricsEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfigurationSetReputationOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigurationSetReputationOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConfigurationSetSendingOptionsRequest:
    boto3_raw_data: "type_defs.PutConfigurationSetSendingOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    SendingEnabled = field("SendingEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfigurationSetSendingOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigurationSetSendingOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConfigurationSetTrackingOptionsRequest:
    boto3_raw_data: "type_defs.PutConfigurationSetTrackingOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    CustomRedirectDomain = field("CustomRedirectDomain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfigurationSetTrackingOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigurationSetTrackingOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDedicatedIpInPoolRequest:
    boto3_raw_data: "type_defs.PutDedicatedIpInPoolRequestTypeDef" = dataclasses.field()

    Ip = field("Ip")
    DestinationPoolName = field("DestinationPoolName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDedicatedIpInPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDedicatedIpInPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDedicatedIpWarmupAttributesRequest:
    boto3_raw_data: "type_defs.PutDedicatedIpWarmupAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    Ip = field("Ip")
    WarmupPercentage = field("WarmupPercentage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutDedicatedIpWarmupAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDedicatedIpWarmupAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEmailIdentityDkimAttributesRequest:
    boto3_raw_data: "type_defs.PutEmailIdentityDkimAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    EmailIdentity = field("EmailIdentity")
    SigningEnabled = field("SigningEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEmailIdentityDkimAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEmailIdentityDkimAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEmailIdentityFeedbackAttributesRequest:
    boto3_raw_data: "type_defs.PutEmailIdentityFeedbackAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    EmailIdentity = field("EmailIdentity")
    EmailForwardingEnabled = field("EmailForwardingEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEmailIdentityFeedbackAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEmailIdentityFeedbackAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEmailIdentityMailFromAttributesRequest:
    boto3_raw_data: "type_defs.PutEmailIdentityMailFromAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    EmailIdentity = field("EmailIdentity")
    MailFromDomain = field("MailFromDomain")
    BehaviorOnMxFailure = field("BehaviorOnMxFailure")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEmailIdentityMailFromAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEmailIdentityMailFromAttributesRequestTypeDef"]
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
class RawMessage:
    boto3_raw_data: "type_defs.RawMessageTypeDef" = dataclasses.field()

    Data = field("Data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RawMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RawMessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Body:
    boto3_raw_data: "type_defs.BodyTypeDef" = dataclasses.field()

    @cached_property
    def Text(self):  # pragma: no cover
        return Content.make_one(self.boto3_raw_data["Text"])

    @cached_property
    def Html(self):  # pragma: no cover
        return Content.make_one(self.boto3_raw_data["Html"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BodyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BodyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchDestinationOutput:
    boto3_raw_data: "type_defs.CloudWatchDestinationOutputTypeDef" = dataclasses.field()

    @cached_property
    def DimensionConfigurations(self):  # pragma: no cover
        return CloudWatchDimensionConfiguration.make_many(
            self.boto3_raw_data["DimensionConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchDestinationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchDestinationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchDestination:
    boto3_raw_data: "type_defs.CloudWatchDestinationTypeDef" = dataclasses.field()

    @cached_property
    def DimensionConfigurations(self):  # pragma: no cover
        return CloudWatchDimensionConfiguration.make_many(
            self.boto3_raw_data["DimensionConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDedicatedIpPoolRequest:
    boto3_raw_data: "type_defs.CreateDedicatedIpPoolRequestTypeDef" = (
        dataclasses.field()
    )

    PoolName = field("PoolName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDedicatedIpPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDedicatedIpPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEmailIdentityRequest:
    boto3_raw_data: "type_defs.CreateEmailIdentityRequestTypeDef" = dataclasses.field()

    EmailIdentity = field("EmailIdentity")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEmailIdentityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEmailIdentityRequestTypeDef"]
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

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateDeliverabilityTestReportResponse:
    boto3_raw_data: "type_defs.CreateDeliverabilityTestReportResponseTypeDef" = (
        dataclasses.field()
    )

    ReportId = field("ReportId")
    DeliverabilityTestStatus = field("DeliverabilityTestStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDeliverabilityTestReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeliverabilityTestReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBlacklistReportsResponse:
    boto3_raw_data: "type_defs.GetBlacklistReportsResponseTypeDef" = dataclasses.field()

    BlacklistReport = field("BlacklistReport")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBlacklistReportsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBlacklistReportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationSetsResponse:
    boto3_raw_data: "type_defs.ListConfigurationSetsResponseTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSets = field("ConfigurationSets")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConfigurationSetsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDedicatedIpPoolsResponse:
    boto3_raw_data: "type_defs.ListDedicatedIpPoolsResponseTypeDef" = (
        dataclasses.field()
    )

    DedicatedIpPools = field("DedicatedIpPools")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDedicatedIpPoolsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDedicatedIpPoolsResponseTypeDef"]
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
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class SendEmailResponse:
    boto3_raw_data: "type_defs.SendEmailResponseTypeDef" = dataclasses.field()

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendEmailResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendEmailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEmailIdentityResponse:
    boto3_raw_data: "type_defs.CreateEmailIdentityResponseTypeDef" = dataclasses.field()

    IdentityType = field("IdentityType")
    VerifiedForSendingStatus = field("VerifiedForSendingStatus")

    @cached_property
    def DkimAttributes(self):  # pragma: no cover
        return DkimAttributes.make_one(self.boto3_raw_data["DkimAttributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEmailIdentityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEmailIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DailyVolume:
    boto3_raw_data: "type_defs.DailyVolumeTypeDef" = dataclasses.field()

    StartDate = field("StartDate")

    @cached_property
    def VolumeStatistics(self):  # pragma: no cover
        return VolumeStatistics.make_one(self.boto3_raw_data["VolumeStatistics"])

    @cached_property
    def DomainIspPlacements(self):  # pragma: no cover
        return DomainIspPlacement.make_many(self.boto3_raw_data["DomainIspPlacements"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DailyVolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DailyVolumeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverallVolume:
    boto3_raw_data: "type_defs.OverallVolumeTypeDef" = dataclasses.field()

    @cached_property
    def VolumeStatistics(self):  # pragma: no cover
        return VolumeStatistics.make_one(self.boto3_raw_data["VolumeStatistics"])

    ReadRatePercent = field("ReadRatePercent")

    @cached_property
    def DomainIspPlacements(self):  # pragma: no cover
        return DomainIspPlacement.make_many(self.boto3_raw_data["DomainIspPlacements"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OverallVolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OverallVolumeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDedicatedIpResponse:
    boto3_raw_data: "type_defs.GetDedicatedIpResponseTypeDef" = dataclasses.field()

    @cached_property
    def DedicatedIp(self):  # pragma: no cover
        return DedicatedIp.make_one(self.boto3_raw_data["DedicatedIp"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDedicatedIpResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDedicatedIpResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDedicatedIpsResponse:
    boto3_raw_data: "type_defs.GetDedicatedIpsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DedicatedIps(self):  # pragma: no cover
        return DedicatedIp.make_many(self.boto3_raw_data["DedicatedIps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDedicatedIpsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDedicatedIpsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeliverabilityTestReportsResponse:
    boto3_raw_data: "type_defs.ListDeliverabilityTestReportsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DeliverabilityTestReports(self):  # pragma: no cover
        return DeliverabilityTestReport.make_many(
            self.boto3_raw_data["DeliverabilityTestReports"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeliverabilityTestReportsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeliverabilityTestReportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainDeliverabilityCampaignResponse:
    boto3_raw_data: "type_defs.GetDomainDeliverabilityCampaignResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainDeliverabilityCampaign(self):  # pragma: no cover
        return DomainDeliverabilityCampaign.make_one(
            self.boto3_raw_data["DomainDeliverabilityCampaign"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDomainDeliverabilityCampaignResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainDeliverabilityCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainDeliverabilityCampaignsResponse:
    boto3_raw_data: "type_defs.ListDomainDeliverabilityCampaignsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainDeliverabilityCampaigns(self):  # pragma: no cover
        return DomainDeliverabilityCampaign.make_many(
            self.boto3_raw_data["DomainDeliverabilityCampaigns"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDomainDeliverabilityCampaignsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainDeliverabilityCampaignsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainDeliverabilityTrackingOptionOutput:
    boto3_raw_data: "type_defs.DomainDeliverabilityTrackingOptionOutputTypeDef" = (
        dataclasses.field()
    )

    Domain = field("Domain")
    SubscriptionStartDate = field("SubscriptionStartDate")

    @cached_property
    def InboxPlacementTrackingOption(self):  # pragma: no cover
        return InboxPlacementTrackingOptionOutput.make_one(
            self.boto3_raw_data["InboxPlacementTrackingOption"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DomainDeliverabilityTrackingOptionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainDeliverabilityTrackingOptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainStatisticsReportRequest:
    boto3_raw_data: "type_defs.GetDomainStatisticsReportRequestTypeDef" = (
        dataclasses.field()
    )

    Domain = field("Domain")
    StartDate = field("StartDate")
    EndDate = field("EndDate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDomainStatisticsReportRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainStatisticsReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainDeliverabilityCampaignsRequest:
    boto3_raw_data: "type_defs.ListDomainDeliverabilityCampaignsRequestTypeDef" = (
        dataclasses.field()
    )

    StartDate = field("StartDate")
    EndDate = field("EndDate")
    SubscribedDomain = field("SubscribedDomain")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDomainDeliverabilityCampaignsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainDeliverabilityCampaignsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReputationOptions:
    boto3_raw_data: "type_defs.ReputationOptionsTypeDef" = dataclasses.field()

    ReputationMetricsEnabled = field("ReputationMetricsEnabled")
    LastFreshStart = field("LastFreshStart")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReputationOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReputationOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountResponse:
    boto3_raw_data: "type_defs.GetAccountResponseTypeDef" = dataclasses.field()

    @cached_property
    def SendQuota(self):  # pragma: no cover
        return SendQuota.make_one(self.boto3_raw_data["SendQuota"])

    SendingEnabled = field("SendingEnabled")
    DedicatedIpAutoWarmupEnabled = field("DedicatedIpAutoWarmupEnabled")
    EnforcementStatus = field("EnforcementStatus")
    ProductionAccessEnabled = field("ProductionAccessEnabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigurationSetResponse:
    boto3_raw_data: "type_defs.GetConfigurationSetResponseTypeDef" = dataclasses.field()

    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def TrackingOptions(self):  # pragma: no cover
        return TrackingOptions.make_one(self.boto3_raw_data["TrackingOptions"])

    @cached_property
    def DeliveryOptions(self):  # pragma: no cover
        return DeliveryOptions.make_one(self.boto3_raw_data["DeliveryOptions"])

    @cached_property
    def ReputationOptions(self):  # pragma: no cover
        return ReputationOptionsOutput.make_one(
            self.boto3_raw_data["ReputationOptions"]
        )

    @cached_property
    def SendingOptions(self):  # pragma: no cover
        return SendingOptions.make_one(self.boto3_raw_data["SendingOptions"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConfigurationSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigurationSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDedicatedIpsRequestPaginate:
    boto3_raw_data: "type_defs.GetDedicatedIpsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PoolName = field("PoolName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDedicatedIpsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDedicatedIpsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListConfigurationSetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationSetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDedicatedIpPoolsRequestPaginate:
    boto3_raw_data: "type_defs.ListDedicatedIpPoolsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDedicatedIpPoolsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDedicatedIpPoolsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeliverabilityTestReportsRequestPaginate:
    boto3_raw_data: "type_defs.ListDeliverabilityTestReportsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeliverabilityTestReportsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeliverabilityTestReportsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEmailIdentitiesRequestPaginate:
    boto3_raw_data: "type_defs.ListEmailIdentitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEmailIdentitiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEmailIdentitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IspPlacement:
    boto3_raw_data: "type_defs.IspPlacementTypeDef" = dataclasses.field()

    IspName = field("IspName")

    @cached_property
    def PlacementStatistics(self):  # pragma: no cover
        return PlacementStatistics.make_one(self.boto3_raw_data["PlacementStatistics"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IspPlacementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IspPlacementTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEmailIdentityResponse:
    boto3_raw_data: "type_defs.GetEmailIdentityResponseTypeDef" = dataclasses.field()

    IdentityType = field("IdentityType")
    FeedbackForwardingStatus = field("FeedbackForwardingStatus")
    VerifiedForSendingStatus = field("VerifiedForSendingStatus")

    @cached_property
    def DkimAttributes(self):  # pragma: no cover
        return DkimAttributes.make_one(self.boto3_raw_data["DkimAttributes"])

    @cached_property
    def MailFromAttributes(self):  # pragma: no cover
        return MailFromAttributes.make_one(self.boto3_raw_data["MailFromAttributes"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEmailIdentityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEmailIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEmailIdentitiesResponse:
    boto3_raw_data: "type_defs.ListEmailIdentitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def EmailIdentities(self):  # pragma: no cover
        return IdentityInfo.make_many(self.boto3_raw_data["EmailIdentities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEmailIdentitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEmailIdentitiesResponseTypeDef"]
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

    @cached_property
    def Subject(self):  # pragma: no cover
        return Content.make_one(self.boto3_raw_data["Subject"])

    @cached_property
    def Body(self):  # pragma: no cover
        return Body.make_one(self.boto3_raw_data["Body"])

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
class EventDestination:
    boto3_raw_data: "type_defs.EventDestinationTypeDef" = dataclasses.field()

    Name = field("Name")
    MatchingEventTypes = field("MatchingEventTypes")
    Enabled = field("Enabled")

    @cached_property
    def KinesisFirehoseDestination(self):  # pragma: no cover
        return KinesisFirehoseDestination.make_one(
            self.boto3_raw_data["KinesisFirehoseDestination"]
        )

    @cached_property
    def CloudWatchDestination(self):  # pragma: no cover
        return CloudWatchDestinationOutput.make_one(
            self.boto3_raw_data["CloudWatchDestination"]
        )

    @cached_property
    def SnsDestination(self):  # pragma: no cover
        return SnsDestination.make_one(self.boto3_raw_data["SnsDestination"])

    @cached_property
    def PinpointDestination(self):  # pragma: no cover
        return PinpointDestination.make_one(self.boto3_raw_data["PinpointDestination"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainStatisticsReportResponse:
    boto3_raw_data: "type_defs.GetDomainStatisticsReportResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OverallVolume(self):  # pragma: no cover
        return OverallVolume.make_one(self.boto3_raw_data["OverallVolume"])

    @cached_property
    def DailyVolumes(self):  # pragma: no cover
        return DailyVolume.make_many(self.boto3_raw_data["DailyVolumes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDomainStatisticsReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainStatisticsReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliverabilityDashboardOptionsResponse:
    boto3_raw_data: "type_defs.GetDeliverabilityDashboardOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    DashboardEnabled = field("DashboardEnabled")
    SubscriptionExpiryDate = field("SubscriptionExpiryDate")
    AccountStatus = field("AccountStatus")

    @cached_property
    def ActiveSubscribedDomains(self):  # pragma: no cover
        return DomainDeliverabilityTrackingOptionOutput.make_many(
            self.boto3_raw_data["ActiveSubscribedDomains"]
        )

    @cached_property
    def PendingExpirationSubscribedDomains(self):  # pragma: no cover
        return DomainDeliverabilityTrackingOptionOutput.make_many(
            self.boto3_raw_data["PendingExpirationSubscribedDomains"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeliverabilityDashboardOptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliverabilityDashboardOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliverabilityTestReportResponse:
    boto3_raw_data: "type_defs.GetDeliverabilityTestReportResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DeliverabilityTestReport(self):  # pragma: no cover
        return DeliverabilityTestReport.make_one(
            self.boto3_raw_data["DeliverabilityTestReport"]
        )

    @cached_property
    def OverallPlacement(self):  # pragma: no cover
        return PlacementStatistics.make_one(self.boto3_raw_data["OverallPlacement"])

    @cached_property
    def IspPlacements(self):  # pragma: no cover
        return IspPlacement.make_many(self.boto3_raw_data["IspPlacements"])

    Message = field("Message")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeliverabilityTestReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliverabilityTestReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainDeliverabilityTrackingOption:
    boto3_raw_data: "type_defs.DomainDeliverabilityTrackingOptionTypeDef" = (
        dataclasses.field()
    )

    Domain = field("Domain")
    SubscriptionStartDate = field("SubscriptionStartDate")
    InboxPlacementTrackingOption = field("InboxPlacementTrackingOption")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DomainDeliverabilityTrackingOptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainDeliverabilityTrackingOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailContent:
    boto3_raw_data: "type_defs.EmailContentTypeDef" = dataclasses.field()

    @cached_property
    def Simple(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["Simple"])

    @cached_property
    def Raw(self):  # pragma: no cover
        return RawMessage.make_one(self.boto3_raw_data["Raw"])

    @cached_property
    def Template(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["Template"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigurationSetEventDestinationsResponse:
    boto3_raw_data: "type_defs.GetConfigurationSetEventDestinationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventDestinations(self):  # pragma: no cover
        return EventDestination.make_many(self.boto3_raw_data["EventDestinations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfigurationSetEventDestinationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigurationSetEventDestinationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDestinationDefinition:
    boto3_raw_data: "type_defs.EventDestinationDefinitionTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    MatchingEventTypes = field("MatchingEventTypes")

    @cached_property
    def KinesisFirehoseDestination(self):  # pragma: no cover
        return KinesisFirehoseDestination.make_one(
            self.boto3_raw_data["KinesisFirehoseDestination"]
        )

    CloudWatchDestination = field("CloudWatchDestination")

    @cached_property
    def SnsDestination(self):  # pragma: no cover
        return SnsDestination.make_one(self.boto3_raw_data["SnsDestination"])

    @cached_property
    def PinpointDestination(self):  # pragma: no cover
        return PinpointDestination.make_one(self.boto3_raw_data["PinpointDestination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventDestinationDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDestinationDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationSetRequest:
    boto3_raw_data: "type_defs.CreateConfigurationSetRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def TrackingOptions(self):  # pragma: no cover
        return TrackingOptions.make_one(self.boto3_raw_data["TrackingOptions"])

    @cached_property
    def DeliveryOptions(self):  # pragma: no cover
        return DeliveryOptions.make_one(self.boto3_raw_data["DeliveryOptions"])

    ReputationOptions = field("ReputationOptions")

    @cached_property
    def SendingOptions(self):  # pragma: no cover
        return SendingOptions.make_one(self.boto3_raw_data["SendingOptions"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConfigurationSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeliverabilityTestReportRequest:
    boto3_raw_data: "type_defs.CreateDeliverabilityTestReportRequestTypeDef" = (
        dataclasses.field()
    )

    FromEmailAddress = field("FromEmailAddress")

    @cached_property
    def Content(self):  # pragma: no cover
        return EmailContent.make_one(self.boto3_raw_data["Content"])

    ReportName = field("ReportName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDeliverabilityTestReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeliverabilityTestReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendEmailRequest:
    boto3_raw_data: "type_defs.SendEmailRequestTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def Content(self):  # pragma: no cover
        return EmailContent.make_one(self.boto3_raw_data["Content"])

    FromEmailAddress = field("FromEmailAddress")
    ReplyToAddresses = field("ReplyToAddresses")
    FeedbackForwardingEmailAddress = field("FeedbackForwardingEmailAddress")

    @cached_property
    def EmailTags(self):  # pragma: no cover
        return MessageTag.make_many(self.boto3_raw_data["EmailTags"])

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendEmailRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendEmailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationSetEventDestinationRequest:
    boto3_raw_data: "type_defs.CreateConfigurationSetEventDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    EventDestinationName = field("EventDestinationName")

    @cached_property
    def EventDestination(self):  # pragma: no cover
        return EventDestinationDefinition.make_one(
            self.boto3_raw_data["EventDestination"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfigurationSetEventDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationSetEventDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationSetEventDestinationRequest:
    boto3_raw_data: "type_defs.UpdateConfigurationSetEventDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    EventDestinationName = field("EventDestinationName")

    @cached_property
    def EventDestination(self):  # pragma: no cover
        return EventDestinationDefinition.make_one(
            self.boto3_raw_data["EventDestination"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfigurationSetEventDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationSetEventDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDeliverabilityDashboardOptionRequest:
    boto3_raw_data: "type_defs.PutDeliverabilityDashboardOptionRequestTypeDef" = (
        dataclasses.field()
    )

    DashboardEnabled = field("DashboardEnabled")
    SubscribedDomains = field("SubscribedDomains")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutDeliverabilityDashboardOptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDeliverabilityDashboardOptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
