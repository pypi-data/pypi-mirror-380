# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_securityhub import type_defs as bs_td


class SECURITYHUBCaster:

    def batch_delete_automation_rules(
        self,
        res: "bs_td.BatchDeleteAutomationRulesResponseTypeDef",
    ) -> "dc_td.BatchDeleteAutomationRulesResponse":
        return dc_td.BatchDeleteAutomationRulesResponse.make_one(res)

    def batch_disable_standards(
        self,
        res: "bs_td.BatchDisableStandardsResponseTypeDef",
    ) -> "dc_td.BatchDisableStandardsResponse":
        return dc_td.BatchDisableStandardsResponse.make_one(res)

    def batch_enable_standards(
        self,
        res: "bs_td.BatchEnableStandardsResponseTypeDef",
    ) -> "dc_td.BatchEnableStandardsResponse":
        return dc_td.BatchEnableStandardsResponse.make_one(res)

    def batch_get_automation_rules(
        self,
        res: "bs_td.BatchGetAutomationRulesResponseTypeDef",
    ) -> "dc_td.BatchGetAutomationRulesResponse":
        return dc_td.BatchGetAutomationRulesResponse.make_one(res)

    def batch_get_configuration_policy_associations(
        self,
        res: "bs_td.BatchGetConfigurationPolicyAssociationsResponseTypeDef",
    ) -> "dc_td.BatchGetConfigurationPolicyAssociationsResponse":
        return dc_td.BatchGetConfigurationPolicyAssociationsResponse.make_one(res)

    def batch_get_security_controls(
        self,
        res: "bs_td.BatchGetSecurityControlsResponseTypeDef",
    ) -> "dc_td.BatchGetSecurityControlsResponse":
        return dc_td.BatchGetSecurityControlsResponse.make_one(res)

    def batch_get_standards_control_associations(
        self,
        res: "bs_td.BatchGetStandardsControlAssociationsResponseTypeDef",
    ) -> "dc_td.BatchGetStandardsControlAssociationsResponse":
        return dc_td.BatchGetStandardsControlAssociationsResponse.make_one(res)

    def batch_import_findings(
        self,
        res: "bs_td.BatchImportFindingsResponseTypeDef",
    ) -> "dc_td.BatchImportFindingsResponse":
        return dc_td.BatchImportFindingsResponse.make_one(res)

    def batch_update_automation_rules(
        self,
        res: "bs_td.BatchUpdateAutomationRulesResponseTypeDef",
    ) -> "dc_td.BatchUpdateAutomationRulesResponse":
        return dc_td.BatchUpdateAutomationRulesResponse.make_one(res)

    def batch_update_findings(
        self,
        res: "bs_td.BatchUpdateFindingsResponseTypeDef",
    ) -> "dc_td.BatchUpdateFindingsResponse":
        return dc_td.BatchUpdateFindingsResponse.make_one(res)

    def batch_update_findings_v2(
        self,
        res: "bs_td.BatchUpdateFindingsV2ResponseTypeDef",
    ) -> "dc_td.BatchUpdateFindingsV2Response":
        return dc_td.BatchUpdateFindingsV2Response.make_one(res)

    def batch_update_standards_control_associations(
        self,
        res: "bs_td.BatchUpdateStandardsControlAssociationsResponseTypeDef",
    ) -> "dc_td.BatchUpdateStandardsControlAssociationsResponse":
        return dc_td.BatchUpdateStandardsControlAssociationsResponse.make_one(res)

    def connector_registrations_v2(
        self,
        res: "bs_td.ConnectorRegistrationsV2ResponseTypeDef",
    ) -> "dc_td.ConnectorRegistrationsV2Response":
        return dc_td.ConnectorRegistrationsV2Response.make_one(res)

    def create_action_target(
        self,
        res: "bs_td.CreateActionTargetResponseTypeDef",
    ) -> "dc_td.CreateActionTargetResponse":
        return dc_td.CreateActionTargetResponse.make_one(res)

    def create_aggregator_v2(
        self,
        res: "bs_td.CreateAggregatorV2ResponseTypeDef",
    ) -> "dc_td.CreateAggregatorV2Response":
        return dc_td.CreateAggregatorV2Response.make_one(res)

    def create_automation_rule(
        self,
        res: "bs_td.CreateAutomationRuleResponseTypeDef",
    ) -> "dc_td.CreateAutomationRuleResponse":
        return dc_td.CreateAutomationRuleResponse.make_one(res)

    def create_automation_rule_v2(
        self,
        res: "bs_td.CreateAutomationRuleV2ResponseTypeDef",
    ) -> "dc_td.CreateAutomationRuleV2Response":
        return dc_td.CreateAutomationRuleV2Response.make_one(res)

    def create_configuration_policy(
        self,
        res: "bs_td.CreateConfigurationPolicyResponseTypeDef",
    ) -> "dc_td.CreateConfigurationPolicyResponse":
        return dc_td.CreateConfigurationPolicyResponse.make_one(res)

    def create_connector_v2(
        self,
        res: "bs_td.CreateConnectorV2ResponseTypeDef",
    ) -> "dc_td.CreateConnectorV2Response":
        return dc_td.CreateConnectorV2Response.make_one(res)

    def create_finding_aggregator(
        self,
        res: "bs_td.CreateFindingAggregatorResponseTypeDef",
    ) -> "dc_td.CreateFindingAggregatorResponse":
        return dc_td.CreateFindingAggregatorResponse.make_one(res)

    def create_insight(
        self,
        res: "bs_td.CreateInsightResponseTypeDef",
    ) -> "dc_td.CreateInsightResponse":
        return dc_td.CreateInsightResponse.make_one(res)

    def create_members(
        self,
        res: "bs_td.CreateMembersResponseTypeDef",
    ) -> "dc_td.CreateMembersResponse":
        return dc_td.CreateMembersResponse.make_one(res)

    def create_ticket_v2(
        self,
        res: "bs_td.CreateTicketV2ResponseTypeDef",
    ) -> "dc_td.CreateTicketV2Response":
        return dc_td.CreateTicketV2Response.make_one(res)

    def decline_invitations(
        self,
        res: "bs_td.DeclineInvitationsResponseTypeDef",
    ) -> "dc_td.DeclineInvitationsResponse":
        return dc_td.DeclineInvitationsResponse.make_one(res)

    def delete_action_target(
        self,
        res: "bs_td.DeleteActionTargetResponseTypeDef",
    ) -> "dc_td.DeleteActionTargetResponse":
        return dc_td.DeleteActionTargetResponse.make_one(res)

    def delete_insight(
        self,
        res: "bs_td.DeleteInsightResponseTypeDef",
    ) -> "dc_td.DeleteInsightResponse":
        return dc_td.DeleteInsightResponse.make_one(res)

    def delete_invitations(
        self,
        res: "bs_td.DeleteInvitationsResponseTypeDef",
    ) -> "dc_td.DeleteInvitationsResponse":
        return dc_td.DeleteInvitationsResponse.make_one(res)

    def delete_members(
        self,
        res: "bs_td.DeleteMembersResponseTypeDef",
    ) -> "dc_td.DeleteMembersResponse":
        return dc_td.DeleteMembersResponse.make_one(res)

    def describe_action_targets(
        self,
        res: "bs_td.DescribeActionTargetsResponseTypeDef",
    ) -> "dc_td.DescribeActionTargetsResponse":
        return dc_td.DescribeActionTargetsResponse.make_one(res)

    def describe_hub(
        self,
        res: "bs_td.DescribeHubResponseTypeDef",
    ) -> "dc_td.DescribeHubResponse":
        return dc_td.DescribeHubResponse.make_one(res)

    def describe_organization_configuration(
        self,
        res: "bs_td.DescribeOrganizationConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationConfigurationResponse":
        return dc_td.DescribeOrganizationConfigurationResponse.make_one(res)

    def describe_products(
        self,
        res: "bs_td.DescribeProductsResponseTypeDef",
    ) -> "dc_td.DescribeProductsResponse":
        return dc_td.DescribeProductsResponse.make_one(res)

    def describe_products_v2(
        self,
        res: "bs_td.DescribeProductsV2ResponseTypeDef",
    ) -> "dc_td.DescribeProductsV2Response":
        return dc_td.DescribeProductsV2Response.make_one(res)

    def describe_security_hub_v2(
        self,
        res: "bs_td.DescribeSecurityHubV2ResponseTypeDef",
    ) -> "dc_td.DescribeSecurityHubV2Response":
        return dc_td.DescribeSecurityHubV2Response.make_one(res)

    def describe_standards(
        self,
        res: "bs_td.DescribeStandardsResponseTypeDef",
    ) -> "dc_td.DescribeStandardsResponse":
        return dc_td.DescribeStandardsResponse.make_one(res)

    def describe_standards_controls(
        self,
        res: "bs_td.DescribeStandardsControlsResponseTypeDef",
    ) -> "dc_td.DescribeStandardsControlsResponse":
        return dc_td.DescribeStandardsControlsResponse.make_one(res)

    def enable_import_findings_for_product(
        self,
        res: "bs_td.EnableImportFindingsForProductResponseTypeDef",
    ) -> "dc_td.EnableImportFindingsForProductResponse":
        return dc_td.EnableImportFindingsForProductResponse.make_one(res)

    def enable_organization_admin_account(
        self,
        res: "bs_td.EnableOrganizationAdminAccountResponseTypeDef",
    ) -> "dc_td.EnableOrganizationAdminAccountResponse":
        return dc_td.EnableOrganizationAdminAccountResponse.make_one(res)

    def enable_security_hub_v2(
        self,
        res: "bs_td.EnableSecurityHubV2ResponseTypeDef",
    ) -> "dc_td.EnableSecurityHubV2Response":
        return dc_td.EnableSecurityHubV2Response.make_one(res)

    def get_administrator_account(
        self,
        res: "bs_td.GetAdministratorAccountResponseTypeDef",
    ) -> "dc_td.GetAdministratorAccountResponse":
        return dc_td.GetAdministratorAccountResponse.make_one(res)

    def get_aggregator_v2(
        self,
        res: "bs_td.GetAggregatorV2ResponseTypeDef",
    ) -> "dc_td.GetAggregatorV2Response":
        return dc_td.GetAggregatorV2Response.make_one(res)

    def get_automation_rule_v2(
        self,
        res: "bs_td.GetAutomationRuleV2ResponseTypeDef",
    ) -> "dc_td.GetAutomationRuleV2Response":
        return dc_td.GetAutomationRuleV2Response.make_one(res)

    def get_configuration_policy(
        self,
        res: "bs_td.GetConfigurationPolicyResponseTypeDef",
    ) -> "dc_td.GetConfigurationPolicyResponse":
        return dc_td.GetConfigurationPolicyResponse.make_one(res)

    def get_configuration_policy_association(
        self,
        res: "bs_td.GetConfigurationPolicyAssociationResponseTypeDef",
    ) -> "dc_td.GetConfigurationPolicyAssociationResponse":
        return dc_td.GetConfigurationPolicyAssociationResponse.make_one(res)

    def get_connector_v2(
        self,
        res: "bs_td.GetConnectorV2ResponseTypeDef",
    ) -> "dc_td.GetConnectorV2Response":
        return dc_td.GetConnectorV2Response.make_one(res)

    def get_enabled_standards(
        self,
        res: "bs_td.GetEnabledStandardsResponseTypeDef",
    ) -> "dc_td.GetEnabledStandardsResponse":
        return dc_td.GetEnabledStandardsResponse.make_one(res)

    def get_finding_aggregator(
        self,
        res: "bs_td.GetFindingAggregatorResponseTypeDef",
    ) -> "dc_td.GetFindingAggregatorResponse":
        return dc_td.GetFindingAggregatorResponse.make_one(res)

    def get_finding_history(
        self,
        res: "bs_td.GetFindingHistoryResponseTypeDef",
    ) -> "dc_td.GetFindingHistoryResponse":
        return dc_td.GetFindingHistoryResponse.make_one(res)

    def get_finding_statistics_v2(
        self,
        res: "bs_td.GetFindingStatisticsV2ResponseTypeDef",
    ) -> "dc_td.GetFindingStatisticsV2Response":
        return dc_td.GetFindingStatisticsV2Response.make_one(res)

    def get_findings(
        self,
        res: "bs_td.GetFindingsResponseTypeDef",
    ) -> "dc_td.GetFindingsResponse":
        return dc_td.GetFindingsResponse.make_one(res)

    def get_findings_v2(
        self,
        res: "bs_td.GetFindingsV2ResponseTypeDef",
    ) -> "dc_td.GetFindingsV2Response":
        return dc_td.GetFindingsV2Response.make_one(res)

    def get_insight_results(
        self,
        res: "bs_td.GetInsightResultsResponseTypeDef",
    ) -> "dc_td.GetInsightResultsResponse":
        return dc_td.GetInsightResultsResponse.make_one(res)

    def get_insights(
        self,
        res: "bs_td.GetInsightsResponseTypeDef",
    ) -> "dc_td.GetInsightsResponse":
        return dc_td.GetInsightsResponse.make_one(res)

    def get_invitations_count(
        self,
        res: "bs_td.GetInvitationsCountResponseTypeDef",
    ) -> "dc_td.GetInvitationsCountResponse":
        return dc_td.GetInvitationsCountResponse.make_one(res)

    def get_master_account(
        self,
        res: "bs_td.GetMasterAccountResponseTypeDef",
    ) -> "dc_td.GetMasterAccountResponse":
        return dc_td.GetMasterAccountResponse.make_one(res)

    def get_members(
        self,
        res: "bs_td.GetMembersResponseTypeDef",
    ) -> "dc_td.GetMembersResponse":
        return dc_td.GetMembersResponse.make_one(res)

    def get_resources_statistics_v2(
        self,
        res: "bs_td.GetResourcesStatisticsV2ResponseTypeDef",
    ) -> "dc_td.GetResourcesStatisticsV2Response":
        return dc_td.GetResourcesStatisticsV2Response.make_one(res)

    def get_resources_v2(
        self,
        res: "bs_td.GetResourcesV2ResponseTypeDef",
    ) -> "dc_td.GetResourcesV2Response":
        return dc_td.GetResourcesV2Response.make_one(res)

    def get_security_control_definition(
        self,
        res: "bs_td.GetSecurityControlDefinitionResponseTypeDef",
    ) -> "dc_td.GetSecurityControlDefinitionResponse":
        return dc_td.GetSecurityControlDefinitionResponse.make_one(res)

    def invite_members(
        self,
        res: "bs_td.InviteMembersResponseTypeDef",
    ) -> "dc_td.InviteMembersResponse":
        return dc_td.InviteMembersResponse.make_one(res)

    def list_aggregators_v2(
        self,
        res: "bs_td.ListAggregatorsV2ResponseTypeDef",
    ) -> "dc_td.ListAggregatorsV2Response":
        return dc_td.ListAggregatorsV2Response.make_one(res)

    def list_automation_rules(
        self,
        res: "bs_td.ListAutomationRulesResponseTypeDef",
    ) -> "dc_td.ListAutomationRulesResponse":
        return dc_td.ListAutomationRulesResponse.make_one(res)

    def list_automation_rules_v2(
        self,
        res: "bs_td.ListAutomationRulesV2ResponseTypeDef",
    ) -> "dc_td.ListAutomationRulesV2Response":
        return dc_td.ListAutomationRulesV2Response.make_one(res)

    def list_configuration_policies(
        self,
        res: "bs_td.ListConfigurationPoliciesResponseTypeDef",
    ) -> "dc_td.ListConfigurationPoliciesResponse":
        return dc_td.ListConfigurationPoliciesResponse.make_one(res)

    def list_configuration_policy_associations(
        self,
        res: "bs_td.ListConfigurationPolicyAssociationsResponseTypeDef",
    ) -> "dc_td.ListConfigurationPolicyAssociationsResponse":
        return dc_td.ListConfigurationPolicyAssociationsResponse.make_one(res)

    def list_connectors_v2(
        self,
        res: "bs_td.ListConnectorsV2ResponseTypeDef",
    ) -> "dc_td.ListConnectorsV2Response":
        return dc_td.ListConnectorsV2Response.make_one(res)

    def list_enabled_products_for_import(
        self,
        res: "bs_td.ListEnabledProductsForImportResponseTypeDef",
    ) -> "dc_td.ListEnabledProductsForImportResponse":
        return dc_td.ListEnabledProductsForImportResponse.make_one(res)

    def list_finding_aggregators(
        self,
        res: "bs_td.ListFindingAggregatorsResponseTypeDef",
    ) -> "dc_td.ListFindingAggregatorsResponse":
        return dc_td.ListFindingAggregatorsResponse.make_one(res)

    def list_invitations(
        self,
        res: "bs_td.ListInvitationsResponseTypeDef",
    ) -> "dc_td.ListInvitationsResponse":
        return dc_td.ListInvitationsResponse.make_one(res)

    def list_members(
        self,
        res: "bs_td.ListMembersResponseTypeDef",
    ) -> "dc_td.ListMembersResponse":
        return dc_td.ListMembersResponse.make_one(res)

    def list_organization_admin_accounts(
        self,
        res: "bs_td.ListOrganizationAdminAccountsResponseTypeDef",
    ) -> "dc_td.ListOrganizationAdminAccountsResponse":
        return dc_td.ListOrganizationAdminAccountsResponse.make_one(res)

    def list_security_control_definitions(
        self,
        res: "bs_td.ListSecurityControlDefinitionsResponseTypeDef",
    ) -> "dc_td.ListSecurityControlDefinitionsResponse":
        return dc_td.ListSecurityControlDefinitionsResponse.make_one(res)

    def list_standards_control_associations(
        self,
        res: "bs_td.ListStandardsControlAssociationsResponseTypeDef",
    ) -> "dc_td.ListStandardsControlAssociationsResponse":
        return dc_td.ListStandardsControlAssociationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_configuration_policy_association(
        self,
        res: "bs_td.StartConfigurationPolicyAssociationResponseTypeDef",
    ) -> "dc_td.StartConfigurationPolicyAssociationResponse":
        return dc_td.StartConfigurationPolicyAssociationResponse.make_one(res)

    def update_aggregator_v2(
        self,
        res: "bs_td.UpdateAggregatorV2ResponseTypeDef",
    ) -> "dc_td.UpdateAggregatorV2Response":
        return dc_td.UpdateAggregatorV2Response.make_one(res)

    def update_configuration_policy(
        self,
        res: "bs_td.UpdateConfigurationPolicyResponseTypeDef",
    ) -> "dc_td.UpdateConfigurationPolicyResponse":
        return dc_td.UpdateConfigurationPolicyResponse.make_one(res)

    def update_finding_aggregator(
        self,
        res: "bs_td.UpdateFindingAggregatorResponseTypeDef",
    ) -> "dc_td.UpdateFindingAggregatorResponse":
        return dc_td.UpdateFindingAggregatorResponse.make_one(res)


securityhub_caster = SECURITYHUBCaster()
