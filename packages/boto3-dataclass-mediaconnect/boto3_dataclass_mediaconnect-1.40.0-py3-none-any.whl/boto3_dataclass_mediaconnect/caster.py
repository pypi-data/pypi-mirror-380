# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediaconnect import type_defs as bs_td


class MEDIACONNECTCaster:

    def add_bridge_outputs(
        self,
        res: "bs_td.AddBridgeOutputsResponseTypeDef",
    ) -> "dc_td.AddBridgeOutputsResponse":
        return dc_td.AddBridgeOutputsResponse.make_one(res)

    def add_bridge_sources(
        self,
        res: "bs_td.AddBridgeSourcesResponseTypeDef",
    ) -> "dc_td.AddBridgeSourcesResponse":
        return dc_td.AddBridgeSourcesResponse.make_one(res)

    def add_flow_media_streams(
        self,
        res: "bs_td.AddFlowMediaStreamsResponseTypeDef",
    ) -> "dc_td.AddFlowMediaStreamsResponse":
        return dc_td.AddFlowMediaStreamsResponse.make_one(res)

    def add_flow_outputs(
        self,
        res: "bs_td.AddFlowOutputsResponseTypeDef",
    ) -> "dc_td.AddFlowOutputsResponse":
        return dc_td.AddFlowOutputsResponse.make_one(res)

    def add_flow_sources(
        self,
        res: "bs_td.AddFlowSourcesResponseTypeDef",
    ) -> "dc_td.AddFlowSourcesResponse":
        return dc_td.AddFlowSourcesResponse.make_one(res)

    def add_flow_vpc_interfaces(
        self,
        res: "bs_td.AddFlowVpcInterfacesResponseTypeDef",
    ) -> "dc_td.AddFlowVpcInterfacesResponse":
        return dc_td.AddFlowVpcInterfacesResponse.make_one(res)

    def create_bridge(
        self,
        res: "bs_td.CreateBridgeResponseTypeDef",
    ) -> "dc_td.CreateBridgeResponse":
        return dc_td.CreateBridgeResponse.make_one(res)

    def create_flow(
        self,
        res: "bs_td.CreateFlowResponseTypeDef",
    ) -> "dc_td.CreateFlowResponse":
        return dc_td.CreateFlowResponse.make_one(res)

    def create_gateway(
        self,
        res: "bs_td.CreateGatewayResponseTypeDef",
    ) -> "dc_td.CreateGatewayResponse":
        return dc_td.CreateGatewayResponse.make_one(res)

    def delete_bridge(
        self,
        res: "bs_td.DeleteBridgeResponseTypeDef",
    ) -> "dc_td.DeleteBridgeResponse":
        return dc_td.DeleteBridgeResponse.make_one(res)

    def delete_flow(
        self,
        res: "bs_td.DeleteFlowResponseTypeDef",
    ) -> "dc_td.DeleteFlowResponse":
        return dc_td.DeleteFlowResponse.make_one(res)

    def delete_gateway(
        self,
        res: "bs_td.DeleteGatewayResponseTypeDef",
    ) -> "dc_td.DeleteGatewayResponse":
        return dc_td.DeleteGatewayResponse.make_one(res)

    def deregister_gateway_instance(
        self,
        res: "bs_td.DeregisterGatewayInstanceResponseTypeDef",
    ) -> "dc_td.DeregisterGatewayInstanceResponse":
        return dc_td.DeregisterGatewayInstanceResponse.make_one(res)

    def describe_bridge(
        self,
        res: "bs_td.DescribeBridgeResponseTypeDef",
    ) -> "dc_td.DescribeBridgeResponse":
        return dc_td.DescribeBridgeResponse.make_one(res)

    def describe_flow(
        self,
        res: "bs_td.DescribeFlowResponseTypeDef",
    ) -> "dc_td.DescribeFlowResponse":
        return dc_td.DescribeFlowResponse.make_one(res)

    def describe_flow_source_metadata(
        self,
        res: "bs_td.DescribeFlowSourceMetadataResponseTypeDef",
    ) -> "dc_td.DescribeFlowSourceMetadataResponse":
        return dc_td.DescribeFlowSourceMetadataResponse.make_one(res)

    def describe_flow_source_thumbnail(
        self,
        res: "bs_td.DescribeFlowSourceThumbnailResponseTypeDef",
    ) -> "dc_td.DescribeFlowSourceThumbnailResponse":
        return dc_td.DescribeFlowSourceThumbnailResponse.make_one(res)

    def describe_gateway(
        self,
        res: "bs_td.DescribeGatewayResponseTypeDef",
    ) -> "dc_td.DescribeGatewayResponse":
        return dc_td.DescribeGatewayResponse.make_one(res)

    def describe_gateway_instance(
        self,
        res: "bs_td.DescribeGatewayInstanceResponseTypeDef",
    ) -> "dc_td.DescribeGatewayInstanceResponse":
        return dc_td.DescribeGatewayInstanceResponse.make_one(res)

    def describe_offering(
        self,
        res: "bs_td.DescribeOfferingResponseTypeDef",
    ) -> "dc_td.DescribeOfferingResponse":
        return dc_td.DescribeOfferingResponse.make_one(res)

    def describe_reservation(
        self,
        res: "bs_td.DescribeReservationResponseTypeDef",
    ) -> "dc_td.DescribeReservationResponse":
        return dc_td.DescribeReservationResponse.make_one(res)

    def grant_flow_entitlements(
        self,
        res: "bs_td.GrantFlowEntitlementsResponseTypeDef",
    ) -> "dc_td.GrantFlowEntitlementsResponse":
        return dc_td.GrantFlowEntitlementsResponse.make_one(res)

    def list_bridges(
        self,
        res: "bs_td.ListBridgesResponseTypeDef",
    ) -> "dc_td.ListBridgesResponse":
        return dc_td.ListBridgesResponse.make_one(res)

    def list_entitlements(
        self,
        res: "bs_td.ListEntitlementsResponseTypeDef",
    ) -> "dc_td.ListEntitlementsResponse":
        return dc_td.ListEntitlementsResponse.make_one(res)

    def list_flows(
        self,
        res: "bs_td.ListFlowsResponseTypeDef",
    ) -> "dc_td.ListFlowsResponse":
        return dc_td.ListFlowsResponse.make_one(res)

    def list_gateway_instances(
        self,
        res: "bs_td.ListGatewayInstancesResponseTypeDef",
    ) -> "dc_td.ListGatewayInstancesResponse":
        return dc_td.ListGatewayInstancesResponse.make_one(res)

    def list_gateways(
        self,
        res: "bs_td.ListGatewaysResponseTypeDef",
    ) -> "dc_td.ListGatewaysResponse":
        return dc_td.ListGatewaysResponse.make_one(res)

    def list_offerings(
        self,
        res: "bs_td.ListOfferingsResponseTypeDef",
    ) -> "dc_td.ListOfferingsResponse":
        return dc_td.ListOfferingsResponse.make_one(res)

    def list_reservations(
        self,
        res: "bs_td.ListReservationsResponseTypeDef",
    ) -> "dc_td.ListReservationsResponse":
        return dc_td.ListReservationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def purchase_offering(
        self,
        res: "bs_td.PurchaseOfferingResponseTypeDef",
    ) -> "dc_td.PurchaseOfferingResponse":
        return dc_td.PurchaseOfferingResponse.make_one(res)

    def remove_bridge_output(
        self,
        res: "bs_td.RemoveBridgeOutputResponseTypeDef",
    ) -> "dc_td.RemoveBridgeOutputResponse":
        return dc_td.RemoveBridgeOutputResponse.make_one(res)

    def remove_bridge_source(
        self,
        res: "bs_td.RemoveBridgeSourceResponseTypeDef",
    ) -> "dc_td.RemoveBridgeSourceResponse":
        return dc_td.RemoveBridgeSourceResponse.make_one(res)

    def remove_flow_media_stream(
        self,
        res: "bs_td.RemoveFlowMediaStreamResponseTypeDef",
    ) -> "dc_td.RemoveFlowMediaStreamResponse":
        return dc_td.RemoveFlowMediaStreamResponse.make_one(res)

    def remove_flow_output(
        self,
        res: "bs_td.RemoveFlowOutputResponseTypeDef",
    ) -> "dc_td.RemoveFlowOutputResponse":
        return dc_td.RemoveFlowOutputResponse.make_one(res)

    def remove_flow_source(
        self,
        res: "bs_td.RemoveFlowSourceResponseTypeDef",
    ) -> "dc_td.RemoveFlowSourceResponse":
        return dc_td.RemoveFlowSourceResponse.make_one(res)

    def remove_flow_vpc_interface(
        self,
        res: "bs_td.RemoveFlowVpcInterfaceResponseTypeDef",
    ) -> "dc_td.RemoveFlowVpcInterfaceResponse":
        return dc_td.RemoveFlowVpcInterfaceResponse.make_one(res)

    def revoke_flow_entitlement(
        self,
        res: "bs_td.RevokeFlowEntitlementResponseTypeDef",
    ) -> "dc_td.RevokeFlowEntitlementResponse":
        return dc_td.RevokeFlowEntitlementResponse.make_one(res)

    def start_flow(
        self,
        res: "bs_td.StartFlowResponseTypeDef",
    ) -> "dc_td.StartFlowResponse":
        return dc_td.StartFlowResponse.make_one(res)

    def stop_flow(
        self,
        res: "bs_td.StopFlowResponseTypeDef",
    ) -> "dc_td.StopFlowResponse":
        return dc_td.StopFlowResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_bridge(
        self,
        res: "bs_td.UpdateBridgeResponseTypeDef",
    ) -> "dc_td.UpdateBridgeResponse":
        return dc_td.UpdateBridgeResponse.make_one(res)

    def update_bridge_output(
        self,
        res: "bs_td.UpdateBridgeOutputResponseTypeDef",
    ) -> "dc_td.UpdateBridgeOutputResponse":
        return dc_td.UpdateBridgeOutputResponse.make_one(res)

    def update_bridge_source(
        self,
        res: "bs_td.UpdateBridgeSourceResponseTypeDef",
    ) -> "dc_td.UpdateBridgeSourceResponse":
        return dc_td.UpdateBridgeSourceResponse.make_one(res)

    def update_bridge_state(
        self,
        res: "bs_td.UpdateBridgeStateResponseTypeDef",
    ) -> "dc_td.UpdateBridgeStateResponse":
        return dc_td.UpdateBridgeStateResponse.make_one(res)

    def update_flow(
        self,
        res: "bs_td.UpdateFlowResponseTypeDef",
    ) -> "dc_td.UpdateFlowResponse":
        return dc_td.UpdateFlowResponse.make_one(res)

    def update_flow_entitlement(
        self,
        res: "bs_td.UpdateFlowEntitlementResponseTypeDef",
    ) -> "dc_td.UpdateFlowEntitlementResponse":
        return dc_td.UpdateFlowEntitlementResponse.make_one(res)

    def update_flow_media_stream(
        self,
        res: "bs_td.UpdateFlowMediaStreamResponseTypeDef",
    ) -> "dc_td.UpdateFlowMediaStreamResponse":
        return dc_td.UpdateFlowMediaStreamResponse.make_one(res)

    def update_flow_output(
        self,
        res: "bs_td.UpdateFlowOutputResponseTypeDef",
    ) -> "dc_td.UpdateFlowOutputResponse":
        return dc_td.UpdateFlowOutputResponse.make_one(res)

    def update_flow_source(
        self,
        res: "bs_td.UpdateFlowSourceResponseTypeDef",
    ) -> "dc_td.UpdateFlowSourceResponse":
        return dc_td.UpdateFlowSourceResponse.make_one(res)

    def update_gateway_instance(
        self,
        res: "bs_td.UpdateGatewayInstanceResponseTypeDef",
    ) -> "dc_td.UpdateGatewayInstanceResponse":
        return dc_td.UpdateGatewayInstanceResponse.make_one(res)


mediaconnect_caster = MEDIACONNECTCaster()
