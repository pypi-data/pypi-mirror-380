# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_groundstation import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ComponentVersion:
    boto3_raw_data: "type_defs.ComponentVersionTypeDef" = dataclasses.field()

    componentType = field("componentType")
    versions = field("versions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateStatus:
    boto3_raw_data: "type_defs.AggregateStatusTypeDef" = dataclasses.field()

    status = field("status")
    signatureMap = field("signatureMap")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AggregateStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AggregateStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AntennaDemodDecodeDetails:
    boto3_raw_data: "type_defs.AntennaDemodDecodeDetailsTypeDef" = dataclasses.field()

    outputNode = field("outputNode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AntennaDemodDecodeDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AntennaDemodDecodeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecodeConfig:
    boto3_raw_data: "type_defs.DecodeConfigTypeDef" = dataclasses.field()

    unvalidatedJSON = field("unvalidatedJSON")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DecodeConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DecodeConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DemodulationConfig:
    boto3_raw_data: "type_defs.DemodulationConfigTypeDef" = dataclasses.field()

    unvalidatedJSON = field("unvalidatedJSON")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DemodulationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DemodulationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Eirp:
    boto3_raw_data: "type_defs.EirpTypeDef" = dataclasses.field()

    units = field("units")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EirpTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EirpTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelContactRequest:
    boto3_raw_data: "type_defs.CancelContactRequestTypeDef" = dataclasses.field()

    contactId = field("contactId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentStatusData:
    boto3_raw_data: "type_defs.ComponentStatusDataTypeDef" = dataclasses.field()

    capabilityArn = field("capabilityArn")
    componentType = field("componentType")
    dataflowId = field("dataflowId")
    status = field("status")
    bytesReceived = field("bytesReceived")
    bytesSent = field("bytesSent")
    packetsDropped = field("packetsDropped")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentStatusDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentStatusDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3RecordingDetails:
    boto3_raw_data: "type_defs.S3RecordingDetailsTypeDef" = dataclasses.field()

    bucketArn = field("bucketArn")
    keyTemplate = field("keyTemplate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3RecordingDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3RecordingDetailsTypeDef"]
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
class ConfigListItem:
    boto3_raw_data: "type_defs.ConfigListItemTypeDef" = dataclasses.field()

    configArn = field("configArn")
    configId = field("configId")
    configType = field("configType")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigListItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataflowEndpointConfig:
    boto3_raw_data: "type_defs.DataflowEndpointConfigTypeDef" = dataclasses.field()

    dataflowEndpointName = field("dataflowEndpointName")
    dataflowEndpointRegion = field("dataflowEndpointRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataflowEndpointConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataflowEndpointConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3RecordingConfig:
    boto3_raw_data: "type_defs.S3RecordingConfigTypeDef" = dataclasses.field()

    bucketArn = field("bucketArn")
    roleArn = field("roleArn")
    prefix = field("prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3RecordingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3RecordingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrackingConfig:
    boto3_raw_data: "type_defs.TrackingConfigTypeDef" = dataclasses.field()

    autotrack = field("autotrack")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrackingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrackingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UplinkEchoConfig:
    boto3_raw_data: "type_defs.UplinkEchoConfigTypeDef" = dataclasses.field()

    antennaUplinkConfigArn = field("antennaUplinkConfigArn")
    enabled = field("enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UplinkEchoConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UplinkEchoConfigTypeDef"]
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

    name = field("name")
    port = field("port")

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
class Elevation:
    boto3_raw_data: "type_defs.ElevationTypeDef" = dataclasses.field()

    unit = field("unit")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ElevationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ElevationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KmsKey:
    boto3_raw_data: "type_defs.KmsKeyTypeDef" = dataclasses.field()

    kmsAliasArn = field("kmsAliasArn")
    kmsAliasName = field("kmsAliasName")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KmsKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KmsKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataflowEndpointListItem:
    boto3_raw_data: "type_defs.DataflowEndpointListItemTypeDef" = dataclasses.field()

    dataflowEndpointGroupArn = field("dataflowEndpointGroupArn")
    dataflowEndpointGroupId = field("dataflowEndpointGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataflowEndpointListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataflowEndpointListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigRequest:
    boto3_raw_data: "type_defs.DeleteConfigRequestTypeDef" = dataclasses.field()

    configId = field("configId")
    configType = field("configType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataflowEndpointGroupRequest:
    boto3_raw_data: "type_defs.DeleteDataflowEndpointGroupRequestTypeDef" = (
        dataclasses.field()
    )

    dataflowEndpointGroupId = field("dataflowEndpointGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDataflowEndpointGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataflowEndpointGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEphemerisRequest:
    boto3_raw_data: "type_defs.DeleteEphemerisRequestTypeDef" = dataclasses.field()

    ephemerisId = field("ephemerisId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEphemerisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEphemerisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMissionProfileRequest:
    boto3_raw_data: "type_defs.DeleteMissionProfileRequestTypeDef" = dataclasses.field()

    missionProfileId = field("missionProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMissionProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMissionProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactRequest:
    boto3_raw_data: "type_defs.DescribeContactRequestTypeDef" = dataclasses.field()

    contactId = field("contactId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactRequestTypeDef"]
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
class DescribeEphemerisRequest:
    boto3_raw_data: "type_defs.DescribeEphemerisRequestTypeDef" = dataclasses.field()

    ephemerisId = field("ephemerisId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEphemerisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEphemerisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscoveryData:
    boto3_raw_data: "type_defs.DiscoveryDataTypeDef" = dataclasses.field()

    capabilityArns = field("capabilityArns")
    privateIpAddresses = field("privateIpAddresses")
    publicIpAddresses = field("publicIpAddresses")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DiscoveryDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DiscoveryDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityDetailsOutput:
    boto3_raw_data: "type_defs.SecurityDetailsOutputTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    securityGroupIds = field("securityGroupIds")
    subnetIds = field("subnetIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Object:
    boto3_raw_data: "type_defs.S3ObjectTypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EphemerisMetaData:
    boto3_raw_data: "type_defs.EphemerisMetaDataTypeDef" = dataclasses.field()

    source = field("source")
    ephemerisId = field("ephemerisId")
    epoch = field("epoch")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EphemerisMetaDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EphemerisMetaDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrequencyBandwidth:
    boto3_raw_data: "type_defs.FrequencyBandwidthTypeDef" = dataclasses.field()

    units = field("units")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FrequencyBandwidthTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrequencyBandwidthTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Frequency:
    boto3_raw_data: "type_defs.FrequencyTypeDef" = dataclasses.field()

    units = field("units")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrequencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FrequencyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentConfigurationRequest:
    boto3_raw_data: "type_defs.GetAgentConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigRequest:
    boto3_raw_data: "type_defs.GetConfigRequestTypeDef" = dataclasses.field()

    configId = field("configId")
    configType = field("configType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetConfigRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataflowEndpointGroupRequest:
    boto3_raw_data: "type_defs.GetDataflowEndpointGroupRequestTypeDef" = (
        dataclasses.field()
    )

    dataflowEndpointGroupId = field("dataflowEndpointGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataflowEndpointGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataflowEndpointGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMinuteUsageRequest:
    boto3_raw_data: "type_defs.GetMinuteUsageRequestTypeDef" = dataclasses.field()

    month = field("month")
    year = field("year")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMinuteUsageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMinuteUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMissionProfileRequest:
    boto3_raw_data: "type_defs.GetMissionProfileRequestTypeDef" = dataclasses.field()

    missionProfileId = field("missionProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMissionProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMissionProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSatelliteRequest:
    boto3_raw_data: "type_defs.GetSatelliteRequestTypeDef" = dataclasses.field()

    satelliteId = field("satelliteId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSatelliteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSatelliteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroundStationData:
    boto3_raw_data: "type_defs.GroundStationDataTypeDef" = dataclasses.field()

    groundStationId = field("groundStationId")
    groundStationName = field("groundStationName")
    region = field("region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroundStationDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroundStationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegerRange:
    boto3_raw_data: "type_defs.IntegerRangeTypeDef" = dataclasses.field()

    maximum = field("maximum")
    minimum = field("minimum")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntegerRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntegerRangeTypeDef"]],
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
class ListConfigsRequest:
    boto3_raw_data: "type_defs.ListConfigsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfigsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataflowEndpointGroupsRequest:
    boto3_raw_data: "type_defs.ListDataflowEndpointGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataflowEndpointGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataflowEndpointGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroundStationsRequest:
    boto3_raw_data: "type_defs.ListGroundStationsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    satelliteId = field("satelliteId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroundStationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroundStationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMissionProfilesRequest:
    boto3_raw_data: "type_defs.ListMissionProfilesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMissionProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMissionProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MissionProfileListItem:
    boto3_raw_data: "type_defs.MissionProfileListItemTypeDef" = dataclasses.field()

    missionProfileArn = field("missionProfileArn")
    missionProfileId = field("missionProfileId")
    name = field("name")
    region = field("region")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MissionProfileListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MissionProfileListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSatellitesRequest:
    boto3_raw_data: "type_defs.ListSatellitesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSatellitesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSatellitesRequestTypeDef"]
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

    resourceArn = field("resourceArn")

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
class SecurityDetails:
    boto3_raw_data: "type_defs.SecurityDetailsTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    securityGroupIds = field("securityGroupIds")
    subnetIds = field("subnetIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SecurityDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SecurityDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tags = field("tags")

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

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class UpdateEphemerisRequest:
    boto3_raw_data: "type_defs.UpdateEphemerisRequestTypeDef" = dataclasses.field()

    enabled = field("enabled")
    ephemerisId = field("ephemerisId")
    name = field("name")
    priority = field("priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEphemerisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEphemerisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentDetails:
    boto3_raw_data: "type_defs.AgentDetailsTypeDef" = dataclasses.field()

    agentVersion = field("agentVersion")

    @cached_property
    def componentVersions(self):  # pragma: no cover
        return ComponentVersion.make_many(self.boto3_raw_data["componentVersions"])

    instanceId = field("instanceId")
    instanceType = field("instanceType")
    agentCpuCores = field("agentCpuCores")
    reservedCpuCores = field("reservedCpuCores")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentStatusRequest:
    boto3_raw_data: "type_defs.UpdateAgentStatusRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")

    @cached_property
    def aggregateStatus(self):  # pragma: no cover
        return AggregateStatus.make_one(self.boto3_raw_data["aggregateStatus"])

    @cached_property
    def componentStatuses(self):  # pragma: no cover
        return ComponentStatusData.make_many(self.boto3_raw_data["componentStatuses"])

    taskId = field("taskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgentStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigIdResponse:
    boto3_raw_data: "type_defs.ConfigIdResponseTypeDef" = dataclasses.field()

    configArn = field("configArn")
    configId = field("configId")
    configType = field("configType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigIdResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactIdResponse:
    boto3_raw_data: "type_defs.ContactIdResponseTypeDef" = dataclasses.field()

    contactId = field("contactId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactIdResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataflowEndpointGroupIdResponse:
    boto3_raw_data: "type_defs.DataflowEndpointGroupIdResponseTypeDef" = (
        dataclasses.field()
    )

    dataflowEndpointGroupId = field("dataflowEndpointGroupId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataflowEndpointGroupIdResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataflowEndpointGroupIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EphemerisIdResponse:
    boto3_raw_data: "type_defs.EphemerisIdResponseTypeDef" = dataclasses.field()

    ephemerisId = field("ephemerisId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EphemerisIdResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EphemerisIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentConfigurationResponse:
    boto3_raw_data: "type_defs.GetAgentConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    taskingDocument = field("taskingDocument")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAgentConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMinuteUsageResponse:
    boto3_raw_data: "type_defs.GetMinuteUsageResponseTypeDef" = dataclasses.field()

    estimatedMinutesRemaining = field("estimatedMinutesRemaining")
    isReservedMinutesCustomer = field("isReservedMinutesCustomer")
    totalReservedMinuteAllocation = field("totalReservedMinuteAllocation")
    totalScheduledMinutes = field("totalScheduledMinutes")
    upcomingMinutesScheduled = field("upcomingMinutesScheduled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMinuteUsageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMinuteUsageResponseTypeDef"]
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

    tags = field("tags")

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
class MissionProfileIdResponse:
    boto3_raw_data: "type_defs.MissionProfileIdResponseTypeDef" = dataclasses.field()

    missionProfileId = field("missionProfileId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MissionProfileIdResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MissionProfileIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterAgentResponse:
    boto3_raw_data: "type_defs.RegisterAgentResponseTypeDef" = dataclasses.field()

    agentId = field("agentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentStatusResponse:
    boto3_raw_data: "type_defs.UpdateAgentStatusResponseTypeDef" = dataclasses.field()

    agentId = field("agentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgentStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigsResponse:
    boto3_raw_data: "type_defs.ListConfigsResponseTypeDef" = dataclasses.field()

    @cached_property
    def configList(self):  # pragma: no cover
        return ConfigListItem.make_many(self.boto3_raw_data["configList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfigsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionDetails:
    boto3_raw_data: "type_defs.ConnectionDetailsTypeDef" = dataclasses.field()

    @cached_property
    def socketAddress(self):  # pragma: no cover
        return SocketAddress.make_one(self.boto3_raw_data["socketAddress"])

    mtu = field("mtu")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataflowEndpoint:
    boto3_raw_data: "type_defs.DataflowEndpointTypeDef" = dataclasses.field()

    @cached_property
    def address(self):  # pragma: no cover
        return SocketAddress.make_one(self.boto3_raw_data["address"])

    mtu = field("mtu")
    name = field("name")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataflowEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataflowEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactData:
    boto3_raw_data: "type_defs.ContactDataTypeDef" = dataclasses.field()

    contactId = field("contactId")
    contactStatus = field("contactStatus")
    endTime = field("endTime")
    errorMessage = field("errorMessage")
    groundStation = field("groundStation")

    @cached_property
    def maximumElevation(self):  # pragma: no cover
        return Elevation.make_one(self.boto3_raw_data["maximumElevation"])

    missionProfileArn = field("missionProfileArn")
    postPassEndTime = field("postPassEndTime")
    prePassStartTime = field("prePassStartTime")
    region = field("region")
    satelliteArn = field("satelliteArn")
    startTime = field("startTime")
    tags = field("tags")
    visibilityEndTime = field("visibilityEndTime")
    visibilityStartTime = field("visibilityStartTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactsRequest:
    boto3_raw_data: "type_defs.ListContactsRequestTypeDef" = dataclasses.field()

    endTime = field("endTime")
    startTime = field("startTime")
    statusList = field("statusList")
    groundStation = field("groundStation")
    maxResults = field("maxResults")
    missionProfileArn = field("missionProfileArn")
    nextToken = field("nextToken")
    satelliteArn = field("satelliteArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEphemeridesRequest:
    boto3_raw_data: "type_defs.ListEphemeridesRequestTypeDef" = dataclasses.field()

    endTime = field("endTime")
    satelliteId = field("satelliteId")
    startTime = field("startTime")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    statusList = field("statusList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEphemeridesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEphemeridesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReserveContactRequest:
    boto3_raw_data: "type_defs.ReserveContactRequestTypeDef" = dataclasses.field()

    endTime = field("endTime")
    groundStation = field("groundStation")
    missionProfileArn = field("missionProfileArn")
    satelliteArn = field("satelliteArn")
    startTime = field("startTime")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReserveContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReserveContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeRange:
    boto3_raw_data: "type_defs.TimeRangeTypeDef" = dataclasses.field()

    endTime = field("endTime")
    startTime = field("startTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMissionProfileRequest:
    boto3_raw_data: "type_defs.CreateMissionProfileRequestTypeDef" = dataclasses.field()

    dataflowEdges = field("dataflowEdges")
    minimumViableContactDurationSeconds = field("minimumViableContactDurationSeconds")
    name = field("name")
    trackingConfigArn = field("trackingConfigArn")
    contactPostPassDurationSeconds = field("contactPostPassDurationSeconds")
    contactPrePassDurationSeconds = field("contactPrePassDurationSeconds")

    @cached_property
    def streamsKmsKey(self):  # pragma: no cover
        return KmsKey.make_one(self.boto3_raw_data["streamsKmsKey"])

    streamsKmsRole = field("streamsKmsRole")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMissionProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMissionProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMissionProfileResponse:
    boto3_raw_data: "type_defs.GetMissionProfileResponseTypeDef" = dataclasses.field()

    contactPostPassDurationSeconds = field("contactPostPassDurationSeconds")
    contactPrePassDurationSeconds = field("contactPrePassDurationSeconds")
    dataflowEdges = field("dataflowEdges")
    minimumViableContactDurationSeconds = field("minimumViableContactDurationSeconds")
    missionProfileArn = field("missionProfileArn")
    missionProfileId = field("missionProfileId")
    name = field("name")
    region = field("region")

    @cached_property
    def streamsKmsKey(self):  # pragma: no cover
        return KmsKey.make_one(self.boto3_raw_data["streamsKmsKey"])

    streamsKmsRole = field("streamsKmsRole")
    tags = field("tags")
    trackingConfigArn = field("trackingConfigArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMissionProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMissionProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMissionProfileRequest:
    boto3_raw_data: "type_defs.UpdateMissionProfileRequestTypeDef" = dataclasses.field()

    missionProfileId = field("missionProfileId")
    contactPostPassDurationSeconds = field("contactPostPassDurationSeconds")
    contactPrePassDurationSeconds = field("contactPrePassDurationSeconds")
    dataflowEdges = field("dataflowEdges")
    minimumViableContactDurationSeconds = field("minimumViableContactDurationSeconds")
    name = field("name")

    @cached_property
    def streamsKmsKey(self):  # pragma: no cover
        return KmsKey.make_one(self.boto3_raw_data["streamsKmsKey"])

    streamsKmsRole = field("streamsKmsRole")
    trackingConfigArn = field("trackingConfigArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMissionProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMissionProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataflowEndpointGroupsResponse:
    boto3_raw_data: "type_defs.ListDataflowEndpointGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataflowEndpointGroupList(self):  # pragma: no cover
        return DataflowEndpointListItem.make_many(
            self.boto3_raw_data["dataflowEndpointGroupList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataflowEndpointGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataflowEndpointGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactRequestWait:
    boto3_raw_data: "type_defs.DescribeContactRequestWaitTypeDef" = dataclasses.field()

    contactId = field("contactId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeContactRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EphemerisDescription:
    boto3_raw_data: "type_defs.EphemerisDescriptionTypeDef" = dataclasses.field()

    ephemerisData = field("ephemerisData")

    @cached_property
    def sourceS3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["sourceS3Object"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EphemerisDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EphemerisDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EphemerisItem:
    boto3_raw_data: "type_defs.EphemerisItemTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    enabled = field("enabled")
    ephemerisId = field("ephemerisId")
    name = field("name")
    priority = field("priority")

    @cached_property
    def sourceS3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["sourceS3Object"])

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EphemerisItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EphemerisItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OEMEphemeris:
    boto3_raw_data: "type_defs.OEMEphemerisTypeDef" = dataclasses.field()

    oemData = field("oemData")

    @cached_property
    def s3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["s3Object"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OEMEphemerisTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OEMEphemerisTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSatelliteResponse:
    boto3_raw_data: "type_defs.GetSatelliteResponseTypeDef" = dataclasses.field()

    @cached_property
    def currentEphemeris(self):  # pragma: no cover
        return EphemerisMetaData.make_one(self.boto3_raw_data["currentEphemeris"])

    groundStations = field("groundStations")
    noradSatelliteID = field("noradSatelliteID")
    satelliteArn = field("satelliteArn")
    satelliteId = field("satelliteId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSatelliteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSatelliteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SatelliteListItem:
    boto3_raw_data: "type_defs.SatelliteListItemTypeDef" = dataclasses.field()

    @cached_property
    def currentEphemeris(self):  # pragma: no cover
        return EphemerisMetaData.make_one(self.boto3_raw_data["currentEphemeris"])

    groundStations = field("groundStations")
    noradSatelliteID = field("noradSatelliteID")
    satelliteArn = field("satelliteArn")
    satelliteId = field("satelliteId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SatelliteListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SatelliteListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpectrumConfig:
    boto3_raw_data: "type_defs.SpectrumConfigTypeDef" = dataclasses.field()

    @cached_property
    def bandwidth(self):  # pragma: no cover
        return FrequencyBandwidth.make_one(self.boto3_raw_data["bandwidth"])

    @cached_property
    def centerFrequency(self):  # pragma: no cover
        return Frequency.make_one(self.boto3_raw_data["centerFrequency"])

    polarization = field("polarization")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpectrumConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SpectrumConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UplinkSpectrumConfig:
    boto3_raw_data: "type_defs.UplinkSpectrumConfigTypeDef" = dataclasses.field()

    @cached_property
    def centerFrequency(self):  # pragma: no cover
        return Frequency.make_one(self.boto3_raw_data["centerFrequency"])

    polarization = field("polarization")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UplinkSpectrumConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UplinkSpectrumConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroundStationsResponse:
    boto3_raw_data: "type_defs.ListGroundStationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def groundStationList(self):  # pragma: no cover
        return GroundStationData.make_many(self.boto3_raw_data["groundStationList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroundStationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroundStationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RangedSocketAddress:
    boto3_raw_data: "type_defs.RangedSocketAddressTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def portRange(self):  # pragma: no cover
        return IntegerRange.make_one(self.boto3_raw_data["portRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RangedSocketAddressTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RangedSocketAddressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListConfigsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfigsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactsRequestPaginate:
    boto3_raw_data: "type_defs.ListContactsRequestPaginateTypeDef" = dataclasses.field()

    endTime = field("endTime")
    startTime = field("startTime")
    statusList = field("statusList")
    groundStation = field("groundStation")
    missionProfileArn = field("missionProfileArn")
    satelliteArn = field("satelliteArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataflowEndpointGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataflowEndpointGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataflowEndpointGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataflowEndpointGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEphemeridesRequestPaginate:
    boto3_raw_data: "type_defs.ListEphemeridesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    endTime = field("endTime")
    satelliteId = field("satelliteId")
    startTime = field("startTime")
    statusList = field("statusList")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEphemeridesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEphemeridesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroundStationsRequestPaginate:
    boto3_raw_data: "type_defs.ListGroundStationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    satelliteId = field("satelliteId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGroundStationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroundStationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMissionProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListMissionProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMissionProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMissionProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSatellitesRequestPaginate:
    boto3_raw_data: "type_defs.ListSatellitesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSatellitesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSatellitesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMissionProfilesResponse:
    boto3_raw_data: "type_defs.ListMissionProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def missionProfileList(self):  # pragma: no cover
        return MissionProfileListItem.make_many(
            self.boto3_raw_data["missionProfileList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMissionProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMissionProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterAgentRequest:
    boto3_raw_data: "type_defs.RegisterAgentRequestTypeDef" = dataclasses.field()

    @cached_property
    def agentDetails(self):  # pragma: no cover
        return AgentDetails.make_one(self.boto3_raw_data["agentDetails"])

    @cached_property
    def discoveryData(self):  # pragma: no cover
        return DiscoveryData.make_one(self.boto3_raw_data["discoveryData"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactsResponse:
    boto3_raw_data: "type_defs.ListContactsResponseTypeDef" = dataclasses.field()

    @cached_property
    def contactList(self):  # pragma: no cover
        return ContactData.make_many(self.boto3_raw_data["contactList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TLEData:
    boto3_raw_data: "type_defs.TLEDataTypeDef" = dataclasses.field()

    tleLine1 = field("tleLine1")
    tleLine2 = field("tleLine2")

    @cached_property
    def validTimeRange(self):  # pragma: no cover
        return TimeRange.make_one(self.boto3_raw_data["validTimeRange"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TLEDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TLEDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EphemerisTypeDescription:
    boto3_raw_data: "type_defs.EphemerisTypeDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def oem(self):  # pragma: no cover
        return EphemerisDescription.make_one(self.boto3_raw_data["oem"])

    @cached_property
    def tle(self):  # pragma: no cover
        return EphemerisDescription.make_one(self.boto3_raw_data["tle"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EphemerisTypeDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EphemerisTypeDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEphemeridesResponse:
    boto3_raw_data: "type_defs.ListEphemeridesResponseTypeDef" = dataclasses.field()

    @cached_property
    def ephemerides(self):  # pragma: no cover
        return EphemerisItem.make_many(self.boto3_raw_data["ephemerides"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEphemeridesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEphemeridesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSatellitesResponse:
    boto3_raw_data: "type_defs.ListSatellitesResponseTypeDef" = dataclasses.field()

    @cached_property
    def satellites(self):  # pragma: no cover
        return SatelliteListItem.make_many(self.boto3_raw_data["satellites"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSatellitesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSatellitesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AntennaDownlinkConfig:
    boto3_raw_data: "type_defs.AntennaDownlinkConfigTypeDef" = dataclasses.field()

    @cached_property
    def spectrumConfig(self):  # pragma: no cover
        return SpectrumConfig.make_one(self.boto3_raw_data["spectrumConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AntennaDownlinkConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AntennaDownlinkConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AntennaDownlinkDemodDecodeConfig:
    boto3_raw_data: "type_defs.AntennaDownlinkDemodDecodeConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def decodeConfig(self):  # pragma: no cover
        return DecodeConfig.make_one(self.boto3_raw_data["decodeConfig"])

    @cached_property
    def demodulationConfig(self):  # pragma: no cover
        return DemodulationConfig.make_one(self.boto3_raw_data["demodulationConfig"])

    @cached_property
    def spectrumConfig(self):  # pragma: no cover
        return SpectrumConfig.make_one(self.boto3_raw_data["spectrumConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AntennaDownlinkDemodDecodeConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AntennaDownlinkDemodDecodeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AntennaUplinkConfig:
    boto3_raw_data: "type_defs.AntennaUplinkConfigTypeDef" = dataclasses.field()

    @cached_property
    def spectrumConfig(self):  # pragma: no cover
        return UplinkSpectrumConfig.make_one(self.boto3_raw_data["spectrumConfig"])

    @cached_property
    def targetEirp(self):  # pragma: no cover
        return Eirp.make_one(self.boto3_raw_data["targetEirp"])

    transmitDisabled = field("transmitDisabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AntennaUplinkConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AntennaUplinkConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RangedConnectionDetails:
    boto3_raw_data: "type_defs.RangedConnectionDetailsTypeDef" = dataclasses.field()

    @cached_property
    def socketAddress(self):  # pragma: no cover
        return RangedSocketAddress.make_one(self.boto3_raw_data["socketAddress"])

    mtu = field("mtu")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RangedConnectionDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RangedConnectionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TLEEphemeris:
    boto3_raw_data: "type_defs.TLEEphemerisTypeDef" = dataclasses.field()

    @cached_property
    def s3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["s3Object"])

    @cached_property
    def tleData(self):  # pragma: no cover
        return TLEData.make_many(self.boto3_raw_data["tleData"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TLEEphemerisTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TLEEphemerisTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEphemerisResponse:
    boto3_raw_data: "type_defs.DescribeEphemerisResponseTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    enabled = field("enabled")
    ephemerisId = field("ephemerisId")
    invalidReason = field("invalidReason")
    name = field("name")
    priority = field("priority")
    satelliteId = field("satelliteId")
    status = field("status")

    @cached_property
    def suppliedData(self):  # pragma: no cover
        return EphemerisTypeDescription.make_one(self.boto3_raw_data["suppliedData"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEphemerisResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEphemerisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigTypeData:
    boto3_raw_data: "type_defs.ConfigTypeDataTypeDef" = dataclasses.field()

    @cached_property
    def antennaDownlinkConfig(self):  # pragma: no cover
        return AntennaDownlinkConfig.make_one(
            self.boto3_raw_data["antennaDownlinkConfig"]
        )

    @cached_property
    def antennaDownlinkDemodDecodeConfig(self):  # pragma: no cover
        return AntennaDownlinkDemodDecodeConfig.make_one(
            self.boto3_raw_data["antennaDownlinkDemodDecodeConfig"]
        )

    @cached_property
    def antennaUplinkConfig(self):  # pragma: no cover
        return AntennaUplinkConfig.make_one(self.boto3_raw_data["antennaUplinkConfig"])

    @cached_property
    def dataflowEndpointConfig(self):  # pragma: no cover
        return DataflowEndpointConfig.make_one(
            self.boto3_raw_data["dataflowEndpointConfig"]
        )

    @cached_property
    def s3RecordingConfig(self):  # pragma: no cover
        return S3RecordingConfig.make_one(self.boto3_raw_data["s3RecordingConfig"])

    @cached_property
    def trackingConfig(self):  # pragma: no cover
        return TrackingConfig.make_one(self.boto3_raw_data["trackingConfig"])

    @cached_property
    def uplinkEchoConfig(self):  # pragma: no cover
        return UplinkEchoConfig.make_one(self.boto3_raw_data["uplinkEchoConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigTypeDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigTypeDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsGroundStationAgentEndpoint:
    boto3_raw_data: "type_defs.AwsGroundStationAgentEndpointTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def egressAddress(self):  # pragma: no cover
        return ConnectionDetails.make_one(self.boto3_raw_data["egressAddress"])

    @cached_property
    def ingressAddress(self):  # pragma: no cover
        return RangedConnectionDetails.make_one(self.boto3_raw_data["ingressAddress"])

    name = field("name")
    agentStatus = field("agentStatus")
    auditResults = field("auditResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AwsGroundStationAgentEndpointTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsGroundStationAgentEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EphemerisData:
    boto3_raw_data: "type_defs.EphemerisDataTypeDef" = dataclasses.field()

    @cached_property
    def oem(self):  # pragma: no cover
        return OEMEphemeris.make_one(self.boto3_raw_data["oem"])

    @cached_property
    def tle(self):  # pragma: no cover
        return TLEEphemeris.make_one(self.boto3_raw_data["tle"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EphemerisDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EphemerisDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigRequest:
    boto3_raw_data: "type_defs.CreateConfigRequestTypeDef" = dataclasses.field()

    @cached_property
    def configData(self):  # pragma: no cover
        return ConfigTypeData.make_one(self.boto3_raw_data["configData"])

    name = field("name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigResponse:
    boto3_raw_data: "type_defs.GetConfigResponseTypeDef" = dataclasses.field()

    configArn = field("configArn")

    @cached_property
    def configData(self):  # pragma: no cover
        return ConfigTypeData.make_one(self.boto3_raw_data["configData"])

    configId = field("configId")
    configType = field("configType")
    name = field("name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetConfigResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigRequest:
    boto3_raw_data: "type_defs.UpdateConfigRequestTypeDef" = dataclasses.field()

    @cached_property
    def configData(self):  # pragma: no cover
        return ConfigTypeData.make_one(self.boto3_raw_data["configData"])

    configId = field("configId")
    configType = field("configType")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointDetailsOutput:
    boto3_raw_data: "type_defs.EndpointDetailsOutputTypeDef" = dataclasses.field()

    @cached_property
    def awsGroundStationAgentEndpoint(self):  # pragma: no cover
        return AwsGroundStationAgentEndpoint.make_one(
            self.boto3_raw_data["awsGroundStationAgentEndpoint"]
        )

    @cached_property
    def endpoint(self):  # pragma: no cover
        return DataflowEndpoint.make_one(self.boto3_raw_data["endpoint"])

    healthReasons = field("healthReasons")
    healthStatus = field("healthStatus")

    @cached_property
    def securityDetails(self):  # pragma: no cover
        return SecurityDetailsOutput.make_one(self.boto3_raw_data["securityDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointDetails:
    boto3_raw_data: "type_defs.EndpointDetailsTypeDef" = dataclasses.field()

    @cached_property
    def awsGroundStationAgentEndpoint(self):  # pragma: no cover
        return AwsGroundStationAgentEndpoint.make_one(
            self.boto3_raw_data["awsGroundStationAgentEndpoint"]
        )

    @cached_property
    def endpoint(self):  # pragma: no cover
        return DataflowEndpoint.make_one(self.boto3_raw_data["endpoint"])

    healthReasons = field("healthReasons")
    healthStatus = field("healthStatus")
    securityDetails = field("securityDetails")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEphemerisRequest:
    boto3_raw_data: "type_defs.CreateEphemerisRequestTypeDef" = dataclasses.field()

    name = field("name")
    satelliteId = field("satelliteId")
    enabled = field("enabled")

    @cached_property
    def ephemeris(self):  # pragma: no cover
        return EphemerisData.make_one(self.boto3_raw_data["ephemeris"])

    expirationTime = field("expirationTime")
    kmsKeyArn = field("kmsKeyArn")
    priority = field("priority")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEphemerisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEphemerisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigDetails:
    boto3_raw_data: "type_defs.ConfigDetailsTypeDef" = dataclasses.field()

    @cached_property
    def antennaDemodDecodeDetails(self):  # pragma: no cover
        return AntennaDemodDecodeDetails.make_one(
            self.boto3_raw_data["antennaDemodDecodeDetails"]
        )

    @cached_property
    def endpointDetails(self):  # pragma: no cover
        return EndpointDetailsOutput.make_one(self.boto3_raw_data["endpointDetails"])

    @cached_property
    def s3RecordingDetails(self):  # pragma: no cover
        return S3RecordingDetails.make_one(self.boto3_raw_data["s3RecordingDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataflowEndpointGroupResponse:
    boto3_raw_data: "type_defs.GetDataflowEndpointGroupResponseTypeDef" = (
        dataclasses.field()
    )

    contactPostPassDurationSeconds = field("contactPostPassDurationSeconds")
    contactPrePassDurationSeconds = field("contactPrePassDurationSeconds")
    dataflowEndpointGroupArn = field("dataflowEndpointGroupArn")
    dataflowEndpointGroupId = field("dataflowEndpointGroupId")

    @cached_property
    def endpointsDetails(self):  # pragma: no cover
        return EndpointDetailsOutput.make_many(self.boto3_raw_data["endpointsDetails"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataflowEndpointGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataflowEndpointGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Destination:
    boto3_raw_data: "type_defs.DestinationTypeDef" = dataclasses.field()

    @cached_property
    def configDetails(self):  # pragma: no cover
        return ConfigDetails.make_one(self.boto3_raw_data["configDetails"])

    configId = field("configId")
    configType = field("configType")
    dataflowDestinationRegion = field("dataflowDestinationRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Source:
    boto3_raw_data: "type_defs.SourceTypeDef" = dataclasses.field()

    @cached_property
    def configDetails(self):  # pragma: no cover
        return ConfigDetails.make_one(self.boto3_raw_data["configDetails"])

    configId = field("configId")
    configType = field("configType")
    dataflowSourceRegion = field("dataflowSourceRegion")

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
class CreateDataflowEndpointGroupRequest:
    boto3_raw_data: "type_defs.CreateDataflowEndpointGroupRequestTypeDef" = (
        dataclasses.field()
    )

    endpointDetails = field("endpointDetails")
    contactPostPassDurationSeconds = field("contactPostPassDurationSeconds")
    contactPrePassDurationSeconds = field("contactPrePassDurationSeconds")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataflowEndpointGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataflowEndpointGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataflowDetail:
    boto3_raw_data: "type_defs.DataflowDetailTypeDef" = dataclasses.field()

    @cached_property
    def destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["destination"])

    errorMessage = field("errorMessage")

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataflowDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataflowDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactResponse:
    boto3_raw_data: "type_defs.DescribeContactResponseTypeDef" = dataclasses.field()

    contactId = field("contactId")
    contactStatus = field("contactStatus")

    @cached_property
    def dataflowList(self):  # pragma: no cover
        return DataflowDetail.make_many(self.boto3_raw_data["dataflowList"])

    endTime = field("endTime")
    errorMessage = field("errorMessage")
    groundStation = field("groundStation")

    @cached_property
    def maximumElevation(self):  # pragma: no cover
        return Elevation.make_one(self.boto3_raw_data["maximumElevation"])

    missionProfileArn = field("missionProfileArn")
    postPassEndTime = field("postPassEndTime")
    prePassStartTime = field("prePassStartTime")
    region = field("region")
    satelliteArn = field("satelliteArn")
    startTime = field("startTime")
    tags = field("tags")
    visibilityEndTime = field("visibilityEndTime")
    visibilityStartTime = field("visibilityStartTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
