# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_networkmanager import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AWSLocation:
    boto3_raw_data: "type_defs.AWSLocationTypeDef" = dataclasses.field()

    Zone = field("Zone")
    SubnetArn = field("SubnetArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AWSLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AWSLocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptAttachmentRequest:
    boto3_raw_data: "type_defs.AcceptAttachmentRequestTypeDef" = dataclasses.field()

    AttachmentId = field("AttachmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptAttachmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountStatus:
    boto3_raw_data: "type_defs.AccountStatusTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    SLRDeploymentStatus = field("SLRDeploymentStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateConnectPeerRequest:
    boto3_raw_data: "type_defs.AssociateConnectPeerRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    ConnectPeerId = field("ConnectPeerId")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateConnectPeerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateConnectPeerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectPeerAssociation:
    boto3_raw_data: "type_defs.ConnectPeerAssociationTypeDef" = dataclasses.field()

    ConnectPeerId = field("ConnectPeerId")
    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectPeerAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectPeerAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateCustomerGatewayRequest:
    boto3_raw_data: "type_defs.AssociateCustomerGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    CustomerGatewayArn = field("CustomerGatewayArn")
    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateCustomerGatewayRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateCustomerGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerGatewayAssociation:
    boto3_raw_data: "type_defs.CustomerGatewayAssociationTypeDef" = dataclasses.field()

    CustomerGatewayArn = field("CustomerGatewayArn")
    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomerGatewayAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerGatewayAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateLinkRequest:
    boto3_raw_data: "type_defs.AssociateLinkRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LinkAssociation:
    boto3_raw_data: "type_defs.LinkAssociationTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")
    LinkAssociationState = field("LinkAssociationState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LinkAssociationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LinkAssociationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateTransitGatewayConnectPeerRequest:
    boto3_raw_data: "type_defs.AssociateTransitGatewayConnectPeerRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    TransitGatewayConnectPeerArn = field("TransitGatewayConnectPeerArn")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateTransitGatewayConnectPeerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateTransitGatewayConnectPeerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitGatewayConnectPeerAssociation:
    boto3_raw_data: "type_defs.TransitGatewayConnectPeerAssociationTypeDef" = (
        dataclasses.field()
    )

    TransitGatewayConnectPeerArn = field("TransitGatewayConnectPeerArn")
    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")
    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TransitGatewayConnectPeerAssociationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitGatewayConnectPeerAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentError:
    boto3_raw_data: "type_defs.AttachmentErrorTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")
    ResourceArn = field("ResourceArn")
    RequestId = field("RequestId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachmentErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Bandwidth:
    boto3_raw_data: "type_defs.BandwidthTypeDef" = dataclasses.field()

    UploadSpeed = field("UploadSpeed")
    DownloadSpeed = field("DownloadSpeed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BandwidthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BandwidthTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BgpOptions:
    boto3_raw_data: "type_defs.BgpOptionsTypeDef" = dataclasses.field()

    PeerAsn = field("PeerAsn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BgpOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BgpOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectAttachmentOptions:
    boto3_raw_data: "type_defs.ConnectAttachmentOptionsTypeDef" = dataclasses.field()

    Protocol = field("Protocol")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectAttachmentOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectAttachmentOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectPeerBgpConfiguration:
    boto3_raw_data: "type_defs.ConnectPeerBgpConfigurationTypeDef" = dataclasses.field()

    CoreNetworkAsn = field("CoreNetworkAsn")
    PeerAsn = field("PeerAsn")
    CoreNetworkAddress = field("CoreNetworkAddress")
    PeerAddress = field("PeerAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectPeerBgpConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectPeerBgpConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectPeerError:
    boto3_raw_data: "type_defs.ConnectPeerErrorTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")
    ResourceArn = field("ResourceArn")
    RequestId = field("RequestId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectPeerErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectPeerErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionHealth:
    boto3_raw_data: "type_defs.ConnectionHealthTypeDef" = dataclasses.field()

    Type = field("Type")
    Status = field("Status")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionHealthTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkChangeEventValues:
    boto3_raw_data: "type_defs.CoreNetworkChangeEventValuesTypeDef" = (
        dataclasses.field()
    )

    EdgeLocation = field("EdgeLocation")
    SegmentName = field("SegmentName")
    NetworkFunctionGroupName = field("NetworkFunctionGroupName")
    AttachmentId = field("AttachmentId")
    Cidr = field("Cidr")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkChangeEventValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkChangeEventValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkEdge:
    boto3_raw_data: "type_defs.CoreNetworkEdgeTypeDef" = dataclasses.field()

    EdgeLocation = field("EdgeLocation")
    Asn = field("Asn")
    InsideCidrBlocks = field("InsideCidrBlocks")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkEdgeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoreNetworkEdgeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkNetworkFunctionGroupIdentifier:
    boto3_raw_data: "type_defs.CoreNetworkNetworkFunctionGroupIdentifierTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    NetworkFunctionGroupName = field("NetworkFunctionGroupName")
    EdgeLocation = field("EdgeLocation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CoreNetworkNetworkFunctionGroupIdentifierTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkNetworkFunctionGroupIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceInsertionSegments:
    boto3_raw_data: "type_defs.ServiceInsertionSegmentsTypeDef" = dataclasses.field()

    SendVia = field("SendVia")
    SendTo = field("SendTo")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceInsertionSegmentsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceInsertionSegmentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkPolicyError:
    boto3_raw_data: "type_defs.CoreNetworkPolicyErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    Message = field("Message")
    Path = field("Path")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkPolicyErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkPolicyErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkPolicyVersion:
    boto3_raw_data: "type_defs.CoreNetworkPolicyVersionTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    PolicyVersionId = field("PolicyVersionId")
    Alias = field("Alias")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    ChangeSetState = field("ChangeSetState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkPolicyVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkPolicyVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkSegmentEdgeIdentifier:
    boto3_raw_data: "type_defs.CoreNetworkSegmentEdgeIdentifierTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    SegmentName = field("SegmentName")
    EdgeLocation = field("EdgeLocation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CoreNetworkSegmentEdgeIdentifierTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkSegmentEdgeIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkSegment:
    boto3_raw_data: "type_defs.CoreNetworkSegmentTypeDef" = dataclasses.field()

    Name = field("Name")
    EdgeLocations = field("EdgeLocations")
    SharedSegments = field("SharedSegments")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkSegmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkSegmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Location:
    boto3_raw_data: "type_defs.LocationTypeDef" = dataclasses.field()

    Address = field("Address")
    Latitude = field("Latitude")
    Longitude = field("Longitude")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOptions:
    boto3_raw_data: "type_defs.VpcOptionsTypeDef" = dataclasses.field()

    Ipv6Support = field("Ipv6Support")
    ApplianceModeSupport = field("ApplianceModeSupport")
    DnsSupport = field("DnsSupport")
    SecurityGroupReferencingSupport = field("SecurityGroupReferencingSupport")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAttachmentRequest:
    boto3_raw_data: "type_defs.DeleteAttachmentRequestTypeDef" = dataclasses.field()

    AttachmentId = field("AttachmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAttachmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectPeerRequest:
    boto3_raw_data: "type_defs.DeleteConnectPeerRequestTypeDef" = dataclasses.field()

    ConnectPeerId = field("ConnectPeerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectPeerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectPeerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionRequest:
    boto3_raw_data: "type_defs.DeleteConnectionRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    ConnectionId = field("ConnectionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCoreNetworkPolicyVersionRequest:
    boto3_raw_data: "type_defs.DeleteCoreNetworkPolicyVersionRequestTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    PolicyVersionId = field("PolicyVersionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCoreNetworkPolicyVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCoreNetworkPolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCoreNetworkRequest:
    boto3_raw_data: "type_defs.DeleteCoreNetworkRequestTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCoreNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCoreNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeviceRequest:
    boto3_raw_data: "type_defs.DeleteDeviceRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlobalNetworkRequest:
    boto3_raw_data: "type_defs.DeleteGlobalNetworkRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGlobalNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlobalNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLinkRequest:
    boto3_raw_data: "type_defs.DeleteLinkRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    LinkId = field("LinkId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteLinkRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePeeringRequest:
    boto3_raw_data: "type_defs.DeletePeeringRequestTypeDef" = dataclasses.field()

    PeeringId = field("PeeringId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePeeringRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePeeringRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSiteRequest:
    boto3_raw_data: "type_defs.DeleteSiteRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    SiteId = field("SiteId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteSiteRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSiteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTransitGatewayRequest:
    boto3_raw_data: "type_defs.DeregisterTransitGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    TransitGatewayArn = field("TransitGatewayArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterTransitGatewayRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTransitGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalNetworksRequest:
    boto3_raw_data: "type_defs.DescribeGlobalNetworksRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkIds = field("GlobalNetworkIds")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGlobalNetworksRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalNetworksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateConnectPeerRequest:
    boto3_raw_data: "type_defs.DisassociateConnectPeerRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    ConnectPeerId = field("ConnectPeerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateConnectPeerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateConnectPeerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateCustomerGatewayRequest:
    boto3_raw_data: "type_defs.DisassociateCustomerGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    CustomerGatewayArn = field("CustomerGatewayArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateCustomerGatewayRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateCustomerGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateLinkRequest:
    boto3_raw_data: "type_defs.DisassociateLinkRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateTransitGatewayConnectPeerRequest:
    boto3_raw_data: "type_defs.DisassociateTransitGatewayConnectPeerRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    TransitGatewayConnectPeerArn = field("TransitGatewayConnectPeerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateTransitGatewayConnectPeerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateTransitGatewayConnectPeerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EdgeOverride:
    boto3_raw_data: "type_defs.EdgeOverrideTypeDef" = dataclasses.field()

    EdgeSets = field("EdgeSets")
    UseEdge = field("UseEdge")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdgeOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdgeOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteCoreNetworkChangeSetRequest:
    boto3_raw_data: "type_defs.ExecuteCoreNetworkChangeSetRequestTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    PolicyVersionId = field("PolicyVersionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExecuteCoreNetworkChangeSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteCoreNetworkChangeSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectAttachmentRequest:
    boto3_raw_data: "type_defs.GetConnectAttachmentRequestTypeDef" = dataclasses.field()

    AttachmentId = field("AttachmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectAttachmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectPeerAssociationsRequest:
    boto3_raw_data: "type_defs.GetConnectPeerAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    ConnectPeerIds = field("ConnectPeerIds")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConnectPeerAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectPeerAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectPeerRequest:
    boto3_raw_data: "type_defs.GetConnectPeerRequestTypeDef" = dataclasses.field()

    ConnectPeerId = field("ConnectPeerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectPeerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectPeerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionsRequest:
    boto3_raw_data: "type_defs.GetConnectionsRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    ConnectionIds = field("ConnectionIds")
    DeviceId = field("DeviceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreNetworkChangeEventsRequest:
    boto3_raw_data: "type_defs.GetCoreNetworkChangeEventsRequestTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    PolicyVersionId = field("PolicyVersionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCoreNetworkChangeEventsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreNetworkChangeEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreNetworkChangeSetRequest:
    boto3_raw_data: "type_defs.GetCoreNetworkChangeSetRequestTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    PolicyVersionId = field("PolicyVersionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCoreNetworkChangeSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreNetworkChangeSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreNetworkPolicyRequest:
    boto3_raw_data: "type_defs.GetCoreNetworkPolicyRequestTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    PolicyVersionId = field("PolicyVersionId")
    Alias = field("Alias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCoreNetworkPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreNetworkPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreNetworkRequest:
    boto3_raw_data: "type_defs.GetCoreNetworkRequestTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCoreNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomerGatewayAssociationsRequest:
    boto3_raw_data: "type_defs.GetCustomerGatewayAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    CustomerGatewayArns = field("CustomerGatewayArns")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCustomerGatewayAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomerGatewayAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDevicesRequest:
    boto3_raw_data: "type_defs.GetDevicesRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    DeviceIds = field("DeviceIds")
    SiteId = field("SiteId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDevicesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDevicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDirectConnectGatewayAttachmentRequest:
    boto3_raw_data: "type_defs.GetDirectConnectGatewayAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    AttachmentId = field("AttachmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDirectConnectGatewayAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDirectConnectGatewayAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLinkAssociationsRequest:
    boto3_raw_data: "type_defs.GetLinkAssociationsRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLinkAssociationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLinkAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLinksRequest:
    boto3_raw_data: "type_defs.GetLinksRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    LinkIds = field("LinkIds")
    SiteId = field("SiteId")
    Type = field("Type")
    Provider = field("Provider")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLinksRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetLinksRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkResourceCountsRequest:
    boto3_raw_data: "type_defs.GetNetworkResourceCountsRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    ResourceType = field("ResourceType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetNetworkResourceCountsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkResourceCountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkResourceCount:
    boto3_raw_data: "type_defs.NetworkResourceCountTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    Count = field("Count")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkResourceCountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkResourceCountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkResourceRelationshipsRequest:
    boto3_raw_data: "type_defs.GetNetworkResourceRelationshipsRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    CoreNetworkId = field("CoreNetworkId")
    RegisteredGatewayArn = field("RegisteredGatewayArn")
    AwsRegion = field("AwsRegion")
    AccountId = field("AccountId")
    ResourceType = field("ResourceType")
    ResourceArn = field("ResourceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNetworkResourceRelationshipsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkResourceRelationshipsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Relationship:
    boto3_raw_data: "type_defs.RelationshipTypeDef" = dataclasses.field()

    From = field("From")
    To = field("To")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelationshipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelationshipTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkResourcesRequest:
    boto3_raw_data: "type_defs.GetNetworkResourcesRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    CoreNetworkId = field("CoreNetworkId")
    RegisteredGatewayArn = field("RegisteredGatewayArn")
    AwsRegion = field("AwsRegion")
    AccountId = field("AccountId")
    ResourceType = field("ResourceType")
    ResourceArn = field("ResourceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNetworkResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkTelemetryRequest:
    boto3_raw_data: "type_defs.GetNetworkTelemetryRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    CoreNetworkId = field("CoreNetworkId")
    RegisteredGatewayArn = field("RegisteredGatewayArn")
    AwsRegion = field("AwsRegion")
    AccountId = field("AccountId")
    ResourceType = field("ResourceType")
    ResourceArn = field("ResourceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNetworkTelemetryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkTelemetryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyRequest:
    boto3_raw_data: "type_defs.GetResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRouteAnalysisRequest:
    boto3_raw_data: "type_defs.GetRouteAnalysisRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    RouteAnalysisId = field("RouteAnalysisId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRouteAnalysisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRouteAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSiteToSiteVpnAttachmentRequest:
    boto3_raw_data: "type_defs.GetSiteToSiteVpnAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    AttachmentId = field("AttachmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSiteToSiteVpnAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSiteToSiteVpnAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSitesRequest:
    boto3_raw_data: "type_defs.GetSitesRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    SiteIds = field("SiteIds")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSitesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetSitesRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransitGatewayConnectPeerAssociationsRequest:
    boto3_raw_data: (
        "type_defs.GetTransitGatewayConnectPeerAssociationsRequestTypeDef"
    ) = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    TransitGatewayConnectPeerArns = field("TransitGatewayConnectPeerArns")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTransitGatewayConnectPeerAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetTransitGatewayConnectPeerAssociationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransitGatewayPeeringRequest:
    boto3_raw_data: "type_defs.GetTransitGatewayPeeringRequestTypeDef" = (
        dataclasses.field()
    )

    PeeringId = field("PeeringId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTransitGatewayPeeringRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransitGatewayPeeringRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransitGatewayRegistrationsRequest:
    boto3_raw_data: "type_defs.GetTransitGatewayRegistrationsRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    TransitGatewayArns = field("TransitGatewayArns")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTransitGatewayRegistrationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransitGatewayRegistrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransitGatewayRouteTableAttachmentRequest:
    boto3_raw_data: "type_defs.GetTransitGatewayRouteTableAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    AttachmentId = field("AttachmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTransitGatewayRouteTableAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransitGatewayRouteTableAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcAttachmentRequest:
    boto3_raw_data: "type_defs.GetVpcAttachmentRequestTypeDef" = dataclasses.field()

    AttachmentId = field("AttachmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVpcAttachmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachmentsRequest:
    boto3_raw_data: "type_defs.ListAttachmentsRequestTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    AttachmentType = field("AttachmentType")
    EdgeLocation = field("EdgeLocation")
    State = field("State")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttachmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectPeersRequest:
    boto3_raw_data: "type_defs.ListConnectPeersRequestTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    ConnectAttachmentId = field("ConnectAttachmentId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectPeersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectPeersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreNetworkPolicyVersionsRequest:
    boto3_raw_data: "type_defs.ListCoreNetworkPolicyVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCoreNetworkPolicyVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreNetworkPolicyVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreNetworksRequest:
    boto3_raw_data: "type_defs.ListCoreNetworksRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoreNetworksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreNetworksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationServiceAccessStatusRequest:
    boto3_raw_data: "type_defs.ListOrganizationServiceAccessStatusRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationServiceAccessStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationServiceAccessStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPeeringsRequest:
    boto3_raw_data: "type_defs.ListPeeringsRequestTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    PeeringType = field("PeeringType")
    EdgeLocation = field("EdgeLocation")
    State = field("State")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPeeringsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPeeringsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFunctionGroup:
    boto3_raw_data: "type_defs.NetworkFunctionGroupTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkFunctionGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFunctionGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkResourceSummary:
    boto3_raw_data: "type_defs.NetworkResourceSummaryTypeDef" = dataclasses.field()

    RegisteredGatewayArn = field("RegisteredGatewayArn")
    ResourceArn = field("ResourceArn")
    ResourceType = field("ResourceType")
    Definition = field("Definition")
    NameTag = field("NameTag")
    IsMiddlebox = field("IsMiddlebox")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkResourceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkRouteDestination:
    boto3_raw_data: "type_defs.NetworkRouteDestinationTypeDef" = dataclasses.field()

    CoreNetworkAttachmentId = field("CoreNetworkAttachmentId")
    TransitGatewayAttachmentId = field("TransitGatewayAttachmentId")
    SegmentName = field("SegmentName")
    NetworkFunctionGroupName = field("NetworkFunctionGroupName")
    EdgeLocation = field("EdgeLocation")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkRouteDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkRouteDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionsErrorContext:
    boto3_raw_data: "type_defs.PermissionsErrorContextTypeDef" = dataclasses.field()

    MissingPermission = field("MissingPermission")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PermissionsErrorContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PermissionsErrorContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutCoreNetworkPolicyRequest:
    boto3_raw_data: "type_defs.PutCoreNetworkPolicyRequestTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    PolicyDocument = field("PolicyDocument")
    Description = field("Description")
    LatestVersionId = field("LatestVersionId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutCoreNetworkPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutCoreNetworkPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    PolicyDocument = field("PolicyDocument")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTransitGatewayRequest:
    boto3_raw_data: "type_defs.RegisterTransitGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    TransitGatewayArn = field("TransitGatewayArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterTransitGatewayRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTransitGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectAttachmentRequest:
    boto3_raw_data: "type_defs.RejectAttachmentRequestTypeDef" = dataclasses.field()

    AttachmentId = field("AttachmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectAttachmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreCoreNetworkPolicyVersionRequest:
    boto3_raw_data: "type_defs.RestoreCoreNetworkPolicyVersionRequestTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    PolicyVersionId = field("PolicyVersionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreCoreNetworkPolicyVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreCoreNetworkPolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteAnalysisCompletion:
    boto3_raw_data: "type_defs.RouteAnalysisCompletionTypeDef" = dataclasses.field()

    ResultCode = field("ResultCode")
    ReasonCode = field("ReasonCode")
    ReasonContext = field("ReasonContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteAnalysisCompletionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteAnalysisCompletionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteAnalysisEndpointOptionsSpecification:
    boto3_raw_data: "type_defs.RouteAnalysisEndpointOptionsSpecificationTypeDef" = (
        dataclasses.field()
    )

    TransitGatewayAttachmentArn = field("TransitGatewayAttachmentArn")
    IpAddress = field("IpAddress")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RouteAnalysisEndpointOptionsSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteAnalysisEndpointOptionsSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteAnalysisEndpointOptions:
    boto3_raw_data: "type_defs.RouteAnalysisEndpointOptionsTypeDef" = (
        dataclasses.field()
    )

    TransitGatewayAttachmentArn = field("TransitGatewayAttachmentArn")
    TransitGatewayArn = field("TransitGatewayArn")
    IpAddress = field("IpAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteAnalysisEndpointOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteAnalysisEndpointOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WhenSentTo:
    boto3_raw_data: "type_defs.WhenSentToTypeDef" = dataclasses.field()

    WhenSentToSegmentsList = field("WhenSentToSegmentsList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WhenSentToTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WhenSentToTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOrganizationServiceAccessUpdateRequest:
    boto3_raw_data: "type_defs.StartOrganizationServiceAccessUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    Action = field("Action")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartOrganizationServiceAccessUpdateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOrganizationServiceAccessUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitGatewayRegistrationStateReason:
    boto3_raw_data: "type_defs.TransitGatewayRegistrationStateReasonTypeDef" = (
        dataclasses.field()
    )

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TransitGatewayRegistrationStateReasonTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitGatewayRegistrationStateReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionRequest:
    boto3_raw_data: "type_defs.UpdateConnectionRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    ConnectionId = field("ConnectionId")
    LinkId = field("LinkId")
    ConnectedLinkId = field("ConnectedLinkId")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCoreNetworkRequest:
    boto3_raw_data: "type_defs.UpdateCoreNetworkRequestTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCoreNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCoreNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectConnectGatewayAttachmentRequest:
    boto3_raw_data: "type_defs.UpdateDirectConnectGatewayAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    AttachmentId = field("AttachmentId")
    EdgeLocations = field("EdgeLocations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDirectConnectGatewayAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectConnectGatewayAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlobalNetworkRequest:
    boto3_raw_data: "type_defs.UpdateGlobalNetworkRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlobalNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNetworkResourceMetadataRequest:
    boto3_raw_data: "type_defs.UpdateNetworkResourceMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    ResourceArn = field("ResourceArn")
    Metadata = field("Metadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateNetworkResourceMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNetworkResourceMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyResponse:
    boto3_raw_data: "type_defs.GetResourcePolicyResponseTypeDef" = dataclasses.field()

    PolicyDocument = field("PolicyDocument")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNetworkResourceMetadataResponse:
    boto3_raw_data: "type_defs.UpdateNetworkResourceMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    Metadata = field("Metadata")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateNetworkResourceMetadataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNetworkResourceMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationStatus:
    boto3_raw_data: "type_defs.OrganizationStatusTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    OrganizationAwsServiceAccessStatus = field("OrganizationAwsServiceAccessStatus")
    SLRDeploymentStatus = field("SLRDeploymentStatus")

    @cached_property
    def AccountStatusList(self):  # pragma: no cover
        return AccountStatus.make_many(self.boto3_raw_data["AccountStatusList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateConnectPeerResponse:
    boto3_raw_data: "type_defs.AssociateConnectPeerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConnectPeerAssociation(self):  # pragma: no cover
        return ConnectPeerAssociation.make_one(
            self.boto3_raw_data["ConnectPeerAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateConnectPeerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateConnectPeerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateConnectPeerResponse:
    boto3_raw_data: "type_defs.DisassociateConnectPeerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConnectPeerAssociation(self):  # pragma: no cover
        return ConnectPeerAssociation.make_one(
            self.boto3_raw_data["ConnectPeerAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateConnectPeerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateConnectPeerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectPeerAssociationsResponse:
    boto3_raw_data: "type_defs.GetConnectPeerAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConnectPeerAssociations(self):  # pragma: no cover
        return ConnectPeerAssociation.make_many(
            self.boto3_raw_data["ConnectPeerAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConnectPeerAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectPeerAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateCustomerGatewayResponse:
    boto3_raw_data: "type_defs.AssociateCustomerGatewayResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CustomerGatewayAssociation(self):  # pragma: no cover
        return CustomerGatewayAssociation.make_one(
            self.boto3_raw_data["CustomerGatewayAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateCustomerGatewayResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateCustomerGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateCustomerGatewayResponse:
    boto3_raw_data: "type_defs.DisassociateCustomerGatewayResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CustomerGatewayAssociation(self):  # pragma: no cover
        return CustomerGatewayAssociation.make_one(
            self.boto3_raw_data["CustomerGatewayAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateCustomerGatewayResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateCustomerGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomerGatewayAssociationsResponse:
    boto3_raw_data: "type_defs.GetCustomerGatewayAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CustomerGatewayAssociations(self):  # pragma: no cover
        return CustomerGatewayAssociation.make_many(
            self.boto3_raw_data["CustomerGatewayAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCustomerGatewayAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomerGatewayAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateLinkResponse:
    boto3_raw_data: "type_defs.AssociateLinkResponseTypeDef" = dataclasses.field()

    @cached_property
    def LinkAssociation(self):  # pragma: no cover
        return LinkAssociation.make_one(self.boto3_raw_data["LinkAssociation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateLinkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateLinkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateLinkResponse:
    boto3_raw_data: "type_defs.DisassociateLinkResponseTypeDef" = dataclasses.field()

    @cached_property
    def LinkAssociation(self):  # pragma: no cover
        return LinkAssociation.make_one(self.boto3_raw_data["LinkAssociation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateLinkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateLinkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLinkAssociationsResponse:
    boto3_raw_data: "type_defs.GetLinkAssociationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def LinkAssociations(self):  # pragma: no cover
        return LinkAssociation.make_many(self.boto3_raw_data["LinkAssociations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLinkAssociationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLinkAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateTransitGatewayConnectPeerResponse:
    boto3_raw_data: "type_defs.AssociateTransitGatewayConnectPeerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TransitGatewayConnectPeerAssociation(self):  # pragma: no cover
        return TransitGatewayConnectPeerAssociation.make_one(
            self.boto3_raw_data["TransitGatewayConnectPeerAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateTransitGatewayConnectPeerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateTransitGatewayConnectPeerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateTransitGatewayConnectPeerResponse:
    boto3_raw_data: "type_defs.DisassociateTransitGatewayConnectPeerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TransitGatewayConnectPeerAssociation(self):  # pragma: no cover
        return TransitGatewayConnectPeerAssociation.make_one(
            self.boto3_raw_data["TransitGatewayConnectPeerAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateTransitGatewayConnectPeerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateTransitGatewayConnectPeerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransitGatewayConnectPeerAssociationsResponse:
    boto3_raw_data: (
        "type_defs.GetTransitGatewayConnectPeerAssociationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def TransitGatewayConnectPeerAssociations(self):  # pragma: no cover
        return TransitGatewayConnectPeerAssociation.make_many(
            self.boto3_raw_data["TransitGatewayConnectPeerAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTransitGatewayConnectPeerAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetTransitGatewayConnectPeerAssociationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectPeerSummary:
    boto3_raw_data: "type_defs.ConnectPeerSummaryTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    ConnectAttachmentId = field("ConnectAttachmentId")
    ConnectPeerId = field("ConnectPeerId")
    EdgeLocation = field("EdgeLocation")
    ConnectPeerState = field("ConnectPeerState")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SubnetArn = field("SubnetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectPeerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectPeerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Connection:
    boto3_raw_data: "type_defs.ConnectionTypeDef" = dataclasses.field()

    ConnectionId = field("ConnectionId")
    ConnectionArn = field("ConnectionArn")
    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    ConnectedDeviceId = field("ConnectedDeviceId")
    LinkId = field("LinkId")
    ConnectedLinkId = field("ConnectedLinkId")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    State = field("State")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkSummary:
    boto3_raw_data: "type_defs.CoreNetworkSummaryTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    CoreNetworkArn = field("CoreNetworkArn")
    GlobalNetworkId = field("GlobalNetworkId")
    OwnerAccountId = field("OwnerAccountId")
    State = field("State")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionRequest:
    boto3_raw_data: "type_defs.CreateConnectionRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    ConnectedDeviceId = field("ConnectedDeviceId")
    LinkId = field("LinkId")
    ConnectedLinkId = field("ConnectedLinkId")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCoreNetworkRequest:
    boto3_raw_data: "type_defs.CreateCoreNetworkRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    PolicyDocument = field("PolicyDocument")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCoreNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCoreNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectConnectGatewayAttachmentRequest:
    boto3_raw_data: "type_defs.CreateDirectConnectGatewayAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    DirectConnectGatewayArn = field("DirectConnectGatewayArn")
    EdgeLocations = field("EdgeLocations")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDirectConnectGatewayAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectConnectGatewayAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalNetworkRequest:
    boto3_raw_data: "type_defs.CreateGlobalNetworkRequestTypeDef" = dataclasses.field()

    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlobalNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSiteToSiteVpnAttachmentRequest:
    boto3_raw_data: "type_defs.CreateSiteToSiteVpnAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    VpnConnectionArn = field("VpnConnectionArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSiteToSiteVpnAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSiteToSiteVpnAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTransitGatewayPeeringRequest:
    boto3_raw_data: "type_defs.CreateTransitGatewayPeeringRequestTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    TransitGatewayArn = field("TransitGatewayArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTransitGatewayPeeringRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTransitGatewayPeeringRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTransitGatewayRouteTableAttachmentRequest:
    boto3_raw_data: (
        "type_defs.CreateTransitGatewayRouteTableAttachmentRequestTypeDef"
    ) = dataclasses.field()

    PeeringId = field("PeeringId")
    TransitGatewayRouteTableArn = field("TransitGatewayRouteTableArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTransitGatewayRouteTableAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CreateTransitGatewayRouteTableAttachmentRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalNetwork:
    boto3_raw_data: "type_defs.GlobalNetworkTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    GlobalNetworkArn = field("GlobalNetworkArn")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    State = field("State")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlobalNetworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GlobalNetworkTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkResource:
    boto3_raw_data: "type_defs.NetworkResourceTypeDef" = dataclasses.field()

    RegisteredGatewayArn = field("RegisteredGatewayArn")
    CoreNetworkId = field("CoreNetworkId")
    AwsRegion = field("AwsRegion")
    AccountId = field("AccountId")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    ResourceArn = field("ResourceArn")
    Definition = field("Definition")
    DefinitionTimestamp = field("DefinitionTimestamp")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Metadata = field("Metadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProposedNetworkFunctionGroupChange:
    boto3_raw_data: "type_defs.ProposedNetworkFunctionGroupChangeTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AttachmentPolicyRuleNumber = field("AttachmentPolicyRuleNumber")
    NetworkFunctionGroupName = field("NetworkFunctionGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProposedNetworkFunctionGroupChangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProposedNetworkFunctionGroupChangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProposedSegmentChange:
    boto3_raw_data: "type_defs.ProposedSegmentChangeTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AttachmentPolicyRuleNumber = field("AttachmentPolicyRuleNumber")
    SegmentName = field("SegmentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProposedSegmentChangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProposedSegmentChangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLinkRequest:
    boto3_raw_data: "type_defs.CreateLinkRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")

    @cached_property
    def Bandwidth(self):  # pragma: no cover
        return Bandwidth.make_one(self.boto3_raw_data["Bandwidth"])

    SiteId = field("SiteId")
    Description = field("Description")
    Type = field("Type")
    Provider = field("Provider")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateLinkRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Link:
    boto3_raw_data: "type_defs.LinkTypeDef" = dataclasses.field()

    LinkId = field("LinkId")
    LinkArn = field("LinkArn")
    GlobalNetworkId = field("GlobalNetworkId")
    SiteId = field("SiteId")
    Description = field("Description")
    Type = field("Type")

    @cached_property
    def Bandwidth(self):  # pragma: no cover
        return Bandwidth.make_one(self.boto3_raw_data["Bandwidth"])

    Provider = field("Provider")
    CreatedAt = field("CreatedAt")
    State = field("State")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LinkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLinkRequest:
    boto3_raw_data: "type_defs.UpdateLinkRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    LinkId = field("LinkId")
    Description = field("Description")
    Type = field("Type")

    @cached_property
    def Bandwidth(self):  # pragma: no cover
        return Bandwidth.make_one(self.boto3_raw_data["Bandwidth"])

    Provider = field("Provider")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateLinkRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectPeerRequest:
    boto3_raw_data: "type_defs.CreateConnectPeerRequestTypeDef" = dataclasses.field()

    ConnectAttachmentId = field("ConnectAttachmentId")
    PeerAddress = field("PeerAddress")
    CoreNetworkAddress = field("CoreNetworkAddress")

    @cached_property
    def BgpOptions(self):  # pragma: no cover
        return BgpOptions.make_one(self.boto3_raw_data["BgpOptions"])

    InsideCidrBlocks = field("InsideCidrBlocks")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")
    SubnetArn = field("SubnetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectPeerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectPeerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectAttachmentRequest:
    boto3_raw_data: "type_defs.CreateConnectAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    EdgeLocation = field("EdgeLocation")
    TransportAttachmentId = field("TransportAttachmentId")

    @cached_property
    def Options(self):  # pragma: no cover
        return ConnectAttachmentOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConnectAttachmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectPeerConfiguration:
    boto3_raw_data: "type_defs.ConnectPeerConfigurationTypeDef" = dataclasses.field()

    CoreNetworkAddress = field("CoreNetworkAddress")
    PeerAddress = field("PeerAddress")
    InsideCidrBlocks = field("InsideCidrBlocks")
    Protocol = field("Protocol")

    @cached_property
    def BgpConfigurations(self):  # pragma: no cover
        return ConnectPeerBgpConfiguration.make_many(
            self.boto3_raw_data["BgpConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectPeerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectPeerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkTelemetry:
    boto3_raw_data: "type_defs.NetworkTelemetryTypeDef" = dataclasses.field()

    RegisteredGatewayArn = field("RegisteredGatewayArn")
    CoreNetworkId = field("CoreNetworkId")
    AwsRegion = field("AwsRegion")
    AccountId = field("AccountId")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    ResourceArn = field("ResourceArn")
    Address = field("Address")

    @cached_property
    def Health(self):  # pragma: no cover
        return ConnectionHealth.make_one(self.boto3_raw_data["Health"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkTelemetryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkTelemetryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkChangeEvent:
    boto3_raw_data: "type_defs.CoreNetworkChangeEventTypeDef" = dataclasses.field()

    Type = field("Type")
    Action = field("Action")
    IdentifierPath = field("IdentifierPath")
    EventTime = field("EventTime")
    Status = field("Status")

    @cached_property
    def Values(self):  # pragma: no cover
        return CoreNetworkChangeEventValues.make_one(self.boto3_raw_data["Values"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkChangeEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkChangeEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkNetworkFunctionGroup:
    boto3_raw_data: "type_defs.CoreNetworkNetworkFunctionGroupTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    EdgeLocations = field("EdgeLocations")

    @cached_property
    def Segments(self):  # pragma: no cover
        return ServiceInsertionSegments.make_one(self.boto3_raw_data["Segments"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CoreNetworkNetworkFunctionGroupTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkNetworkFunctionGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkPolicy:
    boto3_raw_data: "type_defs.CoreNetworkPolicyTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    PolicyVersionId = field("PolicyVersionId")
    Alias = field("Alias")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    ChangeSetState = field("ChangeSetState")

    @cached_property
    def PolicyErrors(self):  # pragma: no cover
        return CoreNetworkPolicyError.make_many(self.boto3_raw_data["PolicyErrors"])

    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreNetworkPolicyVersionsResponse:
    boto3_raw_data: "type_defs.ListCoreNetworkPolicyVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CoreNetworkPolicyVersions(self):  # pragma: no cover
        return CoreNetworkPolicyVersion.make_many(
            self.boto3_raw_data["CoreNetworkPolicyVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCoreNetworkPolicyVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreNetworkPolicyVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTableIdentifier:
    boto3_raw_data: "type_defs.RouteTableIdentifierTypeDef" = dataclasses.field()

    TransitGatewayRouteTableArn = field("TransitGatewayRouteTableArn")

    @cached_property
    def CoreNetworkSegmentEdge(self):  # pragma: no cover
        return CoreNetworkSegmentEdgeIdentifier.make_one(
            self.boto3_raw_data["CoreNetworkSegmentEdge"]
        )

    @cached_property
    def CoreNetworkNetworkFunctionGroup(self):  # pragma: no cover
        return CoreNetworkNetworkFunctionGroupIdentifier.make_one(
            self.boto3_raw_data["CoreNetworkNetworkFunctionGroup"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteTableIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTableIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeviceRequest:
    boto3_raw_data: "type_defs.CreateDeviceRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")

    @cached_property
    def AWSLocation(self):  # pragma: no cover
        return AWSLocation.make_one(self.boto3_raw_data["AWSLocation"])

    Description = field("Description")
    Type = field("Type")
    Vendor = field("Vendor")
    Model = field("Model")
    SerialNumber = field("SerialNumber")

    @cached_property
    def Location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["Location"])

    SiteId = field("SiteId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSiteRequest:
    boto3_raw_data: "type_defs.CreateSiteRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    Description = field("Description")

    @cached_property
    def Location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["Location"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateSiteRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSiteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Device:
    boto3_raw_data: "type_defs.DeviceTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")
    DeviceArn = field("DeviceArn")
    GlobalNetworkId = field("GlobalNetworkId")

    @cached_property
    def AWSLocation(self):  # pragma: no cover
        return AWSLocation.make_one(self.boto3_raw_data["AWSLocation"])

    Description = field("Description")
    Type = field("Type")
    Vendor = field("Vendor")
    Model = field("Model")
    SerialNumber = field("SerialNumber")

    @cached_property
    def Location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["Location"])

    SiteId = field("SiteId")
    CreatedAt = field("CreatedAt")
    State = field("State")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Site:
    boto3_raw_data: "type_defs.SiteTypeDef" = dataclasses.field()

    SiteId = field("SiteId")
    SiteArn = field("SiteArn")
    GlobalNetworkId = field("GlobalNetworkId")
    Description = field("Description")

    @cached_property
    def Location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["Location"])

    CreatedAt = field("CreatedAt")
    State = field("State")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SiteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SiteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeviceRequest:
    boto3_raw_data: "type_defs.UpdateDeviceRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")

    @cached_property
    def AWSLocation(self):  # pragma: no cover
        return AWSLocation.make_one(self.boto3_raw_data["AWSLocation"])

    Description = field("Description")
    Type = field("Type")
    Vendor = field("Vendor")
    Model = field("Model")
    SerialNumber = field("SerialNumber")

    @cached_property
    def Location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["Location"])

    SiteId = field("SiteId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSiteRequest:
    boto3_raw_data: "type_defs.UpdateSiteRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    SiteId = field("SiteId")
    Description = field("Description")

    @cached_property
    def Location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateSiteRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSiteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcAttachmentRequest:
    boto3_raw_data: "type_defs.CreateVpcAttachmentRequestTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    VpcArn = field("VpcArn")
    SubnetArns = field("SubnetArns")

    @cached_property
    def Options(self):  # pragma: no cover
        return VpcOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcAttachmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcAttachmentRequest:
    boto3_raw_data: "type_defs.UpdateVpcAttachmentRequestTypeDef" = dataclasses.field()

    AttachmentId = field("AttachmentId")
    AddSubnetArns = field("AddSubnetArns")
    RemoveSubnetArns = field("RemoveSubnetArns")

    @cached_property
    def Options(self):  # pragma: no cover
        return VpcOptions.make_one(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcAttachmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalNetworksRequestPaginate:
    boto3_raw_data: "type_defs.DescribeGlobalNetworksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkIds = field("GlobalNetworkIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGlobalNetworksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalNetworksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectPeerAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.GetConnectPeerAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    ConnectPeerIds = field("ConnectPeerIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConnectPeerAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectPeerAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionsRequestPaginate:
    boto3_raw_data: "type_defs.GetConnectionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    ConnectionIds = field("ConnectionIds")
    DeviceId = field("DeviceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetConnectionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreNetworkChangeEventsRequestPaginate:
    boto3_raw_data: "type_defs.GetCoreNetworkChangeEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    PolicyVersionId = field("PolicyVersionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCoreNetworkChangeEventsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreNetworkChangeEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreNetworkChangeSetRequestPaginate:
    boto3_raw_data: "type_defs.GetCoreNetworkChangeSetRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    PolicyVersionId = field("PolicyVersionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCoreNetworkChangeSetRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreNetworkChangeSetRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomerGatewayAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.GetCustomerGatewayAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    CustomerGatewayArns = field("CustomerGatewayArns")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCustomerGatewayAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomerGatewayAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDevicesRequestPaginate:
    boto3_raw_data: "type_defs.GetDevicesRequestPaginateTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    DeviceIds = field("DeviceIds")
    SiteId = field("SiteId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDevicesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDevicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLinkAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.GetLinkAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    DeviceId = field("DeviceId")
    LinkId = field("LinkId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLinkAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLinkAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLinksRequestPaginate:
    boto3_raw_data: "type_defs.GetLinksRequestPaginateTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    LinkIds = field("LinkIds")
    SiteId = field("SiteId")
    Type = field("Type")
    Provider = field("Provider")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLinksRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLinksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkResourceCountsRequestPaginate:
    boto3_raw_data: "type_defs.GetNetworkResourceCountsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    ResourceType = field("ResourceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNetworkResourceCountsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkResourceCountsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkResourceRelationshipsRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetNetworkResourceRelationshipsRequestPaginateTypeDef"
    ) = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    CoreNetworkId = field("CoreNetworkId")
    RegisteredGatewayArn = field("RegisteredGatewayArn")
    AwsRegion = field("AwsRegion")
    AccountId = field("AccountId")
    ResourceType = field("ResourceType")
    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNetworkResourceRelationshipsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetNetworkResourceRelationshipsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkResourcesRequestPaginate:
    boto3_raw_data: "type_defs.GetNetworkResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    CoreNetworkId = field("CoreNetworkId")
    RegisteredGatewayArn = field("RegisteredGatewayArn")
    AwsRegion = field("AwsRegion")
    AccountId = field("AccountId")
    ResourceType = field("ResourceType")
    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNetworkResourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkTelemetryRequestPaginate:
    boto3_raw_data: "type_defs.GetNetworkTelemetryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    CoreNetworkId = field("CoreNetworkId")
    RegisteredGatewayArn = field("RegisteredGatewayArn")
    AwsRegion = field("AwsRegion")
    AccountId = field("AccountId")
    ResourceType = field("ResourceType")
    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNetworkTelemetryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkTelemetryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSitesRequestPaginate:
    boto3_raw_data: "type_defs.GetSitesRequestPaginateTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    SiteIds = field("SiteIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSitesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSitesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransitGatewayConnectPeerAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetTransitGatewayConnectPeerAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    TransitGatewayConnectPeerArns = field("TransitGatewayConnectPeerArns")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTransitGatewayConnectPeerAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetTransitGatewayConnectPeerAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransitGatewayRegistrationsRequestPaginate:
    boto3_raw_data: "type_defs.GetTransitGatewayRegistrationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalNetworkId = field("GlobalNetworkId")
    TransitGatewayArns = field("TransitGatewayArns")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTransitGatewayRegistrationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransitGatewayRegistrationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListAttachmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    AttachmentType = field("AttachmentType")
    EdgeLocation = field("EdgeLocation")
    State = field("State")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAttachmentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectPeersRequestPaginate:
    boto3_raw_data: "type_defs.ListConnectPeersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")
    ConnectAttachmentId = field("ConnectAttachmentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConnectPeersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectPeersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreNetworkPolicyVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListCoreNetworkPolicyVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CoreNetworkId = field("CoreNetworkId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCoreNetworkPolicyVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreNetworkPolicyVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreNetworksRequestPaginate:
    boto3_raw_data: "type_defs.ListCoreNetworksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCoreNetworksRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreNetworksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPeeringsRequestPaginate:
    boto3_raw_data: "type_defs.ListPeeringsRequestPaginateTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    PeeringType = field("PeeringType")
    EdgeLocation = field("EdgeLocation")
    State = field("State")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPeeringsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPeeringsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkResourceCountsResponse:
    boto3_raw_data: "type_defs.GetNetworkResourceCountsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NetworkResourceCounts(self):  # pragma: no cover
        return NetworkResourceCount.make_many(
            self.boto3_raw_data["NetworkResourceCounts"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetNetworkResourceCountsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkResourceCountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkResourceRelationshipsResponse:
    boto3_raw_data: "type_defs.GetNetworkResourceRelationshipsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Relationships(self):  # pragma: no cover
        return Relationship.make_many(self.boto3_raw_data["Relationships"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNetworkResourceRelationshipsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkResourceRelationshipsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Via:
    boto3_raw_data: "type_defs.ViaTypeDef" = dataclasses.field()

    @cached_property
    def NetworkFunctionGroups(self):  # pragma: no cover
        return NetworkFunctionGroup.make_many(
            self.boto3_raw_data["NetworkFunctionGroups"]
        )

    @cached_property
    def WithEdgeOverrides(self):  # pragma: no cover
        return EdgeOverride.make_many(self.boto3_raw_data["WithEdgeOverrides"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ViaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathComponent:
    boto3_raw_data: "type_defs.PathComponentTypeDef" = dataclasses.field()

    Sequence = field("Sequence")

    @cached_property
    def Resource(self):  # pragma: no cover
        return NetworkResourceSummary.make_one(self.boto3_raw_data["Resource"])

    DestinationCidrBlock = field("DestinationCidrBlock")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathComponentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PathComponentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkRoute:
    boto3_raw_data: "type_defs.NetworkRouteTypeDef" = dataclasses.field()

    DestinationCidrBlock = field("DestinationCidrBlock")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return NetworkRouteDestination.make_many(self.boto3_raw_data["Destinations"])

    PrefixListId = field("PrefixListId")
    State = field("State")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkRouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkRouteTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PeeringError:
    boto3_raw_data: "type_defs.PeeringErrorTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")
    ResourceArn = field("ResourceArn")
    RequestId = field("RequestId")

    @cached_property
    def MissingPermissionsContext(self):  # pragma: no cover
        return PermissionsErrorContext.make_one(
            self.boto3_raw_data["MissingPermissionsContext"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PeeringErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PeeringErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRouteAnalysisRequest:
    boto3_raw_data: "type_defs.StartRouteAnalysisRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")

    @cached_property
    def Source(self):  # pragma: no cover
        return RouteAnalysisEndpointOptionsSpecification.make_one(
            self.boto3_raw_data["Source"]
        )

    @cached_property
    def Destination(self):  # pragma: no cover
        return RouteAnalysisEndpointOptionsSpecification.make_one(
            self.boto3_raw_data["Destination"]
        )

    IncludeReturnPath = field("IncludeReturnPath")
    UseMiddleboxes = field("UseMiddleboxes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRouteAnalysisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRouteAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitGatewayRegistration:
    boto3_raw_data: "type_defs.TransitGatewayRegistrationTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    TransitGatewayArn = field("TransitGatewayArn")

    @cached_property
    def State(self):  # pragma: no cover
        return TransitGatewayRegistrationStateReason.make_one(
            self.boto3_raw_data["State"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransitGatewayRegistrationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitGatewayRegistrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationServiceAccessStatusResponse:
    boto3_raw_data: "type_defs.ListOrganizationServiceAccessStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrganizationStatus(self):  # pragma: no cover
        return OrganizationStatus.make_one(self.boto3_raw_data["OrganizationStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationServiceAccessStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationServiceAccessStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOrganizationServiceAccessUpdateResponse:
    boto3_raw_data: "type_defs.StartOrganizationServiceAccessUpdateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrganizationStatus(self):  # pragma: no cover
        return OrganizationStatus.make_one(self.boto3_raw_data["OrganizationStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartOrganizationServiceAccessUpdateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOrganizationServiceAccessUpdateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectPeersResponse:
    boto3_raw_data: "type_defs.ListConnectPeersResponseTypeDef" = dataclasses.field()

    @cached_property
    def ConnectPeers(self):  # pragma: no cover
        return ConnectPeerSummary.make_many(self.boto3_raw_data["ConnectPeers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectPeersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectPeersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionResponse:
    boto3_raw_data: "type_defs.CreateConnectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connection(self):  # pragma: no cover
        return Connection.make_one(self.boto3_raw_data["Connection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionResponse:
    boto3_raw_data: "type_defs.DeleteConnectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connection(self):  # pragma: no cover
        return Connection.make_one(self.boto3_raw_data["Connection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionsResponse:
    boto3_raw_data: "type_defs.GetConnectionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connections(self):  # pragma: no cover
        return Connection.make_many(self.boto3_raw_data["Connections"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionResponse:
    boto3_raw_data: "type_defs.UpdateConnectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connection(self):  # pragma: no cover
        return Connection.make_one(self.boto3_raw_data["Connection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreNetworksResponse:
    boto3_raw_data: "type_defs.ListCoreNetworksResponseTypeDef" = dataclasses.field()

    @cached_property
    def CoreNetworks(self):  # pragma: no cover
        return CoreNetworkSummary.make_many(self.boto3_raw_data["CoreNetworks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoreNetworksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreNetworksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalNetworkResponse:
    boto3_raw_data: "type_defs.CreateGlobalNetworkResponseTypeDef" = dataclasses.field()

    @cached_property
    def GlobalNetwork(self):  # pragma: no cover
        return GlobalNetwork.make_one(self.boto3_raw_data["GlobalNetwork"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlobalNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlobalNetworkResponse:
    boto3_raw_data: "type_defs.DeleteGlobalNetworkResponseTypeDef" = dataclasses.field()

    @cached_property
    def GlobalNetwork(self):  # pragma: no cover
        return GlobalNetwork.make_one(self.boto3_raw_data["GlobalNetwork"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGlobalNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlobalNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalNetworksResponse:
    boto3_raw_data: "type_defs.DescribeGlobalNetworksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalNetworks(self):  # pragma: no cover
        return GlobalNetwork.make_many(self.boto3_raw_data["GlobalNetworks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGlobalNetworksResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalNetworksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlobalNetworkResponse:
    boto3_raw_data: "type_defs.UpdateGlobalNetworkResponseTypeDef" = dataclasses.field()

    @cached_property
    def GlobalNetwork(self):  # pragma: no cover
        return GlobalNetwork.make_one(self.boto3_raw_data["GlobalNetwork"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlobalNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkResourcesResponse:
    boto3_raw_data: "type_defs.GetNetworkResourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def NetworkResources(self):  # pragma: no cover
        return NetworkResource.make_many(self.boto3_raw_data["NetworkResources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNetworkResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attachment:
    boto3_raw_data: "type_defs.AttachmentTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    CoreNetworkArn = field("CoreNetworkArn")
    AttachmentId = field("AttachmentId")
    OwnerAccountId = field("OwnerAccountId")
    AttachmentType = field("AttachmentType")
    State = field("State")
    EdgeLocation = field("EdgeLocation")
    EdgeLocations = field("EdgeLocations")
    ResourceArn = field("ResourceArn")
    AttachmentPolicyRuleNumber = field("AttachmentPolicyRuleNumber")
    SegmentName = field("SegmentName")
    NetworkFunctionGroupName = field("NetworkFunctionGroupName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ProposedSegmentChange(self):  # pragma: no cover
        return ProposedSegmentChange.make_one(
            self.boto3_raw_data["ProposedSegmentChange"]
        )

    @cached_property
    def ProposedNetworkFunctionGroupChange(self):  # pragma: no cover
        return ProposedNetworkFunctionGroupChange.make_one(
            self.boto3_raw_data["ProposedNetworkFunctionGroupChange"]
        )

    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def LastModificationErrors(self):  # pragma: no cover
        return AttachmentError.make_many(self.boto3_raw_data["LastModificationErrors"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLinkResponse:
    boto3_raw_data: "type_defs.CreateLinkResponseTypeDef" = dataclasses.field()

    @cached_property
    def Link(self):  # pragma: no cover
        return Link.make_one(self.boto3_raw_data["Link"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLinkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLinkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLinkResponse:
    boto3_raw_data: "type_defs.DeleteLinkResponseTypeDef" = dataclasses.field()

    @cached_property
    def Link(self):  # pragma: no cover
        return Link.make_one(self.boto3_raw_data["Link"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLinkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLinkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLinksResponse:
    boto3_raw_data: "type_defs.GetLinksResponseTypeDef" = dataclasses.field()

    @cached_property
    def Links(self):  # pragma: no cover
        return Link.make_many(self.boto3_raw_data["Links"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLinksResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLinksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLinkResponse:
    boto3_raw_data: "type_defs.UpdateLinkResponseTypeDef" = dataclasses.field()

    @cached_property
    def Link(self):  # pragma: no cover
        return Link.make_one(self.boto3_raw_data["Link"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLinkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLinkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectPeer:
    boto3_raw_data: "type_defs.ConnectPeerTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    ConnectAttachmentId = field("ConnectAttachmentId")
    ConnectPeerId = field("ConnectPeerId")
    EdgeLocation = field("EdgeLocation")
    State = field("State")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return ConnectPeerConfiguration.make_one(self.boto3_raw_data["Configuration"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SubnetArn = field("SubnetArn")

    @cached_property
    def LastModificationErrors(self):  # pragma: no cover
        return ConnectPeerError.make_many(self.boto3_raw_data["LastModificationErrors"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectPeerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectPeerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkTelemetryResponse:
    boto3_raw_data: "type_defs.GetNetworkTelemetryResponseTypeDef" = dataclasses.field()

    @cached_property
    def NetworkTelemetry(self):  # pragma: no cover
        return NetworkTelemetry.make_many(self.boto3_raw_data["NetworkTelemetry"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNetworkTelemetryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkTelemetryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreNetworkChangeEventsResponse:
    boto3_raw_data: "type_defs.GetCoreNetworkChangeEventsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CoreNetworkChangeEvents(self):  # pragma: no cover
        return CoreNetworkChangeEvent.make_many(
            self.boto3_raw_data["CoreNetworkChangeEvents"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCoreNetworkChangeEventsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreNetworkChangeEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetwork:
    boto3_raw_data: "type_defs.CoreNetworkTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    CoreNetworkId = field("CoreNetworkId")
    CoreNetworkArn = field("CoreNetworkArn")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    State = field("State")

    @cached_property
    def Segments(self):  # pragma: no cover
        return CoreNetworkSegment.make_many(self.boto3_raw_data["Segments"])

    @cached_property
    def NetworkFunctionGroups(self):  # pragma: no cover
        return CoreNetworkNetworkFunctionGroup.make_many(
            self.boto3_raw_data["NetworkFunctionGroups"]
        )

    @cached_property
    def Edges(self):  # pragma: no cover
        return CoreNetworkEdge.make_many(self.boto3_raw_data["Edges"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoreNetworkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCoreNetworkPolicyVersionResponse:
    boto3_raw_data: "type_defs.DeleteCoreNetworkPolicyVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CoreNetworkPolicy(self):  # pragma: no cover
        return CoreNetworkPolicy.make_one(self.boto3_raw_data["CoreNetworkPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCoreNetworkPolicyVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCoreNetworkPolicyVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreNetworkPolicyResponse:
    boto3_raw_data: "type_defs.GetCoreNetworkPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CoreNetworkPolicy(self):  # pragma: no cover
        return CoreNetworkPolicy.make_one(self.boto3_raw_data["CoreNetworkPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCoreNetworkPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreNetworkPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutCoreNetworkPolicyResponse:
    boto3_raw_data: "type_defs.PutCoreNetworkPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CoreNetworkPolicy(self):  # pragma: no cover
        return CoreNetworkPolicy.make_one(self.boto3_raw_data["CoreNetworkPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutCoreNetworkPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutCoreNetworkPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreCoreNetworkPolicyVersionResponse:
    boto3_raw_data: "type_defs.RestoreCoreNetworkPolicyVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CoreNetworkPolicy(self):  # pragma: no cover
        return CoreNetworkPolicy.make_one(self.boto3_raw_data["CoreNetworkPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreCoreNetworkPolicyVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreCoreNetworkPolicyVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkRoutesRequest:
    boto3_raw_data: "type_defs.GetNetworkRoutesRequestTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")

    @cached_property
    def RouteTableIdentifier(self):  # pragma: no cover
        return RouteTableIdentifier.make_one(
            self.boto3_raw_data["RouteTableIdentifier"]
        )

    ExactCidrMatches = field("ExactCidrMatches")
    LongestPrefixMatches = field("LongestPrefixMatches")
    SubnetOfMatches = field("SubnetOfMatches")
    SupernetOfMatches = field("SupernetOfMatches")
    PrefixListIds = field("PrefixListIds")
    States = field("States")
    Types = field("Types")
    DestinationFilters = field("DestinationFilters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNetworkRoutesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkRoutesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeviceResponse:
    boto3_raw_data: "type_defs.CreateDeviceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Device(self):  # pragma: no cover
        return Device.make_one(self.boto3_raw_data["Device"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeviceResponse:
    boto3_raw_data: "type_defs.DeleteDeviceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Device(self):  # pragma: no cover
        return Device.make_one(self.boto3_raw_data["Device"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDevicesResponse:
    boto3_raw_data: "type_defs.GetDevicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Devices(self):  # pragma: no cover
        return Device.make_many(self.boto3_raw_data["Devices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDevicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeviceResponse:
    boto3_raw_data: "type_defs.UpdateDeviceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Device(self):  # pragma: no cover
        return Device.make_one(self.boto3_raw_data["Device"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSiteResponse:
    boto3_raw_data: "type_defs.CreateSiteResponseTypeDef" = dataclasses.field()

    @cached_property
    def Site(self):  # pragma: no cover
        return Site.make_one(self.boto3_raw_data["Site"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSiteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSiteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSiteResponse:
    boto3_raw_data: "type_defs.DeleteSiteResponseTypeDef" = dataclasses.field()

    @cached_property
    def Site(self):  # pragma: no cover
        return Site.make_one(self.boto3_raw_data["Site"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSiteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSiteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSitesResponse:
    boto3_raw_data: "type_defs.GetSitesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Sites(self):  # pragma: no cover
        return Site.make_many(self.boto3_raw_data["Sites"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSitesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSitesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSiteResponse:
    boto3_raw_data: "type_defs.UpdateSiteResponseTypeDef" = dataclasses.field()

    @cached_property
    def Site(self):  # pragma: no cover
        return Site.make_one(self.boto3_raw_data["Site"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSiteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSiteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceInsertionAction:
    boto3_raw_data: "type_defs.ServiceInsertionActionTypeDef" = dataclasses.field()

    Action = field("Action")
    Mode = field("Mode")

    @cached_property
    def WhenSentTo(self):  # pragma: no cover
        return WhenSentTo.make_one(self.boto3_raw_data["WhenSentTo"])

    @cached_property
    def Via(self):  # pragma: no cover
        return Via.make_one(self.boto3_raw_data["Via"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceInsertionActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceInsertionActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteAnalysisPath:
    boto3_raw_data: "type_defs.RouteAnalysisPathTypeDef" = dataclasses.field()

    @cached_property
    def CompletionStatus(self):  # pragma: no cover
        return RouteAnalysisCompletion.make_one(self.boto3_raw_data["CompletionStatus"])

    @cached_property
    def Path(self):  # pragma: no cover
        return PathComponent.make_many(self.boto3_raw_data["Path"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteAnalysisPathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteAnalysisPathTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkRoutesResponse:
    boto3_raw_data: "type_defs.GetNetworkRoutesResponseTypeDef" = dataclasses.field()

    RouteTableArn = field("RouteTableArn")

    @cached_property
    def CoreNetworkSegmentEdge(self):  # pragma: no cover
        return CoreNetworkSegmentEdgeIdentifier.make_one(
            self.boto3_raw_data["CoreNetworkSegmentEdge"]
        )

    RouteTableType = field("RouteTableType")
    RouteTableTimestamp = field("RouteTableTimestamp")

    @cached_property
    def NetworkRoutes(self):  # pragma: no cover
        return NetworkRoute.make_many(self.boto3_raw_data["NetworkRoutes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNetworkRoutesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkRoutesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Peering:
    boto3_raw_data: "type_defs.PeeringTypeDef" = dataclasses.field()

    CoreNetworkId = field("CoreNetworkId")
    CoreNetworkArn = field("CoreNetworkArn")
    PeeringId = field("PeeringId")
    OwnerAccountId = field("OwnerAccountId")
    PeeringType = field("PeeringType")
    State = field("State")
    EdgeLocation = field("EdgeLocation")
    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreatedAt = field("CreatedAt")

    @cached_property
    def LastModificationErrors(self):  # pragma: no cover
        return PeeringError.make_many(self.boto3_raw_data["LastModificationErrors"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PeeringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PeeringTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTransitGatewayResponse:
    boto3_raw_data: "type_defs.DeregisterTransitGatewayResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TransitGatewayRegistration(self):  # pragma: no cover
        return TransitGatewayRegistration.make_one(
            self.boto3_raw_data["TransitGatewayRegistration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterTransitGatewayResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTransitGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransitGatewayRegistrationsResponse:
    boto3_raw_data: "type_defs.GetTransitGatewayRegistrationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TransitGatewayRegistrations(self):  # pragma: no cover
        return TransitGatewayRegistration.make_many(
            self.boto3_raw_data["TransitGatewayRegistrations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTransitGatewayRegistrationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransitGatewayRegistrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTransitGatewayResponse:
    boto3_raw_data: "type_defs.RegisterTransitGatewayResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TransitGatewayRegistration(self):  # pragma: no cover
        return TransitGatewayRegistration.make_one(
            self.boto3_raw_data["TransitGatewayRegistration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterTransitGatewayResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTransitGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptAttachmentResponse:
    boto3_raw_data: "type_defs.AcceptAttachmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["Attachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptAttachmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectAttachment:
    boto3_raw_data: "type_defs.ConnectAttachmentTypeDef" = dataclasses.field()

    @cached_property
    def Attachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["Attachment"])

    TransportAttachmentId = field("TransportAttachmentId")

    @cached_property
    def Options(self):  # pragma: no cover
        return ConnectAttachmentOptions.make_one(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectAttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectAttachmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAttachmentResponse:
    boto3_raw_data: "type_defs.DeleteAttachmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["Attachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAttachmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectConnectGatewayAttachment:
    boto3_raw_data: "type_defs.DirectConnectGatewayAttachmentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["Attachment"])

    DirectConnectGatewayArn = field("DirectConnectGatewayArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DirectConnectGatewayAttachmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectConnectGatewayAttachmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachmentsResponse:
    boto3_raw_data: "type_defs.ListAttachmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attachments(self):  # pragma: no cover
        return Attachment.make_many(self.boto3_raw_data["Attachments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttachmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectAttachmentResponse:
    boto3_raw_data: "type_defs.RejectAttachmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["Attachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectAttachmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SiteToSiteVpnAttachment:
    boto3_raw_data: "type_defs.SiteToSiteVpnAttachmentTypeDef" = dataclasses.field()

    @cached_property
    def Attachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["Attachment"])

    VpnConnectionArn = field("VpnConnectionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SiteToSiteVpnAttachmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SiteToSiteVpnAttachmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitGatewayRouteTableAttachment:
    boto3_raw_data: "type_defs.TransitGatewayRouteTableAttachmentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["Attachment"])

    PeeringId = field("PeeringId")
    TransitGatewayRouteTableArn = field("TransitGatewayRouteTableArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TransitGatewayRouteTableAttachmentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitGatewayRouteTableAttachmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcAttachment:
    boto3_raw_data: "type_defs.VpcAttachmentTypeDef" = dataclasses.field()

    @cached_property
    def Attachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["Attachment"])

    SubnetArns = field("SubnetArns")

    @cached_property
    def Options(self):  # pragma: no cover
        return VpcOptions.make_one(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcAttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcAttachmentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectPeerResponse:
    boto3_raw_data: "type_defs.CreateConnectPeerResponseTypeDef" = dataclasses.field()

    @cached_property
    def ConnectPeer(self):  # pragma: no cover
        return ConnectPeer.make_one(self.boto3_raw_data["ConnectPeer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectPeerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectPeerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectPeerResponse:
    boto3_raw_data: "type_defs.DeleteConnectPeerResponseTypeDef" = dataclasses.field()

    @cached_property
    def ConnectPeer(self):  # pragma: no cover
        return ConnectPeer.make_one(self.boto3_raw_data["ConnectPeer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectPeerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectPeerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectPeerResponse:
    boto3_raw_data: "type_defs.GetConnectPeerResponseTypeDef" = dataclasses.field()

    @cached_property
    def ConnectPeer(self):  # pragma: no cover
        return ConnectPeer.make_one(self.boto3_raw_data["ConnectPeer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectPeerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectPeerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCoreNetworkResponse:
    boto3_raw_data: "type_defs.CreateCoreNetworkResponseTypeDef" = dataclasses.field()

    @cached_property
    def CoreNetwork(self):  # pragma: no cover
        return CoreNetwork.make_one(self.boto3_raw_data["CoreNetwork"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCoreNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCoreNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCoreNetworkResponse:
    boto3_raw_data: "type_defs.DeleteCoreNetworkResponseTypeDef" = dataclasses.field()

    @cached_property
    def CoreNetwork(self):  # pragma: no cover
        return CoreNetwork.make_one(self.boto3_raw_data["CoreNetwork"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCoreNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCoreNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreNetworkResponse:
    boto3_raw_data: "type_defs.GetCoreNetworkResponseTypeDef" = dataclasses.field()

    @cached_property
    def CoreNetwork(self):  # pragma: no cover
        return CoreNetwork.make_one(self.boto3_raw_data["CoreNetwork"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCoreNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCoreNetworkResponse:
    boto3_raw_data: "type_defs.UpdateCoreNetworkResponseTypeDef" = dataclasses.field()

    @cached_property
    def CoreNetwork(self):  # pragma: no cover
        return CoreNetwork.make_one(self.boto3_raw_data["CoreNetwork"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCoreNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCoreNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkChangeValues:
    boto3_raw_data: "type_defs.CoreNetworkChangeValuesTypeDef" = dataclasses.field()

    SegmentName = field("SegmentName")
    NetworkFunctionGroupName = field("NetworkFunctionGroupName")
    EdgeLocations = field("EdgeLocations")
    Asn = field("Asn")
    Cidr = field("Cidr")
    DestinationIdentifier = field("DestinationIdentifier")
    InsideCidrBlocks = field("InsideCidrBlocks")
    SharedSegments = field("SharedSegments")

    @cached_property
    def ServiceInsertionActions(self):  # pragma: no cover
        return ServiceInsertionAction.make_many(
            self.boto3_raw_data["ServiceInsertionActions"]
        )

    VpnEcmpSupport = field("VpnEcmpSupport")
    DnsSupport = field("DnsSupport")
    SecurityGroupReferencingSupport = field("SecurityGroupReferencingSupport")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkChangeValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkChangeValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteAnalysis:
    boto3_raw_data: "type_defs.RouteAnalysisTypeDef" = dataclasses.field()

    GlobalNetworkId = field("GlobalNetworkId")
    OwnerAccountId = field("OwnerAccountId")
    RouteAnalysisId = field("RouteAnalysisId")
    StartTimestamp = field("StartTimestamp")
    Status = field("Status")

    @cached_property
    def Source(self):  # pragma: no cover
        return RouteAnalysisEndpointOptions.make_one(self.boto3_raw_data["Source"])

    @cached_property
    def Destination(self):  # pragma: no cover
        return RouteAnalysisEndpointOptions.make_one(self.boto3_raw_data["Destination"])

    IncludeReturnPath = field("IncludeReturnPath")
    UseMiddleboxes = field("UseMiddleboxes")

    @cached_property
    def ForwardPath(self):  # pragma: no cover
        return RouteAnalysisPath.make_one(self.boto3_raw_data["ForwardPath"])

    @cached_property
    def ReturnPath(self):  # pragma: no cover
        return RouteAnalysisPath.make_one(self.boto3_raw_data["ReturnPath"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteAnalysisTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteAnalysisTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePeeringResponse:
    boto3_raw_data: "type_defs.DeletePeeringResponseTypeDef" = dataclasses.field()

    @cached_property
    def Peering(self):  # pragma: no cover
        return Peering.make_one(self.boto3_raw_data["Peering"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePeeringResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePeeringResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPeeringsResponse:
    boto3_raw_data: "type_defs.ListPeeringsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Peerings(self):  # pragma: no cover
        return Peering.make_many(self.boto3_raw_data["Peerings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPeeringsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPeeringsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitGatewayPeering:
    boto3_raw_data: "type_defs.TransitGatewayPeeringTypeDef" = dataclasses.field()

    @cached_property
    def Peering(self):  # pragma: no cover
        return Peering.make_one(self.boto3_raw_data["Peering"])

    TransitGatewayArn = field("TransitGatewayArn")
    TransitGatewayPeeringAttachmentId = field("TransitGatewayPeeringAttachmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransitGatewayPeeringTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitGatewayPeeringTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectAttachmentResponse:
    boto3_raw_data: "type_defs.CreateConnectAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConnectAttachment(self):  # pragma: no cover
        return ConnectAttachment.make_one(self.boto3_raw_data["ConnectAttachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConnectAttachmentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectAttachmentResponse:
    boto3_raw_data: "type_defs.GetConnectAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConnectAttachment(self):  # pragma: no cover
        return ConnectAttachment.make_one(self.boto3_raw_data["ConnectAttachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectAttachmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectConnectGatewayAttachmentResponse:
    boto3_raw_data: "type_defs.CreateDirectConnectGatewayAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DirectConnectGatewayAttachment(self):  # pragma: no cover
        return DirectConnectGatewayAttachment.make_one(
            self.boto3_raw_data["DirectConnectGatewayAttachment"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDirectConnectGatewayAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectConnectGatewayAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDirectConnectGatewayAttachmentResponse:
    boto3_raw_data: "type_defs.GetDirectConnectGatewayAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DirectConnectGatewayAttachment(self):  # pragma: no cover
        return DirectConnectGatewayAttachment.make_one(
            self.boto3_raw_data["DirectConnectGatewayAttachment"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDirectConnectGatewayAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDirectConnectGatewayAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectConnectGatewayAttachmentResponse:
    boto3_raw_data: "type_defs.UpdateDirectConnectGatewayAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DirectConnectGatewayAttachment(self):  # pragma: no cover
        return DirectConnectGatewayAttachment.make_one(
            self.boto3_raw_data["DirectConnectGatewayAttachment"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDirectConnectGatewayAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectConnectGatewayAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSiteToSiteVpnAttachmentResponse:
    boto3_raw_data: "type_defs.CreateSiteToSiteVpnAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SiteToSiteVpnAttachment(self):  # pragma: no cover
        return SiteToSiteVpnAttachment.make_one(
            self.boto3_raw_data["SiteToSiteVpnAttachment"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSiteToSiteVpnAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSiteToSiteVpnAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSiteToSiteVpnAttachmentResponse:
    boto3_raw_data: "type_defs.GetSiteToSiteVpnAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SiteToSiteVpnAttachment(self):  # pragma: no cover
        return SiteToSiteVpnAttachment.make_one(
            self.boto3_raw_data["SiteToSiteVpnAttachment"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSiteToSiteVpnAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSiteToSiteVpnAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTransitGatewayRouteTableAttachmentResponse:
    boto3_raw_data: (
        "type_defs.CreateTransitGatewayRouteTableAttachmentResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def TransitGatewayRouteTableAttachment(self):  # pragma: no cover
        return TransitGatewayRouteTableAttachment.make_one(
            self.boto3_raw_data["TransitGatewayRouteTableAttachment"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTransitGatewayRouteTableAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CreateTransitGatewayRouteTableAttachmentResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransitGatewayRouteTableAttachmentResponse:
    boto3_raw_data: "type_defs.GetTransitGatewayRouteTableAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TransitGatewayRouteTableAttachment(self):  # pragma: no cover
        return TransitGatewayRouteTableAttachment.make_one(
            self.boto3_raw_data["TransitGatewayRouteTableAttachment"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTransitGatewayRouteTableAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransitGatewayRouteTableAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcAttachmentResponse:
    boto3_raw_data: "type_defs.CreateVpcAttachmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcAttachment(self):  # pragma: no cover
        return VpcAttachment.make_one(self.boto3_raw_data["VpcAttachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcAttachmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcAttachmentResponse:
    boto3_raw_data: "type_defs.GetVpcAttachmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcAttachment(self):  # pragma: no cover
        return VpcAttachment.make_one(self.boto3_raw_data["VpcAttachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVpcAttachmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcAttachmentResponse:
    boto3_raw_data: "type_defs.UpdateVpcAttachmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcAttachment(self):  # pragma: no cover
        return VpcAttachment.make_one(self.boto3_raw_data["VpcAttachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcAttachmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreNetworkChange:
    boto3_raw_data: "type_defs.CoreNetworkChangeTypeDef" = dataclasses.field()

    Type = field("Type")
    Action = field("Action")
    Identifier = field("Identifier")

    @cached_property
    def PreviousValues(self):  # pragma: no cover
        return CoreNetworkChangeValues.make_one(self.boto3_raw_data["PreviousValues"])

    @cached_property
    def NewValues(self):  # pragma: no cover
        return CoreNetworkChangeValues.make_one(self.boto3_raw_data["NewValues"])

    IdentifierPath = field("IdentifierPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoreNetworkChangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreNetworkChangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRouteAnalysisResponse:
    boto3_raw_data: "type_defs.GetRouteAnalysisResponseTypeDef" = dataclasses.field()

    @cached_property
    def RouteAnalysis(self):  # pragma: no cover
        return RouteAnalysis.make_one(self.boto3_raw_data["RouteAnalysis"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRouteAnalysisResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRouteAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRouteAnalysisResponse:
    boto3_raw_data: "type_defs.StartRouteAnalysisResponseTypeDef" = dataclasses.field()

    @cached_property
    def RouteAnalysis(self):  # pragma: no cover
        return RouteAnalysis.make_one(self.boto3_raw_data["RouteAnalysis"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRouteAnalysisResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRouteAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTransitGatewayPeeringResponse:
    boto3_raw_data: "type_defs.CreateTransitGatewayPeeringResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TransitGatewayPeering(self):  # pragma: no cover
        return TransitGatewayPeering.make_one(
            self.boto3_raw_data["TransitGatewayPeering"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTransitGatewayPeeringResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTransitGatewayPeeringResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransitGatewayPeeringResponse:
    boto3_raw_data: "type_defs.GetTransitGatewayPeeringResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TransitGatewayPeering(self):  # pragma: no cover
        return TransitGatewayPeering.make_one(
            self.boto3_raw_data["TransitGatewayPeering"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTransitGatewayPeeringResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransitGatewayPeeringResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreNetworkChangeSetResponse:
    boto3_raw_data: "type_defs.GetCoreNetworkChangeSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CoreNetworkChanges(self):  # pragma: no cover
        return CoreNetworkChange.make_many(self.boto3_raw_data["CoreNetworkChanges"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCoreNetworkChangeSetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreNetworkChangeSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
