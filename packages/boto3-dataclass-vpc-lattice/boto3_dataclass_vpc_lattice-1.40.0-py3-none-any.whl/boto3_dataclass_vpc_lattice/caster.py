# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_vpc_lattice import type_defs as bs_td


class VPC_LATTICECaster:

    def batch_update_rule(
        self,
        res: "bs_td.BatchUpdateRuleResponseTypeDef",
    ) -> "dc_td.BatchUpdateRuleResponse":
        return dc_td.BatchUpdateRuleResponse.make_one(res)

    def create_access_log_subscription(
        self,
        res: "bs_td.CreateAccessLogSubscriptionResponseTypeDef",
    ) -> "dc_td.CreateAccessLogSubscriptionResponse":
        return dc_td.CreateAccessLogSubscriptionResponse.make_one(res)

    def create_listener(
        self,
        res: "bs_td.CreateListenerResponseTypeDef",
    ) -> "dc_td.CreateListenerResponse":
        return dc_td.CreateListenerResponse.make_one(res)

    def create_resource_configuration(
        self,
        res: "bs_td.CreateResourceConfigurationResponseTypeDef",
    ) -> "dc_td.CreateResourceConfigurationResponse":
        return dc_td.CreateResourceConfigurationResponse.make_one(res)

    def create_resource_gateway(
        self,
        res: "bs_td.CreateResourceGatewayResponseTypeDef",
    ) -> "dc_td.CreateResourceGatewayResponse":
        return dc_td.CreateResourceGatewayResponse.make_one(res)

    def create_rule(
        self,
        res: "bs_td.CreateRuleResponseTypeDef",
    ) -> "dc_td.CreateRuleResponse":
        return dc_td.CreateRuleResponse.make_one(res)

    def create_service(
        self,
        res: "bs_td.CreateServiceResponseTypeDef",
    ) -> "dc_td.CreateServiceResponse":
        return dc_td.CreateServiceResponse.make_one(res)

    def create_service_network(
        self,
        res: "bs_td.CreateServiceNetworkResponseTypeDef",
    ) -> "dc_td.CreateServiceNetworkResponse":
        return dc_td.CreateServiceNetworkResponse.make_one(res)

    def create_service_network_resource_association(
        self,
        res: "bs_td.CreateServiceNetworkResourceAssociationResponseTypeDef",
    ) -> "dc_td.CreateServiceNetworkResourceAssociationResponse":
        return dc_td.CreateServiceNetworkResourceAssociationResponse.make_one(res)

    def create_service_network_service_association(
        self,
        res: "bs_td.CreateServiceNetworkServiceAssociationResponseTypeDef",
    ) -> "dc_td.CreateServiceNetworkServiceAssociationResponse":
        return dc_td.CreateServiceNetworkServiceAssociationResponse.make_one(res)

    def create_service_network_vpc_association(
        self,
        res: "bs_td.CreateServiceNetworkVpcAssociationResponseTypeDef",
    ) -> "dc_td.CreateServiceNetworkVpcAssociationResponse":
        return dc_td.CreateServiceNetworkVpcAssociationResponse.make_one(res)

    def create_target_group(
        self,
        res: "bs_td.CreateTargetGroupResponseTypeDef",
    ) -> "dc_td.CreateTargetGroupResponse":
        return dc_td.CreateTargetGroupResponse.make_one(res)

    def delete_resource_endpoint_association(
        self,
        res: "bs_td.DeleteResourceEndpointAssociationResponseTypeDef",
    ) -> "dc_td.DeleteResourceEndpointAssociationResponse":
        return dc_td.DeleteResourceEndpointAssociationResponse.make_one(res)

    def delete_resource_gateway(
        self,
        res: "bs_td.DeleteResourceGatewayResponseTypeDef",
    ) -> "dc_td.DeleteResourceGatewayResponse":
        return dc_td.DeleteResourceGatewayResponse.make_one(res)

    def delete_service(
        self,
        res: "bs_td.DeleteServiceResponseTypeDef",
    ) -> "dc_td.DeleteServiceResponse":
        return dc_td.DeleteServiceResponse.make_one(res)

    def delete_service_network_resource_association(
        self,
        res: "bs_td.DeleteServiceNetworkResourceAssociationResponseTypeDef",
    ) -> "dc_td.DeleteServiceNetworkResourceAssociationResponse":
        return dc_td.DeleteServiceNetworkResourceAssociationResponse.make_one(res)

    def delete_service_network_service_association(
        self,
        res: "bs_td.DeleteServiceNetworkServiceAssociationResponseTypeDef",
    ) -> "dc_td.DeleteServiceNetworkServiceAssociationResponse":
        return dc_td.DeleteServiceNetworkServiceAssociationResponse.make_one(res)

    def delete_service_network_vpc_association(
        self,
        res: "bs_td.DeleteServiceNetworkVpcAssociationResponseTypeDef",
    ) -> "dc_td.DeleteServiceNetworkVpcAssociationResponse":
        return dc_td.DeleteServiceNetworkVpcAssociationResponse.make_one(res)

    def delete_target_group(
        self,
        res: "bs_td.DeleteTargetGroupResponseTypeDef",
    ) -> "dc_td.DeleteTargetGroupResponse":
        return dc_td.DeleteTargetGroupResponse.make_one(res)

    def deregister_targets(
        self,
        res: "bs_td.DeregisterTargetsResponseTypeDef",
    ) -> "dc_td.DeregisterTargetsResponse":
        return dc_td.DeregisterTargetsResponse.make_one(res)

    def get_access_log_subscription(
        self,
        res: "bs_td.GetAccessLogSubscriptionResponseTypeDef",
    ) -> "dc_td.GetAccessLogSubscriptionResponse":
        return dc_td.GetAccessLogSubscriptionResponse.make_one(res)

    def get_auth_policy(
        self,
        res: "bs_td.GetAuthPolicyResponseTypeDef",
    ) -> "dc_td.GetAuthPolicyResponse":
        return dc_td.GetAuthPolicyResponse.make_one(res)

    def get_listener(
        self,
        res: "bs_td.GetListenerResponseTypeDef",
    ) -> "dc_td.GetListenerResponse":
        return dc_td.GetListenerResponse.make_one(res)

    def get_resource_configuration(
        self,
        res: "bs_td.GetResourceConfigurationResponseTypeDef",
    ) -> "dc_td.GetResourceConfigurationResponse":
        return dc_td.GetResourceConfigurationResponse.make_one(res)

    def get_resource_gateway(
        self,
        res: "bs_td.GetResourceGatewayResponseTypeDef",
    ) -> "dc_td.GetResourceGatewayResponse":
        return dc_td.GetResourceGatewayResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def get_rule(
        self,
        res: "bs_td.GetRuleResponseTypeDef",
    ) -> "dc_td.GetRuleResponse":
        return dc_td.GetRuleResponse.make_one(res)

    def get_service(
        self,
        res: "bs_td.GetServiceResponseTypeDef",
    ) -> "dc_td.GetServiceResponse":
        return dc_td.GetServiceResponse.make_one(res)

    def get_service_network(
        self,
        res: "bs_td.GetServiceNetworkResponseTypeDef",
    ) -> "dc_td.GetServiceNetworkResponse":
        return dc_td.GetServiceNetworkResponse.make_one(res)

    def get_service_network_resource_association(
        self,
        res: "bs_td.GetServiceNetworkResourceAssociationResponseTypeDef",
    ) -> "dc_td.GetServiceNetworkResourceAssociationResponse":
        return dc_td.GetServiceNetworkResourceAssociationResponse.make_one(res)

    def get_service_network_service_association(
        self,
        res: "bs_td.GetServiceNetworkServiceAssociationResponseTypeDef",
    ) -> "dc_td.GetServiceNetworkServiceAssociationResponse":
        return dc_td.GetServiceNetworkServiceAssociationResponse.make_one(res)

    def get_service_network_vpc_association(
        self,
        res: "bs_td.GetServiceNetworkVpcAssociationResponseTypeDef",
    ) -> "dc_td.GetServiceNetworkVpcAssociationResponse":
        return dc_td.GetServiceNetworkVpcAssociationResponse.make_one(res)

    def get_target_group(
        self,
        res: "bs_td.GetTargetGroupResponseTypeDef",
    ) -> "dc_td.GetTargetGroupResponse":
        return dc_td.GetTargetGroupResponse.make_one(res)

    def list_access_log_subscriptions(
        self,
        res: "bs_td.ListAccessLogSubscriptionsResponseTypeDef",
    ) -> "dc_td.ListAccessLogSubscriptionsResponse":
        return dc_td.ListAccessLogSubscriptionsResponse.make_one(res)

    def list_listeners(
        self,
        res: "bs_td.ListListenersResponseTypeDef",
    ) -> "dc_td.ListListenersResponse":
        return dc_td.ListListenersResponse.make_one(res)

    def list_resource_configurations(
        self,
        res: "bs_td.ListResourceConfigurationsResponseTypeDef",
    ) -> "dc_td.ListResourceConfigurationsResponse":
        return dc_td.ListResourceConfigurationsResponse.make_one(res)

    def list_resource_endpoint_associations(
        self,
        res: "bs_td.ListResourceEndpointAssociationsResponseTypeDef",
    ) -> "dc_td.ListResourceEndpointAssociationsResponse":
        return dc_td.ListResourceEndpointAssociationsResponse.make_one(res)

    def list_resource_gateways(
        self,
        res: "bs_td.ListResourceGatewaysResponseTypeDef",
    ) -> "dc_td.ListResourceGatewaysResponse":
        return dc_td.ListResourceGatewaysResponse.make_one(res)

    def list_rules(
        self,
        res: "bs_td.ListRulesResponseTypeDef",
    ) -> "dc_td.ListRulesResponse":
        return dc_td.ListRulesResponse.make_one(res)

    def list_service_network_resource_associations(
        self,
        res: "bs_td.ListServiceNetworkResourceAssociationsResponseTypeDef",
    ) -> "dc_td.ListServiceNetworkResourceAssociationsResponse":
        return dc_td.ListServiceNetworkResourceAssociationsResponse.make_one(res)

    def list_service_network_service_associations(
        self,
        res: "bs_td.ListServiceNetworkServiceAssociationsResponseTypeDef",
    ) -> "dc_td.ListServiceNetworkServiceAssociationsResponse":
        return dc_td.ListServiceNetworkServiceAssociationsResponse.make_one(res)

    def list_service_network_vpc_associations(
        self,
        res: "bs_td.ListServiceNetworkVpcAssociationsResponseTypeDef",
    ) -> "dc_td.ListServiceNetworkVpcAssociationsResponse":
        return dc_td.ListServiceNetworkVpcAssociationsResponse.make_one(res)

    def list_service_network_vpc_endpoint_associations(
        self,
        res: "bs_td.ListServiceNetworkVpcEndpointAssociationsResponseTypeDef",
    ) -> "dc_td.ListServiceNetworkVpcEndpointAssociationsResponse":
        return dc_td.ListServiceNetworkVpcEndpointAssociationsResponse.make_one(res)

    def list_service_networks(
        self,
        res: "bs_td.ListServiceNetworksResponseTypeDef",
    ) -> "dc_td.ListServiceNetworksResponse":
        return dc_td.ListServiceNetworksResponse.make_one(res)

    def list_services(
        self,
        res: "bs_td.ListServicesResponseTypeDef",
    ) -> "dc_td.ListServicesResponse":
        return dc_td.ListServicesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_target_groups(
        self,
        res: "bs_td.ListTargetGroupsResponseTypeDef",
    ) -> "dc_td.ListTargetGroupsResponse":
        return dc_td.ListTargetGroupsResponse.make_one(res)

    def list_targets(
        self,
        res: "bs_td.ListTargetsResponseTypeDef",
    ) -> "dc_td.ListTargetsResponse":
        return dc_td.ListTargetsResponse.make_one(res)

    def put_auth_policy(
        self,
        res: "bs_td.PutAuthPolicyResponseTypeDef",
    ) -> "dc_td.PutAuthPolicyResponse":
        return dc_td.PutAuthPolicyResponse.make_one(res)

    def register_targets(
        self,
        res: "bs_td.RegisterTargetsResponseTypeDef",
    ) -> "dc_td.RegisterTargetsResponse":
        return dc_td.RegisterTargetsResponse.make_one(res)

    def update_access_log_subscription(
        self,
        res: "bs_td.UpdateAccessLogSubscriptionResponseTypeDef",
    ) -> "dc_td.UpdateAccessLogSubscriptionResponse":
        return dc_td.UpdateAccessLogSubscriptionResponse.make_one(res)

    def update_listener(
        self,
        res: "bs_td.UpdateListenerResponseTypeDef",
    ) -> "dc_td.UpdateListenerResponse":
        return dc_td.UpdateListenerResponse.make_one(res)

    def update_resource_configuration(
        self,
        res: "bs_td.UpdateResourceConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateResourceConfigurationResponse":
        return dc_td.UpdateResourceConfigurationResponse.make_one(res)

    def update_resource_gateway(
        self,
        res: "bs_td.UpdateResourceGatewayResponseTypeDef",
    ) -> "dc_td.UpdateResourceGatewayResponse":
        return dc_td.UpdateResourceGatewayResponse.make_one(res)

    def update_rule(
        self,
        res: "bs_td.UpdateRuleResponseTypeDef",
    ) -> "dc_td.UpdateRuleResponse":
        return dc_td.UpdateRuleResponse.make_one(res)

    def update_service(
        self,
        res: "bs_td.UpdateServiceResponseTypeDef",
    ) -> "dc_td.UpdateServiceResponse":
        return dc_td.UpdateServiceResponse.make_one(res)

    def update_service_network(
        self,
        res: "bs_td.UpdateServiceNetworkResponseTypeDef",
    ) -> "dc_td.UpdateServiceNetworkResponse":
        return dc_td.UpdateServiceNetworkResponse.make_one(res)

    def update_service_network_vpc_association(
        self,
        res: "bs_td.UpdateServiceNetworkVpcAssociationResponseTypeDef",
    ) -> "dc_td.UpdateServiceNetworkVpcAssociationResponse":
        return dc_td.UpdateServiceNetworkVpcAssociationResponse.make_one(res)

    def update_target_group(
        self,
        res: "bs_td.UpdateTargetGroupResponseTypeDef",
    ) -> "dc_td.UpdateTargetGroupResponse":
        return dc_td.UpdateTargetGroupResponse.make_one(res)


vpc_lattice_caster = VPC_LATTICECaster()
