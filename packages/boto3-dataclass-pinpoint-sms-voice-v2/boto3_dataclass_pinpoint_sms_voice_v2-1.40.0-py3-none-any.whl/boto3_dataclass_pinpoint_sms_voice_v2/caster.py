# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pinpoint_sms_voice_v2 import type_defs as bs_td


class PINPOINT_SMS_VOICE_V2Caster:

    def associate_origination_identity(
        self,
        res: "bs_td.AssociateOriginationIdentityResultTypeDef",
    ) -> "dc_td.AssociateOriginationIdentityResult":
        return dc_td.AssociateOriginationIdentityResult.make_one(res)

    def associate_protect_configuration(
        self,
        res: "bs_td.AssociateProtectConfigurationResultTypeDef",
    ) -> "dc_td.AssociateProtectConfigurationResult":
        return dc_td.AssociateProtectConfigurationResult.make_one(res)

    def create_configuration_set(
        self,
        res: "bs_td.CreateConfigurationSetResultTypeDef",
    ) -> "dc_td.CreateConfigurationSetResult":
        return dc_td.CreateConfigurationSetResult.make_one(res)

    def create_event_destination(
        self,
        res: "bs_td.CreateEventDestinationResultTypeDef",
    ) -> "dc_td.CreateEventDestinationResult":
        return dc_td.CreateEventDestinationResult.make_one(res)

    def create_opt_out_list(
        self,
        res: "bs_td.CreateOptOutListResultTypeDef",
    ) -> "dc_td.CreateOptOutListResult":
        return dc_td.CreateOptOutListResult.make_one(res)

    def create_pool(
        self,
        res: "bs_td.CreatePoolResultTypeDef",
    ) -> "dc_td.CreatePoolResult":
        return dc_td.CreatePoolResult.make_one(res)

    def create_protect_configuration(
        self,
        res: "bs_td.CreateProtectConfigurationResultTypeDef",
    ) -> "dc_td.CreateProtectConfigurationResult":
        return dc_td.CreateProtectConfigurationResult.make_one(res)

    def create_registration(
        self,
        res: "bs_td.CreateRegistrationResultTypeDef",
    ) -> "dc_td.CreateRegistrationResult":
        return dc_td.CreateRegistrationResult.make_one(res)

    def create_registration_association(
        self,
        res: "bs_td.CreateRegistrationAssociationResultTypeDef",
    ) -> "dc_td.CreateRegistrationAssociationResult":
        return dc_td.CreateRegistrationAssociationResult.make_one(res)

    def create_registration_attachment(
        self,
        res: "bs_td.CreateRegistrationAttachmentResultTypeDef",
    ) -> "dc_td.CreateRegistrationAttachmentResult":
        return dc_td.CreateRegistrationAttachmentResult.make_one(res)

    def create_registration_version(
        self,
        res: "bs_td.CreateRegistrationVersionResultTypeDef",
    ) -> "dc_td.CreateRegistrationVersionResult":
        return dc_td.CreateRegistrationVersionResult.make_one(res)

    def create_verified_destination_number(
        self,
        res: "bs_td.CreateVerifiedDestinationNumberResultTypeDef",
    ) -> "dc_td.CreateVerifiedDestinationNumberResult":
        return dc_td.CreateVerifiedDestinationNumberResult.make_one(res)

    def delete_account_default_protect_configuration(
        self,
        res: "bs_td.DeleteAccountDefaultProtectConfigurationResultTypeDef",
    ) -> "dc_td.DeleteAccountDefaultProtectConfigurationResult":
        return dc_td.DeleteAccountDefaultProtectConfigurationResult.make_one(res)

    def delete_configuration_set(
        self,
        res: "bs_td.DeleteConfigurationSetResultTypeDef",
    ) -> "dc_td.DeleteConfigurationSetResult":
        return dc_td.DeleteConfigurationSetResult.make_one(res)

    def delete_default_message_type(
        self,
        res: "bs_td.DeleteDefaultMessageTypeResultTypeDef",
    ) -> "dc_td.DeleteDefaultMessageTypeResult":
        return dc_td.DeleteDefaultMessageTypeResult.make_one(res)

    def delete_default_sender_id(
        self,
        res: "bs_td.DeleteDefaultSenderIdResultTypeDef",
    ) -> "dc_td.DeleteDefaultSenderIdResult":
        return dc_td.DeleteDefaultSenderIdResult.make_one(res)

    def delete_event_destination(
        self,
        res: "bs_td.DeleteEventDestinationResultTypeDef",
    ) -> "dc_td.DeleteEventDestinationResult":
        return dc_td.DeleteEventDestinationResult.make_one(res)

    def delete_keyword(
        self,
        res: "bs_td.DeleteKeywordResultTypeDef",
    ) -> "dc_td.DeleteKeywordResult":
        return dc_td.DeleteKeywordResult.make_one(res)

    def delete_media_message_spend_limit_override(
        self,
        res: "bs_td.DeleteMediaMessageSpendLimitOverrideResultTypeDef",
    ) -> "dc_td.DeleteMediaMessageSpendLimitOverrideResult":
        return dc_td.DeleteMediaMessageSpendLimitOverrideResult.make_one(res)

    def delete_opt_out_list(
        self,
        res: "bs_td.DeleteOptOutListResultTypeDef",
    ) -> "dc_td.DeleteOptOutListResult":
        return dc_td.DeleteOptOutListResult.make_one(res)

    def delete_opted_out_number(
        self,
        res: "bs_td.DeleteOptedOutNumberResultTypeDef",
    ) -> "dc_td.DeleteOptedOutNumberResult":
        return dc_td.DeleteOptedOutNumberResult.make_one(res)

    def delete_pool(
        self,
        res: "bs_td.DeletePoolResultTypeDef",
    ) -> "dc_td.DeletePoolResult":
        return dc_td.DeletePoolResult.make_one(res)

    def delete_protect_configuration(
        self,
        res: "bs_td.DeleteProtectConfigurationResultTypeDef",
    ) -> "dc_td.DeleteProtectConfigurationResult":
        return dc_td.DeleteProtectConfigurationResult.make_one(res)

    def delete_protect_configuration_rule_set_number_override(
        self,
        res: "bs_td.DeleteProtectConfigurationRuleSetNumberOverrideResultTypeDef",
    ) -> "dc_td.DeleteProtectConfigurationRuleSetNumberOverrideResult":
        return dc_td.DeleteProtectConfigurationRuleSetNumberOverrideResult.make_one(res)

    def delete_registration(
        self,
        res: "bs_td.DeleteRegistrationResultTypeDef",
    ) -> "dc_td.DeleteRegistrationResult":
        return dc_td.DeleteRegistrationResult.make_one(res)

    def delete_registration_attachment(
        self,
        res: "bs_td.DeleteRegistrationAttachmentResultTypeDef",
    ) -> "dc_td.DeleteRegistrationAttachmentResult":
        return dc_td.DeleteRegistrationAttachmentResult.make_one(res)

    def delete_registration_field_value(
        self,
        res: "bs_td.DeleteRegistrationFieldValueResultTypeDef",
    ) -> "dc_td.DeleteRegistrationFieldValueResult":
        return dc_td.DeleteRegistrationFieldValueResult.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.DeleteResourcePolicyResultTypeDef",
    ) -> "dc_td.DeleteResourcePolicyResult":
        return dc_td.DeleteResourcePolicyResult.make_one(res)

    def delete_text_message_spend_limit_override(
        self,
        res: "bs_td.DeleteTextMessageSpendLimitOverrideResultTypeDef",
    ) -> "dc_td.DeleteTextMessageSpendLimitOverrideResult":
        return dc_td.DeleteTextMessageSpendLimitOverrideResult.make_one(res)

    def delete_verified_destination_number(
        self,
        res: "bs_td.DeleteVerifiedDestinationNumberResultTypeDef",
    ) -> "dc_td.DeleteVerifiedDestinationNumberResult":
        return dc_td.DeleteVerifiedDestinationNumberResult.make_one(res)

    def delete_voice_message_spend_limit_override(
        self,
        res: "bs_td.DeleteVoiceMessageSpendLimitOverrideResultTypeDef",
    ) -> "dc_td.DeleteVoiceMessageSpendLimitOverrideResult":
        return dc_td.DeleteVoiceMessageSpendLimitOverrideResult.make_one(res)

    def describe_account_attributes(
        self,
        res: "bs_td.DescribeAccountAttributesResultTypeDef",
    ) -> "dc_td.DescribeAccountAttributesResult":
        return dc_td.DescribeAccountAttributesResult.make_one(res)

    def describe_account_limits(
        self,
        res: "bs_td.DescribeAccountLimitsResultTypeDef",
    ) -> "dc_td.DescribeAccountLimitsResult":
        return dc_td.DescribeAccountLimitsResult.make_one(res)

    def describe_configuration_sets(
        self,
        res: "bs_td.DescribeConfigurationSetsResultTypeDef",
    ) -> "dc_td.DescribeConfigurationSetsResult":
        return dc_td.DescribeConfigurationSetsResult.make_one(res)

    def describe_keywords(
        self,
        res: "bs_td.DescribeKeywordsResultTypeDef",
    ) -> "dc_td.DescribeKeywordsResult":
        return dc_td.DescribeKeywordsResult.make_one(res)

    def describe_opt_out_lists(
        self,
        res: "bs_td.DescribeOptOutListsResultTypeDef",
    ) -> "dc_td.DescribeOptOutListsResult":
        return dc_td.DescribeOptOutListsResult.make_one(res)

    def describe_opted_out_numbers(
        self,
        res: "bs_td.DescribeOptedOutNumbersResultTypeDef",
    ) -> "dc_td.DescribeOptedOutNumbersResult":
        return dc_td.DescribeOptedOutNumbersResult.make_one(res)

    def describe_phone_numbers(
        self,
        res: "bs_td.DescribePhoneNumbersResultTypeDef",
    ) -> "dc_td.DescribePhoneNumbersResult":
        return dc_td.DescribePhoneNumbersResult.make_one(res)

    def describe_pools(
        self,
        res: "bs_td.DescribePoolsResultTypeDef",
    ) -> "dc_td.DescribePoolsResult":
        return dc_td.DescribePoolsResult.make_one(res)

    def describe_protect_configurations(
        self,
        res: "bs_td.DescribeProtectConfigurationsResultTypeDef",
    ) -> "dc_td.DescribeProtectConfigurationsResult":
        return dc_td.DescribeProtectConfigurationsResult.make_one(res)

    def describe_registration_attachments(
        self,
        res: "bs_td.DescribeRegistrationAttachmentsResultTypeDef",
    ) -> "dc_td.DescribeRegistrationAttachmentsResult":
        return dc_td.DescribeRegistrationAttachmentsResult.make_one(res)

    def describe_registration_field_definitions(
        self,
        res: "bs_td.DescribeRegistrationFieldDefinitionsResultTypeDef",
    ) -> "dc_td.DescribeRegistrationFieldDefinitionsResult":
        return dc_td.DescribeRegistrationFieldDefinitionsResult.make_one(res)

    def describe_registration_field_values(
        self,
        res: "bs_td.DescribeRegistrationFieldValuesResultTypeDef",
    ) -> "dc_td.DescribeRegistrationFieldValuesResult":
        return dc_td.DescribeRegistrationFieldValuesResult.make_one(res)

    def describe_registration_section_definitions(
        self,
        res: "bs_td.DescribeRegistrationSectionDefinitionsResultTypeDef",
    ) -> "dc_td.DescribeRegistrationSectionDefinitionsResult":
        return dc_td.DescribeRegistrationSectionDefinitionsResult.make_one(res)

    def describe_registration_type_definitions(
        self,
        res: "bs_td.DescribeRegistrationTypeDefinitionsResultTypeDef",
    ) -> "dc_td.DescribeRegistrationTypeDefinitionsResult":
        return dc_td.DescribeRegistrationTypeDefinitionsResult.make_one(res)

    def describe_registration_versions(
        self,
        res: "bs_td.DescribeRegistrationVersionsResultTypeDef",
    ) -> "dc_td.DescribeRegistrationVersionsResult":
        return dc_td.DescribeRegistrationVersionsResult.make_one(res)

    def describe_registrations(
        self,
        res: "bs_td.DescribeRegistrationsResultTypeDef",
    ) -> "dc_td.DescribeRegistrationsResult":
        return dc_td.DescribeRegistrationsResult.make_one(res)

    def describe_sender_ids(
        self,
        res: "bs_td.DescribeSenderIdsResultTypeDef",
    ) -> "dc_td.DescribeSenderIdsResult":
        return dc_td.DescribeSenderIdsResult.make_one(res)

    def describe_spend_limits(
        self,
        res: "bs_td.DescribeSpendLimitsResultTypeDef",
    ) -> "dc_td.DescribeSpendLimitsResult":
        return dc_td.DescribeSpendLimitsResult.make_one(res)

    def describe_verified_destination_numbers(
        self,
        res: "bs_td.DescribeVerifiedDestinationNumbersResultTypeDef",
    ) -> "dc_td.DescribeVerifiedDestinationNumbersResult":
        return dc_td.DescribeVerifiedDestinationNumbersResult.make_one(res)

    def disassociate_origination_identity(
        self,
        res: "bs_td.DisassociateOriginationIdentityResultTypeDef",
    ) -> "dc_td.DisassociateOriginationIdentityResult":
        return dc_td.DisassociateOriginationIdentityResult.make_one(res)

    def disassociate_protect_configuration(
        self,
        res: "bs_td.DisassociateProtectConfigurationResultTypeDef",
    ) -> "dc_td.DisassociateProtectConfigurationResult":
        return dc_td.DisassociateProtectConfigurationResult.make_one(res)

    def discard_registration_version(
        self,
        res: "bs_td.DiscardRegistrationVersionResultTypeDef",
    ) -> "dc_td.DiscardRegistrationVersionResult":
        return dc_td.DiscardRegistrationVersionResult.make_one(res)

    def get_protect_configuration_country_rule_set(
        self,
        res: "bs_td.GetProtectConfigurationCountryRuleSetResultTypeDef",
    ) -> "dc_td.GetProtectConfigurationCountryRuleSetResult":
        return dc_td.GetProtectConfigurationCountryRuleSetResult.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResultTypeDef",
    ) -> "dc_td.GetResourcePolicyResult":
        return dc_td.GetResourcePolicyResult.make_one(res)

    def list_pool_origination_identities(
        self,
        res: "bs_td.ListPoolOriginationIdentitiesResultTypeDef",
    ) -> "dc_td.ListPoolOriginationIdentitiesResult":
        return dc_td.ListPoolOriginationIdentitiesResult.make_one(res)

    def list_protect_configuration_rule_set_number_overrides(
        self,
        res: "bs_td.ListProtectConfigurationRuleSetNumberOverridesResultTypeDef",
    ) -> "dc_td.ListProtectConfigurationRuleSetNumberOverridesResult":
        return dc_td.ListProtectConfigurationRuleSetNumberOverridesResult.make_one(res)

    def list_registration_associations(
        self,
        res: "bs_td.ListRegistrationAssociationsResultTypeDef",
    ) -> "dc_td.ListRegistrationAssociationsResult":
        return dc_td.ListRegistrationAssociationsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResultTypeDef",
    ) -> "dc_td.ListTagsForResourceResult":
        return dc_td.ListTagsForResourceResult.make_one(res)

    def put_keyword(
        self,
        res: "bs_td.PutKeywordResultTypeDef",
    ) -> "dc_td.PutKeywordResult":
        return dc_td.PutKeywordResult.make_one(res)

    def put_message_feedback(
        self,
        res: "bs_td.PutMessageFeedbackResultTypeDef",
    ) -> "dc_td.PutMessageFeedbackResult":
        return dc_td.PutMessageFeedbackResult.make_one(res)

    def put_opted_out_number(
        self,
        res: "bs_td.PutOptedOutNumberResultTypeDef",
    ) -> "dc_td.PutOptedOutNumberResult":
        return dc_td.PutOptedOutNumberResult.make_one(res)

    def put_protect_configuration_rule_set_number_override(
        self,
        res: "bs_td.PutProtectConfigurationRuleSetNumberOverrideResultTypeDef",
    ) -> "dc_td.PutProtectConfigurationRuleSetNumberOverrideResult":
        return dc_td.PutProtectConfigurationRuleSetNumberOverrideResult.make_one(res)

    def put_registration_field_value(
        self,
        res: "bs_td.PutRegistrationFieldValueResultTypeDef",
    ) -> "dc_td.PutRegistrationFieldValueResult":
        return dc_td.PutRegistrationFieldValueResult.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResultTypeDef",
    ) -> "dc_td.PutResourcePolicyResult":
        return dc_td.PutResourcePolicyResult.make_one(res)

    def release_phone_number(
        self,
        res: "bs_td.ReleasePhoneNumberResultTypeDef",
    ) -> "dc_td.ReleasePhoneNumberResult":
        return dc_td.ReleasePhoneNumberResult.make_one(res)

    def release_sender_id(
        self,
        res: "bs_td.ReleaseSenderIdResultTypeDef",
    ) -> "dc_td.ReleaseSenderIdResult":
        return dc_td.ReleaseSenderIdResult.make_one(res)

    def request_phone_number(
        self,
        res: "bs_td.RequestPhoneNumberResultTypeDef",
    ) -> "dc_td.RequestPhoneNumberResult":
        return dc_td.RequestPhoneNumberResult.make_one(res)

    def request_sender_id(
        self,
        res: "bs_td.RequestSenderIdResultTypeDef",
    ) -> "dc_td.RequestSenderIdResult":
        return dc_td.RequestSenderIdResult.make_one(res)

    def send_destination_number_verification_code(
        self,
        res: "bs_td.SendDestinationNumberVerificationCodeResultTypeDef",
    ) -> "dc_td.SendDestinationNumberVerificationCodeResult":
        return dc_td.SendDestinationNumberVerificationCodeResult.make_one(res)

    def send_media_message(
        self,
        res: "bs_td.SendMediaMessageResultTypeDef",
    ) -> "dc_td.SendMediaMessageResult":
        return dc_td.SendMediaMessageResult.make_one(res)

    def send_text_message(
        self,
        res: "bs_td.SendTextMessageResultTypeDef",
    ) -> "dc_td.SendTextMessageResult":
        return dc_td.SendTextMessageResult.make_one(res)

    def send_voice_message(
        self,
        res: "bs_td.SendVoiceMessageResultTypeDef",
    ) -> "dc_td.SendVoiceMessageResult":
        return dc_td.SendVoiceMessageResult.make_one(res)

    def set_account_default_protect_configuration(
        self,
        res: "bs_td.SetAccountDefaultProtectConfigurationResultTypeDef",
    ) -> "dc_td.SetAccountDefaultProtectConfigurationResult":
        return dc_td.SetAccountDefaultProtectConfigurationResult.make_one(res)

    def set_default_message_feedback_enabled(
        self,
        res: "bs_td.SetDefaultMessageFeedbackEnabledResultTypeDef",
    ) -> "dc_td.SetDefaultMessageFeedbackEnabledResult":
        return dc_td.SetDefaultMessageFeedbackEnabledResult.make_one(res)

    def set_default_message_type(
        self,
        res: "bs_td.SetDefaultMessageTypeResultTypeDef",
    ) -> "dc_td.SetDefaultMessageTypeResult":
        return dc_td.SetDefaultMessageTypeResult.make_one(res)

    def set_default_sender_id(
        self,
        res: "bs_td.SetDefaultSenderIdResultTypeDef",
    ) -> "dc_td.SetDefaultSenderIdResult":
        return dc_td.SetDefaultSenderIdResult.make_one(res)

    def set_media_message_spend_limit_override(
        self,
        res: "bs_td.SetMediaMessageSpendLimitOverrideResultTypeDef",
    ) -> "dc_td.SetMediaMessageSpendLimitOverrideResult":
        return dc_td.SetMediaMessageSpendLimitOverrideResult.make_one(res)

    def set_text_message_spend_limit_override(
        self,
        res: "bs_td.SetTextMessageSpendLimitOverrideResultTypeDef",
    ) -> "dc_td.SetTextMessageSpendLimitOverrideResult":
        return dc_td.SetTextMessageSpendLimitOverrideResult.make_one(res)

    def set_voice_message_spend_limit_override(
        self,
        res: "bs_td.SetVoiceMessageSpendLimitOverrideResultTypeDef",
    ) -> "dc_td.SetVoiceMessageSpendLimitOverrideResult":
        return dc_td.SetVoiceMessageSpendLimitOverrideResult.make_one(res)

    def submit_registration_version(
        self,
        res: "bs_td.SubmitRegistrationVersionResultTypeDef",
    ) -> "dc_td.SubmitRegistrationVersionResult":
        return dc_td.SubmitRegistrationVersionResult.make_one(res)

    def update_event_destination(
        self,
        res: "bs_td.UpdateEventDestinationResultTypeDef",
    ) -> "dc_td.UpdateEventDestinationResult":
        return dc_td.UpdateEventDestinationResult.make_one(res)

    def update_phone_number(
        self,
        res: "bs_td.UpdatePhoneNumberResultTypeDef",
    ) -> "dc_td.UpdatePhoneNumberResult":
        return dc_td.UpdatePhoneNumberResult.make_one(res)

    def update_pool(
        self,
        res: "bs_td.UpdatePoolResultTypeDef",
    ) -> "dc_td.UpdatePoolResult":
        return dc_td.UpdatePoolResult.make_one(res)

    def update_protect_configuration(
        self,
        res: "bs_td.UpdateProtectConfigurationResultTypeDef",
    ) -> "dc_td.UpdateProtectConfigurationResult":
        return dc_td.UpdateProtectConfigurationResult.make_one(res)

    def update_protect_configuration_country_rule_set(
        self,
        res: "bs_td.UpdateProtectConfigurationCountryRuleSetResultTypeDef",
    ) -> "dc_td.UpdateProtectConfigurationCountryRuleSetResult":
        return dc_td.UpdateProtectConfigurationCountryRuleSetResult.make_one(res)

    def update_sender_id(
        self,
        res: "bs_td.UpdateSenderIdResultTypeDef",
    ) -> "dc_td.UpdateSenderIdResult":
        return dc_td.UpdateSenderIdResult.make_one(res)

    def verify_destination_number(
        self,
        res: "bs_td.VerifyDestinationNumberResultTypeDef",
    ) -> "dc_td.VerifyDestinationNumberResult":
        return dc_td.VerifyDestinationNumberResult.make_one(res)


pinpoint_sms_voice_v2_caster = PINPOINT_SMS_VOICE_V2Caster()
