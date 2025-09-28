# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ses import type_defs as bs_td


class SESCaster:

    def create_custom_verification_email_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_custom_verification_email_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_verified_email_address(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_active_receipt_rule_set(
        self,
        res: "bs_td.DescribeActiveReceiptRuleSetResponseTypeDef",
    ) -> "dc_td.DescribeActiveReceiptRuleSetResponse":
        return dc_td.DescribeActiveReceiptRuleSetResponse.make_one(res)

    def describe_configuration_set(
        self,
        res: "bs_td.DescribeConfigurationSetResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationSetResponse":
        return dc_td.DescribeConfigurationSetResponse.make_one(res)

    def describe_receipt_rule(
        self,
        res: "bs_td.DescribeReceiptRuleResponseTypeDef",
    ) -> "dc_td.DescribeReceiptRuleResponse":
        return dc_td.DescribeReceiptRuleResponse.make_one(res)

    def describe_receipt_rule_set(
        self,
        res: "bs_td.DescribeReceiptRuleSetResponseTypeDef",
    ) -> "dc_td.DescribeReceiptRuleSetResponse":
        return dc_td.DescribeReceiptRuleSetResponse.make_one(res)

    def get_account_sending_enabled(
        self,
        res: "bs_td.GetAccountSendingEnabledResponseTypeDef",
    ) -> "dc_td.GetAccountSendingEnabledResponse":
        return dc_td.GetAccountSendingEnabledResponse.make_one(res)

    def get_custom_verification_email_template(
        self,
        res: "bs_td.GetCustomVerificationEmailTemplateResponseTypeDef",
    ) -> "dc_td.GetCustomVerificationEmailTemplateResponse":
        return dc_td.GetCustomVerificationEmailTemplateResponse.make_one(res)

    def get_identity_dkim_attributes(
        self,
        res: "bs_td.GetIdentityDkimAttributesResponseTypeDef",
    ) -> "dc_td.GetIdentityDkimAttributesResponse":
        return dc_td.GetIdentityDkimAttributesResponse.make_one(res)

    def get_identity_mail_from_domain_attributes(
        self,
        res: "bs_td.GetIdentityMailFromDomainAttributesResponseTypeDef",
    ) -> "dc_td.GetIdentityMailFromDomainAttributesResponse":
        return dc_td.GetIdentityMailFromDomainAttributesResponse.make_one(res)

    def get_identity_notification_attributes(
        self,
        res: "bs_td.GetIdentityNotificationAttributesResponseTypeDef",
    ) -> "dc_td.GetIdentityNotificationAttributesResponse":
        return dc_td.GetIdentityNotificationAttributesResponse.make_one(res)

    def get_identity_policies(
        self,
        res: "bs_td.GetIdentityPoliciesResponseTypeDef",
    ) -> "dc_td.GetIdentityPoliciesResponse":
        return dc_td.GetIdentityPoliciesResponse.make_one(res)

    def get_identity_verification_attributes(
        self,
        res: "bs_td.GetIdentityVerificationAttributesResponseTypeDef",
    ) -> "dc_td.GetIdentityVerificationAttributesResponse":
        return dc_td.GetIdentityVerificationAttributesResponse.make_one(res)

    def get_send_quota(
        self,
        res: "bs_td.GetSendQuotaResponseTypeDef",
    ) -> "dc_td.GetSendQuotaResponse":
        return dc_td.GetSendQuotaResponse.make_one(res)

    def get_send_statistics(
        self,
        res: "bs_td.GetSendStatisticsResponseTypeDef",
    ) -> "dc_td.GetSendStatisticsResponse":
        return dc_td.GetSendStatisticsResponse.make_one(res)

    def get_template(
        self,
        res: "bs_td.GetTemplateResponseTypeDef",
    ) -> "dc_td.GetTemplateResponse":
        return dc_td.GetTemplateResponse.make_one(res)

    def list_configuration_sets(
        self,
        res: "bs_td.ListConfigurationSetsResponseTypeDef",
    ) -> "dc_td.ListConfigurationSetsResponse":
        return dc_td.ListConfigurationSetsResponse.make_one(res)

    def list_custom_verification_email_templates(
        self,
        res: "bs_td.ListCustomVerificationEmailTemplatesResponseTypeDef",
    ) -> "dc_td.ListCustomVerificationEmailTemplatesResponse":
        return dc_td.ListCustomVerificationEmailTemplatesResponse.make_one(res)

    def list_identities(
        self,
        res: "bs_td.ListIdentitiesResponseTypeDef",
    ) -> "dc_td.ListIdentitiesResponse":
        return dc_td.ListIdentitiesResponse.make_one(res)

    def list_identity_policies(
        self,
        res: "bs_td.ListIdentityPoliciesResponseTypeDef",
    ) -> "dc_td.ListIdentityPoliciesResponse":
        return dc_td.ListIdentityPoliciesResponse.make_one(res)

    def list_receipt_filters(
        self,
        res: "bs_td.ListReceiptFiltersResponseTypeDef",
    ) -> "dc_td.ListReceiptFiltersResponse":
        return dc_td.ListReceiptFiltersResponse.make_one(res)

    def list_receipt_rule_sets(
        self,
        res: "bs_td.ListReceiptRuleSetsResponseTypeDef",
    ) -> "dc_td.ListReceiptRuleSetsResponse":
        return dc_td.ListReceiptRuleSetsResponse.make_one(res)

    def list_templates(
        self,
        res: "bs_td.ListTemplatesResponseTypeDef",
    ) -> "dc_td.ListTemplatesResponse":
        return dc_td.ListTemplatesResponse.make_one(res)

    def list_verified_email_addresses(
        self,
        res: "bs_td.ListVerifiedEmailAddressesResponseTypeDef",
    ) -> "dc_td.ListVerifiedEmailAddressesResponse":
        return dc_td.ListVerifiedEmailAddressesResponse.make_one(res)

    def send_bounce(
        self,
        res: "bs_td.SendBounceResponseTypeDef",
    ) -> "dc_td.SendBounceResponse":
        return dc_td.SendBounceResponse.make_one(res)

    def send_bulk_templated_email(
        self,
        res: "bs_td.SendBulkTemplatedEmailResponseTypeDef",
    ) -> "dc_td.SendBulkTemplatedEmailResponse":
        return dc_td.SendBulkTemplatedEmailResponse.make_one(res)

    def send_custom_verification_email(
        self,
        res: "bs_td.SendCustomVerificationEmailResponseTypeDef",
    ) -> "dc_td.SendCustomVerificationEmailResponse":
        return dc_td.SendCustomVerificationEmailResponse.make_one(res)

    def send_email(
        self,
        res: "bs_td.SendEmailResponseTypeDef",
    ) -> "dc_td.SendEmailResponse":
        return dc_td.SendEmailResponse.make_one(res)

    def send_raw_email(
        self,
        res: "bs_td.SendRawEmailResponseTypeDef",
    ) -> "dc_td.SendRawEmailResponse":
        return dc_td.SendRawEmailResponse.make_one(res)

    def send_templated_email(
        self,
        res: "bs_td.SendTemplatedEmailResponseTypeDef",
    ) -> "dc_td.SendTemplatedEmailResponse":
        return dc_td.SendTemplatedEmailResponse.make_one(res)

    def test_render_template(
        self,
        res: "bs_td.TestRenderTemplateResponseTypeDef",
    ) -> "dc_td.TestRenderTemplateResponse":
        return dc_td.TestRenderTemplateResponse.make_one(res)

    def update_account_sending_enabled(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_configuration_set_reputation_metrics_enabled(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_configuration_set_sending_enabled(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_custom_verification_email_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def verify_domain_dkim(
        self,
        res: "bs_td.VerifyDomainDkimResponseTypeDef",
    ) -> "dc_td.VerifyDomainDkimResponse":
        return dc_td.VerifyDomainDkimResponse.make_one(res)

    def verify_domain_identity(
        self,
        res: "bs_td.VerifyDomainIdentityResponseTypeDef",
    ) -> "dc_td.VerifyDomainIdentityResponse":
        return dc_td.VerifyDomainIdentityResponse.make_one(res)

    def verify_email_address(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


ses_caster = SESCaster()
