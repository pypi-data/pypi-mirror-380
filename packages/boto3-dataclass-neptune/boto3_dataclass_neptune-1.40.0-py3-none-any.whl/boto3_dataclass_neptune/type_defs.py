# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_neptune import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddRoleToDBClusterMessage:
    boto3_raw_data: "type_defs.AddRoleToDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    RoleArn = field("RoleArn")
    FeatureName = field("FeatureName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddRoleToDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddRoleToDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddSourceIdentifierToSubscriptionMessage:
    boto3_raw_data: "type_defs.AddSourceIdentifierToSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")
    SourceIdentifier = field("SourceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddSourceIdentifierToSubscriptionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddSourceIdentifierToSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSubscription:
    boto3_raw_data: "type_defs.EventSubscriptionTypeDef" = dataclasses.field()

    CustomerAwsId = field("CustomerAwsId")
    CustSubscriptionId = field("CustSubscriptionId")
    SnsTopicArn = field("SnsTopicArn")
    Status = field("Status")
    SubscriptionCreationTime = field("SubscriptionCreationTime")
    SourceType = field("SourceType")
    SourceIdsList = field("SourceIdsList")
    EventCategoriesList = field("EventCategoriesList")
    Enabled = field("Enabled")
    EventSubscriptionArn = field("EventSubscriptionArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventSubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSubscriptionTypeDef"]
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
class ApplyPendingMaintenanceActionMessage:
    boto3_raw_data: "type_defs.ApplyPendingMaintenanceActionMessageTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")
    ApplyAction = field("ApplyAction")
    OptInType = field("OptInType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplyPendingMaintenanceActionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyPendingMaintenanceActionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityZone:
    boto3_raw_data: "type_defs.AvailabilityZoneTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CharacterSet:
    boto3_raw_data: "type_defs.CharacterSetTypeDef" = dataclasses.field()

    CharacterSetName = field("CharacterSetName")
    CharacterSetDescription = field("CharacterSetDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CharacterSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CharacterSetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchLogsExportConfiguration:
    boto3_raw_data: "type_defs.CloudwatchLogsExportConfigurationTypeDef" = (
        dataclasses.field()
    )

    EnableLogTypes = field("EnableLogTypes")
    DisableLogTypes = field("DisableLogTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudwatchLogsExportConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchLogsExportConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingCloudwatchLogsExports:
    boto3_raw_data: "type_defs.PendingCloudwatchLogsExportsTypeDef" = (
        dataclasses.field()
    )

    LogTypesToEnable = field("LogTypesToEnable")
    LogTypesToDisable = field("LogTypesToDisable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingCloudwatchLogsExportsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingCloudwatchLogsExportsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterParameterGroup:
    boto3_raw_data: "type_defs.DBClusterParameterGroupTypeDef" = dataclasses.field()

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    Description = field("Description")
    DBClusterParameterGroupArn = field("DBClusterParameterGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterParameterGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterParameterGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterSnapshot:
    boto3_raw_data: "type_defs.DBClusterSnapshotTypeDef" = dataclasses.field()

    AvailabilityZones = field("AvailabilityZones")
    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    SnapshotCreateTime = field("SnapshotCreateTime")
    Engine = field("Engine")
    AllocatedStorage = field("AllocatedStorage")
    Status = field("Status")
    Port = field("Port")
    VpcId = field("VpcId")
    ClusterCreateTime = field("ClusterCreateTime")
    MasterUsername = field("MasterUsername")
    EngineVersion = field("EngineVersion")
    LicenseModel = field("LicenseModel")
    SnapshotType = field("SnapshotType")
    PercentProgress = field("PercentProgress")
    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    DBClusterSnapshotArn = field("DBClusterSnapshotArn")
    SourceDBClusterSnapshotArn = field("SourceDBClusterSnapshotArn")
    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")
    StorageType = field("StorageType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterSnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterSnapshotTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBParameterGroup:
    boto3_raw_data: "type_defs.DBParameterGroupTypeDef" = dataclasses.field()

    DBParameterGroupName = field("DBParameterGroupName")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    Description = field("Description")
    DBParameterGroupArn = field("DBParameterGroupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBParameterGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBParameterGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessV2ScalingConfiguration:
    boto3_raw_data: "type_defs.ServerlessV2ScalingConfigurationTypeDef" = (
        dataclasses.field()
    )

    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServerlessV2ScalingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerlessV2ScalingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalClusterMessage:
    boto3_raw_data: "type_defs.CreateGlobalClusterMessageTypeDef" = dataclasses.field()

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    SourceDBClusterIdentifier = field("SourceDBClusterIdentifier")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DeletionProtection = field("DeletionProtection")
    StorageEncrypted = field("StorageEncrypted")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlobalClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterEndpoint:
    boto3_raw_data: "type_defs.DBClusterEndpointTypeDef" = dataclasses.field()

    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointResourceIdentifier = field("DBClusterEndpointResourceIdentifier")
    Endpoint = field("Endpoint")
    Status = field("Status")
    EndpointType = field("EndpointType")
    CustomEndpointType = field("CustomEndpointType")
    StaticMembers = field("StaticMembers")
    ExcludedMembers = field("ExcludedMembers")
    DBClusterEndpointArn = field("DBClusterEndpointArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterMember:
    boto3_raw_data: "type_defs.DBClusterMemberTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    IsClusterWriter = field("IsClusterWriter")
    DBClusterParameterGroupStatus = field("DBClusterParameterGroupStatus")
    PromotionTier = field("PromotionTier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBClusterMemberTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterOptionGroupStatus:
    boto3_raw_data: "type_defs.DBClusterOptionGroupStatusTypeDef" = dataclasses.field()

    DBClusterOptionGroupName = field("DBClusterOptionGroupName")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterOptionGroupStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterOptionGroupStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Parameter:
    boto3_raw_data: "type_defs.ParameterTypeDef" = dataclasses.field()

    ParameterName = field("ParameterName")
    ParameterValue = field("ParameterValue")
    Description = field("Description")
    Source = field("Source")
    ApplyType = field("ApplyType")
    DataType = field("DataType")
    AllowedValues = field("AllowedValues")
    IsModifiable = field("IsModifiable")
    MinimumEngineVersion = field("MinimumEngineVersion")
    ApplyMethod = field("ApplyMethod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterRole:
    boto3_raw_data: "type_defs.DBClusterRoleTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    Status = field("Status")
    FeatureName = field("FeatureName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterRoleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBClusterRoleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterSnapshotAttribute:
    boto3_raw_data: "type_defs.DBClusterSnapshotAttributeTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeValues = field("AttributeValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterSnapshotAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterSnapshotAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessV2ScalingConfigurationInfo:
    boto3_raw_data: "type_defs.ServerlessV2ScalingConfigurationInfoTypeDef" = (
        dataclasses.field()
    )

    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerlessV2ScalingConfigurationInfoTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerlessV2ScalingConfigurationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcSecurityGroupMembership:
    boto3_raw_data: "type_defs.VpcSecurityGroupMembershipTypeDef" = dataclasses.field()

    VpcSecurityGroupId = field("VpcSecurityGroupId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcSecurityGroupMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcSecurityGroupMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Timezone:
    boto3_raw_data: "type_defs.TimezoneTypeDef" = dataclasses.field()

    TimezoneName = field("TimezoneName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimezoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimezoneTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeTarget:
    boto3_raw_data: "type_defs.UpgradeTargetTypeDef" = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    Description = field("Description")
    AutoUpgrade = field("AutoUpgrade")
    IsMajorVersionUpgrade = field("IsMajorVersionUpgrade")
    SupportsGlobalDatabases = field("SupportsGlobalDatabases")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpgradeTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpgradeTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBInstanceStatusInfo:
    boto3_raw_data: "type_defs.DBInstanceStatusInfoTypeDef" = dataclasses.field()

    StatusType = field("StatusType")
    Normal = field("Normal")
    Status = field("Status")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBInstanceStatusInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBInstanceStatusInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBParameterGroupStatus:
    boto3_raw_data: "type_defs.DBParameterGroupStatusTypeDef" = dataclasses.field()

    DBParameterGroupName = field("DBParameterGroupName")
    ParameterApplyStatus = field("ParameterApplyStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBParameterGroupStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBParameterGroupStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSecurityGroupMembership:
    boto3_raw_data: "type_defs.DBSecurityGroupMembershipTypeDef" = dataclasses.field()

    DBSecurityGroupName = field("DBSecurityGroupName")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBSecurityGroupMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBSecurityGroupMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainMembership:
    boto3_raw_data: "type_defs.DomainMembershipTypeDef" = dataclasses.field()

    Domain = field("Domain")
    Status = field("Status")
    FQDN = field("FQDN")
    IAMRoleName = field("IAMRoleName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainMembershipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Endpoint:
    boto3_raw_data: "type_defs.EndpointTypeDef" = dataclasses.field()

    Address = field("Address")
    Port = field("Port")
    HostedZoneId = field("HostedZoneId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionGroupMembership:
    boto3_raw_data: "type_defs.OptionGroupMembershipTypeDef" = dataclasses.field()

    OptionGroupName = field("OptionGroupName")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptionGroupMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptionGroupMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterEndpointMessage:
    boto3_raw_data: "type_defs.DeleteDBClusterEndpointMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDBClusterEndpointMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterMessage:
    boto3_raw_data: "type_defs.DeleteDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    SkipFinalSnapshot = field("SkipFinalSnapshot")
    FinalDBSnapshotIdentifier = field("FinalDBSnapshotIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.DeleteDBClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDBClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterSnapshotMessage:
    boto3_raw_data: "type_defs.DeleteDBClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDBClusterSnapshotMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBInstanceMessage:
    boto3_raw_data: "type_defs.DeleteDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    SkipFinalSnapshot = field("SkipFinalSnapshot")
    FinalDBSnapshotIdentifier = field("FinalDBSnapshotIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBParameterGroupMessage:
    boto3_raw_data: "type_defs.DeleteDBParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDBParameterGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBSubnetGroupMessage:
    boto3_raw_data: "type_defs.DeleteDBSubnetGroupMessageTypeDef" = dataclasses.field()

    DBSubnetGroupName = field("DBSubnetGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBSubnetGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventSubscriptionMessage:
    boto3_raw_data: "type_defs.DeleteEventSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventSubscriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlobalClusterMessage:
    boto3_raw_data: "type_defs.DeleteGlobalClusterMessageTypeDef" = dataclasses.field()

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGlobalClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
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
class DescribeDBClusterSnapshotAttributesMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterSnapshotAttributesMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterSnapshotAttributesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterSnapshotAttributesMessageTypeDef"]
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
class DescribeGlobalClustersMessage:
    boto3_raw_data: "type_defs.DescribeGlobalClustersMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGlobalClustersMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalClustersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeValidDBInstanceModificationsMessage:
    boto3_raw_data: "type_defs.DescribeValidDBInstanceModificationsMessageTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeValidDBInstanceModificationsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeValidDBInstanceModificationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DoubleRange:
    boto3_raw_data: "type_defs.DoubleRangeTypeDef" = dataclasses.field()

    From = field("From")
    To = field("To")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DoubleRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DoubleRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventCategoriesMap:
    boto3_raw_data: "type_defs.EventCategoriesMapTypeDef" = dataclasses.field()

    SourceType = field("SourceType")
    EventCategories = field("EventCategories")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventCategoriesMapTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventCategoriesMapTypeDef"]
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

    SourceIdentifier = field("SourceIdentifier")
    SourceType = field("SourceType")
    Message = field("Message")
    EventCategories = field("EventCategories")
    Date = field("Date")
    SourceArn = field("SourceArn")

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
class FailoverDBClusterMessage:
    boto3_raw_data: "type_defs.FailoverDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    TargetDBInstanceIdentifier = field("TargetDBInstanceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverGlobalClusterMessage:
    boto3_raw_data: "type_defs.FailoverGlobalClusterMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    TargetDbClusterIdentifier = field("TargetDbClusterIdentifier")
    AllowDataLoss = field("AllowDataLoss")
    Switchover = field("Switchover")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverGlobalClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverState:
    boto3_raw_data: "type_defs.FailoverStateTypeDef" = dataclasses.field()

    Status = field("Status")
    FromDbClusterArn = field("FromDbClusterArn")
    ToDbClusterArn = field("ToDbClusterArn")
    IsDataLossAllowed = field("IsDataLossAllowed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailoverStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailoverStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalClusterMember:
    boto3_raw_data: "type_defs.GlobalClusterMemberTypeDef" = dataclasses.field()

    DBClusterArn = field("DBClusterArn")
    Readers = field("Readers")
    IsWriter = field("IsWriter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalClusterMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalClusterMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterEndpointMessage:
    boto3_raw_data: "type_defs.ModifyDBClusterEndpointMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")
    EndpointType = field("EndpointType")
    StaticMembers = field("StaticMembers")
    ExcludedMembers = field("ExcludedMembers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBClusterEndpointMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterSnapshotAttributeMessage:
    boto3_raw_data: "type_defs.ModifyDBClusterSnapshotAttributeMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    AttributeName = field("AttributeName")
    ValuesToAdd = field("ValuesToAdd")
    ValuesToRemove = field("ValuesToRemove")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyDBClusterSnapshotAttributeMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterSnapshotAttributeMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBSubnetGroupMessage:
    boto3_raw_data: "type_defs.ModifyDBSubnetGroupMessageTypeDef" = dataclasses.field()

    DBSubnetGroupName = field("DBSubnetGroupName")
    SubnetIds = field("SubnetIds")
    DBSubnetGroupDescription = field("DBSubnetGroupDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBSubnetGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyEventSubscriptionMessage:
    boto3_raw_data: "type_defs.ModifyEventSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")
    SnsTopicArn = field("SnsTopicArn")
    SourceType = field("SourceType")
    EventCategories = field("EventCategories")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyEventSubscriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyEventSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyGlobalClusterMessage:
    boto3_raw_data: "type_defs.ModifyGlobalClusterMessageTypeDef" = dataclasses.field()

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    NewGlobalClusterIdentifier = field("NewGlobalClusterIdentifier")
    DeletionProtection = field("DeletionProtection")
    EngineVersion = field("EngineVersion")
    AllowMajorVersionUpgrade = field("AllowMajorVersionUpgrade")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyGlobalClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingMaintenanceAction:
    boto3_raw_data: "type_defs.PendingMaintenanceActionTypeDef" = dataclasses.field()

    Action = field("Action")
    AutoAppliedAfterDate = field("AutoAppliedAfterDate")
    ForcedApplyDate = field("ForcedApplyDate")
    OptInStatus = field("OptInStatus")
    CurrentApplyDate = field("CurrentApplyDate")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingMaintenanceActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingMaintenanceActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromoteReadReplicaDBClusterMessage:
    boto3_raw_data: "type_defs.PromoteReadReplicaDBClusterMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromoteReadReplicaDBClusterMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromoteReadReplicaDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Range:
    boto3_raw_data: "type_defs.RangeTypeDef" = dataclasses.field()

    From = field("From")
    To = field("To")
    Step = field("Step")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootDBInstanceMessage:
    boto3_raw_data: "type_defs.RebootDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    ForceFailover = field("ForceFailover")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFromGlobalClusterMessage:
    boto3_raw_data: "type_defs.RemoveFromGlobalClusterMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    DbClusterIdentifier = field("DbClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveFromGlobalClusterMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFromGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveRoleFromDBClusterMessage:
    boto3_raw_data: "type_defs.RemoveRoleFromDBClusterMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    RoleArn = field("RoleArn")
    FeatureName = field("FeatureName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveRoleFromDBClusterMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveRoleFromDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveSourceIdentifierFromSubscriptionMessage:
    boto3_raw_data: "type_defs.RemoveSourceIdentifierFromSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")
    SourceIdentifier = field("SourceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveSourceIdentifierFromSubscriptionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveSourceIdentifierFromSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsFromResourceMessage:
    boto3_raw_data: "type_defs.RemoveTagsFromResourceMessageTypeDef" = (
        dataclasses.field()
    )

    ResourceName = field("ResourceName")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveTagsFromResourceMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsFromResourceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDBClusterMessage:
    boto3_raw_data: "type_defs.StartDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDBClusterMessage:
    boto3_raw_data: "type_defs.StopDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SwitchoverGlobalClusterMessage:
    boto3_raw_data: "type_defs.SwitchoverGlobalClusterMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    TargetDbClusterIdentifier = field("TargetDbClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SwitchoverGlobalClusterMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SwitchoverGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddSourceIdentifierToSubscriptionResult:
    boto3_raw_data: "type_defs.AddSourceIdentifierToSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddSourceIdentifierToSubscriptionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddSourceIdentifierToSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterEndpointOutput:
    boto3_raw_data: "type_defs.CreateDBClusterEndpointOutputTypeDef" = (
        dataclasses.field()
    )

    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointResourceIdentifier = field("DBClusterEndpointResourceIdentifier")
    Endpoint = field("Endpoint")
    Status = field("Status")
    EndpointType = field("EndpointType")
    CustomEndpointType = field("CustomEndpointType")
    StaticMembers = field("StaticMembers")
    ExcludedMembers = field("ExcludedMembers")
    DBClusterEndpointArn = field("DBClusterEndpointArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDBClusterEndpointOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventSubscriptionResult:
    boto3_raw_data: "type_defs.CreateEventSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEventSubscriptionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterParameterGroupNameMessage:
    boto3_raw_data: "type_defs.DBClusterParameterGroupNameMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DBClusterParameterGroupNameMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterParameterGroupNameMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBParameterGroupNameMessage:
    boto3_raw_data: "type_defs.DBParameterGroupNameMessageTypeDef" = dataclasses.field()

    DBParameterGroupName = field("DBParameterGroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBParameterGroupNameMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBParameterGroupNameMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterEndpointOutput:
    boto3_raw_data: "type_defs.DeleteDBClusterEndpointOutputTypeDef" = (
        dataclasses.field()
    )

    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointResourceIdentifier = field("DBClusterEndpointResourceIdentifier")
    Endpoint = field("Endpoint")
    Status = field("Status")
    EndpointType = field("EndpointType")
    CustomEndpointType = field("CustomEndpointType")
    StaticMembers = field("StaticMembers")
    ExcludedMembers = field("ExcludedMembers")
    DBClusterEndpointArn = field("DBClusterEndpointArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDBClusterEndpointOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventSubscriptionResult:
    boto3_raw_data: "type_defs.DeleteEventSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventSubscriptionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventSubscriptionResultTypeDef"]
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
class EventSubscriptionsMessage:
    boto3_raw_data: "type_defs.EventSubscriptionsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def EventSubscriptionsList(self):  # pragma: no cover
        return EventSubscription.make_many(
            self.boto3_raw_data["EventSubscriptionsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventSubscriptionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSubscriptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterEndpointOutput:
    boto3_raw_data: "type_defs.ModifyDBClusterEndpointOutputTypeDef" = (
        dataclasses.field()
    )

    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointResourceIdentifier = field("DBClusterEndpointResourceIdentifier")
    Endpoint = field("Endpoint")
    Status = field("Status")
    EndpointType = field("EndpointType")
    CustomEndpointType = field("CustomEndpointType")
    StaticMembers = field("StaticMembers")
    ExcludedMembers = field("ExcludedMembers")
    DBClusterEndpointArn = field("DBClusterEndpointArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBClusterEndpointOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyEventSubscriptionResult:
    boto3_raw_data: "type_defs.ModifyEventSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyEventSubscriptionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyEventSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveSourceIdentifierFromSubscriptionResult:
    boto3_raw_data: "type_defs.RemoveSourceIdentifierFromSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveSourceIdentifierFromSubscriptionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveSourceIdentifierFromSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsToResourceMessage:
    boto3_raw_data: "type_defs.AddTagsToResourceMessageTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddTagsToResourceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTagsToResourceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.CopyDBClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    SourceDBClusterParameterGroupIdentifier = field(
        "SourceDBClusterParameterGroupIdentifier"
    )
    TargetDBClusterParameterGroupIdentifier = field(
        "TargetDBClusterParameterGroupIdentifier"
    )
    TargetDBClusterParameterGroupDescription = field(
        "TargetDBClusterParameterGroupDescription"
    )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CopyDBClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBClusterSnapshotMessage:
    boto3_raw_data: "type_defs.CopyDBClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    SourceDBClusterSnapshotIdentifier = field("SourceDBClusterSnapshotIdentifier")
    TargetDBClusterSnapshotIdentifier = field("TargetDBClusterSnapshotIdentifier")
    KmsKeyId = field("KmsKeyId")
    PreSignedUrl = field("PreSignedUrl")
    CopyTags = field("CopyTags")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SourceRegion = field("SourceRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDBClusterSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBParameterGroupMessage:
    boto3_raw_data: "type_defs.CopyDBParameterGroupMessageTypeDef" = dataclasses.field()

    SourceDBParameterGroupIdentifier = field("SourceDBParameterGroupIdentifier")
    TargetDBParameterGroupIdentifier = field("TargetDBParameterGroupIdentifier")
    TargetDBParameterGroupDescription = field("TargetDBParameterGroupDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDBParameterGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterEndpointMessage:
    boto3_raw_data: "type_defs.CreateDBClusterEndpointMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")
    EndpointType = field("EndpointType")
    StaticMembers = field("StaticMembers")
    ExcludedMembers = field("ExcludedMembers")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDBClusterEndpointMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.CreateDBClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDBClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterSnapshotMessage:
    boto3_raw_data: "type_defs.CreateDBClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDBClusterSnapshotMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBInstanceMessage:
    boto3_raw_data: "type_defs.CreateDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBInstanceClass = field("DBInstanceClass")
    Engine = field("Engine")
    DBClusterIdentifier = field("DBClusterIdentifier")
    DBName = field("DBName")
    AllocatedStorage = field("AllocatedStorage")
    MasterUsername = field("MasterUsername")
    MasterUserPassword = field("MasterUserPassword")
    DBSecurityGroups = field("DBSecurityGroups")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    AvailabilityZone = field("AvailabilityZone")
    DBSubnetGroupName = field("DBSubnetGroupName")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    DBParameterGroupName = field("DBParameterGroupName")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    PreferredBackupWindow = field("PreferredBackupWindow")
    Port = field("Port")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    LicenseModel = field("LicenseModel")
    Iops = field("Iops")
    OptionGroupName = field("OptionGroupName")
    CharacterSetName = field("CharacterSetName")
    PubliclyAccessible = field("PubliclyAccessible")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    StorageType = field("StorageType")
    TdeCredentialArn = field("TdeCredentialArn")
    TdeCredentialPassword = field("TdeCredentialPassword")
    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    Domain = field("Domain")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    MonitoringInterval = field("MonitoringInterval")
    MonitoringRoleArn = field("MonitoringRoleArn")
    DomainIAMRoleName = field("DomainIAMRoleName")
    PromotionTier = field("PromotionTier")
    Timezone = field("Timezone")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    EnablePerformanceInsights = field("EnablePerformanceInsights")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")
    DeletionProtection = field("DeletionProtection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBParameterGroupMessage:
    boto3_raw_data: "type_defs.CreateDBParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDBParameterGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBSubnetGroupMessage:
    boto3_raw_data: "type_defs.CreateDBSubnetGroupMessageTypeDef" = dataclasses.field()

    DBSubnetGroupName = field("DBSubnetGroupName")
    DBSubnetGroupDescription = field("DBSubnetGroupDescription")
    SubnetIds = field("SubnetIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBSubnetGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventSubscriptionMessage:
    boto3_raw_data: "type_defs.CreateEventSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")
    SnsTopicArn = field("SnsTopicArn")
    SourceType = field("SourceType")
    EventCategories = field("EventCategories")
    SourceIds = field("SourceIds")
    Enabled = field("Enabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEventSubscriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagListMessage:
    boto3_raw_data: "type_defs.TagListMessageTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagListMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagListMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderableDBInstanceOption:
    boto3_raw_data: "type_defs.OrderableDBInstanceOptionTypeDef" = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBInstanceClass = field("DBInstanceClass")
    LicenseModel = field("LicenseModel")

    @cached_property
    def AvailabilityZones(self):  # pragma: no cover
        return AvailabilityZone.make_many(self.boto3_raw_data["AvailabilityZones"])

    MultiAZCapable = field("MultiAZCapable")
    ReadReplicaCapable = field("ReadReplicaCapable")
    Vpc = field("Vpc")
    SupportsStorageEncryption = field("SupportsStorageEncryption")
    StorageType = field("StorageType")
    SupportsIops = field("SupportsIops")
    SupportsEnhancedMonitoring = field("SupportsEnhancedMonitoring")
    SupportsIAMDatabaseAuthentication = field("SupportsIAMDatabaseAuthentication")
    SupportsPerformanceInsights = field("SupportsPerformanceInsights")
    MinStorageSize = field("MinStorageSize")
    MaxStorageSize = field("MaxStorageSize")
    MinIopsPerDbInstance = field("MinIopsPerDbInstance")
    MaxIopsPerDbInstance = field("MaxIopsPerDbInstance")
    MinIopsPerGib = field("MinIopsPerGib")
    MaxIopsPerGib = field("MaxIopsPerGib")
    SupportsGlobalDatabases = field("SupportsGlobalDatabases")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrderableDBInstanceOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrderableDBInstanceOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subnet:
    boto3_raw_data: "type_defs.SubnetTypeDef" = dataclasses.field()

    SubnetIdentifier = field("SubnetIdentifier")

    @cached_property
    def SubnetAvailabilityZone(self):  # pragma: no cover
        return AvailabilityZone.make_one(self.boto3_raw_data["SubnetAvailabilityZone"])

    SubnetStatus = field("SubnetStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubnetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubnetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBInstanceMessage:
    boto3_raw_data: "type_defs.ModifyDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    AllocatedStorage = field("AllocatedStorage")
    DBInstanceClass = field("DBInstanceClass")
    DBSubnetGroupName = field("DBSubnetGroupName")
    DBSecurityGroups = field("DBSecurityGroups")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    ApplyImmediately = field("ApplyImmediately")
    MasterUserPassword = field("MasterUserPassword")
    DBParameterGroupName = field("DBParameterGroupName")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    PreferredBackupWindow = field("PreferredBackupWindow")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    AllowMajorVersionUpgrade = field("AllowMajorVersionUpgrade")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    LicenseModel = field("LicenseModel")
    Iops = field("Iops")
    OptionGroupName = field("OptionGroupName")
    NewDBInstanceIdentifier = field("NewDBInstanceIdentifier")
    StorageType = field("StorageType")
    TdeCredentialArn = field("TdeCredentialArn")
    TdeCredentialPassword = field("TdeCredentialPassword")
    CACertificateIdentifier = field("CACertificateIdentifier")
    Domain = field("Domain")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    MonitoringInterval = field("MonitoringInterval")
    DBPortNumber = field("DBPortNumber")
    PubliclyAccessible = field("PubliclyAccessible")
    MonitoringRoleArn = field("MonitoringRoleArn")
    DomainIAMRoleName = field("DomainIAMRoleName")
    PromotionTier = field("PromotionTier")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    EnablePerformanceInsights = field("EnablePerformanceInsights")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")

    @cached_property
    def CloudwatchLogsExportConfiguration(self):  # pragma: no cover
        return CloudwatchLogsExportConfiguration.make_one(
            self.boto3_raw_data["CloudwatchLogsExportConfiguration"]
        )

    DeletionProtection = field("DeletionProtection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterPendingModifiedValues:
    boto3_raw_data: "type_defs.ClusterPendingModifiedValuesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PendingCloudwatchLogsExports(self):  # pragma: no cover
        return PendingCloudwatchLogsExports.make_one(
            self.boto3_raw_data["PendingCloudwatchLogsExports"]
        )

    DBClusterIdentifier = field("DBClusterIdentifier")
    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")
    EngineVersion = field("EngineVersion")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    StorageType = field("StorageType")
    AllocatedStorage = field("AllocatedStorage")
    Iops = field("Iops")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterPendingModifiedValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterPendingModifiedValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingModifiedValues:
    boto3_raw_data: "type_defs.PendingModifiedValuesTypeDef" = dataclasses.field()

    DBInstanceClass = field("DBInstanceClass")
    AllocatedStorage = field("AllocatedStorage")
    MasterUserPassword = field("MasterUserPassword")
    Port = field("Port")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    LicenseModel = field("LicenseModel")
    Iops = field("Iops")
    DBInstanceIdentifier = field("DBInstanceIdentifier")
    StorageType = field("StorageType")
    CACertificateIdentifier = field("CACertificateIdentifier")
    DBSubnetGroupName = field("DBSubnetGroupName")

    @cached_property
    def PendingCloudwatchLogsExports(self):  # pragma: no cover
        return PendingCloudwatchLogsExports.make_one(
            self.boto3_raw_data["PendingCloudwatchLogsExports"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingModifiedValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingModifiedValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBClusterParameterGroupResult:
    boto3_raw_data: "type_defs.CopyDBClusterParameterGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterParameterGroup(self):  # pragma: no cover
        return DBClusterParameterGroup.make_one(
            self.boto3_raw_data["DBClusterParameterGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CopyDBClusterParameterGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBClusterParameterGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterParameterGroupResult:
    boto3_raw_data: "type_defs.CreateDBClusterParameterGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterParameterGroup(self):  # pragma: no cover
        return DBClusterParameterGroup.make_one(
            self.boto3_raw_data["DBClusterParameterGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDBClusterParameterGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterParameterGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterParameterGroupsMessage:
    boto3_raw_data: "type_defs.DBClusterParameterGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def DBClusterParameterGroups(self):  # pragma: no cover
        return DBClusterParameterGroup.make_many(
            self.boto3_raw_data["DBClusterParameterGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DBClusterParameterGroupsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBClusterSnapshotResult:
    boto3_raw_data: "type_defs.CopyDBClusterSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def DBClusterSnapshot(self):  # pragma: no cover
        return DBClusterSnapshot.make_one(self.boto3_raw_data["DBClusterSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDBClusterSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterSnapshotResult:
    boto3_raw_data: "type_defs.CreateDBClusterSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterSnapshot(self):  # pragma: no cover
        return DBClusterSnapshot.make_one(self.boto3_raw_data["DBClusterSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDBClusterSnapshotResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterSnapshotMessage:
    boto3_raw_data: "type_defs.DBClusterSnapshotMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBClusterSnapshots(self):  # pragma: no cover
        return DBClusterSnapshot.make_many(self.boto3_raw_data["DBClusterSnapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterSnapshotResult:
    boto3_raw_data: "type_defs.DeleteDBClusterSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterSnapshot(self):  # pragma: no cover
        return DBClusterSnapshot.make_one(self.boto3_raw_data["DBClusterSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDBClusterSnapshotResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBParameterGroupResult:
    boto3_raw_data: "type_defs.CopyDBParameterGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def DBParameterGroup(self):  # pragma: no cover
        return DBParameterGroup.make_one(self.boto3_raw_data["DBParameterGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDBParameterGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBParameterGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBParameterGroupResult:
    boto3_raw_data: "type_defs.CreateDBParameterGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBParameterGroup(self):  # pragma: no cover
        return DBParameterGroup.make_one(self.boto3_raw_data["DBParameterGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBParameterGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBParameterGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBParameterGroupsMessage:
    boto3_raw_data: "type_defs.DBParameterGroupsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBParameterGroups(self):  # pragma: no cover
        return DBParameterGroup.make_many(self.boto3_raw_data["DBParameterGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBParameterGroupsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterMessage:
    boto3_raw_data: "type_defs.CreateDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    Engine = field("Engine")
    AvailabilityZones = field("AvailabilityZones")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    CharacterSetName = field("CharacterSetName")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    DatabaseName = field("DatabaseName")
    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    DBSubnetGroupName = field("DBSubnetGroupName")
    EngineVersion = field("EngineVersion")
    Port = field("Port")
    MasterUsername = field("MasterUsername")
    MasterUserPassword = field("MasterUserPassword")
    OptionGroupName = field("OptionGroupName")
    PreferredBackupWindow = field("PreferredBackupWindow")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    ReplicationSourceIdentifier = field("ReplicationSourceIdentifier")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    PreSignedUrl = field("PreSignedUrl")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")
    DeletionProtection = field("DeletionProtection")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfiguration.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    StorageType = field("StorageType")
    SourceRegion = field("SourceRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterMessage:
    boto3_raw_data: "type_defs.ModifyDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    NewDBClusterIdentifier = field("NewDBClusterIdentifier")
    ApplyImmediately = field("ApplyImmediately")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    Port = field("Port")
    MasterUserPassword = field("MasterUserPassword")
    OptionGroupName = field("OptionGroupName")
    PreferredBackupWindow = field("PreferredBackupWindow")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")

    @cached_property
    def CloudwatchLogsExportConfiguration(self):  # pragma: no cover
        return CloudwatchLogsExportConfiguration.make_one(
            self.boto3_raw_data["CloudwatchLogsExportConfiguration"]
        )

    EngineVersion = field("EngineVersion")
    AllowMajorVersionUpgrade = field("AllowMajorVersionUpgrade")
    DBInstanceParameterGroupName = field("DBInstanceParameterGroupName")
    DeletionProtection = field("DeletionProtection")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfiguration.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    StorageType = field("StorageType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBClusterFromSnapshotMessage:
    boto3_raw_data: "type_defs.RestoreDBClusterFromSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    Engine = field("Engine")
    AvailabilityZones = field("AvailabilityZones")
    EngineVersion = field("EngineVersion")
    Port = field("Port")
    DBSubnetGroupName = field("DBSubnetGroupName")
    DatabaseName = field("DatabaseName")
    OptionGroupName = field("OptionGroupName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    KmsKeyId = field("KmsKeyId")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")
    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    DeletionProtection = field("DeletionProtection")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfiguration.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    StorageType = field("StorageType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBClusterFromSnapshotMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBClusterFromSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterEndpointMessage:
    boto3_raw_data: "type_defs.DBClusterEndpointMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBClusterEndpoints(self):  # pragma: no cover
        return DBClusterEndpoint.make_many(self.boto3_raw_data["DBClusterEndpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterEndpointMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterParameterGroupDetails:
    boto3_raw_data: "type_defs.DBClusterParameterGroupDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DBClusterParameterGroupDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterParameterGroupDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBParameterGroupDetails:
    boto3_raw_data: "type_defs.DBParameterGroupDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBParameterGroupDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBParameterGroupDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineDefaults:
    boto3_raw_data: "type_defs.EngineDefaultsTypeDef" = dataclasses.field()

    DBParameterGroupFamily = field("DBParameterGroupFamily")
    Marker = field("Marker")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngineDefaultsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EngineDefaultsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.ModifyDBClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyDBClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBParameterGroupMessage:
    boto3_raw_data: "type_defs.ModifyDBParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBParameterGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetDBClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.ResetDBClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    ResetAllParameters = field("ResetAllParameters")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResetDBClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetDBClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetDBParameterGroupMessage:
    boto3_raw_data: "type_defs.ResetDBParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")
    ResetAllParameters = field("ResetAllParameters")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetDBParameterGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetDBParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterSnapshotAttributesResult:
    boto3_raw_data: "type_defs.DBClusterSnapshotAttributesResultTypeDef" = (
        dataclasses.field()
    )

    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")

    @cached_property
    def DBClusterSnapshotAttributes(self):  # pragma: no cover
        return DBClusterSnapshotAttribute.make_many(
            self.boto3_raw_data["DBClusterSnapshotAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DBClusterSnapshotAttributesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterSnapshotAttributesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBEngineVersion:
    boto3_raw_data: "type_defs.DBEngineVersionTypeDef" = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    DBEngineDescription = field("DBEngineDescription")
    DBEngineVersionDescription = field("DBEngineVersionDescription")

    @cached_property
    def DefaultCharacterSet(self):  # pragma: no cover
        return CharacterSet.make_one(self.boto3_raw_data["DefaultCharacterSet"])

    @cached_property
    def SupportedCharacterSets(self):  # pragma: no cover
        return CharacterSet.make_many(self.boto3_raw_data["SupportedCharacterSets"])

    @cached_property
    def ValidUpgradeTarget(self):  # pragma: no cover
        return UpgradeTarget.make_many(self.boto3_raw_data["ValidUpgradeTarget"])

    @cached_property
    def SupportedTimezones(self):  # pragma: no cover
        return Timezone.make_many(self.boto3_raw_data["SupportedTimezones"])

    ExportableLogTypes = field("ExportableLogTypes")
    SupportsLogExportsToCloudwatchLogs = field("SupportsLogExportsToCloudwatchLogs")
    SupportsReadReplica = field("SupportsReadReplica")
    SupportsGlobalDatabases = field("SupportsGlobalDatabases")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBEngineVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBEngineVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterEndpointsMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterEndpointsMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterEndpointsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterEndpointsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterParameterGroupsMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterParameterGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterParameterGroupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterParametersMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterParametersMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    Source = field("Source")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterParametersMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterParametersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterSnapshotsMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterSnapshotsMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterSnapshotsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterSnapshotsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClustersMessage:
    boto3_raw_data: "type_defs.DescribeDBClustersMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBClustersMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClustersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBEngineVersionsMessage:
    boto3_raw_data: "type_defs.DescribeDBEngineVersionsMessageTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBParameterGroupFamily = field("DBParameterGroupFamily")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    DefaultOnly = field("DefaultOnly")
    ListSupportedCharacterSets = field("ListSupportedCharacterSets")
    ListSupportedTimezones = field("ListSupportedTimezones")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBEngineVersionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBEngineVersionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBInstancesMessage:
    boto3_raw_data: "type_defs.DescribeDBInstancesMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBInstancesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBInstancesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBParameterGroupsMessage:
    boto3_raw_data: "type_defs.DescribeDBParameterGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBParameterGroupsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBParametersMessage:
    boto3_raw_data: "type_defs.DescribeDBParametersMessageTypeDef" = dataclasses.field()

    DBParameterGroupName = field("DBParameterGroupName")
    Source = field("Source")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBParametersMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBParametersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSubnetGroupsMessage:
    boto3_raw_data: "type_defs.DescribeDBSubnetGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    DBSubnetGroupName = field("DBSubnetGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBSubnetGroupsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSubnetGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultClusterParametersMessage:
    boto3_raw_data: "type_defs.DescribeEngineDefaultClusterParametersMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupFamily = field("DBParameterGroupFamily")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEngineDefaultClusterParametersMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineDefaultClusterParametersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultParametersMessage:
    boto3_raw_data: "type_defs.DescribeEngineDefaultParametersMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupFamily = field("DBParameterGroupFamily")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEngineDefaultParametersMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineDefaultParametersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventCategoriesMessage:
    boto3_raw_data: "type_defs.DescribeEventCategoriesMessageTypeDef" = (
        dataclasses.field()
    )

    SourceType = field("SourceType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventCategoriesMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventCategoriesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventSubscriptionsMessage:
    boto3_raw_data: "type_defs.DescribeEventSubscriptionsMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventSubscriptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventSubscriptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrderableDBInstanceOptionsMessage:
    boto3_raw_data: "type_defs.DescribeOrderableDBInstanceOptionsMessageTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBInstanceClass = field("DBInstanceClass")
    LicenseModel = field("LicenseModel")
    Vpc = field("Vpc")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrderableDBInstanceOptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrderableDBInstanceOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePendingMaintenanceActionsMessage:
    boto3_raw_data: "type_defs.DescribePendingMaintenanceActionsMessageTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePendingMaintenanceActionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePendingMaintenanceActionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceMessage:
    boto3_raw_data: "type_defs.ListTagsForResourceMessageTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterEndpointsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBClusterEndpointsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterEndpointsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterEndpointsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterParameterGroupsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeDBClusterParameterGroupsMessagePaginateTypeDef"
    ) = dataclasses.field()

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterParameterGroupsMessagePaginateTypeDef"
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
                "type_defs.DescribeDBClusterParameterGroupsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterParametersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBClusterParametersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    Source = field("Source")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterParametersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterParametersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterSnapshotsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBClusterSnapshotsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterSnapshotsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterSnapshotsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClustersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBClustersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClustersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClustersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBEngineVersionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBEngineVersionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBParameterGroupFamily = field("DBParameterGroupFamily")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    DefaultOnly = field("DefaultOnly")
    ListSupportedCharacterSets = field("ListSupportedCharacterSets")
    ListSupportedTimezones = field("ListSupportedTimezones")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBEngineVersionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBEngineVersionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBInstancesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBInstancesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBInstancesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBInstancesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBParameterGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBParameterGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBParameterGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBParameterGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBParametersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBParametersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")
    Source = field("Source")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBParametersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBParametersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSubnetGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBSubnetGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBSubnetGroupName = field("DBSubnetGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBSubnetGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSubnetGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultParametersMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeEngineDefaultParametersMessagePaginateTypeDef"
    ) = dataclasses.field()

    DBParameterGroupFamily = field("DBParameterGroupFamily")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEngineDefaultParametersMessagePaginateTypeDef"
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
                "type_defs.DescribeEngineDefaultParametersMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventSubscriptionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEventSubscriptionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventSubscriptionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventSubscriptionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalClustersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeGlobalClustersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGlobalClustersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalClustersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrderableDBInstanceOptionsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef"
    ) = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBInstanceClass = field("DBInstanceClass")
    LicenseModel = field("LicenseModel")
    Vpc = field("Vpc")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef"
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
                "type_defs.DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePendingMaintenanceActionsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribePendingMaintenanceActionsMessagePaginateTypeDef"
    ) = dataclasses.field()

    ResourceIdentifier = field("ResourceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePendingMaintenanceActionsMessagePaginateTypeDef"
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
                "type_defs.DescribePendingMaintenanceActionsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBInstancesMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeDBInstancesMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBInstancesMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBInstancesMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBInstancesMessageWait:
    boto3_raw_data: "type_defs.DescribeDBInstancesMessageWaitTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBInstancesMessageWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBInstancesMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEventsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    SourceIdentifier = field("SourceIdentifier")
    SourceType = field("SourceType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Duration = field("Duration")
    EventCategories = field("EventCategories")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventsMessagePaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsMessage:
    boto3_raw_data: "type_defs.DescribeEventsMessageTypeDef" = dataclasses.field()

    SourceIdentifier = field("SourceIdentifier")
    SourceType = field("SourceType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Duration = field("Duration")
    EventCategories = field("EventCategories")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBClusterToPointInTimeMessage:
    boto3_raw_data: "type_defs.RestoreDBClusterToPointInTimeMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    SourceDBClusterIdentifier = field("SourceDBClusterIdentifier")
    RestoreType = field("RestoreType")
    RestoreToTime = field("RestoreToTime")
    UseLatestRestorableTime = field("UseLatestRestorableTime")
    Port = field("Port")
    DBSubnetGroupName = field("DBSubnetGroupName")
    OptionGroupName = field("OptionGroupName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    KmsKeyId = field("KmsKeyId")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")
    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    DeletionProtection = field("DeletionProtection")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfiguration.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    StorageType = field("StorageType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBClusterToPointInTimeMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBClusterToPointInTimeMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventCategoriesMessage:
    boto3_raw_data: "type_defs.EventCategoriesMessageTypeDef" = dataclasses.field()

    @cached_property
    def EventCategoriesMapList(self):  # pragma: no cover
        return EventCategoriesMap.make_many(
            self.boto3_raw_data["EventCategoriesMapList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventCategoriesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventCategoriesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventsMessage:
    boto3_raw_data: "type_defs.EventsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def Events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["Events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventsMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventsMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalCluster:
    boto3_raw_data: "type_defs.GlobalClusterTypeDef" = dataclasses.field()

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    GlobalClusterResourceId = field("GlobalClusterResourceId")
    GlobalClusterArn = field("GlobalClusterArn")
    Status = field("Status")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    StorageEncrypted = field("StorageEncrypted")
    DeletionProtection = field("DeletionProtection")

    @cached_property
    def GlobalClusterMembers(self):  # pragma: no cover
        return GlobalClusterMember.make_many(
            self.boto3_raw_data["GlobalClusterMembers"]
        )

    @cached_property
    def FailoverState(self):  # pragma: no cover
        return FailoverState.make_one(self.boto3_raw_data["FailoverState"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlobalClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GlobalClusterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourcePendingMaintenanceActions:
    boto3_raw_data: "type_defs.ResourcePendingMaintenanceActionsTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")

    @cached_property
    def PendingMaintenanceActionDetails(self):  # pragma: no cover
        return PendingMaintenanceAction.make_many(
            self.boto3_raw_data["PendingMaintenanceActionDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResourcePendingMaintenanceActionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourcePendingMaintenanceActionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidStorageOptions:
    boto3_raw_data: "type_defs.ValidStorageOptionsTypeDef" = dataclasses.field()

    StorageType = field("StorageType")

    @cached_property
    def StorageSize(self):  # pragma: no cover
        return Range.make_many(self.boto3_raw_data["StorageSize"])

    @cached_property
    def ProvisionedIops(self):  # pragma: no cover
        return Range.make_many(self.boto3_raw_data["ProvisionedIops"])

    @cached_property
    def IopsToStorageRatio(self):  # pragma: no cover
        return DoubleRange.make_many(self.boto3_raw_data["IopsToStorageRatio"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidStorageOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidStorageOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderableDBInstanceOptionsMessage:
    boto3_raw_data: "type_defs.OrderableDBInstanceOptionsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrderableDBInstanceOptions(self):  # pragma: no cover
        return OrderableDBInstanceOption.make_many(
            self.boto3_raw_data["OrderableDBInstanceOptions"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrderableDBInstanceOptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrderableDBInstanceOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSubnetGroup:
    boto3_raw_data: "type_defs.DBSubnetGroupTypeDef" = dataclasses.field()

    DBSubnetGroupName = field("DBSubnetGroupName")
    DBSubnetGroupDescription = field("DBSubnetGroupDescription")
    VpcId = field("VpcId")
    SubnetGroupStatus = field("SubnetGroupStatus")

    @cached_property
    def Subnets(self):  # pragma: no cover
        return Subnet.make_many(self.boto3_raw_data["Subnets"])

    DBSubnetGroupArn = field("DBSubnetGroupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBSubnetGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBSubnetGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBCluster:
    boto3_raw_data: "type_defs.DBClusterTypeDef" = dataclasses.field()

    AllocatedStorage = field("AllocatedStorage")
    AvailabilityZones = field("AvailabilityZones")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    CharacterSetName = field("CharacterSetName")
    DatabaseName = field("DatabaseName")
    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterParameterGroup = field("DBClusterParameterGroup")
    DBSubnetGroup = field("DBSubnetGroup")
    Status = field("Status")
    PercentProgress = field("PercentProgress")
    EarliestRestorableTime = field("EarliestRestorableTime")
    Endpoint = field("Endpoint")
    ReaderEndpoint = field("ReaderEndpoint")
    MultiAZ = field("MultiAZ")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    LatestRestorableTime = field("LatestRestorableTime")
    Port = field("Port")
    MasterUsername = field("MasterUsername")

    @cached_property
    def DBClusterOptionGroupMemberships(self):  # pragma: no cover
        return DBClusterOptionGroupStatus.make_many(
            self.boto3_raw_data["DBClusterOptionGroupMemberships"]
        )

    PreferredBackupWindow = field("PreferredBackupWindow")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    ReplicationSourceIdentifier = field("ReplicationSourceIdentifier")
    ReadReplicaIdentifiers = field("ReadReplicaIdentifiers")

    @cached_property
    def DBClusterMembers(self):  # pragma: no cover
        return DBClusterMember.make_many(self.boto3_raw_data["DBClusterMembers"])

    @cached_property
    def VpcSecurityGroups(self):  # pragma: no cover
        return VpcSecurityGroupMembership.make_many(
            self.boto3_raw_data["VpcSecurityGroups"]
        )

    HostedZoneId = field("HostedZoneId")
    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    DbClusterResourceId = field("DbClusterResourceId")
    DBClusterArn = field("DBClusterArn")

    @cached_property
    def AssociatedRoles(self):  # pragma: no cover
        return DBClusterRole.make_many(self.boto3_raw_data["AssociatedRoles"])

    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")
    CloneGroupId = field("CloneGroupId")
    ClusterCreateTime = field("ClusterCreateTime")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    EnabledCloudwatchLogsExports = field("EnabledCloudwatchLogsExports")

    @cached_property
    def PendingModifiedValues(self):  # pragma: no cover
        return ClusterPendingModifiedValues.make_one(
            self.boto3_raw_data["PendingModifiedValues"]
        )

    DeletionProtection = field("DeletionProtection")
    CrossAccountClone = field("CrossAccountClone")
    AutomaticRestartTime = field("AutomaticRestartTime")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfigurationInfo.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    IOOptimizedNextAllowedModificationTime = field(
        "IOOptimizedNextAllowedModificationTime"
    )
    StorageType = field("StorageType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultClusterParametersResult:
    boto3_raw_data: "type_defs.DescribeEngineDefaultClusterParametersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EngineDefaults(self):  # pragma: no cover
        return EngineDefaults.make_one(self.boto3_raw_data["EngineDefaults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEngineDefaultClusterParametersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineDefaultClusterParametersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultParametersResult:
    boto3_raw_data: "type_defs.DescribeEngineDefaultParametersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EngineDefaults(self):  # pragma: no cover
        return EngineDefaults.make_one(self.boto3_raw_data["EngineDefaults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEngineDefaultParametersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineDefaultParametersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterSnapshotAttributesResult:
    boto3_raw_data: "type_defs.DescribeDBClusterSnapshotAttributesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterSnapshotAttributesResult(self):  # pragma: no cover
        return DBClusterSnapshotAttributesResult.make_one(
            self.boto3_raw_data["DBClusterSnapshotAttributesResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterSnapshotAttributesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterSnapshotAttributesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterSnapshotAttributeResult:
    boto3_raw_data: "type_defs.ModifyDBClusterSnapshotAttributeResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterSnapshotAttributesResult(self):  # pragma: no cover
        return DBClusterSnapshotAttributesResult.make_one(
            self.boto3_raw_data["DBClusterSnapshotAttributesResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyDBClusterSnapshotAttributeResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterSnapshotAttributeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBEngineVersionMessage:
    boto3_raw_data: "type_defs.DBEngineVersionMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBEngineVersions(self):  # pragma: no cover
        return DBEngineVersion.make_many(self.boto3_raw_data["DBEngineVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBEngineVersionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBEngineVersionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalClusterResult:
    boto3_raw_data: "type_defs.CreateGlobalClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlobalClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlobalClusterResult:
    boto3_raw_data: "type_defs.DeleteGlobalClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGlobalClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverGlobalClusterResult:
    boto3_raw_data: "type_defs.FailoverGlobalClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverGlobalClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalClustersMessage:
    boto3_raw_data: "type_defs.GlobalClustersMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def GlobalClusters(self):  # pragma: no cover
        return GlobalCluster.make_many(self.boto3_raw_data["GlobalClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalClustersMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalClustersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyGlobalClusterResult:
    boto3_raw_data: "type_defs.ModifyGlobalClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyGlobalClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFromGlobalClusterResult:
    boto3_raw_data: "type_defs.RemoveFromGlobalClusterResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveFromGlobalClusterResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFromGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SwitchoverGlobalClusterResult:
    boto3_raw_data: "type_defs.SwitchoverGlobalClusterResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SwitchoverGlobalClusterResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SwitchoverGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplyPendingMaintenanceActionResult:
    boto3_raw_data: "type_defs.ApplyPendingMaintenanceActionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourcePendingMaintenanceActions(self):  # pragma: no cover
        return ResourcePendingMaintenanceActions.make_one(
            self.boto3_raw_data["ResourcePendingMaintenanceActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplyPendingMaintenanceActionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyPendingMaintenanceActionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingMaintenanceActionsMessage:
    boto3_raw_data: "type_defs.PendingMaintenanceActionsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PendingMaintenanceActions(self):  # pragma: no cover
        return ResourcePendingMaintenanceActions.make_many(
            self.boto3_raw_data["PendingMaintenanceActions"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PendingMaintenanceActionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingMaintenanceActionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidDBInstanceModificationsMessage:
    boto3_raw_data: "type_defs.ValidDBInstanceModificationsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Storage(self):  # pragma: no cover
        return ValidStorageOptions.make_many(self.boto3_raw_data["Storage"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidDBInstanceModificationsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidDBInstanceModificationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBSubnetGroupResult:
    boto3_raw_data: "type_defs.CreateDBSubnetGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def DBSubnetGroup(self):  # pragma: no cover
        return DBSubnetGroup.make_one(self.boto3_raw_data["DBSubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBSubnetGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBSubnetGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBInstance:
    boto3_raw_data: "type_defs.DBInstanceTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBInstanceClass = field("DBInstanceClass")
    Engine = field("Engine")
    DBInstanceStatus = field("DBInstanceStatus")
    MasterUsername = field("MasterUsername")
    DBName = field("DBName")

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["Endpoint"])

    AllocatedStorage = field("AllocatedStorage")
    InstanceCreateTime = field("InstanceCreateTime")
    PreferredBackupWindow = field("PreferredBackupWindow")
    BackupRetentionPeriod = field("BackupRetentionPeriod")

    @cached_property
    def DBSecurityGroups(self):  # pragma: no cover
        return DBSecurityGroupMembership.make_many(
            self.boto3_raw_data["DBSecurityGroups"]
        )

    @cached_property
    def VpcSecurityGroups(self):  # pragma: no cover
        return VpcSecurityGroupMembership.make_many(
            self.boto3_raw_data["VpcSecurityGroups"]
        )

    @cached_property
    def DBParameterGroups(self):  # pragma: no cover
        return DBParameterGroupStatus.make_many(
            self.boto3_raw_data["DBParameterGroups"]
        )

    AvailabilityZone = field("AvailabilityZone")

    @cached_property
    def DBSubnetGroup(self):  # pragma: no cover
        return DBSubnetGroup.make_one(self.boto3_raw_data["DBSubnetGroup"])

    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")

    @cached_property
    def PendingModifiedValues(self):  # pragma: no cover
        return PendingModifiedValues.make_one(
            self.boto3_raw_data["PendingModifiedValues"]
        )

    LatestRestorableTime = field("LatestRestorableTime")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    ReadReplicaSourceDBInstanceIdentifier = field(
        "ReadReplicaSourceDBInstanceIdentifier"
    )
    ReadReplicaDBInstanceIdentifiers = field("ReadReplicaDBInstanceIdentifiers")
    ReadReplicaDBClusterIdentifiers = field("ReadReplicaDBClusterIdentifiers")
    LicenseModel = field("LicenseModel")
    Iops = field("Iops")

    @cached_property
    def OptionGroupMemberships(self):  # pragma: no cover
        return OptionGroupMembership.make_many(
            self.boto3_raw_data["OptionGroupMemberships"]
        )

    CharacterSetName = field("CharacterSetName")
    SecondaryAvailabilityZone = field("SecondaryAvailabilityZone")
    PubliclyAccessible = field("PubliclyAccessible")

    @cached_property
    def StatusInfos(self):  # pragma: no cover
        return DBInstanceStatusInfo.make_many(self.boto3_raw_data["StatusInfos"])

    StorageType = field("StorageType")
    TdeCredentialArn = field("TdeCredentialArn")
    DbInstancePort = field("DbInstancePort")
    DBClusterIdentifier = field("DBClusterIdentifier")
    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    DbiResourceId = field("DbiResourceId")
    CACertificateIdentifier = field("CACertificateIdentifier")

    @cached_property
    def DomainMemberships(self):  # pragma: no cover
        return DomainMembership.make_many(self.boto3_raw_data["DomainMemberships"])

    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    MonitoringInterval = field("MonitoringInterval")
    EnhancedMonitoringResourceArn = field("EnhancedMonitoringResourceArn")
    MonitoringRoleArn = field("MonitoringRoleArn")
    PromotionTier = field("PromotionTier")
    DBInstanceArn = field("DBInstanceArn")
    Timezone = field("Timezone")
    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")
    PerformanceInsightsEnabled = field("PerformanceInsightsEnabled")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    EnabledCloudwatchLogsExports = field("EnabledCloudwatchLogsExports")
    DeletionProtection = field("DeletionProtection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBInstanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSubnetGroupMessage:
    boto3_raw_data: "type_defs.DBSubnetGroupMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBSubnetGroups(self):  # pragma: no cover
        return DBSubnetGroup.make_many(self.boto3_raw_data["DBSubnetGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBSubnetGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBSubnetGroupResult:
    boto3_raw_data: "type_defs.ModifyDBSubnetGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def DBSubnetGroup(self):  # pragma: no cover
        return DBSubnetGroup.make_one(self.boto3_raw_data["DBSubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBSubnetGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBSubnetGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterResult:
    boto3_raw_data: "type_defs.CreateDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterMessage:
    boto3_raw_data: "type_defs.DBClusterMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBClusters(self):  # pragma: no cover
        return DBCluster.make_many(self.boto3_raw_data["DBClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterResult:
    boto3_raw_data: "type_defs.DeleteDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverDBClusterResult:
    boto3_raw_data: "type_defs.FailoverDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterResult:
    boto3_raw_data: "type_defs.ModifyDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromoteReadReplicaDBClusterResult:
    boto3_raw_data: "type_defs.PromoteReadReplicaDBClusterResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromoteReadReplicaDBClusterResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromoteReadReplicaDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBClusterFromSnapshotResult:
    boto3_raw_data: "type_defs.RestoreDBClusterFromSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBClusterFromSnapshotResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBClusterFromSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBClusterToPointInTimeResult:
    boto3_raw_data: "type_defs.RestoreDBClusterToPointInTimeResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBClusterToPointInTimeResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBClusterToPointInTimeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDBClusterResult:
    boto3_raw_data: "type_defs.StartDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDBClusterResult:
    boto3_raw_data: "type_defs.StopDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeValidDBInstanceModificationsResult:
    boto3_raw_data: "type_defs.DescribeValidDBInstanceModificationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ValidDBInstanceModificationsMessage(self):  # pragma: no cover
        return ValidDBInstanceModificationsMessage.make_one(
            self.boto3_raw_data["ValidDBInstanceModificationsMessage"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeValidDBInstanceModificationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeValidDBInstanceModificationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBInstanceResult:
    boto3_raw_data: "type_defs.CreateDBInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBInstanceMessage:
    boto3_raw_data: "type_defs.DBInstanceMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBInstances(self):  # pragma: no cover
        return DBInstance.make_many(self.boto3_raw_data["DBInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBInstanceMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBInstanceResult:
    boto3_raw_data: "type_defs.DeleteDBInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBInstanceResult:
    boto3_raw_data: "type_defs.ModifyDBInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootDBInstanceResult:
    boto3_raw_data: "type_defs.RebootDBInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootDBInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootDBInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
