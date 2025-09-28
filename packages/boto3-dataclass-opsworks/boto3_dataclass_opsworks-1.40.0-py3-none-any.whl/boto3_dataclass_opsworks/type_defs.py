# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_opsworks import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class StackConfigurationManager:
    boto3_raw_data: "type_defs.StackConfigurationManagerTypeDef" = dataclasses.field()

    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackConfigurationManagerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackConfigurationManagerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSource:
    boto3_raw_data: "type_defs.DataSourceTypeDef" = dataclasses.field()

    Type = field("Type")
    Arn = field("Arn")
    DatabaseName = field("DatabaseName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentVariable:
    boto3_raw_data: "type_defs.EnvironmentVariableTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    Secure = field("Secure")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentVariableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Source:
    boto3_raw_data: "type_defs.SourceTypeDef" = dataclasses.field()

    Type = field("Type")
    Url = field("Url")
    Username = field("Username")
    Password = field("Password")
    SshKey = field("SshKey")
    Revision = field("Revision")

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
class SslConfiguration:
    boto3_raw_data: "type_defs.SslConfigurationTypeDef" = dataclasses.field()

    Certificate = field("Certificate")
    PrivateKey = field("PrivateKey")
    Chain = field("Chain")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SslConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SslConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignInstanceRequest:
    boto3_raw_data: "type_defs.AssignInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    LayerIds = field("LayerIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssignInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignVolumeRequest:
    boto3_raw_data: "type_defs.AssignVolumeRequestTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssignVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateElasticIpRequest:
    boto3_raw_data: "type_defs.AssociateElasticIpRequestTypeDef" = dataclasses.field()

    ElasticIp = field("ElasticIp")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateElasticIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateElasticIpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachElasticLoadBalancerRequest:
    boto3_raw_data: "type_defs.AttachElasticLoadBalancerRequestTypeDef" = (
        dataclasses.field()
    )

    ElasticLoadBalancerName = field("ElasticLoadBalancerName")
    LayerId = field("LayerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AttachElasticLoadBalancerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachElasticLoadBalancerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingThresholdsOutput:
    boto3_raw_data: "type_defs.AutoScalingThresholdsOutputTypeDef" = dataclasses.field()

    InstanceCount = field("InstanceCount")
    ThresholdsWaitTime = field("ThresholdsWaitTime")
    IgnoreMetricsTime = field("IgnoreMetricsTime")
    CpuThreshold = field("CpuThreshold")
    MemoryThreshold = field("MemoryThreshold")
    LoadThreshold = field("LoadThreshold")
    Alarms = field("Alarms")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingThresholdsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingThresholdsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingThresholds:
    boto3_raw_data: "type_defs.AutoScalingThresholdsTypeDef" = dataclasses.field()

    InstanceCount = field("InstanceCount")
    ThresholdsWaitTime = field("ThresholdsWaitTime")
    IgnoreMetricsTime = field("IgnoreMetricsTime")
    CpuThreshold = field("CpuThreshold")
    MemoryThreshold = field("MemoryThreshold")
    LoadThreshold = field("LoadThreshold")
    Alarms = field("Alarms")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingThresholdsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingThresholdsTypeDef"]
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

    SnapshotId = field("SnapshotId")
    Iops = field("Iops")
    VolumeSize = field("VolumeSize")
    VolumeType = field("VolumeType")
    DeleteOnTermination = field("DeleteOnTermination")

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
class ChefConfiguration:
    boto3_raw_data: "type_defs.ChefConfigurationTypeDef" = dataclasses.field()

    ManageBerkshelf = field("ManageBerkshelf")
    BerkshelfVersion = field("BerkshelfVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChefConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChefConfigurationTypeDef"]
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
class CloudWatchLogsLogStream:
    boto3_raw_data: "type_defs.CloudWatchLogsLogStreamTypeDef" = dataclasses.field()

    LogGroupName = field("LogGroupName")
    DatetimeFormat = field("DatetimeFormat")
    TimeZone = field("TimeZone")
    File = field("File")
    FileFingerprintLines = field("FileFingerprintLines")
    MultiLineStartPattern = field("MultiLineStartPattern")
    InitialPosition = field("InitialPosition")
    Encoding = field("Encoding")
    BufferDuration = field("BufferDuration")
    BatchCount = field("BatchCount")
    BatchSize = field("BatchSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogsLogStreamTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsLogStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Command:
    boto3_raw_data: "type_defs.CommandTypeDef" = dataclasses.field()

    CommandId = field("CommandId")
    InstanceId = field("InstanceId")
    DeploymentId = field("DeploymentId")
    CreatedAt = field("CreatedAt")
    AcknowledgedAt = field("AcknowledgedAt")
    CompletedAt = field("CompletedAt")
    Status = field("Status")
    ExitCode = field("ExitCode")
    LogUrl = field("LogUrl")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommandTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommandTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeConfiguration:
    boto3_raw_data: "type_defs.VolumeConfigurationTypeDef" = dataclasses.field()

    MountPoint = field("MountPoint")
    NumberOfDisks = field("NumberOfDisks")
    Size = field("Size")
    RaidLevel = field("RaidLevel")
    VolumeType = field("VolumeType")
    Iops = field("Iops")
    Encrypted = field("Encrypted")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VolumeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserProfileRequest:
    boto3_raw_data: "type_defs.CreateUserProfileRequestTypeDef" = dataclasses.field()

    IamUserArn = field("IamUserArn")
    SshUsername = field("SshUsername")
    SshPublicKey = field("SshPublicKey")
    AllowSelfManagement = field("AllowSelfManagement")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppRequest:
    boto3_raw_data: "type_defs.DeleteAppRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceRequest:
    boto3_raw_data: "type_defs.DeleteInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    DeleteElasticIp = field("DeleteElasticIp")
    DeleteVolumes = field("DeleteVolumes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLayerRequest:
    boto3_raw_data: "type_defs.DeleteLayerRequestTypeDef" = dataclasses.field()

    LayerId = field("LayerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLayerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLayerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStackRequest:
    boto3_raw_data: "type_defs.DeleteStackRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserProfileRequest:
    boto3_raw_data: "type_defs.DeleteUserProfileRequestTypeDef" = dataclasses.field()

    IamUserArn = field("IamUserArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentCommandOutput:
    boto3_raw_data: "type_defs.DeploymentCommandOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Args = field("Args")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentCommandOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentCommandOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentCommand:
    boto3_raw_data: "type_defs.DeploymentCommandTypeDef" = dataclasses.field()

    Name = field("Name")
    Args = field("Args")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentCommandTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentCommandTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterEcsClusterRequest:
    boto3_raw_data: "type_defs.DeregisterEcsClusterRequestTypeDef" = dataclasses.field()

    EcsClusterArn = field("EcsClusterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterEcsClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterEcsClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterElasticIpRequest:
    boto3_raw_data: "type_defs.DeregisterElasticIpRequestTypeDef" = dataclasses.field()

    ElasticIp = field("ElasticIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterElasticIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterElasticIpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterInstanceRequest:
    boto3_raw_data: "type_defs.DeregisterInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterRdsDbInstanceRequest:
    boto3_raw_data: "type_defs.DeregisterRdsDbInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    RdsDbInstanceArn = field("RdsDbInstanceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterRdsDbInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterRdsDbInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterVolumeRequest:
    boto3_raw_data: "type_defs.DeregisterVolumeRequestTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppsRequest:
    boto3_raw_data: "type_defs.DescribeAppsRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    AppIds = field("AppIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAppsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppsRequestTypeDef"]
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
class DescribeCommandsRequest:
    boto3_raw_data: "type_defs.DescribeCommandsRequestTypeDef" = dataclasses.field()

    DeploymentId = field("DeploymentId")
    InstanceId = field("InstanceId")
    CommandIds = field("CommandIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCommandsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCommandsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeploymentsRequest:
    boto3_raw_data: "type_defs.DescribeDeploymentsRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    AppId = field("AppId")
    DeploymentIds = field("DeploymentIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeploymentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeploymentsRequestTypeDef"]
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
class DescribeEcsClustersRequest:
    boto3_raw_data: "type_defs.DescribeEcsClustersRequestTypeDef" = dataclasses.field()

    EcsClusterArns = field("EcsClusterArns")
    StackId = field("StackId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEcsClustersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEcsClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsCluster:
    boto3_raw_data: "type_defs.EcsClusterTypeDef" = dataclasses.field()

    EcsClusterArn = field("EcsClusterArn")
    EcsClusterName = field("EcsClusterName")
    StackId = field("StackId")
    RegisteredAt = field("RegisteredAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcsClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EcsClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticIpsRequest:
    boto3_raw_data: "type_defs.DescribeElasticIpsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    StackId = field("StackId")
    Ips = field("Ips")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeElasticIpsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeElasticIpsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticIp:
    boto3_raw_data: "type_defs.ElasticIpTypeDef" = dataclasses.field()

    Ip = field("Ip")
    Name = field("Name")
    Domain = field("Domain")
    Region = field("Region")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ElasticIpTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ElasticIpTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticLoadBalancersRequest:
    boto3_raw_data: "type_defs.DescribeElasticLoadBalancersRequestTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    LayerIds = field("LayerIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeElasticLoadBalancersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeElasticLoadBalancersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticLoadBalancer:
    boto3_raw_data: "type_defs.ElasticLoadBalancerTypeDef" = dataclasses.field()

    ElasticLoadBalancerName = field("ElasticLoadBalancerName")
    Region = field("Region")
    DnsName = field("DnsName")
    StackId = field("StackId")
    LayerId = field("LayerId")
    VpcId = field("VpcId")
    AvailabilityZones = field("AvailabilityZones")
    SubnetIds = field("SubnetIds")
    Ec2InstanceIds = field("Ec2InstanceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticLoadBalancerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticLoadBalancerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancesRequest:
    boto3_raw_data: "type_defs.DescribeInstancesRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    LayerId = field("LayerId")
    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInstancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLayersRequest:
    boto3_raw_data: "type_defs.DescribeLayersRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    LayerIds = field("LayerIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLayersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLayersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBasedAutoScalingRequest:
    boto3_raw_data: "type_defs.DescribeLoadBasedAutoScalingRequestTypeDef" = (
        dataclasses.field()
    )

    LayerIds = field("LayerIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBasedAutoScalingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBasedAutoScalingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfUserProfile:
    boto3_raw_data: "type_defs.SelfUserProfileTypeDef" = dataclasses.field()

    IamUserArn = field("IamUserArn")
    Name = field("Name")
    SshUsername = field("SshUsername")
    SshPublicKey = field("SshPublicKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SelfUserProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SelfUserProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePermissionsRequest:
    boto3_raw_data: "type_defs.DescribePermissionsRequestTypeDef" = dataclasses.field()

    IamUserArn = field("IamUserArn")
    StackId = field("StackId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePermissionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Permission:
    boto3_raw_data: "type_defs.PermissionTypeDef" = dataclasses.field()

    StackId = field("StackId")
    IamUserArn = field("IamUserArn")
    AllowSsh = field("AllowSsh")
    AllowSudo = field("AllowSudo")
    Level = field("Level")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PermissionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRaidArraysRequest:
    boto3_raw_data: "type_defs.DescribeRaidArraysRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    StackId = field("StackId")
    RaidArrayIds = field("RaidArrayIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRaidArraysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRaidArraysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RaidArray:
    boto3_raw_data: "type_defs.RaidArrayTypeDef" = dataclasses.field()

    RaidArrayId = field("RaidArrayId")
    InstanceId = field("InstanceId")
    Name = field("Name")
    RaidLevel = field("RaidLevel")
    NumberOfDisks = field("NumberOfDisks")
    Size = field("Size")
    Device = field("Device")
    MountPoint = field("MountPoint")
    AvailabilityZone = field("AvailabilityZone")
    CreatedAt = field("CreatedAt")
    StackId = field("StackId")
    VolumeType = field("VolumeType")
    Iops = field("Iops")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RaidArrayTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RaidArrayTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRdsDbInstancesRequest:
    boto3_raw_data: "type_defs.DescribeRdsDbInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    RdsDbInstanceArns = field("RdsDbInstanceArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRdsDbInstancesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRdsDbInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbInstance:
    boto3_raw_data: "type_defs.RdsDbInstanceTypeDef" = dataclasses.field()

    RdsDbInstanceArn = field("RdsDbInstanceArn")
    DbInstanceIdentifier = field("DbInstanceIdentifier")
    DbUser = field("DbUser")
    DbPassword = field("DbPassword")
    Region = field("Region")
    Address = field("Address")
    Engine = field("Engine")
    StackId = field("StackId")
    MissingOnRds = field("MissingOnRds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RdsDbInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RdsDbInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceErrorsRequest:
    boto3_raw_data: "type_defs.DescribeServiceErrorsRequestTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    InstanceId = field("InstanceId")
    ServiceErrorIds = field("ServiceErrorIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServiceErrorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceErrorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceError:
    boto3_raw_data: "type_defs.ServiceErrorTypeDef" = dataclasses.field()

    ServiceErrorId = field("ServiceErrorId")
    StackId = field("StackId")
    InstanceId = field("InstanceId")
    Type = field("Type")
    Message = field("Message")
    CreatedAt = field("CreatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackProvisioningParametersRequest:
    boto3_raw_data: "type_defs.DescribeStackProvisioningParametersRequestTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStackProvisioningParametersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackProvisioningParametersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackSummaryRequest:
    boto3_raw_data: "type_defs.DescribeStackSummaryRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackSummaryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackSummaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksRequest:
    boto3_raw_data: "type_defs.DescribeStacksRequestTypeDef" = dataclasses.field()

    StackIds = field("StackIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStacksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTimeBasedAutoScalingRequest:
    boto3_raw_data: "type_defs.DescribeTimeBasedAutoScalingRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTimeBasedAutoScalingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTimeBasedAutoScalingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserProfilesRequest:
    boto3_raw_data: "type_defs.DescribeUserProfilesRequestTypeDef" = dataclasses.field()

    IamUserArns = field("IamUserArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserProfile:
    boto3_raw_data: "type_defs.UserProfileTypeDef" = dataclasses.field()

    IamUserArn = field("IamUserArn")
    Name = field("Name")
    SshUsername = field("SshUsername")
    SshPublicKey = field("SshPublicKey")
    AllowSelfManagement = field("AllowSelfManagement")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserProfileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVolumesRequest:
    boto3_raw_data: "type_defs.DescribeVolumesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    StackId = field("StackId")
    RaidArrayId = field("RaidArrayId")
    VolumeIds = field("VolumeIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVolumesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVolumesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Volume:
    boto3_raw_data: "type_defs.VolumeTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")
    Ec2VolumeId = field("Ec2VolumeId")
    Name = field("Name")
    RaidArrayId = field("RaidArrayId")
    InstanceId = field("InstanceId")
    Status = field("Status")
    Size = field("Size")
    Device = field("Device")
    MountPoint = field("MountPoint")
    Region = field("Region")
    AvailabilityZone = field("AvailabilityZone")
    VolumeType = field("VolumeType")
    Iops = field("Iops")
    Encrypted = field("Encrypted")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachElasticLoadBalancerRequest:
    boto3_raw_data: "type_defs.DetachElasticLoadBalancerRequestTypeDef" = (
        dataclasses.field()
    )

    ElasticLoadBalancerName = field("ElasticLoadBalancerName")
    LayerId = field("LayerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetachElasticLoadBalancerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachElasticLoadBalancerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateElasticIpRequest:
    boto3_raw_data: "type_defs.DisassociateElasticIpRequestTypeDef" = (
        dataclasses.field()
    )

    ElasticIp = field("ElasticIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateElasticIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateElasticIpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHostnameSuggestionRequest:
    boto3_raw_data: "type_defs.GetHostnameSuggestionRequestTypeDef" = (
        dataclasses.field()
    )

    LayerId = field("LayerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHostnameSuggestionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHostnameSuggestionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantAccessRequest:
    boto3_raw_data: "type_defs.GrantAccessRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ValidForInMinutes = field("ValidForInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrantAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrantAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemporaryCredential:
    boto3_raw_data: "type_defs.TemporaryCredentialTypeDef" = dataclasses.field()

    Username = field("Username")
    Password = field("Password")
    ValidForInMinutes = field("ValidForInMinutes")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemporaryCredentialTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemporaryCredentialTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceIdentity:
    boto3_raw_data: "type_defs.InstanceIdentityTypeDef" = dataclasses.field()

    Document = field("Document")
    Signature = field("Signature")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceIdentityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportedOs:
    boto3_raw_data: "type_defs.ReportedOsTypeDef" = dataclasses.field()

    Family = field("Family")
    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportedOsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportedOsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstancesCount:
    boto3_raw_data: "type_defs.InstancesCountTypeDef" = dataclasses.field()

    Assigning = field("Assigning")
    Booting = field("Booting")
    ConnectionLost = field("ConnectionLost")
    Deregistering = field("Deregistering")
    Online = field("Online")
    Pending = field("Pending")
    Rebooting = field("Rebooting")
    Registered = field("Registered")
    Registering = field("Registering")
    Requested = field("Requested")
    RunningSetup = field("RunningSetup")
    SetupFailed = field("SetupFailed")
    ShuttingDown = field("ShuttingDown")
    StartFailed = field("StartFailed")
    StopFailed = field("StopFailed")
    Stopped = field("Stopped")
    Stopping = field("Stopping")
    Terminated = field("Terminated")
    Terminating = field("Terminating")
    Unassigning = field("Unassigning")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstancesCountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstancesCountTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipesOutput:
    boto3_raw_data: "type_defs.RecipesOutputTypeDef" = dataclasses.field()

    Setup = field("Setup")
    Configure = field("Configure")
    Deploy = field("Deploy")
    Undeploy = field("Undeploy")
    Shutdown = field("Shutdown")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecipesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShutdownEventConfiguration:
    boto3_raw_data: "type_defs.ShutdownEventConfigurationTypeDef" = dataclasses.field()

    ExecutionTimeout = field("ExecutionTimeout")
    DelayUntilElbConnectionsDrained = field("DelayUntilElbConnectionsDrained")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ShutdownEventConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ShutdownEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsRequest:
    boto3_raw_data: "type_defs.ListTagsRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperatingSystemConfigurationManager:
    boto3_raw_data: "type_defs.OperatingSystemConfigurationManagerTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OperatingSystemConfigurationManagerTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OperatingSystemConfigurationManagerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootInstanceRequest:
    boto3_raw_data: "type_defs.RebootInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recipes:
    boto3_raw_data: "type_defs.RecipesTypeDef" = dataclasses.field()

    Setup = field("Setup")
    Configure = field("Configure")
    Deploy = field("Deploy")
    Undeploy = field("Undeploy")
    Shutdown = field("Shutdown")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecipesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterEcsClusterRequest:
    boto3_raw_data: "type_defs.RegisterEcsClusterRequestTypeDef" = dataclasses.field()

    EcsClusterArn = field("EcsClusterArn")
    StackId = field("StackId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterEcsClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterEcsClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterElasticIpRequest:
    boto3_raw_data: "type_defs.RegisterElasticIpRequestTypeDef" = dataclasses.field()

    ElasticIp = field("ElasticIp")
    StackId = field("StackId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterElasticIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterElasticIpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterRdsDbInstanceRequest:
    boto3_raw_data: "type_defs.RegisterRdsDbInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    RdsDbInstanceArn = field("RdsDbInstanceArn")
    DbUser = field("DbUser")
    DbPassword = field("DbPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterRdsDbInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterRdsDbInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterVolumeRequest:
    boto3_raw_data: "type_defs.RegisterVolumeRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    Ec2VolumeId = field("Ec2VolumeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetPermissionRequest:
    boto3_raw_data: "type_defs.SetPermissionRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    IamUserArn = field("IamUserArn")
    AllowSsh = field("AllowSsh")
    AllowSudo = field("AllowSudo")
    Level = field("Level")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetPermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetPermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInstanceRequest:
    boto3_raw_data: "type_defs.StartInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartStackRequest:
    boto3_raw_data: "type_defs.StartStackRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartStackRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopInstanceRequest:
    boto3_raw_data: "type_defs.StopInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Force = field("Force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopStackRequest:
    boto3_raw_data: "type_defs.StopStackRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopStackRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopStackRequestTypeDef"]
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
class WeeklyAutoScalingScheduleOutput:
    boto3_raw_data: "type_defs.WeeklyAutoScalingScheduleOutputTypeDef" = (
        dataclasses.field()
    )

    Monday = field("Monday")
    Tuesday = field("Tuesday")
    Wednesday = field("Wednesday")
    Thursday = field("Thursday")
    Friday = field("Friday")
    Saturday = field("Saturday")
    Sunday = field("Sunday")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WeeklyAutoScalingScheduleOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WeeklyAutoScalingScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnassignInstanceRequest:
    boto3_raw_data: "type_defs.UnassignInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnassignInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnassignInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnassignVolumeRequest:
    boto3_raw_data: "type_defs.UnassignVolumeRequestTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnassignVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnassignVolumeRequestTypeDef"]
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
class UpdateElasticIpRequest:
    boto3_raw_data: "type_defs.UpdateElasticIpRequestTypeDef" = dataclasses.field()

    ElasticIp = field("ElasticIp")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateElasticIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateElasticIpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstanceRequest:
    boto3_raw_data: "type_defs.UpdateInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    LayerIds = field("LayerIds")
    InstanceType = field("InstanceType")
    AutoScalingType = field("AutoScalingType")
    Hostname = field("Hostname")
    Os = field("Os")
    AmiId = field("AmiId")
    SshKeyName = field("SshKeyName")
    Architecture = field("Architecture")
    InstallUpdatesOnBoot = field("InstallUpdatesOnBoot")
    EbsOptimized = field("EbsOptimized")
    AgentVersion = field("AgentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMyUserProfileRequest:
    boto3_raw_data: "type_defs.UpdateMyUserProfileRequestTypeDef" = dataclasses.field()

    SshPublicKey = field("SshPublicKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMyUserProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMyUserProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRdsDbInstanceRequest:
    boto3_raw_data: "type_defs.UpdateRdsDbInstanceRequestTypeDef" = dataclasses.field()

    RdsDbInstanceArn = field("RdsDbInstanceArn")
    DbUser = field("DbUser")
    DbPassword = field("DbPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRdsDbInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRdsDbInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserProfileRequest:
    boto3_raw_data: "type_defs.UpdateUserProfileRequestTypeDef" = dataclasses.field()

    IamUserArn = field("IamUserArn")
    SshUsername = field("SshUsername")
    SshPublicKey = field("SshPublicKey")
    AllowSelfManagement = field("AllowSelfManagement")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVolumeRequest:
    boto3_raw_data: "type_defs.UpdateVolumeRequestTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")
    Name = field("Name")
    MountPoint = field("MountPoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WeeklyAutoScalingSchedule:
    boto3_raw_data: "type_defs.WeeklyAutoScalingScheduleTypeDef" = dataclasses.field()

    Monday = field("Monday")
    Tuesday = field("Tuesday")
    Wednesday = field("Wednesday")
    Thursday = field("Thursday")
    Friday = field("Friday")
    Saturday = field("Saturday")
    Sunday = field("Sunday")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WeeklyAutoScalingScheduleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WeeklyAutoScalingScheduleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentVersion:
    boto3_raw_data: "type_defs.AgentVersionTypeDef" = dataclasses.field()

    Version = field("Version")

    @cached_property
    def ConfigurationManager(self):  # pragma: no cover
        return StackConfigurationManager.make_one(
            self.boto3_raw_data["ConfigurationManager"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAgentVersionsRequest:
    boto3_raw_data: "type_defs.DescribeAgentVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")

    @cached_property
    def ConfigurationManager(self):  # pragma: no cover
        return StackConfigurationManager.make_one(
            self.boto3_raw_data["ConfigurationManager"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAgentVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAgentVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class App:
    boto3_raw_data: "type_defs.AppTypeDef" = dataclasses.field()

    AppId = field("AppId")
    StackId = field("StackId")
    Shortname = field("Shortname")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["DataSources"])

    Type = field("Type")

    @cached_property
    def AppSource(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["AppSource"])

    Domains = field("Domains")
    EnableSsl = field("EnableSsl")

    @cached_property
    def SslConfiguration(self):  # pragma: no cover
        return SslConfiguration.make_one(self.boto3_raw_data["SslConfiguration"])

    Attributes = field("Attributes")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Environment(self):  # pragma: no cover
        return EnvironmentVariable.make_many(self.boto3_raw_data["Environment"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppRequest:
    boto3_raw_data: "type_defs.CreateAppRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    Name = field("Name")
    Type = field("Type")
    Shortname = field("Shortname")
    Description = field("Description")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["DataSources"])

    @cached_property
    def AppSource(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["AppSource"])

    Domains = field("Domains")
    EnableSsl = field("EnableSsl")

    @cached_property
    def SslConfiguration(self):  # pragma: no cover
        return SslConfiguration.make_one(self.boto3_raw_data["SslConfiguration"])

    Attributes = field("Attributes")

    @cached_property
    def Environment(self):  # pragma: no cover
        return EnvironmentVariable.make_many(self.boto3_raw_data["Environment"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppRequest:
    boto3_raw_data: "type_defs.UpdateAppRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["DataSources"])

    Type = field("Type")

    @cached_property
    def AppSource(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["AppSource"])

    Domains = field("Domains")
    EnableSsl = field("EnableSsl")

    @cached_property
    def SslConfiguration(self):  # pragma: no cover
        return SslConfiguration.make_one(self.boto3_raw_data["SslConfiguration"])

    Attributes = field("Attributes")

    @cached_property
    def Environment(self):  # pragma: no cover
        return EnvironmentVariable.make_many(self.boto3_raw_data["Environment"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBasedAutoScalingConfiguration:
    boto3_raw_data: "type_defs.LoadBasedAutoScalingConfigurationTypeDef" = (
        dataclasses.field()
    )

    LayerId = field("LayerId")
    Enable = field("Enable")

    @cached_property
    def UpScaling(self):  # pragma: no cover
        return AutoScalingThresholdsOutput.make_one(self.boto3_raw_data["UpScaling"])

    @cached_property
    def DownScaling(self):  # pragma: no cover
        return AutoScalingThresholdsOutput.make_one(self.boto3_raw_data["DownScaling"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoadBasedAutoScalingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBasedAutoScalingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockDeviceMapping:
    boto3_raw_data: "type_defs.BlockDeviceMappingTypeDef" = dataclasses.field()

    DeviceName = field("DeviceName")
    NoDevice = field("NoDevice")
    VirtualName = field("VirtualName")

    @cached_property
    def Ebs(self):  # pragma: no cover
        return EbsBlockDevice.make_one(self.boto3_raw_data["Ebs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BlockDeviceMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockDeviceMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloneStackRequest:
    boto3_raw_data: "type_defs.CloneStackRequestTypeDef" = dataclasses.field()

    SourceStackId = field("SourceStackId")
    ServiceRoleArn = field("ServiceRoleArn")
    Name = field("Name")
    Region = field("Region")
    VpcId = field("VpcId")
    Attributes = field("Attributes")
    DefaultInstanceProfileArn = field("DefaultInstanceProfileArn")
    DefaultOs = field("DefaultOs")
    HostnameTheme = field("HostnameTheme")
    DefaultAvailabilityZone = field("DefaultAvailabilityZone")
    DefaultSubnetId = field("DefaultSubnetId")
    CustomJson = field("CustomJson")

    @cached_property
    def ConfigurationManager(self):  # pragma: no cover
        return StackConfigurationManager.make_one(
            self.boto3_raw_data["ConfigurationManager"]
        )

    @cached_property
    def ChefConfiguration(self):  # pragma: no cover
        return ChefConfiguration.make_one(self.boto3_raw_data["ChefConfiguration"])

    UseCustomCookbooks = field("UseCustomCookbooks")
    UseOpsworksSecurityGroups = field("UseOpsworksSecurityGroups")

    @cached_property
    def CustomCookbooksSource(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["CustomCookbooksSource"])

    DefaultSshKeyName = field("DefaultSshKeyName")
    ClonePermissions = field("ClonePermissions")
    CloneAppIds = field("CloneAppIds")
    DefaultRootDeviceType = field("DefaultRootDeviceType")
    AgentVersion = field("AgentVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloneStackRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloneStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackRequestServiceResourceCreateStack:
    boto3_raw_data: "type_defs.CreateStackRequestServiceResourceCreateStackTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Region = field("Region")
    ServiceRoleArn = field("ServiceRoleArn")
    DefaultInstanceProfileArn = field("DefaultInstanceProfileArn")
    VpcId = field("VpcId")
    Attributes = field("Attributes")
    DefaultOs = field("DefaultOs")
    HostnameTheme = field("HostnameTheme")
    DefaultAvailabilityZone = field("DefaultAvailabilityZone")
    DefaultSubnetId = field("DefaultSubnetId")
    CustomJson = field("CustomJson")

    @cached_property
    def ConfigurationManager(self):  # pragma: no cover
        return StackConfigurationManager.make_one(
            self.boto3_raw_data["ConfigurationManager"]
        )

    @cached_property
    def ChefConfiguration(self):  # pragma: no cover
        return ChefConfiguration.make_one(self.boto3_raw_data["ChefConfiguration"])

    UseCustomCookbooks = field("UseCustomCookbooks")
    UseOpsworksSecurityGroups = field("UseOpsworksSecurityGroups")

    @cached_property
    def CustomCookbooksSource(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["CustomCookbooksSource"])

    DefaultSshKeyName = field("DefaultSshKeyName")
    DefaultRootDeviceType = field("DefaultRootDeviceType")
    AgentVersion = field("AgentVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStackRequestServiceResourceCreateStackTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackRequestServiceResourceCreateStackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackRequest:
    boto3_raw_data: "type_defs.CreateStackRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Region = field("Region")
    ServiceRoleArn = field("ServiceRoleArn")
    DefaultInstanceProfileArn = field("DefaultInstanceProfileArn")
    VpcId = field("VpcId")
    Attributes = field("Attributes")
    DefaultOs = field("DefaultOs")
    HostnameTheme = field("HostnameTheme")
    DefaultAvailabilityZone = field("DefaultAvailabilityZone")
    DefaultSubnetId = field("DefaultSubnetId")
    CustomJson = field("CustomJson")

    @cached_property
    def ConfigurationManager(self):  # pragma: no cover
        return StackConfigurationManager.make_one(
            self.boto3_raw_data["ConfigurationManager"]
        )

    @cached_property
    def ChefConfiguration(self):  # pragma: no cover
        return ChefConfiguration.make_one(self.boto3_raw_data["ChefConfiguration"])

    UseCustomCookbooks = field("UseCustomCookbooks")
    UseOpsworksSecurityGroups = field("UseOpsworksSecurityGroups")

    @cached_property
    def CustomCookbooksSource(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["CustomCookbooksSource"])

    DefaultSshKeyName = field("DefaultSshKeyName")
    DefaultRootDeviceType = field("DefaultRootDeviceType")
    AgentVersion = field("AgentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stack:
    boto3_raw_data: "type_defs.StackTypeDef" = dataclasses.field()

    StackId = field("StackId")
    Name = field("Name")
    Arn = field("Arn")
    Region = field("Region")
    VpcId = field("VpcId")
    Attributes = field("Attributes")
    ServiceRoleArn = field("ServiceRoleArn")
    DefaultInstanceProfileArn = field("DefaultInstanceProfileArn")
    DefaultOs = field("DefaultOs")
    HostnameTheme = field("HostnameTheme")
    DefaultAvailabilityZone = field("DefaultAvailabilityZone")
    DefaultSubnetId = field("DefaultSubnetId")
    CustomJson = field("CustomJson")

    @cached_property
    def ConfigurationManager(self):  # pragma: no cover
        return StackConfigurationManager.make_one(
            self.boto3_raw_data["ConfigurationManager"]
        )

    @cached_property
    def ChefConfiguration(self):  # pragma: no cover
        return ChefConfiguration.make_one(self.boto3_raw_data["ChefConfiguration"])

    UseCustomCookbooks = field("UseCustomCookbooks")
    UseOpsworksSecurityGroups = field("UseOpsworksSecurityGroups")

    @cached_property
    def CustomCookbooksSource(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["CustomCookbooksSource"])

    DefaultSshKeyName = field("DefaultSshKeyName")
    CreatedAt = field("CreatedAt")
    DefaultRootDeviceType = field("DefaultRootDeviceType")
    AgentVersion = field("AgentVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStackRequest:
    boto3_raw_data: "type_defs.UpdateStackRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    Name = field("Name")
    Attributes = field("Attributes")
    ServiceRoleArn = field("ServiceRoleArn")
    DefaultInstanceProfileArn = field("DefaultInstanceProfileArn")
    DefaultOs = field("DefaultOs")
    HostnameTheme = field("HostnameTheme")
    DefaultAvailabilityZone = field("DefaultAvailabilityZone")
    DefaultSubnetId = field("DefaultSubnetId")
    CustomJson = field("CustomJson")

    @cached_property
    def ConfigurationManager(self):  # pragma: no cover
        return StackConfigurationManager.make_one(
            self.boto3_raw_data["ConfigurationManager"]
        )

    @cached_property
    def ChefConfiguration(self):  # pragma: no cover
        return ChefConfiguration.make_one(self.boto3_raw_data["ChefConfiguration"])

    UseCustomCookbooks = field("UseCustomCookbooks")

    @cached_property
    def CustomCookbooksSource(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["CustomCookbooksSource"])

    DefaultSshKeyName = field("DefaultSshKeyName")
    DefaultRootDeviceType = field("DefaultRootDeviceType")
    UseOpsworksSecurityGroups = field("UseOpsworksSecurityGroups")
    AgentVersion = field("AgentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloneStackResult:
    boto3_raw_data: "type_defs.CloneStackResultTypeDef" = dataclasses.field()

    StackId = field("StackId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloneStackResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloneStackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppResult:
    boto3_raw_data: "type_defs.CreateAppResultTypeDef" = dataclasses.field()

    AppId = field("AppId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAppResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateAppResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentResult:
    boto3_raw_data: "type_defs.CreateDeploymentResultTypeDef" = dataclasses.field()

    DeploymentId = field("DeploymentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceResult:
    boto3_raw_data: "type_defs.CreateInstanceResultTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLayerResult:
    boto3_raw_data: "type_defs.CreateLayerResultTypeDef" = dataclasses.field()

    LayerId = field("LayerId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateLayerResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLayerResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackResult:
    boto3_raw_data: "type_defs.CreateStackResultTypeDef" = dataclasses.field()

    StackId = field("StackId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateStackResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserProfileResult:
    boto3_raw_data: "type_defs.CreateUserProfileResultTypeDef" = dataclasses.field()

    IamUserArn = field("IamUserArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserProfileResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserProfileResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackProvisioningParametersResult:
    boto3_raw_data: "type_defs.DescribeStackProvisioningParametersResultTypeDef" = (
        dataclasses.field()
    )

    AgentInstallerUrl = field("AgentInstallerUrl")
    Parameters = field("Parameters")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStackProvisioningParametersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackProvisioningParametersResultTypeDef"]
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
class GetHostnameSuggestionResult:
    boto3_raw_data: "type_defs.GetHostnameSuggestionResultTypeDef" = dataclasses.field()

    LayerId = field("LayerId")
    Hostname = field("Hostname")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHostnameSuggestionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHostnameSuggestionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsResult:
    boto3_raw_data: "type_defs.ListTagsResultTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTagsResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterEcsClusterResult:
    boto3_raw_data: "type_defs.RegisterEcsClusterResultTypeDef" = dataclasses.field()

    EcsClusterArn = field("EcsClusterArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterEcsClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterEcsClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterElasticIpResult:
    boto3_raw_data: "type_defs.RegisterElasticIpResultTypeDef" = dataclasses.field()

    ElasticIp = field("ElasticIp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterElasticIpResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterElasticIpResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterInstanceResult:
    boto3_raw_data: "type_defs.RegisterInstanceResultTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterVolumeResult:
    boto3_raw_data: "type_defs.RegisterVolumeResultTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterVolumeResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterVolumeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsConfigurationOutput:
    boto3_raw_data: "type_defs.CloudWatchLogsConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")

    @cached_property
    def LogStreams(self):  # pragma: no cover
        return CloudWatchLogsLogStream.make_many(self.boto3_raw_data["LogStreams"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudWatchLogsConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsConfiguration:
    boto3_raw_data: "type_defs.CloudWatchLogsConfigurationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @cached_property
    def LogStreams(self):  # pragma: no cover
        return CloudWatchLogsLogStream.make_many(self.boto3_raw_data["LogStreams"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCommandsResult:
    boto3_raw_data: "type_defs.DescribeCommandsResultTypeDef" = dataclasses.field()

    @cached_property
    def Commands(self):  # pragma: no cover
        return Command.make_many(self.boto3_raw_data["Commands"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCommandsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCommandsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Deployment:
    boto3_raw_data: "type_defs.DeploymentTypeDef" = dataclasses.field()

    DeploymentId = field("DeploymentId")
    StackId = field("StackId")
    AppId = field("AppId")
    CreatedAt = field("CreatedAt")
    CompletedAt = field("CompletedAt")
    Duration = field("Duration")
    IamUserArn = field("IamUserArn")
    Comment = field("Comment")

    @cached_property
    def Command(self):  # pragma: no cover
        return DeploymentCommandOutput.make_one(self.boto3_raw_data["Command"])

    Status = field("Status")
    CustomJson = field("CustomJson")
    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppsRequestWait:
    boto3_raw_data: "type_defs.DescribeAppsRequestWaitTypeDef" = dataclasses.field()

    StackId = field("StackId")
    AppIds = field("AppIds")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAppsRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppsRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeploymentsRequestWait:
    boto3_raw_data: "type_defs.DescribeDeploymentsRequestWaitTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    AppId = field("AppId")
    DeploymentIds = field("DeploymentIds")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDeploymentsRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeploymentsRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancesRequestWaitExtraExtraExtra:
    boto3_raw_data: "type_defs.DescribeInstancesRequestWaitExtraExtraExtraTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    LayerId = field("LayerId")
    InstanceIds = field("InstanceIds")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancesRequestWaitExtraExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesRequestWaitExtraExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancesRequestWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeInstancesRequestWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    LayerId = field("LayerId")
    InstanceIds = field("InstanceIds")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancesRequestWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesRequestWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancesRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeInstancesRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    LayerId = field("LayerId")
    InstanceIds = field("InstanceIds")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancesRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancesRequestWait:
    boto3_raw_data: "type_defs.DescribeInstancesRequestWaitTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    LayerId = field("LayerId")
    InstanceIds = field("InstanceIds")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInstancesRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEcsClustersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeEcsClustersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    EcsClusterArns = field("EcsClusterArns")
    StackId = field("StackId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEcsClustersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEcsClustersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEcsClustersResult:
    boto3_raw_data: "type_defs.DescribeEcsClustersResultTypeDef" = dataclasses.field()

    @cached_property
    def EcsClusters(self):  # pragma: no cover
        return EcsCluster.make_many(self.boto3_raw_data["EcsClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEcsClustersResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEcsClustersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticIpsResult:
    boto3_raw_data: "type_defs.DescribeElasticIpsResultTypeDef" = dataclasses.field()

    @cached_property
    def ElasticIps(self):  # pragma: no cover
        return ElasticIp.make_many(self.boto3_raw_data["ElasticIps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeElasticIpsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeElasticIpsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticLoadBalancersResult:
    boto3_raw_data: "type_defs.DescribeElasticLoadBalancersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ElasticLoadBalancers(self):  # pragma: no cover
        return ElasticLoadBalancer.make_many(
            self.boto3_raw_data["ElasticLoadBalancers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeElasticLoadBalancersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeElasticLoadBalancersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMyUserProfileResult:
    boto3_raw_data: "type_defs.DescribeMyUserProfileResultTypeDef" = dataclasses.field()

    @cached_property
    def UserProfile(self):  # pragma: no cover
        return SelfUserProfile.make_one(self.boto3_raw_data["UserProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMyUserProfileResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMyUserProfileResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePermissionsResult:
    boto3_raw_data: "type_defs.DescribePermissionsResultTypeDef" = dataclasses.field()

    @cached_property
    def Permissions(self):  # pragma: no cover
        return Permission.make_many(self.boto3_raw_data["Permissions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePermissionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePermissionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRaidArraysResult:
    boto3_raw_data: "type_defs.DescribeRaidArraysResultTypeDef" = dataclasses.field()

    @cached_property
    def RaidArrays(self):  # pragma: no cover
        return RaidArray.make_many(self.boto3_raw_data["RaidArrays"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRaidArraysResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRaidArraysResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRdsDbInstancesResult:
    boto3_raw_data: "type_defs.DescribeRdsDbInstancesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RdsDbInstances(self):  # pragma: no cover
        return RdsDbInstance.make_many(self.boto3_raw_data["RdsDbInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRdsDbInstancesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRdsDbInstancesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceErrorsResult:
    boto3_raw_data: "type_defs.DescribeServiceErrorsResultTypeDef" = dataclasses.field()

    @cached_property
    def ServiceErrors(self):  # pragma: no cover
        return ServiceError.make_many(self.boto3_raw_data["ServiceErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServiceErrorsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceErrorsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserProfilesResult:
    boto3_raw_data: "type_defs.DescribeUserProfilesResultTypeDef" = dataclasses.field()

    @cached_property
    def UserProfiles(self):  # pragma: no cover
        return UserProfile.make_many(self.boto3_raw_data["UserProfiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserProfilesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserProfilesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVolumesResult:
    boto3_raw_data: "type_defs.DescribeVolumesResultTypeDef" = dataclasses.field()

    @cached_property
    def Volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["Volumes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVolumesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVolumesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantAccessResult:
    boto3_raw_data: "type_defs.GrantAccessResultTypeDef" = dataclasses.field()

    @cached_property
    def TemporaryCredential(self):  # pragma: no cover
        return TemporaryCredential.make_one(self.boto3_raw_data["TemporaryCredential"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantAccessResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrantAccessResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterInstanceRequest:
    boto3_raw_data: "type_defs.RegisterInstanceRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    Hostname = field("Hostname")
    PublicIp = field("PublicIp")
    PrivateIp = field("PrivateIp")
    RsaPublicKey = field("RsaPublicKey")
    RsaPublicKeyFingerprint = field("RsaPublicKeyFingerprint")

    @cached_property
    def InstanceIdentity(self):  # pragma: no cover
        return InstanceIdentity.make_one(self.boto3_raw_data["InstanceIdentity"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSummary:
    boto3_raw_data: "type_defs.StackSummaryTypeDef" = dataclasses.field()

    StackId = field("StackId")
    Name = field("Name")
    Arn = field("Arn")
    LayersCount = field("LayersCount")
    AppsCount = field("AppsCount")

    @cached_property
    def InstancesCount(self):  # pragma: no cover
        return InstancesCount.make_one(self.boto3_raw_data["InstancesCount"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleEventConfiguration:
    boto3_raw_data: "type_defs.LifecycleEventConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def Shutdown(self):  # pragma: no cover
        return ShutdownEventConfiguration.make_one(self.boto3_raw_data["Shutdown"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleEventConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperatingSystem:
    boto3_raw_data: "type_defs.OperatingSystemTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Type = field("Type")

    @cached_property
    def ConfigurationManagers(self):  # pragma: no cover
        return OperatingSystemConfigurationManager.make_many(
            self.boto3_raw_data["ConfigurationManagers"]
        )

    ReportedName = field("ReportedName")
    ReportedVersion = field("ReportedVersion")
    Supported = field("Supported")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperatingSystemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OperatingSystemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeBasedAutoScalingConfiguration:
    boto3_raw_data: "type_defs.TimeBasedAutoScalingConfigurationTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def AutoScalingSchedule(self):  # pragma: no cover
        return WeeklyAutoScalingScheduleOutput.make_one(
            self.boto3_raw_data["AutoScalingSchedule"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TimeBasedAutoScalingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeBasedAutoScalingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAgentVersionsResult:
    boto3_raw_data: "type_defs.DescribeAgentVersionsResultTypeDef" = dataclasses.field()

    @cached_property
    def AgentVersions(self):  # pragma: no cover
        return AgentVersion.make_many(self.boto3_raw_data["AgentVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAgentVersionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAgentVersionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppsResult:
    boto3_raw_data: "type_defs.DescribeAppsResultTypeDef" = dataclasses.field()

    @cached_property
    def Apps(self):  # pragma: no cover
        return App.make_many(self.boto3_raw_data["Apps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAppsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBasedAutoScalingResult:
    boto3_raw_data: "type_defs.DescribeLoadBasedAutoScalingResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoadBasedAutoScalingConfigurations(self):  # pragma: no cover
        return LoadBasedAutoScalingConfiguration.make_many(
            self.boto3_raw_data["LoadBasedAutoScalingConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBasedAutoScalingResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBasedAutoScalingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetLoadBasedAutoScalingRequest:
    boto3_raw_data: "type_defs.SetLoadBasedAutoScalingRequestTypeDef" = (
        dataclasses.field()
    )

    LayerId = field("LayerId")
    Enable = field("Enable")
    UpScaling = field("UpScaling")
    DownScaling = field("DownScaling")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetLoadBasedAutoScalingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetLoadBasedAutoScalingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceRequest:
    boto3_raw_data: "type_defs.CreateInstanceRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    LayerIds = field("LayerIds")
    InstanceType = field("InstanceType")
    AutoScalingType = field("AutoScalingType")
    Hostname = field("Hostname")
    Os = field("Os")
    AmiId = field("AmiId")
    SshKeyName = field("SshKeyName")
    AvailabilityZone = field("AvailabilityZone")
    VirtualizationType = field("VirtualizationType")
    SubnetId = field("SubnetId")
    Architecture = field("Architecture")
    RootDeviceType = field("RootDeviceType")

    @cached_property
    def BlockDeviceMappings(self):  # pragma: no cover
        return BlockDeviceMapping.make_many(self.boto3_raw_data["BlockDeviceMappings"])

    InstallUpdatesOnBoot = field("InstallUpdatesOnBoot")
    EbsOptimized = field("EbsOptimized")
    AgentVersion = field("AgentVersion")
    Tenancy = field("Tenancy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceRequestTypeDef"]
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

    AgentVersion = field("AgentVersion")
    AmiId = field("AmiId")
    Architecture = field("Architecture")
    Arn = field("Arn")
    AutoScalingType = field("AutoScalingType")
    AvailabilityZone = field("AvailabilityZone")

    @cached_property
    def BlockDeviceMappings(self):  # pragma: no cover
        return BlockDeviceMapping.make_many(self.boto3_raw_data["BlockDeviceMappings"])

    CreatedAt = field("CreatedAt")
    EbsOptimized = field("EbsOptimized")
    Ec2InstanceId = field("Ec2InstanceId")
    EcsClusterArn = field("EcsClusterArn")
    EcsContainerInstanceArn = field("EcsContainerInstanceArn")
    ElasticIp = field("ElasticIp")
    Hostname = field("Hostname")
    InfrastructureClass = field("InfrastructureClass")
    InstallUpdatesOnBoot = field("InstallUpdatesOnBoot")
    InstanceId = field("InstanceId")
    InstanceProfileArn = field("InstanceProfileArn")
    InstanceType = field("InstanceType")
    LastServiceErrorId = field("LastServiceErrorId")
    LayerIds = field("LayerIds")
    Os = field("Os")
    Platform = field("Platform")
    PrivateDns = field("PrivateDns")
    PrivateIp = field("PrivateIp")
    PublicDns = field("PublicDns")
    PublicIp = field("PublicIp")
    RegisteredBy = field("RegisteredBy")
    ReportedAgentVersion = field("ReportedAgentVersion")

    @cached_property
    def ReportedOs(self):  # pragma: no cover
        return ReportedOs.make_one(self.boto3_raw_data["ReportedOs"])

    RootDeviceType = field("RootDeviceType")
    RootDeviceVolumeId = field("RootDeviceVolumeId")
    SecurityGroupIds = field("SecurityGroupIds")
    SshHostDsaKeyFingerprint = field("SshHostDsaKeyFingerprint")
    SshHostRsaKeyFingerprint = field("SshHostRsaKeyFingerprint")
    SshKeyName = field("SshKeyName")
    StackId = field("StackId")
    Status = field("Status")
    SubnetId = field("SubnetId")
    Tenancy = field("Tenancy")
    VirtualizationType = field("VirtualizationType")

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
class DescribeStacksResult:
    boto3_raw_data: "type_defs.DescribeStacksResultTypeDef" = dataclasses.field()

    @cached_property
    def Stacks(self):  # pragma: no cover
        return Stack.make_many(self.boto3_raw_data["Stacks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStacksResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeploymentsResult:
    boto3_raw_data: "type_defs.DescribeDeploymentsResultTypeDef" = dataclasses.field()

    @cached_property
    def Deployments(self):  # pragma: no cover
        return Deployment.make_many(self.boto3_raw_data["Deployments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeploymentsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeploymentsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentRequest:
    boto3_raw_data: "type_defs.CreateDeploymentRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    Command = field("Command")
    AppId = field("AppId")
    InstanceIds = field("InstanceIds")
    LayerIds = field("LayerIds")
    Comment = field("Comment")
    CustomJson = field("CustomJson")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackSummaryResult:
    boto3_raw_data: "type_defs.DescribeStackSummaryResultTypeDef" = dataclasses.field()

    @cached_property
    def StackSummary(self):  # pragma: no cover
        return StackSummary.make_one(self.boto3_raw_data["StackSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackSummaryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackSummaryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Layer:
    boto3_raw_data: "type_defs.LayerTypeDef" = dataclasses.field()

    Arn = field("Arn")
    StackId = field("StackId")
    LayerId = field("LayerId")
    Type = field("Type")
    Name = field("Name")
    Shortname = field("Shortname")
    Attributes = field("Attributes")

    @cached_property
    def CloudWatchLogsConfiguration(self):  # pragma: no cover
        return CloudWatchLogsConfigurationOutput.make_one(
            self.boto3_raw_data["CloudWatchLogsConfiguration"]
        )

    CustomInstanceProfileArn = field("CustomInstanceProfileArn")
    CustomJson = field("CustomJson")
    CustomSecurityGroupIds = field("CustomSecurityGroupIds")
    DefaultSecurityGroupNames = field("DefaultSecurityGroupNames")
    Packages = field("Packages")

    @cached_property
    def VolumeConfigurations(self):  # pragma: no cover
        return VolumeConfiguration.make_many(
            self.boto3_raw_data["VolumeConfigurations"]
        )

    EnableAutoHealing = field("EnableAutoHealing")
    AutoAssignElasticIps = field("AutoAssignElasticIps")
    AutoAssignPublicIps = field("AutoAssignPublicIps")

    @cached_property
    def DefaultRecipes(self):  # pragma: no cover
        return RecipesOutput.make_one(self.boto3_raw_data["DefaultRecipes"])

    @cached_property
    def CustomRecipes(self):  # pragma: no cover
        return RecipesOutput.make_one(self.boto3_raw_data["CustomRecipes"])

    CreatedAt = field("CreatedAt")
    InstallUpdatesOnBoot = field("InstallUpdatesOnBoot")
    UseEbsOptimizedInstances = field("UseEbsOptimizedInstances")

    @cached_property
    def LifecycleEventConfiguration(self):  # pragma: no cover
        return LifecycleEventConfiguration.make_one(
            self.boto3_raw_data["LifecycleEventConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LayerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LayerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOperatingSystemsResponse:
    boto3_raw_data: "type_defs.DescribeOperatingSystemsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OperatingSystems(self):  # pragma: no cover
        return OperatingSystem.make_many(self.boto3_raw_data["OperatingSystems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeOperatingSystemsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOperatingSystemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTimeBasedAutoScalingResult:
    boto3_raw_data: "type_defs.DescribeTimeBasedAutoScalingResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimeBasedAutoScalingConfigurations(self):  # pragma: no cover
        return TimeBasedAutoScalingConfiguration.make_many(
            self.boto3_raw_data["TimeBasedAutoScalingConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTimeBasedAutoScalingResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTimeBasedAutoScalingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTimeBasedAutoScalingRequest:
    boto3_raw_data: "type_defs.SetTimeBasedAutoScalingRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    AutoScalingSchedule = field("AutoScalingSchedule")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetTimeBasedAutoScalingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTimeBasedAutoScalingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancesResult:
    boto3_raw_data: "type_defs.DescribeInstancesResultTypeDef" = dataclasses.field()

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInstancesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLayerRequestStackCreateLayer:
    boto3_raw_data: "type_defs.CreateLayerRequestStackCreateLayerTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Name = field("Name")
    Shortname = field("Shortname")
    Attributes = field("Attributes")
    CloudWatchLogsConfiguration = field("CloudWatchLogsConfiguration")
    CustomInstanceProfileArn = field("CustomInstanceProfileArn")
    CustomJson = field("CustomJson")
    CustomSecurityGroupIds = field("CustomSecurityGroupIds")
    Packages = field("Packages")

    @cached_property
    def VolumeConfigurations(self):  # pragma: no cover
        return VolumeConfiguration.make_many(
            self.boto3_raw_data["VolumeConfigurations"]
        )

    EnableAutoHealing = field("EnableAutoHealing")
    AutoAssignElasticIps = field("AutoAssignElasticIps")
    AutoAssignPublicIps = field("AutoAssignPublicIps")
    CustomRecipes = field("CustomRecipes")
    InstallUpdatesOnBoot = field("InstallUpdatesOnBoot")
    UseEbsOptimizedInstances = field("UseEbsOptimizedInstances")

    @cached_property
    def LifecycleEventConfiguration(self):  # pragma: no cover
        return LifecycleEventConfiguration.make_one(
            self.boto3_raw_data["LifecycleEventConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLayerRequestStackCreateLayerTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLayerRequestStackCreateLayerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLayerRequest:
    boto3_raw_data: "type_defs.CreateLayerRequestTypeDef" = dataclasses.field()

    StackId = field("StackId")
    Type = field("Type")
    Name = field("Name")
    Shortname = field("Shortname")
    Attributes = field("Attributes")
    CloudWatchLogsConfiguration = field("CloudWatchLogsConfiguration")
    CustomInstanceProfileArn = field("CustomInstanceProfileArn")
    CustomJson = field("CustomJson")
    CustomSecurityGroupIds = field("CustomSecurityGroupIds")
    Packages = field("Packages")

    @cached_property
    def VolumeConfigurations(self):  # pragma: no cover
        return VolumeConfiguration.make_many(
            self.boto3_raw_data["VolumeConfigurations"]
        )

    EnableAutoHealing = field("EnableAutoHealing")
    AutoAssignElasticIps = field("AutoAssignElasticIps")
    AutoAssignPublicIps = field("AutoAssignPublicIps")
    CustomRecipes = field("CustomRecipes")
    InstallUpdatesOnBoot = field("InstallUpdatesOnBoot")
    UseEbsOptimizedInstances = field("UseEbsOptimizedInstances")

    @cached_property
    def LifecycleEventConfiguration(self):  # pragma: no cover
        return LifecycleEventConfiguration.make_one(
            self.boto3_raw_data["LifecycleEventConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLayerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLayerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLayerRequest:
    boto3_raw_data: "type_defs.UpdateLayerRequestTypeDef" = dataclasses.field()

    LayerId = field("LayerId")
    Name = field("Name")
    Shortname = field("Shortname")
    Attributes = field("Attributes")
    CloudWatchLogsConfiguration = field("CloudWatchLogsConfiguration")
    CustomInstanceProfileArn = field("CustomInstanceProfileArn")
    CustomJson = field("CustomJson")
    CustomSecurityGroupIds = field("CustomSecurityGroupIds")
    Packages = field("Packages")

    @cached_property
    def VolumeConfigurations(self):  # pragma: no cover
        return VolumeConfiguration.make_many(
            self.boto3_raw_data["VolumeConfigurations"]
        )

    EnableAutoHealing = field("EnableAutoHealing")
    AutoAssignElasticIps = field("AutoAssignElasticIps")
    AutoAssignPublicIps = field("AutoAssignPublicIps")
    CustomRecipes = field("CustomRecipes")
    InstallUpdatesOnBoot = field("InstallUpdatesOnBoot")
    UseEbsOptimizedInstances = field("UseEbsOptimizedInstances")

    @cached_property
    def LifecycleEventConfiguration(self):  # pragma: no cover
        return LifecycleEventConfiguration.make_one(
            self.boto3_raw_data["LifecycleEventConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLayerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLayerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLayersResult:
    boto3_raw_data: "type_defs.DescribeLayersResultTypeDef" = dataclasses.field()

    @cached_property
    def Layers(self):  # pragma: no cover
        return Layer.make_many(self.boto3_raw_data["Layers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLayersResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLayersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
