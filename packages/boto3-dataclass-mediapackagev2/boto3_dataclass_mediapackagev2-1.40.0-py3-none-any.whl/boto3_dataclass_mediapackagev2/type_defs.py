# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediapackagev2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CancelHarvestJobRequest:
    boto3_raw_data: "type_defs.CancelHarvestJobRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    HarvestJobName = field("HarvestJobName")
    ETag = field("ETag")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelHarvestJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelHarvestJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CdnAuthConfigurationOutput:
    boto3_raw_data: "type_defs.CdnAuthConfigurationOutputTypeDef" = dataclasses.field()

    CdnIdentifierSecretArns = field("CdnIdentifierSecretArns")
    SecretsRoleArn = field("SecretsRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CdnAuthConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CdnAuthConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CdnAuthConfiguration:
    boto3_raw_data: "type_defs.CdnAuthConfigurationTypeDef" = dataclasses.field()

    CdnIdentifierSecretArns = field("CdnIdentifierSecretArns")
    SecretsRoleArn = field("SecretsRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CdnAuthConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CdnAuthConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelGroupListConfiguration:
    boto3_raw_data: "type_defs.ChannelGroupListConfigurationTypeDef" = (
        dataclasses.field()
    )

    ChannelGroupName = field("ChannelGroupName")
    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ChannelGroupListConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelGroupListConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelListConfiguration:
    boto3_raw_data: "type_defs.ChannelListConfigurationTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    ChannelGroupName = field("ChannelGroupName")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Description = field("Description")
    InputType = field("InputType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelListConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelListConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelGroupRequest:
    boto3_raw_data: "type_defs.CreateChannelGroupRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ClientToken = field("ClientToken")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelGroupRequestTypeDef"]
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
class InputSwitchConfiguration:
    boto3_raw_data: "type_defs.InputSwitchConfigurationTypeDef" = dataclasses.field()

    MQCSInputSwitching = field("MQCSInputSwitching")
    PreferredInput = field("PreferredInput")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputSwitchConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSwitchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputHeaderConfiguration:
    boto3_raw_data: "type_defs.OutputHeaderConfigurationTypeDef" = dataclasses.field()

    PublishMQCS = field("PublishMQCS")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputHeaderConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputHeaderConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestEndpoint:
    boto3_raw_data: "type_defs.IngestEndpointTypeDef" = dataclasses.field()

    Id = field("Id")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IngestEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IngestEndpointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashBaseUrl:
    boto3_raw_data: "type_defs.DashBaseUrlTypeDef" = dataclasses.field()

    Url = field("Url")
    ServiceLocation = field("ServiceLocation")
    DvbPriority = field("DvbPriority")
    DvbWeight = field("DvbWeight")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashBaseUrlTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DashBaseUrlTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashProgramInformation:
    boto3_raw_data: "type_defs.DashProgramInformationTypeDef" = dataclasses.field()

    Title = field("Title")
    Source = field("Source")
    Copyright = field("Copyright")
    LanguageCode = field("LanguageCode")
    MoreInformationUrl = field("MoreInformationUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashProgramInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashProgramInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashUtcTiming:
    boto3_raw_data: "type_defs.DashUtcTimingTypeDef" = dataclasses.field()

    TimingMode = field("TimingMode")
    TimingSource = field("TimingSource")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashUtcTimingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DashUtcTimingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScteDash:
    boto3_raw_data: "type_defs.ScteDashTypeDef" = dataclasses.field()

    AdMarkerDash = field("AdMarkerDash")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScteDashTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScteDashTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HarvesterScheduleConfigurationOutput:
    boto3_raw_data: "type_defs.HarvesterScheduleConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HarvesterScheduleConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HarvesterScheduleConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScteHls:
    boto3_raw_data: "type_defs.ScteHlsTypeDef" = dataclasses.field()

    AdMarkerHls = field("AdMarkerHls")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScteHlsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScteHlsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTag:
    boto3_raw_data: "type_defs.StartTagTypeDef" = dataclasses.field()

    TimeOffset = field("TimeOffset")
    Precise = field("Precise")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForceEndpointErrorConfigurationOutput:
    boto3_raw_data: "type_defs.ForceEndpointErrorConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    EndpointErrorConditions = field("EndpointErrorConditions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ForceEndpointErrorConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForceEndpointErrorConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashDvbFontDownload:
    boto3_raw_data: "type_defs.DashDvbFontDownloadTypeDef" = dataclasses.field()

    Url = field("Url")
    MimeType = field("MimeType")
    FontFamily = field("FontFamily")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashDvbFontDownloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashDvbFontDownloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashDvbMetricsReporting:
    boto3_raw_data: "type_defs.DashDvbMetricsReportingTypeDef" = dataclasses.field()

    ReportingUrl = field("ReportingUrl")
    Probability = field("Probability")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashDvbMetricsReportingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashDvbMetricsReportingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashTtmlConfiguration:
    boto3_raw_data: "type_defs.DashTtmlConfigurationTypeDef" = dataclasses.field()

    TtmlProfile = field("TtmlProfile")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashTtmlConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashTtmlConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelGroupRequest:
    boto3_raw_data: "type_defs.DeleteChannelGroupRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelGroupRequestTypeDef"]
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

    ChannelGroupName = field("ChannelGroupName")
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

    ChannelGroupName = field("ChannelGroupName")
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
class DeleteOriginEndpointPolicyRequest:
    boto3_raw_data: "type_defs.DeleteOriginEndpointPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteOriginEndpointPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOriginEndpointPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOriginEndpointRequest:
    boto3_raw_data: "type_defs.DeleteOriginEndpointRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOriginEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOriginEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationConfig:
    boto3_raw_data: "type_defs.S3DestinationConfigTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    DestinationPath = field("DestinationPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionContractConfiguration:
    boto3_raw_data: "type_defs.EncryptionContractConfigurationTypeDef" = (
        dataclasses.field()
    )

    PresetSpeke20Audio = field("PresetSpeke20Audio")
    PresetSpeke20Video = field("PresetSpeke20Video")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EncryptionContractConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionContractConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionMethod:
    boto3_raw_data: "type_defs.EncryptionMethodTypeDef" = dataclasses.field()

    TsEncryptionMethod = field("TsEncryptionMethod")
    CmafEncryptionMethod = field("CmafEncryptionMethod")
    IsmEncryptionMethod = field("IsmEncryptionMethod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionMethodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionMethodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterConfigurationOutput:
    boto3_raw_data: "type_defs.FilterConfigurationOutputTypeDef" = dataclasses.field()

    ManifestFilter = field("ManifestFilter")
    Start = field("Start")
    End = field("End")
    TimeDelaySeconds = field("TimeDelaySeconds")
    ClipStartTime = field("ClipStartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForceEndpointErrorConfiguration:
    boto3_raw_data: "type_defs.ForceEndpointErrorConfigurationTypeDef" = (
        dataclasses.field()
    )

    EndpointErrorConditions = field("EndpointErrorConditions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ForceEndpointErrorConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForceEndpointErrorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelGroupRequest:
    boto3_raw_data: "type_defs.GetChannelGroupRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelGroupRequestTypeDef"]
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

    ChannelGroupName = field("ChannelGroupName")
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
class GetChannelRequest:
    boto3_raw_data: "type_defs.GetChannelRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetChannelRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHarvestJobRequest:
    boto3_raw_data: "type_defs.GetHarvestJobRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    HarvestJobName = field("HarvestJobName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHarvestJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHarvestJobRequestTypeDef"]
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
class GetOriginEndpointPolicyRequest:
    boto3_raw_data: "type_defs.GetOriginEndpointPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOriginEndpointPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginEndpointPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOriginEndpointRequest:
    boto3_raw_data: "type_defs.GetOriginEndpointRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOriginEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HarvestedDashManifest:
    boto3_raw_data: "type_defs.HarvestedDashManifestTypeDef" = dataclasses.field()

    ManifestName = field("ManifestName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HarvestedDashManifestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HarvestedDashManifestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HarvestedHlsManifest:
    boto3_raw_data: "type_defs.HarvestedHlsManifestTypeDef" = dataclasses.field()

    ManifestName = field("ManifestName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HarvestedHlsManifestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HarvestedHlsManifestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HarvestedLowLatencyHlsManifest:
    boto3_raw_data: "type_defs.HarvestedLowLatencyHlsManifestTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HarvestedLowLatencyHlsManifestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HarvestedLowLatencyHlsManifestTypeDef"]
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
class ListChannelGroupsRequest:
    boto3_raw_data: "type_defs.ListChannelGroupsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelGroupsRequestTypeDef"]
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

    ChannelGroupName = field("ChannelGroupName")
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
class ListDashManifestConfiguration:
    boto3_raw_data: "type_defs.ListDashManifestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")
    Url = field("Url")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDashManifestConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDashManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHarvestJobsRequest:
    boto3_raw_data: "type_defs.ListHarvestJobsRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    Status = field("Status")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHarvestJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHarvestJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHlsManifestConfiguration:
    boto3_raw_data: "type_defs.ListHlsManifestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")
    ChildManifestName = field("ChildManifestName")
    Url = field("Url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHlsManifestConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHlsManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLowLatencyHlsManifestConfiguration:
    boto3_raw_data: "type_defs.ListLowLatencyHlsManifestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")
    ChildManifestName = field("ChildManifestName")
    Url = field("Url")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLowLatencyHlsManifestConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLowLatencyHlsManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMssManifestConfiguration:
    boto3_raw_data: "type_defs.ListMssManifestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")
    Url = field("Url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMssManifestConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMssManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginEndpointsRequest:
    boto3_raw_data: "type_defs.ListOriginEndpointsRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOriginEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginEndpointsRequestTypeDef"]
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
class PutChannelPolicyRequest:
    boto3_raw_data: "type_defs.PutChannelPolicyRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
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
class ResetChannelStateRequest:
    boto3_raw_data: "type_defs.ResetChannelStateRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetChannelStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetChannelStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetOriginEndpointStateRequest:
    boto3_raw_data: "type_defs.ResetOriginEndpointStateRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResetOriginEndpointStateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetOriginEndpointStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScteOutput:
    boto3_raw_data: "type_defs.ScteOutputTypeDef" = dataclasses.field()

    ScteFilter = field("ScteFilter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScteOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScteOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte:
    boto3_raw_data: "type_defs.ScteTypeDef" = dataclasses.field()

    ScteFilter = field("ScteFilter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScteTypeDef"]]
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
class UpdateChannelGroupRequest:
    boto3_raw_data: "type_defs.UpdateChannelGroupRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ETag = field("ETag")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelGroupResponse:
    boto3_raw_data: "type_defs.CreateChannelGroupResponseTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    Arn = field("Arn")
    EgressDomain = field("EgressDomain")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    ETag = field("ETag")
    Description = field("Description")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelGroupResponseTypeDef"]
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
class GetChannelGroupResponse:
    boto3_raw_data: "type_defs.GetChannelGroupResponseTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    Arn = field("Arn")
    EgressDomain = field("EgressDomain")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Description = field("Description")
    ETag = field("ETag")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelGroupResponseTypeDef"]
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

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
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
class GetOriginEndpointPolicyResponse:
    boto3_raw_data: "type_defs.GetOriginEndpointPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    Policy = field("Policy")

    @cached_property
    def CdnAuthConfiguration(self):  # pragma: no cover
        return CdnAuthConfigurationOutput.make_one(
            self.boto3_raw_data["CdnAuthConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOriginEndpointPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginEndpointPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelGroupsResponse:
    boto3_raw_data: "type_defs.ListChannelGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ChannelGroupListConfiguration.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelGroupsResponseTypeDef"]
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
        return ChannelListConfiguration.make_many(self.boto3_raw_data["Items"])

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
class ResetChannelStateResponse:
    boto3_raw_data: "type_defs.ResetChannelStateResponseTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    Arn = field("Arn")
    ResetAt = field("ResetAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetChannelStateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetChannelStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetOriginEndpointStateResponse:
    boto3_raw_data: "type_defs.ResetOriginEndpointStateResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    Arn = field("Arn")
    ResetAt = field("ResetAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResetOriginEndpointStateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetOriginEndpointStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelGroupResponse:
    boto3_raw_data: "type_defs.UpdateChannelGroupResponseTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    Arn = field("Arn")
    EgressDomain = field("EgressDomain")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Description = field("Description")
    ETag = field("ETag")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelGroupResponseTypeDef"]
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

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    ClientToken = field("ClientToken")
    InputType = field("InputType")
    Description = field("Description")

    @cached_property
    def InputSwitchConfiguration(self):  # pragma: no cover
        return InputSwitchConfiguration.make_one(
            self.boto3_raw_data["InputSwitchConfiguration"]
        )

    @cached_property
    def OutputHeaderConfiguration(self):  # pragma: no cover
        return OutputHeaderConfiguration.make_one(
            self.boto3_raw_data["OutputHeaderConfiguration"]
        )

    Tags = field("Tags")

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

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    ETag = field("ETag")
    Description = field("Description")

    @cached_property
    def InputSwitchConfiguration(self):  # pragma: no cover
        return InputSwitchConfiguration.make_one(
            self.boto3_raw_data["InputSwitchConfiguration"]
        )

    @cached_property
    def OutputHeaderConfiguration(self):  # pragma: no cover
        return OutputHeaderConfiguration.make_one(
            self.boto3_raw_data["OutputHeaderConfiguration"]
        )

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
class CreateChannelResponse:
    boto3_raw_data: "type_defs.CreateChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    ChannelGroupName = field("ChannelGroupName")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Description = field("Description")

    @cached_property
    def IngestEndpoints(self):  # pragma: no cover
        return IngestEndpoint.make_many(self.boto3_raw_data["IngestEndpoints"])

    InputType = field("InputType")
    ETag = field("ETag")
    Tags = field("Tags")

    @cached_property
    def InputSwitchConfiguration(self):  # pragma: no cover
        return InputSwitchConfiguration.make_one(
            self.boto3_raw_data["InputSwitchConfiguration"]
        )

    @cached_property
    def OutputHeaderConfiguration(self):  # pragma: no cover
        return OutputHeaderConfiguration.make_one(
            self.boto3_raw_data["OutputHeaderConfiguration"]
        )

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
class GetChannelResponse:
    boto3_raw_data: "type_defs.GetChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelName = field("ChannelName")
    ChannelGroupName = field("ChannelGroupName")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    ResetAt = field("ResetAt")
    Description = field("Description")

    @cached_property
    def IngestEndpoints(self):  # pragma: no cover
        return IngestEndpoint.make_many(self.boto3_raw_data["IngestEndpoints"])

    InputType = field("InputType")
    ETag = field("ETag")
    Tags = field("Tags")

    @cached_property
    def InputSwitchConfiguration(self):  # pragma: no cover
        return InputSwitchConfiguration.make_one(
            self.boto3_raw_data["InputSwitchConfiguration"]
        )

    @cached_property
    def OutputHeaderConfiguration(self):  # pragma: no cover
        return OutputHeaderConfiguration.make_one(
            self.boto3_raw_data["OutputHeaderConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelResponseTypeDef"]
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
    ChannelGroupName = field("ChannelGroupName")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Description = field("Description")

    @cached_property
    def IngestEndpoints(self):  # pragma: no cover
        return IngestEndpoint.make_many(self.boto3_raw_data["IngestEndpoints"])

    InputType = field("InputType")
    ETag = field("ETag")
    Tags = field("Tags")

    @cached_property
    def InputSwitchConfiguration(self):  # pragma: no cover
        return InputSwitchConfiguration.make_one(
            self.boto3_raw_data["InputSwitchConfiguration"]
        )

    @cached_property
    def OutputHeaderConfiguration(self):  # pragma: no cover
        return OutputHeaderConfiguration.make_one(
            self.boto3_raw_data["OutputHeaderConfiguration"]
        )

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
class DashDvbSettingsOutput:
    boto3_raw_data: "type_defs.DashDvbSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def FontDownload(self):  # pragma: no cover
        return DashDvbFontDownload.make_one(self.boto3_raw_data["FontDownload"])

    @cached_property
    def ErrorMetrics(self):  # pragma: no cover
        return DashDvbMetricsReporting.make_many(self.boto3_raw_data["ErrorMetrics"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashDvbSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashDvbSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashDvbSettings:
    boto3_raw_data: "type_defs.DashDvbSettingsTypeDef" = dataclasses.field()

    @cached_property
    def FontDownload(self):  # pragma: no cover
        return DashDvbFontDownload.make_one(self.boto3_raw_data["FontDownload"])

    @cached_property
    def ErrorMetrics(self):  # pragma: no cover
        return DashDvbMetricsReporting.make_many(self.boto3_raw_data["ErrorMetrics"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashDvbSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DashDvbSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashSubtitleConfiguration:
    boto3_raw_data: "type_defs.DashSubtitleConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def TtmlConfiguration(self):  # pragma: no cover
        return DashTtmlConfiguration.make_one(self.boto3_raw_data["TtmlConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashSubtitleConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashSubtitleConfigurationTypeDef"]
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

    @cached_property
    def S3Destination(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["S3Destination"])

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
class SpekeKeyProviderOutput:
    boto3_raw_data: "type_defs.SpekeKeyProviderOutputTypeDef" = dataclasses.field()

    @cached_property
    def EncryptionContractConfiguration(self):  # pragma: no cover
        return EncryptionContractConfiguration.make_one(
            self.boto3_raw_data["EncryptionContractConfiguration"]
        )

    ResourceId = field("ResourceId")
    DrmSystems = field("DrmSystems")
    RoleArn = field("RoleArn")
    Url = field("Url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpekeKeyProviderOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpekeKeyProviderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpekeKeyProvider:
    boto3_raw_data: "type_defs.SpekeKeyProviderTypeDef" = dataclasses.field()

    @cached_property
    def EncryptionContractConfiguration(self):  # pragma: no cover
        return EncryptionContractConfiguration.make_one(
            self.boto3_raw_data["EncryptionContractConfiguration"]
        )

    ResourceId = field("ResourceId")
    DrmSystems = field("DrmSystems")
    RoleArn = field("RoleArn")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpekeKeyProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpekeKeyProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHlsManifestConfiguration:
    boto3_raw_data: "type_defs.GetHlsManifestConfigurationTypeDef" = dataclasses.field()

    ManifestName = field("ManifestName")
    Url = field("Url")
    ChildManifestName = field("ChildManifestName")
    ManifestWindowSeconds = field("ManifestWindowSeconds")
    ProgramDateTimeIntervalSeconds = field("ProgramDateTimeIntervalSeconds")

    @cached_property
    def ScteHls(self):  # pragma: no cover
        return ScteHls.make_one(self.boto3_raw_data["ScteHls"])

    @cached_property
    def FilterConfiguration(self):  # pragma: no cover
        return FilterConfigurationOutput.make_one(
            self.boto3_raw_data["FilterConfiguration"]
        )

    @cached_property
    def StartTag(self):  # pragma: no cover
        return StartTag.make_one(self.boto3_raw_data["StartTag"])

    UrlEncodeChildManifest = field("UrlEncodeChildManifest")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHlsManifestConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHlsManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLowLatencyHlsManifestConfiguration:
    boto3_raw_data: "type_defs.GetLowLatencyHlsManifestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")
    Url = field("Url")
    ChildManifestName = field("ChildManifestName")
    ManifestWindowSeconds = field("ManifestWindowSeconds")
    ProgramDateTimeIntervalSeconds = field("ProgramDateTimeIntervalSeconds")

    @cached_property
    def ScteHls(self):  # pragma: no cover
        return ScteHls.make_one(self.boto3_raw_data["ScteHls"])

    @cached_property
    def FilterConfiguration(self):  # pragma: no cover
        return FilterConfigurationOutput.make_one(
            self.boto3_raw_data["FilterConfiguration"]
        )

    @cached_property
    def StartTag(self):  # pragma: no cover
        return StartTag.make_one(self.boto3_raw_data["StartTag"])

    UrlEncodeChildManifest = field("UrlEncodeChildManifest")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLowLatencyHlsManifestConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLowLatencyHlsManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMssManifestConfiguration:
    boto3_raw_data: "type_defs.GetMssManifestConfigurationTypeDef" = dataclasses.field()

    ManifestName = field("ManifestName")
    Url = field("Url")

    @cached_property
    def FilterConfiguration(self):  # pragma: no cover
        return FilterConfigurationOutput.make_one(
            self.boto3_raw_data["FilterConfiguration"]
        )

    ManifestWindowSeconds = field("ManifestWindowSeconds")
    ManifestLayout = field("ManifestLayout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMssManifestConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMssManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterConfiguration:
    boto3_raw_data: "type_defs.FilterConfigurationTypeDef" = dataclasses.field()

    ManifestFilter = field("ManifestFilter")
    Start = field("Start")
    End = field("End")
    TimeDelaySeconds = field("TimeDelaySeconds")
    ClipStartTime = field("ClipStartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HarvesterScheduleConfiguration:
    boto3_raw_data: "type_defs.HarvesterScheduleConfigurationTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HarvesterScheduleConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HarvesterScheduleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHarvestJobRequestWait:
    boto3_raw_data: "type_defs.GetHarvestJobRequestWaitTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    HarvestJobName = field("HarvestJobName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHarvestJobRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHarvestJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HarvestedManifestsOutput:
    boto3_raw_data: "type_defs.HarvestedManifestsOutputTypeDef" = dataclasses.field()

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return HarvestedHlsManifest.make_many(self.boto3_raw_data["HlsManifests"])

    @cached_property
    def DashManifests(self):  # pragma: no cover
        return HarvestedDashManifest.make_many(self.boto3_raw_data["DashManifests"])

    @cached_property
    def LowLatencyHlsManifests(self):  # pragma: no cover
        return HarvestedLowLatencyHlsManifest.make_many(
            self.boto3_raw_data["LowLatencyHlsManifests"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HarvestedManifestsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HarvestedManifestsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HarvestedManifests:
    boto3_raw_data: "type_defs.HarvestedManifestsTypeDef" = dataclasses.field()

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return HarvestedHlsManifest.make_many(self.boto3_raw_data["HlsManifests"])

    @cached_property
    def DashManifests(self):  # pragma: no cover
        return HarvestedDashManifest.make_many(self.boto3_raw_data["DashManifests"])

    @cached_property
    def LowLatencyHlsManifests(self):  # pragma: no cover
        return HarvestedLowLatencyHlsManifest.make_many(
            self.boto3_raw_data["LowLatencyHlsManifests"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HarvestedManifestsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HarvestedManifestsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListChannelGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListChannelGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelGroupsRequestPaginateTypeDef"]
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

    ChannelGroupName = field("ChannelGroupName")

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
class ListHarvestJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListHarvestJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListHarvestJobsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHarvestJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListOriginEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOriginEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginEndpointListConfiguration:
    boto3_raw_data: "type_defs.OriginEndpointListConfigurationTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    ContainerType = field("ContainerType")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return ListHlsManifestConfiguration.make_many(
            self.boto3_raw_data["HlsManifests"]
        )

    @cached_property
    def LowLatencyHlsManifests(self):  # pragma: no cover
        return ListLowLatencyHlsManifestConfiguration.make_many(
            self.boto3_raw_data["LowLatencyHlsManifests"]
        )

    @cached_property
    def DashManifests(self):  # pragma: no cover
        return ListDashManifestConfiguration.make_many(
            self.boto3_raw_data["DashManifests"]
        )

    @cached_property
    def MssManifests(self):  # pragma: no cover
        return ListMssManifestConfiguration.make_many(
            self.boto3_raw_data["MssManifests"]
        )

    @cached_property
    def ForceEndpointErrorConfiguration(self):  # pragma: no cover
        return ForceEndpointErrorConfigurationOutput.make_one(
            self.boto3_raw_data["ForceEndpointErrorConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OriginEndpointListConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginEndpointListConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutOriginEndpointPolicyRequest:
    boto3_raw_data: "type_defs.PutOriginEndpointPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    Policy = field("Policy")
    CdnAuthConfiguration = field("CdnAuthConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutOriginEndpointPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutOriginEndpointPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDashManifestConfiguration:
    boto3_raw_data: "type_defs.GetDashManifestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")
    Url = field("Url")
    ManifestWindowSeconds = field("ManifestWindowSeconds")

    @cached_property
    def FilterConfiguration(self):  # pragma: no cover
        return FilterConfigurationOutput.make_one(
            self.boto3_raw_data["FilterConfiguration"]
        )

    MinUpdatePeriodSeconds = field("MinUpdatePeriodSeconds")
    MinBufferTimeSeconds = field("MinBufferTimeSeconds")
    SuggestedPresentationDelaySeconds = field("SuggestedPresentationDelaySeconds")
    SegmentTemplateFormat = field("SegmentTemplateFormat")
    PeriodTriggers = field("PeriodTriggers")

    @cached_property
    def ScteDash(self):  # pragma: no cover
        return ScteDash.make_one(self.boto3_raw_data["ScteDash"])

    DrmSignaling = field("DrmSignaling")

    @cached_property
    def UtcTiming(self):  # pragma: no cover
        return DashUtcTiming.make_one(self.boto3_raw_data["UtcTiming"])

    Profiles = field("Profiles")

    @cached_property
    def BaseUrls(self):  # pragma: no cover
        return DashBaseUrl.make_many(self.boto3_raw_data["BaseUrls"])

    @cached_property
    def ProgramInformation(self):  # pragma: no cover
        return DashProgramInformation.make_one(
            self.boto3_raw_data["ProgramInformation"]
        )

    @cached_property
    def DvbSettings(self):  # pragma: no cover
        return DashDvbSettingsOutput.make_one(self.boto3_raw_data["DvbSettings"])

    Compactness = field("Compactness")

    @cached_property
    def SubtitleConfiguration(self):  # pragma: no cover
        return DashSubtitleConfiguration.make_one(
            self.boto3_raw_data["SubtitleConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDashManifestConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDashManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionOutput:
    boto3_raw_data: "type_defs.EncryptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def EncryptionMethod(self):  # pragma: no cover
        return EncryptionMethod.make_one(self.boto3_raw_data["EncryptionMethod"])

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProviderOutput.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    ConstantInitializationVector = field("ConstantInitializationVector")
    KeyRotationIntervalSeconds = field("KeyRotationIntervalSeconds")
    CmafExcludeSegmentDrmMetadata = field("CmafExcludeSegmentDrmMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Encryption:
    boto3_raw_data: "type_defs.EncryptionTypeDef" = dataclasses.field()

    @cached_property
    def EncryptionMethod(self):  # pragma: no cover
        return EncryptionMethod.make_one(self.boto3_raw_data["EncryptionMethod"])

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProvider.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    ConstantInitializationVector = field("ConstantInitializationVector")
    KeyRotationIntervalSeconds = field("KeyRotationIntervalSeconds")
    CmafExcludeSegmentDrmMetadata = field("CmafExcludeSegmentDrmMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncryptionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHarvestJobResponse:
    boto3_raw_data: "type_defs.CreateHarvestJobResponseTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    HarvestJobName = field("HarvestJobName")

    @cached_property
    def HarvestedManifests(self):  # pragma: no cover
        return HarvestedManifestsOutput.make_one(
            self.boto3_raw_data["HarvestedManifests"]
        )

    Description = field("Description")

    @cached_property
    def ScheduleConfiguration(self):  # pragma: no cover
        return HarvesterScheduleConfigurationOutput.make_one(
            self.boto3_raw_data["ScheduleConfiguration"]
        )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Status = field("Status")
    ErrorMessage = field("ErrorMessage")
    ETag = field("ETag")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHarvestJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHarvestJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHarvestJobResponse:
    boto3_raw_data: "type_defs.GetHarvestJobResponseTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    HarvestJobName = field("HarvestJobName")

    @cached_property
    def HarvestedManifests(self):  # pragma: no cover
        return HarvestedManifestsOutput.make_one(
            self.boto3_raw_data["HarvestedManifests"]
        )

    Description = field("Description")

    @cached_property
    def ScheduleConfiguration(self):  # pragma: no cover
        return HarvesterScheduleConfigurationOutput.make_one(
            self.boto3_raw_data["ScheduleConfiguration"]
        )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Status = field("Status")
    ErrorMessage = field("ErrorMessage")
    ETag = field("ETag")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHarvestJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHarvestJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HarvestJob:
    boto3_raw_data: "type_defs.HarvestJobTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    HarvestJobName = field("HarvestJobName")

    @cached_property
    def HarvestedManifests(self):  # pragma: no cover
        return HarvestedManifestsOutput.make_one(
            self.boto3_raw_data["HarvestedManifests"]
        )

    @cached_property
    def ScheduleConfiguration(self):  # pragma: no cover
        return HarvesterScheduleConfigurationOutput.make_one(
            self.boto3_raw_data["ScheduleConfiguration"]
        )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Status = field("Status")
    Description = field("Description")
    ErrorMessage = field("ErrorMessage")
    ETag = field("ETag")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HarvestJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HarvestJobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginEndpointsResponse:
    boto3_raw_data: "type_defs.ListOriginEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return OriginEndpointListConfiguration.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOriginEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentOutput:
    boto3_raw_data: "type_defs.SegmentOutputTypeDef" = dataclasses.field()

    SegmentDurationSeconds = field("SegmentDurationSeconds")
    SegmentName = field("SegmentName")
    TsUseAudioRenditionGroup = field("TsUseAudioRenditionGroup")
    IncludeIframeOnlyStreams = field("IncludeIframeOnlyStreams")
    TsIncludeDvbSubtitles = field("TsIncludeDvbSubtitles")

    @cached_property
    def Scte(self):  # pragma: no cover
        return ScteOutput.make_one(self.boto3_raw_data["Scte"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return EncryptionOutput.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SegmentOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Segment:
    boto3_raw_data: "type_defs.SegmentTypeDef" = dataclasses.field()

    SegmentDurationSeconds = field("SegmentDurationSeconds")
    SegmentName = field("SegmentName")
    TsUseAudioRenditionGroup = field("TsUseAudioRenditionGroup")
    IncludeIframeOnlyStreams = field("IncludeIframeOnlyStreams")
    TsIncludeDvbSubtitles = field("TsIncludeDvbSubtitles")

    @cached_property
    def Scte(self):  # pragma: no cover
        return Scte.make_one(self.boto3_raw_data["Scte"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SegmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDashManifestConfiguration:
    boto3_raw_data: "type_defs.CreateDashManifestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")
    ManifestWindowSeconds = field("ManifestWindowSeconds")
    FilterConfiguration = field("FilterConfiguration")
    MinUpdatePeriodSeconds = field("MinUpdatePeriodSeconds")
    MinBufferTimeSeconds = field("MinBufferTimeSeconds")
    SuggestedPresentationDelaySeconds = field("SuggestedPresentationDelaySeconds")
    SegmentTemplateFormat = field("SegmentTemplateFormat")
    PeriodTriggers = field("PeriodTriggers")

    @cached_property
    def ScteDash(self):  # pragma: no cover
        return ScteDash.make_one(self.boto3_raw_data["ScteDash"])

    DrmSignaling = field("DrmSignaling")

    @cached_property
    def UtcTiming(self):  # pragma: no cover
        return DashUtcTiming.make_one(self.boto3_raw_data["UtcTiming"])

    Profiles = field("Profiles")

    @cached_property
    def BaseUrls(self):  # pragma: no cover
        return DashBaseUrl.make_many(self.boto3_raw_data["BaseUrls"])

    @cached_property
    def ProgramInformation(self):  # pragma: no cover
        return DashProgramInformation.make_one(
            self.boto3_raw_data["ProgramInformation"]
        )

    DvbSettings = field("DvbSettings")
    Compactness = field("Compactness")

    @cached_property
    def SubtitleConfiguration(self):  # pragma: no cover
        return DashSubtitleConfiguration.make_one(
            self.boto3_raw_data["SubtitleConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDashManifestConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDashManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHlsManifestConfiguration:
    boto3_raw_data: "type_defs.CreateHlsManifestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")
    ChildManifestName = field("ChildManifestName")

    @cached_property
    def ScteHls(self):  # pragma: no cover
        return ScteHls.make_one(self.boto3_raw_data["ScteHls"])

    @cached_property
    def StartTag(self):  # pragma: no cover
        return StartTag.make_one(self.boto3_raw_data["StartTag"])

    ManifestWindowSeconds = field("ManifestWindowSeconds")
    ProgramDateTimeIntervalSeconds = field("ProgramDateTimeIntervalSeconds")
    FilterConfiguration = field("FilterConfiguration")
    UrlEncodeChildManifest = field("UrlEncodeChildManifest")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateHlsManifestConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHlsManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLowLatencyHlsManifestConfiguration:
    boto3_raw_data: "type_defs.CreateLowLatencyHlsManifestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")
    ChildManifestName = field("ChildManifestName")

    @cached_property
    def ScteHls(self):  # pragma: no cover
        return ScteHls.make_one(self.boto3_raw_data["ScteHls"])

    @cached_property
    def StartTag(self):  # pragma: no cover
        return StartTag.make_one(self.boto3_raw_data["StartTag"])

    ManifestWindowSeconds = field("ManifestWindowSeconds")
    ProgramDateTimeIntervalSeconds = field("ProgramDateTimeIntervalSeconds")
    FilterConfiguration = field("FilterConfiguration")
    UrlEncodeChildManifest = field("UrlEncodeChildManifest")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLowLatencyHlsManifestConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLowLatencyHlsManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMssManifestConfiguration:
    boto3_raw_data: "type_defs.CreateMssManifestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ManifestName = field("ManifestName")
    ManifestWindowSeconds = field("ManifestWindowSeconds")
    FilterConfiguration = field("FilterConfiguration")
    ManifestLayout = field("ManifestLayout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMssManifestConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMssManifestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHarvestJobsResponse:
    boto3_raw_data: "type_defs.ListHarvestJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return HarvestJob.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHarvestJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHarvestJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHarvestJobRequest:
    boto3_raw_data: "type_defs.CreateHarvestJobRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    HarvestedManifests = field("HarvestedManifests")
    ScheduleConfiguration = field("ScheduleConfiguration")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    Description = field("Description")
    ClientToken = field("ClientToken")
    HarvestJobName = field("HarvestJobName")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHarvestJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHarvestJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOriginEndpointResponse:
    boto3_raw_data: "type_defs.CreateOriginEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    ContainerType = field("ContainerType")

    @cached_property
    def Segment(self):  # pragma: no cover
        return SegmentOutput.make_one(self.boto3_raw_data["Segment"])

    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Description = field("Description")
    StartoverWindowSeconds = field("StartoverWindowSeconds")

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return GetHlsManifestConfiguration.make_many(
            self.boto3_raw_data["HlsManifests"]
        )

    @cached_property
    def LowLatencyHlsManifests(self):  # pragma: no cover
        return GetLowLatencyHlsManifestConfiguration.make_many(
            self.boto3_raw_data["LowLatencyHlsManifests"]
        )

    @cached_property
    def DashManifests(self):  # pragma: no cover
        return GetDashManifestConfiguration.make_many(
            self.boto3_raw_data["DashManifests"]
        )

    @cached_property
    def MssManifests(self):  # pragma: no cover
        return GetMssManifestConfiguration.make_many(
            self.boto3_raw_data["MssManifests"]
        )

    @cached_property
    def ForceEndpointErrorConfiguration(self):  # pragma: no cover
        return ForceEndpointErrorConfigurationOutput.make_one(
            self.boto3_raw_data["ForceEndpointErrorConfiguration"]
        )

    ETag = field("ETag")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOriginEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOriginEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOriginEndpointResponse:
    boto3_raw_data: "type_defs.GetOriginEndpointResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    ContainerType = field("ContainerType")

    @cached_property
    def Segment(self):  # pragma: no cover
        return SegmentOutput.make_one(self.boto3_raw_data["Segment"])

    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    ResetAt = field("ResetAt")
    Description = field("Description")
    StartoverWindowSeconds = field("StartoverWindowSeconds")

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return GetHlsManifestConfiguration.make_many(
            self.boto3_raw_data["HlsManifests"]
        )

    @cached_property
    def LowLatencyHlsManifests(self):  # pragma: no cover
        return GetLowLatencyHlsManifestConfiguration.make_many(
            self.boto3_raw_data["LowLatencyHlsManifests"]
        )

    @cached_property
    def DashManifests(self):  # pragma: no cover
        return GetDashManifestConfiguration.make_many(
            self.boto3_raw_data["DashManifests"]
        )

    @cached_property
    def MssManifests(self):  # pragma: no cover
        return GetMssManifestConfiguration.make_many(
            self.boto3_raw_data["MssManifests"]
        )

    @cached_property
    def ForceEndpointErrorConfiguration(self):  # pragma: no cover
        return ForceEndpointErrorConfigurationOutput.make_one(
            self.boto3_raw_data["ForceEndpointErrorConfiguration"]
        )

    ETag = field("ETag")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOriginEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOriginEndpointResponse:
    boto3_raw_data: "type_defs.UpdateOriginEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    ContainerType = field("ContainerType")

    @cached_property
    def Segment(self):  # pragma: no cover
        return SegmentOutput.make_one(self.boto3_raw_data["Segment"])

    CreatedAt = field("CreatedAt")
    ModifiedAt = field("ModifiedAt")
    Description = field("Description")
    StartoverWindowSeconds = field("StartoverWindowSeconds")

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return GetHlsManifestConfiguration.make_many(
            self.boto3_raw_data["HlsManifests"]
        )

    @cached_property
    def LowLatencyHlsManifests(self):  # pragma: no cover
        return GetLowLatencyHlsManifestConfiguration.make_many(
            self.boto3_raw_data["LowLatencyHlsManifests"]
        )

    @cached_property
    def MssManifests(self):  # pragma: no cover
        return GetMssManifestConfiguration.make_many(
            self.boto3_raw_data["MssManifests"]
        )

    @cached_property
    def ForceEndpointErrorConfiguration(self):  # pragma: no cover
        return ForceEndpointErrorConfigurationOutput.make_one(
            self.boto3_raw_data["ForceEndpointErrorConfiguration"]
        )

    ETag = field("ETag")
    Tags = field("Tags")

    @cached_property
    def DashManifests(self):  # pragma: no cover
        return GetDashManifestConfiguration.make_many(
            self.boto3_raw_data["DashManifests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOriginEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOriginEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOriginEndpointRequest:
    boto3_raw_data: "type_defs.CreateOriginEndpointRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    ContainerType = field("ContainerType")
    Segment = field("Segment")
    ClientToken = field("ClientToken")
    Description = field("Description")
    StartoverWindowSeconds = field("StartoverWindowSeconds")

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return CreateHlsManifestConfiguration.make_many(
            self.boto3_raw_data["HlsManifests"]
        )

    @cached_property
    def LowLatencyHlsManifests(self):  # pragma: no cover
        return CreateLowLatencyHlsManifestConfiguration.make_many(
            self.boto3_raw_data["LowLatencyHlsManifests"]
        )

    @cached_property
    def DashManifests(self):  # pragma: no cover
        return CreateDashManifestConfiguration.make_many(
            self.boto3_raw_data["DashManifests"]
        )

    @cached_property
    def MssManifests(self):  # pragma: no cover
        return CreateMssManifestConfiguration.make_many(
            self.boto3_raw_data["MssManifests"]
        )

    ForceEndpointErrorConfiguration = field("ForceEndpointErrorConfiguration")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOriginEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOriginEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOriginEndpointRequest:
    boto3_raw_data: "type_defs.UpdateOriginEndpointRequestTypeDef" = dataclasses.field()

    ChannelGroupName = field("ChannelGroupName")
    ChannelName = field("ChannelName")
    OriginEndpointName = field("OriginEndpointName")
    ContainerType = field("ContainerType")
    Segment = field("Segment")
    Description = field("Description")
    StartoverWindowSeconds = field("StartoverWindowSeconds")

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return CreateHlsManifestConfiguration.make_many(
            self.boto3_raw_data["HlsManifests"]
        )

    @cached_property
    def LowLatencyHlsManifests(self):  # pragma: no cover
        return CreateLowLatencyHlsManifestConfiguration.make_many(
            self.boto3_raw_data["LowLatencyHlsManifests"]
        )

    @cached_property
    def DashManifests(self):  # pragma: no cover
        return CreateDashManifestConfiguration.make_many(
            self.boto3_raw_data["DashManifests"]
        )

    @cached_property
    def MssManifests(self):  # pragma: no cover
        return CreateMssManifestConfiguration.make_many(
            self.boto3_raw_data["MssManifests"]
        )

    ForceEndpointErrorConfiguration = field("ForceEndpointErrorConfiguration")
    ETag = field("ETag")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOriginEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOriginEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
