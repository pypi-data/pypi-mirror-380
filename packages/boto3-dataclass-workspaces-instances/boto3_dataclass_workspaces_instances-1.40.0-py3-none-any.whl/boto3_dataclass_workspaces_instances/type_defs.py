# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workspaces_instances import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssociateVolumeRequest:
    boto3_raw_data: "type_defs.AssociateVolumeRequestTypeDef" = dataclasses.field()

    WorkspaceInstanceId = field("WorkspaceInstanceId")
    VolumeId = field("VolumeId")
    Device = field("Device")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsBlockDevice:
    boto3_raw_data: "type_defs.EbsBlockDeviceTypeDef" = dataclasses.field()

    VolumeType = field("VolumeType")
    Encrypted = field("Encrypted")
    KmsKeyId = field("KmsKeyId")
    Iops = field("Iops")
    Throughput = field("Throughput")
    VolumeSize = field("VolumeSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EbsBlockDeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EbsBlockDeviceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityReservationTarget:
    boto3_raw_data: "type_defs.CapacityReservationTargetTypeDef" = dataclasses.field()

    CapacityReservationId = field("CapacityReservationId")
    CapacityReservationResourceGroupArn = field("CapacityReservationResourceGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityReservationTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityReservationTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionTrackingSpecificationRequest:
    boto3_raw_data: "type_defs.ConnectionTrackingSpecificationRequestTypeDef" = (
        dataclasses.field()
    )

    TcpEstablishedTimeout = field("TcpEstablishedTimeout")
    UdpStreamTimeout = field("UdpStreamTimeout")
    UdpTimeout = field("UdpTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConnectionTrackingSpecificationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionTrackingSpecificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CpuOptionsRequest:
    boto3_raw_data: "type_defs.CpuOptionsRequestTypeDef" = dataclasses.field()

    AmdSevSnp = field("AmdSevSnp")
    CoreCount = field("CoreCount")
    ThreadsPerCore = field("ThreadsPerCore")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CpuOptionsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CpuOptionsRequestTypeDef"]
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
class CreditSpecificationRequest:
    boto3_raw_data: "type_defs.CreditSpecificationRequestTypeDef" = dataclasses.field()

    CpuCredits = field("CpuCredits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreditSpecificationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreditSpecificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVolumeRequest:
    boto3_raw_data: "type_defs.DeleteVolumeRequestTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceInstanceRequest:
    boto3_raw_data: "type_defs.DeleteWorkspaceInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    WorkspaceInstanceId = field("WorkspaceInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteWorkspaceInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateVolumeRequest:
    boto3_raw_data: "type_defs.DisassociateVolumeRequestTypeDef" = dataclasses.field()

    WorkspaceInstanceId = field("WorkspaceInstanceId")
    VolumeId = field("VolumeId")
    Device = field("Device")
    DisassociateMode = field("DisassociateMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2InstanceError:
    boto3_raw_data: "type_defs.EC2InstanceErrorTypeDef" = dataclasses.field()

    EC2ErrorCode = field("EC2ErrorCode")
    EC2ExceptionType = field("EC2ExceptionType")
    EC2ErrorMessage = field("EC2ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EC2InstanceErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2InstanceErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2ManagedInstance:
    boto3_raw_data: "type_defs.EC2ManagedInstanceTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EC2ManagedInstanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2ManagedInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnaSrdUdpSpecificationRequest:
    boto3_raw_data: "type_defs.EnaSrdUdpSpecificationRequestTypeDef" = (
        dataclasses.field()
    )

    EnaSrdUdpEnabled = field("EnaSrdUdpEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnaSrdUdpSpecificationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnaSrdUdpSpecificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnclaveOptionsRequest:
    boto3_raw_data: "type_defs.EnclaveOptionsRequestTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnclaveOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnclaveOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkspaceInstanceRequest:
    boto3_raw_data: "type_defs.GetWorkspaceInstanceRequestTypeDef" = dataclasses.field()

    WorkspaceInstanceId = field("WorkspaceInstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkspaceInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkspaceInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceInstanceError:
    boto3_raw_data: "type_defs.WorkspaceInstanceErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspaceInstanceErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceInstanceErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HibernationOptionsRequest:
    boto3_raw_data: "type_defs.HibernationOptionsRequestTypeDef" = dataclasses.field()

    Configured = field("Configured")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HibernationOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HibernationOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamInstanceProfileSpecification:
    boto3_raw_data: "type_defs.IamInstanceProfileSpecificationTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IamInstanceProfileSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamInstanceProfileSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceIpv6Address:
    boto3_raw_data: "type_defs.InstanceIpv6AddressTypeDef" = dataclasses.field()

    Ipv6Address = field("Ipv6Address")
    IsPrimaryIpv6 = field("IsPrimaryIpv6")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceIpv6AddressTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceIpv6AddressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceMaintenanceOptionsRequest:
    boto3_raw_data: "type_defs.InstanceMaintenanceOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    AutoRecovery = field("AutoRecovery")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceMaintenanceOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceMaintenanceOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceMetadataOptionsRequest:
    boto3_raw_data: "type_defs.InstanceMetadataOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    HttpEndpoint = field("HttpEndpoint")
    HttpProtocolIpv6 = field("HttpProtocolIpv6")
    HttpPutResponseHopLimit = field("HttpPutResponseHopLimit")
    HttpTokens = field("HttpTokens")
    InstanceMetadataTags = field("InstanceMetadataTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InstanceMetadataOptionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceMetadataOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ipv4PrefixSpecificationRequest:
    boto3_raw_data: "type_defs.Ipv4PrefixSpecificationRequestTypeDef" = (
        dataclasses.field()
    )

    Ipv4Prefix = field("Ipv4Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.Ipv4PrefixSpecificationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ipv4PrefixSpecificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ipv6PrefixSpecificationRequest:
    boto3_raw_data: "type_defs.Ipv6PrefixSpecificationRequestTypeDef" = (
        dataclasses.field()
    )

    Ipv6Prefix = field("Ipv6Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.Ipv6PrefixSpecificationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ipv6PrefixSpecificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateIpAddressSpecification:
    boto3_raw_data: "type_defs.PrivateIpAddressSpecificationTypeDef" = (
        dataclasses.field()
    )

    Primary = field("Primary")
    PrivateIpAddress = field("PrivateIpAddress")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PrivateIpAddressSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateIpAddressSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceNetworkPerformanceOptionsRequest:
    boto3_raw_data: "type_defs.InstanceNetworkPerformanceOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    BandwidthWeighting = field("BandwidthWeighting")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceNetworkPerformanceOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceNetworkPerformanceOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceTypeInfo:
    boto3_raw_data: "type_defs.InstanceTypeInfoTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceTypeInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseConfigurationRequest:
    boto3_raw_data: "type_defs.LicenseConfigurationRequestTypeDef" = dataclasses.field()

    LicenseConfigurationArn = field("LicenseConfigurationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseConfigurationRequestTypeDef"]
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
class ListInstanceTypesRequest:
    boto3_raw_data: "type_defs.ListInstanceTypesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstanceTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRegionsRequest:
    boto3_raw_data: "type_defs.ListRegionsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRegionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRegionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Region:
    boto3_raw_data: "type_defs.RegionTypeDef" = dataclasses.field()

    RegionName = field("RegionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    WorkspaceInstanceId = field("WorkspaceInstanceId")

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
class ListWorkspaceInstancesRequest:
    boto3_raw_data: "type_defs.ListWorkspaceInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    ProvisionStates = field("ProvisionStates")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkspaceInstancesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspaceInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Placement:
    boto3_raw_data: "type_defs.PlacementTypeDef" = dataclasses.field()

    Affinity = field("Affinity")
    AvailabilityZone = field("AvailabilityZone")
    GroupId = field("GroupId")
    GroupName = field("GroupName")
    HostId = field("HostId")
    HostResourceGroupArn = field("HostResourceGroupArn")
    PartitionNumber = field("PartitionNumber")
    Tenancy = field("Tenancy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlacementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlacementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateDnsNameOptionsRequest:
    boto3_raw_data: "type_defs.PrivateDnsNameOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    HostnameType = field("HostnameType")
    EnableResourceNameDnsARecord = field("EnableResourceNameDnsARecord")
    EnableResourceNameDnsAAAARecord = field("EnableResourceNameDnsAAAARecord")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateDnsNameOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateDnsNameOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunInstancesMonitoringEnabled:
    boto3_raw_data: "type_defs.RunInstancesMonitoringEnabledTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RunInstancesMonitoringEnabledTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunInstancesMonitoringEnabledTypeDef"]
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

    WorkspaceInstanceId = field("WorkspaceInstanceId")
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
class BlockDeviceMappingRequest:
    boto3_raw_data: "type_defs.BlockDeviceMappingRequestTypeDef" = dataclasses.field()

    DeviceName = field("DeviceName")

    @cached_property
    def Ebs(self):  # pragma: no cover
        return EbsBlockDevice.make_one(self.boto3_raw_data["Ebs"])

    NoDevice = field("NoDevice")
    VirtualName = field("VirtualName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BlockDeviceMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockDeviceMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityReservationSpecification:
    boto3_raw_data: "type_defs.CapacityReservationSpecificationTypeDef" = (
        dataclasses.field()
    )

    CapacityReservationPreference = field("CapacityReservationPreference")

    @cached_property
    def CapacityReservationTarget(self):  # pragma: no cover
        return CapacityReservationTarget.make_one(
            self.boto3_raw_data["CapacityReservationTarget"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CapacityReservationSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityReservationSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVolumeResponse:
    boto3_raw_data: "type_defs.CreateVolumeResponseTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVolumeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVolumeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceInstanceResponse:
    boto3_raw_data: "type_defs.CreateWorkspaceInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    WorkspaceInstanceId = field("WorkspaceInstanceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkspaceInstanceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceInstanceResponseTypeDef"]
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

    WorkspaceInstanceId = field("WorkspaceInstanceId")

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
class TagSpecification:
    boto3_raw_data: "type_defs.TagSpecificationTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagSpecificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceInstance:
    boto3_raw_data: "type_defs.WorkspaceInstanceTypeDef" = dataclasses.field()

    ProvisionState = field("ProvisionState")
    WorkspaceInstanceId = field("WorkspaceInstanceId")

    @cached_property
    def EC2ManagedInstance(self):  # pragma: no cover
        return EC2ManagedInstance.make_one(self.boto3_raw_data["EC2ManagedInstance"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkspaceInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnaSrdSpecificationRequest:
    boto3_raw_data: "type_defs.EnaSrdSpecificationRequestTypeDef" = dataclasses.field()

    EnaSrdEnabled = field("EnaSrdEnabled")

    @cached_property
    def EnaSrdUdpSpecification(self):  # pragma: no cover
        return EnaSrdUdpSpecificationRequest.make_one(
            self.boto3_raw_data["EnaSrdUdpSpecification"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnaSrdSpecificationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnaSrdSpecificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkspaceInstanceResponse:
    boto3_raw_data: "type_defs.GetWorkspaceInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WorkspaceInstanceErrors(self):  # pragma: no cover
        return WorkspaceInstanceError.make_many(
            self.boto3_raw_data["WorkspaceInstanceErrors"]
        )

    @cached_property
    def EC2InstanceErrors(self):  # pragma: no cover
        return EC2InstanceError.make_many(self.boto3_raw_data["EC2InstanceErrors"])

    ProvisionState = field("ProvisionState")
    WorkspaceInstanceId = field("WorkspaceInstanceId")

    @cached_property
    def EC2ManagedInstance(self):  # pragma: no cover
        return EC2ManagedInstance.make_one(self.boto3_raw_data["EC2ManagedInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkspaceInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkspaceInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceTypesResponse:
    boto3_raw_data: "type_defs.ListInstanceTypesResponseTypeDef" = dataclasses.field()

    @cached_property
    def InstanceTypes(self):  # pragma: no cover
        return InstanceTypeInfo.make_many(self.boto3_raw_data["InstanceTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstanceTypesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceTypesRequestPaginate:
    boto3_raw_data: "type_defs.ListInstanceTypesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstanceTypesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceTypesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRegionsRequestPaginate:
    boto3_raw_data: "type_defs.ListRegionsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRegionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRegionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspaceInstancesRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkspaceInstancesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ProvisionStates = field("ProvisionStates")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkspaceInstancesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspaceInstancesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRegionsResponse:
    boto3_raw_data: "type_defs.ListRegionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Regions(self):  # pragma: no cover
        return Region.make_many(self.boto3_raw_data["Regions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRegionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRegionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpotMarketOptions:
    boto3_raw_data: "type_defs.SpotMarketOptionsTypeDef" = dataclasses.field()

    BlockDurationMinutes = field("BlockDurationMinutes")
    InstanceInterruptionBehavior = field("InstanceInterruptionBehavior")
    MaxPrice = field("MaxPrice")
    SpotInstanceType = field("SpotInstanceType")
    ValidUntilUtc = field("ValidUntilUtc")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpotMarketOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpotMarketOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVolumeRequest:
    boto3_raw_data: "type_defs.CreateVolumeRequestTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")
    ClientToken = field("ClientToken")
    Encrypted = field("Encrypted")
    Iops = field("Iops")
    KmsKeyId = field("KmsKeyId")
    SizeInGB = field("SizeInGB")
    SnapshotId = field("SnapshotId")

    @cached_property
    def TagSpecifications(self):  # pragma: no cover
        return TagSpecification.make_many(self.boto3_raw_data["TagSpecifications"])

    Throughput = field("Throughput")
    VolumeType = field("VolumeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspaceInstancesResponse:
    boto3_raw_data: "type_defs.ListWorkspaceInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WorkspaceInstances(self):  # pragma: no cover
        return WorkspaceInstance.make_many(self.boto3_raw_data["WorkspaceInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkspaceInstancesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspaceInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceNetworkInterfaceSpecification:
    boto3_raw_data: "type_defs.InstanceNetworkInterfaceSpecificationTypeDef" = (
        dataclasses.field()
    )

    AssociateCarrierIpAddress = field("AssociateCarrierIpAddress")
    AssociatePublicIpAddress = field("AssociatePublicIpAddress")

    @cached_property
    def ConnectionTrackingSpecification(self):  # pragma: no cover
        return ConnectionTrackingSpecificationRequest.make_one(
            self.boto3_raw_data["ConnectionTrackingSpecification"]
        )

    Description = field("Description")
    DeviceIndex = field("DeviceIndex")

    @cached_property
    def EnaSrdSpecification(self):  # pragma: no cover
        return EnaSrdSpecificationRequest.make_one(
            self.boto3_raw_data["EnaSrdSpecification"]
        )

    InterfaceType = field("InterfaceType")

    @cached_property
    def Ipv4Prefixes(self):  # pragma: no cover
        return Ipv4PrefixSpecificationRequest.make_many(
            self.boto3_raw_data["Ipv4Prefixes"]
        )

    Ipv4PrefixCount = field("Ipv4PrefixCount")
    Ipv6AddressCount = field("Ipv6AddressCount")

    @cached_property
    def Ipv6Addresses(self):  # pragma: no cover
        return InstanceIpv6Address.make_many(self.boto3_raw_data["Ipv6Addresses"])

    @cached_property
    def Ipv6Prefixes(self):  # pragma: no cover
        return Ipv6PrefixSpecificationRequest.make_many(
            self.boto3_raw_data["Ipv6Prefixes"]
        )

    Ipv6PrefixCount = field("Ipv6PrefixCount")
    NetworkCardIndex = field("NetworkCardIndex")
    NetworkInterfaceId = field("NetworkInterfaceId")
    PrimaryIpv6 = field("PrimaryIpv6")
    PrivateIpAddress = field("PrivateIpAddress")

    @cached_property
    def PrivateIpAddresses(self):  # pragma: no cover
        return PrivateIpAddressSpecification.make_many(
            self.boto3_raw_data["PrivateIpAddresses"]
        )

    SecondaryPrivateIpAddressCount = field("SecondaryPrivateIpAddressCount")
    Groups = field("Groups")
    SubnetId = field("SubnetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceNetworkInterfaceSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceNetworkInterfaceSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceMarketOptionsRequest:
    boto3_raw_data: "type_defs.InstanceMarketOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    MarketType = field("MarketType")

    @cached_property
    def SpotOptions(self):  # pragma: no cover
        return SpotMarketOptions.make_one(self.boto3_raw_data["SpotOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceMarketOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceMarketOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedInstanceRequest:
    boto3_raw_data: "type_defs.ManagedInstanceRequestTypeDef" = dataclasses.field()

    @cached_property
    def BlockDeviceMappings(self):  # pragma: no cover
        return BlockDeviceMappingRequest.make_many(
            self.boto3_raw_data["BlockDeviceMappings"]
        )

    @cached_property
    def CapacityReservationSpecification(self):  # pragma: no cover
        return CapacityReservationSpecification.make_one(
            self.boto3_raw_data["CapacityReservationSpecification"]
        )

    @cached_property
    def CpuOptions(self):  # pragma: no cover
        return CpuOptionsRequest.make_one(self.boto3_raw_data["CpuOptions"])

    @cached_property
    def CreditSpecification(self):  # pragma: no cover
        return CreditSpecificationRequest.make_one(
            self.boto3_raw_data["CreditSpecification"]
        )

    DisableApiStop = field("DisableApiStop")
    EbsOptimized = field("EbsOptimized")
    EnablePrimaryIpv6 = field("EnablePrimaryIpv6")

    @cached_property
    def EnclaveOptions(self):  # pragma: no cover
        return EnclaveOptionsRequest.make_one(self.boto3_raw_data["EnclaveOptions"])

    @cached_property
    def HibernationOptions(self):  # pragma: no cover
        return HibernationOptionsRequest.make_one(
            self.boto3_raw_data["HibernationOptions"]
        )

    @cached_property
    def IamInstanceProfile(self):  # pragma: no cover
        return IamInstanceProfileSpecification.make_one(
            self.boto3_raw_data["IamInstanceProfile"]
        )

    ImageId = field("ImageId")

    @cached_property
    def InstanceMarketOptions(self):  # pragma: no cover
        return InstanceMarketOptionsRequest.make_one(
            self.boto3_raw_data["InstanceMarketOptions"]
        )

    InstanceType = field("InstanceType")

    @cached_property
    def Ipv6Addresses(self):  # pragma: no cover
        return InstanceIpv6Address.make_many(self.boto3_raw_data["Ipv6Addresses"])

    Ipv6AddressCount = field("Ipv6AddressCount")
    KernelId = field("KernelId")
    KeyName = field("KeyName")

    @cached_property
    def LicenseSpecifications(self):  # pragma: no cover
        return LicenseConfigurationRequest.make_many(
            self.boto3_raw_data["LicenseSpecifications"]
        )

    @cached_property
    def MaintenanceOptions(self):  # pragma: no cover
        return InstanceMaintenanceOptionsRequest.make_one(
            self.boto3_raw_data["MaintenanceOptions"]
        )

    @cached_property
    def MetadataOptions(self):  # pragma: no cover
        return InstanceMetadataOptionsRequest.make_one(
            self.boto3_raw_data["MetadataOptions"]
        )

    @cached_property
    def Monitoring(self):  # pragma: no cover
        return RunInstancesMonitoringEnabled.make_one(self.boto3_raw_data["Monitoring"])

    @cached_property
    def NetworkInterfaces(self):  # pragma: no cover
        return InstanceNetworkInterfaceSpecification.make_many(
            self.boto3_raw_data["NetworkInterfaces"]
        )

    @cached_property
    def NetworkPerformanceOptions(self):  # pragma: no cover
        return InstanceNetworkPerformanceOptionsRequest.make_one(
            self.boto3_raw_data["NetworkPerformanceOptions"]
        )

    @cached_property
    def Placement(self):  # pragma: no cover
        return Placement.make_one(self.boto3_raw_data["Placement"])

    @cached_property
    def PrivateDnsNameOptions(self):  # pragma: no cover
        return PrivateDnsNameOptionsRequest.make_one(
            self.boto3_raw_data["PrivateDnsNameOptions"]
        )

    PrivateIpAddress = field("PrivateIpAddress")
    RamdiskId = field("RamdiskId")
    SecurityGroupIds = field("SecurityGroupIds")
    SecurityGroups = field("SecurityGroups")
    SubnetId = field("SubnetId")

    @cached_property
    def TagSpecifications(self):  # pragma: no cover
        return TagSpecification.make_many(self.boto3_raw_data["TagSpecifications"])

    UserData = field("UserData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceInstanceRequest:
    boto3_raw_data: "type_defs.CreateWorkspaceInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedInstance(self):  # pragma: no cover
        return ManagedInstanceRequest.make_one(self.boto3_raw_data["ManagedInstance"])

    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkspaceInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
