# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workmail import type_defs as bs_td


class WORKMAILCaster:

    def assume_impersonation_role(
        self,
        res: "bs_td.AssumeImpersonationRoleResponseTypeDef",
    ) -> "dc_td.AssumeImpersonationRoleResponse":
        return dc_td.AssumeImpersonationRoleResponse.make_one(res)

    def create_group(
        self,
        res: "bs_td.CreateGroupResponseTypeDef",
    ) -> "dc_td.CreateGroupResponse":
        return dc_td.CreateGroupResponse.make_one(res)

    def create_identity_center_application(
        self,
        res: "bs_td.CreateIdentityCenterApplicationResponseTypeDef",
    ) -> "dc_td.CreateIdentityCenterApplicationResponse":
        return dc_td.CreateIdentityCenterApplicationResponse.make_one(res)

    def create_impersonation_role(
        self,
        res: "bs_td.CreateImpersonationRoleResponseTypeDef",
    ) -> "dc_td.CreateImpersonationRoleResponse":
        return dc_td.CreateImpersonationRoleResponse.make_one(res)

    def create_mobile_device_access_rule(
        self,
        res: "bs_td.CreateMobileDeviceAccessRuleResponseTypeDef",
    ) -> "dc_td.CreateMobileDeviceAccessRuleResponse":
        return dc_td.CreateMobileDeviceAccessRuleResponse.make_one(res)

    def create_organization(
        self,
        res: "bs_td.CreateOrganizationResponseTypeDef",
    ) -> "dc_td.CreateOrganizationResponse":
        return dc_td.CreateOrganizationResponse.make_one(res)

    def create_resource(
        self,
        res: "bs_td.CreateResourceResponseTypeDef",
    ) -> "dc_td.CreateResourceResponse":
        return dc_td.CreateResourceResponse.make_one(res)

    def create_user(
        self,
        res: "bs_td.CreateUserResponseTypeDef",
    ) -> "dc_td.CreateUserResponse":
        return dc_td.CreateUserResponse.make_one(res)

    def delete_organization(
        self,
        res: "bs_td.DeleteOrganizationResponseTypeDef",
    ) -> "dc_td.DeleteOrganizationResponse":
        return dc_td.DeleteOrganizationResponse.make_one(res)

    def describe_email_monitoring_configuration(
        self,
        res: "bs_td.DescribeEmailMonitoringConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeEmailMonitoringConfigurationResponse":
        return dc_td.DescribeEmailMonitoringConfigurationResponse.make_one(res)

    def describe_entity(
        self,
        res: "bs_td.DescribeEntityResponseTypeDef",
    ) -> "dc_td.DescribeEntityResponse":
        return dc_td.DescribeEntityResponse.make_one(res)

    def describe_group(
        self,
        res: "bs_td.DescribeGroupResponseTypeDef",
    ) -> "dc_td.DescribeGroupResponse":
        return dc_td.DescribeGroupResponse.make_one(res)

    def describe_identity_provider_configuration(
        self,
        res: "bs_td.DescribeIdentityProviderConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeIdentityProviderConfigurationResponse":
        return dc_td.DescribeIdentityProviderConfigurationResponse.make_one(res)

    def describe_inbound_dmarc_settings(
        self,
        res: "bs_td.DescribeInboundDmarcSettingsResponseTypeDef",
    ) -> "dc_td.DescribeInboundDmarcSettingsResponse":
        return dc_td.DescribeInboundDmarcSettingsResponse.make_one(res)

    def describe_mailbox_export_job(
        self,
        res: "bs_td.DescribeMailboxExportJobResponseTypeDef",
    ) -> "dc_td.DescribeMailboxExportJobResponse":
        return dc_td.DescribeMailboxExportJobResponse.make_one(res)

    def describe_organization(
        self,
        res: "bs_td.DescribeOrganizationResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationResponse":
        return dc_td.DescribeOrganizationResponse.make_one(res)

    def describe_resource(
        self,
        res: "bs_td.DescribeResourceResponseTypeDef",
    ) -> "dc_td.DescribeResourceResponse":
        return dc_td.DescribeResourceResponse.make_one(res)

    def describe_user(
        self,
        res: "bs_td.DescribeUserResponseTypeDef",
    ) -> "dc_td.DescribeUserResponse":
        return dc_td.DescribeUserResponse.make_one(res)

    def get_access_control_effect(
        self,
        res: "bs_td.GetAccessControlEffectResponseTypeDef",
    ) -> "dc_td.GetAccessControlEffectResponse":
        return dc_td.GetAccessControlEffectResponse.make_one(res)

    def get_default_retention_policy(
        self,
        res: "bs_td.GetDefaultRetentionPolicyResponseTypeDef",
    ) -> "dc_td.GetDefaultRetentionPolicyResponse":
        return dc_td.GetDefaultRetentionPolicyResponse.make_one(res)

    def get_impersonation_role(
        self,
        res: "bs_td.GetImpersonationRoleResponseTypeDef",
    ) -> "dc_td.GetImpersonationRoleResponse":
        return dc_td.GetImpersonationRoleResponse.make_one(res)

    def get_impersonation_role_effect(
        self,
        res: "bs_td.GetImpersonationRoleEffectResponseTypeDef",
    ) -> "dc_td.GetImpersonationRoleEffectResponse":
        return dc_td.GetImpersonationRoleEffectResponse.make_one(res)

    def get_mail_domain(
        self,
        res: "bs_td.GetMailDomainResponseTypeDef",
    ) -> "dc_td.GetMailDomainResponse":
        return dc_td.GetMailDomainResponse.make_one(res)

    def get_mailbox_details(
        self,
        res: "bs_td.GetMailboxDetailsResponseTypeDef",
    ) -> "dc_td.GetMailboxDetailsResponse":
        return dc_td.GetMailboxDetailsResponse.make_one(res)

    def get_mobile_device_access_effect(
        self,
        res: "bs_td.GetMobileDeviceAccessEffectResponseTypeDef",
    ) -> "dc_td.GetMobileDeviceAccessEffectResponse":
        return dc_td.GetMobileDeviceAccessEffectResponse.make_one(res)

    def get_mobile_device_access_override(
        self,
        res: "bs_td.GetMobileDeviceAccessOverrideResponseTypeDef",
    ) -> "dc_td.GetMobileDeviceAccessOverrideResponse":
        return dc_td.GetMobileDeviceAccessOverrideResponse.make_one(res)

    def get_personal_access_token_metadata(
        self,
        res: "bs_td.GetPersonalAccessTokenMetadataResponseTypeDef",
    ) -> "dc_td.GetPersonalAccessTokenMetadataResponse":
        return dc_td.GetPersonalAccessTokenMetadataResponse.make_one(res)

    def list_access_control_rules(
        self,
        res: "bs_td.ListAccessControlRulesResponseTypeDef",
    ) -> "dc_td.ListAccessControlRulesResponse":
        return dc_td.ListAccessControlRulesResponse.make_one(res)

    def list_aliases(
        self,
        res: "bs_td.ListAliasesResponseTypeDef",
    ) -> "dc_td.ListAliasesResponse":
        return dc_td.ListAliasesResponse.make_one(res)

    def list_availability_configurations(
        self,
        res: "bs_td.ListAvailabilityConfigurationsResponseTypeDef",
    ) -> "dc_td.ListAvailabilityConfigurationsResponse":
        return dc_td.ListAvailabilityConfigurationsResponse.make_one(res)

    def list_group_members(
        self,
        res: "bs_td.ListGroupMembersResponseTypeDef",
    ) -> "dc_td.ListGroupMembersResponse":
        return dc_td.ListGroupMembersResponse.make_one(res)

    def list_groups(
        self,
        res: "bs_td.ListGroupsResponseTypeDef",
    ) -> "dc_td.ListGroupsResponse":
        return dc_td.ListGroupsResponse.make_one(res)

    def list_groups_for_entity(
        self,
        res: "bs_td.ListGroupsForEntityResponseTypeDef",
    ) -> "dc_td.ListGroupsForEntityResponse":
        return dc_td.ListGroupsForEntityResponse.make_one(res)

    def list_impersonation_roles(
        self,
        res: "bs_td.ListImpersonationRolesResponseTypeDef",
    ) -> "dc_td.ListImpersonationRolesResponse":
        return dc_td.ListImpersonationRolesResponse.make_one(res)

    def list_mail_domains(
        self,
        res: "bs_td.ListMailDomainsResponseTypeDef",
    ) -> "dc_td.ListMailDomainsResponse":
        return dc_td.ListMailDomainsResponse.make_one(res)

    def list_mailbox_export_jobs(
        self,
        res: "bs_td.ListMailboxExportJobsResponseTypeDef",
    ) -> "dc_td.ListMailboxExportJobsResponse":
        return dc_td.ListMailboxExportJobsResponse.make_one(res)

    def list_mailbox_permissions(
        self,
        res: "bs_td.ListMailboxPermissionsResponseTypeDef",
    ) -> "dc_td.ListMailboxPermissionsResponse":
        return dc_td.ListMailboxPermissionsResponse.make_one(res)

    def list_mobile_device_access_overrides(
        self,
        res: "bs_td.ListMobileDeviceAccessOverridesResponseTypeDef",
    ) -> "dc_td.ListMobileDeviceAccessOverridesResponse":
        return dc_td.ListMobileDeviceAccessOverridesResponse.make_one(res)

    def list_mobile_device_access_rules(
        self,
        res: "bs_td.ListMobileDeviceAccessRulesResponseTypeDef",
    ) -> "dc_td.ListMobileDeviceAccessRulesResponse":
        return dc_td.ListMobileDeviceAccessRulesResponse.make_one(res)

    def list_organizations(
        self,
        res: "bs_td.ListOrganizationsResponseTypeDef",
    ) -> "dc_td.ListOrganizationsResponse":
        return dc_td.ListOrganizationsResponse.make_one(res)

    def list_personal_access_tokens(
        self,
        res: "bs_td.ListPersonalAccessTokensResponseTypeDef",
    ) -> "dc_td.ListPersonalAccessTokensResponse":
        return dc_td.ListPersonalAccessTokensResponse.make_one(res)

    def list_resource_delegates(
        self,
        res: "bs_td.ListResourceDelegatesResponseTypeDef",
    ) -> "dc_td.ListResourceDelegatesResponse":
        return dc_td.ListResourceDelegatesResponse.make_one(res)

    def list_resources(
        self,
        res: "bs_td.ListResourcesResponseTypeDef",
    ) -> "dc_td.ListResourcesResponse":
        return dc_td.ListResourcesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)

    def start_mailbox_export_job(
        self,
        res: "bs_td.StartMailboxExportJobResponseTypeDef",
    ) -> "dc_td.StartMailboxExportJobResponse":
        return dc_td.StartMailboxExportJobResponse.make_one(res)

    def test_availability_configuration(
        self,
        res: "bs_td.TestAvailabilityConfigurationResponseTypeDef",
    ) -> "dc_td.TestAvailabilityConfigurationResponse":
        return dc_td.TestAvailabilityConfigurationResponse.make_one(res)


workmail_caster = WORKMAILCaster()
