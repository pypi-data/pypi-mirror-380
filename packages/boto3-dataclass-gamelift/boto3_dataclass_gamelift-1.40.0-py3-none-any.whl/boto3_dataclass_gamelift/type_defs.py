# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_gamelift import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptMatchInput:
    boto3_raw_data: "type_defs.AcceptMatchInputTypeDef" = dataclasses.field()

    TicketId = field("TicketId")
    PlayerIds = field("PlayerIds")
    AcceptanceType = field("AcceptanceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AcceptMatchInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptMatchInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingStrategy:
    boto3_raw_data: "type_defs.RoutingStrategyTypeDef" = dataclasses.field()

    Type = field("Type")
    FleetId = field("FleetId")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoutingStrategyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoutingStrategyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnywhereConfiguration:
    boto3_raw_data: "type_defs.AnywhereConfigurationTypeDef" = dataclasses.field()

    Cost = field("Cost")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnywhereConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnywhereConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValueOutput:
    boto3_raw_data: "type_defs.AttributeValueOutputTypeDef" = dataclasses.field()

    S = field("S")
    N = field("N")
    SL = field("SL")
    SDM = field("SDM")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValue:
    boto3_raw_data: "type_defs.AttributeValueTypeDef" = dataclasses.field()

    S = field("S")
    N = field("N")
    SL = field("SL")
    SDM = field("SDM")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsCredentials:
    boto3_raw_data: "type_defs.AwsCredentialsTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")
    SecretAccessKey = field("SecretAccessKey")
    SessionToken = field("SessionToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsCredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AwsCredentialsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Build:
    boto3_raw_data: "type_defs.BuildTypeDef" = dataclasses.field()

    BuildId = field("BuildId")
    BuildArn = field("BuildArn")
    Name = field("Name")
    Version = field("Version")
    Status = field("Status")
    SizeOnDisk = field("SizeOnDisk")
    OperatingSystem = field("OperatingSystem")
    CreationTime = field("CreationTime")
    ServerSdkVersion = field("ServerSdkVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BuildTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateConfiguration:
    boto3_raw_data: "type_defs.CertificateConfigurationTypeDef" = dataclasses.field()

    CertificateType = field("CertificateType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClaimFilterOption:
    boto3_raw_data: "type_defs.ClaimFilterOptionTypeDef" = dataclasses.field()

    InstanceStatuses = field("InstanceStatuses")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClaimFilterOptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClaimFilterOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameServer:
    boto3_raw_data: "type_defs.GameServerTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    GameServerGroupArn = field("GameServerGroupArn")
    GameServerId = field("GameServerId")
    InstanceId = field("InstanceId")
    ConnectionInfo = field("ConnectionInfo")
    GameServerData = field("GameServerData")
    ClaimStatus = field("ClaimStatus")
    UtilizationStatus = field("UtilizationStatus")
    RegistrationTime = field("RegistrationTime")
    LastClaimTime = field("LastClaimTime")
    LastHealthCheckTime = field("LastHealthCheckTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GameServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GameServerTypeDef"]]
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
class ContainerAttribute:
    boto3_raw_data: "type_defs.ContainerAttributeTypeDef" = dataclasses.field()

    ContainerName = field("ContainerName")
    ContainerRuntimeId = field("ContainerRuntimeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionPortRange:
    boto3_raw_data: "type_defs.ConnectionPortRangeTypeDef" = dataclasses.field()

    FromPort = field("FromPort")
    ToPort = field("ToPort")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionPortRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionPortRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerDependency:
    boto3_raw_data: "type_defs.ContainerDependencyTypeDef" = dataclasses.field()

    ContainerName = field("ContainerName")
    Condition = field("Condition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerDependencyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerDependencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerEnvironment:
    boto3_raw_data: "type_defs.ContainerEnvironmentTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerEnvironmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerEnvironmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerFleetLocationAttributes:
    boto3_raw_data: "type_defs.ContainerFleetLocationAttributesTypeDef" = (
        dataclasses.field()
    )

    Location = field("Location")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContainerFleetLocationAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerFleetLocationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentDetails:
    boto3_raw_data: "type_defs.DeploymentDetailsTypeDef" = dataclasses.field()

    LatestDeploymentId = field("LatestDeploymentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameSessionCreationLimitPolicy:
    boto3_raw_data: "type_defs.GameSessionCreationLimitPolicyTypeDef" = (
        dataclasses.field()
    )

    NewGameSessionsPerCreator = field("NewGameSessionsPerCreator")
    PolicyPeriodInMinutes = field("PolicyPeriodInMinutes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GameSessionCreationLimitPolicyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameSessionCreationLimitPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpPermission:
    boto3_raw_data: "type_defs.IpPermissionTypeDef" = dataclasses.field()

    FromPort = field("FromPort")
    ToPort = field("ToPort")
    IpRange = field("IpRange")
    Protocol = field("Protocol")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpPermissionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpPermissionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogConfiguration:
    boto3_raw_data: "type_defs.LogConfigurationTypeDef" = dataclasses.field()

    LogDestination = field("LogDestination")
    S3BucketName = field("S3BucketName")
    LogGroupArn = field("LogGroupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerHealthCheckOutput:
    boto3_raw_data: "type_defs.ContainerHealthCheckOutputTypeDef" = dataclasses.field()

    Command = field("Command")
    Interval = field("Interval")
    Retries = field("Retries")
    StartPeriod = field("StartPeriod")
    Timeout = field("Timeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerHealthCheckOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerHealthCheckOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerHealthCheck:
    boto3_raw_data: "type_defs.ContainerHealthCheckTypeDef" = dataclasses.field()

    Command = field("Command")
    Interval = field("Interval")
    Retries = field("Retries")
    StartPeriod = field("StartPeriod")
    Timeout = field("Timeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerHealthCheckTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerHealthCheckTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerIdentifier:
    boto3_raw_data: "type_defs.ContainerIdentifierTypeDef" = dataclasses.field()

    ContainerName = field("ContainerName")
    ContainerRuntimeId = field("ContainerRuntimeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerMountPoint:
    boto3_raw_data: "type_defs.ContainerMountPointTypeDef" = dataclasses.field()

    InstancePath = field("InstancePath")
    ContainerPath = field("ContainerPath")
    AccessLevel = field("AccessLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerMountPointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerMountPointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerPortRange:
    boto3_raw_data: "type_defs.ContainerPortRangeTypeDef" = dataclasses.field()

    FromPort = field("FromPort")
    ToPort = field("ToPort")
    Protocol = field("Protocol")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerPortRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerPortRangeTypeDef"]
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
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    RoleArn = field("RoleArn")
    ObjectVersion = field("ObjectVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationConfiguration:
    boto3_raw_data: "type_defs.LocationConfigurationTypeDef" = dataclasses.field()

    Location = field("Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LocationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceCreationLimitPolicy:
    boto3_raw_data: "type_defs.ResourceCreationLimitPolicyTypeDef" = dataclasses.field()

    NewGameSessionsPerCreator = field("NewGameSessionsPerCreator")
    PolicyPeriodInMinutes = field("PolicyPeriodInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceCreationLimitPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceCreationLimitPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationState:
    boto3_raw_data: "type_defs.LocationStateTypeDef" = dataclasses.field()

    Location = field("Location")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceDefinition:
    boto3_raw_data: "type_defs.InstanceDefinitionTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")
    WeightedCapacity = field("WeightedCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateSpecification:
    boto3_raw_data: "type_defs.LaunchTemplateSpecificationTypeDef" = dataclasses.field()

    LaunchTemplateId = field("LaunchTemplateId")
    LaunchTemplateName = field("LaunchTemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchTemplateSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameProperty:
    boto3_raw_data: "type_defs.GamePropertyTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GamePropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GamePropertyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameSessionQueueDestination:
    boto3_raw_data: "type_defs.GameSessionQueueDestinationTypeDef" = dataclasses.field()

    DestinationArn = field("DestinationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GameSessionQueueDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameSessionQueueDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlayerLatencyPolicy:
    boto3_raw_data: "type_defs.PlayerLatencyPolicyTypeDef" = dataclasses.field()

    MaximumIndividualPlayerLatencyMilliseconds = field(
        "MaximumIndividualPlayerLatencyMilliseconds"
    )
    PolicyDurationSeconds = field("PolicyDurationSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlayerLatencyPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlayerLatencyPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchmakingRuleSet:
    boto3_raw_data: "type_defs.MatchmakingRuleSetTypeDef" = dataclasses.field()

    RuleSetBody = field("RuleSetBody")
    RuleSetName = field("RuleSetName")
    RuleSetArn = field("RuleSetArn")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MatchmakingRuleSetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchmakingRuleSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePlayerSessionInput:
    boto3_raw_data: "type_defs.CreatePlayerSessionInputTypeDef" = dataclasses.field()

    GameSessionId = field("GameSessionId")
    PlayerId = field("PlayerId")
    PlayerData = field("PlayerData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePlayerSessionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePlayerSessionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlayerSession:
    boto3_raw_data: "type_defs.PlayerSessionTypeDef" = dataclasses.field()

    PlayerSessionId = field("PlayerSessionId")
    PlayerId = field("PlayerId")
    GameSessionId = field("GameSessionId")
    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    CreationTime = field("CreationTime")
    TerminationTime = field("TerminationTime")
    Status = field("Status")
    IpAddress = field("IpAddress")
    DnsName = field("DnsName")
    Port = field("Port")
    PlayerData = field("PlayerData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlayerSessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlayerSessionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePlayerSessionsInput:
    boto3_raw_data: "type_defs.CreatePlayerSessionsInputTypeDef" = dataclasses.field()

    GameSessionId = field("GameSessionId")
    PlayerIds = field("PlayerIds")
    PlayerDataMap = field("PlayerDataMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePlayerSessionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePlayerSessionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcPeeringAuthorizationInput:
    boto3_raw_data: "type_defs.CreateVpcPeeringAuthorizationInputTypeDef" = (
        dataclasses.field()
    )

    GameLiftAwsAccountId = field("GameLiftAwsAccountId")
    PeerVpcId = field("PeerVpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVpcPeeringAuthorizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcPeeringAuthorizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcPeeringAuthorization:
    boto3_raw_data: "type_defs.VpcPeeringAuthorizationTypeDef" = dataclasses.field()

    GameLiftAwsAccountId = field("GameLiftAwsAccountId")
    PeerVpcAwsAccountId = field("PeerVpcAwsAccountId")
    PeerVpcId = field("PeerVpcId")
    CreationTime = field("CreationTime")
    ExpirationTime = field("ExpirationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcPeeringAuthorizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcPeeringAuthorizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcPeeringConnectionInput:
    boto3_raw_data: "type_defs.CreateVpcPeeringConnectionInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    PeerVpcAwsAccountId = field("PeerVpcAwsAccountId")
    PeerVpcId = field("PeerVpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateVpcPeeringConnectionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcPeeringConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAliasInput:
    boto3_raw_data: "type_defs.DeleteAliasInputTypeDef" = dataclasses.field()

    AliasId = field("AliasId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAliasInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBuildInput:
    boto3_raw_data: "type_defs.DeleteBuildInputTypeDef" = dataclasses.field()

    BuildId = field("BuildId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteBuildInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBuildInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContainerFleetInput:
    boto3_raw_data: "type_defs.DeleteContainerFleetInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContainerFleetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContainerFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContainerGroupDefinitionInput:
    boto3_raw_data: "type_defs.DeleteContainerGroupDefinitionInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    VersionNumber = field("VersionNumber")
    VersionCountToRetain = field("VersionCountToRetain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteContainerGroupDefinitionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContainerGroupDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetInput:
    boto3_raw_data: "type_defs.DeleteFleetInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFleetInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetLocationsInput:
    boto3_raw_data: "type_defs.DeleteFleetLocationsInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    Locations = field("Locations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFleetLocationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetLocationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGameServerGroupInput:
    boto3_raw_data: "type_defs.DeleteGameServerGroupInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    DeleteOption = field("DeleteOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGameServerGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGameServerGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGameSessionQueueInput:
    boto3_raw_data: "type_defs.DeleteGameSessionQueueInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGameSessionQueueInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGameSessionQueueInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLocationInput:
    boto3_raw_data: "type_defs.DeleteLocationInputTypeDef" = dataclasses.field()

    LocationName = field("LocationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLocationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLocationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMatchmakingConfigurationInput:
    boto3_raw_data: "type_defs.DeleteMatchmakingConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMatchmakingConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMatchmakingConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMatchmakingRuleSetInput:
    boto3_raw_data: "type_defs.DeleteMatchmakingRuleSetInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMatchmakingRuleSetInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMatchmakingRuleSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScalingPolicyInput:
    boto3_raw_data: "type_defs.DeleteScalingPolicyInputTypeDef" = dataclasses.field()

    Name = field("Name")
    FleetId = field("FleetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScalingPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScalingPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScriptInput:
    boto3_raw_data: "type_defs.DeleteScriptInputTypeDef" = dataclasses.field()

    ScriptId = field("ScriptId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteScriptInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScriptInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcPeeringAuthorizationInput:
    boto3_raw_data: "type_defs.DeleteVpcPeeringAuthorizationInputTypeDef" = (
        dataclasses.field()
    )

    GameLiftAwsAccountId = field("GameLiftAwsAccountId")
    PeerVpcId = field("PeerVpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVpcPeeringAuthorizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcPeeringAuthorizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcPeeringConnectionInput:
    boto3_raw_data: "type_defs.DeleteVpcPeeringConnectionInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    VpcPeeringConnectionId = field("VpcPeeringConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVpcPeeringConnectionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcPeeringConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentConfiguration:
    boto3_raw_data: "type_defs.DeploymentConfigurationTypeDef" = dataclasses.field()

    ProtectionStrategy = field("ProtectionStrategy")
    MinimumHealthyPercentage = field("MinimumHealthyPercentage")
    ImpairmentStrategy = field("ImpairmentStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterComputeInput:
    boto3_raw_data: "type_defs.DeregisterComputeInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    ComputeName = field("ComputeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterComputeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterComputeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterGameServerInput:
    boto3_raw_data: "type_defs.DeregisterGameServerInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    GameServerId = field("GameServerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterGameServerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterGameServerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAliasInput:
    boto3_raw_data: "type_defs.DescribeAliasInputTypeDef" = dataclasses.field()

    AliasId = field("AliasId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAliasInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBuildInput:
    boto3_raw_data: "type_defs.DescribeBuildInputTypeDef" = dataclasses.field()

    BuildId = field("BuildId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBuildInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBuildInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComputeInput:
    boto3_raw_data: "type_defs.DescribeComputeInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    ComputeName = field("ComputeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeComputeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComputeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContainerFleetInput:
    boto3_raw_data: "type_defs.DescribeContainerFleetInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeContainerFleetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContainerFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContainerGroupDefinitionInput:
    boto3_raw_data: "type_defs.DescribeContainerGroupDefinitionInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    VersionNumber = field("VersionNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeContainerGroupDefinitionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContainerGroupDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEC2InstanceLimitsInput:
    boto3_raw_data: "type_defs.DescribeEC2InstanceLimitsInputTypeDef" = (
        dataclasses.field()
    )

    EC2InstanceType = field("EC2InstanceType")
    Location = field("Location")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEC2InstanceLimitsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEC2InstanceLimitsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2InstanceLimit:
    boto3_raw_data: "type_defs.EC2InstanceLimitTypeDef" = dataclasses.field()

    EC2InstanceType = field("EC2InstanceType")
    CurrentInstances = field("CurrentInstances")
    InstanceLimit = field("InstanceLimit")
    Location = field("Location")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EC2InstanceLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2InstanceLimitTypeDef"]
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
class DescribeFleetAttributesInput:
    boto3_raw_data: "type_defs.DescribeFleetAttributesInputTypeDef" = (
        dataclasses.field()
    )

    FleetIds = field("FleetIds")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetAttributesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetCapacityInput:
    boto3_raw_data: "type_defs.DescribeFleetCapacityInputTypeDef" = dataclasses.field()

    FleetIds = field("FleetIds")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetCapacityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetCapacityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetDeploymentInput:
    boto3_raw_data: "type_defs.DescribeFleetDeploymentInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    DeploymentId = field("DeploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetDeploymentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetDeploymentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationalDeployment:
    boto3_raw_data: "type_defs.LocationalDeploymentTypeDef" = dataclasses.field()

    DeploymentStatus = field("DeploymentStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LocationalDeploymentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocationalDeploymentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    EventId = field("EventId")
    ResourceId = field("ResourceId")
    EventCode = field("EventCode")
    Message = field("Message")
    EventTime = field("EventTime")
    PreSignedLogUrl = field("PreSignedLogUrl")
    Count = field("Count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetLocationAttributesInput:
    boto3_raw_data: "type_defs.DescribeFleetLocationAttributesInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    Locations = field("Locations")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetLocationAttributesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetLocationAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetLocationCapacityInput:
    boto3_raw_data: "type_defs.DescribeFleetLocationCapacityInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    Location = field("Location")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetLocationCapacityInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetLocationCapacityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetLocationUtilizationInput:
    boto3_raw_data: "type_defs.DescribeFleetLocationUtilizationInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    Location = field("Location")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetLocationUtilizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetLocationUtilizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetUtilization:
    boto3_raw_data: "type_defs.FleetUtilizationTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    ActiveServerProcessCount = field("ActiveServerProcessCount")
    ActiveGameSessionCount = field("ActiveGameSessionCount")
    CurrentPlayerSessionCount = field("CurrentPlayerSessionCount")
    MaximumPlayerSessionCount = field("MaximumPlayerSessionCount")
    Location = field("Location")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetUtilizationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetUtilizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetPortSettingsInput:
    boto3_raw_data: "type_defs.DescribeFleetPortSettingsInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    Location = field("Location")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFleetPortSettingsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetPortSettingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetUtilizationInput:
    boto3_raw_data: "type_defs.DescribeFleetUtilizationInputTypeDef" = (
        dataclasses.field()
    )

    FleetIds = field("FleetIds")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFleetUtilizationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetUtilizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameServerGroupInput:
    boto3_raw_data: "type_defs.DescribeGameServerGroupInputTypeDef" = (
        dataclasses.field()
    )

    GameServerGroupName = field("GameServerGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGameServerGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameServerGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameServerInput:
    boto3_raw_data: "type_defs.DescribeGameServerInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    GameServerId = field("GameServerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGameServerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameServerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameServerInstancesInput:
    boto3_raw_data: "type_defs.DescribeGameServerInstancesInputTypeDef" = (
        dataclasses.field()
    )

    GameServerGroupName = field("GameServerGroupName")
    InstanceIds = field("InstanceIds")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGameServerInstancesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameServerInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameServerInstance:
    boto3_raw_data: "type_defs.GameServerInstanceTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    GameServerGroupArn = field("GameServerGroupArn")
    InstanceId = field("InstanceId")
    InstanceStatus = field("InstanceStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GameServerInstanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameServerInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionDetailsInput:
    boto3_raw_data: "type_defs.DescribeGameSessionDetailsInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    GameSessionId = field("GameSessionId")
    AliasId = field("AliasId")
    Location = field("Location")
    StatusFilter = field("StatusFilter")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGameSessionDetailsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionDetailsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionPlacementInput:
    boto3_raw_data: "type_defs.DescribeGameSessionPlacementInputTypeDef" = (
        dataclasses.field()
    )

    PlacementId = field("PlacementId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGameSessionPlacementInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionPlacementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionQueuesInput:
    boto3_raw_data: "type_defs.DescribeGameSessionQueuesInputTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGameSessionQueuesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionQueuesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionsInput:
    boto3_raw_data: "type_defs.DescribeGameSessionsInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    GameSessionId = field("GameSessionId")
    AliasId = field("AliasId")
    Location = field("Location")
    StatusFilter = field("StatusFilter")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGameSessionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancesInput:
    boto3_raw_data: "type_defs.DescribeInstancesInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    InstanceId = field("InstanceId")
    Limit = field("Limit")
    NextToken = field("NextToken")
    Location = field("Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Instance:
    boto3_raw_data: "type_defs.InstanceTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    InstanceId = field("InstanceId")
    IpAddress = field("IpAddress")
    DnsName = field("DnsName")
    OperatingSystem = field("OperatingSystem")
    Type = field("Type")
    Status = field("Status")
    CreationTime = field("CreationTime")
    Location = field("Location")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMatchmakingConfigurationsInput:
    boto3_raw_data: "type_defs.DescribeMatchmakingConfigurationsInputTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")
    RuleSetName = field("RuleSetName")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMatchmakingConfigurationsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMatchmakingConfigurationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMatchmakingInput:
    boto3_raw_data: "type_defs.DescribeMatchmakingInputTypeDef" = dataclasses.field()

    TicketIds = field("TicketIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMatchmakingInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMatchmakingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMatchmakingRuleSetsInput:
    boto3_raw_data: "type_defs.DescribeMatchmakingRuleSetsInputTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMatchmakingRuleSetsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMatchmakingRuleSetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePlayerSessionsInput:
    boto3_raw_data: "type_defs.DescribePlayerSessionsInputTypeDef" = dataclasses.field()

    GameSessionId = field("GameSessionId")
    PlayerId = field("PlayerId")
    PlayerSessionId = field("PlayerSessionId")
    PlayerSessionStatusFilter = field("PlayerSessionStatusFilter")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePlayerSessionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePlayerSessionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuntimeConfigurationInput:
    boto3_raw_data: "type_defs.DescribeRuntimeConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRuntimeConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuntimeConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPoliciesInput:
    boto3_raw_data: "type_defs.DescribeScalingPoliciesInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    StatusFilter = field("StatusFilter")
    Limit = field("Limit")
    NextToken = field("NextToken")
    Location = field("Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeScalingPoliciesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPoliciesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScriptInput:
    boto3_raw_data: "type_defs.DescribeScriptInputTypeDef" = dataclasses.field()

    ScriptId = field("ScriptId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeScriptInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScriptInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcPeeringConnectionsInput:
    boto3_raw_data: "type_defs.DescribeVpcPeeringConnectionsInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVpcPeeringConnectionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcPeeringConnectionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DesiredPlayerSession:
    boto3_raw_data: "type_defs.DesiredPlayerSessionTypeDef" = dataclasses.field()

    PlayerId = field("PlayerId")
    PlayerData = field("PlayerData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DesiredPlayerSessionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DesiredPlayerSessionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2InstanceCounts:
    boto3_raw_data: "type_defs.EC2InstanceCountsTypeDef" = dataclasses.field()

    DESIRED = field("DESIRED")
    MINIMUM = field("MINIMUM")
    MAXIMUM = field("MAXIMUM")
    PENDING = field("PENDING")
    ACTIVE = field("ACTIVE")
    IDLE = field("IDLE")
    TERMINATING = field("TERMINATING")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EC2InstanceCountsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2InstanceCountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterConfigurationOutput:
    boto3_raw_data: "type_defs.FilterConfigurationOutputTypeDef" = dataclasses.field()

    AllowedLocations = field("AllowedLocations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterConfiguration:
    boto3_raw_data: "type_defs.FilterConfigurationTypeDef" = dataclasses.field()

    AllowedLocations = field("AllowedLocations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameServerContainerGroupCounts:
    boto3_raw_data: "type_defs.GameServerContainerGroupCountsTypeDef" = (
        dataclasses.field()
    )

    PENDING = field("PENDING")
    ACTIVE = field("ACTIVE")
    IDLE = field("IDLE")
    TERMINATING = field("TERMINATING")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GameServerContainerGroupCountsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameServerContainerGroupCountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingConfiguration:
    boto3_raw_data: "type_defs.TargetTrackingConfigurationTypeDef" = dataclasses.field()

    TargetValue = field("TargetValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetTrackingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchedPlayerSession:
    boto3_raw_data: "type_defs.MatchedPlayerSessionTypeDef" = dataclasses.field()

    PlayerId = field("PlayerId")
    PlayerSessionId = field("PlayerSessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MatchedPlayerSessionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchedPlayerSessionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlacedPlayerSession:
    boto3_raw_data: "type_defs.PlacedPlayerSessionTypeDef" = dataclasses.field()

    PlayerId = field("PlayerId")
    PlayerSessionId = field("PlayerSessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlacedPlayerSessionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlacedPlayerSessionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlayerLatency:
    boto3_raw_data: "type_defs.PlayerLatencyTypeDef" = dataclasses.field()

    PlayerId = field("PlayerId")
    RegionIdentifier = field("RegionIdentifier")
    LatencyInMilliseconds = field("LatencyInMilliseconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlayerLatencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlayerLatencyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PriorityConfigurationOverrideOutput:
    boto3_raw_data: "type_defs.PriorityConfigurationOverrideOutputTypeDef" = (
        dataclasses.field()
    )

    LocationOrder = field("LocationOrder")
    PlacementFallbackStrategy = field("PlacementFallbackStrategy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PriorityConfigurationOverrideOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PriorityConfigurationOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PriorityConfigurationOutput:
    boto3_raw_data: "type_defs.PriorityConfigurationOutputTypeDef" = dataclasses.field()

    PriorityOrder = field("PriorityOrder")
    LocationOrder = field("LocationOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PriorityConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PriorityConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComputeAccessInput:
    boto3_raw_data: "type_defs.GetComputeAccessInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    ComputeName = field("ComputeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComputeAccessInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComputeAccessInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComputeAuthTokenInput:
    boto3_raw_data: "type_defs.GetComputeAuthTokenInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    ComputeName = field("ComputeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComputeAuthTokenInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComputeAuthTokenInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGameSessionLogUrlInput:
    boto3_raw_data: "type_defs.GetGameSessionLogUrlInputTypeDef" = dataclasses.field()

    GameSessionId = field("GameSessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGameSessionLogUrlInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGameSessionLogUrlInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceAccessInput:
    boto3_raw_data: "type_defs.GetInstanceAccessInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceAccessInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceAccessInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceCredentials:
    boto3_raw_data: "type_defs.InstanceCredentialsTypeDef" = dataclasses.field()

    UserName = field("UserName")
    Secret = field("Secret")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesInput:
    boto3_raw_data: "type_defs.ListAliasesInputTypeDef" = dataclasses.field()

    RoutingStrategyType = field("RoutingStrategyType")
    Name = field("Name")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAliasesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildsInput:
    boto3_raw_data: "type_defs.ListBuildsInputTypeDef" = dataclasses.field()

    Status = field("Status")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBuildsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListBuildsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputeInput:
    boto3_raw_data: "type_defs.ListComputeInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    Location = field("Location")
    ContainerGroupDefinitionName = field("ContainerGroupDefinitionName")
    ComputeStatus = field("ComputeStatus")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListComputeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerFleetsInput:
    boto3_raw_data: "type_defs.ListContainerFleetsInputTypeDef" = dataclasses.field()

    ContainerGroupDefinitionName = field("ContainerGroupDefinitionName")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContainerFleetsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerFleetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerGroupDefinitionVersionsInput:
    boto3_raw_data: "type_defs.ListContainerGroupDefinitionVersionsInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContainerGroupDefinitionVersionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerGroupDefinitionVersionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerGroupDefinitionsInput:
    boto3_raw_data: "type_defs.ListContainerGroupDefinitionsInputTypeDef" = (
        dataclasses.field()
    )

    ContainerGroupType = field("ContainerGroupType")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContainerGroupDefinitionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerGroupDefinitionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetDeploymentsInput:
    boto3_raw_data: "type_defs.ListFleetDeploymentsInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetDeploymentsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetDeploymentsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsInput:
    boto3_raw_data: "type_defs.ListFleetsInputTypeDef" = dataclasses.field()

    BuildId = field("BuildId")
    ScriptId = field("ScriptId")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFleetsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListFleetsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGameServerGroupsInput:
    boto3_raw_data: "type_defs.ListGameServerGroupsInputTypeDef" = dataclasses.field()

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGameServerGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGameServerGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGameServersInput:
    boto3_raw_data: "type_defs.ListGameServersInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    SortOrder = field("SortOrder")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGameServersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGameServersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLocationsInput:
    boto3_raw_data: "type_defs.ListLocationsInputTypeDef" = dataclasses.field()

    Filters = field("Filters")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLocationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLocationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScriptsInput:
    boto3_raw_data: "type_defs.ListScriptsInputTypeDef" = dataclasses.field()

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListScriptsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScriptsInputTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class UDPEndpoint:
    boto3_raw_data: "type_defs.UDPEndpointTypeDef" = dataclasses.field()

    Domain = field("Domain")
    Port = field("Port")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UDPEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UDPEndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PriorityConfigurationOverride:
    boto3_raw_data: "type_defs.PriorityConfigurationOverrideTypeDef" = (
        dataclasses.field()
    )

    LocationOrder = field("LocationOrder")
    PlacementFallbackStrategy = field("PlacementFallbackStrategy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PriorityConfigurationOverrideTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PriorityConfigurationOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PriorityConfiguration:
    boto3_raw_data: "type_defs.PriorityConfigurationTypeDef" = dataclasses.field()

    PriorityOrder = field("PriorityOrder")
    LocationOrder = field("LocationOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PriorityConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PriorityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetConfiguration:
    boto3_raw_data: "type_defs.TargetConfigurationTypeDef" = dataclasses.field()

    TargetValue = field("TargetValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterComputeInput:
    boto3_raw_data: "type_defs.RegisterComputeInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    ComputeName = field("ComputeName")
    CertificatePath = field("CertificatePath")
    DnsName = field("DnsName")
    IpAddress = field("IpAddress")
    Location = field("Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterComputeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterComputeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterGameServerInput:
    boto3_raw_data: "type_defs.RegisterGameServerInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    GameServerId = field("GameServerId")
    InstanceId = field("InstanceId")
    ConnectionInfo = field("ConnectionInfo")
    GameServerData = field("GameServerData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterGameServerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterGameServerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestUploadCredentialsInput:
    boto3_raw_data: "type_defs.RequestUploadCredentialsInputTypeDef" = (
        dataclasses.field()
    )

    BuildId = field("BuildId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RequestUploadCredentialsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestUploadCredentialsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolveAliasInput:
    boto3_raw_data: "type_defs.ResolveAliasInputTypeDef" = dataclasses.field()

    AliasId = field("AliasId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResolveAliasInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolveAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeGameServerGroupInput:
    boto3_raw_data: "type_defs.ResumeGameServerGroupInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    ResumeActions = field("ResumeActions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeGameServerGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeGameServerGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerProcess:
    boto3_raw_data: "type_defs.ServerProcessTypeDef" = dataclasses.field()

    LaunchPath = field("LaunchPath")
    ConcurrentExecutions = field("ConcurrentExecutions")
    Parameters = field("Parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerProcessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerProcessTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchGameSessionsInput:
    boto3_raw_data: "type_defs.SearchGameSessionsInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    AliasId = field("AliasId")
    Location = field("Location")
    FilterExpression = field("FilterExpression")
    SortExpression = field("SortExpression")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchGameSessionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchGameSessionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFleetActionsInput:
    boto3_raw_data: "type_defs.StartFleetActionsInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    Actions = field("Actions")
    Location = field("Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFleetActionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFleetActionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopFleetActionsInput:
    boto3_raw_data: "type_defs.StopFleetActionsInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    Actions = field("Actions")
    Location = field("Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopFleetActionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopFleetActionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopGameSessionPlacementInput:
    boto3_raw_data: "type_defs.StopGameSessionPlacementInputTypeDef" = (
        dataclasses.field()
    )

    PlacementId = field("PlacementId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopGameSessionPlacementInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopGameSessionPlacementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopMatchmakingInput:
    boto3_raw_data: "type_defs.StopMatchmakingInputTypeDef" = dataclasses.field()

    TicketId = field("TicketId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopMatchmakingInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopMatchmakingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuspendGameServerGroupInput:
    boto3_raw_data: "type_defs.SuspendGameServerGroupInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    SuspendActions = field("SuspendActions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuspendGameServerGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuspendGameServerGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateGameSessionInput:
    boto3_raw_data: "type_defs.TerminateGameSessionInputTypeDef" = dataclasses.field()

    GameSessionId = field("GameSessionId")
    TerminationMode = field("TerminationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateGameSessionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateGameSessionInputTypeDef"]
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

    ResourceARN = field("ResourceARN")
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
class UpdateBuildInput:
    boto3_raw_data: "type_defs.UpdateBuildInputTypeDef" = dataclasses.field()

    BuildId = field("BuildId")
    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateBuildInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBuildInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetCapacityInput:
    boto3_raw_data: "type_defs.UpdateFleetCapacityInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    DesiredInstances = field("DesiredInstances")
    MinSize = field("MinSize")
    MaxSize = field("MaxSize")
    Location = field("Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetCapacityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetCapacityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGameServerInput:
    boto3_raw_data: "type_defs.UpdateGameServerInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    GameServerId = field("GameServerId")
    GameServerData = field("GameServerData")
    UtilizationStatus = field("UtilizationStatus")
    HealthCheck = field("HealthCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGameServerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGameServerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateMatchmakingRuleSetInput:
    boto3_raw_data: "type_defs.ValidateMatchmakingRuleSetInputTypeDef" = (
        dataclasses.field()
    )

    RuleSetBody = field("RuleSetBody")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ValidateMatchmakingRuleSetInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateMatchmakingRuleSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcPeeringConnectionStatus:
    boto3_raw_data: "type_defs.VpcPeeringConnectionStatusTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcPeeringConnectionStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcPeeringConnectionStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Alias:
    boto3_raw_data: "type_defs.AliasTypeDef" = dataclasses.field()

    AliasId = field("AliasId")
    Name = field("Name")
    AliasArn = field("AliasArn")
    Description = field("Description")

    @cached_property
    def RoutingStrategy(self):  # pragma: no cover
        return RoutingStrategy.make_one(self.boto3_raw_data["RoutingStrategy"])

    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AliasTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AliasTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAliasInput:
    boto3_raw_data: "type_defs.UpdateAliasInputTypeDef" = dataclasses.field()

    AliasId = field("AliasId")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def RoutingStrategy(self):  # pragma: no cover
        return RoutingStrategy.make_one(self.boto3_raw_data["RoutingStrategy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAliasInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlayerOutput:
    boto3_raw_data: "type_defs.PlayerOutputTypeDef" = dataclasses.field()

    PlayerId = field("PlayerId")
    PlayerAttributes = field("PlayerAttributes")
    Team = field("Team")
    LatencyInMs = field("LatencyInMs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlayerOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlayerOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClaimGameServerInput:
    boto3_raw_data: "type_defs.ClaimGameServerInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    GameServerId = field("GameServerId")
    GameServerData = field("GameServerData")

    @cached_property
    def FilterOption(self):  # pragma: no cover
        return ClaimFilterOption.make_one(self.boto3_raw_data["FilterOption"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClaimGameServerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClaimGameServerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClaimGameServerOutput:
    boto3_raw_data: "type_defs.ClaimGameServerOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameServer(self):  # pragma: no cover
        return GameServer.make_one(self.boto3_raw_data["GameServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClaimGameServerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClaimGameServerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBuildOutput:
    boto3_raw_data: "type_defs.DescribeBuildOutputTypeDef" = dataclasses.field()

    @cached_property
    def Build(self):  # pragma: no cover
        return Build.make_one(self.boto3_raw_data["Build"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBuildOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBuildOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameServerOutput:
    boto3_raw_data: "type_defs.DescribeGameServerOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameServer(self):  # pragma: no cover
        return GameServer.make_one(self.boto3_raw_data["GameServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGameServerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameServerOutputTypeDef"]
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
class GetComputeAuthTokenOutput:
    boto3_raw_data: "type_defs.GetComputeAuthTokenOutputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    ComputeName = field("ComputeName")
    ComputeArn = field("ComputeArn")
    AuthToken = field("AuthToken")
    ExpirationTimestamp = field("ExpirationTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComputeAuthTokenOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComputeAuthTokenOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGameSessionLogUrlOutput:
    boto3_raw_data: "type_defs.GetGameSessionLogUrlOutputTypeDef" = dataclasses.field()

    PreSignedUrl = field("PreSignedUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGameSessionLogUrlOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGameSessionLogUrlOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildsOutput:
    boto3_raw_data: "type_defs.ListBuildsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Builds(self):  # pragma: no cover
        return Build.make_many(self.boto3_raw_data["Builds"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBuildsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsOutput:
    boto3_raw_data: "type_defs.ListFleetsOutputTypeDef" = dataclasses.field()

    FleetIds = field("FleetIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFleetsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGameServersOutput:
    boto3_raw_data: "type_defs.ListGameServersOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameServers(self):  # pragma: no cover
        return GameServer.make_many(self.boto3_raw_data["GameServers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGameServersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGameServersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutScalingPolicyOutput:
    boto3_raw_data: "type_defs.PutScalingPolicyOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutScalingPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutScalingPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterGameServerOutput:
    boto3_raw_data: "type_defs.RegisterGameServerOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameServer(self):  # pragma: no cover
        return GameServer.make_one(self.boto3_raw_data["GameServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterGameServerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterGameServerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolveAliasOutput:
    boto3_raw_data: "type_defs.ResolveAliasOutputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolveAliasOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolveAliasOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFleetActionsOutput:
    boto3_raw_data: "type_defs.StartFleetActionsOutputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFleetActionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFleetActionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopFleetActionsOutput:
    boto3_raw_data: "type_defs.StopFleetActionsOutputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopFleetActionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopFleetActionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBuildOutput:
    boto3_raw_data: "type_defs.UpdateBuildOutputTypeDef" = dataclasses.field()

    @cached_property
    def Build(self):  # pragma: no cover
        return Build.make_one(self.boto3_raw_data["Build"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateBuildOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBuildOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetAttributesOutput:
    boto3_raw_data: "type_defs.UpdateFleetAttributesOutputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetAttributesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetCapacityOutput:
    boto3_raw_data: "type_defs.UpdateFleetCapacityOutputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetCapacityOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetCapacityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetPortSettingsOutput:
    boto3_raw_data: "type_defs.UpdateFleetPortSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFleetPortSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetPortSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGameServerOutput:
    boto3_raw_data: "type_defs.UpdateGameServerOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameServer(self):  # pragma: no cover
        return GameServer.make_one(self.boto3_raw_data["GameServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGameServerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGameServerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateMatchmakingRuleSetOutput:
    boto3_raw_data: "type_defs.ValidateMatchmakingRuleSetOutputTypeDef" = (
        dataclasses.field()
    )

    Valid = field("Valid")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ValidateMatchmakingRuleSetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateMatchmakingRuleSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Compute:
    boto3_raw_data: "type_defs.ComputeTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    ComputeName = field("ComputeName")
    ComputeArn = field("ComputeArn")
    IpAddress = field("IpAddress")
    DnsName = field("DnsName")
    ComputeStatus = field("ComputeStatus")
    Location = field("Location")
    CreationTime = field("CreationTime")
    OperatingSystem = field("OperatingSystem")
    Type = field("Type")
    GameLiftServiceSdkEndpoint = field("GameLiftServiceSdkEndpoint")
    GameLiftAgentEndpoint = field("GameLiftAgentEndpoint")
    InstanceId = field("InstanceId")

    @cached_property
    def ContainerAttributes(self):  # pragma: no cover
        return ContainerAttribute.make_many(self.boto3_raw_data["ContainerAttributes"])

    GameServerContainerGroupDefinitionArn = field(
        "GameServerContainerGroupDefinitionArn"
    )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComputeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetPortSettingsOutput:
    boto3_raw_data: "type_defs.DescribeFleetPortSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")

    @cached_property
    def InboundPermissions(self):  # pragma: no cover
        return IpPermission.make_many(self.boto3_raw_data["InboundPermissions"])

    UpdateStatus = field("UpdateStatus")
    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFleetPortSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetPortSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetPortSettingsInput:
    boto3_raw_data: "type_defs.UpdateFleetPortSettingsInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")

    @cached_property
    def InboundPermissionAuthorizations(self):  # pragma: no cover
        return IpPermission.make_many(
            self.boto3_raw_data["InboundPermissionAuthorizations"]
        )

    @cached_property
    def InboundPermissionRevocations(self):  # pragma: no cover
        return IpPermission.make_many(
            self.boto3_raw_data["InboundPermissionRevocations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetPortSettingsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetPortSettingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerFleet:
    boto3_raw_data: "type_defs.ContainerFleetTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    FleetRoleArn = field("FleetRoleArn")
    GameServerContainerGroupDefinitionName = field(
        "GameServerContainerGroupDefinitionName"
    )
    GameServerContainerGroupDefinitionArn = field(
        "GameServerContainerGroupDefinitionArn"
    )
    PerInstanceContainerGroupDefinitionName = field(
        "PerInstanceContainerGroupDefinitionName"
    )
    PerInstanceContainerGroupDefinitionArn = field(
        "PerInstanceContainerGroupDefinitionArn"
    )

    @cached_property
    def InstanceConnectionPortRange(self):  # pragma: no cover
        return ConnectionPortRange.make_one(
            self.boto3_raw_data["InstanceConnectionPortRange"]
        )

    @cached_property
    def InstanceInboundPermissions(self):  # pragma: no cover
        return IpPermission.make_many(self.boto3_raw_data["InstanceInboundPermissions"])

    GameServerContainerGroupsPerInstance = field("GameServerContainerGroupsPerInstance")
    MaximumGameServerContainerGroupsPerInstance = field(
        "MaximumGameServerContainerGroupsPerInstance"
    )
    InstanceType = field("InstanceType")
    BillingType = field("BillingType")
    Description = field("Description")
    CreationTime = field("CreationTime")
    MetricGroups = field("MetricGroups")
    NewGameSessionProtectionPolicy = field("NewGameSessionProtectionPolicy")

    @cached_property
    def GameSessionCreationLimitPolicy(self):  # pragma: no cover
        return GameSessionCreationLimitPolicy.make_one(
            self.boto3_raw_data["GameSessionCreationLimitPolicy"]
        )

    Status = field("Status")

    @cached_property
    def DeploymentDetails(self):  # pragma: no cover
        return DeploymentDetails.make_one(self.boto3_raw_data["DeploymentDetails"])

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["LogConfiguration"])

    @cached_property
    def LocationAttributes(self):  # pragma: no cover
        return ContainerFleetLocationAttributes.make_many(
            self.boto3_raw_data["LocationAttributes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerFleetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerFleetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComputeAccessOutput:
    boto3_raw_data: "type_defs.GetComputeAccessOutputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    ComputeName = field("ComputeName")
    ComputeArn = field("ComputeArn")

    @cached_property
    def Credentials(self):  # pragma: no cover
        return AwsCredentials.make_one(self.boto3_raw_data["Credentials"])

    Target = field("Target")

    @cached_property
    def ContainerIdentifiers(self):  # pragma: no cover
        return ContainerIdentifier.make_many(
            self.boto3_raw_data["ContainerIdentifiers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComputeAccessOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComputeAccessOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerPortConfigurationOutput:
    boto3_raw_data: "type_defs.ContainerPortConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContainerPortRanges(self):  # pragma: no cover
        return ContainerPortRange.make_many(self.boto3_raw_data["ContainerPortRanges"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContainerPortConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerPortConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerPortConfiguration:
    boto3_raw_data: "type_defs.ContainerPortConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ContainerPortRanges(self):  # pragma: no cover
        return ContainerPortRange.make_many(self.boto3_raw_data["ContainerPortRanges"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerPortConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerPortConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAliasInput:
    boto3_raw_data: "type_defs.CreateAliasInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def RoutingStrategy(self):  # pragma: no cover
        return RoutingStrategy.make_one(self.boto3_raw_data["RoutingStrategy"])

    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAliasInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationInput:
    boto3_raw_data: "type_defs.CreateLocationInputTypeDef" = dataclasses.field()

    LocationName = field("LocationName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMatchmakingRuleSetInput:
    boto3_raw_data: "type_defs.CreateMatchmakingRuleSetInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    RuleSetBody = field("RuleSetBody")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMatchmakingRuleSetInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMatchmakingRuleSetInputTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class CreateBuildInput:
    boto3_raw_data: "type_defs.CreateBuildInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Version = field("Version")

    @cached_property
    def StorageLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["StorageLocation"])

    OperatingSystem = field("OperatingSystem")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ServerSdkVersion = field("ServerSdkVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateBuildInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBuildInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBuildOutput:
    boto3_raw_data: "type_defs.CreateBuildOutputTypeDef" = dataclasses.field()

    @cached_property
    def Build(self):  # pragma: no cover
        return Build.make_one(self.boto3_raw_data["Build"])

    @cached_property
    def UploadCredentials(self):  # pragma: no cover
        return AwsCredentials.make_one(self.boto3_raw_data["UploadCredentials"])

    @cached_property
    def StorageLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["StorageLocation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateBuildOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBuildOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScriptInput:
    boto3_raw_data: "type_defs.CreateScriptInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Version = field("Version")

    @cached_property
    def StorageLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["StorageLocation"])

    ZipFile = field("ZipFile")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateScriptInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScriptInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestUploadCredentialsOutput:
    boto3_raw_data: "type_defs.RequestUploadCredentialsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UploadCredentials(self):  # pragma: no cover
        return AwsCredentials.make_one(self.boto3_raw_data["UploadCredentials"])

    @cached_property
    def StorageLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["StorageLocation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RequestUploadCredentialsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestUploadCredentialsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Script:
    boto3_raw_data: "type_defs.ScriptTypeDef" = dataclasses.field()

    ScriptId = field("ScriptId")
    ScriptArn = field("ScriptArn")
    Name = field("Name")
    Version = field("Version")
    SizeOnDisk = field("SizeOnDisk")
    CreationTime = field("CreationTime")

    @cached_property
    def StorageLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["StorageLocation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScriptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScriptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScriptInput:
    boto3_raw_data: "type_defs.UpdateScriptInputTypeDef" = dataclasses.field()

    ScriptId = field("ScriptId")
    Name = field("Name")
    Version = field("Version")

    @cached_property
    def StorageLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["StorageLocation"])

    ZipFile = field("ZipFile")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateScriptInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScriptInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerFleetInput:
    boto3_raw_data: "type_defs.CreateContainerFleetInputTypeDef" = dataclasses.field()

    FleetRoleArn = field("FleetRoleArn")
    Description = field("Description")
    GameServerContainerGroupDefinitionName = field(
        "GameServerContainerGroupDefinitionName"
    )
    PerInstanceContainerGroupDefinitionName = field(
        "PerInstanceContainerGroupDefinitionName"
    )

    @cached_property
    def InstanceConnectionPortRange(self):  # pragma: no cover
        return ConnectionPortRange.make_one(
            self.boto3_raw_data["InstanceConnectionPortRange"]
        )

    @cached_property
    def InstanceInboundPermissions(self):  # pragma: no cover
        return IpPermission.make_many(self.boto3_raw_data["InstanceInboundPermissions"])

    GameServerContainerGroupsPerInstance = field("GameServerContainerGroupsPerInstance")
    InstanceType = field("InstanceType")
    BillingType = field("BillingType")

    @cached_property
    def Locations(self):  # pragma: no cover
        return LocationConfiguration.make_many(self.boto3_raw_data["Locations"])

    MetricGroups = field("MetricGroups")
    NewGameSessionProtectionPolicy = field("NewGameSessionProtectionPolicy")

    @cached_property
    def GameSessionCreationLimitPolicy(self):  # pragma: no cover
        return GameSessionCreationLimitPolicy.make_one(
            self.boto3_raw_data["GameSessionCreationLimitPolicy"]
        )

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["LogConfiguration"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContainerFleetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetLocationsInput:
    boto3_raw_data: "type_defs.CreateFleetLocationsInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")

    @cached_property
    def Locations(self):  # pragma: no cover
        return LocationConfiguration.make_many(self.boto3_raw_data["Locations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetLocationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetLocationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetAttributes:
    boto3_raw_data: "type_defs.FleetAttributesTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    FleetType = field("FleetType")
    InstanceType = field("InstanceType")
    Description = field("Description")
    Name = field("Name")
    CreationTime = field("CreationTime")
    TerminationTime = field("TerminationTime")
    Status = field("Status")
    BuildId = field("BuildId")
    BuildArn = field("BuildArn")
    ScriptId = field("ScriptId")
    ScriptArn = field("ScriptArn")
    ServerLaunchPath = field("ServerLaunchPath")
    ServerLaunchParameters = field("ServerLaunchParameters")
    LogPaths = field("LogPaths")
    NewGameSessionProtectionPolicy = field("NewGameSessionProtectionPolicy")
    OperatingSystem = field("OperatingSystem")

    @cached_property
    def ResourceCreationLimitPolicy(self):  # pragma: no cover
        return ResourceCreationLimitPolicy.make_one(
            self.boto3_raw_data["ResourceCreationLimitPolicy"]
        )

    MetricGroups = field("MetricGroups")
    StoppedActions = field("StoppedActions")
    InstanceRoleArn = field("InstanceRoleArn")

    @cached_property
    def CertificateConfiguration(self):  # pragma: no cover
        return CertificateConfiguration.make_one(
            self.boto3_raw_data["CertificateConfiguration"]
        )

    ComputeType = field("ComputeType")

    @cached_property
    def AnywhereConfiguration(self):  # pragma: no cover
        return AnywhereConfiguration.make_one(
            self.boto3_raw_data["AnywhereConfiguration"]
        )

    InstanceRoleCredentialsProvider = field("InstanceRoleCredentialsProvider")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetAttributesInput:
    boto3_raw_data: "type_defs.UpdateFleetAttributesInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    Name = field("Name")
    Description = field("Description")
    NewGameSessionProtectionPolicy = field("NewGameSessionProtectionPolicy")

    @cached_property
    def ResourceCreationLimitPolicy(self):  # pragma: no cover
        return ResourceCreationLimitPolicy.make_one(
            self.boto3_raw_data["ResourceCreationLimitPolicy"]
        )

    MetricGroups = field("MetricGroups")

    @cached_property
    def AnywhereConfiguration(self):  # pragma: no cover
        return AnywhereConfiguration.make_one(
            self.boto3_raw_data["AnywhereConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetAttributesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetLocationsOutput:
    boto3_raw_data: "type_defs.CreateFleetLocationsOutputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")

    @cached_property
    def LocationStates(self):  # pragma: no cover
        return LocationState.make_many(self.boto3_raw_data["LocationStates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetLocationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetLocationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetLocationsOutput:
    boto3_raw_data: "type_defs.DeleteFleetLocationsOutputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")

    @cached_property
    def LocationStates(self):  # pragma: no cover
        return LocationState.make_many(self.boto3_raw_data["LocationStates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFleetLocationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetLocationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationAttributes:
    boto3_raw_data: "type_defs.LocationAttributesTypeDef" = dataclasses.field()

    @cached_property
    def LocationState(self):  # pragma: no cover
        return LocationState.make_one(self.boto3_raw_data["LocationState"])

    StoppedActions = field("StoppedActions")
    UpdateStatus = field("UpdateStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LocationAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameServerGroup:
    boto3_raw_data: "type_defs.GameServerGroupTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    GameServerGroupArn = field("GameServerGroupArn")
    RoleArn = field("RoleArn")

    @cached_property
    def InstanceDefinitions(self):  # pragma: no cover
        return InstanceDefinition.make_many(self.boto3_raw_data["InstanceDefinitions"])

    BalancingStrategy = field("BalancingStrategy")
    GameServerProtectionPolicy = field("GameServerProtectionPolicy")
    AutoScalingGroupArn = field("AutoScalingGroupArn")
    Status = field("Status")
    StatusReason = field("StatusReason")
    SuspendedActions = field("SuspendedActions")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GameServerGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GameServerGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGameServerGroupInput:
    boto3_raw_data: "type_defs.UpdateGameServerGroupInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    RoleArn = field("RoleArn")

    @cached_property
    def InstanceDefinitions(self):  # pragma: no cover
        return InstanceDefinition.make_many(self.boto3_raw_data["InstanceDefinitions"])

    GameServerProtectionPolicy = field("GameServerProtectionPolicy")
    BalancingStrategy = field("BalancingStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGameServerGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGameServerGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGameSessionInput:
    boto3_raw_data: "type_defs.CreateGameSessionInputTypeDef" = dataclasses.field()

    MaximumPlayerSessionCount = field("MaximumPlayerSessionCount")
    FleetId = field("FleetId")
    AliasId = field("AliasId")
    Name = field("Name")

    @cached_property
    def GameProperties(self):  # pragma: no cover
        return GameProperty.make_many(self.boto3_raw_data["GameProperties"])

    CreatorId = field("CreatorId")
    GameSessionId = field("GameSessionId")
    IdempotencyToken = field("IdempotencyToken")
    GameSessionData = field("GameSessionData")
    Location = field("Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGameSessionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGameSessionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMatchmakingConfigurationInput:
    boto3_raw_data: "type_defs.CreateMatchmakingConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    RequestTimeoutSeconds = field("RequestTimeoutSeconds")
    AcceptanceRequired = field("AcceptanceRequired")
    RuleSetName = field("RuleSetName")
    Description = field("Description")
    GameSessionQueueArns = field("GameSessionQueueArns")
    AcceptanceTimeoutSeconds = field("AcceptanceTimeoutSeconds")
    NotificationTarget = field("NotificationTarget")
    AdditionalPlayerCount = field("AdditionalPlayerCount")
    CustomEventData = field("CustomEventData")

    @cached_property
    def GameProperties(self):  # pragma: no cover
        return GameProperty.make_many(self.boto3_raw_data["GameProperties"])

    GameSessionData = field("GameSessionData")
    BackfillMode = field("BackfillMode")
    FlexMatchMode = field("FlexMatchMode")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMatchmakingConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMatchmakingConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameSession:
    boto3_raw_data: "type_defs.GameSessionTypeDef" = dataclasses.field()

    GameSessionId = field("GameSessionId")
    Name = field("Name")
    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    CreationTime = field("CreationTime")
    TerminationTime = field("TerminationTime")
    CurrentPlayerSessionCount = field("CurrentPlayerSessionCount")
    MaximumPlayerSessionCount = field("MaximumPlayerSessionCount")
    Status = field("Status")
    StatusReason = field("StatusReason")

    @cached_property
    def GameProperties(self):  # pragma: no cover
        return GameProperty.make_many(self.boto3_raw_data["GameProperties"])

    IpAddress = field("IpAddress")
    DnsName = field("DnsName")
    Port = field("Port")
    PlayerSessionCreationPolicy = field("PlayerSessionCreationPolicy")
    CreatorId = field("CreatorId")
    GameSessionData = field("GameSessionData")
    MatchmakerData = field("MatchmakerData")
    Location = field("Location")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GameSessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GameSessionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchmakingConfiguration:
    boto3_raw_data: "type_defs.MatchmakingConfigurationTypeDef" = dataclasses.field()

    Name = field("Name")
    ConfigurationArn = field("ConfigurationArn")
    Description = field("Description")
    GameSessionQueueArns = field("GameSessionQueueArns")
    RequestTimeoutSeconds = field("RequestTimeoutSeconds")
    AcceptanceTimeoutSeconds = field("AcceptanceTimeoutSeconds")
    AcceptanceRequired = field("AcceptanceRequired")
    RuleSetName = field("RuleSetName")
    RuleSetArn = field("RuleSetArn")
    NotificationTarget = field("NotificationTarget")
    AdditionalPlayerCount = field("AdditionalPlayerCount")
    CustomEventData = field("CustomEventData")
    CreationTime = field("CreationTime")

    @cached_property
    def GameProperties(self):  # pragma: no cover
        return GameProperty.make_many(self.boto3_raw_data["GameProperties"])

    GameSessionData = field("GameSessionData")
    BackfillMode = field("BackfillMode")
    FlexMatchMode = field("FlexMatchMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MatchmakingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchmakingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGameSessionInput:
    boto3_raw_data: "type_defs.UpdateGameSessionInputTypeDef" = dataclasses.field()

    GameSessionId = field("GameSessionId")
    MaximumPlayerSessionCount = field("MaximumPlayerSessionCount")
    Name = field("Name")
    PlayerSessionCreationPolicy = field("PlayerSessionCreationPolicy")
    ProtectionPolicy = field("ProtectionPolicy")

    @cached_property
    def GameProperties(self):  # pragma: no cover
        return GameProperty.make_many(self.boto3_raw_data["GameProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGameSessionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGameSessionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMatchmakingConfigurationInput:
    boto3_raw_data: "type_defs.UpdateMatchmakingConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Description = field("Description")
    GameSessionQueueArns = field("GameSessionQueueArns")
    RequestTimeoutSeconds = field("RequestTimeoutSeconds")
    AcceptanceTimeoutSeconds = field("AcceptanceTimeoutSeconds")
    AcceptanceRequired = field("AcceptanceRequired")
    RuleSetName = field("RuleSetName")
    NotificationTarget = field("NotificationTarget")
    AdditionalPlayerCount = field("AdditionalPlayerCount")
    CustomEventData = field("CustomEventData")

    @cached_property
    def GameProperties(self):  # pragma: no cover
        return GameProperty.make_many(self.boto3_raw_data["GameProperties"])

    GameSessionData = field("GameSessionData")
    BackfillMode = field("BackfillMode")
    FlexMatchMode = field("FlexMatchMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMatchmakingConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMatchmakingConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMatchmakingRuleSetOutput:
    boto3_raw_data: "type_defs.CreateMatchmakingRuleSetOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RuleSet(self):  # pragma: no cover
        return MatchmakingRuleSet.make_one(self.boto3_raw_data["RuleSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMatchmakingRuleSetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMatchmakingRuleSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMatchmakingRuleSetsOutput:
    boto3_raw_data: "type_defs.DescribeMatchmakingRuleSetsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RuleSets(self):  # pragma: no cover
        return MatchmakingRuleSet.make_many(self.boto3_raw_data["RuleSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMatchmakingRuleSetsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMatchmakingRuleSetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePlayerSessionOutput:
    boto3_raw_data: "type_defs.CreatePlayerSessionOutputTypeDef" = dataclasses.field()

    @cached_property
    def PlayerSession(self):  # pragma: no cover
        return PlayerSession.make_one(self.boto3_raw_data["PlayerSession"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePlayerSessionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePlayerSessionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePlayerSessionsOutput:
    boto3_raw_data: "type_defs.CreatePlayerSessionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def PlayerSessions(self):  # pragma: no cover
        return PlayerSession.make_many(self.boto3_raw_data["PlayerSessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePlayerSessionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePlayerSessionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePlayerSessionsOutput:
    boto3_raw_data: "type_defs.DescribePlayerSessionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PlayerSessions(self):  # pragma: no cover
        return PlayerSession.make_many(self.boto3_raw_data["PlayerSessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePlayerSessionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePlayerSessionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcPeeringAuthorizationOutput:
    boto3_raw_data: "type_defs.CreateVpcPeeringAuthorizationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcPeeringAuthorization(self):  # pragma: no cover
        return VpcPeeringAuthorization.make_one(
            self.boto3_raw_data["VpcPeeringAuthorization"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVpcPeeringAuthorizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcPeeringAuthorizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcPeeringAuthorizationsOutput:
    boto3_raw_data: "type_defs.DescribeVpcPeeringAuthorizationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcPeeringAuthorizations(self):  # pragma: no cover
        return VpcPeeringAuthorization.make_many(
            self.boto3_raw_data["VpcPeeringAuthorizations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVpcPeeringAuthorizationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcPeeringAuthorizationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetDeployment:
    boto3_raw_data: "type_defs.FleetDeploymentTypeDef" = dataclasses.field()

    DeploymentId = field("DeploymentId")
    FleetId = field("FleetId")
    GameServerBinaryArn = field("GameServerBinaryArn")
    RollbackGameServerBinaryArn = field("RollbackGameServerBinaryArn")
    PerInstanceBinaryArn = field("PerInstanceBinaryArn")
    RollbackPerInstanceBinaryArn = field("RollbackPerInstanceBinaryArn")
    DeploymentStatus = field("DeploymentStatus")

    @cached_property
    def DeploymentConfiguration(self):  # pragma: no cover
        return DeploymentConfiguration.make_one(
            self.boto3_raw_data["DeploymentConfiguration"]
        )

    CreationTime = field("CreationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetDeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetDeploymentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContainerFleetInput:
    boto3_raw_data: "type_defs.UpdateContainerFleetInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    GameServerContainerGroupDefinitionName = field(
        "GameServerContainerGroupDefinitionName"
    )
    PerInstanceContainerGroupDefinitionName = field(
        "PerInstanceContainerGroupDefinitionName"
    )
    GameServerContainerGroupsPerInstance = field("GameServerContainerGroupsPerInstance")

    @cached_property
    def InstanceConnectionPortRange(self):  # pragma: no cover
        return ConnectionPortRange.make_one(
            self.boto3_raw_data["InstanceConnectionPortRange"]
        )

    @cached_property
    def InstanceInboundPermissionAuthorizations(self):  # pragma: no cover
        return IpPermission.make_many(
            self.boto3_raw_data["InstanceInboundPermissionAuthorizations"]
        )

    @cached_property
    def InstanceInboundPermissionRevocations(self):  # pragma: no cover
        return IpPermission.make_many(
            self.boto3_raw_data["InstanceInboundPermissionRevocations"]
        )

    @cached_property
    def DeploymentConfiguration(self):  # pragma: no cover
        return DeploymentConfiguration.make_one(
            self.boto3_raw_data["DeploymentConfiguration"]
        )

    Description = field("Description")
    MetricGroups = field("MetricGroups")
    NewGameSessionProtectionPolicy = field("NewGameSessionProtectionPolicy")

    @cached_property
    def GameSessionCreationLimitPolicy(self):  # pragma: no cover
        return GameSessionCreationLimitPolicy.make_one(
            self.boto3_raw_data["GameSessionCreationLimitPolicy"]
        )

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["LogConfiguration"])

    RemoveAttributes = field("RemoveAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContainerFleetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContainerFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEC2InstanceLimitsOutput:
    boto3_raw_data: "type_defs.DescribeEC2InstanceLimitsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EC2InstanceLimits(self):  # pragma: no cover
        return EC2InstanceLimit.make_many(self.boto3_raw_data["EC2InstanceLimits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEC2InstanceLimitsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEC2InstanceLimitsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAttributesInputPaginate:
    boto3_raw_data: "type_defs.DescribeFleetAttributesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetIds = field("FleetIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAttributesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAttributesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetCapacityInputPaginate:
    boto3_raw_data: "type_defs.DescribeFleetCapacityInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetIds = field("FleetIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetCapacityInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetCapacityInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetUtilizationInputPaginate:
    boto3_raw_data: "type_defs.DescribeFleetUtilizationInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetIds = field("FleetIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetUtilizationInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetUtilizationInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameServerInstancesInputPaginate:
    boto3_raw_data: "type_defs.DescribeGameServerInstancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    GameServerGroupName = field("GameServerGroupName")
    InstanceIds = field("InstanceIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGameServerInstancesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameServerInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionDetailsInputPaginate:
    boto3_raw_data: "type_defs.DescribeGameSessionDetailsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    GameSessionId = field("GameSessionId")
    AliasId = field("AliasId")
    Location = field("Location")
    StatusFilter = field("StatusFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGameSessionDetailsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionDetailsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionQueuesInputPaginate:
    boto3_raw_data: "type_defs.DescribeGameSessionQueuesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGameSessionQueuesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionQueuesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionsInputPaginate:
    boto3_raw_data: "type_defs.DescribeGameSessionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    GameSessionId = field("GameSessionId")
    AliasId = field("AliasId")
    Location = field("Location")
    StatusFilter = field("StatusFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGameSessionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancesInputPaginate:
    boto3_raw_data: "type_defs.DescribeInstancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    InstanceId = field("InstanceId")
    Location = field("Location")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstancesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMatchmakingConfigurationsInputPaginate:
    boto3_raw_data: (
        "type_defs.DescribeMatchmakingConfigurationsInputPaginateTypeDef"
    ) = dataclasses.field()

    Names = field("Names")
    RuleSetName = field("RuleSetName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMatchmakingConfigurationsInputPaginateTypeDef"
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
                "type_defs.DescribeMatchmakingConfigurationsInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMatchmakingRuleSetsInputPaginate:
    boto3_raw_data: "type_defs.DescribeMatchmakingRuleSetsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMatchmakingRuleSetsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMatchmakingRuleSetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePlayerSessionsInputPaginate:
    boto3_raw_data: "type_defs.DescribePlayerSessionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    GameSessionId = field("GameSessionId")
    PlayerId = field("PlayerId")
    PlayerSessionId = field("PlayerSessionId")
    PlayerSessionStatusFilter = field("PlayerSessionStatusFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePlayerSessionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePlayerSessionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPoliciesInputPaginate:
    boto3_raw_data: "type_defs.DescribeScalingPoliciesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    StatusFilter = field("StatusFilter")
    Location = field("Location")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalingPoliciesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPoliciesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesInputPaginate:
    boto3_raw_data: "type_defs.ListAliasesInputPaginateTypeDef" = dataclasses.field()

    RoutingStrategyType = field("RoutingStrategyType")
    Name = field("Name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildsInputPaginate:
    boto3_raw_data: "type_defs.ListBuildsInputPaginateTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBuildsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputeInputPaginate:
    boto3_raw_data: "type_defs.ListComputeInputPaginateTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    Location = field("Location")
    ContainerGroupDefinitionName = field("ContainerGroupDefinitionName")
    ComputeStatus = field("ComputeStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComputeInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputeInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerFleetsInputPaginate:
    boto3_raw_data: "type_defs.ListContainerFleetsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ContainerGroupDefinitionName = field("ContainerGroupDefinitionName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContainerFleetsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerFleetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerGroupDefinitionVersionsInputPaginate:
    boto3_raw_data: (
        "type_defs.ListContainerGroupDefinitionVersionsInputPaginateTypeDef"
    ) = dataclasses.field()

    Name = field("Name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContainerGroupDefinitionVersionsInputPaginateTypeDef"
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
                "type_defs.ListContainerGroupDefinitionVersionsInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerGroupDefinitionsInputPaginate:
    boto3_raw_data: "type_defs.ListContainerGroupDefinitionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ContainerGroupType = field("ContainerGroupType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContainerGroupDefinitionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerGroupDefinitionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetDeploymentsInputPaginate:
    boto3_raw_data: "type_defs.ListFleetDeploymentsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFleetDeploymentsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetDeploymentsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsInputPaginate:
    boto3_raw_data: "type_defs.ListFleetsInputPaginateTypeDef" = dataclasses.field()

    BuildId = field("BuildId")
    ScriptId = field("ScriptId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGameServerGroupsInputPaginate:
    boto3_raw_data: "type_defs.ListGameServerGroupsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGameServerGroupsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGameServerGroupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGameServersInputPaginate:
    boto3_raw_data: "type_defs.ListGameServersInputPaginateTypeDef" = (
        dataclasses.field()
    )

    GameServerGroupName = field("GameServerGroupName")
    SortOrder = field("SortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGameServersInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGameServersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLocationsInputPaginate:
    boto3_raw_data: "type_defs.ListLocationsInputPaginateTypeDef" = dataclasses.field()

    Filters = field("Filters")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLocationsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLocationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScriptsInputPaginate:
    boto3_raw_data: "type_defs.ListScriptsInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScriptsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScriptsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchGameSessionsInputPaginate:
    boto3_raw_data: "type_defs.SearchGameSessionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    AliasId = field("AliasId")
    Location = field("Location")
    FilterExpression = field("FilterExpression")
    SortExpression = field("SortExpression")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchGameSessionsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchGameSessionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetEventsInputPaginate:
    boto3_raw_data: "type_defs.DescribeFleetEventsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFleetEventsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetEventsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetEventsInput:
    boto3_raw_data: "type_defs.DescribeFleetEventsInputTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetEventsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetEventsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetEventsOutput:
    boto3_raw_data: "type_defs.DescribeFleetEventsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["Events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetEventsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetEventsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetLocationUtilizationOutput:
    boto3_raw_data: "type_defs.DescribeFleetLocationUtilizationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FleetUtilization(self):  # pragma: no cover
        return FleetUtilization.make_one(self.boto3_raw_data["FleetUtilization"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetLocationUtilizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetLocationUtilizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetUtilizationOutput:
    boto3_raw_data: "type_defs.DescribeFleetUtilizationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FleetUtilization(self):  # pragma: no cover
        return FleetUtilization.make_many(self.boto3_raw_data["FleetUtilization"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFleetUtilizationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetUtilizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameServerInstancesOutput:
    boto3_raw_data: "type_defs.DescribeGameServerInstancesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GameServerInstances(self):  # pragma: no cover
        return GameServerInstance.make_many(self.boto3_raw_data["GameServerInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGameServerInstancesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameServerInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancesOutput:
    boto3_raw_data: "type_defs.DescribeInstancesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInstancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetCapacity:
    boto3_raw_data: "type_defs.FleetCapacityTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    InstanceType = field("InstanceType")

    @cached_property
    def InstanceCounts(self):  # pragma: no cover
        return EC2InstanceCounts.make_one(self.boto3_raw_data["InstanceCounts"])

    Location = field("Location")

    @cached_property
    def GameServerContainerGroupCounts(self):  # pragma: no cover
        return GameServerContainerGroupCounts.make_one(
            self.boto3_raw_data["GameServerContainerGroupCounts"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetCapacityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetCapacityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameServerGroupAutoScalingPolicy:
    boto3_raw_data: "type_defs.GameServerGroupAutoScalingPolicyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TargetTrackingConfiguration(self):  # pragma: no cover
        return TargetTrackingConfiguration.make_one(
            self.boto3_raw_data["TargetTrackingConfiguration"]
        )

    EstimatedInstanceWarmup = field("EstimatedInstanceWarmup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GameServerGroupAutoScalingPolicyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameServerGroupAutoScalingPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameSessionConnectionInfo:
    boto3_raw_data: "type_defs.GameSessionConnectionInfoTypeDef" = dataclasses.field()

    GameSessionArn = field("GameSessionArn")
    IpAddress = field("IpAddress")
    DnsName = field("DnsName")
    Port = field("Port")

    @cached_property
    def MatchedPlayerSessions(self):  # pragma: no cover
        return MatchedPlayerSession.make_many(
            self.boto3_raw_data["MatchedPlayerSessions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GameSessionConnectionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameSessionConnectionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameSessionPlacement:
    boto3_raw_data: "type_defs.GameSessionPlacementTypeDef" = dataclasses.field()

    PlacementId = field("PlacementId")
    GameSessionQueueName = field("GameSessionQueueName")
    Status = field("Status")

    @cached_property
    def GameProperties(self):  # pragma: no cover
        return GameProperty.make_many(self.boto3_raw_data["GameProperties"])

    MaximumPlayerSessionCount = field("MaximumPlayerSessionCount")
    GameSessionName = field("GameSessionName")
    GameSessionId = field("GameSessionId")
    GameSessionArn = field("GameSessionArn")
    GameSessionRegion = field("GameSessionRegion")

    @cached_property
    def PlayerLatencies(self):  # pragma: no cover
        return PlayerLatency.make_many(self.boto3_raw_data["PlayerLatencies"])

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    IpAddress = field("IpAddress")
    DnsName = field("DnsName")
    Port = field("Port")

    @cached_property
    def PlacedPlayerSessions(self):  # pragma: no cover
        return PlacedPlayerSession.make_many(
            self.boto3_raw_data["PlacedPlayerSessions"]
        )

    GameSessionData = field("GameSessionData")
    MatchmakerData = field("MatchmakerData")

    @cached_property
    def PriorityConfigurationOverride(self):  # pragma: no cover
        return PriorityConfigurationOverrideOutput.make_one(
            self.boto3_raw_data["PriorityConfigurationOverride"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GameSessionPlacementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameSessionPlacementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameSessionQueue:
    boto3_raw_data: "type_defs.GameSessionQueueTypeDef" = dataclasses.field()

    Name = field("Name")
    GameSessionQueueArn = field("GameSessionQueueArn")
    TimeoutInSeconds = field("TimeoutInSeconds")

    @cached_property
    def PlayerLatencyPolicies(self):  # pragma: no cover
        return PlayerLatencyPolicy.make_many(
            self.boto3_raw_data["PlayerLatencyPolicies"]
        )

    @cached_property
    def Destinations(self):  # pragma: no cover
        return GameSessionQueueDestination.make_many(
            self.boto3_raw_data["Destinations"]
        )

    @cached_property
    def FilterConfiguration(self):  # pragma: no cover
        return FilterConfigurationOutput.make_one(
            self.boto3_raw_data["FilterConfiguration"]
        )

    @cached_property
    def PriorityConfiguration(self):  # pragma: no cover
        return PriorityConfigurationOutput.make_one(
            self.boto3_raw_data["PriorityConfiguration"]
        )

    CustomEventData = field("CustomEventData")
    NotificationTarget = field("NotificationTarget")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GameSessionQueueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameSessionQueueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceAccess:
    boto3_raw_data: "type_defs.InstanceAccessTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    InstanceId = field("InstanceId")
    IpAddress = field("IpAddress")
    OperatingSystem = field("OperatingSystem")

    @cached_property
    def Credentials(self):  # pragma: no cover
        return InstanceCredentials.make_one(self.boto3_raw_data["Credentials"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceAccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceAccessTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PingBeacon:
    boto3_raw_data: "type_defs.PingBeaconTypeDef" = dataclasses.field()

    @cached_property
    def UDPEndpoint(self):  # pragma: no cover
        return UDPEndpoint.make_one(self.boto3_raw_data["UDPEndpoint"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PingBeaconTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PingBeaconTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutScalingPolicyInput:
    boto3_raw_data: "type_defs.PutScalingPolicyInputTypeDef" = dataclasses.field()

    Name = field("Name")
    FleetId = field("FleetId")
    MetricName = field("MetricName")
    ScalingAdjustment = field("ScalingAdjustment")
    ScalingAdjustmentType = field("ScalingAdjustmentType")
    Threshold = field("Threshold")
    ComparisonOperator = field("ComparisonOperator")
    EvaluationPeriods = field("EvaluationPeriods")
    PolicyType = field("PolicyType")

    @cached_property
    def TargetConfiguration(self):  # pragma: no cover
        return TargetConfiguration.make_one(self.boto3_raw_data["TargetConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutScalingPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutScalingPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingPolicy:
    boto3_raw_data: "type_defs.ScalingPolicyTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    Name = field("Name")
    Status = field("Status")
    ScalingAdjustment = field("ScalingAdjustment")
    ScalingAdjustmentType = field("ScalingAdjustmentType")
    ComparisonOperator = field("ComparisonOperator")
    Threshold = field("Threshold")
    EvaluationPeriods = field("EvaluationPeriods")
    MetricName = field("MetricName")
    PolicyType = field("PolicyType")

    @cached_property
    def TargetConfiguration(self):  # pragma: no cover
        return TargetConfiguration.make_one(self.boto3_raw_data["TargetConfiguration"])

    UpdateStatus = field("UpdateStatus")
    Location = field("Location")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScalingPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeConfigurationOutput:
    boto3_raw_data: "type_defs.RuntimeConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def ServerProcesses(self):  # pragma: no cover
        return ServerProcess.make_many(self.boto3_raw_data["ServerProcesses"])

    MaxConcurrentGameSessionActivations = field("MaxConcurrentGameSessionActivations")
    GameSessionActivationTimeoutSeconds = field("GameSessionActivationTimeoutSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeConfiguration:
    boto3_raw_data: "type_defs.RuntimeConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ServerProcesses(self):  # pragma: no cover
        return ServerProcess.make_many(self.boto3_raw_data["ServerProcesses"])

    MaxConcurrentGameSessionActivations = field("MaxConcurrentGameSessionActivations")
    GameSessionActivationTimeoutSeconds = field("GameSessionActivationTimeoutSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcPeeringConnection:
    boto3_raw_data: "type_defs.VpcPeeringConnectionTypeDef" = dataclasses.field()

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")
    IpV4CidrBlock = field("IpV4CidrBlock")
    VpcPeeringConnectionId = field("VpcPeeringConnectionId")

    @cached_property
    def Status(self):  # pragma: no cover
        return VpcPeeringConnectionStatus.make_one(self.boto3_raw_data["Status"])

    PeerVpcId = field("PeerVpcId")
    GameLiftVpcId = field("GameLiftVpcId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcPeeringConnectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcPeeringConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAliasOutput:
    boto3_raw_data: "type_defs.CreateAliasOutputTypeDef" = dataclasses.field()

    @cached_property
    def Alias(self):  # pragma: no cover
        return Alias.make_one(self.boto3_raw_data["Alias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAliasOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAliasOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAliasOutput:
    boto3_raw_data: "type_defs.DescribeAliasOutputTypeDef" = dataclasses.field()

    @cached_property
    def Alias(self):  # pragma: no cover
        return Alias.make_one(self.boto3_raw_data["Alias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAliasOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAliasOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesOutput:
    boto3_raw_data: "type_defs.ListAliasesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Aliases(self):  # pragma: no cover
        return Alias.make_many(self.boto3_raw_data["Aliases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAliasesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAliasOutput:
    boto3_raw_data: "type_defs.UpdateAliasOutputTypeDef" = dataclasses.field()

    @cached_property
    def Alias(self):  # pragma: no cover
        return Alias.make_one(self.boto3_raw_data["Alias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAliasOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAliasOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Player:
    boto3_raw_data: "type_defs.PlayerTypeDef" = dataclasses.field()

    PlayerId = field("PlayerId")
    PlayerAttributes = field("PlayerAttributes")
    Team = field("Team")
    LatencyInMs = field("LatencyInMs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlayerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlayerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComputeOutput:
    boto3_raw_data: "type_defs.DescribeComputeOutputTypeDef" = dataclasses.field()

    @cached_property
    def Compute(self):  # pragma: no cover
        return Compute.make_one(self.boto3_raw_data["Compute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeComputeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComputeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputeOutput:
    boto3_raw_data: "type_defs.ListComputeOutputTypeDef" = dataclasses.field()

    @cached_property
    def ComputeList(self):  # pragma: no cover
        return Compute.make_many(self.boto3_raw_data["ComputeList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListComputeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterComputeOutput:
    boto3_raw_data: "type_defs.RegisterComputeOutputTypeDef" = dataclasses.field()

    @cached_property
    def Compute(self):  # pragma: no cover
        return Compute.make_one(self.boto3_raw_data["Compute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterComputeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterComputeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerFleetOutput:
    boto3_raw_data: "type_defs.CreateContainerFleetOutputTypeDef" = dataclasses.field()

    @cached_property
    def ContainerFleet(self):  # pragma: no cover
        return ContainerFleet.make_one(self.boto3_raw_data["ContainerFleet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContainerFleetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerFleetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContainerFleetOutput:
    boto3_raw_data: "type_defs.DescribeContainerFleetOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContainerFleet(self):  # pragma: no cover
        return ContainerFleet.make_one(self.boto3_raw_data["ContainerFleet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeContainerFleetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContainerFleetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerFleetsOutput:
    boto3_raw_data: "type_defs.ListContainerFleetsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ContainerFleets(self):  # pragma: no cover
        return ContainerFleet.make_many(self.boto3_raw_data["ContainerFleets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContainerFleetsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerFleetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContainerFleetOutput:
    boto3_raw_data: "type_defs.UpdateContainerFleetOutputTypeDef" = dataclasses.field()

    @cached_property
    def ContainerFleet(self):  # pragma: no cover
        return ContainerFleet.make_one(self.boto3_raw_data["ContainerFleet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContainerFleetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContainerFleetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameServerContainerDefinition:
    boto3_raw_data: "type_defs.GameServerContainerDefinitionTypeDef" = (
        dataclasses.field()
    )

    ContainerName = field("ContainerName")

    @cached_property
    def DependsOn(self):  # pragma: no cover
        return ContainerDependency.make_many(self.boto3_raw_data["DependsOn"])

    @cached_property
    def MountPoints(self):  # pragma: no cover
        return ContainerMountPoint.make_many(self.boto3_raw_data["MountPoints"])

    @cached_property
    def EnvironmentOverride(self):  # pragma: no cover
        return ContainerEnvironment.make_many(
            self.boto3_raw_data["EnvironmentOverride"]
        )

    ImageUri = field("ImageUri")

    @cached_property
    def PortConfiguration(self):  # pragma: no cover
        return ContainerPortConfigurationOutput.make_one(
            self.boto3_raw_data["PortConfiguration"]
        )

    ResolvedImageDigest = field("ResolvedImageDigest")
    ServerSdkVersion = field("ServerSdkVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GameServerContainerDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameServerContainerDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportContainerDefinition:
    boto3_raw_data: "type_defs.SupportContainerDefinitionTypeDef" = dataclasses.field()

    ContainerName = field("ContainerName")

    @cached_property
    def DependsOn(self):  # pragma: no cover
        return ContainerDependency.make_many(self.boto3_raw_data["DependsOn"])

    @cached_property
    def MountPoints(self):  # pragma: no cover
        return ContainerMountPoint.make_many(self.boto3_raw_data["MountPoints"])

    @cached_property
    def EnvironmentOverride(self):  # pragma: no cover
        return ContainerEnvironment.make_many(
            self.boto3_raw_data["EnvironmentOverride"]
        )

    Essential = field("Essential")

    @cached_property
    def HealthCheck(self):  # pragma: no cover
        return ContainerHealthCheckOutput.make_one(self.boto3_raw_data["HealthCheck"])

    ImageUri = field("ImageUri")
    MemoryHardLimitMebibytes = field("MemoryHardLimitMebibytes")

    @cached_property
    def PortConfiguration(self):  # pragma: no cover
        return ContainerPortConfigurationOutput.make_one(
            self.boto3_raw_data["PortConfiguration"]
        )

    ResolvedImageDigest = field("ResolvedImageDigest")
    Vcpu = field("Vcpu")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SupportContainerDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportContainerDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScriptOutput:
    boto3_raw_data: "type_defs.CreateScriptOutputTypeDef" = dataclasses.field()

    @cached_property
    def Script(self):  # pragma: no cover
        return Script.make_one(self.boto3_raw_data["Script"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScriptOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScriptOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScriptOutput:
    boto3_raw_data: "type_defs.DescribeScriptOutputTypeDef" = dataclasses.field()

    @cached_property
    def Script(self):  # pragma: no cover
        return Script.make_one(self.boto3_raw_data["Script"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeScriptOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScriptOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScriptsOutput:
    boto3_raw_data: "type_defs.ListScriptsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Scripts(self):  # pragma: no cover
        return Script.make_many(self.boto3_raw_data["Scripts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListScriptsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScriptsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScriptOutput:
    boto3_raw_data: "type_defs.UpdateScriptOutputTypeDef" = dataclasses.field()

    @cached_property
    def Script(self):  # pragma: no cover
        return Script.make_one(self.boto3_raw_data["Script"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateScriptOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScriptOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetOutput:
    boto3_raw_data: "type_defs.CreateFleetOutputTypeDef" = dataclasses.field()

    @cached_property
    def FleetAttributes(self):  # pragma: no cover
        return FleetAttributes.make_one(self.boto3_raw_data["FleetAttributes"])

    @cached_property
    def LocationStates(self):  # pragma: no cover
        return LocationState.make_many(self.boto3_raw_data["LocationStates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFleetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAttributesOutput:
    boto3_raw_data: "type_defs.DescribeFleetAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FleetAttributes(self):  # pragma: no cover
        return FleetAttributes.make_many(self.boto3_raw_data["FleetAttributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFleetAttributesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetLocationAttributesOutput:
    boto3_raw_data: "type_defs.DescribeFleetLocationAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    FleetArn = field("FleetArn")

    @cached_property
    def LocationAttributes(self):  # pragma: no cover
        return LocationAttributes.make_many(self.boto3_raw_data["LocationAttributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetLocationAttributesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetLocationAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGameServerGroupOutput:
    boto3_raw_data: "type_defs.CreateGameServerGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameServerGroup(self):  # pragma: no cover
        return GameServerGroup.make_one(self.boto3_raw_data["GameServerGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGameServerGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGameServerGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGameServerGroupOutput:
    boto3_raw_data: "type_defs.DeleteGameServerGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameServerGroup(self):  # pragma: no cover
        return GameServerGroup.make_one(self.boto3_raw_data["GameServerGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGameServerGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGameServerGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameServerGroupOutput:
    boto3_raw_data: "type_defs.DescribeGameServerGroupOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GameServerGroup(self):  # pragma: no cover
        return GameServerGroup.make_one(self.boto3_raw_data["GameServerGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGameServerGroupOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameServerGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGameServerGroupsOutput:
    boto3_raw_data: "type_defs.ListGameServerGroupsOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameServerGroups(self):  # pragma: no cover
        return GameServerGroup.make_many(self.boto3_raw_data["GameServerGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGameServerGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGameServerGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeGameServerGroupOutput:
    boto3_raw_data: "type_defs.ResumeGameServerGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameServerGroup(self):  # pragma: no cover
        return GameServerGroup.make_one(self.boto3_raw_data["GameServerGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeGameServerGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeGameServerGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuspendGameServerGroupOutput:
    boto3_raw_data: "type_defs.SuspendGameServerGroupOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GameServerGroup(self):  # pragma: no cover
        return GameServerGroup.make_one(self.boto3_raw_data["GameServerGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuspendGameServerGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuspendGameServerGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGameServerGroupOutput:
    boto3_raw_data: "type_defs.UpdateGameServerGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameServerGroup(self):  # pragma: no cover
        return GameServerGroup.make_one(self.boto3_raw_data["GameServerGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGameServerGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGameServerGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGameSessionOutput:
    boto3_raw_data: "type_defs.CreateGameSessionOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameSession(self):  # pragma: no cover
        return GameSession.make_one(self.boto3_raw_data["GameSession"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGameSessionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGameSessionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionsOutput:
    boto3_raw_data: "type_defs.DescribeGameSessionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameSessions(self):  # pragma: no cover
        return GameSession.make_many(self.boto3_raw_data["GameSessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGameSessionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameSessionDetail:
    boto3_raw_data: "type_defs.GameSessionDetailTypeDef" = dataclasses.field()

    @cached_property
    def GameSession(self):  # pragma: no cover
        return GameSession.make_one(self.boto3_raw_data["GameSession"])

    ProtectionPolicy = field("ProtectionPolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GameSessionDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameSessionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchGameSessionsOutput:
    boto3_raw_data: "type_defs.SearchGameSessionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameSessions(self):  # pragma: no cover
        return GameSession.make_many(self.boto3_raw_data["GameSessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchGameSessionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchGameSessionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateGameSessionOutput:
    boto3_raw_data: "type_defs.TerminateGameSessionOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameSession(self):  # pragma: no cover
        return GameSession.make_one(self.boto3_raw_data["GameSession"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateGameSessionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateGameSessionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGameSessionOutput:
    boto3_raw_data: "type_defs.UpdateGameSessionOutputTypeDef" = dataclasses.field()

    @cached_property
    def GameSession(self):  # pragma: no cover
        return GameSession.make_one(self.boto3_raw_data["GameSession"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGameSessionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGameSessionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMatchmakingConfigurationOutput:
    boto3_raw_data: "type_defs.CreateMatchmakingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Configuration(self):  # pragma: no cover
        return MatchmakingConfiguration.make_one(self.boto3_raw_data["Configuration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMatchmakingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMatchmakingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMatchmakingConfigurationsOutput:
    boto3_raw_data: "type_defs.DescribeMatchmakingConfigurationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Configurations(self):  # pragma: no cover
        return MatchmakingConfiguration.make_many(self.boto3_raw_data["Configurations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMatchmakingConfigurationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMatchmakingConfigurationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMatchmakingConfigurationOutput:
    boto3_raw_data: "type_defs.UpdateMatchmakingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Configuration(self):  # pragma: no cover
        return MatchmakingConfiguration.make_one(self.boto3_raw_data["Configuration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMatchmakingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMatchmakingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetDeploymentOutput:
    boto3_raw_data: "type_defs.DescribeFleetDeploymentOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FleetDeployment(self):  # pragma: no cover
        return FleetDeployment.make_one(self.boto3_raw_data["FleetDeployment"])

    LocationalDeployments = field("LocationalDeployments")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFleetDeploymentOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetDeploymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetDeploymentsOutput:
    boto3_raw_data: "type_defs.ListFleetDeploymentsOutputTypeDef" = dataclasses.field()

    @cached_property
    def FleetDeployments(self):  # pragma: no cover
        return FleetDeployment.make_many(self.boto3_raw_data["FleetDeployments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetDeploymentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetDeploymentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetCapacityOutput:
    boto3_raw_data: "type_defs.DescribeFleetCapacityOutputTypeDef" = dataclasses.field()

    @cached_property
    def FleetCapacity(self):  # pragma: no cover
        return FleetCapacity.make_many(self.boto3_raw_data["FleetCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetCapacityOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetCapacityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetLocationCapacityOutput:
    boto3_raw_data: "type_defs.DescribeFleetLocationCapacityOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FleetCapacity(self):  # pragma: no cover
        return FleetCapacity.make_one(self.boto3_raw_data["FleetCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetLocationCapacityOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetLocationCapacityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGameServerGroupInput:
    boto3_raw_data: "type_defs.CreateGameServerGroupInputTypeDef" = dataclasses.field()

    GameServerGroupName = field("GameServerGroupName")
    RoleArn = field("RoleArn")
    MinSize = field("MinSize")
    MaxSize = field("MaxSize")

    @cached_property
    def LaunchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplate"]
        )

    @cached_property
    def InstanceDefinitions(self):  # pragma: no cover
        return InstanceDefinition.make_many(self.boto3_raw_data["InstanceDefinitions"])

    @cached_property
    def AutoScalingPolicy(self):  # pragma: no cover
        return GameServerGroupAutoScalingPolicy.make_one(
            self.boto3_raw_data["AutoScalingPolicy"]
        )

    BalancingStrategy = field("BalancingStrategy")
    GameServerProtectionPolicy = field("GameServerProtectionPolicy")
    VpcSubnets = field("VpcSubnets")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGameServerGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGameServerGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchmakingTicket:
    boto3_raw_data: "type_defs.MatchmakingTicketTypeDef" = dataclasses.field()

    TicketId = field("TicketId")
    ConfigurationName = field("ConfigurationName")
    ConfigurationArn = field("ConfigurationArn")
    Status = field("Status")
    StatusReason = field("StatusReason")
    StatusMessage = field("StatusMessage")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def Players(self):  # pragma: no cover
        return PlayerOutput.make_many(self.boto3_raw_data["Players"])

    @cached_property
    def GameSessionConnectionInfo(self):  # pragma: no cover
        return GameSessionConnectionInfo.make_one(
            self.boto3_raw_data["GameSessionConnectionInfo"]
        )

    EstimatedWaitTime = field("EstimatedWaitTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchmakingTicketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchmakingTicketTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionPlacementOutput:
    boto3_raw_data: "type_defs.DescribeGameSessionPlacementOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GameSessionPlacement(self):  # pragma: no cover
        return GameSessionPlacement.make_one(
            self.boto3_raw_data["GameSessionPlacement"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGameSessionPlacementOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionPlacementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartGameSessionPlacementOutput:
    boto3_raw_data: "type_defs.StartGameSessionPlacementOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GameSessionPlacement(self):  # pragma: no cover
        return GameSessionPlacement.make_one(
            self.boto3_raw_data["GameSessionPlacement"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartGameSessionPlacementOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartGameSessionPlacementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopGameSessionPlacementOutput:
    boto3_raw_data: "type_defs.StopGameSessionPlacementOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GameSessionPlacement(self):  # pragma: no cover
        return GameSessionPlacement.make_one(
            self.boto3_raw_data["GameSessionPlacement"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopGameSessionPlacementOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopGameSessionPlacementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGameSessionQueueOutput:
    boto3_raw_data: "type_defs.CreateGameSessionQueueOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GameSessionQueue(self):  # pragma: no cover
        return GameSessionQueue.make_one(self.boto3_raw_data["GameSessionQueue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGameSessionQueueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGameSessionQueueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionQueuesOutput:
    boto3_raw_data: "type_defs.DescribeGameSessionQueuesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GameSessionQueues(self):  # pragma: no cover
        return GameSessionQueue.make_many(self.boto3_raw_data["GameSessionQueues"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGameSessionQueuesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionQueuesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGameSessionQueueOutput:
    boto3_raw_data: "type_defs.UpdateGameSessionQueueOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GameSessionQueue(self):  # pragma: no cover
        return GameSessionQueue.make_one(self.boto3_raw_data["GameSessionQueue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGameSessionQueueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGameSessionQueueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceAccessOutput:
    boto3_raw_data: "type_defs.GetInstanceAccessOutputTypeDef" = dataclasses.field()

    @cached_property
    def InstanceAccess(self):  # pragma: no cover
        return InstanceAccess.make_one(self.boto3_raw_data["InstanceAccess"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceAccessOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceAccessOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationModel:
    boto3_raw_data: "type_defs.LocationModelTypeDef" = dataclasses.field()

    LocationName = field("LocationName")
    LocationArn = field("LocationArn")

    @cached_property
    def PingBeacon(self):  # pragma: no cover
        return PingBeacon.make_one(self.boto3_raw_data["PingBeacon"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationModelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartGameSessionPlacementInput:
    boto3_raw_data: "type_defs.StartGameSessionPlacementInputTypeDef" = (
        dataclasses.field()
    )

    PlacementId = field("PlacementId")
    GameSessionQueueName = field("GameSessionQueueName")
    MaximumPlayerSessionCount = field("MaximumPlayerSessionCount")

    @cached_property
    def GameProperties(self):  # pragma: no cover
        return GameProperty.make_many(self.boto3_raw_data["GameProperties"])

    GameSessionName = field("GameSessionName")

    @cached_property
    def PlayerLatencies(self):  # pragma: no cover
        return PlayerLatency.make_many(self.boto3_raw_data["PlayerLatencies"])

    @cached_property
    def DesiredPlayerSessions(self):  # pragma: no cover
        return DesiredPlayerSession.make_many(
            self.boto3_raw_data["DesiredPlayerSessions"]
        )

    GameSessionData = field("GameSessionData")
    PriorityConfigurationOverride = field("PriorityConfigurationOverride")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartGameSessionPlacementInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartGameSessionPlacementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGameSessionQueueInput:
    boto3_raw_data: "type_defs.CreateGameSessionQueueInputTypeDef" = dataclasses.field()

    Name = field("Name")
    TimeoutInSeconds = field("TimeoutInSeconds")

    @cached_property
    def PlayerLatencyPolicies(self):  # pragma: no cover
        return PlayerLatencyPolicy.make_many(
            self.boto3_raw_data["PlayerLatencyPolicies"]
        )

    @cached_property
    def Destinations(self):  # pragma: no cover
        return GameSessionQueueDestination.make_many(
            self.boto3_raw_data["Destinations"]
        )

    FilterConfiguration = field("FilterConfiguration")
    PriorityConfiguration = field("PriorityConfiguration")
    CustomEventData = field("CustomEventData")
    NotificationTarget = field("NotificationTarget")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGameSessionQueueInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGameSessionQueueInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGameSessionQueueInput:
    boto3_raw_data: "type_defs.UpdateGameSessionQueueInputTypeDef" = dataclasses.field()

    Name = field("Name")
    TimeoutInSeconds = field("TimeoutInSeconds")

    @cached_property
    def PlayerLatencyPolicies(self):  # pragma: no cover
        return PlayerLatencyPolicy.make_many(
            self.boto3_raw_data["PlayerLatencyPolicies"]
        )

    @cached_property
    def Destinations(self):  # pragma: no cover
        return GameSessionQueueDestination.make_many(
            self.boto3_raw_data["Destinations"]
        )

    FilterConfiguration = field("FilterConfiguration")
    PriorityConfiguration = field("PriorityConfiguration")
    CustomEventData = field("CustomEventData")
    NotificationTarget = field("NotificationTarget")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGameSessionQueueInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGameSessionQueueInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPoliciesOutput:
    boto3_raw_data: "type_defs.DescribeScalingPoliciesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScalingPolicies(self):  # pragma: no cover
        return ScalingPolicy.make_many(self.boto3_raw_data["ScalingPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScalingPoliciesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPoliciesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuntimeConfigurationOutput:
    boto3_raw_data: "type_defs.DescribeRuntimeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RuntimeConfiguration(self):  # pragma: no cover
        return RuntimeConfigurationOutput.make_one(
            self.boto3_raw_data["RuntimeConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRuntimeConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuntimeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuntimeConfigurationOutput:
    boto3_raw_data: "type_defs.UpdateRuntimeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RuntimeConfiguration(self):  # pragma: no cover
        return RuntimeConfigurationOutput.make_one(
            self.boto3_raw_data["RuntimeConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRuntimeConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuntimeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcPeeringConnectionsOutput:
    boto3_raw_data: "type_defs.DescribeVpcPeeringConnectionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcPeeringConnections(self):  # pragma: no cover
        return VpcPeeringConnection.make_many(
            self.boto3_raw_data["VpcPeeringConnections"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVpcPeeringConnectionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcPeeringConnectionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerGroupDefinition:
    boto3_raw_data: "type_defs.ContainerGroupDefinitionTypeDef" = dataclasses.field()

    Name = field("Name")
    ContainerGroupDefinitionArn = field("ContainerGroupDefinitionArn")
    CreationTime = field("CreationTime")
    OperatingSystem = field("OperatingSystem")
    ContainerGroupType = field("ContainerGroupType")
    TotalMemoryLimitMebibytes = field("TotalMemoryLimitMebibytes")
    TotalVcpuLimit = field("TotalVcpuLimit")

    @cached_property
    def GameServerContainerDefinition(self):  # pragma: no cover
        return GameServerContainerDefinition.make_one(
            self.boto3_raw_data["GameServerContainerDefinition"]
        )

    @cached_property
    def SupportContainerDefinitions(self):  # pragma: no cover
        return SupportContainerDefinition.make_many(
            self.boto3_raw_data["SupportContainerDefinitions"]
        )

    VersionNumber = field("VersionNumber")
    VersionDescription = field("VersionDescription")
    Status = field("Status")
    StatusReason = field("StatusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerGroupDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerGroupDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GameServerContainerDefinitionInput:
    boto3_raw_data: "type_defs.GameServerContainerDefinitionInputTypeDef" = (
        dataclasses.field()
    )

    ContainerName = field("ContainerName")
    ImageUri = field("ImageUri")
    PortConfiguration = field("PortConfiguration")
    ServerSdkVersion = field("ServerSdkVersion")

    @cached_property
    def DependsOn(self):  # pragma: no cover
        return ContainerDependency.make_many(self.boto3_raw_data["DependsOn"])

    @cached_property
    def MountPoints(self):  # pragma: no cover
        return ContainerMountPoint.make_many(self.boto3_raw_data["MountPoints"])

    @cached_property
    def EnvironmentOverride(self):  # pragma: no cover
        return ContainerEnvironment.make_many(
            self.boto3_raw_data["EnvironmentOverride"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GameServerContainerDefinitionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GameServerContainerDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportContainerDefinitionInput:
    boto3_raw_data: "type_defs.SupportContainerDefinitionInputTypeDef" = (
        dataclasses.field()
    )

    ContainerName = field("ContainerName")
    ImageUri = field("ImageUri")

    @cached_property
    def DependsOn(self):  # pragma: no cover
        return ContainerDependency.make_many(self.boto3_raw_data["DependsOn"])

    @cached_property
    def MountPoints(self):  # pragma: no cover
        return ContainerMountPoint.make_many(self.boto3_raw_data["MountPoints"])

    @cached_property
    def EnvironmentOverride(self):  # pragma: no cover
        return ContainerEnvironment.make_many(
            self.boto3_raw_data["EnvironmentOverride"]
        )

    Essential = field("Essential")
    HealthCheck = field("HealthCheck")
    MemoryHardLimitMebibytes = field("MemoryHardLimitMebibytes")
    PortConfiguration = field("PortConfiguration")
    Vcpu = field("Vcpu")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SupportContainerDefinitionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportContainerDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGameSessionDetailsOutput:
    boto3_raw_data: "type_defs.DescribeGameSessionDetailsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GameSessionDetails(self):  # pragma: no cover
        return GameSessionDetail.make_many(self.boto3_raw_data["GameSessionDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGameSessionDetailsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGameSessionDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMatchmakingOutput:
    boto3_raw_data: "type_defs.DescribeMatchmakingOutputTypeDef" = dataclasses.field()

    @cached_property
    def TicketList(self):  # pragma: no cover
        return MatchmakingTicket.make_many(self.boto3_raw_data["TicketList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMatchmakingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMatchmakingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMatchBackfillOutput:
    boto3_raw_data: "type_defs.StartMatchBackfillOutputTypeDef" = dataclasses.field()

    @cached_property
    def MatchmakingTicket(self):  # pragma: no cover
        return MatchmakingTicket.make_one(self.boto3_raw_data["MatchmakingTicket"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMatchBackfillOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMatchBackfillOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMatchmakingOutput:
    boto3_raw_data: "type_defs.StartMatchmakingOutputTypeDef" = dataclasses.field()

    @cached_property
    def MatchmakingTicket(self):  # pragma: no cover
        return MatchmakingTicket.make_one(self.boto3_raw_data["MatchmakingTicket"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMatchmakingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMatchmakingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationOutput:
    boto3_raw_data: "type_defs.CreateLocationOutputTypeDef" = dataclasses.field()

    @cached_property
    def Location(self):  # pragma: no cover
        return LocationModel.make_one(self.boto3_raw_data["Location"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLocationsOutput:
    boto3_raw_data: "type_defs.ListLocationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Locations(self):  # pragma: no cover
        return LocationModel.make_many(self.boto3_raw_data["Locations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLocationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLocationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetInput:
    boto3_raw_data: "type_defs.CreateFleetInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    BuildId = field("BuildId")
    ScriptId = field("ScriptId")
    ServerLaunchPath = field("ServerLaunchPath")
    ServerLaunchParameters = field("ServerLaunchParameters")
    LogPaths = field("LogPaths")
    EC2InstanceType = field("EC2InstanceType")

    @cached_property
    def EC2InboundPermissions(self):  # pragma: no cover
        return IpPermission.make_many(self.boto3_raw_data["EC2InboundPermissions"])

    NewGameSessionProtectionPolicy = field("NewGameSessionProtectionPolicy")
    RuntimeConfiguration = field("RuntimeConfiguration")

    @cached_property
    def ResourceCreationLimitPolicy(self):  # pragma: no cover
        return ResourceCreationLimitPolicy.make_one(
            self.boto3_raw_data["ResourceCreationLimitPolicy"]
        )

    MetricGroups = field("MetricGroups")
    PeerVpcAwsAccountId = field("PeerVpcAwsAccountId")
    PeerVpcId = field("PeerVpcId")
    FleetType = field("FleetType")
    InstanceRoleArn = field("InstanceRoleArn")

    @cached_property
    def CertificateConfiguration(self):  # pragma: no cover
        return CertificateConfiguration.make_one(
            self.boto3_raw_data["CertificateConfiguration"]
        )

    @cached_property
    def Locations(self):  # pragma: no cover
        return LocationConfiguration.make_many(self.boto3_raw_data["Locations"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ComputeType = field("ComputeType")

    @cached_property
    def AnywhereConfiguration(self):  # pragma: no cover
        return AnywhereConfiguration.make_one(
            self.boto3_raw_data["AnywhereConfiguration"]
        )

    InstanceRoleCredentialsProvider = field("InstanceRoleCredentialsProvider")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFleetInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuntimeConfigurationInput:
    boto3_raw_data: "type_defs.UpdateRuntimeConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    FleetId = field("FleetId")
    RuntimeConfiguration = field("RuntimeConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRuntimeConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuntimeConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMatchBackfillInput:
    boto3_raw_data: "type_defs.StartMatchBackfillInputTypeDef" = dataclasses.field()

    ConfigurationName = field("ConfigurationName")
    Players = field("Players")
    TicketId = field("TicketId")
    GameSessionArn = field("GameSessionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMatchBackfillInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMatchBackfillInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMatchmakingInput:
    boto3_raw_data: "type_defs.StartMatchmakingInputTypeDef" = dataclasses.field()

    ConfigurationName = field("ConfigurationName")
    Players = field("Players")
    TicketId = field("TicketId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMatchmakingInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMatchmakingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerGroupDefinitionOutput:
    boto3_raw_data: "type_defs.CreateContainerGroupDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContainerGroupDefinition(self):  # pragma: no cover
        return ContainerGroupDefinition.make_one(
            self.boto3_raw_data["ContainerGroupDefinition"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateContainerGroupDefinitionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerGroupDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContainerGroupDefinitionOutput:
    boto3_raw_data: "type_defs.DescribeContainerGroupDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContainerGroupDefinition(self):  # pragma: no cover
        return ContainerGroupDefinition.make_one(
            self.boto3_raw_data["ContainerGroupDefinition"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeContainerGroupDefinitionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContainerGroupDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerGroupDefinitionVersionsOutput:
    boto3_raw_data: "type_defs.ListContainerGroupDefinitionVersionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContainerGroupDefinitions(self):  # pragma: no cover
        return ContainerGroupDefinition.make_many(
            self.boto3_raw_data["ContainerGroupDefinitions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContainerGroupDefinitionVersionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerGroupDefinitionVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerGroupDefinitionsOutput:
    boto3_raw_data: "type_defs.ListContainerGroupDefinitionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContainerGroupDefinitions(self):  # pragma: no cover
        return ContainerGroupDefinition.make_many(
            self.boto3_raw_data["ContainerGroupDefinitions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContainerGroupDefinitionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerGroupDefinitionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContainerGroupDefinitionOutput:
    boto3_raw_data: "type_defs.UpdateContainerGroupDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContainerGroupDefinition(self):  # pragma: no cover
        return ContainerGroupDefinition.make_one(
            self.boto3_raw_data["ContainerGroupDefinition"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateContainerGroupDefinitionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContainerGroupDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerGroupDefinitionInput:
    boto3_raw_data: "type_defs.CreateContainerGroupDefinitionInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    TotalMemoryLimitMebibytes = field("TotalMemoryLimitMebibytes")
    TotalVcpuLimit = field("TotalVcpuLimit")
    OperatingSystem = field("OperatingSystem")
    ContainerGroupType = field("ContainerGroupType")

    @cached_property
    def GameServerContainerDefinition(self):  # pragma: no cover
        return GameServerContainerDefinitionInput.make_one(
            self.boto3_raw_data["GameServerContainerDefinition"]
        )

    @cached_property
    def SupportContainerDefinitions(self):  # pragma: no cover
        return SupportContainerDefinitionInput.make_many(
            self.boto3_raw_data["SupportContainerDefinitions"]
        )

    VersionDescription = field("VersionDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateContainerGroupDefinitionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerGroupDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContainerGroupDefinitionInput:
    boto3_raw_data: "type_defs.UpdateContainerGroupDefinitionInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def GameServerContainerDefinition(self):  # pragma: no cover
        return GameServerContainerDefinitionInput.make_one(
            self.boto3_raw_data["GameServerContainerDefinition"]
        )

    @cached_property
    def SupportContainerDefinitions(self):  # pragma: no cover
        return SupportContainerDefinitionInput.make_many(
            self.boto3_raw_data["SupportContainerDefinitions"]
        )

    TotalMemoryLimitMebibytes = field("TotalMemoryLimitMebibytes")
    TotalVcpuLimit = field("TotalVcpuLimit")
    VersionDescription = field("VersionDescription")
    SourceVersionNumber = field("SourceVersionNumber")
    OperatingSystem = field("OperatingSystem")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateContainerGroupDefinitionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContainerGroupDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
