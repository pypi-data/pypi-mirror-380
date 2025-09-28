# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pcs import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountingRequest:
    boto3_raw_data: "type_defs.AccountingRequestTypeDef" = dataclasses.field()

    mode = field("mode")
    defaultPurgeTimeInDays = field("defaultPurgeTimeInDays")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountingRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Accounting:
    boto3_raw_data: "type_defs.AccountingTypeDef" = dataclasses.field()

    mode = field("mode")
    defaultPurgeTimeInDays = field("defaultPurgeTimeInDays")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlurmCustomSetting:
    boto3_raw_data: "type_defs.SlurmCustomSettingTypeDef" = dataclasses.field()

    parameterName = field("parameterName")
    parameterValue = field("parameterValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlurmCustomSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlurmCustomSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlurmAuthKey:
    boto3_raw_data: "type_defs.SlurmAuthKeyTypeDef" = dataclasses.field()

    secretArn = field("secretArn")
    secretVersion = field("secretVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlurmAuthKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlurmAuthKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterSummary:
    boto3_raw_data: "type_defs.ClusterSummaryTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    arn = field("arn")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Endpoint:
    boto3_raw_data: "type_defs.EndpointTypeDef" = dataclasses.field()

    type = field("type")
    privateIpAddress = field("privateIpAddress")
    port = field("port")
    publicIpAddress = field("publicIpAddress")
    ipv6Address = field("ipv6Address")

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
class ErrorInfo:
    boto3_raw_data: "type_defs.ErrorInfoTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Networking:
    boto3_raw_data: "type_defs.NetworkingTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")
    networkType = field("networkType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scheduler:
    boto3_raw_data: "type_defs.SchedulerTypeDef" = dataclasses.field()

    type = field("type")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchedulerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchedulerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeNodeGroupConfiguration:
    boto3_raw_data: "type_defs.ComputeNodeGroupConfigurationTypeDef" = (
        dataclasses.field()
    )

    computeNodeGroupId = field("computeNodeGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComputeNodeGroupConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeNodeGroupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeNodeGroupSummary:
    boto3_raw_data: "type_defs.ComputeNodeGroupSummaryTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    arn = field("arn")
    clusterId = field("clusterId")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeNodeGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeNodeGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLaunchTemplate:
    boto3_raw_data: "type_defs.CustomLaunchTemplateTypeDef" = dataclasses.field()

    id = field("id")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomLaunchTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLaunchTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceConfig:
    boto3_raw_data: "type_defs.InstanceConfigTypeDef" = dataclasses.field()

    instanceType = field("instanceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingConfiguration:
    boto3_raw_data: "type_defs.ScalingConfigurationTypeDef" = dataclasses.field()

    minInstanceCount = field("minInstanceCount")
    maxInstanceCount = field("maxInstanceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpotOptions:
    boto3_raw_data: "type_defs.SpotOptionsTypeDef" = dataclasses.field()

    allocationStrategy = field("allocationStrategy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpotOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SpotOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkingRequest:
    boto3_raw_data: "type_defs.NetworkingRequestTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")
    networkType = field("networkType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkingRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchedulerRequest:
    boto3_raw_data: "type_defs.SchedulerRequestTypeDef" = dataclasses.field()

    type = field("type")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchedulerRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchedulerRequestTypeDef"]
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
class ScalingConfigurationRequest:
    boto3_raw_data: "type_defs.ScalingConfigurationRequestTypeDef" = dataclasses.field()

    minInstanceCount = field("minInstanceCount")
    maxInstanceCount = field("maxInstanceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterRequest:
    boto3_raw_data: "type_defs.DeleteClusterRequestTypeDef" = dataclasses.field()

    clusterIdentifier = field("clusterIdentifier")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComputeNodeGroupRequest:
    boto3_raw_data: "type_defs.DeleteComputeNodeGroupRequestTypeDef" = (
        dataclasses.field()
    )

    clusterIdentifier = field("clusterIdentifier")
    computeNodeGroupIdentifier = field("computeNodeGroupIdentifier")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteComputeNodeGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComputeNodeGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQueueRequest:
    boto3_raw_data: "type_defs.DeleteQueueRequestTypeDef" = dataclasses.field()

    clusterIdentifier = field("clusterIdentifier")
    queueIdentifier = field("queueIdentifier")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClusterRequest:
    boto3_raw_data: "type_defs.GetClusterRequestTypeDef" = dataclasses.field()

    clusterIdentifier = field("clusterIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetClusterRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComputeNodeGroupRequest:
    boto3_raw_data: "type_defs.GetComputeNodeGroupRequestTypeDef" = dataclasses.field()

    clusterIdentifier = field("clusterIdentifier")
    computeNodeGroupIdentifier = field("computeNodeGroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComputeNodeGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComputeNodeGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueRequest:
    boto3_raw_data: "type_defs.GetQueueRequestTypeDef" = dataclasses.field()

    clusterIdentifier = field("clusterIdentifier")
    queueIdentifier = field("queueIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQueueRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetQueueRequestTypeDef"]],
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
class ListClustersRequest:
    boto3_raw_data: "type_defs.ListClustersRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputeNodeGroupsRequest:
    boto3_raw_data: "type_defs.ListComputeNodeGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    clusterIdentifier = field("clusterIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComputeNodeGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputeNodeGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesRequest:
    boto3_raw_data: "type_defs.ListQueuesRequestTypeDef" = dataclasses.field()

    clusterIdentifier = field("clusterIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListQueuesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueSummary:
    boto3_raw_data: "type_defs.QueueSummaryTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    arn = field("arn")
    clusterId = field("clusterId")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueSummaryTypeDef"]],
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
class RegisterComputeNodeGroupInstanceRequest:
    boto3_raw_data: "type_defs.RegisterComputeNodeGroupInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    clusterIdentifier = field("clusterIdentifier")
    bootstrapId = field("bootstrapId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterComputeNodeGroupInstanceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterComputeNodeGroupInstanceRequestTypeDef"]
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
class ClusterSlurmConfigurationRequest:
    boto3_raw_data: "type_defs.ClusterSlurmConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    scaleDownIdleTimeInSeconds = field("scaleDownIdleTimeInSeconds")

    @cached_property
    def slurmCustomSettings(self):  # pragma: no cover
        return SlurmCustomSetting.make_many(self.boto3_raw_data["slurmCustomSettings"])

    @cached_property
    def accounting(self):  # pragma: no cover
        return AccountingRequest.make_one(self.boto3_raw_data["accounting"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ClusterSlurmConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterSlurmConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeNodeGroupSlurmConfigurationRequest:
    boto3_raw_data: "type_defs.ComputeNodeGroupSlurmConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def slurmCustomSettings(self):  # pragma: no cover
        return SlurmCustomSetting.make_many(self.boto3_raw_data["slurmCustomSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComputeNodeGroupSlurmConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeNodeGroupSlurmConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeNodeGroupSlurmConfiguration:
    boto3_raw_data: "type_defs.ComputeNodeGroupSlurmConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def slurmCustomSettings(self):  # pragma: no cover
        return SlurmCustomSetting.make_many(self.boto3_raw_data["slurmCustomSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComputeNodeGroupSlurmConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeNodeGroupSlurmConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComputeNodeGroupSlurmConfigurationRequest:
    boto3_raw_data: (
        "type_defs.UpdateComputeNodeGroupSlurmConfigurationRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def slurmCustomSettings(self):  # pragma: no cover
        return SlurmCustomSetting.make_many(self.boto3_raw_data["slurmCustomSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateComputeNodeGroupSlurmConfigurationRequestTypeDef"
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
                "type_defs.UpdateComputeNodeGroupSlurmConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterSlurmConfiguration:
    boto3_raw_data: "type_defs.ClusterSlurmConfigurationTypeDef" = dataclasses.field()

    scaleDownIdleTimeInSeconds = field("scaleDownIdleTimeInSeconds")

    @cached_property
    def slurmCustomSettings(self):  # pragma: no cover
        return SlurmCustomSetting.make_many(self.boto3_raw_data["slurmCustomSettings"])

    @cached_property
    def authKey(self):  # pragma: no cover
        return SlurmAuthKey.make_one(self.boto3_raw_data["authKey"])

    @cached_property
    def accounting(self):  # pragma: no cover
        return Accounting.make_one(self.boto3_raw_data["accounting"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterSlurmConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterSlurmConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueRequest:
    boto3_raw_data: "type_defs.CreateQueueRequestTypeDef" = dataclasses.field()

    clusterIdentifier = field("clusterIdentifier")
    queueName = field("queueName")

    @cached_property
    def computeNodeGroupConfigurations(self):  # pragma: no cover
        return ComputeNodeGroupConfiguration.make_many(
            self.boto3_raw_data["computeNodeGroupConfigurations"]
        )

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Queue:
    boto3_raw_data: "type_defs.QueueTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    arn = field("arn")
    clusterId = field("clusterId")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    status = field("status")

    @cached_property
    def computeNodeGroupConfigurations(self):  # pragma: no cover
        return ComputeNodeGroupConfiguration.make_many(
            self.boto3_raw_data["computeNodeGroupConfigurations"]
        )

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return ErrorInfo.make_many(self.boto3_raw_data["errorInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueRequest:
    boto3_raw_data: "type_defs.UpdateQueueRequestTypeDef" = dataclasses.field()

    clusterIdentifier = field("clusterIdentifier")
    queueIdentifier = field("queueIdentifier")

    @cached_property
    def computeNodeGroupConfigurations(self):  # pragma: no cover
        return ComputeNodeGroupConfiguration.make_many(
            self.boto3_raw_data["computeNodeGroupConfigurations"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueRequestTypeDef"]
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
class ListClustersResponse:
    boto3_raw_data: "type_defs.ListClustersResponseTypeDef" = dataclasses.field()

    @cached_property
    def clusters(self):  # pragma: no cover
        return ClusterSummary.make_many(self.boto3_raw_data["clusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputeNodeGroupsResponse:
    boto3_raw_data: "type_defs.ListComputeNodeGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def computeNodeGroups(self):  # pragma: no cover
        return ComputeNodeGroupSummary.make_many(
            self.boto3_raw_data["computeNodeGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListComputeNodeGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputeNodeGroupsResponseTypeDef"]
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
class RegisterComputeNodeGroupInstanceResponse:
    boto3_raw_data: "type_defs.RegisterComputeNodeGroupInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    nodeID = field("nodeID")
    sharedSecret = field("sharedSecret")

    @cached_property
    def endpoints(self):  # pragma: no cover
        return Endpoint.make_many(self.boto3_raw_data["endpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterComputeNodeGroupInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterComputeNodeGroupInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersRequestPaginate:
    boto3_raw_data: "type_defs.ListClustersRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputeNodeGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListComputeNodeGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    clusterIdentifier = field("clusterIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComputeNodeGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputeNodeGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesRequestPaginate:
    boto3_raw_data: "type_defs.ListQueuesRequestPaginateTypeDef" = dataclasses.field()

    clusterIdentifier = field("clusterIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueuesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesResponse:
    boto3_raw_data: "type_defs.ListQueuesResponseTypeDef" = dataclasses.field()

    @cached_property
    def queues(self):  # pragma: no cover
        return QueueSummary.make_many(self.boto3_raw_data["queues"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueuesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterRequest:
    boto3_raw_data: "type_defs.CreateClusterRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")

    @cached_property
    def scheduler(self):  # pragma: no cover
        return SchedulerRequest.make_one(self.boto3_raw_data["scheduler"])

    size = field("size")

    @cached_property
    def networking(self):  # pragma: no cover
        return NetworkingRequest.make_one(self.boto3_raw_data["networking"])

    @cached_property
    def slurmConfiguration(self):  # pragma: no cover
        return ClusterSlurmConfigurationRequest.make_one(
            self.boto3_raw_data["slurmConfiguration"]
        )

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComputeNodeGroupRequest:
    boto3_raw_data: "type_defs.CreateComputeNodeGroupRequestTypeDef" = (
        dataclasses.field()
    )

    clusterIdentifier = field("clusterIdentifier")
    computeNodeGroupName = field("computeNodeGroupName")
    subnetIds = field("subnetIds")

    @cached_property
    def customLaunchTemplate(self):  # pragma: no cover
        return CustomLaunchTemplate.make_one(
            self.boto3_raw_data["customLaunchTemplate"]
        )

    iamInstanceProfileArn = field("iamInstanceProfileArn")

    @cached_property
    def scalingConfiguration(self):  # pragma: no cover
        return ScalingConfigurationRequest.make_one(
            self.boto3_raw_data["scalingConfiguration"]
        )

    @cached_property
    def instanceConfigs(self):  # pragma: no cover
        return InstanceConfig.make_many(self.boto3_raw_data["instanceConfigs"])

    amiId = field("amiId")
    purchaseOption = field("purchaseOption")

    @cached_property
    def spotOptions(self):  # pragma: no cover
        return SpotOptions.make_one(self.boto3_raw_data["spotOptions"])

    @cached_property
    def slurmConfiguration(self):  # pragma: no cover
        return ComputeNodeGroupSlurmConfigurationRequest.make_one(
            self.boto3_raw_data["slurmConfiguration"]
        )

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateComputeNodeGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComputeNodeGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeNodeGroup:
    boto3_raw_data: "type_defs.ComputeNodeGroupTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    arn = field("arn")
    clusterId = field("clusterId")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    status = field("status")
    subnetIds = field("subnetIds")

    @cached_property
    def customLaunchTemplate(self):  # pragma: no cover
        return CustomLaunchTemplate.make_one(
            self.boto3_raw_data["customLaunchTemplate"]
        )

    iamInstanceProfileArn = field("iamInstanceProfileArn")

    @cached_property
    def scalingConfiguration(self):  # pragma: no cover
        return ScalingConfiguration.make_one(
            self.boto3_raw_data["scalingConfiguration"]
        )

    @cached_property
    def instanceConfigs(self):  # pragma: no cover
        return InstanceConfig.make_many(self.boto3_raw_data["instanceConfigs"])

    amiId = field("amiId")
    purchaseOption = field("purchaseOption")

    @cached_property
    def spotOptions(self):  # pragma: no cover
        return SpotOptions.make_one(self.boto3_raw_data["spotOptions"])

    @cached_property
    def slurmConfiguration(self):  # pragma: no cover
        return ComputeNodeGroupSlurmConfiguration.make_one(
            self.boto3_raw_data["slurmConfiguration"]
        )

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return ErrorInfo.make_many(self.boto3_raw_data["errorInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputeNodeGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeNodeGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComputeNodeGroupRequest:
    boto3_raw_data: "type_defs.UpdateComputeNodeGroupRequestTypeDef" = (
        dataclasses.field()
    )

    clusterIdentifier = field("clusterIdentifier")
    computeNodeGroupIdentifier = field("computeNodeGroupIdentifier")
    amiId = field("amiId")
    subnetIds = field("subnetIds")

    @cached_property
    def customLaunchTemplate(self):  # pragma: no cover
        return CustomLaunchTemplate.make_one(
            self.boto3_raw_data["customLaunchTemplate"]
        )

    purchaseOption = field("purchaseOption")

    @cached_property
    def spotOptions(self):  # pragma: no cover
        return SpotOptions.make_one(self.boto3_raw_data["spotOptions"])

    @cached_property
    def scalingConfiguration(self):  # pragma: no cover
        return ScalingConfigurationRequest.make_one(
            self.boto3_raw_data["scalingConfiguration"]
        )

    iamInstanceProfileArn = field("iamInstanceProfileArn")

    @cached_property
    def slurmConfiguration(self):  # pragma: no cover
        return UpdateComputeNodeGroupSlurmConfigurationRequest.make_one(
            self.boto3_raw_data["slurmConfiguration"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateComputeNodeGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComputeNodeGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cluster:
    boto3_raw_data: "type_defs.ClusterTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")

    @cached_property
    def scheduler(self):  # pragma: no cover
        return Scheduler.make_one(self.boto3_raw_data["scheduler"])

    size = field("size")

    @cached_property
    def networking(self):  # pragma: no cover
        return Networking.make_one(self.boto3_raw_data["networking"])

    @cached_property
    def slurmConfiguration(self):  # pragma: no cover
        return ClusterSlurmConfiguration.make_one(
            self.boto3_raw_data["slurmConfiguration"]
        )

    @cached_property
    def endpoints(self):  # pragma: no cover
        return Endpoint.make_many(self.boto3_raw_data["endpoints"])

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return ErrorInfo.make_many(self.boto3_raw_data["errorInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueResponse:
    boto3_raw_data: "type_defs.CreateQueueResponseTypeDef" = dataclasses.field()

    @cached_property
    def queue(self):  # pragma: no cover
        return Queue.make_one(self.boto3_raw_data["queue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQueueResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueResponse:
    boto3_raw_data: "type_defs.GetQueueResponseTypeDef" = dataclasses.field()

    @cached_property
    def queue(self):  # pragma: no cover
        return Queue.make_one(self.boto3_raw_data["queue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQueueResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueResponse:
    boto3_raw_data: "type_defs.UpdateQueueResponseTypeDef" = dataclasses.field()

    @cached_property
    def queue(self):  # pragma: no cover
        return Queue.make_one(self.boto3_raw_data["queue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQueueResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComputeNodeGroupResponse:
    boto3_raw_data: "type_defs.CreateComputeNodeGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def computeNodeGroup(self):  # pragma: no cover
        return ComputeNodeGroup.make_one(self.boto3_raw_data["computeNodeGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateComputeNodeGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComputeNodeGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComputeNodeGroupResponse:
    boto3_raw_data: "type_defs.GetComputeNodeGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def computeNodeGroup(self):  # pragma: no cover
        return ComputeNodeGroup.make_one(self.boto3_raw_data["computeNodeGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComputeNodeGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComputeNodeGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComputeNodeGroupResponse:
    boto3_raw_data: "type_defs.UpdateComputeNodeGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def computeNodeGroup(self):  # pragma: no cover
        return ComputeNodeGroup.make_one(self.boto3_raw_data["computeNodeGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateComputeNodeGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComputeNodeGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterResponse:
    boto3_raw_data: "type_defs.CreateClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClusterResponse:
    boto3_raw_data: "type_defs.GetClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
