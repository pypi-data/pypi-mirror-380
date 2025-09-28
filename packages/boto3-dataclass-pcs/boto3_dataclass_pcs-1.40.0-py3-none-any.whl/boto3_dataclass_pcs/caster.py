# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pcs import type_defs as bs_td


class PCSCaster:

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResponseTypeDef",
    ) -> "dc_td.CreateClusterResponse":
        return dc_td.CreateClusterResponse.make_one(res)

    def create_compute_node_group(
        self,
        res: "bs_td.CreateComputeNodeGroupResponseTypeDef",
    ) -> "dc_td.CreateComputeNodeGroupResponse":
        return dc_td.CreateComputeNodeGroupResponse.make_one(res)

    def create_queue(
        self,
        res: "bs_td.CreateQueueResponseTypeDef",
    ) -> "dc_td.CreateQueueResponse":
        return dc_td.CreateQueueResponse.make_one(res)

    def get_cluster(
        self,
        res: "bs_td.GetClusterResponseTypeDef",
    ) -> "dc_td.GetClusterResponse":
        return dc_td.GetClusterResponse.make_one(res)

    def get_compute_node_group(
        self,
        res: "bs_td.GetComputeNodeGroupResponseTypeDef",
    ) -> "dc_td.GetComputeNodeGroupResponse":
        return dc_td.GetComputeNodeGroupResponse.make_one(res)

    def get_queue(
        self,
        res: "bs_td.GetQueueResponseTypeDef",
    ) -> "dc_td.GetQueueResponse":
        return dc_td.GetQueueResponse.make_one(res)

    def list_clusters(
        self,
        res: "bs_td.ListClustersResponseTypeDef",
    ) -> "dc_td.ListClustersResponse":
        return dc_td.ListClustersResponse.make_one(res)

    def list_compute_node_groups(
        self,
        res: "bs_td.ListComputeNodeGroupsResponseTypeDef",
    ) -> "dc_td.ListComputeNodeGroupsResponse":
        return dc_td.ListComputeNodeGroupsResponse.make_one(res)

    def list_queues(
        self,
        res: "bs_td.ListQueuesResponseTypeDef",
    ) -> "dc_td.ListQueuesResponse":
        return dc_td.ListQueuesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def register_compute_node_group_instance(
        self,
        res: "bs_td.RegisterComputeNodeGroupInstanceResponseTypeDef",
    ) -> "dc_td.RegisterComputeNodeGroupInstanceResponse":
        return dc_td.RegisterComputeNodeGroupInstanceResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_compute_node_group(
        self,
        res: "bs_td.UpdateComputeNodeGroupResponseTypeDef",
    ) -> "dc_td.UpdateComputeNodeGroupResponse":
        return dc_td.UpdateComputeNodeGroupResponse.make_one(res)

    def update_queue(
        self,
        res: "bs_td.UpdateQueueResponseTypeDef",
    ) -> "dc_td.UpdateQueueResponse":
        return dc_td.UpdateQueueResponse.make_one(res)


pcs_caster = PCSCaster()
