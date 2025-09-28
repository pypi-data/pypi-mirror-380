# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_odb import type_defs as bs_td


class ODBCaster:

    def create_cloud_autonomous_vm_cluster(
        self,
        res: "bs_td.CreateCloudAutonomousVmClusterOutputTypeDef",
    ) -> "dc_td.CreateCloudAutonomousVmClusterOutput":
        return dc_td.CreateCloudAutonomousVmClusterOutput.make_one(res)

    def create_cloud_exadata_infrastructure(
        self,
        res: "bs_td.CreateCloudExadataInfrastructureOutputTypeDef",
    ) -> "dc_td.CreateCloudExadataInfrastructureOutput":
        return dc_td.CreateCloudExadataInfrastructureOutput.make_one(res)

    def create_cloud_vm_cluster(
        self,
        res: "bs_td.CreateCloudVmClusterOutputTypeDef",
    ) -> "dc_td.CreateCloudVmClusterOutput":
        return dc_td.CreateCloudVmClusterOutput.make_one(res)

    def create_odb_network(
        self,
        res: "bs_td.CreateOdbNetworkOutputTypeDef",
    ) -> "dc_td.CreateOdbNetworkOutput":
        return dc_td.CreateOdbNetworkOutput.make_one(res)

    def create_odb_peering_connection(
        self,
        res: "bs_td.CreateOdbPeeringConnectionOutputTypeDef",
    ) -> "dc_td.CreateOdbPeeringConnectionOutput":
        return dc_td.CreateOdbPeeringConnectionOutput.make_one(res)

    def get_cloud_autonomous_vm_cluster(
        self,
        res: "bs_td.GetCloudAutonomousVmClusterOutputTypeDef",
    ) -> "dc_td.GetCloudAutonomousVmClusterOutput":
        return dc_td.GetCloudAutonomousVmClusterOutput.make_one(res)

    def get_cloud_exadata_infrastructure(
        self,
        res: "bs_td.GetCloudExadataInfrastructureOutputTypeDef",
    ) -> "dc_td.GetCloudExadataInfrastructureOutput":
        return dc_td.GetCloudExadataInfrastructureOutput.make_one(res)

    def get_cloud_exadata_infrastructure_unallocated_resources(
        self,
        res: "bs_td.GetCloudExadataInfrastructureUnallocatedResourcesOutputTypeDef",
    ) -> "dc_td.GetCloudExadataInfrastructureUnallocatedResourcesOutput":
        return dc_td.GetCloudExadataInfrastructureUnallocatedResourcesOutput.make_one(
            res
        )

    def get_cloud_vm_cluster(
        self,
        res: "bs_td.GetCloudVmClusterOutputTypeDef",
    ) -> "dc_td.GetCloudVmClusterOutput":
        return dc_td.GetCloudVmClusterOutput.make_one(res)

    def get_db_node(
        self,
        res: "bs_td.GetDbNodeOutputTypeDef",
    ) -> "dc_td.GetDbNodeOutput":
        return dc_td.GetDbNodeOutput.make_one(res)

    def get_db_server(
        self,
        res: "bs_td.GetDbServerOutputTypeDef",
    ) -> "dc_td.GetDbServerOutput":
        return dc_td.GetDbServerOutput.make_one(res)

    def get_oci_onboarding_status(
        self,
        res: "bs_td.GetOciOnboardingStatusOutputTypeDef",
    ) -> "dc_td.GetOciOnboardingStatusOutput":
        return dc_td.GetOciOnboardingStatusOutput.make_one(res)

    def get_odb_network(
        self,
        res: "bs_td.GetOdbNetworkOutputTypeDef",
    ) -> "dc_td.GetOdbNetworkOutput":
        return dc_td.GetOdbNetworkOutput.make_one(res)

    def get_odb_peering_connection(
        self,
        res: "bs_td.GetOdbPeeringConnectionOutputTypeDef",
    ) -> "dc_td.GetOdbPeeringConnectionOutput":
        return dc_td.GetOdbPeeringConnectionOutput.make_one(res)

    def list_autonomous_virtual_machines(
        self,
        res: "bs_td.ListAutonomousVirtualMachinesOutputTypeDef",
    ) -> "dc_td.ListAutonomousVirtualMachinesOutput":
        return dc_td.ListAutonomousVirtualMachinesOutput.make_one(res)

    def list_cloud_autonomous_vm_clusters(
        self,
        res: "bs_td.ListCloudAutonomousVmClustersOutputTypeDef",
    ) -> "dc_td.ListCloudAutonomousVmClustersOutput":
        return dc_td.ListCloudAutonomousVmClustersOutput.make_one(res)

    def list_cloud_exadata_infrastructures(
        self,
        res: "bs_td.ListCloudExadataInfrastructuresOutputTypeDef",
    ) -> "dc_td.ListCloudExadataInfrastructuresOutput":
        return dc_td.ListCloudExadataInfrastructuresOutput.make_one(res)

    def list_cloud_vm_clusters(
        self,
        res: "bs_td.ListCloudVmClustersOutputTypeDef",
    ) -> "dc_td.ListCloudVmClustersOutput":
        return dc_td.ListCloudVmClustersOutput.make_one(res)

    def list_db_nodes(
        self,
        res: "bs_td.ListDbNodesOutputTypeDef",
    ) -> "dc_td.ListDbNodesOutput":
        return dc_td.ListDbNodesOutput.make_one(res)

    def list_db_servers(
        self,
        res: "bs_td.ListDbServersOutputTypeDef",
    ) -> "dc_td.ListDbServersOutput":
        return dc_td.ListDbServersOutput.make_one(res)

    def list_db_system_shapes(
        self,
        res: "bs_td.ListDbSystemShapesOutputTypeDef",
    ) -> "dc_td.ListDbSystemShapesOutput":
        return dc_td.ListDbSystemShapesOutput.make_one(res)

    def list_gi_versions(
        self,
        res: "bs_td.ListGiVersionsOutputTypeDef",
    ) -> "dc_td.ListGiVersionsOutput":
        return dc_td.ListGiVersionsOutput.make_one(res)

    def list_odb_networks(
        self,
        res: "bs_td.ListOdbNetworksOutputTypeDef",
    ) -> "dc_td.ListOdbNetworksOutput":
        return dc_td.ListOdbNetworksOutput.make_one(res)

    def list_odb_peering_connections(
        self,
        res: "bs_td.ListOdbPeeringConnectionsOutputTypeDef",
    ) -> "dc_td.ListOdbPeeringConnectionsOutput":
        return dc_td.ListOdbPeeringConnectionsOutput.make_one(res)

    def list_system_versions(
        self,
        res: "bs_td.ListSystemVersionsOutputTypeDef",
    ) -> "dc_td.ListSystemVersionsOutput":
        return dc_td.ListSystemVersionsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def reboot_db_node(
        self,
        res: "bs_td.RebootDbNodeOutputTypeDef",
    ) -> "dc_td.RebootDbNodeOutput":
        return dc_td.RebootDbNodeOutput.make_one(res)

    def start_db_node(
        self,
        res: "bs_td.StartDbNodeOutputTypeDef",
    ) -> "dc_td.StartDbNodeOutput":
        return dc_td.StartDbNodeOutput.make_one(res)

    def stop_db_node(
        self,
        res: "bs_td.StopDbNodeOutputTypeDef",
    ) -> "dc_td.StopDbNodeOutput":
        return dc_td.StopDbNodeOutput.make_one(res)

    def update_cloud_exadata_infrastructure(
        self,
        res: "bs_td.UpdateCloudExadataInfrastructureOutputTypeDef",
    ) -> "dc_td.UpdateCloudExadataInfrastructureOutput":
        return dc_td.UpdateCloudExadataInfrastructureOutput.make_one(res)

    def update_odb_network(
        self,
        res: "bs_td.UpdateOdbNetworkOutputTypeDef",
    ) -> "dc_td.UpdateOdbNetworkOutput":
        return dc_td.UpdateOdbNetworkOutput.make_one(res)


odb_caster = ODBCaster()
