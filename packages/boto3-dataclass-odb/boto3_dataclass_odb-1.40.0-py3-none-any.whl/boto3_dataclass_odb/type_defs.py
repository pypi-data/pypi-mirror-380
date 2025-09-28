# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_odb import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptMarketplaceRegistrationInput:
    boto3_raw_data: "type_defs.AcceptMarketplaceRegistrationInputTypeDef" = (
        dataclasses.field()
    )

    marketplaceRegistrationToken = field("marketplaceRegistrationToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptMarketplaceRegistrationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptMarketplaceRegistrationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutonomousVirtualMachineSummary:
    boto3_raw_data: "type_defs.AutonomousVirtualMachineSummaryTypeDef" = (
        dataclasses.field()
    )

    autonomousVirtualMachineId = field("autonomousVirtualMachineId")
    status = field("status")
    statusReason = field("statusReason")
    vmName = field("vmName")
    dbServerId = field("dbServerId")
    dbServerDisplayName = field("dbServerDisplayName")
    cpuCoreCount = field("cpuCoreCount")
    memorySizeInGBs = field("memorySizeInGBs")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")
    clientIpAddress = field("clientIpAddress")
    cloudAutonomousVmClusterId = field("cloudAutonomousVmClusterId")
    ocid = field("ocid")
    ociResourceAnchorName = field("ociResourceAnchorName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutonomousVirtualMachineSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutonomousVirtualMachineSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudAutonomousVmClusterResourceDetails:
    boto3_raw_data: "type_defs.CloudAutonomousVmClusterResourceDetailsTypeDef" = (
        dataclasses.field()
    )

    cloudAutonomousVmClusterId = field("cloudAutonomousVmClusterId")
    unallocatedAdbStorageInTBs = field("unallocatedAdbStorageInTBs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudAutonomousVmClusterResourceDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudAutonomousVmClusterResourceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerContact:
    boto3_raw_data: "type_defs.CustomerContactTypeDef" = dataclasses.field()

    email = field("email")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomerContactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomerContactTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataCollectionOptions:
    boto3_raw_data: "type_defs.DataCollectionOptionsTypeDef" = dataclasses.field()

    isDiagnosticsEventsEnabled = field("isDiagnosticsEventsEnabled")
    isHealthMonitoringEnabled = field("isHealthMonitoringEnabled")
    isIncidentLogsEnabled = field("isIncidentLogsEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataCollectionOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataCollectionOptionsTypeDef"]
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
class CreateOdbNetworkInput:
    boto3_raw_data: "type_defs.CreateOdbNetworkInputTypeDef" = dataclasses.field()

    displayName = field("displayName")
    clientSubnetCidr = field("clientSubnetCidr")
    availabilityZone = field("availabilityZone")
    availabilityZoneId = field("availabilityZoneId")
    backupSubnetCidr = field("backupSubnetCidr")
    customDomainName = field("customDomainName")
    defaultDnsPrefix = field("defaultDnsPrefix")
    clientToken = field("clientToken")
    s3Access = field("s3Access")
    zeroEtlAccess = field("zeroEtlAccess")
    s3PolicyDocument = field("s3PolicyDocument")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOdbNetworkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOdbNetworkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOdbPeeringConnectionInput:
    boto3_raw_data: "type_defs.CreateOdbPeeringConnectionInputTypeDef" = (
        dataclasses.field()
    )

    odbNetworkId = field("odbNetworkId")
    peerNetworkId = field("peerNetworkId")
    displayName = field("displayName")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOdbPeeringConnectionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOdbPeeringConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DayOfWeek:
    boto3_raw_data: "type_defs.DayOfWeekTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DayOfWeekTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DayOfWeekTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbIormConfig:
    boto3_raw_data: "type_defs.DbIormConfigTypeDef" = dataclasses.field()

    dbName = field("dbName")
    flashCacheLimit = field("flashCacheLimit")
    share = field("share")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DbIormConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DbIormConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbNodeSummary:
    boto3_raw_data: "type_defs.DbNodeSummaryTypeDef" = dataclasses.field()

    dbNodeId = field("dbNodeId")
    dbNodeArn = field("dbNodeArn")
    status = field("status")
    statusReason = field("statusReason")
    additionalDetails = field("additionalDetails")
    backupIpId = field("backupIpId")
    backupVnic2Id = field("backupVnic2Id")
    backupVnicId = field("backupVnicId")
    cpuCoreCount = field("cpuCoreCount")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")
    dbServerId = field("dbServerId")
    dbSystemId = field("dbSystemId")
    faultDomain = field("faultDomain")
    hostIpId = field("hostIpId")
    hostname = field("hostname")
    ocid = field("ocid")
    ociResourceAnchorName = field("ociResourceAnchorName")
    maintenanceType = field("maintenanceType")
    memorySizeInGBs = field("memorySizeInGBs")
    softwareStorageSizeInGB = field("softwareStorageSizeInGB")
    createdAt = field("createdAt")
    timeMaintenanceWindowEnd = field("timeMaintenanceWindowEnd")
    timeMaintenanceWindowStart = field("timeMaintenanceWindowStart")
    totalCpuCoreCount = field("totalCpuCoreCount")
    vnic2Id = field("vnic2Id")
    vnicId = field("vnicId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DbNodeSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DbNodeSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbNode:
    boto3_raw_data: "type_defs.DbNodeTypeDef" = dataclasses.field()

    dbNodeId = field("dbNodeId")
    dbNodeArn = field("dbNodeArn")
    status = field("status")
    statusReason = field("statusReason")
    additionalDetails = field("additionalDetails")
    backupIpId = field("backupIpId")
    backupVnic2Id = field("backupVnic2Id")
    backupVnicId = field("backupVnicId")
    cpuCoreCount = field("cpuCoreCount")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")
    dbServerId = field("dbServerId")
    dbSystemId = field("dbSystemId")
    faultDomain = field("faultDomain")
    hostIpId = field("hostIpId")
    hostname = field("hostname")
    ocid = field("ocid")
    ociResourceAnchorName = field("ociResourceAnchorName")
    maintenanceType = field("maintenanceType")
    memorySizeInGBs = field("memorySizeInGBs")
    softwareStorageSizeInGB = field("softwareStorageSizeInGB")
    createdAt = field("createdAt")
    timeMaintenanceWindowEnd = field("timeMaintenanceWindowEnd")
    timeMaintenanceWindowStart = field("timeMaintenanceWindowStart")
    totalCpuCoreCount = field("totalCpuCoreCount")
    vnic2Id = field("vnic2Id")
    vnicId = field("vnicId")
    privateIpAddress = field("privateIpAddress")
    floatingIpAddress = field("floatingIpAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DbNodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DbNodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbServerPatchingDetails:
    boto3_raw_data: "type_defs.DbServerPatchingDetailsTypeDef" = dataclasses.field()

    estimatedPatchDuration = field("estimatedPatchDuration")
    patchingStatus = field("patchingStatus")
    timePatchingEnded = field("timePatchingEnded")
    timePatchingStarted = field("timePatchingStarted")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DbServerPatchingDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DbServerPatchingDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbSystemShapeSummary:
    boto3_raw_data: "type_defs.DbSystemShapeSummaryTypeDef" = dataclasses.field()

    availableCoreCount = field("availableCoreCount")
    availableCoreCountPerNode = field("availableCoreCountPerNode")
    availableDataStorageInTBs = field("availableDataStorageInTBs")
    availableDataStoragePerServerInTBs = field("availableDataStoragePerServerInTBs")
    availableDbNodePerNodeInGBs = field("availableDbNodePerNodeInGBs")
    availableDbNodeStorageInGBs = field("availableDbNodeStorageInGBs")
    availableMemoryInGBs = field("availableMemoryInGBs")
    availableMemoryPerNodeInGBs = field("availableMemoryPerNodeInGBs")
    coreCountIncrement = field("coreCountIncrement")
    maxStorageCount = field("maxStorageCount")
    maximumNodeCount = field("maximumNodeCount")
    minCoreCountPerNode = field("minCoreCountPerNode")
    minDataStorageInTBs = field("minDataStorageInTBs")
    minDbNodeStoragePerNodeInGBs = field("minDbNodeStoragePerNodeInGBs")
    minMemoryPerNodeInGBs = field("minMemoryPerNodeInGBs")
    minStorageCount = field("minStorageCount")
    minimumCoreCount = field("minimumCoreCount")
    minimumNodeCount = field("minimumNodeCount")
    runtimeMinimumCoreCount = field("runtimeMinimumCoreCount")
    shapeFamily = field("shapeFamily")
    shapeType = field("shapeType")
    name = field("name")
    computeModel = field("computeModel")
    areServerTypesSupported = field("areServerTypesSupported")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DbSystemShapeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DbSystemShapeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCloudAutonomousVmClusterInput:
    boto3_raw_data: "type_defs.DeleteCloudAutonomousVmClusterInputTypeDef" = (
        dataclasses.field()
    )

    cloudAutonomousVmClusterId = field("cloudAutonomousVmClusterId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCloudAutonomousVmClusterInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCloudAutonomousVmClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCloudExadataInfrastructureInput:
    boto3_raw_data: "type_defs.DeleteCloudExadataInfrastructureInputTypeDef" = (
        dataclasses.field()
    )

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCloudExadataInfrastructureInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCloudExadataInfrastructureInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCloudVmClusterInput:
    boto3_raw_data: "type_defs.DeleteCloudVmClusterInputTypeDef" = dataclasses.field()

    cloudVmClusterId = field("cloudVmClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCloudVmClusterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCloudVmClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOdbNetworkInput:
    boto3_raw_data: "type_defs.DeleteOdbNetworkInputTypeDef" = dataclasses.field()

    odbNetworkId = field("odbNetworkId")
    deleteAssociatedResources = field("deleteAssociatedResources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOdbNetworkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOdbNetworkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOdbPeeringConnectionInput:
    boto3_raw_data: "type_defs.DeleteOdbPeeringConnectionInputTypeDef" = (
        dataclasses.field()
    )

    odbPeeringConnectionId = field("odbPeeringConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteOdbPeeringConnectionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOdbPeeringConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudAutonomousVmClusterInput:
    boto3_raw_data: "type_defs.GetCloudAutonomousVmClusterInputTypeDef" = (
        dataclasses.field()
    )

    cloudAutonomousVmClusterId = field("cloudAutonomousVmClusterId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCloudAutonomousVmClusterInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudAutonomousVmClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudExadataInfrastructureInput:
    boto3_raw_data: "type_defs.GetCloudExadataInfrastructureInputTypeDef" = (
        dataclasses.field()
    )

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudExadataInfrastructureInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudExadataInfrastructureInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudExadataInfrastructureUnallocatedResourcesInput:
    boto3_raw_data: (
        "type_defs.GetCloudExadataInfrastructureUnallocatedResourcesInputTypeDef"
    ) = dataclasses.field()

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    dbServers = field("dbServers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudExadataInfrastructureUnallocatedResourcesInputTypeDef"
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
                "type_defs.GetCloudExadataInfrastructureUnallocatedResourcesInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudVmClusterInput:
    boto3_raw_data: "type_defs.GetCloudVmClusterInputTypeDef" = dataclasses.field()

    cloudVmClusterId = field("cloudVmClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCloudVmClusterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudVmClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDbNodeInput:
    boto3_raw_data: "type_defs.GetDbNodeInputTypeDef" = dataclasses.field()

    cloudVmClusterId = field("cloudVmClusterId")
    dbNodeId = field("dbNodeId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDbNodeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetDbNodeInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDbServerInput:
    boto3_raw_data: "type_defs.GetDbServerInputTypeDef" = dataclasses.field()

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    dbServerId = field("dbServerId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDbServerInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDbServerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOdbNetworkInput:
    boto3_raw_data: "type_defs.GetOdbNetworkInputTypeDef" = dataclasses.field()

    odbNetworkId = field("odbNetworkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOdbNetworkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOdbNetworkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOdbPeeringConnectionInput:
    boto3_raw_data: "type_defs.GetOdbPeeringConnectionInputTypeDef" = (
        dataclasses.field()
    )

    odbPeeringConnectionId = field("odbPeeringConnectionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOdbPeeringConnectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOdbPeeringConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OdbPeeringConnection:
    boto3_raw_data: "type_defs.OdbPeeringConnectionTypeDef" = dataclasses.field()

    odbPeeringConnectionId = field("odbPeeringConnectionId")
    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    odbPeeringConnectionArn = field("odbPeeringConnectionArn")
    odbNetworkArn = field("odbNetworkArn")
    peerNetworkArn = field("peerNetworkArn")
    odbPeeringConnectionType = field("odbPeeringConnectionType")
    createdAt = field("createdAt")
    percentProgress = field("percentProgress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OdbPeeringConnectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OdbPeeringConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GiVersionSummary:
    boto3_raw_data: "type_defs.GiVersionSummaryTypeDef" = dataclasses.field()

    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GiVersionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GiVersionSummaryTypeDef"]
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
class ListAutonomousVirtualMachinesInput:
    boto3_raw_data: "type_defs.ListAutonomousVirtualMachinesInputTypeDef" = (
        dataclasses.field()
    )

    cloudAutonomousVmClusterId = field("cloudAutonomousVmClusterId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutonomousVirtualMachinesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutonomousVirtualMachinesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudAutonomousVmClustersInput:
    boto3_raw_data: "type_defs.ListCloudAutonomousVmClustersInputTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudAutonomousVmClustersInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudAutonomousVmClustersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudExadataInfrastructuresInput:
    boto3_raw_data: "type_defs.ListCloudExadataInfrastructuresInputTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudExadataInfrastructuresInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudExadataInfrastructuresInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudVmClustersInput:
    boto3_raw_data: "type_defs.ListCloudVmClustersInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCloudVmClustersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudVmClustersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbNodesInput:
    boto3_raw_data: "type_defs.ListDbNodesInputTypeDef" = dataclasses.field()

    cloudVmClusterId = field("cloudVmClusterId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListDbNodesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbNodesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbServersInput:
    boto3_raw_data: "type_defs.ListDbServersInputTypeDef" = dataclasses.field()

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbServersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbServersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbSystemShapesInput:
    boto3_raw_data: "type_defs.ListDbSystemShapesInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    availabilityZone = field("availabilityZone")
    availabilityZoneId = field("availabilityZoneId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbSystemShapesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbSystemShapesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGiVersionsInput:
    boto3_raw_data: "type_defs.ListGiVersionsInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    shape = field("shape")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGiVersionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGiVersionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOdbNetworksInput:
    boto3_raw_data: "type_defs.ListOdbNetworksInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOdbNetworksInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOdbNetworksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOdbPeeringConnectionsInput:
    boto3_raw_data: "type_defs.ListOdbPeeringConnectionsInputTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    odbNetworkId = field("odbNetworkId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOdbPeeringConnectionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOdbPeeringConnectionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OdbPeeringConnectionSummary:
    boto3_raw_data: "type_defs.OdbPeeringConnectionSummaryTypeDef" = dataclasses.field()

    odbPeeringConnectionId = field("odbPeeringConnectionId")
    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    odbPeeringConnectionArn = field("odbPeeringConnectionArn")
    odbNetworkArn = field("odbNetworkArn")
    peerNetworkArn = field("peerNetworkArn")
    odbPeeringConnectionType = field("odbPeeringConnectionType")
    createdAt = field("createdAt")
    percentProgress = field("percentProgress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OdbPeeringConnectionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OdbPeeringConnectionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSystemVersionsInput:
    boto3_raw_data: "type_defs.ListSystemVersionsInputTypeDef" = dataclasses.field()

    giVersion = field("giVersion")
    shape = field("shape")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSystemVersionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSystemVersionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SystemVersionSummary:
    boto3_raw_data: "type_defs.SystemVersionSummaryTypeDef" = dataclasses.field()

    giVersion = field("giVersion")
    shape = field("shape")
    systemVersions = field("systemVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SystemVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SystemVersionSummaryTypeDef"]
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
class Month:
    boto3_raw_data: "type_defs.MonthTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonthTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedS3BackupAccess:
    boto3_raw_data: "type_defs.ManagedS3BackupAccessTypeDef" = dataclasses.field()

    status = field("status")
    ipv4Addresses = field("ipv4Addresses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedS3BackupAccessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedS3BackupAccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Access:
    boto3_raw_data: "type_defs.S3AccessTypeDef" = dataclasses.field()

    status = field("status")
    ipv4Addresses = field("ipv4Addresses")
    domainName = field("domainName")
    s3PolicyDocument = field("s3PolicyDocument")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3AccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3AccessTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNetworkEndpoint:
    boto3_raw_data: "type_defs.ServiceNetworkEndpointTypeDef" = dataclasses.field()

    vpcEndpointId = field("vpcEndpointId")
    vpcEndpointType = field("vpcEndpointType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceNetworkEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNetworkEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZeroEtlAccess:
    boto3_raw_data: "type_defs.ZeroEtlAccessTypeDef" = dataclasses.field()

    status = field("status")
    cidr = field("cidr")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ZeroEtlAccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ZeroEtlAccessTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OciDnsForwardingConfig:
    boto3_raw_data: "type_defs.OciDnsForwardingConfigTypeDef" = dataclasses.field()

    domainName = field("domainName")
    ociDnsListenerIp = field("ociDnsListenerIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OciDnsForwardingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OciDnsForwardingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootDbNodeInput:
    boto3_raw_data: "type_defs.RebootDbNodeInputTypeDef" = dataclasses.field()

    cloudVmClusterId = field("cloudVmClusterId")
    dbNodeId = field("dbNodeId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RebootDbNodeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootDbNodeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDbNodeInput:
    boto3_raw_data: "type_defs.StartDbNodeInputTypeDef" = dataclasses.field()

    cloudVmClusterId = field("cloudVmClusterId")
    dbNodeId = field("dbNodeId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartDbNodeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDbNodeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDbNodeInput:
    boto3_raw_data: "type_defs.StopDbNodeInputTypeDef" = dataclasses.field()

    cloudVmClusterId = field("cloudVmClusterId")
    dbNodeId = field("dbNodeId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopDbNodeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopDbNodeInputTypeDef"]],
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
class UpdateOdbNetworkInput:
    boto3_raw_data: "type_defs.UpdateOdbNetworkInputTypeDef" = dataclasses.field()

    odbNetworkId = field("odbNetworkId")
    displayName = field("displayName")
    peeredCidrsToBeAdded = field("peeredCidrsToBeAdded")
    peeredCidrsToBeRemoved = field("peeredCidrsToBeRemoved")
    s3Access = field("s3Access")
    zeroEtlAccess = field("zeroEtlAccess")
    s3PolicyDocument = field("s3PolicyDocument")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOdbNetworkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOdbNetworkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudExadataInfrastructureUnallocatedResources:
    boto3_raw_data: (
        "type_defs.CloudExadataInfrastructureUnallocatedResourcesTypeDef"
    ) = dataclasses.field()

    @cached_property
    def cloudAutonomousVmClusters(self):  # pragma: no cover
        return CloudAutonomousVmClusterResourceDetails.make_many(
            self.boto3_raw_data["cloudAutonomousVmClusters"]
        )

    cloudExadataInfrastructureDisplayName = field(
        "cloudExadataInfrastructureDisplayName"
    )
    exadataStorageInTBs = field("exadataStorageInTBs")
    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    localStorageInGBs = field("localStorageInGBs")
    memoryInGBs = field("memoryInGBs")
    ocpus = field("ocpus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudExadataInfrastructureUnallocatedResourcesTypeDef"
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
                "type_defs.CloudExadataInfrastructureUnallocatedResourcesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudVmClusterInput:
    boto3_raw_data: "type_defs.CreateCloudVmClusterInputTypeDef" = dataclasses.field()

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    cpuCoreCount = field("cpuCoreCount")
    displayName = field("displayName")
    giVersion = field("giVersion")
    hostname = field("hostname")
    sshPublicKeys = field("sshPublicKeys")
    odbNetworkId = field("odbNetworkId")
    clusterName = field("clusterName")

    @cached_property
    def dataCollectionOptions(self):  # pragma: no cover
        return DataCollectionOptions.make_one(
            self.boto3_raw_data["dataCollectionOptions"]
        )

    dataStorageSizeInTBs = field("dataStorageSizeInTBs")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")
    dbServers = field("dbServers")
    tags = field("tags")
    isLocalBackupEnabled = field("isLocalBackupEnabled")
    isSparseDiskgroupEnabled = field("isSparseDiskgroupEnabled")
    licenseModel = field("licenseModel")
    memorySizeInGBs = field("memorySizeInGBs")
    systemVersion = field("systemVersion")
    timeZone = field("timeZone")
    clientToken = field("clientToken")
    scanListenerPortTcp = field("scanListenerPortTcp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCloudVmClusterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudVmClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudAutonomousVmClusterOutput:
    boto3_raw_data: "type_defs.CreateCloudAutonomousVmClusterOutputTypeDef" = (
        dataclasses.field()
    )

    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    cloudAutonomousVmClusterId = field("cloudAutonomousVmClusterId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCloudAutonomousVmClusterOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudAutonomousVmClusterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudExadataInfrastructureOutput:
    boto3_raw_data: "type_defs.CreateCloudExadataInfrastructureOutputTypeDef" = (
        dataclasses.field()
    )

    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCloudExadataInfrastructureOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudExadataInfrastructureOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudVmClusterOutput:
    boto3_raw_data: "type_defs.CreateCloudVmClusterOutputTypeDef" = dataclasses.field()

    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    cloudVmClusterId = field("cloudVmClusterId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCloudVmClusterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudVmClusterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOdbNetworkOutput:
    boto3_raw_data: "type_defs.CreateOdbNetworkOutputTypeDef" = dataclasses.field()

    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    odbNetworkId = field("odbNetworkId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOdbNetworkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOdbNetworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOdbPeeringConnectionOutput:
    boto3_raw_data: "type_defs.CreateOdbPeeringConnectionOutputTypeDef" = (
        dataclasses.field()
    )

    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    odbPeeringConnectionId = field("odbPeeringConnectionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOdbPeeringConnectionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOdbPeeringConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOciOnboardingStatusOutput:
    boto3_raw_data: "type_defs.GetOciOnboardingStatusOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    existingTenancyActivationLink = field("existingTenancyActivationLink")
    newTenancyActivationLink = field("newTenancyActivationLink")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOciOnboardingStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOciOnboardingStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutonomousVirtualMachinesOutput:
    boto3_raw_data: "type_defs.ListAutonomousVirtualMachinesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def autonomousVirtualMachines(self):  # pragma: no cover
        return AutonomousVirtualMachineSummary.make_many(
            self.boto3_raw_data["autonomousVirtualMachines"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutonomousVirtualMachinesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutonomousVirtualMachinesOutputTypeDef"]
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
class RebootDbNodeOutput:
    boto3_raw_data: "type_defs.RebootDbNodeOutputTypeDef" = dataclasses.field()

    dbNodeId = field("dbNodeId")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootDbNodeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootDbNodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDbNodeOutput:
    boto3_raw_data: "type_defs.StartDbNodeOutputTypeDef" = dataclasses.field()

    dbNodeId = field("dbNodeId")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartDbNodeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDbNodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDbNodeOutput:
    boto3_raw_data: "type_defs.StopDbNodeOutputTypeDef" = dataclasses.field()

    dbNodeId = field("dbNodeId")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopDbNodeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDbNodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCloudExadataInfrastructureOutput:
    boto3_raw_data: "type_defs.UpdateCloudExadataInfrastructureOutputTypeDef" = (
        dataclasses.field()
    )

    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCloudExadataInfrastructureOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCloudExadataInfrastructureOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOdbNetworkOutput:
    boto3_raw_data: "type_defs.UpdateOdbNetworkOutputTypeDef" = dataclasses.field()

    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    odbNetworkId = field("odbNetworkId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOdbNetworkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOdbNetworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExadataIormConfig:
    boto3_raw_data: "type_defs.ExadataIormConfigTypeDef" = dataclasses.field()

    @cached_property
    def dbPlans(self):  # pragma: no cover
        return DbIormConfig.make_many(self.boto3_raw_data["dbPlans"])

    lifecycleDetails = field("lifecycleDetails")
    lifecycleState = field("lifecycleState")
    objective = field("objective")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExadataIormConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExadataIormConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbNodesOutput:
    boto3_raw_data: "type_defs.ListDbNodesOutputTypeDef" = dataclasses.field()

    @cached_property
    def dbNodes(self):  # pragma: no cover
        return DbNodeSummary.make_many(self.boto3_raw_data["dbNodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListDbNodesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbNodesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDbNodeOutput:
    boto3_raw_data: "type_defs.GetDbNodeOutputTypeDef" = dataclasses.field()

    @cached_property
    def dbNode(self):  # pragma: no cover
        return DbNode.make_one(self.boto3_raw_data["dbNode"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDbNodeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetDbNodeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbServerSummary:
    boto3_raw_data: "type_defs.DbServerSummaryTypeDef" = dataclasses.field()

    dbServerId = field("dbServerId")
    status = field("status")
    statusReason = field("statusReason")
    cpuCoreCount = field("cpuCoreCount")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")

    @cached_property
    def dbServerPatchingDetails(self):  # pragma: no cover
        return DbServerPatchingDetails.make_one(
            self.boto3_raw_data["dbServerPatchingDetails"]
        )

    displayName = field("displayName")
    exadataInfrastructureId = field("exadataInfrastructureId")
    ocid = field("ocid")
    ociResourceAnchorName = field("ociResourceAnchorName")
    maxCpuCount = field("maxCpuCount")
    maxDbNodeStorageInGBs = field("maxDbNodeStorageInGBs")
    maxMemoryInGBs = field("maxMemoryInGBs")
    memorySizeInGBs = field("memorySizeInGBs")
    shape = field("shape")
    createdAt = field("createdAt")
    vmClusterIds = field("vmClusterIds")
    computeModel = field("computeModel")
    autonomousVmClusterIds = field("autonomousVmClusterIds")
    autonomousVirtualMachineIds = field("autonomousVirtualMachineIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DbServerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DbServerSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbServer:
    boto3_raw_data: "type_defs.DbServerTypeDef" = dataclasses.field()

    dbServerId = field("dbServerId")
    status = field("status")
    statusReason = field("statusReason")
    cpuCoreCount = field("cpuCoreCount")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")

    @cached_property
    def dbServerPatchingDetails(self):  # pragma: no cover
        return DbServerPatchingDetails.make_one(
            self.boto3_raw_data["dbServerPatchingDetails"]
        )

    displayName = field("displayName")
    exadataInfrastructureId = field("exadataInfrastructureId")
    ocid = field("ocid")
    ociResourceAnchorName = field("ociResourceAnchorName")
    maxCpuCount = field("maxCpuCount")
    maxDbNodeStorageInGBs = field("maxDbNodeStorageInGBs")
    maxMemoryInGBs = field("maxMemoryInGBs")
    memorySizeInGBs = field("memorySizeInGBs")
    shape = field("shape")
    createdAt = field("createdAt")
    vmClusterIds = field("vmClusterIds")
    computeModel = field("computeModel")
    autonomousVmClusterIds = field("autonomousVmClusterIds")
    autonomousVirtualMachineIds = field("autonomousVirtualMachineIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DbServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DbServerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbSystemShapesOutput:
    boto3_raw_data: "type_defs.ListDbSystemShapesOutputTypeDef" = dataclasses.field()

    @cached_property
    def dbSystemShapes(self):  # pragma: no cover
        return DbSystemShapeSummary.make_many(self.boto3_raw_data["dbSystemShapes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbSystemShapesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbSystemShapesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOdbPeeringConnectionOutput:
    boto3_raw_data: "type_defs.GetOdbPeeringConnectionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def odbPeeringConnection(self):  # pragma: no cover
        return OdbPeeringConnection.make_one(
            self.boto3_raw_data["odbPeeringConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOdbPeeringConnectionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOdbPeeringConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGiVersionsOutput:
    boto3_raw_data: "type_defs.ListGiVersionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def giVersions(self):  # pragma: no cover
        return GiVersionSummary.make_many(self.boto3_raw_data["giVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGiVersionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGiVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutonomousVirtualMachinesInputPaginate:
    boto3_raw_data: "type_defs.ListAutonomousVirtualMachinesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    cloudAutonomousVmClusterId = field("cloudAutonomousVmClusterId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutonomousVirtualMachinesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutonomousVirtualMachinesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudAutonomousVmClustersInputPaginate:
    boto3_raw_data: "type_defs.ListCloudAutonomousVmClustersInputPaginateTypeDef" = (
        dataclasses.field()
    )

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudAutonomousVmClustersInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudAutonomousVmClustersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudExadataInfrastructuresInputPaginate:
    boto3_raw_data: "type_defs.ListCloudExadataInfrastructuresInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudExadataInfrastructuresInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudExadataInfrastructuresInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudVmClustersInputPaginate:
    boto3_raw_data: "type_defs.ListCloudVmClustersInputPaginateTypeDef" = (
        dataclasses.field()
    )

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCloudVmClustersInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudVmClustersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbNodesInputPaginate:
    boto3_raw_data: "type_defs.ListDbNodesInputPaginateTypeDef" = dataclasses.field()

    cloudVmClusterId = field("cloudVmClusterId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbNodesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbNodesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbServersInputPaginate:
    boto3_raw_data: "type_defs.ListDbServersInputPaginateTypeDef" = dataclasses.field()

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbServersInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbServersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbSystemShapesInputPaginate:
    boto3_raw_data: "type_defs.ListDbSystemShapesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    availabilityZone = field("availabilityZone")
    availabilityZoneId = field("availabilityZoneId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDbSystemShapesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbSystemShapesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGiVersionsInputPaginate:
    boto3_raw_data: "type_defs.ListGiVersionsInputPaginateTypeDef" = dataclasses.field()

    shape = field("shape")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGiVersionsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGiVersionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOdbNetworksInputPaginate:
    boto3_raw_data: "type_defs.ListOdbNetworksInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOdbNetworksInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOdbNetworksInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOdbPeeringConnectionsInputPaginate:
    boto3_raw_data: "type_defs.ListOdbPeeringConnectionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    odbNetworkId = field("odbNetworkId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOdbPeeringConnectionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOdbPeeringConnectionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSystemVersionsInputPaginate:
    boto3_raw_data: "type_defs.ListSystemVersionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    giVersion = field("giVersion")
    shape = field("shape")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSystemVersionsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSystemVersionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOdbPeeringConnectionsOutput:
    boto3_raw_data: "type_defs.ListOdbPeeringConnectionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def odbPeeringConnections(self):  # pragma: no cover
        return OdbPeeringConnectionSummary.make_many(
            self.boto3_raw_data["odbPeeringConnections"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOdbPeeringConnectionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOdbPeeringConnectionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSystemVersionsOutput:
    boto3_raw_data: "type_defs.ListSystemVersionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def systemVersions(self):  # pragma: no cover
        return SystemVersionSummary.make_many(self.boto3_raw_data["systemVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSystemVersionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSystemVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowOutput:
    boto3_raw_data: "type_defs.MaintenanceWindowOutputTypeDef" = dataclasses.field()

    customActionTimeoutInMins = field("customActionTimeoutInMins")

    @cached_property
    def daysOfWeek(self):  # pragma: no cover
        return DayOfWeek.make_many(self.boto3_raw_data["daysOfWeek"])

    hoursOfDay = field("hoursOfDay")
    isCustomActionTimeoutEnabled = field("isCustomActionTimeoutEnabled")
    leadTimeInWeeks = field("leadTimeInWeeks")

    @cached_property
    def months(self):  # pragma: no cover
        return Month.make_many(self.boto3_raw_data["months"])

    patchingMode = field("patchingMode")
    preference = field("preference")
    skipRu = field("skipRu")
    weeksOfMonth = field("weeksOfMonth")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MaintenanceWindowOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindow:
    boto3_raw_data: "type_defs.MaintenanceWindowTypeDef" = dataclasses.field()

    customActionTimeoutInMins = field("customActionTimeoutInMins")

    @cached_property
    def daysOfWeek(self):  # pragma: no cover
        return DayOfWeek.make_many(self.boto3_raw_data["daysOfWeek"])

    hoursOfDay = field("hoursOfDay")
    isCustomActionTimeoutEnabled = field("isCustomActionTimeoutEnabled")
    leadTimeInWeeks = field("leadTimeInWeeks")

    @cached_property
    def months(self):  # pragma: no cover
        return Month.make_many(self.boto3_raw_data["months"])

    patchingMode = field("patchingMode")
    preference = field("preference")
    skipRu = field("skipRu")
    weeksOfMonth = field("weeksOfMonth")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MaintenanceWindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedServices:
    boto3_raw_data: "type_defs.ManagedServicesTypeDef" = dataclasses.field()

    serviceNetworkArn = field("serviceNetworkArn")
    resourceGatewayArn = field("resourceGatewayArn")
    managedServicesIpv4Cidrs = field("managedServicesIpv4Cidrs")

    @cached_property
    def serviceNetworkEndpoint(self):  # pragma: no cover
        return ServiceNetworkEndpoint.make_one(
            self.boto3_raw_data["serviceNetworkEndpoint"]
        )

    @cached_property
    def managedS3BackupAccess(self):  # pragma: no cover
        return ManagedS3BackupAccess.make_one(
            self.boto3_raw_data["managedS3BackupAccess"]
        )

    @cached_property
    def zeroEtlAccess(self):  # pragma: no cover
        return ZeroEtlAccess.make_one(self.boto3_raw_data["zeroEtlAccess"])

    @cached_property
    def s3Access(self):  # pragma: no cover
        return S3Access.make_one(self.boto3_raw_data["s3Access"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManagedServicesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManagedServicesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudExadataInfrastructureUnallocatedResourcesOutput:
    boto3_raw_data: (
        "type_defs.GetCloudExadataInfrastructureUnallocatedResourcesOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def cloudExadataInfrastructureUnallocatedResources(self):  # pragma: no cover
        return CloudExadataInfrastructureUnallocatedResources.make_one(
            self.boto3_raw_data["cloudExadataInfrastructureUnallocatedResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudExadataInfrastructureUnallocatedResourcesOutputTypeDef"
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
                "type_defs.GetCloudExadataInfrastructureUnallocatedResourcesOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudVmClusterSummary:
    boto3_raw_data: "type_defs.CloudVmClusterSummaryTypeDef" = dataclasses.field()

    cloudVmClusterId = field("cloudVmClusterId")
    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    cloudVmClusterArn = field("cloudVmClusterArn")
    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    clusterName = field("clusterName")
    cpuCoreCount = field("cpuCoreCount")

    @cached_property
    def dataCollectionOptions(self):  # pragma: no cover
        return DataCollectionOptions.make_one(
            self.boto3_raw_data["dataCollectionOptions"]
        )

    dataStorageSizeInTBs = field("dataStorageSizeInTBs")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")
    dbServers = field("dbServers")
    diskRedundancy = field("diskRedundancy")
    giVersion = field("giVersion")
    hostname = field("hostname")

    @cached_property
    def iormConfigCache(self):  # pragma: no cover
        return ExadataIormConfig.make_one(self.boto3_raw_data["iormConfigCache"])

    isLocalBackupEnabled = field("isLocalBackupEnabled")
    isSparseDiskgroupEnabled = field("isSparseDiskgroupEnabled")
    lastUpdateHistoryEntryId = field("lastUpdateHistoryEntryId")
    licenseModel = field("licenseModel")
    listenerPort = field("listenerPort")
    memorySizeInGBs = field("memorySizeInGBs")
    nodeCount = field("nodeCount")
    ocid = field("ocid")
    ociResourceAnchorName = field("ociResourceAnchorName")
    ociUrl = field("ociUrl")
    domain = field("domain")
    scanDnsName = field("scanDnsName")
    scanDnsRecordId = field("scanDnsRecordId")
    scanIpIds = field("scanIpIds")
    shape = field("shape")
    sshPublicKeys = field("sshPublicKeys")
    storageSizeInGBs = field("storageSizeInGBs")
    systemVersion = field("systemVersion")
    createdAt = field("createdAt")
    timeZone = field("timeZone")
    vipIds = field("vipIds")
    odbNetworkId = field("odbNetworkId")
    percentProgress = field("percentProgress")
    computeModel = field("computeModel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudVmClusterSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudVmClusterSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudVmCluster:
    boto3_raw_data: "type_defs.CloudVmClusterTypeDef" = dataclasses.field()

    cloudVmClusterId = field("cloudVmClusterId")
    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    cloudVmClusterArn = field("cloudVmClusterArn")
    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    clusterName = field("clusterName")
    cpuCoreCount = field("cpuCoreCount")

    @cached_property
    def dataCollectionOptions(self):  # pragma: no cover
        return DataCollectionOptions.make_one(
            self.boto3_raw_data["dataCollectionOptions"]
        )

    dataStorageSizeInTBs = field("dataStorageSizeInTBs")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")
    dbServers = field("dbServers")
    diskRedundancy = field("diskRedundancy")
    giVersion = field("giVersion")
    hostname = field("hostname")

    @cached_property
    def iormConfigCache(self):  # pragma: no cover
        return ExadataIormConfig.make_one(self.boto3_raw_data["iormConfigCache"])

    isLocalBackupEnabled = field("isLocalBackupEnabled")
    isSparseDiskgroupEnabled = field("isSparseDiskgroupEnabled")
    lastUpdateHistoryEntryId = field("lastUpdateHistoryEntryId")
    licenseModel = field("licenseModel")
    listenerPort = field("listenerPort")
    memorySizeInGBs = field("memorySizeInGBs")
    nodeCount = field("nodeCount")
    ocid = field("ocid")
    ociResourceAnchorName = field("ociResourceAnchorName")
    ociUrl = field("ociUrl")
    domain = field("domain")
    scanDnsName = field("scanDnsName")
    scanDnsRecordId = field("scanDnsRecordId")
    scanIpIds = field("scanIpIds")
    shape = field("shape")
    sshPublicKeys = field("sshPublicKeys")
    storageSizeInGBs = field("storageSizeInGBs")
    systemVersion = field("systemVersion")
    createdAt = field("createdAt")
    timeZone = field("timeZone")
    vipIds = field("vipIds")
    odbNetworkId = field("odbNetworkId")
    percentProgress = field("percentProgress")
    computeModel = field("computeModel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloudVmClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CloudVmClusterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbServersOutput:
    boto3_raw_data: "type_defs.ListDbServersOutputTypeDef" = dataclasses.field()

    @cached_property
    def dbServers(self):  # pragma: no cover
        return DbServerSummary.make_many(self.boto3_raw_data["dbServers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbServersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbServersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDbServerOutput:
    boto3_raw_data: "type_defs.GetDbServerOutputTypeDef" = dataclasses.field()

    @cached_property
    def dbServer(self):  # pragma: no cover
        return DbServer.make_one(self.boto3_raw_data["dbServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDbServerOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDbServerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudAutonomousVmClusterSummary:
    boto3_raw_data: "type_defs.CloudAutonomousVmClusterSummaryTypeDef" = (
        dataclasses.field()
    )

    cloudAutonomousVmClusterId = field("cloudAutonomousVmClusterId")
    cloudAutonomousVmClusterArn = field("cloudAutonomousVmClusterArn")
    odbNetworkId = field("odbNetworkId")
    ociResourceAnchorName = field("ociResourceAnchorName")
    percentProgress = field("percentProgress")
    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    autonomousDataStoragePercentage = field("autonomousDataStoragePercentage")
    autonomousDataStorageSizeInTBs = field("autonomousDataStorageSizeInTBs")
    availableAutonomousDataStorageSizeInTBs = field(
        "availableAutonomousDataStorageSizeInTBs"
    )
    availableContainerDatabases = field("availableContainerDatabases")
    availableCpus = field("availableCpus")
    computeModel = field("computeModel")
    cpuCoreCount = field("cpuCoreCount")
    cpuCoreCountPerNode = field("cpuCoreCountPerNode")
    cpuPercentage = field("cpuPercentage")
    dataStorageSizeInGBs = field("dataStorageSizeInGBs")
    dataStorageSizeInTBs = field("dataStorageSizeInTBs")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")
    dbServers = field("dbServers")
    description = field("description")
    domain = field("domain")
    exadataStorageInTBsLowestScaledValue = field("exadataStorageInTBsLowestScaledValue")
    hostname = field("hostname")
    ocid = field("ocid")
    ociUrl = field("ociUrl")
    isMtlsEnabledVmCluster = field("isMtlsEnabledVmCluster")
    licenseModel = field("licenseModel")

    @cached_property
    def maintenanceWindow(self):  # pragma: no cover
        return MaintenanceWindowOutput.make_one(
            self.boto3_raw_data["maintenanceWindow"]
        )

    maxAcdsLowestScaledValue = field("maxAcdsLowestScaledValue")
    memoryPerOracleComputeUnitInGBs = field("memoryPerOracleComputeUnitInGBs")
    memorySizeInGBs = field("memorySizeInGBs")
    nodeCount = field("nodeCount")
    nonProvisionableAutonomousContainerDatabases = field(
        "nonProvisionableAutonomousContainerDatabases"
    )
    provisionableAutonomousContainerDatabases = field(
        "provisionableAutonomousContainerDatabases"
    )
    provisionedAutonomousContainerDatabases = field(
        "provisionedAutonomousContainerDatabases"
    )
    provisionedCpus = field("provisionedCpus")
    reclaimableCpus = field("reclaimableCpus")
    reservedCpus = field("reservedCpus")
    scanListenerPortNonTls = field("scanListenerPortNonTls")
    scanListenerPortTls = field("scanListenerPortTls")
    shape = field("shape")
    createdAt = field("createdAt")
    timeDatabaseSslCertificateExpires = field("timeDatabaseSslCertificateExpires")
    timeOrdsCertificateExpires = field("timeOrdsCertificateExpires")
    timeZone = field("timeZone")
    totalContainerDatabases = field("totalContainerDatabases")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudAutonomousVmClusterSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudAutonomousVmClusterSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudAutonomousVmCluster:
    boto3_raw_data: "type_defs.CloudAutonomousVmClusterTypeDef" = dataclasses.field()

    cloudAutonomousVmClusterId = field("cloudAutonomousVmClusterId")
    cloudAutonomousVmClusterArn = field("cloudAutonomousVmClusterArn")
    odbNetworkId = field("odbNetworkId")
    ociResourceAnchorName = field("ociResourceAnchorName")
    percentProgress = field("percentProgress")
    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    autonomousDataStoragePercentage = field("autonomousDataStoragePercentage")
    autonomousDataStorageSizeInTBs = field("autonomousDataStorageSizeInTBs")
    availableAutonomousDataStorageSizeInTBs = field(
        "availableAutonomousDataStorageSizeInTBs"
    )
    availableContainerDatabases = field("availableContainerDatabases")
    availableCpus = field("availableCpus")
    computeModel = field("computeModel")
    cpuCoreCount = field("cpuCoreCount")
    cpuCoreCountPerNode = field("cpuCoreCountPerNode")
    cpuPercentage = field("cpuPercentage")
    dataStorageSizeInGBs = field("dataStorageSizeInGBs")
    dataStorageSizeInTBs = field("dataStorageSizeInTBs")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")
    dbServers = field("dbServers")
    description = field("description")
    domain = field("domain")
    exadataStorageInTBsLowestScaledValue = field("exadataStorageInTBsLowestScaledValue")
    hostname = field("hostname")
    ocid = field("ocid")
    ociUrl = field("ociUrl")
    isMtlsEnabledVmCluster = field("isMtlsEnabledVmCluster")
    licenseModel = field("licenseModel")

    @cached_property
    def maintenanceWindow(self):  # pragma: no cover
        return MaintenanceWindowOutput.make_one(
            self.boto3_raw_data["maintenanceWindow"]
        )

    maxAcdsLowestScaledValue = field("maxAcdsLowestScaledValue")
    memoryPerOracleComputeUnitInGBs = field("memoryPerOracleComputeUnitInGBs")
    memorySizeInGBs = field("memorySizeInGBs")
    nodeCount = field("nodeCount")
    nonProvisionableAutonomousContainerDatabases = field(
        "nonProvisionableAutonomousContainerDatabases"
    )
    provisionableAutonomousContainerDatabases = field(
        "provisionableAutonomousContainerDatabases"
    )
    provisionedAutonomousContainerDatabases = field(
        "provisionedAutonomousContainerDatabases"
    )
    provisionedCpus = field("provisionedCpus")
    reclaimableCpus = field("reclaimableCpus")
    reservedCpus = field("reservedCpus")
    scanListenerPortNonTls = field("scanListenerPortNonTls")
    scanListenerPortTls = field("scanListenerPortTls")
    shape = field("shape")
    createdAt = field("createdAt")
    timeDatabaseSslCertificateExpires = field("timeDatabaseSslCertificateExpires")
    timeOrdsCertificateExpires = field("timeOrdsCertificateExpires")
    timeZone = field("timeZone")
    totalContainerDatabases = field("totalContainerDatabases")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudAutonomousVmClusterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudAutonomousVmClusterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudExadataInfrastructureSummary:
    boto3_raw_data: "type_defs.CloudExadataInfrastructureSummaryTypeDef" = (
        dataclasses.field()
    )

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    cloudExadataInfrastructureArn = field("cloudExadataInfrastructureArn")
    activatedStorageCount = field("activatedStorageCount")
    additionalStorageCount = field("additionalStorageCount")
    availableStorageSizeInGBs = field("availableStorageSizeInGBs")
    availabilityZone = field("availabilityZone")
    availabilityZoneId = field("availabilityZoneId")
    computeCount = field("computeCount")
    cpuCount = field("cpuCount")

    @cached_property
    def customerContactsToSendToOCI(self):  # pragma: no cover
        return CustomerContact.make_many(
            self.boto3_raw_data["customerContactsToSendToOCI"]
        )

    dataStorageSizeInTBs = field("dataStorageSizeInTBs")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")
    dbServerVersion = field("dbServerVersion")
    lastMaintenanceRunId = field("lastMaintenanceRunId")

    @cached_property
    def maintenanceWindow(self):  # pragma: no cover
        return MaintenanceWindowOutput.make_one(
            self.boto3_raw_data["maintenanceWindow"]
        )

    maxCpuCount = field("maxCpuCount")
    maxDataStorageInTBs = field("maxDataStorageInTBs")
    maxDbNodeStorageSizeInGBs = field("maxDbNodeStorageSizeInGBs")
    maxMemoryInGBs = field("maxMemoryInGBs")
    memorySizeInGBs = field("memorySizeInGBs")
    monthlyDbServerVersion = field("monthlyDbServerVersion")
    monthlyStorageServerVersion = field("monthlyStorageServerVersion")
    nextMaintenanceRunId = field("nextMaintenanceRunId")
    ociResourceAnchorName = field("ociResourceAnchorName")
    ociUrl = field("ociUrl")
    ocid = field("ocid")
    shape = field("shape")
    storageCount = field("storageCount")
    storageServerVersion = field("storageServerVersion")
    createdAt = field("createdAt")
    totalStorageSizeInGBs = field("totalStorageSizeInGBs")
    percentProgress = field("percentProgress")
    databaseServerType = field("databaseServerType")
    storageServerType = field("storageServerType")
    computeModel = field("computeModel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudExadataInfrastructureSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudExadataInfrastructureSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudExadataInfrastructure:
    boto3_raw_data: "type_defs.CloudExadataInfrastructureTypeDef" = dataclasses.field()

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    cloudExadataInfrastructureArn = field("cloudExadataInfrastructureArn")
    activatedStorageCount = field("activatedStorageCount")
    additionalStorageCount = field("additionalStorageCount")
    availableStorageSizeInGBs = field("availableStorageSizeInGBs")
    availabilityZone = field("availabilityZone")
    availabilityZoneId = field("availabilityZoneId")
    computeCount = field("computeCount")
    cpuCount = field("cpuCount")

    @cached_property
    def customerContactsToSendToOCI(self):  # pragma: no cover
        return CustomerContact.make_many(
            self.boto3_raw_data["customerContactsToSendToOCI"]
        )

    dataStorageSizeInTBs = field("dataStorageSizeInTBs")
    dbNodeStorageSizeInGBs = field("dbNodeStorageSizeInGBs")
    dbServerVersion = field("dbServerVersion")
    lastMaintenanceRunId = field("lastMaintenanceRunId")

    @cached_property
    def maintenanceWindow(self):  # pragma: no cover
        return MaintenanceWindowOutput.make_one(
            self.boto3_raw_data["maintenanceWindow"]
        )

    maxCpuCount = field("maxCpuCount")
    maxDataStorageInTBs = field("maxDataStorageInTBs")
    maxDbNodeStorageSizeInGBs = field("maxDbNodeStorageSizeInGBs")
    maxMemoryInGBs = field("maxMemoryInGBs")
    memorySizeInGBs = field("memorySizeInGBs")
    monthlyDbServerVersion = field("monthlyDbServerVersion")
    monthlyStorageServerVersion = field("monthlyStorageServerVersion")
    nextMaintenanceRunId = field("nextMaintenanceRunId")
    ociResourceAnchorName = field("ociResourceAnchorName")
    ociUrl = field("ociUrl")
    ocid = field("ocid")
    shape = field("shape")
    storageCount = field("storageCount")
    storageServerVersion = field("storageServerVersion")
    createdAt = field("createdAt")
    totalStorageSizeInGBs = field("totalStorageSizeInGBs")
    percentProgress = field("percentProgress")
    databaseServerType = field("databaseServerType")
    storageServerType = field("storageServerType")
    computeModel = field("computeModel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudExadataInfrastructureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudExadataInfrastructureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OdbNetworkSummary:
    boto3_raw_data: "type_defs.OdbNetworkSummaryTypeDef" = dataclasses.field()

    odbNetworkId = field("odbNetworkId")
    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    odbNetworkArn = field("odbNetworkArn")
    availabilityZone = field("availabilityZone")
    availabilityZoneId = field("availabilityZoneId")
    clientSubnetCidr = field("clientSubnetCidr")
    backupSubnetCidr = field("backupSubnetCidr")
    customDomainName = field("customDomainName")
    defaultDnsPrefix = field("defaultDnsPrefix")
    peeredCidrs = field("peeredCidrs")
    ociNetworkAnchorId = field("ociNetworkAnchorId")
    ociNetworkAnchorUrl = field("ociNetworkAnchorUrl")
    ociResourceAnchorName = field("ociResourceAnchorName")
    ociVcnId = field("ociVcnId")
    ociVcnUrl = field("ociVcnUrl")

    @cached_property
    def ociDnsForwardingConfigs(self):  # pragma: no cover
        return OciDnsForwardingConfig.make_many(
            self.boto3_raw_data["ociDnsForwardingConfigs"]
        )

    createdAt = field("createdAt")
    percentProgress = field("percentProgress")

    @cached_property
    def managedServices(self):  # pragma: no cover
        return ManagedServices.make_one(self.boto3_raw_data["managedServices"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OdbNetworkSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OdbNetworkSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OdbNetwork:
    boto3_raw_data: "type_defs.OdbNetworkTypeDef" = dataclasses.field()

    odbNetworkId = field("odbNetworkId")
    displayName = field("displayName")
    status = field("status")
    statusReason = field("statusReason")
    odbNetworkArn = field("odbNetworkArn")
    availabilityZone = field("availabilityZone")
    availabilityZoneId = field("availabilityZoneId")
    clientSubnetCidr = field("clientSubnetCidr")
    backupSubnetCidr = field("backupSubnetCidr")
    customDomainName = field("customDomainName")
    defaultDnsPrefix = field("defaultDnsPrefix")
    peeredCidrs = field("peeredCidrs")
    ociNetworkAnchorId = field("ociNetworkAnchorId")
    ociNetworkAnchorUrl = field("ociNetworkAnchorUrl")
    ociResourceAnchorName = field("ociResourceAnchorName")
    ociVcnId = field("ociVcnId")
    ociVcnUrl = field("ociVcnUrl")

    @cached_property
    def ociDnsForwardingConfigs(self):  # pragma: no cover
        return OciDnsForwardingConfig.make_many(
            self.boto3_raw_data["ociDnsForwardingConfigs"]
        )

    createdAt = field("createdAt")
    percentProgress = field("percentProgress")

    @cached_property
    def managedServices(self):  # pragma: no cover
        return ManagedServices.make_one(self.boto3_raw_data["managedServices"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OdbNetworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OdbNetworkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudVmClustersOutput:
    boto3_raw_data: "type_defs.ListCloudVmClustersOutputTypeDef" = dataclasses.field()

    @cached_property
    def cloudVmClusters(self):  # pragma: no cover
        return CloudVmClusterSummary.make_many(self.boto3_raw_data["cloudVmClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCloudVmClustersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudVmClustersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudVmClusterOutput:
    boto3_raw_data: "type_defs.GetCloudVmClusterOutputTypeDef" = dataclasses.field()

    @cached_property
    def cloudVmCluster(self):  # pragma: no cover
        return CloudVmCluster.make_one(self.boto3_raw_data["cloudVmCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCloudVmClusterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudVmClusterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudAutonomousVmClustersOutput:
    boto3_raw_data: "type_defs.ListCloudAutonomousVmClustersOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cloudAutonomousVmClusters(self):  # pragma: no cover
        return CloudAutonomousVmClusterSummary.make_many(
            self.boto3_raw_data["cloudAutonomousVmClusters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudAutonomousVmClustersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudAutonomousVmClustersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudAutonomousVmClusterOutput:
    boto3_raw_data: "type_defs.GetCloudAutonomousVmClusterOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cloudAutonomousVmCluster(self):  # pragma: no cover
        return CloudAutonomousVmCluster.make_one(
            self.boto3_raw_data["cloudAutonomousVmCluster"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudAutonomousVmClusterOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudAutonomousVmClusterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudExadataInfrastructuresOutput:
    boto3_raw_data: "type_defs.ListCloudExadataInfrastructuresOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cloudExadataInfrastructures(self):  # pragma: no cover
        return CloudExadataInfrastructureSummary.make_many(
            self.boto3_raw_data["cloudExadataInfrastructures"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudExadataInfrastructuresOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudExadataInfrastructuresOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudExadataInfrastructureOutput:
    boto3_raw_data: "type_defs.GetCloudExadataInfrastructureOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cloudExadataInfrastructure(self):  # pragma: no cover
        return CloudExadataInfrastructure.make_one(
            self.boto3_raw_data["cloudExadataInfrastructure"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudExadataInfrastructureOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudExadataInfrastructureOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudAutonomousVmClusterInput:
    boto3_raw_data: "type_defs.CreateCloudAutonomousVmClusterInputTypeDef" = (
        dataclasses.field()
    )

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    odbNetworkId = field("odbNetworkId")
    displayName = field("displayName")
    autonomousDataStorageSizeInTBs = field("autonomousDataStorageSizeInTBs")
    cpuCoreCountPerNode = field("cpuCoreCountPerNode")
    memoryPerOracleComputeUnitInGBs = field("memoryPerOracleComputeUnitInGBs")
    totalContainerDatabases = field("totalContainerDatabases")
    clientToken = field("clientToken")
    dbServers = field("dbServers")
    description = field("description")
    isMtlsEnabledVmCluster = field("isMtlsEnabledVmCluster")
    licenseModel = field("licenseModel")
    maintenanceWindow = field("maintenanceWindow")
    scanListenerPortNonTls = field("scanListenerPortNonTls")
    scanListenerPortTls = field("scanListenerPortTls")
    tags = field("tags")
    timeZone = field("timeZone")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCloudAutonomousVmClusterInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudAutonomousVmClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudExadataInfrastructureInput:
    boto3_raw_data: "type_defs.CreateCloudExadataInfrastructureInputTypeDef" = (
        dataclasses.field()
    )

    displayName = field("displayName")
    shape = field("shape")
    computeCount = field("computeCount")
    storageCount = field("storageCount")
    availabilityZone = field("availabilityZone")
    availabilityZoneId = field("availabilityZoneId")
    tags = field("tags")

    @cached_property
    def customerContactsToSendToOCI(self):  # pragma: no cover
        return CustomerContact.make_many(
            self.boto3_raw_data["customerContactsToSendToOCI"]
        )

    maintenanceWindow = field("maintenanceWindow")
    clientToken = field("clientToken")
    databaseServerType = field("databaseServerType")
    storageServerType = field("storageServerType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCloudExadataInfrastructureInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudExadataInfrastructureInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCloudExadataInfrastructureInput:
    boto3_raw_data: "type_defs.UpdateCloudExadataInfrastructureInputTypeDef" = (
        dataclasses.field()
    )

    cloudExadataInfrastructureId = field("cloudExadataInfrastructureId")
    maintenanceWindow = field("maintenanceWindow")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCloudExadataInfrastructureInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCloudExadataInfrastructureInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOdbNetworksOutput:
    boto3_raw_data: "type_defs.ListOdbNetworksOutputTypeDef" = dataclasses.field()

    @cached_property
    def odbNetworks(self):  # pragma: no cover
        return OdbNetworkSummary.make_many(self.boto3_raw_data["odbNetworks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOdbNetworksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOdbNetworksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOdbNetworkOutput:
    boto3_raw_data: "type_defs.GetOdbNetworkOutputTypeDef" = dataclasses.field()

    @cached_property
    def odbNetwork(self):  # pragma: no cover
        return OdbNetwork.make_one(self.boto3_raw_data["odbNetwork"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOdbNetworkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOdbNetworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
