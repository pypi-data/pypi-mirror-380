# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_route53resolver import type_defs as bs_td


class ROUTE53RESOLVERCaster:

    def associate_firewall_rule_group(
        self,
        res: "bs_td.AssociateFirewallRuleGroupResponseTypeDef",
    ) -> "dc_td.AssociateFirewallRuleGroupResponse":
        return dc_td.AssociateFirewallRuleGroupResponse.make_one(res)

    def associate_resolver_endpoint_ip_address(
        self,
        res: "bs_td.AssociateResolverEndpointIpAddressResponseTypeDef",
    ) -> "dc_td.AssociateResolverEndpointIpAddressResponse":
        return dc_td.AssociateResolverEndpointIpAddressResponse.make_one(res)

    def associate_resolver_query_log_config(
        self,
        res: "bs_td.AssociateResolverQueryLogConfigResponseTypeDef",
    ) -> "dc_td.AssociateResolverQueryLogConfigResponse":
        return dc_td.AssociateResolverQueryLogConfigResponse.make_one(res)

    def associate_resolver_rule(
        self,
        res: "bs_td.AssociateResolverRuleResponseTypeDef",
    ) -> "dc_td.AssociateResolverRuleResponse":
        return dc_td.AssociateResolverRuleResponse.make_one(res)

    def create_firewall_domain_list(
        self,
        res: "bs_td.CreateFirewallDomainListResponseTypeDef",
    ) -> "dc_td.CreateFirewallDomainListResponse":
        return dc_td.CreateFirewallDomainListResponse.make_one(res)

    def create_firewall_rule(
        self,
        res: "bs_td.CreateFirewallRuleResponseTypeDef",
    ) -> "dc_td.CreateFirewallRuleResponse":
        return dc_td.CreateFirewallRuleResponse.make_one(res)

    def create_firewall_rule_group(
        self,
        res: "bs_td.CreateFirewallRuleGroupResponseTypeDef",
    ) -> "dc_td.CreateFirewallRuleGroupResponse":
        return dc_td.CreateFirewallRuleGroupResponse.make_one(res)

    def create_outpost_resolver(
        self,
        res: "bs_td.CreateOutpostResolverResponseTypeDef",
    ) -> "dc_td.CreateOutpostResolverResponse":
        return dc_td.CreateOutpostResolverResponse.make_one(res)

    def create_resolver_endpoint(
        self,
        res: "bs_td.CreateResolverEndpointResponseTypeDef",
    ) -> "dc_td.CreateResolverEndpointResponse":
        return dc_td.CreateResolverEndpointResponse.make_one(res)

    def create_resolver_query_log_config(
        self,
        res: "bs_td.CreateResolverQueryLogConfigResponseTypeDef",
    ) -> "dc_td.CreateResolverQueryLogConfigResponse":
        return dc_td.CreateResolverQueryLogConfigResponse.make_one(res)

    def create_resolver_rule(
        self,
        res: "bs_td.CreateResolverRuleResponseTypeDef",
    ) -> "dc_td.CreateResolverRuleResponse":
        return dc_td.CreateResolverRuleResponse.make_one(res)

    def delete_firewall_domain_list(
        self,
        res: "bs_td.DeleteFirewallDomainListResponseTypeDef",
    ) -> "dc_td.DeleteFirewallDomainListResponse":
        return dc_td.DeleteFirewallDomainListResponse.make_one(res)

    def delete_firewall_rule(
        self,
        res: "bs_td.DeleteFirewallRuleResponseTypeDef",
    ) -> "dc_td.DeleteFirewallRuleResponse":
        return dc_td.DeleteFirewallRuleResponse.make_one(res)

    def delete_firewall_rule_group(
        self,
        res: "bs_td.DeleteFirewallRuleGroupResponseTypeDef",
    ) -> "dc_td.DeleteFirewallRuleGroupResponse":
        return dc_td.DeleteFirewallRuleGroupResponse.make_one(res)

    def delete_outpost_resolver(
        self,
        res: "bs_td.DeleteOutpostResolverResponseTypeDef",
    ) -> "dc_td.DeleteOutpostResolverResponse":
        return dc_td.DeleteOutpostResolverResponse.make_one(res)

    def delete_resolver_endpoint(
        self,
        res: "bs_td.DeleteResolverEndpointResponseTypeDef",
    ) -> "dc_td.DeleteResolverEndpointResponse":
        return dc_td.DeleteResolverEndpointResponse.make_one(res)

    def delete_resolver_query_log_config(
        self,
        res: "bs_td.DeleteResolverQueryLogConfigResponseTypeDef",
    ) -> "dc_td.DeleteResolverQueryLogConfigResponse":
        return dc_td.DeleteResolverQueryLogConfigResponse.make_one(res)

    def delete_resolver_rule(
        self,
        res: "bs_td.DeleteResolverRuleResponseTypeDef",
    ) -> "dc_td.DeleteResolverRuleResponse":
        return dc_td.DeleteResolverRuleResponse.make_one(res)

    def disassociate_firewall_rule_group(
        self,
        res: "bs_td.DisassociateFirewallRuleGroupResponseTypeDef",
    ) -> "dc_td.DisassociateFirewallRuleGroupResponse":
        return dc_td.DisassociateFirewallRuleGroupResponse.make_one(res)

    def disassociate_resolver_endpoint_ip_address(
        self,
        res: "bs_td.DisassociateResolverEndpointIpAddressResponseTypeDef",
    ) -> "dc_td.DisassociateResolverEndpointIpAddressResponse":
        return dc_td.DisassociateResolverEndpointIpAddressResponse.make_one(res)

    def disassociate_resolver_query_log_config(
        self,
        res: "bs_td.DisassociateResolverQueryLogConfigResponseTypeDef",
    ) -> "dc_td.DisassociateResolverQueryLogConfigResponse":
        return dc_td.DisassociateResolverQueryLogConfigResponse.make_one(res)

    def disassociate_resolver_rule(
        self,
        res: "bs_td.DisassociateResolverRuleResponseTypeDef",
    ) -> "dc_td.DisassociateResolverRuleResponse":
        return dc_td.DisassociateResolverRuleResponse.make_one(res)

    def get_firewall_config(
        self,
        res: "bs_td.GetFirewallConfigResponseTypeDef",
    ) -> "dc_td.GetFirewallConfigResponse":
        return dc_td.GetFirewallConfigResponse.make_one(res)

    def get_firewall_domain_list(
        self,
        res: "bs_td.GetFirewallDomainListResponseTypeDef",
    ) -> "dc_td.GetFirewallDomainListResponse":
        return dc_td.GetFirewallDomainListResponse.make_one(res)

    def get_firewall_rule_group(
        self,
        res: "bs_td.GetFirewallRuleGroupResponseTypeDef",
    ) -> "dc_td.GetFirewallRuleGroupResponse":
        return dc_td.GetFirewallRuleGroupResponse.make_one(res)

    def get_firewall_rule_group_association(
        self,
        res: "bs_td.GetFirewallRuleGroupAssociationResponseTypeDef",
    ) -> "dc_td.GetFirewallRuleGroupAssociationResponse":
        return dc_td.GetFirewallRuleGroupAssociationResponse.make_one(res)

    def get_firewall_rule_group_policy(
        self,
        res: "bs_td.GetFirewallRuleGroupPolicyResponseTypeDef",
    ) -> "dc_td.GetFirewallRuleGroupPolicyResponse":
        return dc_td.GetFirewallRuleGroupPolicyResponse.make_one(res)

    def get_outpost_resolver(
        self,
        res: "bs_td.GetOutpostResolverResponseTypeDef",
    ) -> "dc_td.GetOutpostResolverResponse":
        return dc_td.GetOutpostResolverResponse.make_one(res)

    def get_resolver_config(
        self,
        res: "bs_td.GetResolverConfigResponseTypeDef",
    ) -> "dc_td.GetResolverConfigResponse":
        return dc_td.GetResolverConfigResponse.make_one(res)

    def get_resolver_dnssec_config(
        self,
        res: "bs_td.GetResolverDnssecConfigResponseTypeDef",
    ) -> "dc_td.GetResolverDnssecConfigResponse":
        return dc_td.GetResolverDnssecConfigResponse.make_one(res)

    def get_resolver_endpoint(
        self,
        res: "bs_td.GetResolverEndpointResponseTypeDef",
    ) -> "dc_td.GetResolverEndpointResponse":
        return dc_td.GetResolverEndpointResponse.make_one(res)

    def get_resolver_query_log_config(
        self,
        res: "bs_td.GetResolverQueryLogConfigResponseTypeDef",
    ) -> "dc_td.GetResolverQueryLogConfigResponse":
        return dc_td.GetResolverQueryLogConfigResponse.make_one(res)

    def get_resolver_query_log_config_association(
        self,
        res: "bs_td.GetResolverQueryLogConfigAssociationResponseTypeDef",
    ) -> "dc_td.GetResolverQueryLogConfigAssociationResponse":
        return dc_td.GetResolverQueryLogConfigAssociationResponse.make_one(res)

    def get_resolver_query_log_config_policy(
        self,
        res: "bs_td.GetResolverQueryLogConfigPolicyResponseTypeDef",
    ) -> "dc_td.GetResolverQueryLogConfigPolicyResponse":
        return dc_td.GetResolverQueryLogConfigPolicyResponse.make_one(res)

    def get_resolver_rule(
        self,
        res: "bs_td.GetResolverRuleResponseTypeDef",
    ) -> "dc_td.GetResolverRuleResponse":
        return dc_td.GetResolverRuleResponse.make_one(res)

    def get_resolver_rule_association(
        self,
        res: "bs_td.GetResolverRuleAssociationResponseTypeDef",
    ) -> "dc_td.GetResolverRuleAssociationResponse":
        return dc_td.GetResolverRuleAssociationResponse.make_one(res)

    def get_resolver_rule_policy(
        self,
        res: "bs_td.GetResolverRulePolicyResponseTypeDef",
    ) -> "dc_td.GetResolverRulePolicyResponse":
        return dc_td.GetResolverRulePolicyResponse.make_one(res)

    def import_firewall_domains(
        self,
        res: "bs_td.ImportFirewallDomainsResponseTypeDef",
    ) -> "dc_td.ImportFirewallDomainsResponse":
        return dc_td.ImportFirewallDomainsResponse.make_one(res)

    def list_firewall_configs(
        self,
        res: "bs_td.ListFirewallConfigsResponseTypeDef",
    ) -> "dc_td.ListFirewallConfigsResponse":
        return dc_td.ListFirewallConfigsResponse.make_one(res)

    def list_firewall_domain_lists(
        self,
        res: "bs_td.ListFirewallDomainListsResponseTypeDef",
    ) -> "dc_td.ListFirewallDomainListsResponse":
        return dc_td.ListFirewallDomainListsResponse.make_one(res)

    def list_firewall_domains(
        self,
        res: "bs_td.ListFirewallDomainsResponseTypeDef",
    ) -> "dc_td.ListFirewallDomainsResponse":
        return dc_td.ListFirewallDomainsResponse.make_one(res)

    def list_firewall_rule_group_associations(
        self,
        res: "bs_td.ListFirewallRuleGroupAssociationsResponseTypeDef",
    ) -> "dc_td.ListFirewallRuleGroupAssociationsResponse":
        return dc_td.ListFirewallRuleGroupAssociationsResponse.make_one(res)

    def list_firewall_rule_groups(
        self,
        res: "bs_td.ListFirewallRuleGroupsResponseTypeDef",
    ) -> "dc_td.ListFirewallRuleGroupsResponse":
        return dc_td.ListFirewallRuleGroupsResponse.make_one(res)

    def list_firewall_rules(
        self,
        res: "bs_td.ListFirewallRulesResponseTypeDef",
    ) -> "dc_td.ListFirewallRulesResponse":
        return dc_td.ListFirewallRulesResponse.make_one(res)

    def list_outpost_resolvers(
        self,
        res: "bs_td.ListOutpostResolversResponseTypeDef",
    ) -> "dc_td.ListOutpostResolversResponse":
        return dc_td.ListOutpostResolversResponse.make_one(res)

    def list_resolver_configs(
        self,
        res: "bs_td.ListResolverConfigsResponseTypeDef",
    ) -> "dc_td.ListResolverConfigsResponse":
        return dc_td.ListResolverConfigsResponse.make_one(res)

    def list_resolver_dnssec_configs(
        self,
        res: "bs_td.ListResolverDnssecConfigsResponseTypeDef",
    ) -> "dc_td.ListResolverDnssecConfigsResponse":
        return dc_td.ListResolverDnssecConfigsResponse.make_one(res)

    def list_resolver_endpoint_ip_addresses(
        self,
        res: "bs_td.ListResolverEndpointIpAddressesResponseTypeDef",
    ) -> "dc_td.ListResolverEndpointIpAddressesResponse":
        return dc_td.ListResolverEndpointIpAddressesResponse.make_one(res)

    def list_resolver_endpoints(
        self,
        res: "bs_td.ListResolverEndpointsResponseTypeDef",
    ) -> "dc_td.ListResolverEndpointsResponse":
        return dc_td.ListResolverEndpointsResponse.make_one(res)

    def list_resolver_query_log_config_associations(
        self,
        res: "bs_td.ListResolverQueryLogConfigAssociationsResponseTypeDef",
    ) -> "dc_td.ListResolverQueryLogConfigAssociationsResponse":
        return dc_td.ListResolverQueryLogConfigAssociationsResponse.make_one(res)

    def list_resolver_query_log_configs(
        self,
        res: "bs_td.ListResolverQueryLogConfigsResponseTypeDef",
    ) -> "dc_td.ListResolverQueryLogConfigsResponse":
        return dc_td.ListResolverQueryLogConfigsResponse.make_one(res)

    def list_resolver_rule_associations(
        self,
        res: "bs_td.ListResolverRuleAssociationsResponseTypeDef",
    ) -> "dc_td.ListResolverRuleAssociationsResponse":
        return dc_td.ListResolverRuleAssociationsResponse.make_one(res)

    def list_resolver_rules(
        self,
        res: "bs_td.ListResolverRulesResponseTypeDef",
    ) -> "dc_td.ListResolverRulesResponse":
        return dc_td.ListResolverRulesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_firewall_rule_group_policy(
        self,
        res: "bs_td.PutFirewallRuleGroupPolicyResponseTypeDef",
    ) -> "dc_td.PutFirewallRuleGroupPolicyResponse":
        return dc_td.PutFirewallRuleGroupPolicyResponse.make_one(res)

    def put_resolver_query_log_config_policy(
        self,
        res: "bs_td.PutResolverQueryLogConfigPolicyResponseTypeDef",
    ) -> "dc_td.PutResolverQueryLogConfigPolicyResponse":
        return dc_td.PutResolverQueryLogConfigPolicyResponse.make_one(res)

    def put_resolver_rule_policy(
        self,
        res: "bs_td.PutResolverRulePolicyResponseTypeDef",
    ) -> "dc_td.PutResolverRulePolicyResponse":
        return dc_td.PutResolverRulePolicyResponse.make_one(res)

    def update_firewall_config(
        self,
        res: "bs_td.UpdateFirewallConfigResponseTypeDef",
    ) -> "dc_td.UpdateFirewallConfigResponse":
        return dc_td.UpdateFirewallConfigResponse.make_one(res)

    def update_firewall_domains(
        self,
        res: "bs_td.UpdateFirewallDomainsResponseTypeDef",
    ) -> "dc_td.UpdateFirewallDomainsResponse":
        return dc_td.UpdateFirewallDomainsResponse.make_one(res)

    def update_firewall_rule(
        self,
        res: "bs_td.UpdateFirewallRuleResponseTypeDef",
    ) -> "dc_td.UpdateFirewallRuleResponse":
        return dc_td.UpdateFirewallRuleResponse.make_one(res)

    def update_firewall_rule_group_association(
        self,
        res: "bs_td.UpdateFirewallRuleGroupAssociationResponseTypeDef",
    ) -> "dc_td.UpdateFirewallRuleGroupAssociationResponse":
        return dc_td.UpdateFirewallRuleGroupAssociationResponse.make_one(res)

    def update_outpost_resolver(
        self,
        res: "bs_td.UpdateOutpostResolverResponseTypeDef",
    ) -> "dc_td.UpdateOutpostResolverResponse":
        return dc_td.UpdateOutpostResolverResponse.make_one(res)

    def update_resolver_config(
        self,
        res: "bs_td.UpdateResolverConfigResponseTypeDef",
    ) -> "dc_td.UpdateResolverConfigResponse":
        return dc_td.UpdateResolverConfigResponse.make_one(res)

    def update_resolver_dnssec_config(
        self,
        res: "bs_td.UpdateResolverDnssecConfigResponseTypeDef",
    ) -> "dc_td.UpdateResolverDnssecConfigResponse":
        return dc_td.UpdateResolverDnssecConfigResponse.make_one(res)

    def update_resolver_endpoint(
        self,
        res: "bs_td.UpdateResolverEndpointResponseTypeDef",
    ) -> "dc_td.UpdateResolverEndpointResponse":
        return dc_td.UpdateResolverEndpointResponse.make_one(res)

    def update_resolver_rule(
        self,
        res: "bs_td.UpdateResolverRuleResponseTypeDef",
    ) -> "dc_td.UpdateResolverRuleResponse":
        return dc_td.UpdateResolverRuleResponse.make_one(res)


route53resolver_caster = ROUTE53RESOLVERCaster()
