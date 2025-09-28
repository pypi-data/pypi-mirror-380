# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sesv2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ReviewDetails:
    boto3_raw_data: "type_defs.ReviewDetailsTypeDef" = dataclasses.field()

    Status = field("Status")
    CaseId = field("CaseId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReviewDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReviewDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchivingOptions:
    boto3_raw_data: "type_defs.ArchivingOptionsTypeDef" = dataclasses.field()

    ArchiveArn = field("ArchiveArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArchivingOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchivingOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataError:
    boto3_raw_data: "type_defs.MetricDataErrorTypeDef" = dataclasses.field()

    Id = field("Id")
    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDataErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDataErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataResult:
    boto3_raw_data: "type_defs.MetricDataResultTypeDef" = dataclasses.field()

    Id = field("Id")
    Timestamps = field("Timestamps")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDataResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDataResultTypeDef"]
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
class Bounce:
    boto3_raw_data: "type_defs.BounceTypeDef" = dataclasses.field()

    BounceType = field("BounceType")
    BounceSubType = field("BounceSubType")
    DiagnosticCode = field("DiagnosticCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BounceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BounceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BulkEmailEntryResult:
    boto3_raw_data: "type_defs.BulkEmailEntryResultTypeDef" = dataclasses.field()

    Status = field("Status")
    Error = field("Error")
    MessageId = field("MessageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BulkEmailEntryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BulkEmailEntryResultTypeDef"]
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
class CancelExportJobRequest:
    boto3_raw_data: "type_defs.CancelExportJobRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelExportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelExportJobRequestTypeDef"]
        ],
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
class Complaint:
    boto3_raw_data: "type_defs.ComplaintTypeDef" = dataclasses.field()

    ComplaintSubType = field("ComplaintSubType")
    ComplaintFeedbackType = field("ComplaintFeedbackType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComplaintTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComplaintTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactListDestination:
    boto3_raw_data: "type_defs.ContactListDestinationTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")
    ContactListImportAction = field("ContactListImportAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactListDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactListDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactList:
    boto3_raw_data: "type_defs.ContactListTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactListTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicPreference:
    boto3_raw_data: "type_defs.TopicPreferenceTypeDef" = dataclasses.field()

    TopicName = field("TopicName")
    SubscriptionStatus = field("SubscriptionStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TopicPreferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TopicPreferenceTypeDef"]],
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
    MaxDeliverySeconds = field("MaxDeliverySeconds")

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
    HttpsPolicy = field("HttpsPolicy")

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
class Topic:
    boto3_raw_data: "type_defs.TopicTypeDef" = dataclasses.field()

    TopicName = field("TopicName")
    DisplayName = field("DisplayName")
    DefaultSubscriptionStatus = field("DefaultSubscriptionStatus")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TopicTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TopicTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomVerificationEmailTemplateRequest:
    boto3_raw_data: "type_defs.CreateCustomVerificationEmailTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    TemplateName = field("TemplateName")
    FromEmailAddress = field("FromEmailAddress")
    TemplateSubject = field("TemplateSubject")
    TemplateContent = field("TemplateContent")
    SuccessRedirectionURL = field("SuccessRedirectionURL")
    FailureRedirectionURL = field("FailureRedirectionURL")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomVerificationEmailTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomVerificationEmailTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEmailIdentityPolicyRequest:
    boto3_raw_data: "type_defs.CreateEmailIdentityPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    EmailIdentity = field("EmailIdentity")
    PolicyName = field("PolicyName")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEmailIdentityPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEmailIdentityPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DkimSigningAttributes:
    boto3_raw_data: "type_defs.DkimSigningAttributesTypeDef" = dataclasses.field()

    DomainSigningSelector = field("DomainSigningSelector")
    DomainSigningPrivateKey = field("DomainSigningPrivateKey")
    NextSigningKeyLength = field("NextSigningKeyLength")
    DomainSigningAttributesOrigin = field("DomainSigningAttributesOrigin")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DkimSigningAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DkimSigningAttributesTypeDef"]
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
    SigningAttributesOrigin = field("SigningAttributesOrigin")
    NextSigningKeyLength = field("NextSigningKeyLength")
    CurrentSigningKeyLength = field("CurrentSigningKeyLength")
    LastKeyGenerationTimestamp = field("LastKeyGenerationTimestamp")

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
class EmailTemplateContent:
    boto3_raw_data: "type_defs.EmailTemplateContentTypeDef" = dataclasses.field()

    Subject = field("Subject")
    Text = field("Text")
    Html = field("Html")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailTemplateContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailTemplateContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportDestination:
    boto3_raw_data: "type_defs.ExportDestinationTypeDef" = dataclasses.field()

    DataFormat = field("DataFormat")
    S3Url = field("S3Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportDataSource:
    boto3_raw_data: "type_defs.ImportDataSourceTypeDef" = dataclasses.field()

    S3Url = field("S3Url")
    DataFormat = field("DataFormat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportDataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTenantResourceAssociationRequest:
    boto3_raw_data: "type_defs.CreateTenantResourceAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    TenantName = field("TenantName")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTenantResourceAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTenantResourceAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomVerificationEmailTemplateMetadata:
    boto3_raw_data: "type_defs.CustomVerificationEmailTemplateMetadataTypeDef" = (
        dataclasses.field()
    )

    TemplateName = field("TemplateName")
    FromEmailAddress = field("FromEmailAddress")
    TemplateSubject = field("TemplateSubject")
    SuccessRedirectionURL = field("SuccessRedirectionURL")
    FailureRedirectionURL = field("FailureRedirectionURL")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomVerificationEmailTemplateMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomVerificationEmailTemplateMetadataTypeDef"]
        ],
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
class DashboardAttributes:
    boto3_raw_data: "type_defs.DashboardAttributesTypeDef" = dataclasses.field()

    EngagementMetrics = field("EngagementMetrics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashboardAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashboardAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashboardOptions:
    boto3_raw_data: "type_defs.DashboardOptionsTypeDef" = dataclasses.field()

    EngagementMetrics = field("EngagementMetrics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashboardOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashboardOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DedicatedIpPool:
    boto3_raw_data: "type_defs.DedicatedIpPoolTypeDef" = dataclasses.field()

    PoolName = field("PoolName")
    ScalingMode = field("ScalingMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DedicatedIpPoolTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DedicatedIpPoolTypeDef"]],
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
class DeleteContactListRequest:
    boto3_raw_data: "type_defs.DeleteContactListRequestTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContactListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContactListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContactRequest:
    boto3_raw_data: "type_defs.DeleteContactRequestTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")
    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomVerificationEmailTemplateRequest:
    boto3_raw_data: "type_defs.DeleteCustomVerificationEmailTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    TemplateName = field("TemplateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCustomVerificationEmailTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomVerificationEmailTemplateRequestTypeDef"]
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
class DeleteEmailIdentityPolicyRequest:
    boto3_raw_data: "type_defs.DeleteEmailIdentityPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    EmailIdentity = field("EmailIdentity")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEmailIdentityPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEmailIdentityPolicyRequestTypeDef"]
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
class DeleteEmailTemplateRequest:
    boto3_raw_data: "type_defs.DeleteEmailTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")

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
class DeleteMultiRegionEndpointRequest:
    boto3_raw_data: "type_defs.DeleteMultiRegionEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    EndpointName = field("EndpointName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMultiRegionEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiRegionEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSuppressedDestinationRequest:
    boto3_raw_data: "type_defs.DeleteSuppressedDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteSuppressedDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSuppressedDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTenantRequest:
    boto3_raw_data: "type_defs.DeleteTenantRequestTypeDef" = dataclasses.field()

    TenantName = field("TenantName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTenantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTenantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTenantResourceAssociationRequest:
    boto3_raw_data: "type_defs.DeleteTenantResourceAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    TenantName = field("TenantName")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTenantResourceAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTenantResourceAssociationRequestTypeDef"]
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
class RouteDetails:
    boto3_raw_data: "type_defs.RouteDetailsTypeDef" = dataclasses.field()

    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteDetailsTypeDef"]],
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
class EmailTemplateMetadata:
    boto3_raw_data: "type_defs.EmailTemplateMetadataTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    CreatedTimestamp = field("CreatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailTemplateMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailTemplateMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventBridgeDestination:
    boto3_raw_data: "type_defs.EventBridgeDestinationTypeDef" = dataclasses.field()

    EventBusArn = field("EventBusArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventBridgeDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventBridgeDestinationTypeDef"]
        ],
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
class ExportJobSummary:
    boto3_raw_data: "type_defs.ExportJobSummaryTypeDef" = dataclasses.field()

    JobId = field("JobId")
    ExportSourceType = field("ExportSourceType")
    JobStatus = field("JobStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    CompletedTimestamp = field("CompletedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportMetric:
    boto3_raw_data: "type_defs.ExportMetricTypeDef" = dataclasses.field()

    Name = field("Name")
    Aggregation = field("Aggregation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportMetricTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportStatistics:
    boto3_raw_data: "type_defs.ExportStatisticsTypeDef" = dataclasses.field()

    ProcessedRecordsCount = field("ProcessedRecordsCount")
    ExportedRecordsCount = field("ExportedRecordsCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureInfo:
    boto3_raw_data: "type_defs.FailureInfoTypeDef" = dataclasses.field()

    FailedRecordsS3Url = field("FailedRecordsS3Url")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailureInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailureInfoTypeDef"]]
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
class SuppressionAttributes:
    boto3_raw_data: "type_defs.SuppressionAttributesTypeDef" = dataclasses.field()

    SuppressedReasons = field("SuppressedReasons")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuppressionAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuppressionAttributesTypeDef"]
        ],
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
class SuppressionOptionsOutput:
    boto3_raw_data: "type_defs.SuppressionOptionsOutputTypeDef" = dataclasses.field()

    SuppressedReasons = field("SuppressedReasons")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuppressionOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuppressionOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactListRequest:
    boto3_raw_data: "type_defs.GetContactListRequestTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactRequest:
    boto3_raw_data: "type_defs.GetContactRequestTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")
    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetContactRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomVerificationEmailTemplateRequest:
    boto3_raw_data: "type_defs.GetCustomVerificationEmailTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    TemplateName = field("TemplateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCustomVerificationEmailTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomVerificationEmailTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDedicatedIpPoolRequest:
    boto3_raw_data: "type_defs.GetDedicatedIpPoolRequestTypeDef" = dataclasses.field()

    PoolName = field("PoolName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDedicatedIpPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDedicatedIpPoolRequestTypeDef"]
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
class GetEmailIdentityPoliciesRequest:
    boto3_raw_data: "type_defs.GetEmailIdentityPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    EmailIdentity = field("EmailIdentity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEmailIdentityPoliciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEmailIdentityPoliciesRequestTypeDef"]
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
class GetEmailTemplateRequest:
    boto3_raw_data: "type_defs.GetEmailTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")

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
class GetExportJobRequest:
    boto3_raw_data: "type_defs.GetExportJobRequestTypeDef" = dataclasses.field()

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
class GetImportJobRequest:
    boto3_raw_data: "type_defs.GetImportJobRequestTypeDef" = dataclasses.field()

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
class GetMessageInsightsRequest:
    boto3_raw_data: "type_defs.GetMessageInsightsRequestTypeDef" = dataclasses.field()

    MessageId = field("MessageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMessageInsightsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMessageInsightsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMultiRegionEndpointRequest:
    boto3_raw_data: "type_defs.GetMultiRegionEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    EndpointName = field("EndpointName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMultiRegionEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMultiRegionEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Route:
    boto3_raw_data: "type_defs.RouteTypeDef" = dataclasses.field()

    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReputationEntityRequest:
    boto3_raw_data: "type_defs.GetReputationEntityRequestTypeDef" = dataclasses.field()

    ReputationEntityReference = field("ReputationEntityReference")
    ReputationEntityType = field("ReputationEntityType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReputationEntityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReputationEntityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSuppressedDestinationRequest:
    boto3_raw_data: "type_defs.GetSuppressedDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSuppressedDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSuppressedDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTenantRequest:
    boto3_raw_data: "type_defs.GetTenantRequestTypeDef" = dataclasses.field()

    TenantName = field("TenantName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTenantRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTenantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardianAttributes:
    boto3_raw_data: "type_defs.GuardianAttributesTypeDef" = dataclasses.field()

    OptimizedSharedDelivery = field("OptimizedSharedDelivery")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardianAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardianAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardianOptions:
    boto3_raw_data: "type_defs.GuardianOptionsTypeDef" = dataclasses.field()

    OptimizedSharedDelivery = field("OptimizedSharedDelivery")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GuardianOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GuardianOptionsTypeDef"]],
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
    VerificationStatus = field("VerificationStatus")

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
class SuppressionListDestination:
    boto3_raw_data: "type_defs.SuppressionListDestinationTypeDef" = dataclasses.field()

    SuppressionListImportAction = field("SuppressionListImportAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuppressionListDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuppressionListDestinationTypeDef"]
        ],
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
class ListContactListsRequest:
    boto3_raw_data: "type_defs.ListContactListsRequestTypeDef" = dataclasses.field()

    PageSize = field("PageSize")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactListsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactListsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicFilter:
    boto3_raw_data: "type_defs.TopicFilterTypeDef" = dataclasses.field()

    TopicName = field("TopicName")
    UseDefaultIfPreferenceUnavailable = field("UseDefaultIfPreferenceUnavailable")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TopicFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TopicFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomVerificationEmailTemplatesRequest:
    boto3_raw_data: "type_defs.ListCustomVerificationEmailTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomVerificationEmailTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomVerificationEmailTemplatesRequestTypeDef"]
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
class ListEmailTemplatesRequest:
    boto3_raw_data: "type_defs.ListEmailTemplatesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEmailTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEmailTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportJobsRequest:
    boto3_raw_data: "type_defs.ListExportJobsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    PageSize = field("PageSize")
    ExportSourceType = field("ExportSourceType")
    JobStatus = field("JobStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportJobsRequest:
    boto3_raw_data: "type_defs.ListImportJobsRequestTypeDef" = dataclasses.field()

    ImportDestinationType = field("ImportDestinationType")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagementOptions:
    boto3_raw_data: "type_defs.ListManagementOptionsTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")
    TopicName = field("TopicName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagementOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagementOptionsTypeDef"]
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
class ListMultiRegionEndpointsRequest:
    boto3_raw_data: "type_defs.ListMultiRegionEndpointsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMultiRegionEndpointsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiRegionEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiRegionEndpoint:
    boto3_raw_data: "type_defs.MultiRegionEndpointTypeDef" = dataclasses.field()

    EndpointName = field("EndpointName")
    Status = field("Status")
    EndpointId = field("EndpointId")
    Regions = field("Regions")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiRegionEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiRegionEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsRequest:
    boto3_raw_data: "type_defs.ListRecommendationsRequestTypeDef" = dataclasses.field()

    Filter = field("Filter")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recommendation:
    boto3_raw_data: "type_defs.RecommendationTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Type = field("Type")
    Description = field("Description")
    Status = field("Status")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    Impact = field("Impact")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecommendationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReputationEntitiesRequest:
    boto3_raw_data: "type_defs.ListReputationEntitiesRequestTypeDef" = (
        dataclasses.field()
    )

    Filter = field("Filter")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReputationEntitiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReputationEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTenantsRequest:
    boto3_raw_data: "type_defs.ListResourceTenantsRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    PageSize = field("PageSize")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceTenantsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTenantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTenantMetadata:
    boto3_raw_data: "type_defs.ResourceTenantMetadataTypeDef" = dataclasses.field()

    TenantName = field("TenantName")
    TenantId = field("TenantId")
    ResourceArn = field("ResourceArn")
    AssociatedTimestamp = field("AssociatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceTenantMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceTenantMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuppressedDestinationSummary:
    boto3_raw_data: "type_defs.SuppressedDestinationSummaryTypeDef" = (
        dataclasses.field()
    )

    EmailAddress = field("EmailAddress")
    Reason = field("Reason")
    LastUpdateTime = field("LastUpdateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuppressedDestinationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuppressedDestinationSummaryTypeDef"]
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
class ListTenantResourcesRequest:
    boto3_raw_data: "type_defs.ListTenantResourcesRequestTypeDef" = dataclasses.field()

    TenantName = field("TenantName")
    Filter = field("Filter")
    PageSize = field("PageSize")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTenantResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTenantResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TenantResource:
    boto3_raw_data: "type_defs.TenantResourceTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TenantResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TenantResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTenantsRequest:
    boto3_raw_data: "type_defs.ListTenantsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTenantsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTenantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TenantInfo:
    boto3_raw_data: "type_defs.TenantInfoTypeDef" = dataclasses.field()

    TenantName = field("TenantName")
    TenantId = field("TenantId")
    TenantArn = field("TenantArn")
    CreatedTimestamp = field("CreatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TenantInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TenantInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageInsightsFiltersOutput:
    boto3_raw_data: "type_defs.MessageInsightsFiltersOutputTypeDef" = (
        dataclasses.field()
    )

    FromEmailAddress = field("FromEmailAddress")
    Destination = field("Destination")
    Subject = field("Subject")
    Isp = field("Isp")
    LastDeliveryEvent = field("LastDeliveryEvent")
    LastEngagementEvent = field("LastEngagementEvent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageInsightsFiltersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageInsightsFiltersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageInsightsFilters:
    boto3_raw_data: "type_defs.MessageInsightsFiltersTypeDef" = dataclasses.field()

    FromEmailAddress = field("FromEmailAddress")
    Destination = field("Destination")
    Subject = field("Subject")
    Isp = field("Isp")
    LastDeliveryEvent = field("LastDeliveryEvent")
    LastEngagementEvent = field("LastEngagementEvent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageInsightsFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageInsightsFiltersTypeDef"]
        ],
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
class PutAccountDetailsRequest:
    boto3_raw_data: "type_defs.PutAccountDetailsRequestTypeDef" = dataclasses.field()

    MailType = field("MailType")
    WebsiteURL = field("WebsiteURL")
    ContactLanguage = field("ContactLanguage")
    UseCaseDescription = field("UseCaseDescription")
    AdditionalContactEmailAddresses = field("AdditionalContactEmailAddresses")
    ProductionAccessEnabled = field("ProductionAccessEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccountDetailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountDetailsRequestTypeDef"]
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
class PutAccountSuppressionAttributesRequest:
    boto3_raw_data: "type_defs.PutAccountSuppressionAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    SuppressedReasons = field("SuppressedReasons")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAccountSuppressionAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountSuppressionAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConfigurationSetArchivingOptionsRequest:
    boto3_raw_data: "type_defs.PutConfigurationSetArchivingOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    ArchiveArn = field("ArchiveArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfigurationSetArchivingOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigurationSetArchivingOptionsRequestTypeDef"]
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
    MaxDeliverySeconds = field("MaxDeliverySeconds")

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
class PutConfigurationSetSuppressionOptionsRequest:
    boto3_raw_data: "type_defs.PutConfigurationSetSuppressionOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    SuppressedReasons = field("SuppressedReasons")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfigurationSetSuppressionOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigurationSetSuppressionOptionsRequestTypeDef"]
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
    HttpsPolicy = field("HttpsPolicy")

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
class PutDedicatedIpPoolScalingAttributesRequest:
    boto3_raw_data: "type_defs.PutDedicatedIpPoolScalingAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    PoolName = field("PoolName")
    ScalingMode = field("ScalingMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutDedicatedIpPoolScalingAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDedicatedIpPoolScalingAttributesRequestTypeDef"]
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
class PutEmailIdentityConfigurationSetAttributesRequest:
    boto3_raw_data: (
        "type_defs.PutEmailIdentityConfigurationSetAttributesRequestTypeDef"
    ) = dataclasses.field()

    EmailIdentity = field("EmailIdentity")
    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEmailIdentityConfigurationSetAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.PutEmailIdentityConfigurationSetAttributesRequestTypeDef"
            ]
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
class PutSuppressedDestinationRequest:
    boto3_raw_data: "type_defs.PutSuppressedDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    EmailAddress = field("EmailAddress")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutSuppressedDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSuppressedDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplacementTemplate:
    boto3_raw_data: "type_defs.ReplacementTemplateTypeDef" = dataclasses.field()

    ReplacementTemplateData = field("ReplacementTemplateData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplacementTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplacementTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusRecord:
    boto3_raw_data: "type_defs.StatusRecordTypeDef" = dataclasses.field()

    Status = field("Status")
    Cause = field("Cause")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatusRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SOARecord:
    boto3_raw_data: "type_defs.SOARecordTypeDef" = dataclasses.field()

    PrimaryNameServer = field("PrimaryNameServer")
    AdminEmail = field("AdminEmail")
    SerialNumber = field("SerialNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SOARecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SOARecordTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendCustomVerificationEmailRequest:
    boto3_raw_data: "type_defs.SendCustomVerificationEmailRequestTypeDef" = (
        dataclasses.field()
    )

    EmailAddress = field("EmailAddress")
    TemplateName = field("TemplateName")
    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SendCustomVerificationEmailRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendCustomVerificationEmailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuppressedDestinationAttributes:
    boto3_raw_data: "type_defs.SuppressedDestinationAttributesTypeDef" = (
        dataclasses.field()
    )

    MessageId = field("MessageId")
    FeedbackId = field("FeedbackId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SuppressedDestinationAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuppressedDestinationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuppressionOptions:
    boto3_raw_data: "type_defs.SuppressionOptionsTypeDef" = dataclasses.field()

    SuppressedReasons = field("SuppressedReasons")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuppressionOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuppressionOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestRenderEmailTemplateRequest:
    boto3_raw_data: "type_defs.TestRenderEmailTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    TemplateName = field("TemplateName")
    TemplateData = field("TemplateData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TestRenderEmailTemplateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestRenderEmailTemplateRequestTypeDef"]
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
class UpdateCustomVerificationEmailTemplateRequest:
    boto3_raw_data: "type_defs.UpdateCustomVerificationEmailTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    TemplateName = field("TemplateName")
    FromEmailAddress = field("FromEmailAddress")
    TemplateSubject = field("TemplateSubject")
    TemplateContent = field("TemplateContent")
    SuccessRedirectionURL = field("SuccessRedirectionURL")
    FailureRedirectionURL = field("FailureRedirectionURL")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomVerificationEmailTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomVerificationEmailTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEmailIdentityPolicyRequest:
    boto3_raw_data: "type_defs.UpdateEmailIdentityPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    EmailIdentity = field("EmailIdentity")
    PolicyName = field("PolicyName")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEmailIdentityPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEmailIdentityPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReputationEntityCustomerManagedStatusRequest:
    boto3_raw_data: (
        "type_defs.UpdateReputationEntityCustomerManagedStatusRequestTypeDef"
    ) = dataclasses.field()

    ReputationEntityType = field("ReputationEntityType")
    ReputationEntityReference = field("ReputationEntityReference")
    SendingStatus = field("SendingStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateReputationEntityCustomerManagedStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateReputationEntityCustomerManagedStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReputationEntityPolicyRequest:
    boto3_raw_data: "type_defs.UpdateReputationEntityPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ReputationEntityType = field("ReputationEntityType")
    ReputationEntityReference = field("ReputationEntityReference")
    ReputationEntityPolicy = field("ReputationEntityPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateReputationEntityPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReputationEntityPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountDetails:
    boto3_raw_data: "type_defs.AccountDetailsTypeDef" = dataclasses.field()

    MailType = field("MailType")
    WebsiteURL = field("WebsiteURL")
    ContactLanguage = field("ContactLanguage")
    UseCaseDescription = field("UseCaseDescription")
    AdditionalContactEmailAddresses = field("AdditionalContactEmailAddresses")

    @cached_property
    def ReviewDetails(self):  # pragma: no cover
        return ReviewDetails.make_one(self.boto3_raw_data["ReviewDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attachment:
    boto3_raw_data: "type_defs.AttachmentTypeDef" = dataclasses.field()

    RawContent = field("RawContent")
    FileName = field("FileName")
    ContentDisposition = field("ContentDisposition")
    ContentDescription = field("ContentDescription")
    ContentId = field("ContentId")
    ContentTransferEncoding = field("ContentTransferEncoding")
    ContentType = field("ContentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachmentTypeDef"]]
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
class BatchGetMetricDataQuery:
    boto3_raw_data: "type_defs.BatchGetMetricDataQueryTypeDef" = dataclasses.field()

    Id = field("Id")
    Namespace = field("Namespace")
    Metric = field("Metric")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    Dimensions = field("Dimensions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetMetricDataQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetMetricDataQueryTypeDef"]
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
class ListSuppressedDestinationsRequest:
    boto3_raw_data: "type_defs.ListSuppressedDestinationsRequestTypeDef" = (
        dataclasses.field()
    )

    Reasons = field("Reasons")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSuppressedDestinationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSuppressedDestinationsRequestTypeDef"]
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
class BatchGetMetricDataResponse:
    boto3_raw_data: "type_defs.BatchGetMetricDataResponseTypeDef" = dataclasses.field()

    @cached_property
    def Results(self):  # pragma: no cover
        return MetricDataResult.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return MetricDataError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetMetricDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetMetricDataResponseTypeDef"]
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
class CreateExportJobResponse:
    boto3_raw_data: "type_defs.CreateExportJobResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")

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
class CreateImportJobResponse:
    boto3_raw_data: "type_defs.CreateImportJobResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")

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
class CreateMultiRegionEndpointResponse:
    boto3_raw_data: "type_defs.CreateMultiRegionEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    EndpointId = field("EndpointId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMultiRegionEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiRegionEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMultiRegionEndpointResponse:
    boto3_raw_data: "type_defs.DeleteMultiRegionEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMultiRegionEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiRegionEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomVerificationEmailTemplateResponse:
    boto3_raw_data: "type_defs.GetCustomVerificationEmailTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    TemplateName = field("TemplateName")
    FromEmailAddress = field("FromEmailAddress")
    TemplateSubject = field("TemplateSubject")
    TemplateContent = field("TemplateContent")
    SuccessRedirectionURL = field("SuccessRedirectionURL")
    FailureRedirectionURL = field("FailureRedirectionURL")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCustomVerificationEmailTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomVerificationEmailTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEmailIdentityPoliciesResponse:
    boto3_raw_data: "type_defs.GetEmailIdentityPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    Policies = field("Policies")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEmailIdentityPoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEmailIdentityPoliciesResponseTypeDef"]
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
class PutEmailIdentityDkimSigningAttributesResponse:
    boto3_raw_data: "type_defs.PutEmailIdentityDkimSigningAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    DkimStatus = field("DkimStatus")
    DkimTokens = field("DkimTokens")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEmailIdentityDkimSigningAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEmailIdentityDkimSigningAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendCustomVerificationEmailResponse:
    boto3_raw_data: "type_defs.SendCustomVerificationEmailResponseTypeDef" = (
        dataclasses.field()
    )

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SendCustomVerificationEmailResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendCustomVerificationEmailResponseTypeDef"]
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
class TestRenderEmailTemplateResponse:
    boto3_raw_data: "type_defs.TestRenderEmailTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    RenderedTemplate = field("RenderedTemplate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TestRenderEmailTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestRenderEmailTemplateResponseTypeDef"]
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
class SendBulkEmailResponse:
    boto3_raw_data: "type_defs.SendBulkEmailResponseTypeDef" = dataclasses.field()

    @cached_property
    def BulkEmailEntryResults(self):  # pragma: no cover
        return BulkEmailEntryResult.make_many(
            self.boto3_raw_data["BulkEmailEntryResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendBulkEmailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendBulkEmailResponseTypeDef"]
        ],
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
class EventDetails:
    boto3_raw_data: "type_defs.EventDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Bounce(self):  # pragma: no cover
        return Bounce.make_one(self.boto3_raw_data["Bounce"])

    @cached_property
    def Complaint(self):  # pragma: no cover
        return Complaint.make_one(self.boto3_raw_data["Complaint"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactListsResponse:
    boto3_raw_data: "type_defs.ListContactListsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ContactLists(self):  # pragma: no cover
        return ContactList.make_many(self.boto3_raw_data["ContactLists"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactListsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactListsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Contact:
    boto3_raw_data: "type_defs.ContactTypeDef" = dataclasses.field()

    EmailAddress = field("EmailAddress")

    @cached_property
    def TopicPreferences(self):  # pragma: no cover
        return TopicPreference.make_many(self.boto3_raw_data["TopicPreferences"])

    @cached_property
    def TopicDefaultPreferences(self):  # pragma: no cover
        return TopicPreference.make_many(self.boto3_raw_data["TopicDefaultPreferences"])

    UnsubscribeAll = field("UnsubscribeAll")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactRequest:
    boto3_raw_data: "type_defs.CreateContactRequestTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")
    EmailAddress = field("EmailAddress")

    @cached_property
    def TopicPreferences(self):  # pragma: no cover
        return TopicPreference.make_many(self.boto3_raw_data["TopicPreferences"])

    UnsubscribeAll = field("UnsubscribeAll")
    AttributesData = field("AttributesData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactResponse:
    boto3_raw_data: "type_defs.GetContactResponseTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")
    EmailAddress = field("EmailAddress")

    @cached_property
    def TopicPreferences(self):  # pragma: no cover
        return TopicPreference.make_many(self.boto3_raw_data["TopicPreferences"])

    @cached_property
    def TopicDefaultPreferences(self):  # pragma: no cover
        return TopicPreference.make_many(self.boto3_raw_data["TopicDefaultPreferences"])

    UnsubscribeAll = field("UnsubscribeAll")
    AttributesData = field("AttributesData")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactRequest:
    boto3_raw_data: "type_defs.UpdateContactRequestTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")
    EmailAddress = field("EmailAddress")

    @cached_property
    def TopicPreferences(self):  # pragma: no cover
        return TopicPreference.make_many(self.boto3_raw_data["TopicPreferences"])

    UnsubscribeAll = field("UnsubscribeAll")
    AttributesData = field("AttributesData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactRequestTypeDef"]
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

    ScalingMode = field("ScalingMode")

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
class CreateTenantRequest:
    boto3_raw_data: "type_defs.CreateTenantRequestTypeDef" = dataclasses.field()

    TenantName = field("TenantName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTenantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTenantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTenantResponse:
    boto3_raw_data: "type_defs.CreateTenantResponseTypeDef" = dataclasses.field()

    TenantName = field("TenantName")
    TenantId = field("TenantId")
    TenantArn = field("TenantArn")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SendingStatus = field("SendingStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTenantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTenantResponseTypeDef"]
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
class Tenant:
    boto3_raw_data: "type_defs.TenantTypeDef" = dataclasses.field()

    TenantName = field("TenantName")
    TenantId = field("TenantId")
    TenantArn = field("TenantArn")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SendingStatus = field("SendingStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TenantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TenantTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactListRequest:
    boto3_raw_data: "type_defs.CreateContactListRequestTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")

    @cached_property
    def Topics(self):  # pragma: no cover
        return Topic.make_many(self.boto3_raw_data["Topics"])

    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactListResponse:
    boto3_raw_data: "type_defs.GetContactListResponseTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")

    @cached_property
    def Topics(self):  # pragma: no cover
        return Topic.make_many(self.boto3_raw_data["Topics"])

    Description = field("Description")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactListResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactListRequest:
    boto3_raw_data: "type_defs.UpdateContactListRequestTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")

    @cached_property
    def Topics(self):  # pragma: no cover
        return Topic.make_many(self.boto3_raw_data["Topics"])

    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContactListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactListRequestTypeDef"]
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

    @cached_property
    def DkimSigningAttributes(self):  # pragma: no cover
        return DkimSigningAttributes.make_one(
            self.boto3_raw_data["DkimSigningAttributes"]
        )

    ConfigurationSetName = field("ConfigurationSetName")

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
class PutEmailIdentityDkimSigningAttributesRequest:
    boto3_raw_data: "type_defs.PutEmailIdentityDkimSigningAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    EmailIdentity = field("EmailIdentity")
    SigningAttributesOrigin = field("SigningAttributesOrigin")

    @cached_property
    def SigningAttributes(self):  # pragma: no cover
        return DkimSigningAttributes.make_one(self.boto3_raw_data["SigningAttributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEmailIdentityDkimSigningAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEmailIdentityDkimSigningAttributesRequestTypeDef"]
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
class CreateEmailTemplateRequest:
    boto3_raw_data: "type_defs.CreateEmailTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")

    @cached_property
    def TemplateContent(self):  # pragma: no cover
        return EmailTemplateContent.make_one(self.boto3_raw_data["TemplateContent"])

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
class GetEmailTemplateResponse:
    boto3_raw_data: "type_defs.GetEmailTemplateResponseTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")

    @cached_property
    def TemplateContent(self):  # pragma: no cover
        return EmailTemplateContent.make_one(self.boto3_raw_data["TemplateContent"])

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
class UpdateEmailTemplateRequest:
    boto3_raw_data: "type_defs.UpdateEmailTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")

    @cached_property
    def TemplateContent(self):  # pragma: no cover
        return EmailTemplateContent.make_one(self.boto3_raw_data["TemplateContent"])

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
class ListCustomVerificationEmailTemplatesResponse:
    boto3_raw_data: "type_defs.ListCustomVerificationEmailTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CustomVerificationEmailTemplates(self):  # pragma: no cover
        return CustomVerificationEmailTemplateMetadata.make_many(
            self.boto3_raw_data["CustomVerificationEmailTemplates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomVerificationEmailTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomVerificationEmailTemplatesResponseTypeDef"]
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
class GetDedicatedIpPoolResponse:
    boto3_raw_data: "type_defs.GetDedicatedIpPoolResponseTypeDef" = dataclasses.field()

    @cached_property
    def DedicatedIpPool(self):  # pragma: no cover
        return DedicatedIpPool.make_one(self.boto3_raw_data["DedicatedIpPool"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDedicatedIpPoolResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDedicatedIpPoolResponseTypeDef"]
        ],
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
class Details:
    boto3_raw_data: "type_defs.DetailsTypeDef" = dataclasses.field()

    @cached_property
    def RoutesDetails(self):  # pragma: no cover
        return RouteDetails.make_many(self.boto3_raw_data["RoutesDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetailsTypeDef"]]
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
class ListEmailTemplatesResponse:
    boto3_raw_data: "type_defs.ListEmailTemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def TemplatesMetadata(self):  # pragma: no cover
        return EmailTemplateMetadata.make_many(self.boto3_raw_data["TemplatesMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEmailTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEmailTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportJobsResponse:
    boto3_raw_data: "type_defs.ListExportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ExportJobs(self):  # pragma: no cover
        return ExportJobSummary.make_many(self.boto3_raw_data["ExportJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsDataSourceOutput:
    boto3_raw_data: "type_defs.MetricsDataSourceOutputTypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")
    Namespace = field("Namespace")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return ExportMetric.make_many(self.boto3_raw_data["Metrics"])

    StartDate = field("StartDate")
    EndDate = field("EndDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricsDataSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricsDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsDataSource:
    boto3_raw_data: "type_defs.MetricsDataSourceTypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")
    Namespace = field("Namespace")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return ExportMetric.make_many(self.boto3_raw_data["Metrics"])

    StartDate = field("StartDate")
    EndDate = field("EndDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricsDataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricsDataSourceTypeDef"]
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
class GetMultiRegionEndpointResponse:
    boto3_raw_data: "type_defs.GetMultiRegionEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    EndpointName = field("EndpointName")
    EndpointId = field("EndpointId")

    @cached_property
    def Routes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["Routes"])

    Status = field("Status")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMultiRegionEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMultiRegionEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VdmAttributes:
    boto3_raw_data: "type_defs.VdmAttributesTypeDef" = dataclasses.field()

    VdmEnabled = field("VdmEnabled")

    @cached_property
    def DashboardAttributes(self):  # pragma: no cover
        return DashboardAttributes.make_one(self.boto3_raw_data["DashboardAttributes"])

    @cached_property
    def GuardianAttributes(self):  # pragma: no cover
        return GuardianAttributes.make_one(self.boto3_raw_data["GuardianAttributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VdmAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VdmAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VdmOptions:
    boto3_raw_data: "type_defs.VdmOptionsTypeDef" = dataclasses.field()

    @cached_property
    def DashboardOptions(self):  # pragma: no cover
        return DashboardOptions.make_one(self.boto3_raw_data["DashboardOptions"])

    @cached_property
    def GuardianOptions(self):  # pragma: no cover
        return GuardianOptions.make_one(self.boto3_raw_data["GuardianOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VdmOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VdmOptionsTypeDef"]]
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
class ImportDestination:
    boto3_raw_data: "type_defs.ImportDestinationTypeDef" = dataclasses.field()

    @cached_property
    def SuppressionListDestination(self):  # pragma: no cover
        return SuppressionListDestination.make_one(
            self.boto3_raw_data["SuppressionListDestination"]
        )

    @cached_property
    def ContactListDestination(self):  # pragma: no cover
        return ContactListDestination.make_one(
            self.boto3_raw_data["ContactListDestination"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactsFilter:
    boto3_raw_data: "type_defs.ListContactsFilterTypeDef" = dataclasses.field()

    FilteredStatus = field("FilteredStatus")

    @cached_property
    def TopicFilter(self):  # pragma: no cover
        return TopicFilter.make_one(self.boto3_raw_data["TopicFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultiRegionEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListMultiRegionEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMultiRegionEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiRegionEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReputationEntitiesRequestPaginate:
    boto3_raw_data: "type_defs.ListReputationEntitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Filter = field("Filter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReputationEntitiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReputationEntitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTenantsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceTenantsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceTenantsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTenantsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTenantResourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListTenantResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TenantName = field("TenantName")
    Filter = field("Filter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTenantResourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTenantResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTenantsRequestPaginate:
    boto3_raw_data: "type_defs.ListTenantsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTenantsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTenantsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultiRegionEndpointsResponse:
    boto3_raw_data: "type_defs.ListMultiRegionEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MultiRegionEndpoints(self):  # pragma: no cover
        return MultiRegionEndpoint.make_many(
            self.boto3_raw_data["MultiRegionEndpoints"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMultiRegionEndpointsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiRegionEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsResponse:
    boto3_raw_data: "type_defs.ListRecommendationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Recommendations(self):  # pragma: no cover
        return Recommendation.make_many(self.boto3_raw_data["Recommendations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTenantsResponse:
    boto3_raw_data: "type_defs.ListResourceTenantsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceTenants(self):  # pragma: no cover
        return ResourceTenantMetadata.make_many(self.boto3_raw_data["ResourceTenants"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceTenantsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTenantsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSuppressedDestinationsResponse:
    boto3_raw_data: "type_defs.ListSuppressedDestinationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SuppressedDestinationSummaries(self):  # pragma: no cover
        return SuppressedDestinationSummary.make_many(
            self.boto3_raw_data["SuppressedDestinationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSuppressedDestinationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSuppressedDestinationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTenantResourcesResponse:
    boto3_raw_data: "type_defs.ListTenantResourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def TenantResources(self):  # pragma: no cover
        return TenantResource.make_many(self.boto3_raw_data["TenantResources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTenantResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTenantResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTenantsResponse:
    boto3_raw_data: "type_defs.ListTenantsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tenants(self):  # pragma: no cover
        return TenantInfo.make_many(self.boto3_raw_data["Tenants"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTenantsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTenantsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageInsightsDataSourceOutput:
    boto3_raw_data: "type_defs.MessageInsightsDataSourceOutputTypeDef" = (
        dataclasses.field()
    )

    StartDate = field("StartDate")
    EndDate = field("EndDate")

    @cached_property
    def Include(self):  # pragma: no cover
        return MessageInsightsFiltersOutput.make_one(self.boto3_raw_data["Include"])

    @cached_property
    def Exclude(self):  # pragma: no cover
        return MessageInsightsFiltersOutput.make_one(self.boto3_raw_data["Exclude"])

    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MessageInsightsDataSourceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageInsightsDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageInsightsDataSource:
    boto3_raw_data: "type_defs.MessageInsightsDataSourceTypeDef" = dataclasses.field()

    StartDate = field("StartDate")
    EndDate = field("EndDate")

    @cached_property
    def Include(self):  # pragma: no cover
        return MessageInsightsFilters.make_one(self.boto3_raw_data["Include"])

    @cached_property
    def Exclude(self):  # pragma: no cover
        return MessageInsightsFilters.make_one(self.boto3_raw_data["Exclude"])

    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageInsightsDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageInsightsDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplacementEmailContent:
    boto3_raw_data: "type_defs.ReplacementEmailContentTypeDef" = dataclasses.field()

    @cached_property
    def ReplacementTemplate(self):  # pragma: no cover
        return ReplacementTemplate.make_one(self.boto3_raw_data["ReplacementTemplate"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplacementEmailContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplacementEmailContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReputationEntity:
    boto3_raw_data: "type_defs.ReputationEntityTypeDef" = dataclasses.field()

    ReputationEntityReference = field("ReputationEntityReference")
    ReputationEntityType = field("ReputationEntityType")
    ReputationManagementPolicy = field("ReputationManagementPolicy")

    @cached_property
    def CustomerManagedStatus(self):  # pragma: no cover
        return StatusRecord.make_one(self.boto3_raw_data["CustomerManagedStatus"])

    @cached_property
    def AwsSesManagedStatus(self):  # pragma: no cover
        return StatusRecord.make_one(self.boto3_raw_data["AwsSesManagedStatus"])

    SendingStatusAggregate = field("SendingStatusAggregate")
    ReputationImpact = field("ReputationImpact")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReputationEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReputationEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerificationInfo:
    boto3_raw_data: "type_defs.VerificationInfoTypeDef" = dataclasses.field()

    LastCheckedTimestamp = field("LastCheckedTimestamp")
    LastSuccessTimestamp = field("LastSuccessTimestamp")
    ErrorType = field("ErrorType")

    @cached_property
    def SOARecord(self):  # pragma: no cover
        return SOARecord.make_one(self.boto3_raw_data["SOARecord"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VerificationInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerificationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuppressedDestination:
    boto3_raw_data: "type_defs.SuppressedDestinationTypeDef" = dataclasses.field()

    EmailAddress = field("EmailAddress")
    Reason = field("Reason")
    LastUpdateTime = field("LastUpdateTime")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return SuppressedDestinationAttributes.make_one(
            self.boto3_raw_data["Attributes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuppressedDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuppressedDestinationTypeDef"]
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

    TemplateName = field("TemplateName")
    TemplateArn = field("TemplateArn")

    @cached_property
    def TemplateContent(self):  # pragma: no cover
        return EmailTemplateContent.make_one(self.boto3_raw_data["TemplateContent"])

    TemplateData = field("TemplateData")

    @cached_property
    def Headers(self):  # pragma: no cover
        return MessageHeader.make_many(self.boto3_raw_data["Headers"])

    @cached_property
    def Attachments(self):  # pragma: no cover
        return Attachment.make_many(self.boto3_raw_data["Attachments"])

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
class BatchGetMetricDataRequest:
    boto3_raw_data: "type_defs.BatchGetMetricDataRequestTypeDef" = dataclasses.field()

    @cached_property
    def Queries(self):  # pragma: no cover
        return BatchGetMetricDataQuery.make_many(self.boto3_raw_data["Queries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetMetricDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetMetricDataRequestTypeDef"]
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

    @cached_property
    def Headers(self):  # pragma: no cover
        return MessageHeader.make_many(self.boto3_raw_data["Headers"])

    @cached_property
    def Attachments(self):  # pragma: no cover
        return Attachment.make_many(self.boto3_raw_data["Attachments"])

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
    def EventBridgeDestination(self):  # pragma: no cover
        return EventBridgeDestination.make_one(
            self.boto3_raw_data["EventBridgeDestination"]
        )

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
class InsightsEvent:
    boto3_raw_data: "type_defs.InsightsEventTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    Type = field("Type")

    @cached_property
    def Details(self):  # pragma: no cover
        return EventDetails.make_one(self.boto3_raw_data["Details"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightsEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightsEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactsResponse:
    boto3_raw_data: "type_defs.ListContactsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Contacts(self):  # pragma: no cover
        return Contact.make_many(self.boto3_raw_data["Contacts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTenantResponse:
    boto3_raw_data: "type_defs.GetTenantResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tenant(self):  # pragma: no cover
        return Tenant.make_one(self.boto3_raw_data["Tenant"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTenantResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTenantResponseTypeDef"]
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
class CreateMultiRegionEndpointRequest:
    boto3_raw_data: "type_defs.CreateMultiRegionEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    EndpointName = field("EndpointName")

    @cached_property
    def Details(self):  # pragma: no cover
        return Details.make_one(self.boto3_raw_data["Details"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMultiRegionEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiRegionEndpointRequestTypeDef"]
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
class GetAccountResponse:
    boto3_raw_data: "type_defs.GetAccountResponseTypeDef" = dataclasses.field()

    DedicatedIpAutoWarmupEnabled = field("DedicatedIpAutoWarmupEnabled")
    EnforcementStatus = field("EnforcementStatus")
    ProductionAccessEnabled = field("ProductionAccessEnabled")

    @cached_property
    def SendQuota(self):  # pragma: no cover
        return SendQuota.make_one(self.boto3_raw_data["SendQuota"])

    SendingEnabled = field("SendingEnabled")

    @cached_property
    def SuppressionAttributes(self):  # pragma: no cover
        return SuppressionAttributes.make_one(
            self.boto3_raw_data["SuppressionAttributes"]
        )

    @cached_property
    def Details(self):  # pragma: no cover
        return AccountDetails.make_one(self.boto3_raw_data["Details"])

    @cached_property
    def VdmAttributes(self):  # pragma: no cover
        return VdmAttributes.make_one(self.boto3_raw_data["VdmAttributes"])

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
class PutAccountVdmAttributesRequest:
    boto3_raw_data: "type_defs.PutAccountVdmAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VdmAttributes(self):  # pragma: no cover
        return VdmAttributes.make_one(self.boto3_raw_data["VdmAttributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutAccountVdmAttributesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountVdmAttributesRequestTypeDef"]
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
    def SuppressionOptions(self):  # pragma: no cover
        return SuppressionOptionsOutput.make_one(
            self.boto3_raw_data["SuppressionOptions"]
        )

    @cached_property
    def VdmOptions(self):  # pragma: no cover
        return VdmOptions.make_one(self.boto3_raw_data["VdmOptions"])

    @cached_property
    def ArchivingOptions(self):  # pragma: no cover
        return ArchivingOptions.make_one(self.boto3_raw_data["ArchivingOptions"])

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
class PutConfigurationSetVdmOptionsRequest:
    boto3_raw_data: "type_defs.PutConfigurationSetVdmOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def VdmOptions(self):  # pragma: no cover
        return VdmOptions.make_one(self.boto3_raw_data["VdmOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfigurationSetVdmOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigurationSetVdmOptionsRequestTypeDef"]
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

    @cached_property
    def ImportDestination(self):  # pragma: no cover
        return ImportDestination.make_one(self.boto3_raw_data["ImportDestination"])

    @cached_property
    def ImportDataSource(self):  # pragma: no cover
        return ImportDataSource.make_one(self.boto3_raw_data["ImportDataSource"])

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
class GetImportJobResponse:
    boto3_raw_data: "type_defs.GetImportJobResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def ImportDestination(self):  # pragma: no cover
        return ImportDestination.make_one(self.boto3_raw_data["ImportDestination"])

    @cached_property
    def ImportDataSource(self):  # pragma: no cover
        return ImportDataSource.make_one(self.boto3_raw_data["ImportDataSource"])

    @cached_property
    def FailureInfo(self):  # pragma: no cover
        return FailureInfo.make_one(self.boto3_raw_data["FailureInfo"])

    JobStatus = field("JobStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    CompletedTimestamp = field("CompletedTimestamp")
    ProcessedRecordsCount = field("ProcessedRecordsCount")
    FailedRecordsCount = field("FailedRecordsCount")

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
class ImportJobSummary:
    boto3_raw_data: "type_defs.ImportJobSummaryTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def ImportDestination(self):  # pragma: no cover
        return ImportDestination.make_one(self.boto3_raw_data["ImportDestination"])

    JobStatus = field("JobStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    ProcessedRecordsCount = field("ProcessedRecordsCount")
    FailedRecordsCount = field("FailedRecordsCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportJobSummaryTypeDef"]
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
class ListContactsRequest:
    boto3_raw_data: "type_defs.ListContactsRequestTypeDef" = dataclasses.field()

    ContactListName = field("ContactListName")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ListContactsFilter.make_one(self.boto3_raw_data["Filter"])

    PageSize = field("PageSize")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportDataSourceOutput:
    boto3_raw_data: "type_defs.ExportDataSourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def MetricsDataSource(self):  # pragma: no cover
        return MetricsDataSourceOutput.make_one(
            self.boto3_raw_data["MetricsDataSource"]
        )

    @cached_property
    def MessageInsightsDataSource(self):  # pragma: no cover
        return MessageInsightsDataSourceOutput.make_one(
            self.boto3_raw_data["MessageInsightsDataSource"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportDataSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportDataSource:
    boto3_raw_data: "type_defs.ExportDataSourceTypeDef" = dataclasses.field()

    @cached_property
    def MetricsDataSource(self):  # pragma: no cover
        return MetricsDataSource.make_one(self.boto3_raw_data["MetricsDataSource"])

    @cached_property
    def MessageInsightsDataSource(self):  # pragma: no cover
        return MessageInsightsDataSource.make_one(
            self.boto3_raw_data["MessageInsightsDataSource"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportDataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BulkEmailEntry:
    boto3_raw_data: "type_defs.BulkEmailEntryTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def ReplacementTags(self):  # pragma: no cover
        return MessageTag.make_many(self.boto3_raw_data["ReplacementTags"])

    @cached_property
    def ReplacementEmailContent(self):  # pragma: no cover
        return ReplacementEmailContent.make_one(
            self.boto3_raw_data["ReplacementEmailContent"]
        )

    @cached_property
    def ReplacementHeaders(self):  # pragma: no cover
        return MessageHeader.make_many(self.boto3_raw_data["ReplacementHeaders"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BulkEmailEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BulkEmailEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReputationEntityResponse:
    boto3_raw_data: "type_defs.GetReputationEntityResponseTypeDef" = dataclasses.field()

    @cached_property
    def ReputationEntity(self):  # pragma: no cover
        return ReputationEntity.make_one(self.boto3_raw_data["ReputationEntity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReputationEntityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReputationEntityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReputationEntitiesResponse:
    boto3_raw_data: "type_defs.ListReputationEntitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReputationEntities(self):  # pragma: no cover
        return ReputationEntity.make_many(self.boto3_raw_data["ReputationEntities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReputationEntitiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReputationEntitiesResponseTypeDef"]
        ],
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

    Policies = field("Policies")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ConfigurationSetName = field("ConfigurationSetName")
    VerificationStatus = field("VerificationStatus")

    @cached_property
    def VerificationInfo(self):  # pragma: no cover
        return VerificationInfo.make_one(self.boto3_raw_data["VerificationInfo"])

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
class GetSuppressedDestinationResponse:
    boto3_raw_data: "type_defs.GetSuppressedDestinationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SuppressedDestination(self):  # pragma: no cover
        return SuppressedDestination.make_one(
            self.boto3_raw_data["SuppressedDestination"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSuppressedDestinationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSuppressedDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BulkEmailContent:
    boto3_raw_data: "type_defs.BulkEmailContentTypeDef" = dataclasses.field()

    @cached_property
    def Template(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["Template"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BulkEmailContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BulkEmailContentTypeDef"]
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

    SuppressionOptions = field("SuppressionOptions")

    @cached_property
    def VdmOptions(self):  # pragma: no cover
        return VdmOptions.make_one(self.boto3_raw_data["VdmOptions"])

    @cached_property
    def ArchivingOptions(self):  # pragma: no cover
        return ArchivingOptions.make_one(self.boto3_raw_data["ArchivingOptions"])

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
    def EventBridgeDestination(self):  # pragma: no cover
        return EventBridgeDestination.make_one(
            self.boto3_raw_data["EventBridgeDestination"]
        )

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
class EmailInsights:
    boto3_raw_data: "type_defs.EmailInsightsTypeDef" = dataclasses.field()

    Destination = field("Destination")
    Isp = field("Isp")

    @cached_property
    def Events(self):  # pragma: no cover
        return InsightsEvent.make_many(self.boto3_raw_data["Events"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailInsightsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailInsightsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportJobsResponse:
    boto3_raw_data: "type_defs.ListImportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ImportJobs(self):  # pragma: no cover
        return ImportJobSummary.make_many(self.boto3_raw_data["ImportJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportJobsResponseTypeDef"]
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

    JobId = field("JobId")
    ExportSourceType = field("ExportSourceType")
    JobStatus = field("JobStatus")

    @cached_property
    def ExportDestination(self):  # pragma: no cover
        return ExportDestination.make_one(self.boto3_raw_data["ExportDestination"])

    @cached_property
    def ExportDataSource(self):  # pragma: no cover
        return ExportDataSourceOutput.make_one(self.boto3_raw_data["ExportDataSource"])

    CreatedTimestamp = field("CreatedTimestamp")
    CompletedTimestamp = field("CompletedTimestamp")

    @cached_property
    def FailureInfo(self):  # pragma: no cover
        return FailureInfo.make_one(self.boto3_raw_data["FailureInfo"])

    @cached_property
    def Statistics(self):  # pragma: no cover
        return ExportStatistics.make_one(self.boto3_raw_data["Statistics"])

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
class SendBulkEmailRequest:
    boto3_raw_data: "type_defs.SendBulkEmailRequestTypeDef" = dataclasses.field()

    @cached_property
    def DefaultContent(self):  # pragma: no cover
        return BulkEmailContent.make_one(self.boto3_raw_data["DefaultContent"])

    @cached_property
    def BulkEmailEntries(self):  # pragma: no cover
        return BulkEmailEntry.make_many(self.boto3_raw_data["BulkEmailEntries"])

    FromEmailAddress = field("FromEmailAddress")
    FromEmailAddressIdentityArn = field("FromEmailAddressIdentityArn")
    ReplyToAddresses = field("ReplyToAddresses")
    FeedbackForwardingEmailAddress = field("FeedbackForwardingEmailAddress")
    FeedbackForwardingEmailAddressIdentityArn = field(
        "FeedbackForwardingEmailAddressIdentityArn"
    )

    @cached_property
    def DefaultEmailTags(self):  # pragma: no cover
        return MessageTag.make_many(self.boto3_raw_data["DefaultEmailTags"])

    ConfigurationSetName = field("ConfigurationSetName")
    EndpointId = field("EndpointId")
    TenantName = field("TenantName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendBulkEmailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendBulkEmailRequestTypeDef"]
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
    def Content(self):  # pragma: no cover
        return EmailContent.make_one(self.boto3_raw_data["Content"])

    FromEmailAddress = field("FromEmailAddress")
    FromEmailAddressIdentityArn = field("FromEmailAddressIdentityArn")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    ReplyToAddresses = field("ReplyToAddresses")
    FeedbackForwardingEmailAddress = field("FeedbackForwardingEmailAddress")
    FeedbackForwardingEmailAddressIdentityArn = field(
        "FeedbackForwardingEmailAddressIdentityArn"
    )

    @cached_property
    def EmailTags(self):  # pragma: no cover
        return MessageTag.make_many(self.boto3_raw_data["EmailTags"])

    ConfigurationSetName = field("ConfigurationSetName")
    EndpointId = field("EndpointId")
    TenantName = field("TenantName")

    @cached_property
    def ListManagementOptions(self):  # pragma: no cover
        return ListManagementOptions.make_one(
            self.boto3_raw_data["ListManagementOptions"]
        )

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
class GetMessageInsightsResponse:
    boto3_raw_data: "type_defs.GetMessageInsightsResponseTypeDef" = dataclasses.field()

    MessageId = field("MessageId")
    FromEmailAddress = field("FromEmailAddress")
    Subject = field("Subject")

    @cached_property
    def EmailTags(self):  # pragma: no cover
        return MessageTag.make_many(self.boto3_raw_data["EmailTags"])

    @cached_property
    def Insights(self):  # pragma: no cover
        return EmailInsights.make_many(self.boto3_raw_data["Insights"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMessageInsightsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMessageInsightsResponseTypeDef"]
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


@dataclasses.dataclass(frozen=True)
class CreateExportJobRequest:
    boto3_raw_data: "type_defs.CreateExportJobRequestTypeDef" = dataclasses.field()

    ExportDataSource = field("ExportDataSource")

    @cached_property
    def ExportDestination(self):  # pragma: no cover
        return ExportDestination.make_one(self.boto3_raw_data["ExportDestination"])

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
