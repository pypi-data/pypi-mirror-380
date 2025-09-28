# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediaconnect import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class VpcInterfaceAttachment:
    boto3_raw_data: "type_defs.VpcInterfaceAttachmentTypeDef" = dataclasses.field()

    VpcInterfaceName = field("VpcInterfaceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcInterfaceAttachmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcInterfaceAttachmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddBridgeNetworkOutputRequest:
    boto3_raw_data: "type_defs.AddBridgeNetworkOutputRequestTypeDef" = (
        dataclasses.field()
    )

    IpAddress = field("IpAddress")
    Name = field("Name")
    NetworkName = field("NetworkName")
    Port = field("Port")
    Protocol = field("Protocol")
    Ttl = field("Ttl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddBridgeNetworkOutputRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddBridgeNetworkOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastSourceSettings:
    boto3_raw_data: "type_defs.MulticastSourceSettingsTypeDef" = dataclasses.field()

    MulticastSourceIp = field("MulticastSourceIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MulticastSourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MulticastSourceSettingsTypeDef"]
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
class AddEgressGatewayBridgeRequest:
    boto3_raw_data: "type_defs.AddEgressGatewayBridgeRequestTypeDef" = (
        dataclasses.field()
    )

    MaxBitrate = field("MaxBitrate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddEgressGatewayBridgeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddEgressGatewayBridgeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcInterfaceRequest:
    boto3_raw_data: "type_defs.VpcInterfaceRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RoleArn = field("RoleArn")
    SecurityGroupIds = field("SecurityGroupIds")
    SubnetId = field("SubnetId")
    NetworkInterfaceType = field("NetworkInterfaceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcInterfaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcInterface:
    boto3_raw_data: "type_defs.VpcInterfaceTypeDef" = dataclasses.field()

    Name = field("Name")
    NetworkInterfaceIds = field("NetworkInterfaceIds")
    NetworkInterfaceType = field("NetworkInterfaceType")
    RoleArn = field("RoleArn")
    SecurityGroupIds = field("SecurityGroupIds")
    SubnetId = field("SubnetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcInterfaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddIngressGatewayBridgeRequest:
    boto3_raw_data: "type_defs.AddIngressGatewayBridgeRequestTypeDef" = (
        dataclasses.field()
    )

    MaxBitrate = field("MaxBitrate")
    MaxOutputs = field("MaxOutputs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddIngressGatewayBridgeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddIngressGatewayBridgeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddMaintenance:
    boto3_raw_data: "type_defs.AddMaintenanceTypeDef" = dataclasses.field()

    MaintenanceDay = field("MaintenanceDay")
    MaintenanceStartHour = field("MaintenanceStartHour")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddMaintenanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddMaintenanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Encryption:
    boto3_raw_data: "type_defs.EncryptionTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    Algorithm = field("Algorithm")
    ConstantInitializationVector = field("ConstantInitializationVector")
    DeviceId = field("DeviceId")
    KeyType = field("KeyType")
    Region = field("Region")
    ResourceId = field("ResourceId")
    SecretArn = field("SecretArn")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncryptionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SilentAudio:
    boto3_raw_data: "type_defs.SilentAudioTypeDef" = dataclasses.field()

    State = field("State")
    ThresholdSeconds = field("ThresholdSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SilentAudioTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SilentAudioTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlackFrames:
    boto3_raw_data: "type_defs.BlackFramesTypeDef" = dataclasses.field()

    State = field("State")
    ThresholdSeconds = field("ThresholdSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlackFramesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlackFramesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BridgeFlowOutput:
    boto3_raw_data: "type_defs.BridgeFlowOutputTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    FlowSourceArn = field("FlowSourceArn")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BridgeFlowOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BridgeFlowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BridgeNetworkOutput:
    boto3_raw_data: "type_defs.BridgeNetworkOutputTypeDef" = dataclasses.field()

    IpAddress = field("IpAddress")
    Name = field("Name")
    NetworkName = field("NetworkName")
    Port = field("Port")
    Protocol = field("Protocol")
    Ttl = field("Ttl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BridgeNetworkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BridgeNetworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EgressGatewayBridge:
    boto3_raw_data: "type_defs.EgressGatewayBridgeTypeDef" = dataclasses.field()

    MaxBitrate = field("MaxBitrate")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EgressGatewayBridgeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EgressGatewayBridgeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressGatewayBridge:
    boto3_raw_data: "type_defs.IngressGatewayBridgeTypeDef" = dataclasses.field()

    MaxBitrate = field("MaxBitrate")
    MaxOutputs = field("MaxOutputs")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressGatewayBridgeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressGatewayBridgeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageDetail:
    boto3_raw_data: "type_defs.MessageDetailTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayNetwork:
    boto3_raw_data: "type_defs.GatewayNetworkTypeDef" = dataclasses.field()

    CidrBlock = field("CidrBlock")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayNetworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GatewayNetworkTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBridgeRequest:
    boto3_raw_data: "type_defs.DeleteBridgeRequestTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBridgeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBridgeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFlowRequest:
    boto3_raw_data: "type_defs.DeleteFlowRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayRequest:
    boto3_raw_data: "type_defs.DeleteGatewayRequestTypeDef" = dataclasses.field()

    GatewayArn = field("GatewayArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterGatewayInstanceRequest:
    boto3_raw_data: "type_defs.DeregisterGatewayInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    GatewayInstanceArn = field("GatewayInstanceArn")
    Force = field("Force")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterGatewayInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterGatewayInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBridgeRequest:
    boto3_raw_data: "type_defs.DescribeBridgeRequestTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBridgeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBridgeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowRequest:
    boto3_raw_data: "type_defs.DescribeFlowRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Messages:
    boto3_raw_data: "type_defs.MessagesTypeDef" = dataclasses.field()

    Errors = field("Errors")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessagesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessagesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowSourceMetadataRequest:
    boto3_raw_data: "type_defs.DescribeFlowSourceMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFlowSourceMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowSourceMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowSourceThumbnailRequest:
    boto3_raw_data: "type_defs.DescribeFlowSourceThumbnailRequestTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFlowSourceThumbnailRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowSourceThumbnailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayInstanceRequest:
    boto3_raw_data: "type_defs.DescribeGatewayInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    GatewayInstanceArn = field("GatewayInstanceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGatewayInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayRequest:
    boto3_raw_data: "type_defs.DescribeGatewayRequestTypeDef" = dataclasses.field()

    GatewayArn = field("GatewayArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOfferingRequest:
    boto3_raw_data: "type_defs.DescribeOfferingRequestTypeDef" = dataclasses.field()

    OfferingArn = field("OfferingArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOfferingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOfferingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservationRequest:
    boto3_raw_data: "type_defs.DescribeReservationRequestTypeDef" = dataclasses.field()

    ReservationArn = field("ReservationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReservationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterfaceRequest:
    boto3_raw_data: "type_defs.InterfaceRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InterfaceRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Interface:
    boto3_raw_data: "type_defs.InterfaceTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InterfaceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncodingParametersRequest:
    boto3_raw_data: "type_defs.EncodingParametersRequestTypeDef" = dataclasses.field()

    CompressionFactor = field("CompressionFactor")
    EncoderProfile = field("EncoderProfile")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncodingParametersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncodingParametersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncodingParameters:
    boto3_raw_data: "type_defs.EncodingParametersTypeDef" = dataclasses.field()

    CompressionFactor = field("CompressionFactor")
    EncoderProfile = field("EncoderProfile")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncodingParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncodingParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourcePriority:
    boto3_raw_data: "type_defs.SourcePriorityTypeDef" = dataclasses.field()

    PrimarySource = field("PrimarySource")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourcePriorityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourcePriorityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Maintenance:
    boto3_raw_data: "type_defs.MaintenanceTypeDef" = dataclasses.field()

    MaintenanceDay = field("MaintenanceDay")
    MaintenanceDeadline = field("MaintenanceDeadline")
    MaintenanceScheduledDate = field("MaintenanceScheduledDate")
    MaintenanceStartHour = field("MaintenanceStartHour")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MaintenanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MaintenanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FmtpRequest:
    boto3_raw_data: "type_defs.FmtpRequestTypeDef" = dataclasses.field()

    ChannelOrder = field("ChannelOrder")
    Colorimetry = field("Colorimetry")
    ExactFramerate = field("ExactFramerate")
    Par = field("Par")
    Range = field("Range")
    ScanMode = field("ScanMode")
    Tcs = field("Tcs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FmtpRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FmtpRequestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Fmtp:
    boto3_raw_data: "type_defs.FmtpTypeDef" = dataclasses.field()

    ChannelOrder = field("ChannelOrder")
    Colorimetry = field("Colorimetry")
    ExactFramerate = field("ExactFramerate")
    Par = field("Par")
    Range = field("Range")
    ScanMode = field("ScanMode")
    Tcs = field("Tcs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FmtpTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FmtpTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameResolution:
    boto3_raw_data: "type_defs.FrameResolutionTypeDef" = dataclasses.field()

    FrameHeight = field("FrameHeight")
    FrameWidth = field("FrameWidth")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrameResolutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FrameResolutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrozenFrames:
    boto3_raw_data: "type_defs.FrozenFramesTypeDef" = dataclasses.field()

    State = field("State")
    ThresholdSeconds = field("ThresholdSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrozenFramesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FrozenFramesTypeDef"]],
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
class ListBridgesRequest:
    boto3_raw_data: "type_defs.ListBridgesRequestTypeDef" = dataclasses.field()

    FilterArn = field("FilterArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBridgesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBridgesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedBridge:
    boto3_raw_data: "type_defs.ListedBridgeTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")
    BridgeState = field("BridgeState")
    BridgeType = field("BridgeType")
    Name = field("Name")
    PlacementArn = field("PlacementArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedBridgeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedBridgeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitlementsRequest:
    boto3_raw_data: "type_defs.ListEntitlementsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntitlementsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitlementsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedEntitlement:
    boto3_raw_data: "type_defs.ListedEntitlementTypeDef" = dataclasses.field()

    EntitlementArn = field("EntitlementArn")
    EntitlementName = field("EntitlementName")
    DataTransferSubscriberFeePercent = field("DataTransferSubscriberFeePercent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedEntitlementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListedEntitlementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowsRequest:
    boto3_raw_data: "type_defs.ListFlowsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFlowsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewayInstancesRequest:
    boto3_raw_data: "type_defs.ListGatewayInstancesRequestTypeDef" = dataclasses.field()

    FilterArn = field("FilterArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewayInstancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewayInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedGatewayInstance:
    boto3_raw_data: "type_defs.ListedGatewayInstanceTypeDef" = dataclasses.field()

    GatewayArn = field("GatewayArn")
    GatewayInstanceArn = field("GatewayInstanceArn")
    InstanceId = field("InstanceId")
    InstanceState = field("InstanceState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListedGatewayInstanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListedGatewayInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysRequest:
    boto3_raw_data: "type_defs.ListGatewaysRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedGateway:
    boto3_raw_data: "type_defs.ListedGatewayTypeDef" = dataclasses.field()

    GatewayArn = field("GatewayArn")
    GatewayState = field("GatewayState")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedGatewayTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedGatewayTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOfferingsRequest:
    boto3_raw_data: "type_defs.ListOfferingsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOfferingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOfferingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationsRequest:
    boto3_raw_data: "type_defs.ListReservationsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReservationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationsRequestTypeDef"]
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
class NdiDiscoveryServerConfig:
    boto3_raw_data: "type_defs.NdiDiscoveryServerConfigTypeDef" = dataclasses.field()

    DiscoveryServerAddress = field("DiscoveryServerAddress")
    VpcInterfaceAdapter = field("VpcInterfaceAdapter")
    DiscoveryServerPort = field("DiscoveryServerPort")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NdiDiscoveryServerConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NdiDiscoveryServerConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSpecification:
    boto3_raw_data: "type_defs.ResourceSpecificationTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ReservedBitrate = field("ReservedBitrate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Transport:
    boto3_raw_data: "type_defs.TransportTypeDef" = dataclasses.field()

    Protocol = field("Protocol")
    CidrAllowList = field("CidrAllowList")
    MaxBitrate = field("MaxBitrate")
    MaxLatency = field("MaxLatency")
    MaxSyncBuffer = field("MaxSyncBuffer")
    MinLatency = field("MinLatency")
    RemoteId = field("RemoteId")
    SenderControlPort = field("SenderControlPort")
    SenderIpAddress = field("SenderIpAddress")
    SmoothingLatency = field("SmoothingLatency")
    SourceListenerAddress = field("SourceListenerAddress")
    SourceListenerPort = field("SourceListenerPort")
    StreamId = field("StreamId")
    NdiSpeedHqQuality = field("NdiSpeedHqQuality")
    NdiProgramName = field("NdiProgramName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransportTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseOfferingRequest:
    boto3_raw_data: "type_defs.PurchaseOfferingRequestTypeDef" = dataclasses.field()

    OfferingArn = field("OfferingArn")
    ReservationName = field("ReservationName")
    Start = field("Start")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PurchaseOfferingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseOfferingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveBridgeOutputRequest:
    boto3_raw_data: "type_defs.RemoveBridgeOutputRequestTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")
    OutputName = field("OutputName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveBridgeOutputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveBridgeOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveBridgeSourceRequest:
    boto3_raw_data: "type_defs.RemoveBridgeSourceRequestTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")
    SourceName = field("SourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveBridgeSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveBridgeSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFlowMediaStreamRequest:
    boto3_raw_data: "type_defs.RemoveFlowMediaStreamRequestTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")
    MediaStreamName = field("MediaStreamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveFlowMediaStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFlowMediaStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFlowOutputRequest:
    boto3_raw_data: "type_defs.RemoveFlowOutputRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    OutputArn = field("OutputArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveFlowOutputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFlowOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFlowSourceRequest:
    boto3_raw_data: "type_defs.RemoveFlowSourceRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    SourceArn = field("SourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveFlowSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFlowSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFlowVpcInterfaceRequest:
    boto3_raw_data: "type_defs.RemoveFlowVpcInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")
    VpcInterfaceName = field("VpcInterfaceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveFlowVpcInterfaceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFlowVpcInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeFlowEntitlementRequest:
    boto3_raw_data: "type_defs.RevokeFlowEntitlementRequestTypeDef" = (
        dataclasses.field()
    )

    EntitlementArn = field("EntitlementArn")
    FlowArn = field("FlowArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeFlowEntitlementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeFlowEntitlementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlowRequest:
    boto3_raw_data: "type_defs.StartFlowRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopFlowRequest:
    boto3_raw_data: "type_defs.StopFlowRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopFlowRequestTypeDef"]],
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
    Tags = field("Tags")

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
class UpdateBridgeNetworkOutputRequest:
    boto3_raw_data: "type_defs.UpdateBridgeNetworkOutputRequestTypeDef" = (
        dataclasses.field()
    )

    IpAddress = field("IpAddress")
    NetworkName = field("NetworkName")
    Port = field("Port")
    Protocol = field("Protocol")
    Ttl = field("Ttl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateBridgeNetworkOutputRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeNetworkOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEgressGatewayBridgeRequest:
    boto3_raw_data: "type_defs.UpdateEgressGatewayBridgeRequestTypeDef" = (
        dataclasses.field()
    )

    MaxBitrate = field("MaxBitrate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEgressGatewayBridgeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEgressGatewayBridgeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIngressGatewayBridgeRequest:
    boto3_raw_data: "type_defs.UpdateIngressGatewayBridgeRequestTypeDef" = (
        dataclasses.field()
    )

    MaxBitrate = field("MaxBitrate")
    MaxOutputs = field("MaxOutputs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateIngressGatewayBridgeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIngressGatewayBridgeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBridgeStateRequest:
    boto3_raw_data: "type_defs.UpdateBridgeStateRequestTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")
    DesiredState = field("DesiredState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBridgeStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEncryption:
    boto3_raw_data: "type_defs.UpdateEncryptionTypeDef" = dataclasses.field()

    Algorithm = field("Algorithm")
    ConstantInitializationVector = field("ConstantInitializationVector")
    DeviceId = field("DeviceId")
    KeyType = field("KeyType")
    Region = field("Region")
    ResourceId = field("ResourceId")
    RoleArn = field("RoleArn")
    SecretArn = field("SecretArn")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateEncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEncryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMaintenance:
    boto3_raw_data: "type_defs.UpdateMaintenanceTypeDef" = dataclasses.field()

    MaintenanceDay = field("MaintenanceDay")
    MaintenanceScheduledDate = field("MaintenanceScheduledDate")
    MaintenanceStartHour = field("MaintenanceStartHour")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateMaintenanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMaintenanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayInstanceRequest:
    boto3_raw_data: "type_defs.UpdateGatewayInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    GatewayInstanceArn = field("GatewayInstanceArn")
    BridgePlacement = field("BridgePlacement")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGatewayInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddBridgeFlowSourceRequest:
    boto3_raw_data: "type_defs.AddBridgeFlowSourceRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    Name = field("Name")

    @cached_property
    def FlowVpcInterfaceAttachment(self):  # pragma: no cover
        return VpcInterfaceAttachment.make_one(
            self.boto3_raw_data["FlowVpcInterfaceAttachment"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddBridgeFlowSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddBridgeFlowSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BridgeFlowSource:
    boto3_raw_data: "type_defs.BridgeFlowSourceTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    Name = field("Name")

    @cached_property
    def FlowVpcInterfaceAttachment(self):  # pragma: no cover
        return VpcInterfaceAttachment.make_one(
            self.boto3_raw_data["FlowVpcInterfaceAttachment"]
        )

    OutputArn = field("OutputArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BridgeFlowSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BridgeFlowSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayBridgeSource:
    boto3_raw_data: "type_defs.GatewayBridgeSourceTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @cached_property
    def VpcInterfaceAttachment(self):  # pragma: no cover
        return VpcInterfaceAttachment.make_one(
            self.boto3_raw_data["VpcInterfaceAttachment"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GatewayBridgeSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayBridgeSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetGatewayBridgeSourceRequest:
    boto3_raw_data: "type_defs.SetGatewayBridgeSourceRequestTypeDef" = (
        dataclasses.field()
    )

    BridgeArn = field("BridgeArn")

    @cached_property
    def VpcInterfaceAttachment(self):  # pragma: no cover
        return VpcInterfaceAttachment.make_one(
            self.boto3_raw_data["VpcInterfaceAttachment"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetGatewayBridgeSourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetGatewayBridgeSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBridgeFlowSourceRequest:
    boto3_raw_data: "type_defs.UpdateBridgeFlowSourceRequestTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")

    @cached_property
    def FlowVpcInterfaceAttachment(self):  # pragma: no cover
        return VpcInterfaceAttachment.make_one(
            self.boto3_raw_data["FlowVpcInterfaceAttachment"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateBridgeFlowSourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeFlowSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayBridgeSourceRequest:
    boto3_raw_data: "type_defs.UpdateGatewayBridgeSourceRequestTypeDef" = (
        dataclasses.field()
    )

    BridgeArn = field("BridgeArn")

    @cached_property
    def VpcInterfaceAttachment(self):  # pragma: no cover
        return VpcInterfaceAttachment.make_one(
            self.boto3_raw_data["VpcInterfaceAttachment"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGatewayBridgeSourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayBridgeSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddBridgeOutputRequest:
    boto3_raw_data: "type_defs.AddBridgeOutputRequestTypeDef" = dataclasses.field()

    @cached_property
    def NetworkOutput(self):  # pragma: no cover
        return AddBridgeNetworkOutputRequest.make_one(
            self.boto3_raw_data["NetworkOutput"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddBridgeOutputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddBridgeOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddBridgeNetworkSourceRequest:
    boto3_raw_data: "type_defs.AddBridgeNetworkSourceRequestTypeDef" = (
        dataclasses.field()
    )

    MulticastIp = field("MulticastIp")
    Name = field("Name")
    NetworkName = field("NetworkName")
    Port = field("Port")
    Protocol = field("Protocol")

    @cached_property
    def MulticastSourceSettings(self):  # pragma: no cover
        return MulticastSourceSettings.make_one(
            self.boto3_raw_data["MulticastSourceSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddBridgeNetworkSourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddBridgeNetworkSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BridgeNetworkSource:
    boto3_raw_data: "type_defs.BridgeNetworkSourceTypeDef" = dataclasses.field()

    MulticastIp = field("MulticastIp")
    Name = field("Name")
    NetworkName = field("NetworkName")
    Port = field("Port")
    Protocol = field("Protocol")

    @cached_property
    def MulticastSourceSettings(self):  # pragma: no cover
        return MulticastSourceSettings.make_one(
            self.boto3_raw_data["MulticastSourceSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BridgeNetworkSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BridgeNetworkSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBridgeNetworkSourceRequest:
    boto3_raw_data: "type_defs.UpdateBridgeNetworkSourceRequestTypeDef" = (
        dataclasses.field()
    )

    MulticastIp = field("MulticastIp")

    @cached_property
    def MulticastSourceSettings(self):  # pragma: no cover
        return MulticastSourceSettings.make_one(
            self.boto3_raw_data["MulticastSourceSettings"]
        )

    NetworkName = field("NetworkName")
    Port = field("Port")
    Protocol = field("Protocol")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateBridgeNetworkSourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeNetworkSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBridgeResponse:
    boto3_raw_data: "type_defs.DeleteBridgeResponseTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBridgeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBridgeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFlowResponse:
    boto3_raw_data: "type_defs.DeleteFlowResponseTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayResponse:
    boto3_raw_data: "type_defs.DeleteGatewayResponseTypeDef" = dataclasses.field()

    GatewayArn = field("GatewayArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterGatewayInstanceResponse:
    boto3_raw_data: "type_defs.DeregisterGatewayInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    GatewayInstanceArn = field("GatewayInstanceArn")
    InstanceState = field("InstanceState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterGatewayInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterGatewayInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    Tags = field("Tags")

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
class RemoveBridgeOutputResponse:
    boto3_raw_data: "type_defs.RemoveBridgeOutputResponseTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")
    OutputName = field("OutputName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveBridgeOutputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveBridgeOutputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveBridgeSourceResponse:
    boto3_raw_data: "type_defs.RemoveBridgeSourceResponseTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")
    SourceName = field("SourceName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveBridgeSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveBridgeSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFlowMediaStreamResponse:
    boto3_raw_data: "type_defs.RemoveFlowMediaStreamResponseTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")
    MediaStreamName = field("MediaStreamName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveFlowMediaStreamResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFlowMediaStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFlowOutputResponse:
    boto3_raw_data: "type_defs.RemoveFlowOutputResponseTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    OutputArn = field("OutputArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveFlowOutputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFlowOutputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFlowSourceResponse:
    boto3_raw_data: "type_defs.RemoveFlowSourceResponseTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    SourceArn = field("SourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveFlowSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFlowSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFlowVpcInterfaceResponse:
    boto3_raw_data: "type_defs.RemoveFlowVpcInterfaceResponseTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")
    NonDeletedNetworkInterfaceIds = field("NonDeletedNetworkInterfaceIds")
    VpcInterfaceName = field("VpcInterfaceName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveFlowVpcInterfaceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFlowVpcInterfaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeFlowEntitlementResponse:
    boto3_raw_data: "type_defs.RevokeFlowEntitlementResponseTypeDef" = (
        dataclasses.field()
    )

    EntitlementArn = field("EntitlementArn")
    FlowArn = field("FlowArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RevokeFlowEntitlementResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeFlowEntitlementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlowResponse:
    boto3_raw_data: "type_defs.StartFlowResponseTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartFlowResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopFlowResponse:
    boto3_raw_data: "type_defs.StopFlowResponseTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopFlowResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBridgeStateResponse:
    boto3_raw_data: "type_defs.UpdateBridgeStateResponseTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")
    DesiredState = field("DesiredState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBridgeStateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayInstanceResponse:
    boto3_raw_data: "type_defs.UpdateGatewayInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    BridgePlacement = field("BridgePlacement")
    GatewayInstanceArn = field("GatewayInstanceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGatewayInstanceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddFlowVpcInterfacesRequest:
    boto3_raw_data: "type_defs.AddFlowVpcInterfacesRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def VpcInterfaces(self):  # pragma: no cover
        return VpcInterfaceRequest.make_many(self.boto3_raw_data["VpcInterfaces"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddFlowVpcInterfacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddFlowVpcInterfacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddFlowVpcInterfacesResponse:
    boto3_raw_data: "type_defs.AddFlowVpcInterfacesResponseTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")

    @cached_property
    def VpcInterfaces(self):  # pragma: no cover
        return VpcInterface.make_many(self.boto3_raw_data["VpcInterfaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddFlowVpcInterfacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddFlowVpcInterfacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Entitlement:
    boto3_raw_data: "type_defs.EntitlementTypeDef" = dataclasses.field()

    EntitlementArn = field("EntitlementArn")
    Name = field("Name")
    Subscribers = field("Subscribers")
    DataTransferSubscriberFeePercent = field("DataTransferSubscriberFeePercent")
    Description = field("Description")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    EntitlementStatus = field("EntitlementStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntitlementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntitlementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantEntitlementRequest:
    boto3_raw_data: "type_defs.GrantEntitlementRequestTypeDef" = dataclasses.field()

    Subscribers = field("Subscribers")
    DataTransferSubscriberFeePercent = field("DataTransferSubscriberFeePercent")
    Description = field("Description")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    EntitlementStatus = field("EntitlementStatus")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrantEntitlementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrantEntitlementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioMonitoringSetting:
    boto3_raw_data: "type_defs.AudioMonitoringSettingTypeDef" = dataclasses.field()

    @cached_property
    def SilentAudio(self):  # pragma: no cover
        return SilentAudio.make_one(self.boto3_raw_data["SilentAudio"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioMonitoringSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioMonitoringSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BridgeOutput:
    boto3_raw_data: "type_defs.BridgeOutputTypeDef" = dataclasses.field()

    @cached_property
    def FlowOutput(self):  # pragma: no cover
        return BridgeFlowOutput.make_one(self.boto3_raw_data["FlowOutput"])

    @cached_property
    def NetworkOutput(self):  # pragma: no cover
        return BridgeNetworkOutput.make_one(self.boto3_raw_data["NetworkOutput"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BridgeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BridgeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayInstance:
    boto3_raw_data: "type_defs.GatewayInstanceTypeDef" = dataclasses.field()

    BridgePlacement = field("BridgePlacement")
    ConnectionStatus = field("ConnectionStatus")
    GatewayArn = field("GatewayArn")
    GatewayInstanceArn = field("GatewayInstanceArn")
    InstanceId = field("InstanceId")
    InstanceState = field("InstanceState")
    RunningBridgeCount = field("RunningBridgeCount")

    @cached_property
    def InstanceMessages(self):  # pragma: no cover
        return MessageDetail.make_many(self.boto3_raw_data["InstanceMessages"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GatewayInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThumbnailDetails:
    boto3_raw_data: "type_defs.ThumbnailDetailsTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def ThumbnailMessages(self):  # pragma: no cover
        return MessageDetail.make_many(self.boto3_raw_data["ThumbnailMessages"])

    Thumbnail = field("Thumbnail")
    Timecode = field("Timecode")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThumbnailDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThumbnailDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGatewayRequest:
    boto3_raw_data: "type_defs.CreateGatewayRequestTypeDef" = dataclasses.field()

    EgressCidrBlocks = field("EgressCidrBlocks")
    Name = field("Name")

    @cached_property
    def Networks(self):  # pragma: no cover
        return GatewayNetwork.make_many(self.boto3_raw_data["Networks"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Gateway:
    boto3_raw_data: "type_defs.GatewayTypeDef" = dataclasses.field()

    EgressCidrBlocks = field("EgressCidrBlocks")
    GatewayArn = field("GatewayArn")
    Name = field("Name")

    @cached_property
    def Networks(self):  # pragma: no cover
        return GatewayNetwork.make_many(self.boto3_raw_data["Networks"])

    @cached_property
    def GatewayMessages(self):  # pragma: no cover
        return MessageDetail.make_many(self.boto3_raw_data["GatewayMessages"])

    GatewayState = field("GatewayState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GatewayTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowRequestWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeFlowRequestWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFlowRequestWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowRequestWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeFlowRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFlowRequestWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowRequestWait:
    boto3_raw_data: "type_defs.DescribeFlowRequestWaitTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFlowRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationConfigurationRequest:
    boto3_raw_data: "type_defs.DestinationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    DestinationIp = field("DestinationIp")
    DestinationPort = field("DestinationPort")

    @cached_property
    def Interface(self):  # pragma: no cover
        return InterfaceRequest.make_one(self.boto3_raw_data["Interface"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DestinationConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputConfigurationRequest:
    boto3_raw_data: "type_defs.InputConfigurationRequestTypeDef" = dataclasses.field()

    InputPort = field("InputPort")

    @cached_property
    def Interface(self):  # pragma: no cover
        return InterfaceRequest.make_one(self.boto3_raw_data["Interface"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationConfiguration:
    boto3_raw_data: "type_defs.DestinationConfigurationTypeDef" = dataclasses.field()

    DestinationIp = field("DestinationIp")
    DestinationPort = field("DestinationPort")

    @cached_property
    def Interface(self):  # pragma: no cover
        return Interface.make_one(self.boto3_raw_data["Interface"])

    OutboundIp = field("OutboundIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputConfiguration:
    boto3_raw_data: "type_defs.InputConfigurationTypeDef" = dataclasses.field()

    InputIp = field("InputIp")
    InputPort = field("InputPort")

    @cached_property
    def Interface(self):  # pragma: no cover
        return Interface.make_one(self.boto3_raw_data["Interface"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverConfig:
    boto3_raw_data: "type_defs.FailoverConfigTypeDef" = dataclasses.field()

    FailoverMode = field("FailoverMode")
    RecoveryWindow = field("RecoveryWindow")

    @cached_property
    def SourcePriority(self):  # pragma: no cover
        return SourcePriority.make_one(self.boto3_raw_data["SourcePriority"])

    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailoverConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailoverConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFailoverConfig:
    boto3_raw_data: "type_defs.UpdateFailoverConfigTypeDef" = dataclasses.field()

    FailoverMode = field("FailoverMode")
    RecoveryWindow = field("RecoveryWindow")

    @cached_property
    def SourcePriority(self):  # pragma: no cover
        return SourcePriority.make_one(self.boto3_raw_data["SourcePriority"])

    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFailoverConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFailoverConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedFlow:
    boto3_raw_data: "type_defs.ListedFlowTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")
    Description = field("Description")
    FlowArn = field("FlowArn")
    Name = field("Name")
    SourceType = field("SourceType")
    Status = field("Status")

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return Maintenance.make_one(self.boto3_raw_data["Maintenance"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedFlowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedFlowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStreamAttributesRequest:
    boto3_raw_data: "type_defs.MediaStreamAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Fmtp(self):  # pragma: no cover
        return FmtpRequest.make_one(self.boto3_raw_data["Fmtp"])

    Lang = field("Lang")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaStreamAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaStreamAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStreamAttributes:
    boto3_raw_data: "type_defs.MediaStreamAttributesTypeDef" = dataclasses.field()

    @cached_property
    def Fmtp(self):  # pragma: no cover
        return Fmtp.make_one(self.boto3_raw_data["Fmtp"])

    Lang = field("Lang")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaStreamAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaStreamAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransportStream:
    boto3_raw_data: "type_defs.TransportStreamTypeDef" = dataclasses.field()

    Pid = field("Pid")
    StreamType = field("StreamType")
    Channels = field("Channels")
    Codec = field("Codec")
    FrameRate = field("FrameRate")

    @cached_property
    def FrameResolution(self):  # pragma: no cover
        return FrameResolution.make_one(self.boto3_raw_data["FrameResolution"])

    SampleRate = field("SampleRate")
    SampleSize = field("SampleSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransportStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransportStreamTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoMonitoringSetting:
    boto3_raw_data: "type_defs.VideoMonitoringSettingTypeDef" = dataclasses.field()

    @cached_property
    def BlackFrames(self):  # pragma: no cover
        return BlackFrames.make_one(self.boto3_raw_data["BlackFrames"])

    @cached_property
    def FrozenFrames(self):  # pragma: no cover
        return FrozenFrames.make_one(self.boto3_raw_data["FrozenFrames"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoMonitoringSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoMonitoringSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBridgesRequestPaginate:
    boto3_raw_data: "type_defs.ListBridgesRequestPaginateTypeDef" = dataclasses.field()

    FilterArn = field("FilterArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBridgesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBridgesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitlementsRequestPaginate:
    boto3_raw_data: "type_defs.ListEntitlementsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEntitlementsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitlementsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowsRequestPaginate:
    boto3_raw_data: "type_defs.ListFlowsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewayInstancesRequestPaginate:
    boto3_raw_data: "type_defs.ListGatewayInstancesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FilterArn = field("FilterArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGatewayInstancesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewayInstancesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysRequestPaginate:
    boto3_raw_data: "type_defs.ListGatewaysRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOfferingsRequestPaginate:
    boto3_raw_data: "type_defs.ListOfferingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOfferingsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOfferingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationsRequestPaginate:
    boto3_raw_data: "type_defs.ListReservationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReservationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBridgesResponse:
    boto3_raw_data: "type_defs.ListBridgesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Bridges(self):  # pragma: no cover
        return ListedBridge.make_many(self.boto3_raw_data["Bridges"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBridgesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBridgesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitlementsResponse:
    boto3_raw_data: "type_defs.ListEntitlementsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return ListedEntitlement.make_many(self.boto3_raw_data["Entitlements"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntitlementsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitlementsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewayInstancesResponse:
    boto3_raw_data: "type_defs.ListGatewayInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Instances(self):  # pragma: no cover
        return ListedGatewayInstance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewayInstancesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewayInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysResponse:
    boto3_raw_data: "type_defs.ListGatewaysResponseTypeDef" = dataclasses.field()

    @cached_property
    def Gateways(self):  # pragma: no cover
        return ListedGateway.make_many(self.boto3_raw_data["Gateways"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NdiConfigOutput:
    boto3_raw_data: "type_defs.NdiConfigOutputTypeDef" = dataclasses.field()

    NdiState = field("NdiState")
    MachineName = field("MachineName")

    @cached_property
    def NdiDiscoveryServers(self):  # pragma: no cover
        return NdiDiscoveryServerConfig.make_many(
            self.boto3_raw_data["NdiDiscoveryServers"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NdiConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NdiConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NdiConfig:
    boto3_raw_data: "type_defs.NdiConfigTypeDef" = dataclasses.field()

    NdiState = field("NdiState")
    MachineName = field("MachineName")

    @cached_property
    def NdiDiscoveryServers(self):  # pragma: no cover
        return NdiDiscoveryServerConfig.make_many(
            self.boto3_raw_data["NdiDiscoveryServers"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NdiConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NdiConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Offering:
    boto3_raw_data: "type_defs.OfferingTypeDef" = dataclasses.field()

    CurrencyCode = field("CurrencyCode")
    Duration = field("Duration")
    DurationUnits = field("DurationUnits")
    OfferingArn = field("OfferingArn")
    OfferingDescription = field("OfferingDescription")
    PricePerUnit = field("PricePerUnit")
    PriceUnits = field("PriceUnits")

    @cached_property
    def ResourceSpecification(self):  # pragma: no cover
        return ResourceSpecification.make_one(
            self.boto3_raw_data["ResourceSpecification"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OfferingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OfferingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Reservation:
    boto3_raw_data: "type_defs.ReservationTypeDef" = dataclasses.field()

    CurrencyCode = field("CurrencyCode")
    Duration = field("Duration")
    DurationUnits = field("DurationUnits")
    End = field("End")
    OfferingArn = field("OfferingArn")
    OfferingDescription = field("OfferingDescription")
    PricePerUnit = field("PricePerUnit")
    PriceUnits = field("PriceUnits")
    ReservationArn = field("ReservationArn")
    ReservationName = field("ReservationName")
    ReservationState = field("ReservationState")

    @cached_property
    def ResourceSpecification(self):  # pragma: no cover
        return ResourceSpecification.make_one(
            self.boto3_raw_data["ResourceSpecification"]
        )

    Start = field("Start")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReservationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReservationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBridgeOutputRequest:
    boto3_raw_data: "type_defs.UpdateBridgeOutputRequestTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")
    OutputName = field("OutputName")

    @cached_property
    def NetworkOutput(self):  # pragma: no cover
        return UpdateBridgeNetworkOutputRequest.make_one(
            self.boto3_raw_data["NetworkOutput"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBridgeOutputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowEntitlementRequest:
    boto3_raw_data: "type_defs.UpdateFlowEntitlementRequestTypeDef" = (
        dataclasses.field()
    )

    EntitlementArn = field("EntitlementArn")
    FlowArn = field("FlowArn")
    Description = field("Description")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return UpdateEncryption.make_one(self.boto3_raw_data["Encryption"])

    EntitlementStatus = field("EntitlementStatus")
    Subscribers = field("Subscribers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowEntitlementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowEntitlementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddBridgeOutputsRequest:
    boto3_raw_data: "type_defs.AddBridgeOutputsRequestTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return AddBridgeOutputRequest.make_many(self.boto3_raw_data["Outputs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddBridgeOutputsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddBridgeOutputsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddBridgeSourceRequest:
    boto3_raw_data: "type_defs.AddBridgeSourceRequestTypeDef" = dataclasses.field()

    @cached_property
    def FlowSource(self):  # pragma: no cover
        return AddBridgeFlowSourceRequest.make_one(self.boto3_raw_data["FlowSource"])

    @cached_property
    def NetworkSource(self):  # pragma: no cover
        return AddBridgeNetworkSourceRequest.make_one(
            self.boto3_raw_data["NetworkSource"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddBridgeSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddBridgeSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BridgeSource:
    boto3_raw_data: "type_defs.BridgeSourceTypeDef" = dataclasses.field()

    @cached_property
    def FlowSource(self):  # pragma: no cover
        return BridgeFlowSource.make_one(self.boto3_raw_data["FlowSource"])

    @cached_property
    def NetworkSource(self):  # pragma: no cover
        return BridgeNetworkSource.make_one(self.boto3_raw_data["NetworkSource"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BridgeSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BridgeSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBridgeSourceRequest:
    boto3_raw_data: "type_defs.UpdateBridgeSourceRequestTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")
    SourceName = field("SourceName")

    @cached_property
    def FlowSource(self):  # pragma: no cover
        return UpdateBridgeFlowSourceRequest.make_one(self.boto3_raw_data["FlowSource"])

    @cached_property
    def NetworkSource(self):  # pragma: no cover
        return UpdateBridgeNetworkSourceRequest.make_one(
            self.boto3_raw_data["NetworkSource"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBridgeSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantFlowEntitlementsResponse:
    boto3_raw_data: "type_defs.GrantFlowEntitlementsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return Entitlement.make_many(self.boto3_raw_data["Entitlements"])

    FlowArn = field("FlowArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GrantFlowEntitlementsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrantFlowEntitlementsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowEntitlementResponse:
    boto3_raw_data: "type_defs.UpdateFlowEntitlementResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Entitlement(self):  # pragma: no cover
        return Entitlement.make_one(self.boto3_raw_data["Entitlement"])

    FlowArn = field("FlowArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFlowEntitlementResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowEntitlementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantFlowEntitlementsRequest:
    boto3_raw_data: "type_defs.GrantFlowEntitlementsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return GrantEntitlementRequest.make_many(self.boto3_raw_data["Entitlements"])

    FlowArn = field("FlowArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrantFlowEntitlementsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrantFlowEntitlementsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddBridgeOutputsResponse:
    boto3_raw_data: "type_defs.AddBridgeOutputsResponseTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return BridgeOutput.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddBridgeOutputsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddBridgeOutputsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBridgeOutputResponse:
    boto3_raw_data: "type_defs.UpdateBridgeOutputResponseTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @cached_property
    def Output(self):  # pragma: no cover
        return BridgeOutput.make_one(self.boto3_raw_data["Output"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBridgeOutputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeOutputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayInstanceResponse:
    boto3_raw_data: "type_defs.DescribeGatewayInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GatewayInstance(self):  # pragma: no cover
        return GatewayInstance.make_one(self.boto3_raw_data["GatewayInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGatewayInstanceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowSourceThumbnailResponse:
    boto3_raw_data: "type_defs.DescribeFlowSourceThumbnailResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ThumbnailDetails(self):  # pragma: no cover
        return ThumbnailDetails.make_one(self.boto3_raw_data["ThumbnailDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFlowSourceThumbnailResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowSourceThumbnailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGatewayResponse:
    boto3_raw_data: "type_defs.CreateGatewayResponseTypeDef" = dataclasses.field()

    @cached_property
    def Gateway(self):  # pragma: no cover
        return Gateway.make_one(self.boto3_raw_data["Gateway"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayResponse:
    boto3_raw_data: "type_defs.DescribeGatewayResponseTypeDef" = dataclasses.field()

    @cached_property
    def Gateway(self):  # pragma: no cover
        return Gateway.make_one(self.boto3_raw_data["Gateway"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStreamOutputConfigurationRequest:
    boto3_raw_data: "type_defs.MediaStreamOutputConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    EncodingName = field("EncodingName")
    MediaStreamName = field("MediaStreamName")

    @cached_property
    def DestinationConfigurations(self):  # pragma: no cover
        return DestinationConfigurationRequest.make_many(
            self.boto3_raw_data["DestinationConfigurations"]
        )

    @cached_property
    def EncodingParameters(self):  # pragma: no cover
        return EncodingParametersRequest.make_one(
            self.boto3_raw_data["EncodingParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaStreamOutputConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaStreamOutputConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStreamSourceConfigurationRequest:
    boto3_raw_data: "type_defs.MediaStreamSourceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    EncodingName = field("EncodingName")
    MediaStreamName = field("MediaStreamName")

    @cached_property
    def InputConfigurations(self):  # pragma: no cover
        return InputConfigurationRequest.make_many(
            self.boto3_raw_data["InputConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaStreamSourceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaStreamSourceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStreamOutputConfiguration:
    boto3_raw_data: "type_defs.MediaStreamOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    EncodingName = field("EncodingName")
    MediaStreamName = field("MediaStreamName")

    @cached_property
    def DestinationConfigurations(self):  # pragma: no cover
        return DestinationConfiguration.make_many(
            self.boto3_raw_data["DestinationConfigurations"]
        )

    @cached_property
    def EncodingParameters(self):  # pragma: no cover
        return EncodingParameters.make_one(self.boto3_raw_data["EncodingParameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MediaStreamOutputConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaStreamOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStreamSourceConfiguration:
    boto3_raw_data: "type_defs.MediaStreamSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    EncodingName = field("EncodingName")
    MediaStreamName = field("MediaStreamName")

    @cached_property
    def InputConfigurations(self):  # pragma: no cover
        return InputConfiguration.make_many(self.boto3_raw_data["InputConfigurations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MediaStreamSourceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaStreamSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBridgeRequest:
    boto3_raw_data: "type_defs.UpdateBridgeRequestTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @cached_property
    def EgressGatewayBridge(self):  # pragma: no cover
        return UpdateEgressGatewayBridgeRequest.make_one(
            self.boto3_raw_data["EgressGatewayBridge"]
        )

    @cached_property
    def IngressGatewayBridge(self):  # pragma: no cover
        return UpdateIngressGatewayBridgeRequest.make_one(
            self.boto3_raw_data["IngressGatewayBridge"]
        )

    @cached_property
    def SourceFailoverConfig(self):  # pragma: no cover
        return UpdateFailoverConfig.make_one(
            self.boto3_raw_data["SourceFailoverConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBridgeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowsResponse:
    boto3_raw_data: "type_defs.ListFlowsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Flows(self):  # pragma: no cover
        return ListedFlow.make_many(self.boto3_raw_data["Flows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFlowsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddMediaStreamRequest:
    boto3_raw_data: "type_defs.AddMediaStreamRequestTypeDef" = dataclasses.field()

    MediaStreamId = field("MediaStreamId")
    MediaStreamName = field("MediaStreamName")
    MediaStreamType = field("MediaStreamType")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return MediaStreamAttributesRequest.make_one(self.boto3_raw_data["Attributes"])

    ClockRate = field("ClockRate")
    Description = field("Description")
    VideoFormat = field("VideoFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddMediaStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddMediaStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowMediaStreamRequest:
    boto3_raw_data: "type_defs.UpdateFlowMediaStreamRequestTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")
    MediaStreamName = field("MediaStreamName")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return MediaStreamAttributesRequest.make_one(self.boto3_raw_data["Attributes"])

    ClockRate = field("ClockRate")
    Description = field("Description")
    MediaStreamType = field("MediaStreamType")
    VideoFormat = field("VideoFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowMediaStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowMediaStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStream:
    boto3_raw_data: "type_defs.MediaStreamTypeDef" = dataclasses.field()

    Fmt = field("Fmt")
    MediaStreamId = field("MediaStreamId")
    MediaStreamName = field("MediaStreamName")
    MediaStreamType = field("MediaStreamType")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return MediaStreamAttributes.make_one(self.boto3_raw_data["Attributes"])

    ClockRate = field("ClockRate")
    Description = field("Description")
    VideoFormat = field("VideoFormat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MediaStreamTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransportStreamProgram:
    boto3_raw_data: "type_defs.TransportStreamProgramTypeDef" = dataclasses.field()

    PcrPid = field("PcrPid")
    ProgramNumber = field("ProgramNumber")
    ProgramPid = field("ProgramPid")

    @cached_property
    def Streams(self):  # pragma: no cover
        return TransportStream.make_many(self.boto3_raw_data["Streams"])

    ProgramName = field("ProgramName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransportStreamProgramTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransportStreamProgramTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoringConfigOutput:
    boto3_raw_data: "type_defs.MonitoringConfigOutputTypeDef" = dataclasses.field()

    ThumbnailState = field("ThumbnailState")

    @cached_property
    def AudioMonitoringSettings(self):  # pragma: no cover
        return AudioMonitoringSetting.make_many(
            self.boto3_raw_data["AudioMonitoringSettings"]
        )

    ContentQualityAnalysisState = field("ContentQualityAnalysisState")

    @cached_property
    def VideoMonitoringSettings(self):  # pragma: no cover
        return VideoMonitoringSetting.make_many(
            self.boto3_raw_data["VideoMonitoringSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitoringConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoringConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoringConfig:
    boto3_raw_data: "type_defs.MonitoringConfigTypeDef" = dataclasses.field()

    ThumbnailState = field("ThumbnailState")

    @cached_property
    def AudioMonitoringSettings(self):  # pragma: no cover
        return AudioMonitoringSetting.make_many(
            self.boto3_raw_data["AudioMonitoringSettings"]
        )

    ContentQualityAnalysisState = field("ContentQualityAnalysisState")

    @cached_property
    def VideoMonitoringSettings(self):  # pragma: no cover
        return VideoMonitoringSetting.make_many(
            self.boto3_raw_data["VideoMonitoringSettings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonitoringConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoringConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOfferingResponse:
    boto3_raw_data: "type_defs.DescribeOfferingResponseTypeDef" = dataclasses.field()

    @cached_property
    def Offering(self):  # pragma: no cover
        return Offering.make_one(self.boto3_raw_data["Offering"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOfferingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOfferingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOfferingsResponse:
    boto3_raw_data: "type_defs.ListOfferingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Offerings(self):  # pragma: no cover
        return Offering.make_many(self.boto3_raw_data["Offerings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOfferingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOfferingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservationResponse:
    boto3_raw_data: "type_defs.DescribeReservationResponseTypeDef" = dataclasses.field()

    @cached_property
    def Reservation(self):  # pragma: no cover
        return Reservation.make_one(self.boto3_raw_data["Reservation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReservationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationsResponse:
    boto3_raw_data: "type_defs.ListReservationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Reservations(self):  # pragma: no cover
        return Reservation.make_many(self.boto3_raw_data["Reservations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReservationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseOfferingResponse:
    boto3_raw_data: "type_defs.PurchaseOfferingResponseTypeDef" = dataclasses.field()

    @cached_property
    def Reservation(self):  # pragma: no cover
        return Reservation.make_one(self.boto3_raw_data["Reservation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PurchaseOfferingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseOfferingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddBridgeSourcesRequest:
    boto3_raw_data: "type_defs.AddBridgeSourcesRequestTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @cached_property
    def Sources(self):  # pragma: no cover
        return AddBridgeSourceRequest.make_many(self.boto3_raw_data["Sources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddBridgeSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddBridgeSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBridgeRequest:
    boto3_raw_data: "type_defs.CreateBridgeRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    PlacementArn = field("PlacementArn")

    @cached_property
    def Sources(self):  # pragma: no cover
        return AddBridgeSourceRequest.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def EgressGatewayBridge(self):  # pragma: no cover
        return AddEgressGatewayBridgeRequest.make_one(
            self.boto3_raw_data["EgressGatewayBridge"]
        )

    @cached_property
    def IngressGatewayBridge(self):  # pragma: no cover
        return AddIngressGatewayBridgeRequest.make_one(
            self.boto3_raw_data["IngressGatewayBridge"]
        )

    @cached_property
    def Outputs(self):  # pragma: no cover
        return AddBridgeOutputRequest.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def SourceFailoverConfig(self):  # pragma: no cover
        return FailoverConfig.make_one(self.boto3_raw_data["SourceFailoverConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBridgeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBridgeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddBridgeSourcesResponse:
    boto3_raw_data: "type_defs.AddBridgeSourcesResponseTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @cached_property
    def Sources(self):  # pragma: no cover
        return BridgeSource.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddBridgeSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddBridgeSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Bridge:
    boto3_raw_data: "type_defs.BridgeTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")
    BridgeState = field("BridgeState")
    Name = field("Name")
    PlacementArn = field("PlacementArn")

    @cached_property
    def BridgeMessages(self):  # pragma: no cover
        return MessageDetail.make_many(self.boto3_raw_data["BridgeMessages"])

    @cached_property
    def EgressGatewayBridge(self):  # pragma: no cover
        return EgressGatewayBridge.make_one(self.boto3_raw_data["EgressGatewayBridge"])

    @cached_property
    def IngressGatewayBridge(self):  # pragma: no cover
        return IngressGatewayBridge.make_one(
            self.boto3_raw_data["IngressGatewayBridge"]
        )

    @cached_property
    def Outputs(self):  # pragma: no cover
        return BridgeOutput.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def SourceFailoverConfig(self):  # pragma: no cover
        return FailoverConfig.make_one(self.boto3_raw_data["SourceFailoverConfig"])

    @cached_property
    def Sources(self):  # pragma: no cover
        return BridgeSource.make_many(self.boto3_raw_data["Sources"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BridgeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BridgeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBridgeSourceResponse:
    boto3_raw_data: "type_defs.UpdateBridgeSourceResponseTypeDef" = dataclasses.field()

    BridgeArn = field("BridgeArn")

    @cached_property
    def Source(self):  # pragma: no cover
        return BridgeSource.make_one(self.boto3_raw_data["Source"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBridgeSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddOutputRequest:
    boto3_raw_data: "type_defs.AddOutputRequestTypeDef" = dataclasses.field()

    Protocol = field("Protocol")
    CidrAllowList = field("CidrAllowList")
    Description = field("Description")
    Destination = field("Destination")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    MaxLatency = field("MaxLatency")

    @cached_property
    def MediaStreamOutputConfigurations(self):  # pragma: no cover
        return MediaStreamOutputConfigurationRequest.make_many(
            self.boto3_raw_data["MediaStreamOutputConfigurations"]
        )

    MinLatency = field("MinLatency")
    Name = field("Name")
    Port = field("Port")
    RemoteId = field("RemoteId")
    SenderControlPort = field("SenderControlPort")
    SmoothingLatency = field("SmoothingLatency")
    StreamId = field("StreamId")

    @cached_property
    def VpcInterfaceAttachment(self):  # pragma: no cover
        return VpcInterfaceAttachment.make_one(
            self.boto3_raw_data["VpcInterfaceAttachment"]
        )

    OutputStatus = field("OutputStatus")
    NdiSpeedHqQuality = field("NdiSpeedHqQuality")
    NdiProgramName = field("NdiProgramName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddOutputRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowOutputRequest:
    boto3_raw_data: "type_defs.UpdateFlowOutputRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    OutputArn = field("OutputArn")
    CidrAllowList = field("CidrAllowList")
    Description = field("Description")
    Destination = field("Destination")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return UpdateEncryption.make_one(self.boto3_raw_data["Encryption"])

    MaxLatency = field("MaxLatency")

    @cached_property
    def MediaStreamOutputConfigurations(self):  # pragma: no cover
        return MediaStreamOutputConfigurationRequest.make_many(
            self.boto3_raw_data["MediaStreamOutputConfigurations"]
        )

    MinLatency = field("MinLatency")
    Port = field("Port")
    Protocol = field("Protocol")
    RemoteId = field("RemoteId")
    SenderControlPort = field("SenderControlPort")
    SenderIpAddress = field("SenderIpAddress")
    SmoothingLatency = field("SmoothingLatency")
    StreamId = field("StreamId")

    @cached_property
    def VpcInterfaceAttachment(self):  # pragma: no cover
        return VpcInterfaceAttachment.make_one(
            self.boto3_raw_data["VpcInterfaceAttachment"]
        )

    OutputStatus = field("OutputStatus")
    NdiProgramName = field("NdiProgramName")
    NdiSpeedHqQuality = field("NdiSpeedHqQuality")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowOutputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetSourceRequest:
    boto3_raw_data: "type_defs.SetSourceRequestTypeDef" = dataclasses.field()

    @cached_property
    def Decryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Decryption"])

    Description = field("Description")
    EntitlementArn = field("EntitlementArn")
    IngestPort = field("IngestPort")
    MaxBitrate = field("MaxBitrate")
    MaxLatency = field("MaxLatency")
    MaxSyncBuffer = field("MaxSyncBuffer")

    @cached_property
    def MediaStreamSourceConfigurations(self):  # pragma: no cover
        return MediaStreamSourceConfigurationRequest.make_many(
            self.boto3_raw_data["MediaStreamSourceConfigurations"]
        )

    MinLatency = field("MinLatency")
    Name = field("Name")
    Protocol = field("Protocol")
    SenderControlPort = field("SenderControlPort")
    SenderIpAddress = field("SenderIpAddress")
    SourceListenerAddress = field("SourceListenerAddress")
    SourceListenerPort = field("SourceListenerPort")
    StreamId = field("StreamId")
    VpcInterfaceName = field("VpcInterfaceName")
    WhitelistCidr = field("WhitelistCidr")

    @cached_property
    def GatewayBridgeSource(self):  # pragma: no cover
        return SetGatewayBridgeSourceRequest.make_one(
            self.boto3_raw_data["GatewayBridgeSource"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SetSourceRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowSourceRequest:
    boto3_raw_data: "type_defs.UpdateFlowSourceRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")
    SourceArn = field("SourceArn")

    @cached_property
    def Decryption(self):  # pragma: no cover
        return UpdateEncryption.make_one(self.boto3_raw_data["Decryption"])

    Description = field("Description")
    EntitlementArn = field("EntitlementArn")
    IngestPort = field("IngestPort")
    MaxBitrate = field("MaxBitrate")
    MaxLatency = field("MaxLatency")
    MaxSyncBuffer = field("MaxSyncBuffer")

    @cached_property
    def MediaStreamSourceConfigurations(self):  # pragma: no cover
        return MediaStreamSourceConfigurationRequest.make_many(
            self.boto3_raw_data["MediaStreamSourceConfigurations"]
        )

    MinLatency = field("MinLatency")
    Protocol = field("Protocol")
    SenderControlPort = field("SenderControlPort")
    SenderIpAddress = field("SenderIpAddress")
    SourceListenerAddress = field("SourceListenerAddress")
    SourceListenerPort = field("SourceListenerPort")
    StreamId = field("StreamId")
    VpcInterfaceName = field("VpcInterfaceName")
    WhitelistCidr = field("WhitelistCidr")

    @cached_property
    def GatewayBridgeSource(self):  # pragma: no cover
        return UpdateGatewayBridgeSourceRequest.make_one(
            self.boto3_raw_data["GatewayBridgeSource"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Output:
    boto3_raw_data: "type_defs.OutputTypeDef" = dataclasses.field()

    Name = field("Name")
    OutputArn = field("OutputArn")
    DataTransferSubscriberFeePercent = field("DataTransferSubscriberFeePercent")
    Description = field("Description")
    Destination = field("Destination")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    EntitlementArn = field("EntitlementArn")
    ListenerAddress = field("ListenerAddress")
    MediaLiveInputArn = field("MediaLiveInputArn")

    @cached_property
    def MediaStreamOutputConfigurations(self):  # pragma: no cover
        return MediaStreamOutputConfiguration.make_many(
            self.boto3_raw_data["MediaStreamOutputConfigurations"]
        )

    Port = field("Port")

    @cached_property
    def Transport(self):  # pragma: no cover
        return Transport.make_one(self.boto3_raw_data["Transport"])

    @cached_property
    def VpcInterfaceAttachment(self):  # pragma: no cover
        return VpcInterfaceAttachment.make_one(
            self.boto3_raw_data["VpcInterfaceAttachment"]
        )

    BridgeArn = field("BridgeArn")
    BridgePorts = field("BridgePorts")
    OutputStatus = field("OutputStatus")
    PeerIpAddress = field("PeerIpAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Source:
    boto3_raw_data: "type_defs.SourceTypeDef" = dataclasses.field()

    Name = field("Name")
    SourceArn = field("SourceArn")
    DataTransferSubscriberFeePercent = field("DataTransferSubscriberFeePercent")

    @cached_property
    def Decryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Decryption"])

    Description = field("Description")
    EntitlementArn = field("EntitlementArn")
    IngestIp = field("IngestIp")
    IngestPort = field("IngestPort")

    @cached_property
    def MediaStreamSourceConfigurations(self):  # pragma: no cover
        return MediaStreamSourceConfiguration.make_many(
            self.boto3_raw_data["MediaStreamSourceConfigurations"]
        )

    SenderControlPort = field("SenderControlPort")
    SenderIpAddress = field("SenderIpAddress")

    @cached_property
    def Transport(self):  # pragma: no cover
        return Transport.make_one(self.boto3_raw_data["Transport"])

    VpcInterfaceName = field("VpcInterfaceName")
    WhitelistCidr = field("WhitelistCidr")

    @cached_property
    def GatewayBridgeSource(self):  # pragma: no cover
        return GatewayBridgeSource.make_one(self.boto3_raw_data["GatewayBridgeSource"])

    PeerIpAddress = field("PeerIpAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddFlowMediaStreamsRequest:
    boto3_raw_data: "type_defs.AddFlowMediaStreamsRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def MediaStreams(self):  # pragma: no cover
        return AddMediaStreamRequest.make_many(self.boto3_raw_data["MediaStreams"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddFlowMediaStreamsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddFlowMediaStreamsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddFlowMediaStreamsResponse:
    boto3_raw_data: "type_defs.AddFlowMediaStreamsResponseTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def MediaStreams(self):  # pragma: no cover
        return MediaStream.make_many(self.boto3_raw_data["MediaStreams"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddFlowMediaStreamsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddFlowMediaStreamsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowMediaStreamResponse:
    boto3_raw_data: "type_defs.UpdateFlowMediaStreamResponseTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")

    @cached_property
    def MediaStream(self):  # pragma: no cover
        return MediaStream.make_one(self.boto3_raw_data["MediaStream"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFlowMediaStreamResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowMediaStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransportMediaInfo:
    boto3_raw_data: "type_defs.TransportMediaInfoTypeDef" = dataclasses.field()

    @cached_property
    def Programs(self):  # pragma: no cover
        return TransportStreamProgram.make_many(self.boto3_raw_data["Programs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransportMediaInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransportMediaInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBridgeResponse:
    boto3_raw_data: "type_defs.CreateBridgeResponseTypeDef" = dataclasses.field()

    @cached_property
    def Bridge(self):  # pragma: no cover
        return Bridge.make_one(self.boto3_raw_data["Bridge"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBridgeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBridgeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBridgeResponse:
    boto3_raw_data: "type_defs.DescribeBridgeResponseTypeDef" = dataclasses.field()

    @cached_property
    def Bridge(self):  # pragma: no cover
        return Bridge.make_one(self.boto3_raw_data["Bridge"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBridgeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBridgeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBridgeResponse:
    boto3_raw_data: "type_defs.UpdateBridgeResponseTypeDef" = dataclasses.field()

    @cached_property
    def Bridge(self):  # pragma: no cover
        return Bridge.make_one(self.boto3_raw_data["Bridge"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBridgeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBridgeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddFlowOutputsRequest:
    boto3_raw_data: "type_defs.AddFlowOutputsRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return AddOutputRequest.make_many(self.boto3_raw_data["Outputs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddFlowOutputsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddFlowOutputsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddFlowSourcesRequest:
    boto3_raw_data: "type_defs.AddFlowSourcesRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def Sources(self):  # pragma: no cover
        return SetSourceRequest.make_many(self.boto3_raw_data["Sources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddFlowSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddFlowSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddFlowOutputsResponse:
    boto3_raw_data: "type_defs.AddFlowOutputsResponseTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddFlowOutputsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddFlowOutputsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowOutputResponse:
    boto3_raw_data: "type_defs.UpdateFlowOutputResponseTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def Output(self):  # pragma: no cover
        return Output.make_one(self.boto3_raw_data["Output"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowOutputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowOutputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddFlowSourcesResponse:
    boto3_raw_data: "type_defs.AddFlowSourcesResponseTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def Sources(self):  # pragma: no cover
        return Source.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddFlowSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddFlowSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Flow:
    boto3_raw_data: "type_defs.FlowTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return Entitlement.make_many(self.boto3_raw_data["Entitlements"])

    FlowArn = field("FlowArn")
    Name = field("Name")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def Source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["Source"])

    Status = field("Status")
    Description = field("Description")
    EgressIp = field("EgressIp")

    @cached_property
    def MediaStreams(self):  # pragma: no cover
        return MediaStream.make_many(self.boto3_raw_data["MediaStreams"])

    @cached_property
    def SourceFailoverConfig(self):  # pragma: no cover
        return FailoverConfig.make_one(self.boto3_raw_data["SourceFailoverConfig"])

    @cached_property
    def Sources(self):  # pragma: no cover
        return Source.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def VpcInterfaces(self):  # pragma: no cover
        return VpcInterface.make_many(self.boto3_raw_data["VpcInterfaces"])

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return Maintenance.make_one(self.boto3_raw_data["Maintenance"])

    @cached_property
    def SourceMonitoringConfig(self):  # pragma: no cover
        return MonitoringConfigOutput.make_one(
            self.boto3_raw_data["SourceMonitoringConfig"]
        )

    FlowSize = field("FlowSize")

    @cached_property
    def NdiConfig(self):  # pragma: no cover
        return NdiConfigOutput.make_one(self.boto3_raw_data["NdiConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowSourceResponse:
    boto3_raw_data: "type_defs.UpdateFlowSourceResponseTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def Source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["Source"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowSourceMetadataResponse:
    boto3_raw_data: "type_defs.DescribeFlowSourceMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")

    @cached_property
    def Messages(self):  # pragma: no cover
        return MessageDetail.make_many(self.boto3_raw_data["Messages"])

    Timestamp = field("Timestamp")

    @cached_property
    def TransportMediaInfo(self):  # pragma: no cover
        return TransportMediaInfo.make_one(self.boto3_raw_data["TransportMediaInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFlowSourceMetadataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowSourceMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlowRequest:
    boto3_raw_data: "type_defs.CreateFlowRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    AvailabilityZone = field("AvailabilityZone")

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return GrantEntitlementRequest.make_many(self.boto3_raw_data["Entitlements"])

    @cached_property
    def MediaStreams(self):  # pragma: no cover
        return AddMediaStreamRequest.make_many(self.boto3_raw_data["MediaStreams"])

    @cached_property
    def Outputs(self):  # pragma: no cover
        return AddOutputRequest.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def Source(self):  # pragma: no cover
        return SetSourceRequest.make_one(self.boto3_raw_data["Source"])

    @cached_property
    def SourceFailoverConfig(self):  # pragma: no cover
        return FailoverConfig.make_one(self.boto3_raw_data["SourceFailoverConfig"])

    @cached_property
    def Sources(self):  # pragma: no cover
        return SetSourceRequest.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def VpcInterfaces(self):  # pragma: no cover
        return VpcInterfaceRequest.make_many(self.boto3_raw_data["VpcInterfaces"])

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return AddMaintenance.make_one(self.boto3_raw_data["Maintenance"])

    SourceMonitoringConfig = field("SourceMonitoringConfig")
    FlowSize = field("FlowSize")
    NdiConfig = field("NdiConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowRequest:
    boto3_raw_data: "type_defs.UpdateFlowRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @cached_property
    def SourceFailoverConfig(self):  # pragma: no cover
        return UpdateFailoverConfig.make_one(
            self.boto3_raw_data["SourceFailoverConfig"]
        )

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return UpdateMaintenance.make_one(self.boto3_raw_data["Maintenance"])

    SourceMonitoringConfig = field("SourceMonitoringConfig")
    NdiConfig = field("NdiConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlowResponse:
    boto3_raw_data: "type_defs.CreateFlowResponseTypeDef" = dataclasses.field()

    @cached_property
    def Flow(self):  # pragma: no cover
        return Flow.make_one(self.boto3_raw_data["Flow"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowResponse:
    boto3_raw_data: "type_defs.DescribeFlowResponseTypeDef" = dataclasses.field()

    @cached_property
    def Flow(self):  # pragma: no cover
        return Flow.make_one(self.boto3_raw_data["Flow"])

    @cached_property
    def Messages(self):  # pragma: no cover
        return Messages.make_one(self.boto3_raw_data["Messages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowResponse:
    boto3_raw_data: "type_defs.UpdateFlowResponseTypeDef" = dataclasses.field()

    @cached_property
    def Flow(self):  # pragma: no cover
        return Flow.make_one(self.boto3_raw_data["Flow"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
