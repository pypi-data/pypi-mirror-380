# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_globalaccelerator import type_defs as bs_td


class GLOBALACCELERATORCaster:

    def add_custom_routing_endpoints(
        self,
        res: "bs_td.AddCustomRoutingEndpointsResponseTypeDef",
    ) -> "dc_td.AddCustomRoutingEndpointsResponse":
        return dc_td.AddCustomRoutingEndpointsResponse.make_one(res)

    def add_endpoints(
        self,
        res: "bs_td.AddEndpointsResponseTypeDef",
    ) -> "dc_td.AddEndpointsResponse":
        return dc_td.AddEndpointsResponse.make_one(res)

    def advertise_byoip_cidr(
        self,
        res: "bs_td.AdvertiseByoipCidrResponseTypeDef",
    ) -> "dc_td.AdvertiseByoipCidrResponse":
        return dc_td.AdvertiseByoipCidrResponse.make_one(res)

    def allow_custom_routing_traffic(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_accelerator(
        self,
        res: "bs_td.CreateAcceleratorResponseTypeDef",
    ) -> "dc_td.CreateAcceleratorResponse":
        return dc_td.CreateAcceleratorResponse.make_one(res)

    def create_cross_account_attachment(
        self,
        res: "bs_td.CreateCrossAccountAttachmentResponseTypeDef",
    ) -> "dc_td.CreateCrossAccountAttachmentResponse":
        return dc_td.CreateCrossAccountAttachmentResponse.make_one(res)

    def create_custom_routing_accelerator(
        self,
        res: "bs_td.CreateCustomRoutingAcceleratorResponseTypeDef",
    ) -> "dc_td.CreateCustomRoutingAcceleratorResponse":
        return dc_td.CreateCustomRoutingAcceleratorResponse.make_one(res)

    def create_custom_routing_endpoint_group(
        self,
        res: "bs_td.CreateCustomRoutingEndpointGroupResponseTypeDef",
    ) -> "dc_td.CreateCustomRoutingEndpointGroupResponse":
        return dc_td.CreateCustomRoutingEndpointGroupResponse.make_one(res)

    def create_custom_routing_listener(
        self,
        res: "bs_td.CreateCustomRoutingListenerResponseTypeDef",
    ) -> "dc_td.CreateCustomRoutingListenerResponse":
        return dc_td.CreateCustomRoutingListenerResponse.make_one(res)

    def create_endpoint_group(
        self,
        res: "bs_td.CreateEndpointGroupResponseTypeDef",
    ) -> "dc_td.CreateEndpointGroupResponse":
        return dc_td.CreateEndpointGroupResponse.make_one(res)

    def create_listener(
        self,
        res: "bs_td.CreateListenerResponseTypeDef",
    ) -> "dc_td.CreateListenerResponse":
        return dc_td.CreateListenerResponse.make_one(res)

    def delete_accelerator(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_cross_account_attachment(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_custom_routing_accelerator(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_custom_routing_endpoint_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_custom_routing_listener(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_endpoint_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_listener(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deny_custom_routing_traffic(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deprovision_byoip_cidr(
        self,
        res: "bs_td.DeprovisionByoipCidrResponseTypeDef",
    ) -> "dc_td.DeprovisionByoipCidrResponse":
        return dc_td.DeprovisionByoipCidrResponse.make_one(res)

    def describe_accelerator(
        self,
        res: "bs_td.DescribeAcceleratorResponseTypeDef",
    ) -> "dc_td.DescribeAcceleratorResponse":
        return dc_td.DescribeAcceleratorResponse.make_one(res)

    def describe_accelerator_attributes(
        self,
        res: "bs_td.DescribeAcceleratorAttributesResponseTypeDef",
    ) -> "dc_td.DescribeAcceleratorAttributesResponse":
        return dc_td.DescribeAcceleratorAttributesResponse.make_one(res)

    def describe_cross_account_attachment(
        self,
        res: "bs_td.DescribeCrossAccountAttachmentResponseTypeDef",
    ) -> "dc_td.DescribeCrossAccountAttachmentResponse":
        return dc_td.DescribeCrossAccountAttachmentResponse.make_one(res)

    def describe_custom_routing_accelerator(
        self,
        res: "bs_td.DescribeCustomRoutingAcceleratorResponseTypeDef",
    ) -> "dc_td.DescribeCustomRoutingAcceleratorResponse":
        return dc_td.DescribeCustomRoutingAcceleratorResponse.make_one(res)

    def describe_custom_routing_accelerator_attributes(
        self,
        res: "bs_td.DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    ) -> "dc_td.DescribeCustomRoutingAcceleratorAttributesResponse":
        return dc_td.DescribeCustomRoutingAcceleratorAttributesResponse.make_one(res)

    def describe_custom_routing_endpoint_group(
        self,
        res: "bs_td.DescribeCustomRoutingEndpointGroupResponseTypeDef",
    ) -> "dc_td.DescribeCustomRoutingEndpointGroupResponse":
        return dc_td.DescribeCustomRoutingEndpointGroupResponse.make_one(res)

    def describe_custom_routing_listener(
        self,
        res: "bs_td.DescribeCustomRoutingListenerResponseTypeDef",
    ) -> "dc_td.DescribeCustomRoutingListenerResponse":
        return dc_td.DescribeCustomRoutingListenerResponse.make_one(res)

    def describe_endpoint_group(
        self,
        res: "bs_td.DescribeEndpointGroupResponseTypeDef",
    ) -> "dc_td.DescribeEndpointGroupResponse":
        return dc_td.DescribeEndpointGroupResponse.make_one(res)

    def describe_listener(
        self,
        res: "bs_td.DescribeListenerResponseTypeDef",
    ) -> "dc_td.DescribeListenerResponse":
        return dc_td.DescribeListenerResponse.make_one(res)

    def list_accelerators(
        self,
        res: "bs_td.ListAcceleratorsResponseTypeDef",
    ) -> "dc_td.ListAcceleratorsResponse":
        return dc_td.ListAcceleratorsResponse.make_one(res)

    def list_byoip_cidrs(
        self,
        res: "bs_td.ListByoipCidrsResponseTypeDef",
    ) -> "dc_td.ListByoipCidrsResponse":
        return dc_td.ListByoipCidrsResponse.make_one(res)

    def list_cross_account_attachments(
        self,
        res: "bs_td.ListCrossAccountAttachmentsResponseTypeDef",
    ) -> "dc_td.ListCrossAccountAttachmentsResponse":
        return dc_td.ListCrossAccountAttachmentsResponse.make_one(res)

    def list_cross_account_resource_accounts(
        self,
        res: "bs_td.ListCrossAccountResourceAccountsResponseTypeDef",
    ) -> "dc_td.ListCrossAccountResourceAccountsResponse":
        return dc_td.ListCrossAccountResourceAccountsResponse.make_one(res)

    def list_cross_account_resources(
        self,
        res: "bs_td.ListCrossAccountResourcesResponseTypeDef",
    ) -> "dc_td.ListCrossAccountResourcesResponse":
        return dc_td.ListCrossAccountResourcesResponse.make_one(res)

    def list_custom_routing_accelerators(
        self,
        res: "bs_td.ListCustomRoutingAcceleratorsResponseTypeDef",
    ) -> "dc_td.ListCustomRoutingAcceleratorsResponse":
        return dc_td.ListCustomRoutingAcceleratorsResponse.make_one(res)

    def list_custom_routing_endpoint_groups(
        self,
        res: "bs_td.ListCustomRoutingEndpointGroupsResponseTypeDef",
    ) -> "dc_td.ListCustomRoutingEndpointGroupsResponse":
        return dc_td.ListCustomRoutingEndpointGroupsResponse.make_one(res)

    def list_custom_routing_listeners(
        self,
        res: "bs_td.ListCustomRoutingListenersResponseTypeDef",
    ) -> "dc_td.ListCustomRoutingListenersResponse":
        return dc_td.ListCustomRoutingListenersResponse.make_one(res)

    def list_custom_routing_port_mappings(
        self,
        res: "bs_td.ListCustomRoutingPortMappingsResponseTypeDef",
    ) -> "dc_td.ListCustomRoutingPortMappingsResponse":
        return dc_td.ListCustomRoutingPortMappingsResponse.make_one(res)

    def list_custom_routing_port_mappings_by_destination(
        self,
        res: "bs_td.ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    ) -> "dc_td.ListCustomRoutingPortMappingsByDestinationResponse":
        return dc_td.ListCustomRoutingPortMappingsByDestinationResponse.make_one(res)

    def list_endpoint_groups(
        self,
        res: "bs_td.ListEndpointGroupsResponseTypeDef",
    ) -> "dc_td.ListEndpointGroupsResponse":
        return dc_td.ListEndpointGroupsResponse.make_one(res)

    def list_listeners(
        self,
        res: "bs_td.ListListenersResponseTypeDef",
    ) -> "dc_td.ListListenersResponse":
        return dc_td.ListListenersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def provision_byoip_cidr(
        self,
        res: "bs_td.ProvisionByoipCidrResponseTypeDef",
    ) -> "dc_td.ProvisionByoipCidrResponse":
        return dc_td.ProvisionByoipCidrResponse.make_one(res)

    def remove_custom_routing_endpoints(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_endpoints(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_accelerator(
        self,
        res: "bs_td.UpdateAcceleratorResponseTypeDef",
    ) -> "dc_td.UpdateAcceleratorResponse":
        return dc_td.UpdateAcceleratorResponse.make_one(res)

    def update_accelerator_attributes(
        self,
        res: "bs_td.UpdateAcceleratorAttributesResponseTypeDef",
    ) -> "dc_td.UpdateAcceleratorAttributesResponse":
        return dc_td.UpdateAcceleratorAttributesResponse.make_one(res)

    def update_cross_account_attachment(
        self,
        res: "bs_td.UpdateCrossAccountAttachmentResponseTypeDef",
    ) -> "dc_td.UpdateCrossAccountAttachmentResponse":
        return dc_td.UpdateCrossAccountAttachmentResponse.make_one(res)

    def update_custom_routing_accelerator(
        self,
        res: "bs_td.UpdateCustomRoutingAcceleratorResponseTypeDef",
    ) -> "dc_td.UpdateCustomRoutingAcceleratorResponse":
        return dc_td.UpdateCustomRoutingAcceleratorResponse.make_one(res)

    def update_custom_routing_accelerator_attributes(
        self,
        res: "bs_td.UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    ) -> "dc_td.UpdateCustomRoutingAcceleratorAttributesResponse":
        return dc_td.UpdateCustomRoutingAcceleratorAttributesResponse.make_one(res)

    def update_custom_routing_listener(
        self,
        res: "bs_td.UpdateCustomRoutingListenerResponseTypeDef",
    ) -> "dc_td.UpdateCustomRoutingListenerResponse":
        return dc_td.UpdateCustomRoutingListenerResponse.make_one(res)

    def update_endpoint_group(
        self,
        res: "bs_td.UpdateEndpointGroupResponseTypeDef",
    ) -> "dc_td.UpdateEndpointGroupResponse":
        return dc_td.UpdateEndpointGroupResponse.make_one(res)

    def update_listener(
        self,
        res: "bs_td.UpdateListenerResponseTypeDef",
    ) -> "dc_td.UpdateListenerResponse":
        return dc_td.UpdateListenerResponse.make_one(res)

    def withdraw_byoip_cidr(
        self,
        res: "bs_td.WithdrawByoipCidrResponseTypeDef",
    ) -> "dc_td.WithdrawByoipCidrResponse":
        return dc_td.WithdrawByoipCidrResponse.make_one(res)


globalaccelerator_caster = GLOBALACCELERATORCaster()
