# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_network_firewall import type_defs as bs_td


class NETWORK_FIREWALLCaster:

    def accept_network_firewall_transit_gateway_attachment(
        self,
        res: "bs_td.AcceptNetworkFirewallTransitGatewayAttachmentResponseTypeDef",
    ) -> "dc_td.AcceptNetworkFirewallTransitGatewayAttachmentResponse":
        return dc_td.AcceptNetworkFirewallTransitGatewayAttachmentResponse.make_one(res)

    def associate_availability_zones(
        self,
        res: "bs_td.AssociateAvailabilityZonesResponseTypeDef",
    ) -> "dc_td.AssociateAvailabilityZonesResponse":
        return dc_td.AssociateAvailabilityZonesResponse.make_one(res)

    def associate_firewall_policy(
        self,
        res: "bs_td.AssociateFirewallPolicyResponseTypeDef",
    ) -> "dc_td.AssociateFirewallPolicyResponse":
        return dc_td.AssociateFirewallPolicyResponse.make_one(res)

    def associate_subnets(
        self,
        res: "bs_td.AssociateSubnetsResponseTypeDef",
    ) -> "dc_td.AssociateSubnetsResponse":
        return dc_td.AssociateSubnetsResponse.make_one(res)

    def create_firewall(
        self,
        res: "bs_td.CreateFirewallResponseTypeDef",
    ) -> "dc_td.CreateFirewallResponse":
        return dc_td.CreateFirewallResponse.make_one(res)

    def create_firewall_policy(
        self,
        res: "bs_td.CreateFirewallPolicyResponseTypeDef",
    ) -> "dc_td.CreateFirewallPolicyResponse":
        return dc_td.CreateFirewallPolicyResponse.make_one(res)

    def create_rule_group(
        self,
        res: "bs_td.CreateRuleGroupResponseTypeDef",
    ) -> "dc_td.CreateRuleGroupResponse":
        return dc_td.CreateRuleGroupResponse.make_one(res)

    def create_tls_inspection_configuration(
        self,
        res: "bs_td.CreateTLSInspectionConfigurationResponseTypeDef",
    ) -> "dc_td.CreateTLSInspectionConfigurationResponse":
        return dc_td.CreateTLSInspectionConfigurationResponse.make_one(res)

    def create_vpc_endpoint_association(
        self,
        res: "bs_td.CreateVpcEndpointAssociationResponseTypeDef",
    ) -> "dc_td.CreateVpcEndpointAssociationResponse":
        return dc_td.CreateVpcEndpointAssociationResponse.make_one(res)

    def delete_firewall(
        self,
        res: "bs_td.DeleteFirewallResponseTypeDef",
    ) -> "dc_td.DeleteFirewallResponse":
        return dc_td.DeleteFirewallResponse.make_one(res)

    def delete_firewall_policy(
        self,
        res: "bs_td.DeleteFirewallPolicyResponseTypeDef",
    ) -> "dc_td.DeleteFirewallPolicyResponse":
        return dc_td.DeleteFirewallPolicyResponse.make_one(res)

    def delete_network_firewall_transit_gateway_attachment(
        self,
        res: "bs_td.DeleteNetworkFirewallTransitGatewayAttachmentResponseTypeDef",
    ) -> "dc_td.DeleteNetworkFirewallTransitGatewayAttachmentResponse":
        return dc_td.DeleteNetworkFirewallTransitGatewayAttachmentResponse.make_one(res)

    def delete_rule_group(
        self,
        res: "bs_td.DeleteRuleGroupResponseTypeDef",
    ) -> "dc_td.DeleteRuleGroupResponse":
        return dc_td.DeleteRuleGroupResponse.make_one(res)

    def delete_tls_inspection_configuration(
        self,
        res: "bs_td.DeleteTLSInspectionConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteTLSInspectionConfigurationResponse":
        return dc_td.DeleteTLSInspectionConfigurationResponse.make_one(res)

    def delete_vpc_endpoint_association(
        self,
        res: "bs_td.DeleteVpcEndpointAssociationResponseTypeDef",
    ) -> "dc_td.DeleteVpcEndpointAssociationResponse":
        return dc_td.DeleteVpcEndpointAssociationResponse.make_one(res)

    def describe_firewall(
        self,
        res: "bs_td.DescribeFirewallResponseTypeDef",
    ) -> "dc_td.DescribeFirewallResponse":
        return dc_td.DescribeFirewallResponse.make_one(res)

    def describe_firewall_metadata(
        self,
        res: "bs_td.DescribeFirewallMetadataResponseTypeDef",
    ) -> "dc_td.DescribeFirewallMetadataResponse":
        return dc_td.DescribeFirewallMetadataResponse.make_one(res)

    def describe_firewall_policy(
        self,
        res: "bs_td.DescribeFirewallPolicyResponseTypeDef",
    ) -> "dc_td.DescribeFirewallPolicyResponse":
        return dc_td.DescribeFirewallPolicyResponse.make_one(res)

    def describe_flow_operation(
        self,
        res: "bs_td.DescribeFlowOperationResponseTypeDef",
    ) -> "dc_td.DescribeFlowOperationResponse":
        return dc_td.DescribeFlowOperationResponse.make_one(res)

    def describe_logging_configuration(
        self,
        res: "bs_td.DescribeLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeLoggingConfigurationResponse":
        return dc_td.DescribeLoggingConfigurationResponse.make_one(res)

    def describe_resource_policy(
        self,
        res: "bs_td.DescribeResourcePolicyResponseTypeDef",
    ) -> "dc_td.DescribeResourcePolicyResponse":
        return dc_td.DescribeResourcePolicyResponse.make_one(res)

    def describe_rule_group(
        self,
        res: "bs_td.DescribeRuleGroupResponseTypeDef",
    ) -> "dc_td.DescribeRuleGroupResponse":
        return dc_td.DescribeRuleGroupResponse.make_one(res)

    def describe_rule_group_metadata(
        self,
        res: "bs_td.DescribeRuleGroupMetadataResponseTypeDef",
    ) -> "dc_td.DescribeRuleGroupMetadataResponse":
        return dc_td.DescribeRuleGroupMetadataResponse.make_one(res)

    def describe_rule_group_summary(
        self,
        res: "bs_td.DescribeRuleGroupSummaryResponseTypeDef",
    ) -> "dc_td.DescribeRuleGroupSummaryResponse":
        return dc_td.DescribeRuleGroupSummaryResponse.make_one(res)

    def describe_tls_inspection_configuration(
        self,
        res: "bs_td.DescribeTLSInspectionConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeTLSInspectionConfigurationResponse":
        return dc_td.DescribeTLSInspectionConfigurationResponse.make_one(res)

    def describe_vpc_endpoint_association(
        self,
        res: "bs_td.DescribeVpcEndpointAssociationResponseTypeDef",
    ) -> "dc_td.DescribeVpcEndpointAssociationResponse":
        return dc_td.DescribeVpcEndpointAssociationResponse.make_one(res)

    def disassociate_availability_zones(
        self,
        res: "bs_td.DisassociateAvailabilityZonesResponseTypeDef",
    ) -> "dc_td.DisassociateAvailabilityZonesResponse":
        return dc_td.DisassociateAvailabilityZonesResponse.make_one(res)

    def disassociate_subnets(
        self,
        res: "bs_td.DisassociateSubnetsResponseTypeDef",
    ) -> "dc_td.DisassociateSubnetsResponse":
        return dc_td.DisassociateSubnetsResponse.make_one(res)

    def get_analysis_report_results(
        self,
        res: "bs_td.GetAnalysisReportResultsResponseTypeDef",
    ) -> "dc_td.GetAnalysisReportResultsResponse":
        return dc_td.GetAnalysisReportResultsResponse.make_one(res)

    def list_analysis_reports(
        self,
        res: "bs_td.ListAnalysisReportsResponseTypeDef",
    ) -> "dc_td.ListAnalysisReportsResponse":
        return dc_td.ListAnalysisReportsResponse.make_one(res)

    def list_firewall_policies(
        self,
        res: "bs_td.ListFirewallPoliciesResponseTypeDef",
    ) -> "dc_td.ListFirewallPoliciesResponse":
        return dc_td.ListFirewallPoliciesResponse.make_one(res)

    def list_firewalls(
        self,
        res: "bs_td.ListFirewallsResponseTypeDef",
    ) -> "dc_td.ListFirewallsResponse":
        return dc_td.ListFirewallsResponse.make_one(res)

    def list_flow_operation_results(
        self,
        res: "bs_td.ListFlowOperationResultsResponseTypeDef",
    ) -> "dc_td.ListFlowOperationResultsResponse":
        return dc_td.ListFlowOperationResultsResponse.make_one(res)

    def list_flow_operations(
        self,
        res: "bs_td.ListFlowOperationsResponseTypeDef",
    ) -> "dc_td.ListFlowOperationsResponse":
        return dc_td.ListFlowOperationsResponse.make_one(res)

    def list_rule_groups(
        self,
        res: "bs_td.ListRuleGroupsResponseTypeDef",
    ) -> "dc_td.ListRuleGroupsResponse":
        return dc_td.ListRuleGroupsResponse.make_one(res)

    def list_tls_inspection_configurations(
        self,
        res: "bs_td.ListTLSInspectionConfigurationsResponseTypeDef",
    ) -> "dc_td.ListTLSInspectionConfigurationsResponse":
        return dc_td.ListTLSInspectionConfigurationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_vpc_endpoint_associations(
        self,
        res: "bs_td.ListVpcEndpointAssociationsResponseTypeDef",
    ) -> "dc_td.ListVpcEndpointAssociationsResponse":
        return dc_td.ListVpcEndpointAssociationsResponse.make_one(res)

    def reject_network_firewall_transit_gateway_attachment(
        self,
        res: "bs_td.RejectNetworkFirewallTransitGatewayAttachmentResponseTypeDef",
    ) -> "dc_td.RejectNetworkFirewallTransitGatewayAttachmentResponse":
        return dc_td.RejectNetworkFirewallTransitGatewayAttachmentResponse.make_one(res)

    def start_analysis_report(
        self,
        res: "bs_td.StartAnalysisReportResponseTypeDef",
    ) -> "dc_td.StartAnalysisReportResponse":
        return dc_td.StartAnalysisReportResponse.make_one(res)

    def start_flow_capture(
        self,
        res: "bs_td.StartFlowCaptureResponseTypeDef",
    ) -> "dc_td.StartFlowCaptureResponse":
        return dc_td.StartFlowCaptureResponse.make_one(res)

    def start_flow_flush(
        self,
        res: "bs_td.StartFlowFlushResponseTypeDef",
    ) -> "dc_td.StartFlowFlushResponse":
        return dc_td.StartFlowFlushResponse.make_one(res)

    def update_availability_zone_change_protection(
        self,
        res: "bs_td.UpdateAvailabilityZoneChangeProtectionResponseTypeDef",
    ) -> "dc_td.UpdateAvailabilityZoneChangeProtectionResponse":
        return dc_td.UpdateAvailabilityZoneChangeProtectionResponse.make_one(res)

    def update_firewall_analysis_settings(
        self,
        res: "bs_td.UpdateFirewallAnalysisSettingsResponseTypeDef",
    ) -> "dc_td.UpdateFirewallAnalysisSettingsResponse":
        return dc_td.UpdateFirewallAnalysisSettingsResponse.make_one(res)

    def update_firewall_delete_protection(
        self,
        res: "bs_td.UpdateFirewallDeleteProtectionResponseTypeDef",
    ) -> "dc_td.UpdateFirewallDeleteProtectionResponse":
        return dc_td.UpdateFirewallDeleteProtectionResponse.make_one(res)

    def update_firewall_description(
        self,
        res: "bs_td.UpdateFirewallDescriptionResponseTypeDef",
    ) -> "dc_td.UpdateFirewallDescriptionResponse":
        return dc_td.UpdateFirewallDescriptionResponse.make_one(res)

    def update_firewall_encryption_configuration(
        self,
        res: "bs_td.UpdateFirewallEncryptionConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateFirewallEncryptionConfigurationResponse":
        return dc_td.UpdateFirewallEncryptionConfigurationResponse.make_one(res)

    def update_firewall_policy(
        self,
        res: "bs_td.UpdateFirewallPolicyResponseTypeDef",
    ) -> "dc_td.UpdateFirewallPolicyResponse":
        return dc_td.UpdateFirewallPolicyResponse.make_one(res)

    def update_firewall_policy_change_protection(
        self,
        res: "bs_td.UpdateFirewallPolicyChangeProtectionResponseTypeDef",
    ) -> "dc_td.UpdateFirewallPolicyChangeProtectionResponse":
        return dc_td.UpdateFirewallPolicyChangeProtectionResponse.make_one(res)

    def update_logging_configuration(
        self,
        res: "bs_td.UpdateLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateLoggingConfigurationResponse":
        return dc_td.UpdateLoggingConfigurationResponse.make_one(res)

    def update_rule_group(
        self,
        res: "bs_td.UpdateRuleGroupResponseTypeDef",
    ) -> "dc_td.UpdateRuleGroupResponse":
        return dc_td.UpdateRuleGroupResponse.make_one(res)

    def update_subnet_change_protection(
        self,
        res: "bs_td.UpdateSubnetChangeProtectionResponseTypeDef",
    ) -> "dc_td.UpdateSubnetChangeProtectionResponse":
        return dc_td.UpdateSubnetChangeProtectionResponse.make_one(res)

    def update_tls_inspection_configuration(
        self,
        res: "bs_td.UpdateTLSInspectionConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateTLSInspectionConfigurationResponse":
        return dc_td.UpdateTLSInspectionConfigurationResponse.make_one(res)


network_firewall_caster = NETWORK_FIREWALLCaster()
