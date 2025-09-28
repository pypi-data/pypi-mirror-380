# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mailmanager import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddHeaderAction:
    boto3_raw_data: "type_defs.AddHeaderActionTypeDef" = dataclasses.field()

    HeaderName = field("HeaderName")
    HeaderValue = field("HeaderValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddHeaderActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddHeaderActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonInstance:
    boto3_raw_data: "type_defs.AddonInstanceTypeDef" = dataclasses.field()

    AddonInstanceId = field("AddonInstanceId")
    AddonSubscriptionId = field("AddonSubscriptionId")
    AddonName = field("AddonName")
    AddonInstanceArn = field("AddonInstanceArn")
    CreatedTimestamp = field("CreatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddonInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddonInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonSubscription:
    boto3_raw_data: "type_defs.AddonSubscriptionTypeDef" = dataclasses.field()

    AddonSubscriptionId = field("AddonSubscriptionId")
    AddonName = field("AddonName")
    AddonSubscriptionArn = field("AddonSubscriptionArn")
    CreatedTimestamp = field("CreatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddonSubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddonSubscriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddressFilter:
    boto3_raw_data: "type_defs.AddressFilterTypeDef" = dataclasses.field()

    AddressPrefix = field("AddressPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddressList:
    boto3_raw_data: "type_defs.AddressListTypeDef" = dataclasses.field()

    AddressListId = field("AddressListId")
    AddressListArn = field("AddressListArn")
    AddressListName = field("AddressListName")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressListTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Analysis:
    boto3_raw_data: "type_defs.AnalysisTypeDef" = dataclasses.field()

    Analyzer = field("Analyzer")
    ResultField = field("ResultField")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveAction:
    boto3_raw_data: "type_defs.ArchiveActionTypeDef" = dataclasses.field()

    TargetArchive = field("TargetArchive")
    ActionFailurePolicy = field("ActionFailurePolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArchiveActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArchiveActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveBooleanToEvaluate:
    boto3_raw_data: "type_defs.ArchiveBooleanToEvaluateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveBooleanToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveBooleanToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveRetention:
    boto3_raw_data: "type_defs.ArchiveRetentionTypeDef" = dataclasses.field()

    RetentionPeriod = field("RetentionPeriod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArchiveRetentionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveRetentionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveStringToEvaluate:
    boto3_raw_data: "type_defs.ArchiveStringToEvaluateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveStringToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveStringToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Archive:
    boto3_raw_data: "type_defs.ArchiveTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")
    ArchiveName = field("ArchiveName")
    ArchiveState = field("ArchiveState")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArchiveTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArchiveTypeDef"]]
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
class ImportDataFormat:
    boto3_raw_data: "type_defs.ImportDataFormatTypeDef" = dataclasses.field()

    ImportDataType = field("ImportDataType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportDataFormatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDataFormatTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressPointConfiguration:
    boto3_raw_data: "type_defs.IngressPointConfigurationTypeDef" = dataclasses.field()

    SmtpPassword = field("SmtpPassword")
    SecretArn = field("SecretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressPointConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressPointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAddonInstanceRequest:
    boto3_raw_data: "type_defs.DeleteAddonInstanceRequestTypeDef" = dataclasses.field()

    AddonInstanceId = field("AddonInstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAddonInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAddonInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAddonSubscriptionRequest:
    boto3_raw_data: "type_defs.DeleteAddonSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    AddonSubscriptionId = field("AddonSubscriptionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAddonSubscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAddonSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAddressListRequest:
    boto3_raw_data: "type_defs.DeleteAddressListRequestTypeDef" = dataclasses.field()

    AddressListId = field("AddressListId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAddressListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAddressListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteArchiveRequest:
    boto3_raw_data: "type_defs.DeleteArchiveRequestTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteArchiveRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteArchiveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIngressPointRequest:
    boto3_raw_data: "type_defs.DeleteIngressPointRequestTypeDef" = dataclasses.field()

    IngressPointId = field("IngressPointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIngressPointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIngressPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRelayRequest:
    boto3_raw_data: "type_defs.DeleteRelayRequestTypeDef" = dataclasses.field()

    RelayId = field("RelayId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRelayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRelayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRuleSetRequest:
    boto3_raw_data: "type_defs.DeleteRuleSetRequestTypeDef" = dataclasses.field()

    RuleSetId = field("RuleSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRuleSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRuleSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrafficPolicyRequest:
    boto3_raw_data: "type_defs.DeleteTrafficPolicyRequestTypeDef" = dataclasses.field()

    TrafficPolicyId = field("TrafficPolicyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTrafficPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrafficPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliverToMailboxAction:
    boto3_raw_data: "type_defs.DeliverToMailboxActionTypeDef" = dataclasses.field()

    MailboxArn = field("MailboxArn")
    RoleArn = field("RoleArn")
    ActionFailurePolicy = field("ActionFailurePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeliverToMailboxActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliverToMailboxActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliverToQBusinessAction:
    boto3_raw_data: "type_defs.DeliverToQBusinessActionTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    IndexId = field("IndexId")
    RoleArn = field("RoleArn")
    ActionFailurePolicy = field("ActionFailurePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeliverToQBusinessActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliverToQBusinessActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterMemberFromAddressListRequest:
    boto3_raw_data: "type_defs.DeregisterMemberFromAddressListRequestTypeDef" = (
        dataclasses.field()
    )

    AddressListId = field("AddressListId")
    Address = field("Address")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterMemberFromAddressListRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterMemberFromAddressListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Envelope:
    boto3_raw_data: "type_defs.EnvelopeTypeDef" = dataclasses.field()

    Helo = field("Helo")
    From = field("From")
    To = field("To")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvelopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvelopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ExportDestinationConfiguration:
    boto3_raw_data: "type_defs.S3ExportDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    S3Location = field("S3Location")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3ExportDestinationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ExportDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportStatus:
    boto3_raw_data: "type_defs.ExportStatusTypeDef" = dataclasses.field()

    SubmissionTimestamp = field("SubmissionTimestamp")
    CompletionTimestamp = field("CompletionTimestamp")
    State = field("State")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAddonInstanceRequest:
    boto3_raw_data: "type_defs.GetAddonInstanceRequestTypeDef" = dataclasses.field()

    AddonInstanceId = field("AddonInstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAddonInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAddonInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAddonSubscriptionRequest:
    boto3_raw_data: "type_defs.GetAddonSubscriptionRequestTypeDef" = dataclasses.field()

    AddonSubscriptionId = field("AddonSubscriptionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAddonSubscriptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAddonSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAddressListImportJobRequest:
    boto3_raw_data: "type_defs.GetAddressListImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAddressListImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAddressListImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAddressListRequest:
    boto3_raw_data: "type_defs.GetAddressListRequestTypeDef" = dataclasses.field()

    AddressListId = field("AddressListId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAddressListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAddressListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveExportRequest:
    boto3_raw_data: "type_defs.GetArchiveExportRequestTypeDef" = dataclasses.field()

    ExportId = field("ExportId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArchiveExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveMessageContentRequest:
    boto3_raw_data: "type_defs.GetArchiveMessageContentRequestTypeDef" = (
        dataclasses.field()
    )

    ArchivedMessageId = field("ArchivedMessageId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetArchiveMessageContentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveMessageContentRequestTypeDef"]
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

    Text = field("Text")
    Html = field("Html")
    MessageMalformed = field("MessageMalformed")

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
class GetArchiveMessageRequest:
    boto3_raw_data: "type_defs.GetArchiveMessageRequestTypeDef" = dataclasses.field()

    ArchivedMessageId = field("ArchivedMessageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArchiveMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metadata:
    boto3_raw_data: "type_defs.MetadataTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    IngressPointId = field("IngressPointId")
    TrafficPolicyId = field("TrafficPolicyId")
    RuleSetId = field("RuleSetId")
    SenderHostname = field("SenderHostname")
    SenderIpAddress = field("SenderIpAddress")
    TlsCipherSuite = field("TlsCipherSuite")
    TlsProtocol = field("TlsProtocol")
    SendingMethod = field("SendingMethod")
    SourceIdentity = field("SourceIdentity")
    SendingPool = field("SendingPool")
    ConfigurationSet = field("ConfigurationSet")
    SourceArn = field("SourceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetadataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveRequest:
    boto3_raw_data: "type_defs.GetArchiveRequestTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetArchiveRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveSearchRequest:
    boto3_raw_data: "type_defs.GetArchiveSearchRequestTypeDef" = dataclasses.field()

    SearchId = field("SearchId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArchiveSearchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveSearchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchStatus:
    boto3_raw_data: "type_defs.SearchStatusTypeDef" = dataclasses.field()

    SubmissionTimestamp = field("SubmissionTimestamp")
    CompletionTimestamp = field("CompletionTimestamp")
    State = field("State")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveSearchResultsRequest:
    boto3_raw_data: "type_defs.GetArchiveSearchResultsRequestTypeDef" = (
        dataclasses.field()
    )

    SearchId = field("SearchId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetArchiveSearchResultsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveSearchResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIngressPointRequest:
    boto3_raw_data: "type_defs.GetIngressPointRequestTypeDef" = dataclasses.field()

    IngressPointId = field("IngressPointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIngressPointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIngressPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemberOfAddressListRequest:
    boto3_raw_data: "type_defs.GetMemberOfAddressListRequestTypeDef" = (
        dataclasses.field()
    )

    AddressListId = field("AddressListId")
    Address = field("Address")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMemberOfAddressListRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMemberOfAddressListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelayRequest:
    boto3_raw_data: "type_defs.GetRelayRequestTypeDef" = dataclasses.field()

    RelayId = field("RelayId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRelayRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRelayRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelayAuthenticationOutput:
    boto3_raw_data: "type_defs.RelayAuthenticationOutputTypeDef" = dataclasses.field()

    SecretArn = field("SecretArn")
    NoAuthentication = field("NoAuthentication")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelayAuthenticationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelayAuthenticationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuleSetRequest:
    boto3_raw_data: "type_defs.GetRuleSetRequestTypeDef" = dataclasses.field()

    RuleSetId = field("RuleSetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRuleSetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRuleSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrafficPolicyRequest:
    boto3_raw_data: "type_defs.GetTrafficPolicyRequestTypeDef" = dataclasses.field()

    TrafficPolicyId = field("TrafficPolicyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrafficPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrafficPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressAnalysis:
    boto3_raw_data: "type_defs.IngressAnalysisTypeDef" = dataclasses.field()

    Analyzer = field("Analyzer")
    ResultField = field("ResultField")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IngressAnalysisTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IngressAnalysisTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressIsInAddressListOutput:
    boto3_raw_data: "type_defs.IngressIsInAddressListOutputTypeDef" = (
        dataclasses.field()
    )

    Attribute = field("Attribute")
    AddressLists = field("AddressLists")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressIsInAddressListOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressIsInAddressListOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressIpToEvaluate:
    boto3_raw_data: "type_defs.IngressIpToEvaluateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressIpToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressIpToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressIpv6ToEvaluate:
    boto3_raw_data: "type_defs.IngressIpv6ToEvaluateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressIpv6ToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressIpv6ToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressIsInAddressList:
    boto3_raw_data: "type_defs.IngressIsInAddressListTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    AddressLists = field("AddressLists")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressIsInAddressListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressIsInAddressListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressPointPasswordConfiguration:
    boto3_raw_data: "type_defs.IngressPointPasswordConfigurationTypeDef" = (
        dataclasses.field()
    )

    SmtpPasswordVersion = field("SmtpPasswordVersion")
    PreviousSmtpPasswordVersion = field("PreviousSmtpPasswordVersion")
    PreviousSmtpPasswordExpiryTimestamp = field("PreviousSmtpPasswordExpiryTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IngressPointPasswordConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressPointPasswordConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressPoint:
    boto3_raw_data: "type_defs.IngressPointTypeDef" = dataclasses.field()

    IngressPointName = field("IngressPointName")
    IngressPointId = field("IngressPointId")
    Status = field("Status")
    Type = field("Type")
    ARecord = field("ARecord")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IngressPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IngressPointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressTlsProtocolToEvaluate:
    boto3_raw_data: "type_defs.IngressTlsProtocolToEvaluateTypeDef" = (
        dataclasses.field()
    )

    Attribute = field("Attribute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressTlsProtocolToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressTlsProtocolToEvaluateTypeDef"]
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
class ListAddonInstancesRequest:
    boto3_raw_data: "type_defs.ListAddonInstancesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAddonInstancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddonInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddonSubscriptionsRequest:
    boto3_raw_data: "type_defs.ListAddonSubscriptionsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAddonSubscriptionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddonSubscriptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddressListImportJobsRequest:
    boto3_raw_data: "type_defs.ListAddressListImportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    AddressListId = field("AddressListId")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAddressListImportJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddressListImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddressListsRequest:
    boto3_raw_data: "type_defs.ListAddressListsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAddressListsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddressListsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchiveExportsRequest:
    boto3_raw_data: "type_defs.ListArchiveExportsRequestTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchiveExportsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchiveExportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchiveSearchesRequest:
    boto3_raw_data: "type_defs.ListArchiveSearchesRequestTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchiveSearchesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchiveSearchesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchivesRequest:
    boto3_raw_data: "type_defs.ListArchivesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchivesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchivesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIngressPointsRequest:
    boto3_raw_data: "type_defs.ListIngressPointsRequestTypeDef" = dataclasses.field()

    PageSize = field("PageSize")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIngressPointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIngressPointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavedAddress:
    boto3_raw_data: "type_defs.SavedAddressTypeDef" = dataclasses.field()

    Address = field("Address")
    CreatedTimestamp = field("CreatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SavedAddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SavedAddressTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRelaysRequest:
    boto3_raw_data: "type_defs.ListRelaysRequestTypeDef" = dataclasses.field()

    PageSize = field("PageSize")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRelaysRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRelaysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Relay:
    boto3_raw_data: "type_defs.RelayTypeDef" = dataclasses.field()

    RelayId = field("RelayId")
    RelayName = field("RelayName")
    LastModifiedTimestamp = field("LastModifiedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelayTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelayTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleSetsRequest:
    boto3_raw_data: "type_defs.ListRuleSetsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleSet:
    boto3_raw_data: "type_defs.RuleSetTypeDef" = dataclasses.field()

    RuleSetId = field("RuleSetId")
    RuleSetName = field("RuleSetName")
    LastModificationDate = field("LastModificationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleSetTypeDef"]]
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
class ListTrafficPoliciesRequest:
    boto3_raw_data: "type_defs.ListTrafficPoliciesRequestTypeDef" = dataclasses.field()

    PageSize = field("PageSize")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrafficPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficPolicy:
    boto3_raw_data: "type_defs.TrafficPolicyTypeDef" = dataclasses.field()

    TrafficPolicyName = field("TrafficPolicyName")
    TrafficPolicyId = field("TrafficPolicyId")
    DefaultAction = field("DefaultAction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrafficPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrafficPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateNetworkConfiguration:
    boto3_raw_data: "type_defs.PrivateNetworkConfigurationTypeDef" = dataclasses.field()

    VpcEndpointId = field("VpcEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateNetworkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateNetworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicNetworkConfiguration:
    boto3_raw_data: "type_defs.PublicNetworkConfigurationTypeDef" = dataclasses.field()

    IpType = field("IpType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublicNetworkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublicNetworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterMemberToAddressListRequest:
    boto3_raw_data: "type_defs.RegisterMemberToAddressListRequestTypeDef" = (
        dataclasses.field()
    )

    AddressListId = field("AddressListId")
    Address = field("Address")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterMemberToAddressListRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterMemberToAddressListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelayAction:
    boto3_raw_data: "type_defs.RelayActionTypeDef" = dataclasses.field()

    Relay = field("Relay")
    ActionFailurePolicy = field("ActionFailurePolicy")
    MailFrom = field("MailFrom")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelayActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelayActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelayAuthentication:
    boto3_raw_data: "type_defs.RelayAuthenticationTypeDef" = dataclasses.field()

    SecretArn = field("SecretArn")
    NoAuthentication = field("NoAuthentication")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelayAuthenticationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelayAuthenticationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplaceRecipientActionOutput:
    boto3_raw_data: "type_defs.ReplaceRecipientActionOutputTypeDef" = (
        dataclasses.field()
    )

    ReplaceWith = field("ReplaceWith")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplaceRecipientActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplaceRecipientActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplaceRecipientAction:
    boto3_raw_data: "type_defs.ReplaceRecipientActionTypeDef" = dataclasses.field()

    ReplaceWith = field("ReplaceWith")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplaceRecipientActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplaceRecipientActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Action:
    boto3_raw_data: "type_defs.S3ActionTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    S3Bucket = field("S3Bucket")
    ActionFailurePolicy = field("ActionFailurePolicy")
    S3Prefix = field("S3Prefix")
    S3SseKmsKeyId = field("S3SseKmsKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendAction:
    boto3_raw_data: "type_defs.SendActionTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    ActionFailurePolicy = field("ActionFailurePolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SendActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnsAction:
    boto3_raw_data: "type_defs.SnsActionTypeDef" = dataclasses.field()

    TopicArn = field("TopicArn")
    RoleArn = field("RoleArn")
    ActionFailurePolicy = field("ActionFailurePolicy")
    Encoding = field("Encoding")
    PayloadType = field("PayloadType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnsActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnsActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleIsInAddressListOutput:
    boto3_raw_data: "type_defs.RuleIsInAddressListOutputTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    AddressLists = field("AddressLists")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleIsInAddressListOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleIsInAddressListOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleDmarcExpressionOutput:
    boto3_raw_data: "type_defs.RuleDmarcExpressionOutputTypeDef" = dataclasses.field()

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleDmarcExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleDmarcExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleDmarcExpression:
    boto3_raw_data: "type_defs.RuleDmarcExpressionTypeDef" = dataclasses.field()

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleDmarcExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleDmarcExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleIpToEvaluate:
    boto3_raw_data: "type_defs.RuleIpToEvaluateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleIpToEvaluateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleIpToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleIsInAddressList:
    boto3_raw_data: "type_defs.RuleIsInAddressListTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    AddressLists = field("AddressLists")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleIsInAddressListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleIsInAddressListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleNumberToEvaluate:
    boto3_raw_data: "type_defs.RuleNumberToEvaluateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleNumberToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleNumberToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAddressListImportJobRequest:
    boto3_raw_data: "type_defs.StartAddressListImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartAddressListImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAddressListImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopAddressListImportJobRequest:
    boto3_raw_data: "type_defs.StopAddressListImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopAddressListImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopAddressListImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopArchiveExportRequest:
    boto3_raw_data: "type_defs.StopArchiveExportRequestTypeDef" = dataclasses.field()

    ExportId = field("ExportId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopArchiveExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopArchiveExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopArchiveSearchRequest:
    boto3_raw_data: "type_defs.StopArchiveSearchRequestTypeDef" = dataclasses.field()

    SearchId = field("SearchId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopArchiveSearchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopArchiveSearchRequestTypeDef"]
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
class ListMembersOfAddressListRequest:
    boto3_raw_data: "type_defs.ListMembersOfAddressListRequestTypeDef" = (
        dataclasses.field()
    )

    AddressListId = field("AddressListId")

    @cached_property
    def Filter(self):  # pragma: no cover
        return AddressFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMembersOfAddressListRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersOfAddressListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleStringToEvaluate:
    boto3_raw_data: "type_defs.RuleStringToEvaluateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    MimeHeaderAttribute = field("MimeHeaderAttribute")

    @cached_property
    def Analysis(self):  # pragma: no cover
        return Analysis.make_one(self.boto3_raw_data["Analysis"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleStringToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleStringToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleVerdictToEvaluate:
    boto3_raw_data: "type_defs.RuleVerdictToEvaluateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @cached_property
    def Analysis(self):  # pragma: no cover
        return Analysis.make_one(self.boto3_raw_data["Analysis"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleVerdictToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleVerdictToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveBooleanExpression:
    boto3_raw_data: "type_defs.ArchiveBooleanExpressionTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return ArchiveBooleanToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveBooleanExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveBooleanExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateArchiveRequest:
    boto3_raw_data: "type_defs.UpdateArchiveRequestTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")
    ArchiveName = field("ArchiveName")

    @cached_property
    def Retention(self):  # pragma: no cover
        return ArchiveRetention.make_one(self.boto3_raw_data["Retention"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateArchiveRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateArchiveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveStringExpressionOutput:
    boto3_raw_data: "type_defs.ArchiveStringExpressionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return ArchiveStringToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ArchiveStringExpressionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveStringExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveStringExpression:
    boto3_raw_data: "type_defs.ArchiveStringExpressionTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return ArchiveStringToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveStringExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveStringExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAddonInstanceRequest:
    boto3_raw_data: "type_defs.CreateAddonInstanceRequestTypeDef" = dataclasses.field()

    AddonSubscriptionId = field("AddonSubscriptionId")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAddonInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAddonInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAddonSubscriptionRequest:
    boto3_raw_data: "type_defs.CreateAddonSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    AddonName = field("AddonName")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAddonSubscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAddonSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAddressListRequest:
    boto3_raw_data: "type_defs.CreateAddressListRequestTypeDef" = dataclasses.field()

    AddressListName = field("AddressListName")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAddressListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAddressListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateArchiveRequest:
    boto3_raw_data: "type_defs.CreateArchiveRequestTypeDef" = dataclasses.field()

    ArchiveName = field("ArchiveName")
    ClientToken = field("ClientToken")

    @cached_property
    def Retention(self):  # pragma: no cover
        return ArchiveRetention.make_one(self.boto3_raw_data["Retention"])

    KmsKeyArn = field("KmsKeyArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateArchiveRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateArchiveRequestTypeDef"]
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
class CreateAddonInstanceResponse:
    boto3_raw_data: "type_defs.CreateAddonInstanceResponseTypeDef" = dataclasses.field()

    AddonInstanceId = field("AddonInstanceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAddonInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAddonInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAddonSubscriptionResponse:
    boto3_raw_data: "type_defs.CreateAddonSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    AddonSubscriptionId = field("AddonSubscriptionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAddonSubscriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAddonSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAddressListImportJobResponse:
    boto3_raw_data: "type_defs.CreateAddressListImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    PreSignedUrl = field("PreSignedUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAddressListImportJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAddressListImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAddressListResponse:
    boto3_raw_data: "type_defs.CreateAddressListResponseTypeDef" = dataclasses.field()

    AddressListId = field("AddressListId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAddressListResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAddressListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateArchiveResponse:
    boto3_raw_data: "type_defs.CreateArchiveResponseTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateArchiveResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateArchiveResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIngressPointResponse:
    boto3_raw_data: "type_defs.CreateIngressPointResponseTypeDef" = dataclasses.field()

    IngressPointId = field("IngressPointId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIngressPointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIngressPointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRelayResponse:
    boto3_raw_data: "type_defs.CreateRelayResponseTypeDef" = dataclasses.field()

    RelayId = field("RelayId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRelayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRelayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleSetResponse:
    boto3_raw_data: "type_defs.CreateRuleSetResponseTypeDef" = dataclasses.field()

    RuleSetId = field("RuleSetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRuleSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrafficPolicyResponse:
    boto3_raw_data: "type_defs.CreateTrafficPolicyResponseTypeDef" = dataclasses.field()

    TrafficPolicyId = field("TrafficPolicyId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrafficPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrafficPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAddonInstanceResponse:
    boto3_raw_data: "type_defs.GetAddonInstanceResponseTypeDef" = dataclasses.field()

    AddonSubscriptionId = field("AddonSubscriptionId")
    AddonName = field("AddonName")
    AddonInstanceArn = field("AddonInstanceArn")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAddonInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAddonInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAddonSubscriptionResponse:
    boto3_raw_data: "type_defs.GetAddonSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    AddonName = field("AddonName")
    AddonSubscriptionArn = field("AddonSubscriptionArn")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAddonSubscriptionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAddonSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAddressListResponse:
    boto3_raw_data: "type_defs.GetAddressListResponseTypeDef" = dataclasses.field()

    AddressListId = field("AddressListId")
    AddressListArn = field("AddressListArn")
    AddressListName = field("AddressListName")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAddressListResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAddressListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveResponse:
    boto3_raw_data: "type_defs.GetArchiveResponseTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")
    ArchiveName = field("ArchiveName")
    ArchiveArn = field("ArchiveArn")
    ArchiveState = field("ArchiveState")

    @cached_property
    def Retention(self):  # pragma: no cover
        return ArchiveRetention.make_one(self.boto3_raw_data["Retention"])

    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    KmsKeyArn = field("KmsKeyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArchiveResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemberOfAddressListResponse:
    boto3_raw_data: "type_defs.GetMemberOfAddressListResponseTypeDef" = (
        dataclasses.field()
    )

    Address = field("Address")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMemberOfAddressListResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMemberOfAddressListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddonInstancesResponse:
    boto3_raw_data: "type_defs.ListAddonInstancesResponseTypeDef" = dataclasses.field()

    @cached_property
    def AddonInstances(self):  # pragma: no cover
        return AddonInstance.make_many(self.boto3_raw_data["AddonInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAddonInstancesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddonInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddonSubscriptionsResponse:
    boto3_raw_data: "type_defs.ListAddonSubscriptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AddonSubscriptions(self):  # pragma: no cover
        return AddonSubscription.make_many(self.boto3_raw_data["AddonSubscriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAddonSubscriptionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddonSubscriptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddressListsResponse:
    boto3_raw_data: "type_defs.ListAddressListsResponseTypeDef" = dataclasses.field()

    @cached_property
    def AddressLists(self):  # pragma: no cover
        return AddressList.make_many(self.boto3_raw_data["AddressLists"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAddressListsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddressListsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchivesResponse:
    boto3_raw_data: "type_defs.ListArchivesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Archives(self):  # pragma: no cover
        return Archive.make_many(self.boto3_raw_data["Archives"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchivesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchivesResponseTypeDef"]
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
class StartArchiveExportResponse:
    boto3_raw_data: "type_defs.StartArchiveExportResponseTypeDef" = dataclasses.field()

    ExportId = field("ExportId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartArchiveExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartArchiveExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartArchiveSearchResponse:
    boto3_raw_data: "type_defs.StartArchiveSearchResponseTypeDef" = dataclasses.field()

    SearchId = field("SearchId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartArchiveSearchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartArchiveSearchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAddressListImportJobRequest:
    boto3_raw_data: "type_defs.CreateAddressListImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    AddressListId = field("AddressListId")
    Name = field("Name")

    @cached_property
    def ImportDataFormat(self):  # pragma: no cover
        return ImportDataFormat.make_one(self.boto3_raw_data["ImportDataFormat"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAddressListImportJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAddressListImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAddressListImportJobResponse:
    boto3_raw_data: "type_defs.GetAddressListImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    Name = field("Name")
    Status = field("Status")
    PreSignedUrl = field("PreSignedUrl")
    ImportedItemsCount = field("ImportedItemsCount")
    FailedItemsCount = field("FailedItemsCount")

    @cached_property
    def ImportDataFormat(self):  # pragma: no cover
        return ImportDataFormat.make_one(self.boto3_raw_data["ImportDataFormat"])

    AddressListId = field("AddressListId")
    CreatedTimestamp = field("CreatedTimestamp")
    StartTimestamp = field("StartTimestamp")
    CompletedTimestamp = field("CompletedTimestamp")
    Error = field("Error")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAddressListImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAddressListImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportJob:
    boto3_raw_data: "type_defs.ImportJobTypeDef" = dataclasses.field()

    JobId = field("JobId")
    Name = field("Name")
    Status = field("Status")
    PreSignedUrl = field("PreSignedUrl")

    @cached_property
    def ImportDataFormat(self):  # pragma: no cover
        return ImportDataFormat.make_one(self.boto3_raw_data["ImportDataFormat"])

    AddressListId = field("AddressListId")
    CreatedTimestamp = field("CreatedTimestamp")
    ImportedItemsCount = field("ImportedItemsCount")
    FailedItemsCount = field("FailedItemsCount")
    StartTimestamp = field("StartTimestamp")
    CompletedTimestamp = field("CompletedTimestamp")
    Error = field("Error")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportJobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIngressPointRequest:
    boto3_raw_data: "type_defs.UpdateIngressPointRequestTypeDef" = dataclasses.field()

    IngressPointId = field("IngressPointId")
    IngressPointName = field("IngressPointName")
    StatusToUpdate = field("StatusToUpdate")
    RuleSetId = field("RuleSetId")
    TrafficPolicyId = field("TrafficPolicyId")

    @cached_property
    def IngressPointConfiguration(self):  # pragma: no cover
        return IngressPointConfiguration.make_one(
            self.boto3_raw_data["IngressPointConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIngressPointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIngressPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Row:
    boto3_raw_data: "type_defs.RowTypeDef" = dataclasses.field()

    ArchivedMessageId = field("ArchivedMessageId")
    ReceivedTimestamp = field("ReceivedTimestamp")
    Date = field("Date")
    To = field("To")
    From = field("From")
    Cc = field("Cc")
    Subject = field("Subject")
    MessageId = field("MessageId")
    HasAttachments = field("HasAttachments")
    ReceivedHeaders = field("ReceivedHeaders")
    InReplyTo = field("InReplyTo")
    XMailer = field("XMailer")
    XOriginalMailer = field("XOriginalMailer")
    XPriority = field("XPriority")
    IngressPointId = field("IngressPointId")
    SenderHostname = field("SenderHostname")
    SenderIpAddress = field("SenderIpAddress")

    @cached_property
    def Envelope(self):  # pragma: no cover
        return Envelope.make_one(self.boto3_raw_data["Envelope"])

    SourceArn = field("SourceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportDestinationConfiguration:
    boto3_raw_data: "type_defs.ExportDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3(self):  # pragma: no cover
        return S3ExportDestinationConfiguration.make_one(self.boto3_raw_data["S3"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportDestinationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSummary:
    boto3_raw_data: "type_defs.ExportSummaryTypeDef" = dataclasses.field()

    ExportId = field("ExportId")

    @cached_property
    def Status(self):  # pragma: no cover
        return ExportStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveMessageContentResponse:
    boto3_raw_data: "type_defs.GetArchiveMessageContentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Body(self):  # pragma: no cover
        return MessageBody.make_one(self.boto3_raw_data["Body"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetArchiveMessageContentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveMessageContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveMessageResponse:
    boto3_raw_data: "type_defs.GetArchiveMessageResponseTypeDef" = dataclasses.field()

    MessageDownloadLink = field("MessageDownloadLink")

    @cached_property
    def Metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["Metadata"])

    @cached_property
    def Envelope(self):  # pragma: no cover
        return Envelope.make_one(self.boto3_raw_data["Envelope"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArchiveMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSummary:
    boto3_raw_data: "type_defs.SearchSummaryTypeDef" = dataclasses.field()

    SearchId = field("SearchId")

    @cached_property
    def Status(self):  # pragma: no cover
        return SearchStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelayResponse:
    boto3_raw_data: "type_defs.GetRelayResponseTypeDef" = dataclasses.field()

    RelayId = field("RelayId")
    RelayArn = field("RelayArn")
    RelayName = field("RelayName")
    ServerName = field("ServerName")
    ServerPort = field("ServerPort")

    @cached_property
    def Authentication(self):  # pragma: no cover
        return RelayAuthenticationOutput.make_one(self.boto3_raw_data["Authentication"])

    CreatedTimestamp = field("CreatedTimestamp")
    LastModifiedTimestamp = field("LastModifiedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRelayResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressStringToEvaluate:
    boto3_raw_data: "type_defs.IngressStringToEvaluateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @cached_property
    def Analysis(self):  # pragma: no cover
        return IngressAnalysis.make_one(self.boto3_raw_data["Analysis"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressStringToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressStringToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressBooleanToEvaluateOutput:
    boto3_raw_data: "type_defs.IngressBooleanToEvaluateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Analysis(self):  # pragma: no cover
        return IngressAnalysis.make_one(self.boto3_raw_data["Analysis"])

    @cached_property
    def IsInAddressList(self):  # pragma: no cover
        return IngressIsInAddressListOutput.make_one(
            self.boto3_raw_data["IsInAddressList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IngressBooleanToEvaluateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressBooleanToEvaluateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressIpv4ExpressionOutput:
    boto3_raw_data: "type_defs.IngressIpv4ExpressionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return IngressIpToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressIpv4ExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressIpv4ExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressIpv4Expression:
    boto3_raw_data: "type_defs.IngressIpv4ExpressionTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return IngressIpToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressIpv4ExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressIpv4ExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressIpv6ExpressionOutput:
    boto3_raw_data: "type_defs.IngressIpv6ExpressionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return IngressIpv6ToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressIpv6ExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressIpv6ExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressIpv6Expression:
    boto3_raw_data: "type_defs.IngressIpv6ExpressionTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return IngressIpv6ToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressIpv6ExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressIpv6ExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressPointAuthConfiguration:
    boto3_raw_data: "type_defs.IngressPointAuthConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IngressPointPasswordConfiguration(self):  # pragma: no cover
        return IngressPointPasswordConfiguration.make_one(
            self.boto3_raw_data["IngressPointPasswordConfiguration"]
        )

    SecretArn = field("SecretArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IngressPointAuthConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressPointAuthConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIngressPointsResponse:
    boto3_raw_data: "type_defs.ListIngressPointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def IngressPoints(self):  # pragma: no cover
        return IngressPoint.make_many(self.boto3_raw_data["IngressPoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIngressPointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIngressPointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressTlsProtocolExpression:
    boto3_raw_data: "type_defs.IngressTlsProtocolExpressionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return IngressTlsProtocolToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressTlsProtocolExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressTlsProtocolExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddonInstancesRequestPaginate:
    boto3_raw_data: "type_defs.ListAddonInstancesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAddonInstancesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddonInstancesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddonSubscriptionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAddonSubscriptionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAddonSubscriptionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddonSubscriptionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddressListImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListAddressListImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AddressListId = field("AddressListId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAddressListImportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddressListImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddressListsRequestPaginate:
    boto3_raw_data: "type_defs.ListAddressListsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAddressListsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddressListsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchiveExportsRequestPaginate:
    boto3_raw_data: "type_defs.ListArchiveExportsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ArchiveId = field("ArchiveId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListArchiveExportsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchiveExportsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchiveSearchesRequestPaginate:
    boto3_raw_data: "type_defs.ListArchiveSearchesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ArchiveId = field("ArchiveId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListArchiveSearchesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchiveSearchesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchivesRequestPaginate:
    boto3_raw_data: "type_defs.ListArchivesRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchivesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchivesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIngressPointsRequestPaginate:
    boto3_raw_data: "type_defs.ListIngressPointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIngressPointsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIngressPointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersOfAddressListRequestPaginate:
    boto3_raw_data: "type_defs.ListMembersOfAddressListRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AddressListId = field("AddressListId")

    @cached_property
    def Filter(self):  # pragma: no cover
        return AddressFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMembersOfAddressListRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersOfAddressListRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRelaysRequestPaginate:
    boto3_raw_data: "type_defs.ListRelaysRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRelaysRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRelaysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListRuleSetsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleSetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListTrafficPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersOfAddressListResponse:
    boto3_raw_data: "type_defs.ListMembersOfAddressListResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Addresses(self):  # pragma: no cover
        return SavedAddress.make_many(self.boto3_raw_data["Addresses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMembersOfAddressListResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersOfAddressListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRelaysResponse:
    boto3_raw_data: "type_defs.ListRelaysResponseTypeDef" = dataclasses.field()

    @cached_property
    def Relays(self):  # pragma: no cover
        return Relay.make_many(self.boto3_raw_data["Relays"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRelaysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRelaysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleSetsResponse:
    boto3_raw_data: "type_defs.ListRuleSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def RuleSets(self):  # pragma: no cover
        return RuleSet.make_many(self.boto3_raw_data["RuleSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPoliciesResponse:
    boto3_raw_data: "type_defs.ListTrafficPoliciesResponseTypeDef" = dataclasses.field()

    @cached_property
    def TrafficPolicies(self):  # pragma: no cover
        return TrafficPolicy.make_many(self.boto3_raw_data["TrafficPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrafficPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConfiguration:
    boto3_raw_data: "type_defs.NetworkConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def PublicNetworkConfiguration(self):  # pragma: no cover
        return PublicNetworkConfiguration.make_one(
            self.boto3_raw_data["PublicNetworkConfiguration"]
        )

    @cached_property
    def PrivateNetworkConfiguration(self):  # pragma: no cover
        return PrivateNetworkConfiguration.make_one(
            self.boto3_raw_data["PrivateNetworkConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleActionOutput:
    boto3_raw_data: "type_defs.RuleActionOutputTypeDef" = dataclasses.field()

    Drop = field("Drop")

    @cached_property
    def Relay(self):  # pragma: no cover
        return RelayAction.make_one(self.boto3_raw_data["Relay"])

    @cached_property
    def Archive(self):  # pragma: no cover
        return ArchiveAction.make_one(self.boto3_raw_data["Archive"])

    @cached_property
    def WriteToS3(self):  # pragma: no cover
        return S3Action.make_one(self.boto3_raw_data["WriteToS3"])

    @cached_property
    def Send(self):  # pragma: no cover
        return SendAction.make_one(self.boto3_raw_data["Send"])

    @cached_property
    def AddHeader(self):  # pragma: no cover
        return AddHeaderAction.make_one(self.boto3_raw_data["AddHeader"])

    @cached_property
    def ReplaceRecipient(self):  # pragma: no cover
        return ReplaceRecipientActionOutput.make_one(
            self.boto3_raw_data["ReplaceRecipient"]
        )

    @cached_property
    def DeliverToMailbox(self):  # pragma: no cover
        return DeliverToMailboxAction.make_one(self.boto3_raw_data["DeliverToMailbox"])

    @cached_property
    def DeliverToQBusiness(self):  # pragma: no cover
        return DeliverToQBusinessAction.make_one(
            self.boto3_raw_data["DeliverToQBusiness"]
        )

    @cached_property
    def PublishToSns(self):  # pragma: no cover
        return SnsAction.make_one(self.boto3_raw_data["PublishToSns"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleBooleanToEvaluateOutput:
    boto3_raw_data: "type_defs.RuleBooleanToEvaluateOutputTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @cached_property
    def Analysis(self):  # pragma: no cover
        return Analysis.make_one(self.boto3_raw_data["Analysis"])

    @cached_property
    def IsInAddressList(self):  # pragma: no cover
        return RuleIsInAddressListOutput.make_one(
            self.boto3_raw_data["IsInAddressList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleBooleanToEvaluateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleBooleanToEvaluateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleIpExpressionOutput:
    boto3_raw_data: "type_defs.RuleIpExpressionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return RuleIpToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleIpExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleIpExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleIpExpression:
    boto3_raw_data: "type_defs.RuleIpExpressionTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return RuleIpToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleIpExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleIpExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleNumberExpression:
    boto3_raw_data: "type_defs.RuleNumberExpressionTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return RuleNumberToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleNumberExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleNumberExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleStringExpressionOutput:
    boto3_raw_data: "type_defs.RuleStringExpressionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return RuleStringToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleStringExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleStringExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleStringExpression:
    boto3_raw_data: "type_defs.RuleStringExpressionTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return RuleStringToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleStringExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleStringExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleVerdictExpressionOutput:
    boto3_raw_data: "type_defs.RuleVerdictExpressionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return RuleVerdictToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleVerdictExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleVerdictExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleVerdictExpression:
    boto3_raw_data: "type_defs.RuleVerdictExpressionTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return RuleVerdictToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleVerdictExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleVerdictExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveFilterConditionOutput:
    boto3_raw_data: "type_defs.ArchiveFilterConditionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StringExpression(self):  # pragma: no cover
        return ArchiveStringExpressionOutput.make_one(
            self.boto3_raw_data["StringExpression"]
        )

    @cached_property
    def BooleanExpression(self):  # pragma: no cover
        return ArchiveBooleanExpression.make_one(
            self.boto3_raw_data["BooleanExpression"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveFilterConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveFilterConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveFilterCondition:
    boto3_raw_data: "type_defs.ArchiveFilterConditionTypeDef" = dataclasses.field()

    @cached_property
    def StringExpression(self):  # pragma: no cover
        return ArchiveStringExpression.make_one(self.boto3_raw_data["StringExpression"])

    @cached_property
    def BooleanExpression(self):  # pragma: no cover
        return ArchiveBooleanExpression.make_one(
            self.boto3_raw_data["BooleanExpression"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveFilterConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveFilterConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddressListImportJobsResponse:
    boto3_raw_data: "type_defs.ListAddressListImportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ImportJobs(self):  # pragma: no cover
        return ImportJob.make_many(self.boto3_raw_data["ImportJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAddressListImportJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddressListImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveSearchResultsResponse:
    boto3_raw_data: "type_defs.GetArchiveSearchResultsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Rows(self):  # pragma: no cover
        return Row.make_many(self.boto3_raw_data["Rows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetArchiveSearchResultsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveSearchResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchiveExportsResponse:
    boto3_raw_data: "type_defs.ListArchiveExportsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Exports(self):  # pragma: no cover
        return ExportSummary.make_many(self.boto3_raw_data["Exports"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchiveExportsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchiveExportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchiveSearchesResponse:
    boto3_raw_data: "type_defs.ListArchiveSearchesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Searches(self):  # pragma: no cover
        return SearchSummary.make_many(self.boto3_raw_data["Searches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchiveSearchesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchiveSearchesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressStringExpressionOutput:
    boto3_raw_data: "type_defs.IngressStringExpressionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return IngressStringToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IngressStringExpressionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressStringExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressStringExpression:
    boto3_raw_data: "type_defs.IngressStringExpressionTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return IngressStringToEvaluate.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressStringExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressStringExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressBooleanExpressionOutput:
    boto3_raw_data: "type_defs.IngressBooleanExpressionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return IngressBooleanToEvaluateOutput.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IngressBooleanExpressionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressBooleanExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressBooleanToEvaluate:
    boto3_raw_data: "type_defs.IngressBooleanToEvaluateTypeDef" = dataclasses.field()

    @cached_property
    def Analysis(self):  # pragma: no cover
        return IngressAnalysis.make_one(self.boto3_raw_data["Analysis"])

    IsInAddressList = field("IsInAddressList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressBooleanToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressBooleanToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIngressPointRequest:
    boto3_raw_data: "type_defs.CreateIngressPointRequestTypeDef" = dataclasses.field()

    IngressPointName = field("IngressPointName")
    Type = field("Type")
    RuleSetId = field("RuleSetId")
    TrafficPolicyId = field("TrafficPolicyId")
    ClientToken = field("ClientToken")

    @cached_property
    def IngressPointConfiguration(self):  # pragma: no cover
        return IngressPointConfiguration.make_one(
            self.boto3_raw_data["IngressPointConfiguration"]
        )

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIngressPointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIngressPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIngressPointResponse:
    boto3_raw_data: "type_defs.GetIngressPointResponseTypeDef" = dataclasses.field()

    IngressPointId = field("IngressPointId")
    IngressPointName = field("IngressPointName")
    IngressPointArn = field("IngressPointArn")
    Status = field("Status")
    Type = field("Type")
    ARecord = field("ARecord")
    RuleSetId = field("RuleSetId")
    TrafficPolicyId = field("TrafficPolicyId")

    @cached_property
    def IngressPointAuthConfiguration(self):  # pragma: no cover
        return IngressPointAuthConfiguration.make_one(
            self.boto3_raw_data["IngressPointAuthConfiguration"]
        )

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIngressPointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIngressPointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRelayRequest:
    boto3_raw_data: "type_defs.CreateRelayRequestTypeDef" = dataclasses.field()

    RelayName = field("RelayName")
    ServerName = field("ServerName")
    ServerPort = field("ServerPort")
    Authentication = field("Authentication")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRelayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRelayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRelayRequest:
    boto3_raw_data: "type_defs.UpdateRelayRequestTypeDef" = dataclasses.field()

    RelayId = field("RelayId")
    RelayName = field("RelayName")
    ServerName = field("ServerName")
    ServerPort = field("ServerPort")
    Authentication = field("Authentication")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRelayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRelayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleAction:
    boto3_raw_data: "type_defs.RuleActionTypeDef" = dataclasses.field()

    Drop = field("Drop")

    @cached_property
    def Relay(self):  # pragma: no cover
        return RelayAction.make_one(self.boto3_raw_data["Relay"])

    @cached_property
    def Archive(self):  # pragma: no cover
        return ArchiveAction.make_one(self.boto3_raw_data["Archive"])

    @cached_property
    def WriteToS3(self):  # pragma: no cover
        return S3Action.make_one(self.boto3_raw_data["WriteToS3"])

    @cached_property
    def Send(self):  # pragma: no cover
        return SendAction.make_one(self.boto3_raw_data["Send"])

    @cached_property
    def AddHeader(self):  # pragma: no cover
        return AddHeaderAction.make_one(self.boto3_raw_data["AddHeader"])

    ReplaceRecipient = field("ReplaceRecipient")

    @cached_property
    def DeliverToMailbox(self):  # pragma: no cover
        return DeliverToMailboxAction.make_one(self.boto3_raw_data["DeliverToMailbox"])

    @cached_property
    def DeliverToQBusiness(self):  # pragma: no cover
        return DeliverToQBusinessAction.make_one(
            self.boto3_raw_data["DeliverToQBusiness"]
        )

    @cached_property
    def PublishToSns(self):  # pragma: no cover
        return SnsAction.make_one(self.boto3_raw_data["PublishToSns"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleBooleanExpressionOutput:
    boto3_raw_data: "type_defs.RuleBooleanExpressionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Evaluate(self):  # pragma: no cover
        return RuleBooleanToEvaluateOutput.make_one(self.boto3_raw_data["Evaluate"])

    Operator = field("Operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleBooleanExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleBooleanExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleBooleanToEvaluate:
    boto3_raw_data: "type_defs.RuleBooleanToEvaluateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @cached_property
    def Analysis(self):  # pragma: no cover
        return Analysis.make_one(self.boto3_raw_data["Analysis"])

    IsInAddressList = field("IsInAddressList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleBooleanToEvaluateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleBooleanToEvaluateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveFiltersOutput:
    boto3_raw_data: "type_defs.ArchiveFiltersOutputTypeDef" = dataclasses.field()

    @cached_property
    def Include(self):  # pragma: no cover
        return ArchiveFilterConditionOutput.make_many(self.boto3_raw_data["Include"])

    @cached_property
    def Unless(self):  # pragma: no cover
        return ArchiveFilterConditionOutput.make_many(self.boto3_raw_data["Unless"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveFiltersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveFiltersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveFilters:
    boto3_raw_data: "type_defs.ArchiveFiltersTypeDef" = dataclasses.field()

    @cached_property
    def Include(self):  # pragma: no cover
        return ArchiveFilterCondition.make_many(self.boto3_raw_data["Include"])

    @cached_property
    def Unless(self):  # pragma: no cover
        return ArchiveFilterCondition.make_many(self.boto3_raw_data["Unless"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArchiveFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArchiveFiltersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyConditionOutput:
    boto3_raw_data: "type_defs.PolicyConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def StringExpression(self):  # pragma: no cover
        return IngressStringExpressionOutput.make_one(
            self.boto3_raw_data["StringExpression"]
        )

    @cached_property
    def IpExpression(self):  # pragma: no cover
        return IngressIpv4ExpressionOutput.make_one(self.boto3_raw_data["IpExpression"])

    @cached_property
    def Ipv6Expression(self):  # pragma: no cover
        return IngressIpv6ExpressionOutput.make_one(
            self.boto3_raw_data["Ipv6Expression"]
        )

    @cached_property
    def TlsExpression(self):  # pragma: no cover
        return IngressTlsProtocolExpression.make_one(
            self.boto3_raw_data["TlsExpression"]
        )

    @cached_property
    def BooleanExpression(self):  # pragma: no cover
        return IngressBooleanExpressionOutput.make_one(
            self.boto3_raw_data["BooleanExpression"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleConditionOutput:
    boto3_raw_data: "type_defs.RuleConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def BooleanExpression(self):  # pragma: no cover
        return RuleBooleanExpressionOutput.make_one(
            self.boto3_raw_data["BooleanExpression"]
        )

    @cached_property
    def StringExpression(self):  # pragma: no cover
        return RuleStringExpressionOutput.make_one(
            self.boto3_raw_data["StringExpression"]
        )

    @cached_property
    def NumberExpression(self):  # pragma: no cover
        return RuleNumberExpression.make_one(self.boto3_raw_data["NumberExpression"])

    @cached_property
    def IpExpression(self):  # pragma: no cover
        return RuleIpExpressionOutput.make_one(self.boto3_raw_data["IpExpression"])

    @cached_property
    def VerdictExpression(self):  # pragma: no cover
        return RuleVerdictExpressionOutput.make_one(
            self.boto3_raw_data["VerdictExpression"]
        )

    @cached_property
    def DmarcExpression(self):  # pragma: no cover
        return RuleDmarcExpressionOutput.make_one(
            self.boto3_raw_data["DmarcExpression"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveExportResponse:
    boto3_raw_data: "type_defs.GetArchiveExportResponseTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ArchiveFiltersOutput.make_one(self.boto3_raw_data["Filters"])

    FromTimestamp = field("FromTimestamp")
    ToTimestamp = field("ToTimestamp")
    MaxResults = field("MaxResults")

    @cached_property
    def ExportDestinationConfiguration(self):  # pragma: no cover
        return ExportDestinationConfiguration.make_one(
            self.boto3_raw_data["ExportDestinationConfiguration"]
        )

    @cached_property
    def Status(self):  # pragma: no cover
        return ExportStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArchiveExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveSearchResponse:
    boto3_raw_data: "type_defs.GetArchiveSearchResponseTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ArchiveFiltersOutput.make_one(self.boto3_raw_data["Filters"])

    FromTimestamp = field("FromTimestamp")
    ToTimestamp = field("ToTimestamp")
    MaxResults = field("MaxResults")

    @cached_property
    def Status(self):  # pragma: no cover
        return SearchStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArchiveSearchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveSearchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyStatementOutput:
    boto3_raw_data: "type_defs.PolicyStatementOutputTypeDef" = dataclasses.field()

    @cached_property
    def Conditions(self):  # pragma: no cover
        return PolicyConditionOutput.make_many(self.boto3_raw_data["Conditions"])

    Action = field("Action")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressBooleanExpression:
    boto3_raw_data: "type_defs.IngressBooleanExpressionTypeDef" = dataclasses.field()

    Evaluate = field("Evaluate")
    Operator = field("Operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressBooleanExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressBooleanExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleOutput:
    boto3_raw_data: "type_defs.RuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def Actions(self):  # pragma: no cover
        return RuleActionOutput.make_many(self.boto3_raw_data["Actions"])

    Name = field("Name")

    @cached_property
    def Conditions(self):  # pragma: no cover
        return RuleConditionOutput.make_many(self.boto3_raw_data["Conditions"])

    @cached_property
    def Unless(self):  # pragma: no cover
        return RuleConditionOutput.make_many(self.boto3_raw_data["Unless"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleBooleanExpression:
    boto3_raw_data: "type_defs.RuleBooleanExpressionTypeDef" = dataclasses.field()

    Evaluate = field("Evaluate")
    Operator = field("Operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleBooleanExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleBooleanExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartArchiveExportRequest:
    boto3_raw_data: "type_defs.StartArchiveExportRequestTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")
    FromTimestamp = field("FromTimestamp")
    ToTimestamp = field("ToTimestamp")

    @cached_property
    def ExportDestinationConfiguration(self):  # pragma: no cover
        return ExportDestinationConfiguration.make_one(
            self.boto3_raw_data["ExportDestinationConfiguration"]
        )

    Filters = field("Filters")
    MaxResults = field("MaxResults")
    IncludeMetadata = field("IncludeMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartArchiveExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartArchiveExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartArchiveSearchRequest:
    boto3_raw_data: "type_defs.StartArchiveSearchRequestTypeDef" = dataclasses.field()

    ArchiveId = field("ArchiveId")
    FromTimestamp = field("FromTimestamp")
    ToTimestamp = field("ToTimestamp")
    MaxResults = field("MaxResults")
    Filters = field("Filters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartArchiveSearchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartArchiveSearchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrafficPolicyResponse:
    boto3_raw_data: "type_defs.GetTrafficPolicyResponseTypeDef" = dataclasses.field()

    TrafficPolicyName = field("TrafficPolicyName")
    TrafficPolicyId = field("TrafficPolicyId")
    TrafficPolicyArn = field("TrafficPolicyArn")

    @cached_property
    def PolicyStatements(self):  # pragma: no cover
        return PolicyStatementOutput.make_many(self.boto3_raw_data["PolicyStatements"])

    MaxMessageSizeBytes = field("MaxMessageSizeBytes")
    DefaultAction = field("DefaultAction")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrafficPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrafficPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuleSetResponse:
    boto3_raw_data: "type_defs.GetRuleSetResponseTypeDef" = dataclasses.field()

    RuleSetId = field("RuleSetId")
    RuleSetArn = field("RuleSetArn")
    RuleSetName = field("RuleSetName")
    CreatedDate = field("CreatedDate")
    LastModificationDate = field("LastModificationDate")

    @cached_property
    def Rules(self):  # pragma: no cover
        return RuleOutput.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRuleSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRuleSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyCondition:
    boto3_raw_data: "type_defs.PolicyConditionTypeDef" = dataclasses.field()

    StringExpression = field("StringExpression")
    IpExpression = field("IpExpression")
    Ipv6Expression = field("Ipv6Expression")

    @cached_property
    def TlsExpression(self):  # pragma: no cover
        return IngressTlsProtocolExpression.make_one(
            self.boto3_raw_data["TlsExpression"]
        )

    BooleanExpression = field("BooleanExpression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleCondition:
    boto3_raw_data: "type_defs.RuleConditionTypeDef" = dataclasses.field()

    BooleanExpression = field("BooleanExpression")
    StringExpression = field("StringExpression")

    @cached_property
    def NumberExpression(self):  # pragma: no cover
        return RuleNumberExpression.make_one(self.boto3_raw_data["NumberExpression"])

    IpExpression = field("IpExpression")
    VerdictExpression = field("VerdictExpression")
    DmarcExpression = field("DmarcExpression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyStatement:
    boto3_raw_data: "type_defs.PolicyStatementTypeDef" = dataclasses.field()

    Conditions = field("Conditions")
    Action = field("Action")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyStatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyStatementTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    Actions = field("Actions")
    Name = field("Name")
    Conditions = field("Conditions")
    Unless = field("Unless")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrafficPolicyRequest:
    boto3_raw_data: "type_defs.CreateTrafficPolicyRequestTypeDef" = dataclasses.field()

    TrafficPolicyName = field("TrafficPolicyName")
    PolicyStatements = field("PolicyStatements")
    DefaultAction = field("DefaultAction")
    ClientToken = field("ClientToken")
    MaxMessageSizeBytes = field("MaxMessageSizeBytes")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrafficPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrafficPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrafficPolicyRequest:
    boto3_raw_data: "type_defs.UpdateTrafficPolicyRequestTypeDef" = dataclasses.field()

    TrafficPolicyId = field("TrafficPolicyId")
    TrafficPolicyName = field("TrafficPolicyName")
    PolicyStatements = field("PolicyStatements")
    DefaultAction = field("DefaultAction")
    MaxMessageSizeBytes = field("MaxMessageSizeBytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTrafficPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrafficPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleSetRequest:
    boto3_raw_data: "type_defs.CreateRuleSetRequestTypeDef" = dataclasses.field()

    RuleSetName = field("RuleSetName")
    Rules = field("Rules")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRuleSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleSetRequest:
    boto3_raw_data: "type_defs.UpdateRuleSetRequestTypeDef" = dataclasses.field()

    RuleSetId = field("RuleSetId")
    RuleSetName = field("RuleSetName")
    Rules = field("Rules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
