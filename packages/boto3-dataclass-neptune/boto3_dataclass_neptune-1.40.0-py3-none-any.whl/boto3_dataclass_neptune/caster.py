# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_neptune import type_defs as bs_td


class NEPTUNECaster:

    def add_role_to_db_cluster(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def add_source_identifier_to_subscription(
        self,
        res: "bs_td.AddSourceIdentifierToSubscriptionResultTypeDef",
    ) -> "dc_td.AddSourceIdentifierToSubscriptionResult":
        return dc_td.AddSourceIdentifierToSubscriptionResult.make_one(res)

    def add_tags_to_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def apply_pending_maintenance_action(
        self,
        res: "bs_td.ApplyPendingMaintenanceActionResultTypeDef",
    ) -> "dc_td.ApplyPendingMaintenanceActionResult":
        return dc_td.ApplyPendingMaintenanceActionResult.make_one(res)

    def copy_db_cluster_parameter_group(
        self,
        res: "bs_td.CopyDBClusterParameterGroupResultTypeDef",
    ) -> "dc_td.CopyDBClusterParameterGroupResult":
        return dc_td.CopyDBClusterParameterGroupResult.make_one(res)

    def copy_db_cluster_snapshot(
        self,
        res: "bs_td.CopyDBClusterSnapshotResultTypeDef",
    ) -> "dc_td.CopyDBClusterSnapshotResult":
        return dc_td.CopyDBClusterSnapshotResult.make_one(res)

    def copy_db_parameter_group(
        self,
        res: "bs_td.CopyDBParameterGroupResultTypeDef",
    ) -> "dc_td.CopyDBParameterGroupResult":
        return dc_td.CopyDBParameterGroupResult.make_one(res)

    def create_db_cluster(
        self,
        res: "bs_td.CreateDBClusterResultTypeDef",
    ) -> "dc_td.CreateDBClusterResult":
        return dc_td.CreateDBClusterResult.make_one(res)

    def create_db_cluster_endpoint(
        self,
        res: "bs_td.CreateDBClusterEndpointOutputTypeDef",
    ) -> "dc_td.CreateDBClusterEndpointOutput":
        return dc_td.CreateDBClusterEndpointOutput.make_one(res)

    def create_db_cluster_parameter_group(
        self,
        res: "bs_td.CreateDBClusterParameterGroupResultTypeDef",
    ) -> "dc_td.CreateDBClusterParameterGroupResult":
        return dc_td.CreateDBClusterParameterGroupResult.make_one(res)

    def create_db_cluster_snapshot(
        self,
        res: "bs_td.CreateDBClusterSnapshotResultTypeDef",
    ) -> "dc_td.CreateDBClusterSnapshotResult":
        return dc_td.CreateDBClusterSnapshotResult.make_one(res)

    def create_db_instance(
        self,
        res: "bs_td.CreateDBInstanceResultTypeDef",
    ) -> "dc_td.CreateDBInstanceResult":
        return dc_td.CreateDBInstanceResult.make_one(res)

    def create_db_parameter_group(
        self,
        res: "bs_td.CreateDBParameterGroupResultTypeDef",
    ) -> "dc_td.CreateDBParameterGroupResult":
        return dc_td.CreateDBParameterGroupResult.make_one(res)

    def create_db_subnet_group(
        self,
        res: "bs_td.CreateDBSubnetGroupResultTypeDef",
    ) -> "dc_td.CreateDBSubnetGroupResult":
        return dc_td.CreateDBSubnetGroupResult.make_one(res)

    def create_event_subscription(
        self,
        res: "bs_td.CreateEventSubscriptionResultTypeDef",
    ) -> "dc_td.CreateEventSubscriptionResult":
        return dc_td.CreateEventSubscriptionResult.make_one(res)

    def create_global_cluster(
        self,
        res: "bs_td.CreateGlobalClusterResultTypeDef",
    ) -> "dc_td.CreateGlobalClusterResult":
        return dc_td.CreateGlobalClusterResult.make_one(res)

    def delete_db_cluster(
        self,
        res: "bs_td.DeleteDBClusterResultTypeDef",
    ) -> "dc_td.DeleteDBClusterResult":
        return dc_td.DeleteDBClusterResult.make_one(res)

    def delete_db_cluster_endpoint(
        self,
        res: "bs_td.DeleteDBClusterEndpointOutputTypeDef",
    ) -> "dc_td.DeleteDBClusterEndpointOutput":
        return dc_td.DeleteDBClusterEndpointOutput.make_one(res)

    def delete_db_cluster_parameter_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_db_cluster_snapshot(
        self,
        res: "bs_td.DeleteDBClusterSnapshotResultTypeDef",
    ) -> "dc_td.DeleteDBClusterSnapshotResult":
        return dc_td.DeleteDBClusterSnapshotResult.make_one(res)

    def delete_db_instance(
        self,
        res: "bs_td.DeleteDBInstanceResultTypeDef",
    ) -> "dc_td.DeleteDBInstanceResult":
        return dc_td.DeleteDBInstanceResult.make_one(res)

    def delete_db_parameter_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_db_subnet_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_event_subscription(
        self,
        res: "bs_td.DeleteEventSubscriptionResultTypeDef",
    ) -> "dc_td.DeleteEventSubscriptionResult":
        return dc_td.DeleteEventSubscriptionResult.make_one(res)

    def delete_global_cluster(
        self,
        res: "bs_td.DeleteGlobalClusterResultTypeDef",
    ) -> "dc_td.DeleteGlobalClusterResult":
        return dc_td.DeleteGlobalClusterResult.make_one(res)

    def describe_db_cluster_endpoints(
        self,
        res: "bs_td.DBClusterEndpointMessageTypeDef",
    ) -> "dc_td.DBClusterEndpointMessage":
        return dc_td.DBClusterEndpointMessage.make_one(res)

    def describe_db_cluster_parameter_groups(
        self,
        res: "bs_td.DBClusterParameterGroupsMessageTypeDef",
    ) -> "dc_td.DBClusterParameterGroupsMessage":
        return dc_td.DBClusterParameterGroupsMessage.make_one(res)

    def describe_db_cluster_parameters(
        self,
        res: "bs_td.DBClusterParameterGroupDetailsTypeDef",
    ) -> "dc_td.DBClusterParameterGroupDetails":
        return dc_td.DBClusterParameterGroupDetails.make_one(res)

    def describe_db_cluster_snapshot_attributes(
        self,
        res: "bs_td.DescribeDBClusterSnapshotAttributesResultTypeDef",
    ) -> "dc_td.DescribeDBClusterSnapshotAttributesResult":
        return dc_td.DescribeDBClusterSnapshotAttributesResult.make_one(res)

    def describe_db_cluster_snapshots(
        self,
        res: "bs_td.DBClusterSnapshotMessageTypeDef",
    ) -> "dc_td.DBClusterSnapshotMessage":
        return dc_td.DBClusterSnapshotMessage.make_one(res)

    def describe_db_clusters(
        self,
        res: "bs_td.DBClusterMessageTypeDef",
    ) -> "dc_td.DBClusterMessage":
        return dc_td.DBClusterMessage.make_one(res)

    def describe_db_engine_versions(
        self,
        res: "bs_td.DBEngineVersionMessageTypeDef",
    ) -> "dc_td.DBEngineVersionMessage":
        return dc_td.DBEngineVersionMessage.make_one(res)

    def describe_db_instances(
        self,
        res: "bs_td.DBInstanceMessageTypeDef",
    ) -> "dc_td.DBInstanceMessage":
        return dc_td.DBInstanceMessage.make_one(res)

    def describe_db_parameter_groups(
        self,
        res: "bs_td.DBParameterGroupsMessageTypeDef",
    ) -> "dc_td.DBParameterGroupsMessage":
        return dc_td.DBParameterGroupsMessage.make_one(res)

    def describe_db_parameters(
        self,
        res: "bs_td.DBParameterGroupDetailsTypeDef",
    ) -> "dc_td.DBParameterGroupDetails":
        return dc_td.DBParameterGroupDetails.make_one(res)

    def describe_db_subnet_groups(
        self,
        res: "bs_td.DBSubnetGroupMessageTypeDef",
    ) -> "dc_td.DBSubnetGroupMessage":
        return dc_td.DBSubnetGroupMessage.make_one(res)

    def describe_engine_default_cluster_parameters(
        self,
        res: "bs_td.DescribeEngineDefaultClusterParametersResultTypeDef",
    ) -> "dc_td.DescribeEngineDefaultClusterParametersResult":
        return dc_td.DescribeEngineDefaultClusterParametersResult.make_one(res)

    def describe_engine_default_parameters(
        self,
        res: "bs_td.DescribeEngineDefaultParametersResultTypeDef",
    ) -> "dc_td.DescribeEngineDefaultParametersResult":
        return dc_td.DescribeEngineDefaultParametersResult.make_one(res)

    def describe_event_categories(
        self,
        res: "bs_td.EventCategoriesMessageTypeDef",
    ) -> "dc_td.EventCategoriesMessage":
        return dc_td.EventCategoriesMessage.make_one(res)

    def describe_event_subscriptions(
        self,
        res: "bs_td.EventSubscriptionsMessageTypeDef",
    ) -> "dc_td.EventSubscriptionsMessage":
        return dc_td.EventSubscriptionsMessage.make_one(res)

    def describe_events(
        self,
        res: "bs_td.EventsMessageTypeDef",
    ) -> "dc_td.EventsMessage":
        return dc_td.EventsMessage.make_one(res)

    def describe_global_clusters(
        self,
        res: "bs_td.GlobalClustersMessageTypeDef",
    ) -> "dc_td.GlobalClustersMessage":
        return dc_td.GlobalClustersMessage.make_one(res)

    def describe_orderable_db_instance_options(
        self,
        res: "bs_td.OrderableDBInstanceOptionsMessageTypeDef",
    ) -> "dc_td.OrderableDBInstanceOptionsMessage":
        return dc_td.OrderableDBInstanceOptionsMessage.make_one(res)

    def describe_pending_maintenance_actions(
        self,
        res: "bs_td.PendingMaintenanceActionsMessageTypeDef",
    ) -> "dc_td.PendingMaintenanceActionsMessage":
        return dc_td.PendingMaintenanceActionsMessage.make_one(res)

    def describe_valid_db_instance_modifications(
        self,
        res: "bs_td.DescribeValidDBInstanceModificationsResultTypeDef",
    ) -> "dc_td.DescribeValidDBInstanceModificationsResult":
        return dc_td.DescribeValidDBInstanceModificationsResult.make_one(res)

    def failover_db_cluster(
        self,
        res: "bs_td.FailoverDBClusterResultTypeDef",
    ) -> "dc_td.FailoverDBClusterResult":
        return dc_td.FailoverDBClusterResult.make_one(res)

    def failover_global_cluster(
        self,
        res: "bs_td.FailoverGlobalClusterResultTypeDef",
    ) -> "dc_td.FailoverGlobalClusterResult":
        return dc_td.FailoverGlobalClusterResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.TagListMessageTypeDef",
    ) -> "dc_td.TagListMessage":
        return dc_td.TagListMessage.make_one(res)

    def modify_db_cluster(
        self,
        res: "bs_td.ModifyDBClusterResultTypeDef",
    ) -> "dc_td.ModifyDBClusterResult":
        return dc_td.ModifyDBClusterResult.make_one(res)

    def modify_db_cluster_endpoint(
        self,
        res: "bs_td.ModifyDBClusterEndpointOutputTypeDef",
    ) -> "dc_td.ModifyDBClusterEndpointOutput":
        return dc_td.ModifyDBClusterEndpointOutput.make_one(res)

    def modify_db_cluster_parameter_group(
        self,
        res: "bs_td.DBClusterParameterGroupNameMessageTypeDef",
    ) -> "dc_td.DBClusterParameterGroupNameMessage":
        return dc_td.DBClusterParameterGroupNameMessage.make_one(res)

    def modify_db_cluster_snapshot_attribute(
        self,
        res: "bs_td.ModifyDBClusterSnapshotAttributeResultTypeDef",
    ) -> "dc_td.ModifyDBClusterSnapshotAttributeResult":
        return dc_td.ModifyDBClusterSnapshotAttributeResult.make_one(res)

    def modify_db_instance(
        self,
        res: "bs_td.ModifyDBInstanceResultTypeDef",
    ) -> "dc_td.ModifyDBInstanceResult":
        return dc_td.ModifyDBInstanceResult.make_one(res)

    def modify_db_parameter_group(
        self,
        res: "bs_td.DBParameterGroupNameMessageTypeDef",
    ) -> "dc_td.DBParameterGroupNameMessage":
        return dc_td.DBParameterGroupNameMessage.make_one(res)

    def modify_db_subnet_group(
        self,
        res: "bs_td.ModifyDBSubnetGroupResultTypeDef",
    ) -> "dc_td.ModifyDBSubnetGroupResult":
        return dc_td.ModifyDBSubnetGroupResult.make_one(res)

    def modify_event_subscription(
        self,
        res: "bs_td.ModifyEventSubscriptionResultTypeDef",
    ) -> "dc_td.ModifyEventSubscriptionResult":
        return dc_td.ModifyEventSubscriptionResult.make_one(res)

    def modify_global_cluster(
        self,
        res: "bs_td.ModifyGlobalClusterResultTypeDef",
    ) -> "dc_td.ModifyGlobalClusterResult":
        return dc_td.ModifyGlobalClusterResult.make_one(res)

    def promote_read_replica_db_cluster(
        self,
        res: "bs_td.PromoteReadReplicaDBClusterResultTypeDef",
    ) -> "dc_td.PromoteReadReplicaDBClusterResult":
        return dc_td.PromoteReadReplicaDBClusterResult.make_one(res)

    def reboot_db_instance(
        self,
        res: "bs_td.RebootDBInstanceResultTypeDef",
    ) -> "dc_td.RebootDBInstanceResult":
        return dc_td.RebootDBInstanceResult.make_one(res)

    def remove_from_global_cluster(
        self,
        res: "bs_td.RemoveFromGlobalClusterResultTypeDef",
    ) -> "dc_td.RemoveFromGlobalClusterResult":
        return dc_td.RemoveFromGlobalClusterResult.make_one(res)

    def remove_role_from_db_cluster(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_source_identifier_from_subscription(
        self,
        res: "bs_td.RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    ) -> "dc_td.RemoveSourceIdentifierFromSubscriptionResult":
        return dc_td.RemoveSourceIdentifierFromSubscriptionResult.make_one(res)

    def remove_tags_from_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def reset_db_cluster_parameter_group(
        self,
        res: "bs_td.DBClusterParameterGroupNameMessageTypeDef",
    ) -> "dc_td.DBClusterParameterGroupNameMessage":
        return dc_td.DBClusterParameterGroupNameMessage.make_one(res)

    def reset_db_parameter_group(
        self,
        res: "bs_td.DBParameterGroupNameMessageTypeDef",
    ) -> "dc_td.DBParameterGroupNameMessage":
        return dc_td.DBParameterGroupNameMessage.make_one(res)

    def restore_db_cluster_from_snapshot(
        self,
        res: "bs_td.RestoreDBClusterFromSnapshotResultTypeDef",
    ) -> "dc_td.RestoreDBClusterFromSnapshotResult":
        return dc_td.RestoreDBClusterFromSnapshotResult.make_one(res)

    def restore_db_cluster_to_point_in_time(
        self,
        res: "bs_td.RestoreDBClusterToPointInTimeResultTypeDef",
    ) -> "dc_td.RestoreDBClusterToPointInTimeResult":
        return dc_td.RestoreDBClusterToPointInTimeResult.make_one(res)

    def start_db_cluster(
        self,
        res: "bs_td.StartDBClusterResultTypeDef",
    ) -> "dc_td.StartDBClusterResult":
        return dc_td.StartDBClusterResult.make_one(res)

    def stop_db_cluster(
        self,
        res: "bs_td.StopDBClusterResultTypeDef",
    ) -> "dc_td.StopDBClusterResult":
        return dc_td.StopDBClusterResult.make_one(res)

    def switchover_global_cluster(
        self,
        res: "bs_td.SwitchoverGlobalClusterResultTypeDef",
    ) -> "dc_td.SwitchoverGlobalClusterResult":
        return dc_td.SwitchoverGlobalClusterResult.make_one(res)


neptune_caster = NEPTUNECaster()
