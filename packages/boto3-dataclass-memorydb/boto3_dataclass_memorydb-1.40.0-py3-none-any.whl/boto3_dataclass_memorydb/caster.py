# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_memorydb import type_defs as bs_td


class MEMORYDBCaster:

    def batch_update_cluster(
        self,
        res: "bs_td.BatchUpdateClusterResponseTypeDef",
    ) -> "dc_td.BatchUpdateClusterResponse":
        return dc_td.BatchUpdateClusterResponse.make_one(res)

    def copy_snapshot(
        self,
        res: "bs_td.CopySnapshotResponseTypeDef",
    ) -> "dc_td.CopySnapshotResponse":
        return dc_td.CopySnapshotResponse.make_one(res)

    def create_acl(
        self,
        res: "bs_td.CreateACLResponseTypeDef",
    ) -> "dc_td.CreateACLResponse":
        return dc_td.CreateACLResponse.make_one(res)

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResponseTypeDef",
    ) -> "dc_td.CreateClusterResponse":
        return dc_td.CreateClusterResponse.make_one(res)

    def create_multi_region_cluster(
        self,
        res: "bs_td.CreateMultiRegionClusterResponseTypeDef",
    ) -> "dc_td.CreateMultiRegionClusterResponse":
        return dc_td.CreateMultiRegionClusterResponse.make_one(res)

    def create_parameter_group(
        self,
        res: "bs_td.CreateParameterGroupResponseTypeDef",
    ) -> "dc_td.CreateParameterGroupResponse":
        return dc_td.CreateParameterGroupResponse.make_one(res)

    def create_snapshot(
        self,
        res: "bs_td.CreateSnapshotResponseTypeDef",
    ) -> "dc_td.CreateSnapshotResponse":
        return dc_td.CreateSnapshotResponse.make_one(res)

    def create_subnet_group(
        self,
        res: "bs_td.CreateSubnetGroupResponseTypeDef",
    ) -> "dc_td.CreateSubnetGroupResponse":
        return dc_td.CreateSubnetGroupResponse.make_one(res)

    def create_user(
        self,
        res: "bs_td.CreateUserResponseTypeDef",
    ) -> "dc_td.CreateUserResponse":
        return dc_td.CreateUserResponse.make_one(res)

    def delete_acl(
        self,
        res: "bs_td.DeleteACLResponseTypeDef",
    ) -> "dc_td.DeleteACLResponse":
        return dc_td.DeleteACLResponse.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterResponseTypeDef",
    ) -> "dc_td.DeleteClusterResponse":
        return dc_td.DeleteClusterResponse.make_one(res)

    def delete_multi_region_cluster(
        self,
        res: "bs_td.DeleteMultiRegionClusterResponseTypeDef",
    ) -> "dc_td.DeleteMultiRegionClusterResponse":
        return dc_td.DeleteMultiRegionClusterResponse.make_one(res)

    def delete_parameter_group(
        self,
        res: "bs_td.DeleteParameterGroupResponseTypeDef",
    ) -> "dc_td.DeleteParameterGroupResponse":
        return dc_td.DeleteParameterGroupResponse.make_one(res)

    def delete_snapshot(
        self,
        res: "bs_td.DeleteSnapshotResponseTypeDef",
    ) -> "dc_td.DeleteSnapshotResponse":
        return dc_td.DeleteSnapshotResponse.make_one(res)

    def delete_subnet_group(
        self,
        res: "bs_td.DeleteSubnetGroupResponseTypeDef",
    ) -> "dc_td.DeleteSubnetGroupResponse":
        return dc_td.DeleteSubnetGroupResponse.make_one(res)

    def delete_user(
        self,
        res: "bs_td.DeleteUserResponseTypeDef",
    ) -> "dc_td.DeleteUserResponse":
        return dc_td.DeleteUserResponse.make_one(res)

    def describe_acls(
        self,
        res: "bs_td.DescribeACLsResponseTypeDef",
    ) -> "dc_td.DescribeACLsResponse":
        return dc_td.DescribeACLsResponse.make_one(res)

    def describe_clusters(
        self,
        res: "bs_td.DescribeClustersResponseTypeDef",
    ) -> "dc_td.DescribeClustersResponse":
        return dc_td.DescribeClustersResponse.make_one(res)

    def describe_engine_versions(
        self,
        res: "bs_td.DescribeEngineVersionsResponseTypeDef",
    ) -> "dc_td.DescribeEngineVersionsResponse":
        return dc_td.DescribeEngineVersionsResponse.make_one(res)

    def describe_events(
        self,
        res: "bs_td.DescribeEventsResponseTypeDef",
    ) -> "dc_td.DescribeEventsResponse":
        return dc_td.DescribeEventsResponse.make_one(res)

    def describe_multi_region_clusters(
        self,
        res: "bs_td.DescribeMultiRegionClustersResponseTypeDef",
    ) -> "dc_td.DescribeMultiRegionClustersResponse":
        return dc_td.DescribeMultiRegionClustersResponse.make_one(res)

    def describe_parameter_groups(
        self,
        res: "bs_td.DescribeParameterGroupsResponseTypeDef",
    ) -> "dc_td.DescribeParameterGroupsResponse":
        return dc_td.DescribeParameterGroupsResponse.make_one(res)

    def describe_parameters(
        self,
        res: "bs_td.DescribeParametersResponseTypeDef",
    ) -> "dc_td.DescribeParametersResponse":
        return dc_td.DescribeParametersResponse.make_one(res)

    def describe_reserved_nodes(
        self,
        res: "bs_td.DescribeReservedNodesResponseTypeDef",
    ) -> "dc_td.DescribeReservedNodesResponse":
        return dc_td.DescribeReservedNodesResponse.make_one(res)

    def describe_reserved_nodes_offerings(
        self,
        res: "bs_td.DescribeReservedNodesOfferingsResponseTypeDef",
    ) -> "dc_td.DescribeReservedNodesOfferingsResponse":
        return dc_td.DescribeReservedNodesOfferingsResponse.make_one(res)

    def describe_service_updates(
        self,
        res: "bs_td.DescribeServiceUpdatesResponseTypeDef",
    ) -> "dc_td.DescribeServiceUpdatesResponse":
        return dc_td.DescribeServiceUpdatesResponse.make_one(res)

    def describe_snapshots(
        self,
        res: "bs_td.DescribeSnapshotsResponseTypeDef",
    ) -> "dc_td.DescribeSnapshotsResponse":
        return dc_td.DescribeSnapshotsResponse.make_one(res)

    def describe_subnet_groups(
        self,
        res: "bs_td.DescribeSubnetGroupsResponseTypeDef",
    ) -> "dc_td.DescribeSubnetGroupsResponse":
        return dc_td.DescribeSubnetGroupsResponse.make_one(res)

    def describe_users(
        self,
        res: "bs_td.DescribeUsersResponseTypeDef",
    ) -> "dc_td.DescribeUsersResponse":
        return dc_td.DescribeUsersResponse.make_one(res)

    def failover_shard(
        self,
        res: "bs_td.FailoverShardResponseTypeDef",
    ) -> "dc_td.FailoverShardResponse":
        return dc_td.FailoverShardResponse.make_one(res)

    def list_allowed_multi_region_cluster_updates(
        self,
        res: "bs_td.ListAllowedMultiRegionClusterUpdatesResponseTypeDef",
    ) -> "dc_td.ListAllowedMultiRegionClusterUpdatesResponse":
        return dc_td.ListAllowedMultiRegionClusterUpdatesResponse.make_one(res)

    def list_allowed_node_type_updates(
        self,
        res: "bs_td.ListAllowedNodeTypeUpdatesResponseTypeDef",
    ) -> "dc_td.ListAllowedNodeTypeUpdatesResponse":
        return dc_td.ListAllowedNodeTypeUpdatesResponse.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsResponseTypeDef",
    ) -> "dc_td.ListTagsResponse":
        return dc_td.ListTagsResponse.make_one(res)

    def purchase_reserved_nodes_offering(
        self,
        res: "bs_td.PurchaseReservedNodesOfferingResponseTypeDef",
    ) -> "dc_td.PurchaseReservedNodesOfferingResponse":
        return dc_td.PurchaseReservedNodesOfferingResponse.make_one(res)

    def reset_parameter_group(
        self,
        res: "bs_td.ResetParameterGroupResponseTypeDef",
    ) -> "dc_td.ResetParameterGroupResponse":
        return dc_td.ResetParameterGroupResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.TagResourceResponseTypeDef",
    ) -> "dc_td.TagResourceResponse":
        return dc_td.TagResourceResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.UntagResourceResponseTypeDef",
    ) -> "dc_td.UntagResourceResponse":
        return dc_td.UntagResourceResponse.make_one(res)

    def update_acl(
        self,
        res: "bs_td.UpdateACLResponseTypeDef",
    ) -> "dc_td.UpdateACLResponse":
        return dc_td.UpdateACLResponse.make_one(res)

    def update_cluster(
        self,
        res: "bs_td.UpdateClusterResponseTypeDef",
    ) -> "dc_td.UpdateClusterResponse":
        return dc_td.UpdateClusterResponse.make_one(res)

    def update_multi_region_cluster(
        self,
        res: "bs_td.UpdateMultiRegionClusterResponseTypeDef",
    ) -> "dc_td.UpdateMultiRegionClusterResponse":
        return dc_td.UpdateMultiRegionClusterResponse.make_one(res)

    def update_parameter_group(
        self,
        res: "bs_td.UpdateParameterGroupResponseTypeDef",
    ) -> "dc_td.UpdateParameterGroupResponse":
        return dc_td.UpdateParameterGroupResponse.make_one(res)

    def update_subnet_group(
        self,
        res: "bs_td.UpdateSubnetGroupResponseTypeDef",
    ) -> "dc_td.UpdateSubnetGroupResponse":
        return dc_td.UpdateSubnetGroupResponse.make_one(res)

    def update_user(
        self,
        res: "bs_td.UpdateUserResponseTypeDef",
    ) -> "dc_td.UpdateUserResponse":
        return dc_td.UpdateUserResponse.make_one(res)


memorydb_caster = MEMORYDBCaster()
