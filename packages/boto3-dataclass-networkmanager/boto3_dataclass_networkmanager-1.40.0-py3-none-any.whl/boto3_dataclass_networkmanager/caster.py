# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_networkmanager import type_defs as bs_td


class NETWORKMANAGERCaster:

    def accept_attachment(
        self,
        res: "bs_td.AcceptAttachmentResponseTypeDef",
    ) -> "dc_td.AcceptAttachmentResponse":
        return dc_td.AcceptAttachmentResponse.make_one(res)

    def associate_connect_peer(
        self,
        res: "bs_td.AssociateConnectPeerResponseTypeDef",
    ) -> "dc_td.AssociateConnectPeerResponse":
        return dc_td.AssociateConnectPeerResponse.make_one(res)

    def associate_customer_gateway(
        self,
        res: "bs_td.AssociateCustomerGatewayResponseTypeDef",
    ) -> "dc_td.AssociateCustomerGatewayResponse":
        return dc_td.AssociateCustomerGatewayResponse.make_one(res)

    def associate_link(
        self,
        res: "bs_td.AssociateLinkResponseTypeDef",
    ) -> "dc_td.AssociateLinkResponse":
        return dc_td.AssociateLinkResponse.make_one(res)

    def associate_transit_gateway_connect_peer(
        self,
        res: "bs_td.AssociateTransitGatewayConnectPeerResponseTypeDef",
    ) -> "dc_td.AssociateTransitGatewayConnectPeerResponse":
        return dc_td.AssociateTransitGatewayConnectPeerResponse.make_one(res)

    def create_connect_attachment(
        self,
        res: "bs_td.CreateConnectAttachmentResponseTypeDef",
    ) -> "dc_td.CreateConnectAttachmentResponse":
        return dc_td.CreateConnectAttachmentResponse.make_one(res)

    def create_connect_peer(
        self,
        res: "bs_td.CreateConnectPeerResponseTypeDef",
    ) -> "dc_td.CreateConnectPeerResponse":
        return dc_td.CreateConnectPeerResponse.make_one(res)

    def create_connection(
        self,
        res: "bs_td.CreateConnectionResponseTypeDef",
    ) -> "dc_td.CreateConnectionResponse":
        return dc_td.CreateConnectionResponse.make_one(res)

    def create_core_network(
        self,
        res: "bs_td.CreateCoreNetworkResponseTypeDef",
    ) -> "dc_td.CreateCoreNetworkResponse":
        return dc_td.CreateCoreNetworkResponse.make_one(res)

    def create_device(
        self,
        res: "bs_td.CreateDeviceResponseTypeDef",
    ) -> "dc_td.CreateDeviceResponse":
        return dc_td.CreateDeviceResponse.make_one(res)

    def create_direct_connect_gateway_attachment(
        self,
        res: "bs_td.CreateDirectConnectGatewayAttachmentResponseTypeDef",
    ) -> "dc_td.CreateDirectConnectGatewayAttachmentResponse":
        return dc_td.CreateDirectConnectGatewayAttachmentResponse.make_one(res)

    def create_global_network(
        self,
        res: "bs_td.CreateGlobalNetworkResponseTypeDef",
    ) -> "dc_td.CreateGlobalNetworkResponse":
        return dc_td.CreateGlobalNetworkResponse.make_one(res)

    def create_link(
        self,
        res: "bs_td.CreateLinkResponseTypeDef",
    ) -> "dc_td.CreateLinkResponse":
        return dc_td.CreateLinkResponse.make_one(res)

    def create_site(
        self,
        res: "bs_td.CreateSiteResponseTypeDef",
    ) -> "dc_td.CreateSiteResponse":
        return dc_td.CreateSiteResponse.make_one(res)

    def create_site_to_site_vpn_attachment(
        self,
        res: "bs_td.CreateSiteToSiteVpnAttachmentResponseTypeDef",
    ) -> "dc_td.CreateSiteToSiteVpnAttachmentResponse":
        return dc_td.CreateSiteToSiteVpnAttachmentResponse.make_one(res)

    def create_transit_gateway_peering(
        self,
        res: "bs_td.CreateTransitGatewayPeeringResponseTypeDef",
    ) -> "dc_td.CreateTransitGatewayPeeringResponse":
        return dc_td.CreateTransitGatewayPeeringResponse.make_one(res)

    def create_transit_gateway_route_table_attachment(
        self,
        res: "bs_td.CreateTransitGatewayRouteTableAttachmentResponseTypeDef",
    ) -> "dc_td.CreateTransitGatewayRouteTableAttachmentResponse":
        return dc_td.CreateTransitGatewayRouteTableAttachmentResponse.make_one(res)

    def create_vpc_attachment(
        self,
        res: "bs_td.CreateVpcAttachmentResponseTypeDef",
    ) -> "dc_td.CreateVpcAttachmentResponse":
        return dc_td.CreateVpcAttachmentResponse.make_one(res)

    def delete_attachment(
        self,
        res: "bs_td.DeleteAttachmentResponseTypeDef",
    ) -> "dc_td.DeleteAttachmentResponse":
        return dc_td.DeleteAttachmentResponse.make_one(res)

    def delete_connect_peer(
        self,
        res: "bs_td.DeleteConnectPeerResponseTypeDef",
    ) -> "dc_td.DeleteConnectPeerResponse":
        return dc_td.DeleteConnectPeerResponse.make_one(res)

    def delete_connection(
        self,
        res: "bs_td.DeleteConnectionResponseTypeDef",
    ) -> "dc_td.DeleteConnectionResponse":
        return dc_td.DeleteConnectionResponse.make_one(res)

    def delete_core_network(
        self,
        res: "bs_td.DeleteCoreNetworkResponseTypeDef",
    ) -> "dc_td.DeleteCoreNetworkResponse":
        return dc_td.DeleteCoreNetworkResponse.make_one(res)

    def delete_core_network_policy_version(
        self,
        res: "bs_td.DeleteCoreNetworkPolicyVersionResponseTypeDef",
    ) -> "dc_td.DeleteCoreNetworkPolicyVersionResponse":
        return dc_td.DeleteCoreNetworkPolicyVersionResponse.make_one(res)

    def delete_device(
        self,
        res: "bs_td.DeleteDeviceResponseTypeDef",
    ) -> "dc_td.DeleteDeviceResponse":
        return dc_td.DeleteDeviceResponse.make_one(res)

    def delete_global_network(
        self,
        res: "bs_td.DeleteGlobalNetworkResponseTypeDef",
    ) -> "dc_td.DeleteGlobalNetworkResponse":
        return dc_td.DeleteGlobalNetworkResponse.make_one(res)

    def delete_link(
        self,
        res: "bs_td.DeleteLinkResponseTypeDef",
    ) -> "dc_td.DeleteLinkResponse":
        return dc_td.DeleteLinkResponse.make_one(res)

    def delete_peering(
        self,
        res: "bs_td.DeletePeeringResponseTypeDef",
    ) -> "dc_td.DeletePeeringResponse":
        return dc_td.DeletePeeringResponse.make_one(res)

    def delete_site(
        self,
        res: "bs_td.DeleteSiteResponseTypeDef",
    ) -> "dc_td.DeleteSiteResponse":
        return dc_td.DeleteSiteResponse.make_one(res)

    def deregister_transit_gateway(
        self,
        res: "bs_td.DeregisterTransitGatewayResponseTypeDef",
    ) -> "dc_td.DeregisterTransitGatewayResponse":
        return dc_td.DeregisterTransitGatewayResponse.make_one(res)

    def describe_global_networks(
        self,
        res: "bs_td.DescribeGlobalNetworksResponseTypeDef",
    ) -> "dc_td.DescribeGlobalNetworksResponse":
        return dc_td.DescribeGlobalNetworksResponse.make_one(res)

    def disassociate_connect_peer(
        self,
        res: "bs_td.DisassociateConnectPeerResponseTypeDef",
    ) -> "dc_td.DisassociateConnectPeerResponse":
        return dc_td.DisassociateConnectPeerResponse.make_one(res)

    def disassociate_customer_gateway(
        self,
        res: "bs_td.DisassociateCustomerGatewayResponseTypeDef",
    ) -> "dc_td.DisassociateCustomerGatewayResponse":
        return dc_td.DisassociateCustomerGatewayResponse.make_one(res)

    def disassociate_link(
        self,
        res: "bs_td.DisassociateLinkResponseTypeDef",
    ) -> "dc_td.DisassociateLinkResponse":
        return dc_td.DisassociateLinkResponse.make_one(res)

    def disassociate_transit_gateway_connect_peer(
        self,
        res: "bs_td.DisassociateTransitGatewayConnectPeerResponseTypeDef",
    ) -> "dc_td.DisassociateTransitGatewayConnectPeerResponse":
        return dc_td.DisassociateTransitGatewayConnectPeerResponse.make_one(res)

    def get_connect_attachment(
        self,
        res: "bs_td.GetConnectAttachmentResponseTypeDef",
    ) -> "dc_td.GetConnectAttachmentResponse":
        return dc_td.GetConnectAttachmentResponse.make_one(res)

    def get_connect_peer(
        self,
        res: "bs_td.GetConnectPeerResponseTypeDef",
    ) -> "dc_td.GetConnectPeerResponse":
        return dc_td.GetConnectPeerResponse.make_one(res)

    def get_connect_peer_associations(
        self,
        res: "bs_td.GetConnectPeerAssociationsResponseTypeDef",
    ) -> "dc_td.GetConnectPeerAssociationsResponse":
        return dc_td.GetConnectPeerAssociationsResponse.make_one(res)

    def get_connections(
        self,
        res: "bs_td.GetConnectionsResponseTypeDef",
    ) -> "dc_td.GetConnectionsResponse":
        return dc_td.GetConnectionsResponse.make_one(res)

    def get_core_network(
        self,
        res: "bs_td.GetCoreNetworkResponseTypeDef",
    ) -> "dc_td.GetCoreNetworkResponse":
        return dc_td.GetCoreNetworkResponse.make_one(res)

    def get_core_network_change_events(
        self,
        res: "bs_td.GetCoreNetworkChangeEventsResponseTypeDef",
    ) -> "dc_td.GetCoreNetworkChangeEventsResponse":
        return dc_td.GetCoreNetworkChangeEventsResponse.make_one(res)

    def get_core_network_change_set(
        self,
        res: "bs_td.GetCoreNetworkChangeSetResponseTypeDef",
    ) -> "dc_td.GetCoreNetworkChangeSetResponse":
        return dc_td.GetCoreNetworkChangeSetResponse.make_one(res)

    def get_core_network_policy(
        self,
        res: "bs_td.GetCoreNetworkPolicyResponseTypeDef",
    ) -> "dc_td.GetCoreNetworkPolicyResponse":
        return dc_td.GetCoreNetworkPolicyResponse.make_one(res)

    def get_customer_gateway_associations(
        self,
        res: "bs_td.GetCustomerGatewayAssociationsResponseTypeDef",
    ) -> "dc_td.GetCustomerGatewayAssociationsResponse":
        return dc_td.GetCustomerGatewayAssociationsResponse.make_one(res)

    def get_devices(
        self,
        res: "bs_td.GetDevicesResponseTypeDef",
    ) -> "dc_td.GetDevicesResponse":
        return dc_td.GetDevicesResponse.make_one(res)

    def get_direct_connect_gateway_attachment(
        self,
        res: "bs_td.GetDirectConnectGatewayAttachmentResponseTypeDef",
    ) -> "dc_td.GetDirectConnectGatewayAttachmentResponse":
        return dc_td.GetDirectConnectGatewayAttachmentResponse.make_one(res)

    def get_link_associations(
        self,
        res: "bs_td.GetLinkAssociationsResponseTypeDef",
    ) -> "dc_td.GetLinkAssociationsResponse":
        return dc_td.GetLinkAssociationsResponse.make_one(res)

    def get_links(
        self,
        res: "bs_td.GetLinksResponseTypeDef",
    ) -> "dc_td.GetLinksResponse":
        return dc_td.GetLinksResponse.make_one(res)

    def get_network_resource_counts(
        self,
        res: "bs_td.GetNetworkResourceCountsResponseTypeDef",
    ) -> "dc_td.GetNetworkResourceCountsResponse":
        return dc_td.GetNetworkResourceCountsResponse.make_one(res)

    def get_network_resource_relationships(
        self,
        res: "bs_td.GetNetworkResourceRelationshipsResponseTypeDef",
    ) -> "dc_td.GetNetworkResourceRelationshipsResponse":
        return dc_td.GetNetworkResourceRelationshipsResponse.make_one(res)

    def get_network_resources(
        self,
        res: "bs_td.GetNetworkResourcesResponseTypeDef",
    ) -> "dc_td.GetNetworkResourcesResponse":
        return dc_td.GetNetworkResourcesResponse.make_one(res)

    def get_network_routes(
        self,
        res: "bs_td.GetNetworkRoutesResponseTypeDef",
    ) -> "dc_td.GetNetworkRoutesResponse":
        return dc_td.GetNetworkRoutesResponse.make_one(res)

    def get_network_telemetry(
        self,
        res: "bs_td.GetNetworkTelemetryResponseTypeDef",
    ) -> "dc_td.GetNetworkTelemetryResponse":
        return dc_td.GetNetworkTelemetryResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def get_route_analysis(
        self,
        res: "bs_td.GetRouteAnalysisResponseTypeDef",
    ) -> "dc_td.GetRouteAnalysisResponse":
        return dc_td.GetRouteAnalysisResponse.make_one(res)

    def get_site_to_site_vpn_attachment(
        self,
        res: "bs_td.GetSiteToSiteVpnAttachmentResponseTypeDef",
    ) -> "dc_td.GetSiteToSiteVpnAttachmentResponse":
        return dc_td.GetSiteToSiteVpnAttachmentResponse.make_one(res)

    def get_sites(
        self,
        res: "bs_td.GetSitesResponseTypeDef",
    ) -> "dc_td.GetSitesResponse":
        return dc_td.GetSitesResponse.make_one(res)

    def get_transit_gateway_connect_peer_associations(
        self,
        res: "bs_td.GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    ) -> "dc_td.GetTransitGatewayConnectPeerAssociationsResponse":
        return dc_td.GetTransitGatewayConnectPeerAssociationsResponse.make_one(res)

    def get_transit_gateway_peering(
        self,
        res: "bs_td.GetTransitGatewayPeeringResponseTypeDef",
    ) -> "dc_td.GetTransitGatewayPeeringResponse":
        return dc_td.GetTransitGatewayPeeringResponse.make_one(res)

    def get_transit_gateway_registrations(
        self,
        res: "bs_td.GetTransitGatewayRegistrationsResponseTypeDef",
    ) -> "dc_td.GetTransitGatewayRegistrationsResponse":
        return dc_td.GetTransitGatewayRegistrationsResponse.make_one(res)

    def get_transit_gateway_route_table_attachment(
        self,
        res: "bs_td.GetTransitGatewayRouteTableAttachmentResponseTypeDef",
    ) -> "dc_td.GetTransitGatewayRouteTableAttachmentResponse":
        return dc_td.GetTransitGatewayRouteTableAttachmentResponse.make_one(res)

    def get_vpc_attachment(
        self,
        res: "bs_td.GetVpcAttachmentResponseTypeDef",
    ) -> "dc_td.GetVpcAttachmentResponse":
        return dc_td.GetVpcAttachmentResponse.make_one(res)

    def list_attachments(
        self,
        res: "bs_td.ListAttachmentsResponseTypeDef",
    ) -> "dc_td.ListAttachmentsResponse":
        return dc_td.ListAttachmentsResponse.make_one(res)

    def list_connect_peers(
        self,
        res: "bs_td.ListConnectPeersResponseTypeDef",
    ) -> "dc_td.ListConnectPeersResponse":
        return dc_td.ListConnectPeersResponse.make_one(res)

    def list_core_network_policy_versions(
        self,
        res: "bs_td.ListCoreNetworkPolicyVersionsResponseTypeDef",
    ) -> "dc_td.ListCoreNetworkPolicyVersionsResponse":
        return dc_td.ListCoreNetworkPolicyVersionsResponse.make_one(res)

    def list_core_networks(
        self,
        res: "bs_td.ListCoreNetworksResponseTypeDef",
    ) -> "dc_td.ListCoreNetworksResponse":
        return dc_td.ListCoreNetworksResponse.make_one(res)

    def list_organization_service_access_status(
        self,
        res: "bs_td.ListOrganizationServiceAccessStatusResponseTypeDef",
    ) -> "dc_td.ListOrganizationServiceAccessStatusResponse":
        return dc_td.ListOrganizationServiceAccessStatusResponse.make_one(res)

    def list_peerings(
        self,
        res: "bs_td.ListPeeringsResponseTypeDef",
    ) -> "dc_td.ListPeeringsResponse":
        return dc_td.ListPeeringsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_core_network_policy(
        self,
        res: "bs_td.PutCoreNetworkPolicyResponseTypeDef",
    ) -> "dc_td.PutCoreNetworkPolicyResponse":
        return dc_td.PutCoreNetworkPolicyResponse.make_one(res)

    def register_transit_gateway(
        self,
        res: "bs_td.RegisterTransitGatewayResponseTypeDef",
    ) -> "dc_td.RegisterTransitGatewayResponse":
        return dc_td.RegisterTransitGatewayResponse.make_one(res)

    def reject_attachment(
        self,
        res: "bs_td.RejectAttachmentResponseTypeDef",
    ) -> "dc_td.RejectAttachmentResponse":
        return dc_td.RejectAttachmentResponse.make_one(res)

    def restore_core_network_policy_version(
        self,
        res: "bs_td.RestoreCoreNetworkPolicyVersionResponseTypeDef",
    ) -> "dc_td.RestoreCoreNetworkPolicyVersionResponse":
        return dc_td.RestoreCoreNetworkPolicyVersionResponse.make_one(res)

    def start_organization_service_access_update(
        self,
        res: "bs_td.StartOrganizationServiceAccessUpdateResponseTypeDef",
    ) -> "dc_td.StartOrganizationServiceAccessUpdateResponse":
        return dc_td.StartOrganizationServiceAccessUpdateResponse.make_one(res)

    def start_route_analysis(
        self,
        res: "bs_td.StartRouteAnalysisResponseTypeDef",
    ) -> "dc_td.StartRouteAnalysisResponse":
        return dc_td.StartRouteAnalysisResponse.make_one(res)

    def update_connection(
        self,
        res: "bs_td.UpdateConnectionResponseTypeDef",
    ) -> "dc_td.UpdateConnectionResponse":
        return dc_td.UpdateConnectionResponse.make_one(res)

    def update_core_network(
        self,
        res: "bs_td.UpdateCoreNetworkResponseTypeDef",
    ) -> "dc_td.UpdateCoreNetworkResponse":
        return dc_td.UpdateCoreNetworkResponse.make_one(res)

    def update_device(
        self,
        res: "bs_td.UpdateDeviceResponseTypeDef",
    ) -> "dc_td.UpdateDeviceResponse":
        return dc_td.UpdateDeviceResponse.make_one(res)

    def update_direct_connect_gateway_attachment(
        self,
        res: "bs_td.UpdateDirectConnectGatewayAttachmentResponseTypeDef",
    ) -> "dc_td.UpdateDirectConnectGatewayAttachmentResponse":
        return dc_td.UpdateDirectConnectGatewayAttachmentResponse.make_one(res)

    def update_global_network(
        self,
        res: "bs_td.UpdateGlobalNetworkResponseTypeDef",
    ) -> "dc_td.UpdateGlobalNetworkResponse":
        return dc_td.UpdateGlobalNetworkResponse.make_one(res)

    def update_link(
        self,
        res: "bs_td.UpdateLinkResponseTypeDef",
    ) -> "dc_td.UpdateLinkResponse":
        return dc_td.UpdateLinkResponse.make_one(res)

    def update_network_resource_metadata(
        self,
        res: "bs_td.UpdateNetworkResourceMetadataResponseTypeDef",
    ) -> "dc_td.UpdateNetworkResourceMetadataResponse":
        return dc_td.UpdateNetworkResourceMetadataResponse.make_one(res)

    def update_site(
        self,
        res: "bs_td.UpdateSiteResponseTypeDef",
    ) -> "dc_td.UpdateSiteResponse":
        return dc_td.UpdateSiteResponse.make_one(res)

    def update_vpc_attachment(
        self,
        res: "bs_td.UpdateVpcAttachmentResponseTypeDef",
    ) -> "dc_td.UpdateVpcAttachmentResponse":
        return dc_td.UpdateVpcAttachmentResponse.make_one(res)


networkmanager_caster = NETWORKMANAGERCaster()
