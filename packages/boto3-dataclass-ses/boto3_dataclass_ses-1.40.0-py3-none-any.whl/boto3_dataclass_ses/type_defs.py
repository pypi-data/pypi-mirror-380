# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ses import type_defs


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
class BounceAction:
    boto3_raw_data: "type_defs.BounceActionTypeDef" = dataclasses.field()

    SmtpReplyCode = field("SmtpReplyCode")
    Message = field("Message")
    Sender = field("Sender")
    TopicArn = field("TopicArn")
    StatusCode = field("StatusCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BounceActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BounceActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BulkEmailDestinationStatus:
    boto3_raw_data: "type_defs.BulkEmailDestinationStatusTypeDef" = dataclasses.field()

    Status = field("Status")
    Error = field("Error")
    MessageId = field("MessageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BulkEmailDestinationStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BulkEmailDestinationStatusTypeDef"]
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
class CloneReceiptRuleSetRequest:
    boto3_raw_data: "type_defs.CloneReceiptRuleSetRequestTypeDef" = dataclasses.field()

    RuleSetName = field("RuleSetName")
    OriginalRuleSetName = field("OriginalRuleSetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloneReceiptRuleSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloneReceiptRuleSetRequestTypeDef"]
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
class ConfigurationSet:
    boto3_raw_data: "type_defs.ConfigurationSetTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectAction:
    boto3_raw_data: "type_defs.ConnectActionTypeDef" = dataclasses.field()

    InstanceARN = field("InstanceARN")
    IAMRoleARN = field("IAMRoleARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectActionTypeDef"]],
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
class CreateReceiptRuleSetRequest:
    boto3_raw_data: "type_defs.CreateReceiptRuleSetRequestTypeDef" = dataclasses.field()

    RuleSetName = field("RuleSetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReceiptRuleSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReceiptRuleSetRequestTypeDef"]
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
    SubjectPart = field("SubjectPart")
    TextPart = field("TextPart")
    HtmlPart = field("HtmlPart")

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
class CustomVerificationEmailTemplate:
    boto3_raw_data: "type_defs.CustomVerificationEmailTemplateTypeDef" = (
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
        boto3_raw_data: T.Optional["type_defs.CustomVerificationEmailTemplateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomVerificationEmailTemplateTypeDef"]
        ],
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
class DeleteConfigurationSetTrackingOptionsRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationSetTrackingOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfigurationSetTrackingOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationSetTrackingOptionsRequestTypeDef"]
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
class DeleteIdentityPolicyRequest:
    boto3_raw_data: "type_defs.DeleteIdentityPolicyRequestTypeDef" = dataclasses.field()

    Identity = field("Identity")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdentityPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentityPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdentityRequest:
    boto3_raw_data: "type_defs.DeleteIdentityRequestTypeDef" = dataclasses.field()

    Identity = field("Identity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdentityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReceiptFilterRequest:
    boto3_raw_data: "type_defs.DeleteReceiptFilterRequestTypeDef" = dataclasses.field()

    FilterName = field("FilterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReceiptFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReceiptFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReceiptRuleRequest:
    boto3_raw_data: "type_defs.DeleteReceiptRuleRequestTypeDef" = dataclasses.field()

    RuleSetName = field("RuleSetName")
    RuleName = field("RuleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReceiptRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReceiptRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReceiptRuleSetRequest:
    boto3_raw_data: "type_defs.DeleteReceiptRuleSetRequestTypeDef" = dataclasses.field()

    RuleSetName = field("RuleSetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReceiptRuleSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReceiptRuleSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTemplateRequest:
    boto3_raw_data: "type_defs.DeleteTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVerifiedEmailAddressRequest:
    boto3_raw_data: "type_defs.DeleteVerifiedEmailAddressRequestTypeDef" = (
        dataclasses.field()
    )

    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVerifiedEmailAddressRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVerifiedEmailAddressRequestTypeDef"]
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
class ReceiptRuleSetMetadata:
    boto3_raw_data: "type_defs.ReceiptRuleSetMetadataTypeDef" = dataclasses.field()

    Name = field("Name")
    CreatedTimestamp = field("CreatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReceiptRuleSetMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReceiptRuleSetMetadataTypeDef"]
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
class DescribeConfigurationSetRequest:
    boto3_raw_data: "type_defs.DescribeConfigurationSetRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    ConfigurationSetAttributeNames = field("ConfigurationSetAttributeNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConfigurationSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationSetRequestTypeDef"]
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

    SendingEnabled = field("SendingEnabled")
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
class DescribeReceiptRuleRequest:
    boto3_raw_data: "type_defs.DescribeReceiptRuleRequestTypeDef" = dataclasses.field()

    RuleSetName = field("RuleSetName")
    RuleName = field("RuleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReceiptRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReceiptRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReceiptRuleSetRequest:
    boto3_raw_data: "type_defs.DescribeReceiptRuleSetRequestTypeDef" = (
        dataclasses.field()
    )

    RuleSetName = field("RuleSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeReceiptRuleSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReceiptRuleSetRequestTypeDef"]
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

    IAMRoleARN = field("IAMRoleARN")
    DeliveryStreamARN = field("DeliveryStreamARN")

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
class SNSDestination:
    boto3_raw_data: "type_defs.SNSDestinationTypeDef" = dataclasses.field()

    TopicARN = field("TopicARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SNSDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SNSDestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionField:
    boto3_raw_data: "type_defs.ExtensionFieldTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtensionFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtensionFieldTypeDef"]],
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
class GetIdentityDkimAttributesRequest:
    boto3_raw_data: "type_defs.GetIdentityDkimAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    Identities = field("Identities")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIdentityDkimAttributesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityDkimAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityDkimAttributes:
    boto3_raw_data: "type_defs.IdentityDkimAttributesTypeDef" = dataclasses.field()

    DkimEnabled = field("DkimEnabled")
    DkimVerificationStatus = field("DkimVerificationStatus")
    DkimTokens = field("DkimTokens")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityDkimAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityDkimAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityMailFromDomainAttributesRequest:
    boto3_raw_data: "type_defs.GetIdentityMailFromDomainAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    Identities = field("Identities")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityMailFromDomainAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityMailFromDomainAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityMailFromDomainAttributes:
    boto3_raw_data: "type_defs.IdentityMailFromDomainAttributesTypeDef" = (
        dataclasses.field()
    )

    MailFromDomain = field("MailFromDomain")
    MailFromDomainStatus = field("MailFromDomainStatus")
    BehaviorOnMXFailure = field("BehaviorOnMXFailure")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdentityMailFromDomainAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityMailFromDomainAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityNotificationAttributesRequest:
    boto3_raw_data: "type_defs.GetIdentityNotificationAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    Identities = field("Identities")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityNotificationAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityNotificationAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityNotificationAttributes:
    boto3_raw_data: "type_defs.IdentityNotificationAttributesTypeDef" = (
        dataclasses.field()
    )

    BounceTopic = field("BounceTopic")
    ComplaintTopic = field("ComplaintTopic")
    DeliveryTopic = field("DeliveryTopic")
    ForwardingEnabled = field("ForwardingEnabled")
    HeadersInBounceNotificationsEnabled = field("HeadersInBounceNotificationsEnabled")
    HeadersInComplaintNotificationsEnabled = field(
        "HeadersInComplaintNotificationsEnabled"
    )
    HeadersInDeliveryNotificationsEnabled = field(
        "HeadersInDeliveryNotificationsEnabled"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdentityNotificationAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityNotificationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityPoliciesRequest:
    boto3_raw_data: "type_defs.GetIdentityPoliciesRequestTypeDef" = dataclasses.field()

    Identity = field("Identity")
    PolicyNames = field("PolicyNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdentityPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityVerificationAttributesRequest:
    boto3_raw_data: "type_defs.GetIdentityVerificationAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    Identities = field("Identities")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityVerificationAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityVerificationAttributesRequestTypeDef"]
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
class IdentityVerificationAttributes:
    boto3_raw_data: "type_defs.IdentityVerificationAttributesTypeDef" = (
        dataclasses.field()
    )

    VerificationStatus = field("VerificationStatus")
    VerificationToken = field("VerificationToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdentityVerificationAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityVerificationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendDataPoint:
    boto3_raw_data: "type_defs.SendDataPointTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    DeliveryAttempts = field("DeliveryAttempts")
    Bounces = field("Bounces")
    Complaints = field("Complaints")
    Rejects = field("Rejects")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendDataPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SendDataPointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateRequest:
    boto3_raw_data: "type_defs.GetTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaAction:
    boto3_raw_data: "type_defs.LambdaActionTypeDef" = dataclasses.field()

    FunctionArn = field("FunctionArn")
    TopicArn = field("TopicArn")
    InvocationType = field("InvocationType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaActionTypeDef"]],
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
class ListConfigurationSetsRequest:
    boto3_raw_data: "type_defs.ListConfigurationSetsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxItems = field("MaxItems")

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
class ListCustomVerificationEmailTemplatesRequest:
    boto3_raw_data: "type_defs.ListCustomVerificationEmailTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

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
class ListIdentitiesRequest:
    boto3_raw_data: "type_defs.ListIdentitiesRequestTypeDef" = dataclasses.field()

    IdentityType = field("IdentityType")
    NextToken = field("NextToken")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityPoliciesRequest:
    boto3_raw_data: "type_defs.ListIdentityPoliciesRequestTypeDef" = dataclasses.field()

    Identity = field("Identity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentityPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceiptRuleSetsRequest:
    boto3_raw_data: "type_defs.ListReceiptRuleSetsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReceiptRuleSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceiptRuleSetsRequestTypeDef"]
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
    MaxItems = field("MaxItems")

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
class TemplateMetadata:
    boto3_raw_data: "type_defs.TemplateMetadataTypeDef" = dataclasses.field()

    Name = field("Name")
    CreatedTimestamp = field("CreatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIdentityPolicyRequest:
    boto3_raw_data: "type_defs.PutIdentityPolicyRequestTypeDef" = dataclasses.field()

    Identity = field("Identity")
    PolicyName = field("PolicyName")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutIdentityPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIdentityPolicyRequestTypeDef"]
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

    BucketName = field("BucketName")
    TopicArn = field("TopicArn")
    ObjectKeyPrefix = field("ObjectKeyPrefix")
    KmsKeyArn = field("KmsKeyArn")
    IamRoleArn = field("IamRoleArn")

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
class SNSAction:
    boto3_raw_data: "type_defs.SNSActionTypeDef" = dataclasses.field()

    TopicArn = field("TopicArn")
    Encoding = field("Encoding")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SNSActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SNSActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopAction:
    boto3_raw_data: "type_defs.StopActionTypeDef" = dataclasses.field()

    Scope = field("Scope")
    TopicArn = field("TopicArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkmailAction:
    boto3_raw_data: "type_defs.WorkmailActionTypeDef" = dataclasses.field()

    OrganizationArn = field("OrganizationArn")
    TopicArn = field("TopicArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkmailActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkmailActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceiptIpFilter:
    boto3_raw_data: "type_defs.ReceiptIpFilterTypeDef" = dataclasses.field()

    Policy = field("Policy")
    Cidr = field("Cidr")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReceiptIpFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReceiptIpFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReorderReceiptRuleSetRequest:
    boto3_raw_data: "type_defs.ReorderReceiptRuleSetRequestTypeDef" = (
        dataclasses.field()
    )

    RuleSetName = field("RuleSetName")
    RuleNames = field("RuleNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReorderReceiptRuleSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReorderReceiptRuleSetRequestTypeDef"]
        ],
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
class SetActiveReceiptRuleSetRequest:
    boto3_raw_data: "type_defs.SetActiveReceiptRuleSetRequestTypeDef" = (
        dataclasses.field()
    )

    RuleSetName = field("RuleSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetActiveReceiptRuleSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetActiveReceiptRuleSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIdentityDkimEnabledRequest:
    boto3_raw_data: "type_defs.SetIdentityDkimEnabledRequestTypeDef" = (
        dataclasses.field()
    )

    Identity = field("Identity")
    DkimEnabled = field("DkimEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetIdentityDkimEnabledRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIdentityDkimEnabledRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIdentityFeedbackForwardingEnabledRequest:
    boto3_raw_data: "type_defs.SetIdentityFeedbackForwardingEnabledRequestTypeDef" = (
        dataclasses.field()
    )

    Identity = field("Identity")
    ForwardingEnabled = field("ForwardingEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetIdentityFeedbackForwardingEnabledRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIdentityFeedbackForwardingEnabledRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIdentityHeadersInNotificationsEnabledRequest:
    boto3_raw_data: (
        "type_defs.SetIdentityHeadersInNotificationsEnabledRequestTypeDef"
    ) = dataclasses.field()

    Identity = field("Identity")
    NotificationType = field("NotificationType")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetIdentityHeadersInNotificationsEnabledRequestTypeDef"
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
                "type_defs.SetIdentityHeadersInNotificationsEnabledRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIdentityMailFromDomainRequest:
    boto3_raw_data: "type_defs.SetIdentityMailFromDomainRequestTypeDef" = (
        dataclasses.field()
    )

    Identity = field("Identity")
    MailFromDomain = field("MailFromDomain")
    BehaviorOnMXFailure = field("BehaviorOnMXFailure")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetIdentityMailFromDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIdentityMailFromDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIdentityNotificationTopicRequest:
    boto3_raw_data: "type_defs.SetIdentityNotificationTopicRequestTypeDef" = (
        dataclasses.field()
    )

    Identity = field("Identity")
    NotificationType = field("NotificationType")
    SnsTopic = field("SnsTopic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetIdentityNotificationTopicRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIdentityNotificationTopicRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetReceiptRulePositionRequest:
    boto3_raw_data: "type_defs.SetReceiptRulePositionRequestTypeDef" = (
        dataclasses.field()
    )

    RuleSetName = field("RuleSetName")
    RuleName = field("RuleName")
    After = field("After")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetReceiptRulePositionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetReceiptRulePositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestRenderTemplateRequest:
    boto3_raw_data: "type_defs.TestRenderTemplateRequestTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    TemplateData = field("TemplateData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestRenderTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestRenderTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountSendingEnabledRequest:
    boto3_raw_data: "type_defs.UpdateAccountSendingEnabledRequestTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccountSendingEnabledRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountSendingEnabledRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationSetReputationMetricsEnabledRequest:
    boto3_raw_data: (
        "type_defs.UpdateConfigurationSetReputationMetricsEnabledRequestTypeDef"
    ) = dataclasses.field()

    ConfigurationSetName = field("ConfigurationSetName")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfigurationSetReputationMetricsEnabledRequestTypeDef"
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
                "type_defs.UpdateConfigurationSetReputationMetricsEnabledRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationSetSendingEnabledRequest:
    boto3_raw_data: "type_defs.UpdateConfigurationSetSendingEnabledRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfigurationSetSendingEnabledRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationSetSendingEnabledRequestTypeDef"]
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
class VerifyDomainDkimRequest:
    boto3_raw_data: "type_defs.VerifyDomainDkimRequestTypeDef" = dataclasses.field()

    Domain = field("Domain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyDomainDkimRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyDomainDkimRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyDomainIdentityRequest:
    boto3_raw_data: "type_defs.VerifyDomainIdentityRequestTypeDef" = dataclasses.field()

    Domain = field("Domain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyDomainIdentityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyDomainIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyEmailAddressRequest:
    boto3_raw_data: "type_defs.VerifyEmailAddressRequestTypeDef" = dataclasses.field()

    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyEmailAddressRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyEmailAddressRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyEmailIdentityRequest:
    boto3_raw_data: "type_defs.VerifyEmailIdentityRequestTypeDef" = dataclasses.field()

    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyEmailIdentityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyEmailIdentityRequestTypeDef"]
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
class BulkEmailDestination:
    boto3_raw_data: "type_defs.BulkEmailDestinationTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def ReplacementTags(self):  # pragma: no cover
        return MessageTag.make_many(self.boto3_raw_data["ReplacementTags"])

    ReplacementTemplateData = field("ReplacementTemplateData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BulkEmailDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BulkEmailDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendTemplatedEmailRequest:
    boto3_raw_data: "type_defs.SendTemplatedEmailRequestTypeDef" = dataclasses.field()

    Source = field("Source")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    Template = field("Template")
    TemplateData = field("TemplateData")
    ReplyToAddresses = field("ReplyToAddresses")
    ReturnPath = field("ReturnPath")
    SourceArn = field("SourceArn")
    ReturnPathArn = field("ReturnPathArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return MessageTag.make_many(self.boto3_raw_data["Tags"])

    ConfigurationSetName = field("ConfigurationSetName")
    TemplateArn = field("TemplateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendTemplatedEmailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendTemplatedEmailRequestTypeDef"]
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
class CreateConfigurationSetRequest:
    boto3_raw_data: "type_defs.CreateConfigurationSetRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationSet(self):  # pragma: no cover
        return ConfigurationSet.make_one(self.boto3_raw_data["ConfigurationSet"])

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
class CreateConfigurationSetTrackingOptionsRequest:
    boto3_raw_data: "type_defs.CreateConfigurationSetTrackingOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def TrackingOptions(self):  # pragma: no cover
        return TrackingOptions.make_one(self.boto3_raw_data["TrackingOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfigurationSetTrackingOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationSetTrackingOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationSetTrackingOptionsRequest:
    boto3_raw_data: "type_defs.UpdateConfigurationSetTrackingOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def TrackingOptions(self):  # pragma: no cover
        return TrackingOptions.make_one(self.boto3_raw_data["TrackingOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfigurationSetTrackingOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationSetTrackingOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateRequest:
    boto3_raw_data: "type_defs.CreateTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def Template(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["Template"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTemplateRequest:
    boto3_raw_data: "type_defs.UpdateTemplateRequestTypeDef" = dataclasses.field()

    @cached_property
    def Template(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["Template"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTemplateRequestTypeDef"]
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

    @cached_property
    def DeliveryOptions(self):  # pragma: no cover
        return DeliveryOptions.make_one(self.boto3_raw_data["DeliveryOptions"])

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
class GetAccountSendingEnabledResponse:
    boto3_raw_data: "type_defs.GetAccountSendingEnabledResponseTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccountSendingEnabledResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountSendingEnabledResponseTypeDef"]
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
class GetIdentityPoliciesResponse:
    boto3_raw_data: "type_defs.GetIdentityPoliciesResponseTypeDef" = dataclasses.field()

    Policies = field("Policies")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdentityPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSendQuotaResponse:
    boto3_raw_data: "type_defs.GetSendQuotaResponseTypeDef" = dataclasses.field()

    Max24HourSend = field("Max24HourSend")
    MaxSendRate = field("MaxSendRate")
    SentLast24Hours = field("SentLast24Hours")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSendQuotaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSendQuotaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateResponse:
    boto3_raw_data: "type_defs.GetTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def Template(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["Template"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateResponseTypeDef"]
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

    @cached_property
    def ConfigurationSets(self):  # pragma: no cover
        return ConfigurationSet.make_many(self.boto3_raw_data["ConfigurationSets"])

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
class ListCustomVerificationEmailTemplatesResponse:
    boto3_raw_data: "type_defs.ListCustomVerificationEmailTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CustomVerificationEmailTemplates(self):  # pragma: no cover
        return CustomVerificationEmailTemplate.make_many(
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
class ListIdentitiesResponse:
    boto3_raw_data: "type_defs.ListIdentitiesResponseTypeDef" = dataclasses.field()

    Identities = field("Identities")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityPoliciesResponse:
    boto3_raw_data: "type_defs.ListIdentityPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    PolicyNames = field("PolicyNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentityPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceiptRuleSetsResponse:
    boto3_raw_data: "type_defs.ListReceiptRuleSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def RuleSets(self):  # pragma: no cover
        return ReceiptRuleSetMetadata.make_many(self.boto3_raw_data["RuleSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReceiptRuleSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceiptRuleSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVerifiedEmailAddressesResponse:
    boto3_raw_data: "type_defs.ListVerifiedEmailAddressesResponseTypeDef" = (
        dataclasses.field()
    )

    VerifiedEmailAddresses = field("VerifiedEmailAddresses")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVerifiedEmailAddressesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVerifiedEmailAddressesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendBounceResponse:
    boto3_raw_data: "type_defs.SendBounceResponseTypeDef" = dataclasses.field()

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendBounceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendBounceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendBulkTemplatedEmailResponse:
    boto3_raw_data: "type_defs.SendBulkTemplatedEmailResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Status(self):  # pragma: no cover
        return BulkEmailDestinationStatus.make_many(self.boto3_raw_data["Status"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendBulkTemplatedEmailResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendBulkTemplatedEmailResponseTypeDef"]
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
class SendRawEmailResponse:
    boto3_raw_data: "type_defs.SendRawEmailResponseTypeDef" = dataclasses.field()

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendRawEmailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendRawEmailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendTemplatedEmailResponse:
    boto3_raw_data: "type_defs.SendTemplatedEmailResponseTypeDef" = dataclasses.field()

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendTemplatedEmailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendTemplatedEmailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestRenderTemplateResponse:
    boto3_raw_data: "type_defs.TestRenderTemplateResponseTypeDef" = dataclasses.field()

    RenderedTemplate = field("RenderedTemplate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestRenderTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestRenderTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyDomainDkimResponse:
    boto3_raw_data: "type_defs.VerifyDomainDkimResponseTypeDef" = dataclasses.field()

    DkimTokens = field("DkimTokens")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyDomainDkimResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyDomainDkimResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyDomainIdentityResponse:
    boto3_raw_data: "type_defs.VerifyDomainIdentityResponseTypeDef" = (
        dataclasses.field()
    )

    VerificationToken = field("VerificationToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyDomainIdentityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyDomainIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityDkimAttributesResponse:
    boto3_raw_data: "type_defs.GetIdentityDkimAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    DkimAttributes = field("DkimAttributes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityDkimAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityDkimAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityMailFromDomainAttributesResponse:
    boto3_raw_data: "type_defs.GetIdentityMailFromDomainAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    MailFromDomainAttributes = field("MailFromDomainAttributes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityMailFromDomainAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityMailFromDomainAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityNotificationAttributesResponse:
    boto3_raw_data: "type_defs.GetIdentityNotificationAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    NotificationAttributes = field("NotificationAttributes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityNotificationAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityNotificationAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityVerificationAttributesRequestWait:
    boto3_raw_data: "type_defs.GetIdentityVerificationAttributesRequestWaitTypeDef" = (
        dataclasses.field()
    )

    Identities = field("Identities")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityVerificationAttributesRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityVerificationAttributesRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityVerificationAttributesResponse:
    boto3_raw_data: "type_defs.GetIdentityVerificationAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    VerificationAttributes = field("VerificationAttributes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityVerificationAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityVerificationAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSendStatisticsResponse:
    boto3_raw_data: "type_defs.GetSendStatisticsResponseTypeDef" = dataclasses.field()

    @cached_property
    def SendDataPoints(self):  # pragma: no cover
        return SendDataPoint.make_many(self.boto3_raw_data["SendDataPoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSendStatisticsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSendStatisticsResponseTypeDef"]
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
class ListCustomVerificationEmailTemplatesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListCustomVerificationEmailTemplatesRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomVerificationEmailTemplatesRequestPaginateTypeDef"
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
                "type_defs.ListCustomVerificationEmailTemplatesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentitiesRequestPaginate:
    boto3_raw_data: "type_defs.ListIdentitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    IdentityType = field("IdentityType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdentitiesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceiptRuleSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListReceiptRuleSetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReceiptRuleSetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceiptRuleSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplatesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplatesRequestPaginateTypeDef"]
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
    def TemplatesMetadata(self):  # pragma: no cover
        return TemplateMetadata.make_many(self.boto3_raw_data["TemplatesMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class MessageDsn:
    boto3_raw_data: "type_defs.MessageDsnTypeDef" = dataclasses.field()

    ReportingMta = field("ReportingMta")
    ArrivalDate = field("ArrivalDate")

    @cached_property
    def ExtensionFields(self):  # pragma: no cover
        return ExtensionField.make_many(self.boto3_raw_data["ExtensionFields"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageDsnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageDsnTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipientDsnFields:
    boto3_raw_data: "type_defs.RecipientDsnFieldsTypeDef" = dataclasses.field()

    Action = field("Action")
    Status = field("Status")
    FinalRecipient = field("FinalRecipient")
    RemoteMta = field("RemoteMta")
    DiagnosticCode = field("DiagnosticCode")
    LastAttemptDate = field("LastAttemptDate")

    @cached_property
    def ExtensionFields(self):  # pragma: no cover
        return ExtensionField.make_many(self.boto3_raw_data["ExtensionFields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecipientDsnFieldsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecipientDsnFieldsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceiptAction:
    boto3_raw_data: "type_defs.ReceiptActionTypeDef" = dataclasses.field()

    @cached_property
    def S3Action(self):  # pragma: no cover
        return S3Action.make_one(self.boto3_raw_data["S3Action"])

    @cached_property
    def BounceAction(self):  # pragma: no cover
        return BounceAction.make_one(self.boto3_raw_data["BounceAction"])

    @cached_property
    def WorkmailAction(self):  # pragma: no cover
        return WorkmailAction.make_one(self.boto3_raw_data["WorkmailAction"])

    @cached_property
    def LambdaAction(self):  # pragma: no cover
        return LambdaAction.make_one(self.boto3_raw_data["LambdaAction"])

    @cached_property
    def StopAction(self):  # pragma: no cover
        return StopAction.make_one(self.boto3_raw_data["StopAction"])

    @cached_property
    def AddHeaderAction(self):  # pragma: no cover
        return AddHeaderAction.make_one(self.boto3_raw_data["AddHeaderAction"])

    @cached_property
    def SNSAction(self):  # pragma: no cover
        return SNSAction.make_one(self.boto3_raw_data["SNSAction"])

    @cached_property
    def ConnectAction(self):  # pragma: no cover
        return ConnectAction.make_one(self.boto3_raw_data["ConnectAction"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReceiptActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReceiptActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceiptFilter:
    boto3_raw_data: "type_defs.ReceiptFilterTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def IpFilter(self):  # pragma: no cover
        return ReceiptIpFilter.make_one(self.boto3_raw_data["IpFilter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReceiptFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReceiptFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendRawEmailRequest:
    boto3_raw_data: "type_defs.SendRawEmailRequestTypeDef" = dataclasses.field()

    @cached_property
    def RawMessage(self):  # pragma: no cover
        return RawMessage.make_one(self.boto3_raw_data["RawMessage"])

    Source = field("Source")
    Destinations = field("Destinations")
    FromArn = field("FromArn")
    SourceArn = field("SourceArn")
    ReturnPathArn = field("ReturnPathArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return MessageTag.make_many(self.boto3_raw_data["Tags"])

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendRawEmailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendRawEmailRequestTypeDef"]
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
class SendBulkTemplatedEmailRequest:
    boto3_raw_data: "type_defs.SendBulkTemplatedEmailRequestTypeDef" = (
        dataclasses.field()
    )

    Source = field("Source")
    Template = field("Template")
    DefaultTemplateData = field("DefaultTemplateData")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return BulkEmailDestination.make_many(self.boto3_raw_data["Destinations"])

    SourceArn = field("SourceArn")
    ReplyToAddresses = field("ReplyToAddresses")
    ReturnPath = field("ReturnPath")
    ReturnPathArn = field("ReturnPathArn")
    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def DefaultTags(self):  # pragma: no cover
        return MessageTag.make_many(self.boto3_raw_data["DefaultTags"])

    TemplateArn = field("TemplateArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendBulkTemplatedEmailRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendBulkTemplatedEmailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDestinationOutput:
    boto3_raw_data: "type_defs.EventDestinationOutputTypeDef" = dataclasses.field()

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
    def SNSDestination(self):  # pragma: no cover
        return SNSDestination.make_one(self.boto3_raw_data["SNSDestination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventDestinationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDestinationOutputTypeDef"]
        ],
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
        return CloudWatchDestination.make_one(
            self.boto3_raw_data["CloudWatchDestination"]
        )

    @cached_property
    def SNSDestination(self):  # pragma: no cover
        return SNSDestination.make_one(self.boto3_raw_data["SNSDestination"])

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
class BouncedRecipientInfo:
    boto3_raw_data: "type_defs.BouncedRecipientInfoTypeDef" = dataclasses.field()

    Recipient = field("Recipient")
    RecipientArn = field("RecipientArn")
    BounceType = field("BounceType")

    @cached_property
    def RecipientDsnFields(self):  # pragma: no cover
        return RecipientDsnFields.make_one(self.boto3_raw_data["RecipientDsnFields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BouncedRecipientInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BouncedRecipientInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceiptRuleOutput:
    boto3_raw_data: "type_defs.ReceiptRuleOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Enabled = field("Enabled")
    TlsPolicy = field("TlsPolicy")
    Recipients = field("Recipients")

    @cached_property
    def Actions(self):  # pragma: no cover
        return ReceiptAction.make_many(self.boto3_raw_data["Actions"])

    ScanEnabled = field("ScanEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReceiptRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReceiptRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceiptRule:
    boto3_raw_data: "type_defs.ReceiptRuleTypeDef" = dataclasses.field()

    Name = field("Name")
    Enabled = field("Enabled")
    TlsPolicy = field("TlsPolicy")
    Recipients = field("Recipients")

    @cached_property
    def Actions(self):  # pragma: no cover
        return ReceiptAction.make_many(self.boto3_raw_data["Actions"])

    ScanEnabled = field("ScanEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReceiptRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReceiptRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReceiptFilterRequest:
    boto3_raw_data: "type_defs.CreateReceiptFilterRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filter(self):  # pragma: no cover
        return ReceiptFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReceiptFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReceiptFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceiptFiltersResponse:
    boto3_raw_data: "type_defs.ListReceiptFiltersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return ReceiptFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReceiptFiltersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceiptFiltersResponseTypeDef"]
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

    Source = field("Source")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def Message(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["Message"])

    ReplyToAddresses = field("ReplyToAddresses")
    ReturnPath = field("ReturnPath")
    SourceArn = field("SourceArn")
    ReturnPathArn = field("ReturnPathArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return MessageTag.make_many(self.boto3_raw_data["Tags"])

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
class DescribeConfigurationSetResponse:
    boto3_raw_data: "type_defs.DescribeConfigurationSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationSet(self):  # pragma: no cover
        return ConfigurationSet.make_one(self.boto3_raw_data["ConfigurationSet"])

    @cached_property
    def EventDestinations(self):  # pragma: no cover
        return EventDestinationOutput.make_many(
            self.boto3_raw_data["EventDestinations"]
        )

    @cached_property
    def TrackingOptions(self):  # pragma: no cover
        return TrackingOptions.make_one(self.boto3_raw_data["TrackingOptions"])

    @cached_property
    def DeliveryOptions(self):  # pragma: no cover
        return DeliveryOptions.make_one(self.boto3_raw_data["DeliveryOptions"])

    @cached_property
    def ReputationOptions(self):  # pragma: no cover
        return ReputationOptions.make_one(self.boto3_raw_data["ReputationOptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConfigurationSetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendBounceRequest:
    boto3_raw_data: "type_defs.SendBounceRequestTypeDef" = dataclasses.field()

    OriginalMessageId = field("OriginalMessageId")
    BounceSender = field("BounceSender")

    @cached_property
    def BouncedRecipientInfoList(self):  # pragma: no cover
        return BouncedRecipientInfo.make_many(
            self.boto3_raw_data["BouncedRecipientInfoList"]
        )

    Explanation = field("Explanation")

    @cached_property
    def MessageDsn(self):  # pragma: no cover
        return MessageDsn.make_one(self.boto3_raw_data["MessageDsn"])

    BounceSenderArn = field("BounceSenderArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendBounceRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendBounceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActiveReceiptRuleSetResponse:
    boto3_raw_data: "type_defs.DescribeActiveReceiptRuleSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metadata(self):  # pragma: no cover
        return ReceiptRuleSetMetadata.make_one(self.boto3_raw_data["Metadata"])

    @cached_property
    def Rules(self):  # pragma: no cover
        return ReceiptRuleOutput.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeActiveReceiptRuleSetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActiveReceiptRuleSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReceiptRuleResponse:
    boto3_raw_data: "type_defs.DescribeReceiptRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Rule(self):  # pragma: no cover
        return ReceiptRuleOutput.make_one(self.boto3_raw_data["Rule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReceiptRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReceiptRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReceiptRuleSetResponse:
    boto3_raw_data: "type_defs.DescribeReceiptRuleSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metadata(self):  # pragma: no cover
        return ReceiptRuleSetMetadata.make_one(self.boto3_raw_data["Metadata"])

    @cached_property
    def Rules(self):  # pragma: no cover
        return ReceiptRuleOutput.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeReceiptRuleSetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReceiptRuleSetResponseTypeDef"]
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
    EventDestination = field("EventDestination")

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
    EventDestination = field("EventDestination")

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
class CreateReceiptRuleRequest:
    boto3_raw_data: "type_defs.CreateReceiptRuleRequestTypeDef" = dataclasses.field()

    RuleSetName = field("RuleSetName")
    Rule = field("Rule")
    After = field("After")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReceiptRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReceiptRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReceiptRuleRequest:
    boto3_raw_data: "type_defs.UpdateReceiptRuleRequestTypeDef" = dataclasses.field()

    RuleSetName = field("RuleSetName")
    Rule = field("Rule")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReceiptRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReceiptRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
