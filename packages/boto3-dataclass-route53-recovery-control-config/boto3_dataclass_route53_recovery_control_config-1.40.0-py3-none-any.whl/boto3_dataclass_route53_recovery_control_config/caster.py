# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_route53_recovery_control_config import type_defs as bs_td


class ROUTE53_RECOVERY_CONTROL_CONFIGCaster:

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResponseTypeDef",
    ) -> "dc_td.CreateClusterResponse":
        return dc_td.CreateClusterResponse.make_one(res)

    def create_control_panel(
        self,
        res: "bs_td.CreateControlPanelResponseTypeDef",
    ) -> "dc_td.CreateControlPanelResponse":
        return dc_td.CreateControlPanelResponse.make_one(res)

    def create_routing_control(
        self,
        res: "bs_td.CreateRoutingControlResponseTypeDef",
    ) -> "dc_td.CreateRoutingControlResponse":
        return dc_td.CreateRoutingControlResponse.make_one(res)

    def create_safety_rule(
        self,
        res: "bs_td.CreateSafetyRuleResponseTypeDef",
    ) -> "dc_td.CreateSafetyRuleResponse":
        return dc_td.CreateSafetyRuleResponse.make_one(res)

    def describe_cluster(
        self,
        res: "bs_td.DescribeClusterResponseTypeDef",
    ) -> "dc_td.DescribeClusterResponse":
        return dc_td.DescribeClusterResponse.make_one(res)

    def describe_control_panel(
        self,
        res: "bs_td.DescribeControlPanelResponseTypeDef",
    ) -> "dc_td.DescribeControlPanelResponse":
        return dc_td.DescribeControlPanelResponse.make_one(res)

    def describe_routing_control(
        self,
        res: "bs_td.DescribeRoutingControlResponseTypeDef",
    ) -> "dc_td.DescribeRoutingControlResponse":
        return dc_td.DescribeRoutingControlResponse.make_one(res)

    def describe_safety_rule(
        self,
        res: "bs_td.DescribeSafetyRuleResponseTypeDef",
    ) -> "dc_td.DescribeSafetyRuleResponse":
        return dc_td.DescribeSafetyRuleResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def list_associated_route53_health_checks(
        self,
        res: "bs_td.ListAssociatedRoute53HealthChecksResponseTypeDef",
    ) -> "dc_td.ListAssociatedRoute53HealthChecksResponse":
        return dc_td.ListAssociatedRoute53HealthChecksResponse.make_one(res)

    def list_clusters(
        self,
        res: "bs_td.ListClustersResponseTypeDef",
    ) -> "dc_td.ListClustersResponse":
        return dc_td.ListClustersResponse.make_one(res)

    def list_control_panels(
        self,
        res: "bs_td.ListControlPanelsResponseTypeDef",
    ) -> "dc_td.ListControlPanelsResponse":
        return dc_td.ListControlPanelsResponse.make_one(res)

    def list_routing_controls(
        self,
        res: "bs_td.ListRoutingControlsResponseTypeDef",
    ) -> "dc_td.ListRoutingControlsResponse":
        return dc_td.ListRoutingControlsResponse.make_one(res)

    def list_safety_rules(
        self,
        res: "bs_td.ListSafetyRulesResponseTypeDef",
    ) -> "dc_td.ListSafetyRulesResponse":
        return dc_td.ListSafetyRulesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_cluster(
        self,
        res: "bs_td.UpdateClusterResponseTypeDef",
    ) -> "dc_td.UpdateClusterResponse":
        return dc_td.UpdateClusterResponse.make_one(res)

    def update_control_panel(
        self,
        res: "bs_td.UpdateControlPanelResponseTypeDef",
    ) -> "dc_td.UpdateControlPanelResponse":
        return dc_td.UpdateControlPanelResponse.make_one(res)

    def update_routing_control(
        self,
        res: "bs_td.UpdateRoutingControlResponseTypeDef",
    ) -> "dc_td.UpdateRoutingControlResponse":
        return dc_td.UpdateRoutingControlResponse.make_one(res)

    def update_safety_rule(
        self,
        res: "bs_td.UpdateSafetyRuleResponseTypeDef",
    ) -> "dc_td.UpdateSafetyRuleResponse":
        return dc_td.UpdateSafetyRuleResponse.make_one(res)


route53_recovery_control_config_caster = ROUTE53_RECOVERY_CONTROL_CONFIGCaster()
