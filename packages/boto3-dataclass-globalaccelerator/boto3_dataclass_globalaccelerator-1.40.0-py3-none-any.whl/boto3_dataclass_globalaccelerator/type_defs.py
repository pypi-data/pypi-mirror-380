# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_globalaccelerator import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceleratorAttributes:
    boto3_raw_data: "type_defs.AcceleratorAttributesTypeDef" = dataclasses.field()

    FlowLogsEnabled = field("FlowLogsEnabled")
    FlowLogsS3Bucket = field("FlowLogsS3Bucket")
    FlowLogsS3Prefix = field("FlowLogsS3Prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceleratorAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceleratorAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceleratorEvent:
    boto3_raw_data: "type_defs.AcceleratorEventTypeDef" = dataclasses.field()

    Message = field("Message")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AcceleratorEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceleratorEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpSet:
    boto3_raw_data: "type_defs.IpSetTypeDef" = dataclasses.field()

    IpFamily = field("IpFamily")
    IpAddresses = field("IpAddresses")
    IpAddressFamily = field("IpAddressFamily")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomRoutingEndpointConfiguration:
    boto3_raw_data: "type_defs.CustomRoutingEndpointConfigurationTypeDef" = (
        dataclasses.field()
    )

    EndpointId = field("EndpointId")
    AttachmentArn = field("AttachmentArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomRoutingEndpointConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomRoutingEndpointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomRoutingEndpointDescription:
    boto3_raw_data: "type_defs.CustomRoutingEndpointDescriptionTypeDef" = (
        dataclasses.field()
    )

    EndpointId = field("EndpointId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomRoutingEndpointDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomRoutingEndpointDescriptionTypeDef"]
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
class EndpointConfiguration:
    boto3_raw_data: "type_defs.EndpointConfigurationTypeDef" = dataclasses.field()

    EndpointId = field("EndpointId")
    Weight = field("Weight")
    ClientIPPreservationEnabled = field("ClientIPPreservationEnabled")
    AttachmentArn = field("AttachmentArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointDescription:
    boto3_raw_data: "type_defs.EndpointDescriptionTypeDef" = dataclasses.field()

    EndpointId = field("EndpointId")
    Weight = field("Weight")
    HealthState = field("HealthState")
    HealthReason = field("HealthReason")
    ClientIPPreservationEnabled = field("ClientIPPreservationEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvertiseByoipCidrRequest:
    boto3_raw_data: "type_defs.AdvertiseByoipCidrRequestTypeDef" = dataclasses.field()

    Cidr = field("Cidr")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvertiseByoipCidrRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvertiseByoipCidrRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowCustomRoutingTrafficRequest:
    boto3_raw_data: "type_defs.AllowCustomRoutingTrafficRequestTypeDef" = (
        dataclasses.field()
    )

    EndpointGroupArn = field("EndpointGroupArn")
    EndpointId = field("EndpointId")
    DestinationAddresses = field("DestinationAddresses")
    DestinationPorts = field("DestinationPorts")
    AllowAllTrafficToEndpoint = field("AllowAllTrafficToEndpoint")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AllowCustomRoutingTrafficRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowCustomRoutingTrafficRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    EndpointId = field("EndpointId")
    Cidr = field("Cidr")
    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ByoipCidrEvent:
    boto3_raw_data: "type_defs.ByoipCidrEventTypeDef" = dataclasses.field()

    Message = field("Message")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ByoipCidrEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ByoipCidrEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CidrAuthorizationContext:
    boto3_raw_data: "type_defs.CidrAuthorizationContextTypeDef" = dataclasses.field()

    Message = field("Message")
    Signature = field("Signature")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CidrAuthorizationContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CidrAuthorizationContextTypeDef"]
        ],
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
class CustomRoutingDestinationConfiguration:
    boto3_raw_data: "type_defs.CustomRoutingDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    FromPort = field("FromPort")
    ToPort = field("ToPort")
    Protocols = field("Protocols")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomRoutingDestinationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomRoutingDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortRange:
    boto3_raw_data: "type_defs.PortRangeTypeDef" = dataclasses.field()

    FromPort = field("FromPort")
    ToPort = field("ToPort")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortOverride:
    boto3_raw_data: "type_defs.PortOverrideTypeDef" = dataclasses.field()

    ListenerPort = field("ListenerPort")
    EndpointPort = field("EndpointPort")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrossAccountResource:
    boto3_raw_data: "type_defs.CrossAccountResourceTypeDef" = dataclasses.field()

    EndpointId = field("EndpointId")
    Cidr = field("Cidr")
    AttachmentArn = field("AttachmentArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CrossAccountResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrossAccountResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomRoutingAcceleratorAttributes:
    boto3_raw_data: "type_defs.CustomRoutingAcceleratorAttributesTypeDef" = (
        dataclasses.field()
    )

    FlowLogsEnabled = field("FlowLogsEnabled")
    FlowLogsS3Bucket = field("FlowLogsS3Bucket")
    FlowLogsS3Prefix = field("FlowLogsS3Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomRoutingAcceleratorAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomRoutingAcceleratorAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomRoutingDestinationDescription:
    boto3_raw_data: "type_defs.CustomRoutingDestinationDescriptionTypeDef" = (
        dataclasses.field()
    )

    FromPort = field("FromPort")
    ToPort = field("ToPort")
    Protocols = field("Protocols")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomRoutingDestinationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomRoutingDestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAcceleratorRequest:
    boto3_raw_data: "type_defs.DeleteAcceleratorRequestTypeDef" = dataclasses.field()

    AcceleratorArn = field("AcceleratorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAcceleratorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAcceleratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCrossAccountAttachmentRequest:
    boto3_raw_data: "type_defs.DeleteCrossAccountAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    AttachmentArn = field("AttachmentArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCrossAccountAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCrossAccountAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomRoutingAcceleratorRequest:
    boto3_raw_data: "type_defs.DeleteCustomRoutingAcceleratorRequestTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCustomRoutingAcceleratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomRoutingAcceleratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomRoutingEndpointGroupRequest:
    boto3_raw_data: "type_defs.DeleteCustomRoutingEndpointGroupRequestTypeDef" = (
        dataclasses.field()
    )

    EndpointGroupArn = field("EndpointGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCustomRoutingEndpointGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomRoutingEndpointGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomRoutingListenerRequest:
    boto3_raw_data: "type_defs.DeleteCustomRoutingListenerRequestTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCustomRoutingListenerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomRoutingListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEndpointGroupRequest:
    boto3_raw_data: "type_defs.DeleteEndpointGroupRequestTypeDef" = dataclasses.field()

    EndpointGroupArn = field("EndpointGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEndpointGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEndpointGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteListenerRequest:
    boto3_raw_data: "type_defs.DeleteListenerRequestTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteListenerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DenyCustomRoutingTrafficRequest:
    boto3_raw_data: "type_defs.DenyCustomRoutingTrafficRequestTypeDef" = (
        dataclasses.field()
    )

    EndpointGroupArn = field("EndpointGroupArn")
    EndpointId = field("EndpointId")
    DestinationAddresses = field("DestinationAddresses")
    DestinationPorts = field("DestinationPorts")
    DenyAllTrafficToEndpoint = field("DenyAllTrafficToEndpoint")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DenyCustomRoutingTrafficRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DenyCustomRoutingTrafficRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeprovisionByoipCidrRequest:
    boto3_raw_data: "type_defs.DeprovisionByoipCidrRequestTypeDef" = dataclasses.field()

    Cidr = field("Cidr")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeprovisionByoipCidrRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeprovisionByoipCidrRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAcceleratorAttributesRequest:
    boto3_raw_data: "type_defs.DescribeAcceleratorAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAcceleratorAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAcceleratorAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAcceleratorRequest:
    boto3_raw_data: "type_defs.DescribeAcceleratorRequestTypeDef" = dataclasses.field()

    AcceleratorArn = field("AcceleratorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAcceleratorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAcceleratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCrossAccountAttachmentRequest:
    boto3_raw_data: "type_defs.DescribeCrossAccountAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    AttachmentArn = field("AttachmentArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCrossAccountAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCrossAccountAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomRoutingAcceleratorAttributesRequest:
    boto3_raw_data: (
        "type_defs.DescribeCustomRoutingAcceleratorAttributesRequestTypeDef"
    ) = dataclasses.field()

    AcceleratorArn = field("AcceleratorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomRoutingAcceleratorAttributesRequestTypeDef"
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
                "type_defs.DescribeCustomRoutingAcceleratorAttributesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomRoutingAcceleratorRequest:
    boto3_raw_data: "type_defs.DescribeCustomRoutingAcceleratorRequestTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomRoutingAcceleratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomRoutingAcceleratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomRoutingEndpointGroupRequest:
    boto3_raw_data: "type_defs.DescribeCustomRoutingEndpointGroupRequestTypeDef" = (
        dataclasses.field()
    )

    EndpointGroupArn = field("EndpointGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomRoutingEndpointGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomRoutingEndpointGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomRoutingListenerRequest:
    boto3_raw_data: "type_defs.DescribeCustomRoutingListenerRequestTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomRoutingListenerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomRoutingListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointGroupRequest:
    boto3_raw_data: "type_defs.DescribeEndpointGroupRequestTypeDef" = (
        dataclasses.field()
    )

    EndpointGroupArn = field("EndpointGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeListenerRequest:
    boto3_raw_data: "type_defs.DescribeListenerRequestTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeListenerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SocketAddress:
    boto3_raw_data: "type_defs.SocketAddressTypeDef" = dataclasses.field()

    IpAddress = field("IpAddress")
    Port = field("Port")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SocketAddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SocketAddressTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointIdentifier:
    boto3_raw_data: "type_defs.EndpointIdentifierTypeDef" = dataclasses.field()

    EndpointId = field("EndpointId")
    ClientIPPreservationEnabled = field("ClientIPPreservationEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointIdentifierTypeDef"]
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
class ListAcceleratorsRequest:
    boto3_raw_data: "type_defs.ListAcceleratorsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAcceleratorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAcceleratorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListByoipCidrsRequest:
    boto3_raw_data: "type_defs.ListByoipCidrsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListByoipCidrsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListByoipCidrsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCrossAccountAttachmentsRequest:
    boto3_raw_data: "type_defs.ListCrossAccountAttachmentsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCrossAccountAttachmentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCrossAccountAttachmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCrossAccountResourcesRequest:
    boto3_raw_data: "type_defs.ListCrossAccountResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceOwnerAwsAccountId = field("ResourceOwnerAwsAccountId")
    AcceleratorArn = field("AcceleratorArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCrossAccountResourcesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCrossAccountResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingAcceleratorsRequest:
    boto3_raw_data: "type_defs.ListCustomRoutingAcceleratorsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingAcceleratorsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingAcceleratorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingEndpointGroupsRequest:
    boto3_raw_data: "type_defs.ListCustomRoutingEndpointGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingEndpointGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingEndpointGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingListenersRequest:
    boto3_raw_data: "type_defs.ListCustomRoutingListenersRequestTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingListenersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingListenersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingPortMappingsByDestinationRequest:
    boto3_raw_data: (
        "type_defs.ListCustomRoutingPortMappingsByDestinationRequestTypeDef"
    ) = dataclasses.field()

    EndpointId = field("EndpointId")
    DestinationAddress = field("DestinationAddress")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingPortMappingsByDestinationRequestTypeDef"
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
                "type_defs.ListCustomRoutingPortMappingsByDestinationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingPortMappingsRequest:
    boto3_raw_data: "type_defs.ListCustomRoutingPortMappingsRequestTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")
    EndpointGroupArn = field("EndpointGroupArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingPortMappingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingPortMappingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointGroupsRequest:
    boto3_raw_data: "type_defs.ListEndpointGroupsRequestTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEndpointGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListListenersRequest:
    boto3_raw_data: "type_defs.ListListenersRequestTypeDef" = dataclasses.field()

    AcceleratorArn = field("AcceleratorArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListListenersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListListenersRequestTypeDef"]
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
class RemoveCustomRoutingEndpointsRequest:
    boto3_raw_data: "type_defs.RemoveCustomRoutingEndpointsRequestTypeDef" = (
        dataclasses.field()
    )

    EndpointIds = field("EndpointIds")
    EndpointGroupArn = field("EndpointGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveCustomRoutingEndpointsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveCustomRoutingEndpointsRequestTypeDef"]
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
class UpdateAcceleratorAttributesRequest:
    boto3_raw_data: "type_defs.UpdateAcceleratorAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")
    FlowLogsEnabled = field("FlowLogsEnabled")
    FlowLogsS3Bucket = field("FlowLogsS3Bucket")
    FlowLogsS3Prefix = field("FlowLogsS3Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAcceleratorAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAcceleratorAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAcceleratorRequest:
    boto3_raw_data: "type_defs.UpdateAcceleratorRequestTypeDef" = dataclasses.field()

    AcceleratorArn = field("AcceleratorArn")
    Name = field("Name")
    IpAddressType = field("IpAddressType")
    IpAddresses = field("IpAddresses")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAcceleratorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAcceleratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomRoutingAcceleratorAttributesRequest:
    boto3_raw_data: (
        "type_defs.UpdateCustomRoutingAcceleratorAttributesRequestTypeDef"
    ) = dataclasses.field()

    AcceleratorArn = field("AcceleratorArn")
    FlowLogsEnabled = field("FlowLogsEnabled")
    FlowLogsS3Bucket = field("FlowLogsS3Bucket")
    FlowLogsS3Prefix = field("FlowLogsS3Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomRoutingAcceleratorAttributesRequestTypeDef"
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
                "type_defs.UpdateCustomRoutingAcceleratorAttributesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomRoutingAcceleratorRequest:
    boto3_raw_data: "type_defs.UpdateCustomRoutingAcceleratorRequestTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")
    Name = field("Name")
    IpAddressType = field("IpAddressType")
    IpAddresses = field("IpAddresses")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomRoutingAcceleratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomRoutingAcceleratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WithdrawByoipCidrRequest:
    boto3_raw_data: "type_defs.WithdrawByoipCidrRequestTypeDef" = dataclasses.field()

    Cidr = field("Cidr")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WithdrawByoipCidrRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WithdrawByoipCidrRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Accelerator:
    boto3_raw_data: "type_defs.AcceleratorTypeDef" = dataclasses.field()

    AcceleratorArn = field("AcceleratorArn")
    Name = field("Name")
    IpAddressType = field("IpAddressType")
    Enabled = field("Enabled")

    @cached_property
    def IpSets(self):  # pragma: no cover
        return IpSet.make_many(self.boto3_raw_data["IpSets"])

    DnsName = field("DnsName")
    Status = field("Status")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")
    DualStackDnsName = field("DualStackDnsName")

    @cached_property
    def Events(self):  # pragma: no cover
        return AcceleratorEvent.make_many(self.boto3_raw_data["Events"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AcceleratorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AcceleratorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomRoutingAccelerator:
    boto3_raw_data: "type_defs.CustomRoutingAcceleratorTypeDef" = dataclasses.field()

    AcceleratorArn = field("AcceleratorArn")
    Name = field("Name")
    IpAddressType = field("IpAddressType")
    Enabled = field("Enabled")

    @cached_property
    def IpSets(self):  # pragma: no cover
        return IpSet.make_many(self.boto3_raw_data["IpSets"])

    DnsName = field("DnsName")
    Status = field("Status")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomRoutingAcceleratorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomRoutingAcceleratorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddCustomRoutingEndpointsRequest:
    boto3_raw_data: "type_defs.AddCustomRoutingEndpointsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndpointConfigurations(self):  # pragma: no cover
        return CustomRoutingEndpointConfiguration.make_many(
            self.boto3_raw_data["EndpointConfigurations"]
        )

    EndpointGroupArn = field("EndpointGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddCustomRoutingEndpointsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddCustomRoutingEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddCustomRoutingEndpointsResponse:
    boto3_raw_data: "type_defs.AddCustomRoutingEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndpointDescriptions(self):  # pragma: no cover
        return CustomRoutingEndpointDescription.make_many(
            self.boto3_raw_data["EndpointDescriptions"]
        )

    EndpointGroupArn = field("EndpointGroupArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddCustomRoutingEndpointsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddCustomRoutingEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAcceleratorAttributesResponse:
    boto3_raw_data: "type_defs.DescribeAcceleratorAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AcceleratorAttributes(self):  # pragma: no cover
        return AcceleratorAttributes.make_one(
            self.boto3_raw_data["AcceleratorAttributes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAcceleratorAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAcceleratorAttributesResponseTypeDef"]
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
class ListCrossAccountResourceAccountsResponse:
    boto3_raw_data: "type_defs.ListCrossAccountResourceAccountsResponseTypeDef" = (
        dataclasses.field()
    )

    ResourceOwnerAwsAccountIds = field("ResourceOwnerAwsAccountIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCrossAccountResourceAccountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCrossAccountResourceAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAcceleratorAttributesResponse:
    boto3_raw_data: "type_defs.UpdateAcceleratorAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AcceleratorAttributes(self):  # pragma: no cover
        return AcceleratorAttributes.make_one(
            self.boto3_raw_data["AcceleratorAttributes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAcceleratorAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAcceleratorAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddEndpointsRequest:
    boto3_raw_data: "type_defs.AddEndpointsRequestTypeDef" = dataclasses.field()

    @cached_property
    def EndpointConfigurations(self):  # pragma: no cover
        return EndpointConfiguration.make_many(
            self.boto3_raw_data["EndpointConfigurations"]
        )

    EndpointGroupArn = field("EndpointGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddEndpointsResponse:
    boto3_raw_data: "type_defs.AddEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointDescriptions(self):  # pragma: no cover
        return EndpointDescription.make_many(
            self.boto3_raw_data["EndpointDescriptions"]
        )

    EndpointGroupArn = field("EndpointGroupArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddEndpointsResponseTypeDef"]
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

    AttachmentArn = field("AttachmentArn")
    Name = field("Name")
    Principals = field("Principals")

    @cached_property
    def Resources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["Resources"])

    LastModifiedTime = field("LastModifiedTime")
    CreatedTime = field("CreatedTime")

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
class UpdateCrossAccountAttachmentRequest:
    boto3_raw_data: "type_defs.UpdateCrossAccountAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    AttachmentArn = field("AttachmentArn")
    Name = field("Name")
    AddPrincipals = field("AddPrincipals")
    RemovePrincipals = field("RemovePrincipals")

    @cached_property
    def AddResources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["AddResources"])

    @cached_property
    def RemoveResources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["RemoveResources"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCrossAccountAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCrossAccountAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ByoipCidr:
    boto3_raw_data: "type_defs.ByoipCidrTypeDef" = dataclasses.field()

    Cidr = field("Cidr")
    State = field("State")

    @cached_property
    def Events(self):  # pragma: no cover
        return ByoipCidrEvent.make_many(self.boto3_raw_data["Events"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ByoipCidrTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ByoipCidrTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionByoipCidrRequest:
    boto3_raw_data: "type_defs.ProvisionByoipCidrRequestTypeDef" = dataclasses.field()

    Cidr = field("Cidr")

    @cached_property
    def CidrAuthorizationContext(self):  # pragma: no cover
        return CidrAuthorizationContext.make_one(
            self.boto3_raw_data["CidrAuthorizationContext"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionByoipCidrRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionByoipCidrRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAcceleratorRequest:
    boto3_raw_data: "type_defs.CreateAcceleratorRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    IdempotencyToken = field("IdempotencyToken")
    IpAddressType = field("IpAddressType")
    IpAddresses = field("IpAddresses")
    Enabled = field("Enabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAcceleratorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAcceleratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCrossAccountAttachmentRequest:
    boto3_raw_data: "type_defs.CreateCrossAccountAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    IdempotencyToken = field("IdempotencyToken")
    Principals = field("Principals")

    @cached_property
    def Resources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["Resources"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCrossAccountAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCrossAccountAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomRoutingAcceleratorRequest:
    boto3_raw_data: "type_defs.CreateCustomRoutingAcceleratorRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    IdempotencyToken = field("IdempotencyToken")
    IpAddressType = field("IpAddressType")
    IpAddresses = field("IpAddresses")
    Enabled = field("Enabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomRoutingAcceleratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomRoutingAcceleratorRequestTypeDef"]
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

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateCustomRoutingEndpointGroupRequest:
    boto3_raw_data: "type_defs.CreateCustomRoutingEndpointGroupRequestTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")
    EndpointGroupRegion = field("EndpointGroupRegion")

    @cached_property
    def DestinationConfigurations(self):  # pragma: no cover
        return CustomRoutingDestinationConfiguration.make_many(
            self.boto3_raw_data["DestinationConfigurations"]
        )

    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomRoutingEndpointGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomRoutingEndpointGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomRoutingListenerRequest:
    boto3_raw_data: "type_defs.CreateCustomRoutingListenerRequestTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")

    @cached_property
    def PortRanges(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["PortRanges"])

    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomRoutingListenerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomRoutingListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateListenerRequest:
    boto3_raw_data: "type_defs.CreateListenerRequestTypeDef" = dataclasses.field()

    AcceleratorArn = field("AcceleratorArn")

    @cached_property
    def PortRanges(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["PortRanges"])

    Protocol = field("Protocol")
    IdempotencyToken = field("IdempotencyToken")
    ClientAffinity = field("ClientAffinity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateListenerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomRoutingListener:
    boto3_raw_data: "type_defs.CustomRoutingListenerTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")

    @cached_property
    def PortRanges(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["PortRanges"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomRoutingListenerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomRoutingListenerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Listener:
    boto3_raw_data: "type_defs.ListenerTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")

    @cached_property
    def PortRanges(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["PortRanges"])

    Protocol = field("Protocol")
    ClientAffinity = field("ClientAffinity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListenerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListenerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomRoutingListenerRequest:
    boto3_raw_data: "type_defs.UpdateCustomRoutingListenerRequestTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")

    @cached_property
    def PortRanges(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["PortRanges"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomRoutingListenerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomRoutingListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateListenerRequest:
    boto3_raw_data: "type_defs.UpdateListenerRequestTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")

    @cached_property
    def PortRanges(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["PortRanges"])

    Protocol = field("Protocol")
    ClientAffinity = field("ClientAffinity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateListenerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEndpointGroupRequest:
    boto3_raw_data: "type_defs.CreateEndpointGroupRequestTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")
    EndpointGroupRegion = field("EndpointGroupRegion")
    IdempotencyToken = field("IdempotencyToken")

    @cached_property
    def EndpointConfigurations(self):  # pragma: no cover
        return EndpointConfiguration.make_many(
            self.boto3_raw_data["EndpointConfigurations"]
        )

    TrafficDialPercentage = field("TrafficDialPercentage")
    HealthCheckPort = field("HealthCheckPort")
    HealthCheckProtocol = field("HealthCheckProtocol")
    HealthCheckPath = field("HealthCheckPath")
    HealthCheckIntervalSeconds = field("HealthCheckIntervalSeconds")
    ThresholdCount = field("ThresholdCount")

    @cached_property
    def PortOverrides(self):  # pragma: no cover
        return PortOverride.make_many(self.boto3_raw_data["PortOverrides"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointGroup:
    boto3_raw_data: "type_defs.EndpointGroupTypeDef" = dataclasses.field()

    EndpointGroupArn = field("EndpointGroupArn")
    EndpointGroupRegion = field("EndpointGroupRegion")

    @cached_property
    def EndpointDescriptions(self):  # pragma: no cover
        return EndpointDescription.make_many(
            self.boto3_raw_data["EndpointDescriptions"]
        )

    TrafficDialPercentage = field("TrafficDialPercentage")
    HealthCheckPort = field("HealthCheckPort")
    HealthCheckProtocol = field("HealthCheckProtocol")
    HealthCheckPath = field("HealthCheckPath")
    HealthCheckIntervalSeconds = field("HealthCheckIntervalSeconds")
    ThresholdCount = field("ThresholdCount")

    @cached_property
    def PortOverrides(self):  # pragma: no cover
        return PortOverride.make_many(self.boto3_raw_data["PortOverrides"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointGroupRequest:
    boto3_raw_data: "type_defs.UpdateEndpointGroupRequestTypeDef" = dataclasses.field()

    EndpointGroupArn = field("EndpointGroupArn")

    @cached_property
    def EndpointConfigurations(self):  # pragma: no cover
        return EndpointConfiguration.make_many(
            self.boto3_raw_data["EndpointConfigurations"]
        )

    TrafficDialPercentage = field("TrafficDialPercentage")
    HealthCheckPort = field("HealthCheckPort")
    HealthCheckProtocol = field("HealthCheckProtocol")
    HealthCheckPath = field("HealthCheckPath")
    HealthCheckIntervalSeconds = field("HealthCheckIntervalSeconds")
    ThresholdCount = field("ThresholdCount")

    @cached_property
    def PortOverrides(self):  # pragma: no cover
        return PortOverride.make_many(self.boto3_raw_data["PortOverrides"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCrossAccountResourcesResponse:
    boto3_raw_data: "type_defs.ListCrossAccountResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CrossAccountResources(self):  # pragma: no cover
        return CrossAccountResource.make_many(
            self.boto3_raw_data["CrossAccountResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCrossAccountResourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCrossAccountResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomRoutingAcceleratorAttributesResponse:
    boto3_raw_data: (
        "type_defs.DescribeCustomRoutingAcceleratorAttributesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AcceleratorAttributes(self):  # pragma: no cover
        return CustomRoutingAcceleratorAttributes.make_one(
            self.boto3_raw_data["AcceleratorAttributes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomRoutingAcceleratorAttributesResponseTypeDef"
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
                "type_defs.DescribeCustomRoutingAcceleratorAttributesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomRoutingAcceleratorAttributesResponse:
    boto3_raw_data: (
        "type_defs.UpdateCustomRoutingAcceleratorAttributesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AcceleratorAttributes(self):  # pragma: no cover
        return CustomRoutingAcceleratorAttributes.make_one(
            self.boto3_raw_data["AcceleratorAttributes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomRoutingAcceleratorAttributesResponseTypeDef"
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
                "type_defs.UpdateCustomRoutingAcceleratorAttributesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomRoutingEndpointGroup:
    boto3_raw_data: "type_defs.CustomRoutingEndpointGroupTypeDef" = dataclasses.field()

    EndpointGroupArn = field("EndpointGroupArn")
    EndpointGroupRegion = field("EndpointGroupRegion")

    @cached_property
    def DestinationDescriptions(self):  # pragma: no cover
        return CustomRoutingDestinationDescription.make_many(
            self.boto3_raw_data["DestinationDescriptions"]
        )

    @cached_property
    def EndpointDescriptions(self):  # pragma: no cover
        return CustomRoutingEndpointDescription.make_many(
            self.boto3_raw_data["EndpointDescriptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomRoutingEndpointGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomRoutingEndpointGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationPortMapping:
    boto3_raw_data: "type_defs.DestinationPortMappingTypeDef" = dataclasses.field()

    AcceleratorArn = field("AcceleratorArn")

    @cached_property
    def AcceleratorSocketAddresses(self):  # pragma: no cover
        return SocketAddress.make_many(
            self.boto3_raw_data["AcceleratorSocketAddresses"]
        )

    EndpointGroupArn = field("EndpointGroupArn")
    EndpointId = field("EndpointId")
    EndpointGroupRegion = field("EndpointGroupRegion")

    @cached_property
    def DestinationSocketAddress(self):  # pragma: no cover
        return SocketAddress.make_one(self.boto3_raw_data["DestinationSocketAddress"])

    IpAddressType = field("IpAddressType")
    DestinationTrafficState = field("DestinationTrafficState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationPortMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationPortMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortMapping:
    boto3_raw_data: "type_defs.PortMappingTypeDef" = dataclasses.field()

    AcceleratorPort = field("AcceleratorPort")
    EndpointGroupArn = field("EndpointGroupArn")
    EndpointId = field("EndpointId")

    @cached_property
    def DestinationSocketAddress(self):  # pragma: no cover
        return SocketAddress.make_one(self.boto3_raw_data["DestinationSocketAddress"])

    Protocols = field("Protocols")
    DestinationTrafficState = field("DestinationTrafficState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortMappingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveEndpointsRequest:
    boto3_raw_data: "type_defs.RemoveEndpointsRequestTypeDef" = dataclasses.field()

    @cached_property
    def EndpointIdentifiers(self):  # pragma: no cover
        return EndpointIdentifier.make_many(self.boto3_raw_data["EndpointIdentifiers"])

    EndpointGroupArn = field("EndpointGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAcceleratorsRequestPaginate:
    boto3_raw_data: "type_defs.ListAcceleratorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAcceleratorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAcceleratorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListByoipCidrsRequestPaginate:
    boto3_raw_data: "type_defs.ListByoipCidrsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListByoipCidrsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListByoipCidrsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCrossAccountAttachmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListCrossAccountAttachmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCrossAccountAttachmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCrossAccountAttachmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCrossAccountResourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListCrossAccountResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceOwnerAwsAccountId = field("ResourceOwnerAwsAccountId")
    AcceleratorArn = field("AcceleratorArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCrossAccountResourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCrossAccountResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingAcceleratorsRequestPaginate:
    boto3_raw_data: "type_defs.ListCustomRoutingAcceleratorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingAcceleratorsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingAcceleratorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingEndpointGroupsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListCustomRoutingEndpointGroupsRequestPaginateTypeDef"
    ) = dataclasses.field()

    ListenerArn = field("ListenerArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingEndpointGroupsRequestPaginateTypeDef"
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
                "type_defs.ListCustomRoutingEndpointGroupsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingListenersRequestPaginate:
    boto3_raw_data: "type_defs.ListCustomRoutingListenersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingListenersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingListenersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingPortMappingsByDestinationRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListCustomRoutingPortMappingsByDestinationRequestPaginateTypeDef"
    ) = dataclasses.field()

    EndpointId = field("EndpointId")
    DestinationAddress = field("DestinationAddress")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingPortMappingsByDestinationRequestPaginateTypeDef"
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
                "type_defs.ListCustomRoutingPortMappingsByDestinationRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingPortMappingsRequestPaginate:
    boto3_raw_data: "type_defs.ListCustomRoutingPortMappingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")
    EndpointGroupArn = field("EndpointGroupArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingPortMappingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingPortMappingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListEndpointGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEndpointGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListListenersRequestPaginate:
    boto3_raw_data: "type_defs.ListListenersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AcceleratorArn = field("AcceleratorArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListListenersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListListenersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAcceleratorResponse:
    boto3_raw_data: "type_defs.CreateAcceleratorResponseTypeDef" = dataclasses.field()

    @cached_property
    def Accelerator(self):  # pragma: no cover
        return Accelerator.make_one(self.boto3_raw_data["Accelerator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAcceleratorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAcceleratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAcceleratorResponse:
    boto3_raw_data: "type_defs.DescribeAcceleratorResponseTypeDef" = dataclasses.field()

    @cached_property
    def Accelerator(self):  # pragma: no cover
        return Accelerator.make_one(self.boto3_raw_data["Accelerator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAcceleratorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAcceleratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAcceleratorsResponse:
    boto3_raw_data: "type_defs.ListAcceleratorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Accelerators(self):  # pragma: no cover
        return Accelerator.make_many(self.boto3_raw_data["Accelerators"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAcceleratorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAcceleratorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAcceleratorResponse:
    boto3_raw_data: "type_defs.UpdateAcceleratorResponseTypeDef" = dataclasses.field()

    @cached_property
    def Accelerator(self):  # pragma: no cover
        return Accelerator.make_one(self.boto3_raw_data["Accelerator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAcceleratorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAcceleratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomRoutingAcceleratorResponse:
    boto3_raw_data: "type_defs.CreateCustomRoutingAcceleratorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Accelerator(self):  # pragma: no cover
        return CustomRoutingAccelerator.make_one(self.boto3_raw_data["Accelerator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomRoutingAcceleratorResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomRoutingAcceleratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomRoutingAcceleratorResponse:
    boto3_raw_data: "type_defs.DescribeCustomRoutingAcceleratorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Accelerator(self):  # pragma: no cover
        return CustomRoutingAccelerator.make_one(self.boto3_raw_data["Accelerator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomRoutingAcceleratorResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomRoutingAcceleratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingAcceleratorsResponse:
    boto3_raw_data: "type_defs.ListCustomRoutingAcceleratorsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Accelerators(self):  # pragma: no cover
        return CustomRoutingAccelerator.make_many(self.boto3_raw_data["Accelerators"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingAcceleratorsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingAcceleratorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomRoutingAcceleratorResponse:
    boto3_raw_data: "type_defs.UpdateCustomRoutingAcceleratorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Accelerator(self):  # pragma: no cover
        return CustomRoutingAccelerator.make_one(self.boto3_raw_data["Accelerator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomRoutingAcceleratorResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomRoutingAcceleratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCrossAccountAttachmentResponse:
    boto3_raw_data: "type_defs.CreateCrossAccountAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CrossAccountAttachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["CrossAccountAttachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCrossAccountAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCrossAccountAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCrossAccountAttachmentResponse:
    boto3_raw_data: "type_defs.DescribeCrossAccountAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CrossAccountAttachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["CrossAccountAttachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCrossAccountAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCrossAccountAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCrossAccountAttachmentsResponse:
    boto3_raw_data: "type_defs.ListCrossAccountAttachmentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CrossAccountAttachments(self):  # pragma: no cover
        return Attachment.make_many(self.boto3_raw_data["CrossAccountAttachments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCrossAccountAttachmentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCrossAccountAttachmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCrossAccountAttachmentResponse:
    boto3_raw_data: "type_defs.UpdateCrossAccountAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CrossAccountAttachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["CrossAccountAttachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCrossAccountAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCrossAccountAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvertiseByoipCidrResponse:
    boto3_raw_data: "type_defs.AdvertiseByoipCidrResponseTypeDef" = dataclasses.field()

    @cached_property
    def ByoipCidr(self):  # pragma: no cover
        return ByoipCidr.make_one(self.boto3_raw_data["ByoipCidr"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvertiseByoipCidrResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvertiseByoipCidrResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeprovisionByoipCidrResponse:
    boto3_raw_data: "type_defs.DeprovisionByoipCidrResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ByoipCidr(self):  # pragma: no cover
        return ByoipCidr.make_one(self.boto3_raw_data["ByoipCidr"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeprovisionByoipCidrResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeprovisionByoipCidrResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListByoipCidrsResponse:
    boto3_raw_data: "type_defs.ListByoipCidrsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ByoipCidrs(self):  # pragma: no cover
        return ByoipCidr.make_many(self.boto3_raw_data["ByoipCidrs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListByoipCidrsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListByoipCidrsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionByoipCidrResponse:
    boto3_raw_data: "type_defs.ProvisionByoipCidrResponseTypeDef" = dataclasses.field()

    @cached_property
    def ByoipCidr(self):  # pragma: no cover
        return ByoipCidr.make_one(self.boto3_raw_data["ByoipCidr"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionByoipCidrResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionByoipCidrResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WithdrawByoipCidrResponse:
    boto3_raw_data: "type_defs.WithdrawByoipCidrResponseTypeDef" = dataclasses.field()

    @cached_property
    def ByoipCidr(self):  # pragma: no cover
        return ByoipCidr.make_one(self.boto3_raw_data["ByoipCidr"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WithdrawByoipCidrResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WithdrawByoipCidrResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomRoutingListenerResponse:
    boto3_raw_data: "type_defs.CreateCustomRoutingListenerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Listener(self):  # pragma: no cover
        return CustomRoutingListener.make_one(self.boto3_raw_data["Listener"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomRoutingListenerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomRoutingListenerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomRoutingListenerResponse:
    boto3_raw_data: "type_defs.DescribeCustomRoutingListenerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Listener(self):  # pragma: no cover
        return CustomRoutingListener.make_one(self.boto3_raw_data["Listener"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomRoutingListenerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomRoutingListenerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingListenersResponse:
    boto3_raw_data: "type_defs.ListCustomRoutingListenersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Listeners(self):  # pragma: no cover
        return CustomRoutingListener.make_many(self.boto3_raw_data["Listeners"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingListenersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingListenersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomRoutingListenerResponse:
    boto3_raw_data: "type_defs.UpdateCustomRoutingListenerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Listener(self):  # pragma: no cover
        return CustomRoutingListener.make_one(self.boto3_raw_data["Listener"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomRoutingListenerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomRoutingListenerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateListenerResponse:
    boto3_raw_data: "type_defs.CreateListenerResponseTypeDef" = dataclasses.field()

    @cached_property
    def Listener(self):  # pragma: no cover
        return Listener.make_one(self.boto3_raw_data["Listener"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateListenerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateListenerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeListenerResponse:
    boto3_raw_data: "type_defs.DescribeListenerResponseTypeDef" = dataclasses.field()

    @cached_property
    def Listener(self):  # pragma: no cover
        return Listener.make_one(self.boto3_raw_data["Listener"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeListenerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeListenerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListListenersResponse:
    boto3_raw_data: "type_defs.ListListenersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Listeners(self):  # pragma: no cover
        return Listener.make_many(self.boto3_raw_data["Listeners"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListListenersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListListenersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateListenerResponse:
    boto3_raw_data: "type_defs.UpdateListenerResponseTypeDef" = dataclasses.field()

    @cached_property
    def Listener(self):  # pragma: no cover
        return Listener.make_one(self.boto3_raw_data["Listener"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateListenerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateListenerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEndpointGroupResponse:
    boto3_raw_data: "type_defs.CreateEndpointGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointGroup(self):  # pragma: no cover
        return EndpointGroup.make_one(self.boto3_raw_data["EndpointGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointGroupResponse:
    boto3_raw_data: "type_defs.DescribeEndpointGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndpointGroup(self):  # pragma: no cover
        return EndpointGroup.make_one(self.boto3_raw_data["EndpointGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEndpointGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointGroupsResponse:
    boto3_raw_data: "type_defs.ListEndpointGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointGroups(self):  # pragma: no cover
        return EndpointGroup.make_many(self.boto3_raw_data["EndpointGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEndpointGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointGroupResponse:
    boto3_raw_data: "type_defs.UpdateEndpointGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointGroup(self):  # pragma: no cover
        return EndpointGroup.make_one(self.boto3_raw_data["EndpointGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomRoutingEndpointGroupResponse:
    boto3_raw_data: "type_defs.CreateCustomRoutingEndpointGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndpointGroup(self):  # pragma: no cover
        return CustomRoutingEndpointGroup.make_one(self.boto3_raw_data["EndpointGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomRoutingEndpointGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomRoutingEndpointGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomRoutingEndpointGroupResponse:
    boto3_raw_data: "type_defs.DescribeCustomRoutingEndpointGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndpointGroup(self):  # pragma: no cover
        return CustomRoutingEndpointGroup.make_one(self.boto3_raw_data["EndpointGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomRoutingEndpointGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomRoutingEndpointGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingEndpointGroupsResponse:
    boto3_raw_data: "type_defs.ListCustomRoutingEndpointGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndpointGroups(self):  # pragma: no cover
        return CustomRoutingEndpointGroup.make_many(
            self.boto3_raw_data["EndpointGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingEndpointGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingEndpointGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingPortMappingsByDestinationResponse:
    boto3_raw_data: (
        "type_defs.ListCustomRoutingPortMappingsByDestinationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def DestinationPortMappings(self):  # pragma: no cover
        return DestinationPortMapping.make_many(
            self.boto3_raw_data["DestinationPortMappings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingPortMappingsByDestinationResponseTypeDef"
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
                "type_defs.ListCustomRoutingPortMappingsByDestinationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomRoutingPortMappingsResponse:
    boto3_raw_data: "type_defs.ListCustomRoutingPortMappingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PortMappings(self):  # pragma: no cover
        return PortMapping.make_many(self.boto3_raw_data["PortMappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomRoutingPortMappingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomRoutingPortMappingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
