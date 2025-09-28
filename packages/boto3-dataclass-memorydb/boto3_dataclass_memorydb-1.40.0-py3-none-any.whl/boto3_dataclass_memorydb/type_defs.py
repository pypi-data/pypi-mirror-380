# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_memorydb import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ACLPendingChanges:
    boto3_raw_data: "type_defs.ACLPendingChangesTypeDef" = dataclasses.field()

    UserNamesToRemove = field("UserNamesToRemove")
    UserNamesToAdd = field("UserNamesToAdd")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ACLPendingChangesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ACLPendingChangesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ACLsUpdateStatus:
    boto3_raw_data: "type_defs.ACLsUpdateStatusTypeDef" = dataclasses.field()

    ACLToApply = field("ACLToApply")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ACLsUpdateStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ACLsUpdateStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationMode:
    boto3_raw_data: "type_defs.AuthenticationModeTypeDef" = dataclasses.field()

    Type = field("Type")
    Passwords = field("Passwords")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationModeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationModeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Authentication:
    boto3_raw_data: "type_defs.AuthenticationTypeDef" = dataclasses.field()

    Type = field("Type")
    PasswordCount = field("PasswordCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthenticationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthenticationTypeDef"]],
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
class ServiceUpdateRequest:
    boto3_raw_data: "type_defs.ServiceUpdateRequestTypeDef" = dataclasses.field()

    ServiceUpdateNameToApply = field("ServiceUpdateNameToApply")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceUpdateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceUpdateRequestTypeDef"]
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
class UnprocessedCluster:
    boto3_raw_data: "type_defs.UnprocessedClusterTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")
    ErrorType = field("ErrorType")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedClusterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedClusterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingModifiedServiceUpdate:
    boto3_raw_data: "type_defs.PendingModifiedServiceUpdateTypeDef" = (
        dataclasses.field()
    )

    ServiceUpdateName = field("ServiceUpdateName")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingModifiedServiceUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingModifiedServiceUpdateTypeDef"]
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
class SecurityGroupMembership:
    boto3_raw_data: "type_defs.SecurityGroupMembershipTypeDef" = dataclasses.field()

    SecurityGroupId = field("SecurityGroupId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityGroupMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityGroupMembershipTypeDef"]
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
class ParameterGroup:
    boto3_raw_data: "type_defs.ParameterGroupTypeDef" = dataclasses.field()

    Name = field("Name")
    Family = field("Family")
    Description = field("Description")
    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteACLRequest:
    boto3_raw_data: "type_defs.DeleteACLRequestTypeDef" = dataclasses.field()

    ACLName = field("ACLName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteACLRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteACLRequestTypeDef"]
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

    ClusterName = field("ClusterName")
    MultiRegionClusterName = field("MultiRegionClusterName")
    FinalSnapshotName = field("FinalSnapshotName")

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
class DeleteMultiRegionClusterRequest:
    boto3_raw_data: "type_defs.DeleteMultiRegionClusterRequestTypeDef" = (
        dataclasses.field()
    )

    MultiRegionClusterName = field("MultiRegionClusterName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMultiRegionClusterRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiRegionClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteParameterGroupRequest:
    boto3_raw_data: "type_defs.DeleteParameterGroupRequestTypeDef" = dataclasses.field()

    ParameterGroupName = field("ParameterGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteParameterGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteParameterGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotRequest:
    boto3_raw_data: "type_defs.DeleteSnapshotRequestTypeDef" = dataclasses.field()

    SnapshotName = field("SnapshotName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubnetGroupRequest:
    boto3_raw_data: "type_defs.DeleteSubnetGroupRequestTypeDef" = dataclasses.field()

    SubnetGroupName = field("SubnetGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSubnetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubnetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserRequest:
    boto3_raw_data: "type_defs.DeleteUserRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserRequestTypeDef"]
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
class DescribeACLsRequest:
    boto3_raw_data: "type_defs.DescribeACLsRequestTypeDef" = dataclasses.field()

    ACLName = field("ACLName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeACLsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeACLsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClustersRequest:
    boto3_raw_data: "type_defs.DescribeClustersRequestTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ShowShardDetails = field("ShowShardDetails")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClustersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineVersionsRequest:
    boto3_raw_data: "type_defs.DescribeEngineVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    ParameterGroupFamily = field("ParameterGroupFamily")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    DefaultOnly = field("DefaultOnly")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEngineVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineVersionInfo:
    boto3_raw_data: "type_defs.EngineVersionInfoTypeDef" = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    EnginePatchVersion = field("EnginePatchVersion")
    ParameterGroupFamily = field("ParameterGroupFamily")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngineVersionInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngineVersionInfoTypeDef"]
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

    SourceName = field("SourceName")
    SourceType = field("SourceType")
    Message = field("Message")
    Date = field("Date")

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
class DescribeMultiRegionClustersRequest:
    boto3_raw_data: "type_defs.DescribeMultiRegionClustersRequestTypeDef" = (
        dataclasses.field()
    )

    MultiRegionClusterName = field("MultiRegionClusterName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ShowClusterDetails = field("ShowClusterDetails")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMultiRegionClustersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiRegionClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeParameterGroupsRequest:
    boto3_raw_data: "type_defs.DescribeParameterGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeParameterGroupsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeParameterGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeParametersRequest:
    boto3_raw_data: "type_defs.DescribeParametersRequestTypeDef" = dataclasses.field()

    ParameterGroupName = field("ParameterGroupName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeParametersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeParametersRequestTypeDef"]
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

    Name = field("Name")
    Value = field("Value")
    Description = field("Description")
    DataType = field("DataType")
    AllowedValues = field("AllowedValues")
    MinimumEngineVersion = field("MinimumEngineVersion")

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
class DescribeReservedNodesOfferingsRequest:
    boto3_raw_data: "type_defs.DescribeReservedNodesOfferingsRequestTypeDef" = (
        dataclasses.field()
    )

    ReservedNodesOfferingId = field("ReservedNodesOfferingId")
    NodeType = field("NodeType")
    Duration = field("Duration")
    OfferingType = field("OfferingType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedNodesOfferingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedNodesOfferingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodesRequest:
    boto3_raw_data: "type_defs.DescribeReservedNodesRequestTypeDef" = (
        dataclasses.field()
    )

    ReservationId = field("ReservationId")
    ReservedNodesOfferingId = field("ReservedNodesOfferingId")
    NodeType = field("NodeType")
    Duration = field("Duration")
    OfferingType = field("OfferingType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReservedNodesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedNodesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceUpdatesRequest:
    boto3_raw_data: "type_defs.DescribeServiceUpdatesRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceUpdateName = field("ServiceUpdateName")
    ClusterNames = field("ClusterNames")
    Status = field("Status")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeServiceUpdatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceUpdatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceUpdate:
    boto3_raw_data: "type_defs.ServiceUpdateTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")
    ServiceUpdateName = field("ServiceUpdateName")
    ReleaseDate = field("ReleaseDate")
    Description = field("Description")
    Status = field("Status")
    Type = field("Type")
    Engine = field("Engine")
    NodesUpdated = field("NodesUpdated")
    AutoUpdateStartDate = field("AutoUpdateStartDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceUpdateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsRequest:
    boto3_raw_data: "type_defs.DescribeSnapshotsRequestTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")
    SnapshotName = field("SnapshotName")
    Source = field("Source")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ShowDetail = field("ShowDetail")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSubnetGroupsRequest:
    boto3_raw_data: "type_defs.DescribeSubnetGroupsRequestTypeDef" = dataclasses.field()

    SubnetGroupName = field("SubnetGroupName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSubnetGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSubnetGroupsRequestTypeDef"]
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
class FailoverShardRequest:
    boto3_raw_data: "type_defs.FailoverShardRequestTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")
    ShardName = field("ShardName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverShardRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverShardRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAllowedMultiRegionClusterUpdatesRequest:
    boto3_raw_data: "type_defs.ListAllowedMultiRegionClusterUpdatesRequestTypeDef" = (
        dataclasses.field()
    )

    MultiRegionClusterName = field("MultiRegionClusterName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAllowedMultiRegionClusterUpdatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAllowedMultiRegionClusterUpdatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAllowedNodeTypeUpdatesRequest:
    boto3_raw_data: "type_defs.ListAllowedNodeTypeUpdatesRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterName = field("ClusterName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAllowedNodeTypeUpdatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAllowedNodeTypeUpdatesRequestTypeDef"]
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
class RegionalCluster:
    boto3_raw_data: "type_defs.RegionalClusterTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")
    Region = field("Region")
    Status = field("Status")
    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionalClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegionalClusterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterNameValue:
    boto3_raw_data: "type_defs.ParameterNameValueTypeDef" = dataclasses.field()

    ParameterName = field("ParameterName")
    ParameterValue = field("ParameterValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterNameValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterNameValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurringCharge:
    boto3_raw_data: "type_defs.RecurringChargeTypeDef" = dataclasses.field()

    RecurringChargeAmount = field("RecurringChargeAmount")
    RecurringChargeFrequency = field("RecurringChargeFrequency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecurringChargeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecurringChargeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaConfigurationRequest:
    boto3_raw_data: "type_defs.ReplicaConfigurationRequestTypeDef" = dataclasses.field()

    ReplicaCount = field("ReplicaCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicaConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetParameterGroupRequest:
    boto3_raw_data: "type_defs.ResetParameterGroupRequestTypeDef" = dataclasses.field()

    ParameterGroupName = field("ParameterGroupName")
    AllParameters = field("AllParameters")
    ParameterNames = field("ParameterNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetParameterGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetParameterGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotMigration:
    boto3_raw_data: "type_defs.SlotMigrationTypeDef" = dataclasses.field()

    ProgressPercentage = field("ProgressPercentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotMigrationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotMigrationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShardConfigurationRequest:
    boto3_raw_data: "type_defs.ShardConfigurationRequestTypeDef" = dataclasses.field()

    ShardCount = field("ShardCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ShardConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ShardConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShardConfiguration:
    boto3_raw_data: "type_defs.ShardConfigurationTypeDef" = dataclasses.field()

    Slots = field("Slots")
    ReplicaCount = field("ReplicaCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ShardConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ShardConfigurationTypeDef"]
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
class UpdateACLRequest:
    boto3_raw_data: "type_defs.UpdateACLRequestTypeDef" = dataclasses.field()

    ACLName = field("ACLName")
    UserNamesToAdd = field("UserNamesToAdd")
    UserNamesToRemove = field("UserNamesToRemove")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateACLRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubnetGroupRequest:
    boto3_raw_data: "type_defs.UpdateSubnetGroupRequestTypeDef" = dataclasses.field()

    SubnetGroupName = field("SubnetGroupName")
    Description = field("Description")
    SubnetIds = field("SubnetIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSubnetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubnetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ACL:
    boto3_raw_data: "type_defs.ACLTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    UserNames = field("UserNames")
    MinimumEngineVersion = field("MinimumEngineVersion")

    @cached_property
    def PendingChanges(self):  # pragma: no cover
        return ACLPendingChanges.make_one(self.boto3_raw_data["PendingChanges"])

    Clusters = field("Clusters")
    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ACLTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ACLTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserRequest:
    boto3_raw_data: "type_defs.UpdateUserRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @cached_property
    def AuthenticationMode(self):  # pragma: no cover
        return AuthenticationMode.make_one(self.boto3_raw_data["AuthenticationMode"])

    AccessString = field("AccessString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    AccessString = field("AccessString")
    ACLNames = field("ACLNames")
    MinimumEngineVersion = field("MinimumEngineVersion")

    @cached_property
    def Authentication(self):  # pragma: no cover
        return Authentication.make_one(self.boto3_raw_data["Authentication"])

    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subnet:
    boto3_raw_data: "type_defs.SubnetTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @cached_property
    def AvailabilityZone(self):  # pragma: no cover
        return AvailabilityZone.make_one(self.boto3_raw_data["AvailabilityZone"])

    SupportedNetworkTypes = field("SupportedNetworkTypes")

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
class BatchUpdateClusterRequest:
    boto3_raw_data: "type_defs.BatchUpdateClusterRequestTypeDef" = dataclasses.field()

    ClusterNames = field("ClusterNames")

    @cached_property
    def ServiceUpdate(self):  # pragma: no cover
        return ServiceUpdateRequest.make_one(self.boto3_raw_data["ServiceUpdate"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAllowedMultiRegionClusterUpdatesResponse:
    boto3_raw_data: "type_defs.ListAllowedMultiRegionClusterUpdatesResponseTypeDef" = (
        dataclasses.field()
    )

    ScaleUpNodeTypes = field("ScaleUpNodeTypes")
    ScaleDownNodeTypes = field("ScaleDownNodeTypes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAllowedMultiRegionClusterUpdatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAllowedMultiRegionClusterUpdatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAllowedNodeTypeUpdatesResponse:
    boto3_raw_data: "type_defs.ListAllowedNodeTypeUpdatesResponseTypeDef" = (
        dataclasses.field()
    )

    ScaleUpNodeTypes = field("ScaleUpNodeTypes")
    ScaleDownNodeTypes = field("ScaleDownNodeTypes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAllowedNodeTypeUpdatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAllowedNodeTypeUpdatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Node:
    boto3_raw_data: "type_defs.NodeTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    AvailabilityZone = field("AvailabilityZone")
    CreateTime = field("CreateTime")

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["Endpoint"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySnapshotRequest:
    boto3_raw_data: "type_defs.CopySnapshotRequestTypeDef" = dataclasses.field()

    SourceSnapshotName = field("SourceSnapshotName")
    TargetSnapshotName = field("TargetSnapshotName")
    TargetBucket = field("TargetBucket")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopySnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopySnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateACLRequest:
    boto3_raw_data: "type_defs.CreateACLRequestTypeDef" = dataclasses.field()

    ACLName = field("ACLName")
    UserNames = field("UserNames")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateACLRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateACLRequestTypeDef"]
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

    ClusterName = field("ClusterName")
    NodeType = field("NodeType")
    ACLName = field("ACLName")
    MultiRegionClusterName = field("MultiRegionClusterName")
    ParameterGroupName = field("ParameterGroupName")
    Description = field("Description")
    NumShards = field("NumShards")
    NumReplicasPerShard = field("NumReplicasPerShard")
    SubnetGroupName = field("SubnetGroupName")
    SecurityGroupIds = field("SecurityGroupIds")
    MaintenanceWindow = field("MaintenanceWindow")
    Port = field("Port")
    SnsTopicArn = field("SnsTopicArn")
    TLSEnabled = field("TLSEnabled")
    KmsKeyId = field("KmsKeyId")
    SnapshotArns = field("SnapshotArns")
    SnapshotName = field("SnapshotName")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SnapshotWindow = field("SnapshotWindow")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    DataTiering = field("DataTiering")
    NetworkType = field("NetworkType")
    IpDiscovery = field("IpDiscovery")

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
class CreateMultiRegionClusterRequest:
    boto3_raw_data: "type_defs.CreateMultiRegionClusterRequestTypeDef" = (
        dataclasses.field()
    )

    MultiRegionClusterNameSuffix = field("MultiRegionClusterNameSuffix")
    NodeType = field("NodeType")
    Description = field("Description")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    MultiRegionParameterGroupName = field("MultiRegionParameterGroupName")
    NumShards = field("NumShards")
    TLSEnabled = field("TLSEnabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMultiRegionClusterRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiRegionClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateParameterGroupRequest:
    boto3_raw_data: "type_defs.CreateParameterGroupRequestTypeDef" = dataclasses.field()

    ParameterGroupName = field("ParameterGroupName")
    Family = field("Family")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateParameterGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateParameterGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotRequest:
    boto3_raw_data: "type_defs.CreateSnapshotRequestTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")
    SnapshotName = field("SnapshotName")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubnetGroupRequest:
    boto3_raw_data: "type_defs.CreateSubnetGroupRequestTypeDef" = dataclasses.field()

    SubnetGroupName = field("SubnetGroupName")
    SubnetIds = field("SubnetIds")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSubnetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubnetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserRequest:
    boto3_raw_data: "type_defs.CreateUserRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @cached_property
    def AuthenticationMode(self):  # pragma: no cover
        return AuthenticationMode.make_one(self.boto3_raw_data["AuthenticationMode"])

    AccessString = field("AccessString")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsResponse:
    boto3_raw_data: "type_defs.ListTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedNodesOfferingRequest:
    boto3_raw_data: "type_defs.PurchaseReservedNodesOfferingRequestTypeDef" = (
        dataclasses.field()
    )

    ReservedNodesOfferingId = field("ReservedNodesOfferingId")
    ReservationId = field("ReservationId")
    NodeCount = field("NodeCount")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedNodesOfferingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseReservedNodesOfferingRequestTypeDef"]
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
class TagResourceResponse:
    boto3_raw_data: "type_defs.TagResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceResponse:
    boto3_raw_data: "type_defs.UntagResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateParameterGroupResponse:
    boto3_raw_data: "type_defs.CreateParameterGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ParameterGroup(self):  # pragma: no cover
        return ParameterGroup.make_one(self.boto3_raw_data["ParameterGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateParameterGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateParameterGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteParameterGroupResponse:
    boto3_raw_data: "type_defs.DeleteParameterGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ParameterGroup(self):  # pragma: no cover
        return ParameterGroup.make_one(self.boto3_raw_data["ParameterGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteParameterGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteParameterGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeParameterGroupsResponse:
    boto3_raw_data: "type_defs.DescribeParameterGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ParameterGroups(self):  # pragma: no cover
        return ParameterGroup.make_many(self.boto3_raw_data["ParameterGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeParameterGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeParameterGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetParameterGroupResponse:
    boto3_raw_data: "type_defs.ResetParameterGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def ParameterGroup(self):  # pragma: no cover
        return ParameterGroup.make_one(self.boto3_raw_data["ParameterGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetParameterGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetParameterGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateParameterGroupResponse:
    boto3_raw_data: "type_defs.UpdateParameterGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ParameterGroup(self):  # pragma: no cover
        return ParameterGroup.make_one(self.boto3_raw_data["ParameterGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateParameterGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateParameterGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeACLsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeACLsRequestPaginateTypeDef" = dataclasses.field()

    ACLName = field("ACLName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeACLsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeACLsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClustersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeClustersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterName = field("ClusterName")
    ShowShardDetails = field("ShowShardDetails")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClustersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClustersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineVersionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeEngineVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    ParameterGroupFamily = field("ParameterGroupFamily")
    DefaultOnly = field("DefaultOnly")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEngineVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiRegionClustersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeMultiRegionClustersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    MultiRegionClusterName = field("MultiRegionClusterName")
    ShowClusterDetails = field("ShowClusterDetails")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMultiRegionClustersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiRegionClustersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeParameterGroupsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeParameterGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeParameterGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeParameterGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeParametersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeParametersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeParametersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeParametersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodesOfferingsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeReservedNodesOfferingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ReservedNodesOfferingId = field("ReservedNodesOfferingId")
    NodeType = field("NodeType")
    Duration = field("Duration")
    OfferingType = field("OfferingType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedNodesOfferingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedNodesOfferingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeReservedNodesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ReservationId = field("ReservationId")
    ReservedNodesOfferingId = field("ReservedNodesOfferingId")
    NodeType = field("NodeType")
    Duration = field("Duration")
    OfferingType = field("OfferingType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedNodesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedNodesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceUpdatesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeServiceUpdatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ServiceUpdateName = field("ServiceUpdateName")
    ClusterNames = field("ClusterNames")
    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceUpdatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceUpdatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSnapshotsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterName = field("ClusterName")
    SnapshotName = field("SnapshotName")
    Source = field("Source")
    ShowDetail = field("ShowDetail")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSubnetGroupsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSubnetGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SubnetGroupName = field("SubnetGroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSubnetGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSubnetGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineVersionsResponse:
    boto3_raw_data: "type_defs.DescribeEngineVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EngineVersions(self):  # pragma: no cover
        return EngineVersionInfo.make_many(self.boto3_raw_data["EngineVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEngineVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SourceName = field("SourceName")
    SourceType = field("SourceType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Duration = field("Duration")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsRequest:
    boto3_raw_data: "type_defs.DescribeEventsRequestTypeDef" = dataclasses.field()

    SourceName = field("SourceName")
    SourceType = field("SourceType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Duration = field("Duration")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsResponse:
    boto3_raw_data: "type_defs.DescribeEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["Events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeParametersResponse:
    boto3_raw_data: "type_defs.DescribeParametersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeParametersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeParametersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceUpdatesResponse:
    boto3_raw_data: "type_defs.DescribeServiceUpdatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServiceUpdates(self):  # pragma: no cover
        return ServiceUpdate.make_many(self.boto3_raw_data["ServiceUpdates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeServiceUpdatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceUpdatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeUsersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsersRequest:
    boto3_raw_data: "type_defs.DescribeUsersRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUsersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiRegionCluster:
    boto3_raw_data: "type_defs.MultiRegionClusterTypeDef" = dataclasses.field()

    MultiRegionClusterName = field("MultiRegionClusterName")
    Description = field("Description")
    Status = field("Status")
    NodeType = field("NodeType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    NumberOfShards = field("NumberOfShards")

    @cached_property
    def Clusters(self):  # pragma: no cover
        return RegionalCluster.make_many(self.boto3_raw_data["Clusters"])

    MultiRegionParameterGroupName = field("MultiRegionParameterGroupName")
    TLSEnabled = field("TLSEnabled")
    ARN = field("ARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiRegionClusterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiRegionClusterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateParameterGroupRequest:
    boto3_raw_data: "type_defs.UpdateParameterGroupRequestTypeDef" = dataclasses.field()

    ParameterGroupName = field("ParameterGroupName")

    @cached_property
    def ParameterNameValues(self):  # pragma: no cover
        return ParameterNameValue.make_many(self.boto3_raw_data["ParameterNameValues"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateParameterGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateParameterGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedNode:
    boto3_raw_data: "type_defs.ReservedNodeTypeDef" = dataclasses.field()

    ReservationId = field("ReservationId")
    ReservedNodesOfferingId = field("ReservedNodesOfferingId")
    NodeType = field("NodeType")
    StartTime = field("StartTime")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    NodeCount = field("NodeCount")
    OfferingType = field("OfferingType")
    State = field("State")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReservedNodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReservedNodeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedNodesOffering:
    boto3_raw_data: "type_defs.ReservedNodesOfferingTypeDef" = dataclasses.field()

    ReservedNodesOfferingId = field("ReservedNodesOfferingId")
    NodeType = field("NodeType")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    OfferingType = field("OfferingType")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedNodesOfferingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedNodesOfferingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReshardingStatus:
    boto3_raw_data: "type_defs.ReshardingStatusTypeDef" = dataclasses.field()

    @cached_property
    def SlotMigration(self):  # pragma: no cover
        return SlotMigration.make_one(self.boto3_raw_data["SlotMigration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReshardingStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReshardingStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterRequest:
    boto3_raw_data: "type_defs.UpdateClusterRequestTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")
    Description = field("Description")
    SecurityGroupIds = field("SecurityGroupIds")
    MaintenanceWindow = field("MaintenanceWindow")
    SnsTopicArn = field("SnsTopicArn")
    SnsTopicStatus = field("SnsTopicStatus")
    ParameterGroupName = field("ParameterGroupName")
    SnapshotWindow = field("SnapshotWindow")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    NodeType = field("NodeType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")

    @cached_property
    def ReplicaConfiguration(self):  # pragma: no cover
        return ReplicaConfigurationRequest.make_one(
            self.boto3_raw_data["ReplicaConfiguration"]
        )

    @cached_property
    def ShardConfiguration(self):  # pragma: no cover
        return ShardConfigurationRequest.make_one(
            self.boto3_raw_data["ShardConfiguration"]
        )

    ACLName = field("ACLName")
    IpDiscovery = field("IpDiscovery")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMultiRegionClusterRequest:
    boto3_raw_data: "type_defs.UpdateMultiRegionClusterRequestTypeDef" = (
        dataclasses.field()
    )

    MultiRegionClusterName = field("MultiRegionClusterName")
    NodeType = field("NodeType")
    Description = field("Description")
    EngineVersion = field("EngineVersion")

    @cached_property
    def ShardConfiguration(self):  # pragma: no cover
        return ShardConfigurationRequest.make_one(
            self.boto3_raw_data["ShardConfiguration"]
        )

    MultiRegionParameterGroupName = field("MultiRegionParameterGroupName")
    UpdateStrategy = field("UpdateStrategy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMultiRegionClusterRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMultiRegionClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShardDetail:
    boto3_raw_data: "type_defs.ShardDetailTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return ShardConfiguration.make_one(self.boto3_raw_data["Configuration"])

    Size = field("Size")
    SnapshotCreationTime = field("SnapshotCreationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShardDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShardDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateACLResponse:
    boto3_raw_data: "type_defs.CreateACLResponseTypeDef" = dataclasses.field()

    @cached_property
    def ACL(self):  # pragma: no cover
        return ACL.make_one(self.boto3_raw_data["ACL"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateACLResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateACLResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteACLResponse:
    boto3_raw_data: "type_defs.DeleteACLResponseTypeDef" = dataclasses.field()

    @cached_property
    def ACL(self):  # pragma: no cover
        return ACL.make_one(self.boto3_raw_data["ACL"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteACLResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteACLResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeACLsResponse:
    boto3_raw_data: "type_defs.DescribeACLsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ACLs(self):  # pragma: no cover
        return ACL.make_many(self.boto3_raw_data["ACLs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeACLsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeACLsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateACLResponse:
    boto3_raw_data: "type_defs.UpdateACLResponseTypeDef" = dataclasses.field()

    @cached_property
    def ACL(self):  # pragma: no cover
        return ACL.make_one(self.boto3_raw_data["ACL"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateACLResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateACLResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserResponse:
    boto3_raw_data: "type_defs.CreateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserResponse:
    boto3_raw_data: "type_defs.DeleteUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsersResponse:
    boto3_raw_data: "type_defs.DescribeUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUsersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserResponse:
    boto3_raw_data: "type_defs.UpdateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubnetGroup:
    boto3_raw_data: "type_defs.SubnetGroupTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    VpcId = field("VpcId")

    @cached_property
    def Subnets(self):  # pragma: no cover
        return Subnet.make_many(self.boto3_raw_data["Subnets"])

    ARN = field("ARN")
    SupportedNetworkTypes = field("SupportedNetworkTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubnetGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubnetGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Shard:
    boto3_raw_data: "type_defs.ShardTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    Slots = field("Slots")

    @cached_property
    def Nodes(self):  # pragma: no cover
        return Node.make_many(self.boto3_raw_data["Nodes"])

    NumberOfNodes = field("NumberOfNodes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShardTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultiRegionClusterResponse:
    boto3_raw_data: "type_defs.CreateMultiRegionClusterResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MultiRegionCluster(self):  # pragma: no cover
        return MultiRegionCluster.make_one(self.boto3_raw_data["MultiRegionCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMultiRegionClusterResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiRegionClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMultiRegionClusterResponse:
    boto3_raw_data: "type_defs.DeleteMultiRegionClusterResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MultiRegionCluster(self):  # pragma: no cover
        return MultiRegionCluster.make_one(self.boto3_raw_data["MultiRegionCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMultiRegionClusterResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiRegionClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiRegionClustersResponse:
    boto3_raw_data: "type_defs.DescribeMultiRegionClustersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MultiRegionClusters(self):  # pragma: no cover
        return MultiRegionCluster.make_many(self.boto3_raw_data["MultiRegionClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMultiRegionClustersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiRegionClustersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMultiRegionClusterResponse:
    boto3_raw_data: "type_defs.UpdateMultiRegionClusterResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MultiRegionCluster(self):  # pragma: no cover
        return MultiRegionCluster.make_one(self.boto3_raw_data["MultiRegionCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMultiRegionClusterResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMultiRegionClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodesResponse:
    boto3_raw_data: "type_defs.DescribeReservedNodesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReservedNodes(self):  # pragma: no cover
        return ReservedNode.make_many(self.boto3_raw_data["ReservedNodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeReservedNodesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedNodesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedNodesOfferingResponse:
    boto3_raw_data: "type_defs.PurchaseReservedNodesOfferingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReservedNode(self):  # pragma: no cover
        return ReservedNode.make_one(self.boto3_raw_data["ReservedNode"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedNodesOfferingResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseReservedNodesOfferingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodesOfferingsResponse:
    boto3_raw_data: "type_defs.DescribeReservedNodesOfferingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReservedNodesOfferings(self):  # pragma: no cover
        return ReservedNodesOffering.make_many(
            self.boto3_raw_data["ReservedNodesOfferings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedNodesOfferingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedNodesOfferingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterPendingUpdates:
    boto3_raw_data: "type_defs.ClusterPendingUpdatesTypeDef" = dataclasses.field()

    @cached_property
    def Resharding(self):  # pragma: no cover
        return ReshardingStatus.make_one(self.boto3_raw_data["Resharding"])

    @cached_property
    def ACLs(self):  # pragma: no cover
        return ACLsUpdateStatus.make_one(self.boto3_raw_data["ACLs"])

    @cached_property
    def ServiceUpdates(self):  # pragma: no cover
        return PendingModifiedServiceUpdate.make_many(
            self.boto3_raw_data["ServiceUpdates"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterPendingUpdatesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterPendingUpdatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterConfiguration:
    boto3_raw_data: "type_defs.ClusterConfigurationTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    NodeType = field("NodeType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    MaintenanceWindow = field("MaintenanceWindow")
    TopicArn = field("TopicArn")
    Port = field("Port")
    ParameterGroupName = field("ParameterGroupName")
    SubnetGroupName = field("SubnetGroupName")
    VpcId = field("VpcId")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    SnapshotWindow = field("SnapshotWindow")
    NumShards = field("NumShards")

    @cached_property
    def Shards(self):  # pragma: no cover
        return ShardDetail.make_many(self.boto3_raw_data["Shards"])

    MultiRegionParameterGroupName = field("MultiRegionParameterGroupName")
    MultiRegionClusterName = field("MultiRegionClusterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubnetGroupResponse:
    boto3_raw_data: "type_defs.CreateSubnetGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def SubnetGroup(self):  # pragma: no cover
        return SubnetGroup.make_one(self.boto3_raw_data["SubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSubnetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubnetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubnetGroupResponse:
    boto3_raw_data: "type_defs.DeleteSubnetGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def SubnetGroup(self):  # pragma: no cover
        return SubnetGroup.make_one(self.boto3_raw_data["SubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSubnetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubnetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSubnetGroupsResponse:
    boto3_raw_data: "type_defs.DescribeSubnetGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SubnetGroups(self):  # pragma: no cover
        return SubnetGroup.make_many(self.boto3_raw_data["SubnetGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSubnetGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSubnetGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubnetGroupResponse:
    boto3_raw_data: "type_defs.UpdateSubnetGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def SubnetGroup(self):  # pragma: no cover
        return SubnetGroup.make_one(self.boto3_raw_data["SubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSubnetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubnetGroupResponseTypeDef"]
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

    Name = field("Name")
    Description = field("Description")
    Status = field("Status")

    @cached_property
    def PendingUpdates(self):  # pragma: no cover
        return ClusterPendingUpdates.make_one(self.boto3_raw_data["PendingUpdates"])

    MultiRegionClusterName = field("MultiRegionClusterName")
    NumberOfShards = field("NumberOfShards")

    @cached_property
    def Shards(self):  # pragma: no cover
        return Shard.make_many(self.boto3_raw_data["Shards"])

    AvailabilityMode = field("AvailabilityMode")

    @cached_property
    def ClusterEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["ClusterEndpoint"])

    NodeType = field("NodeType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    EnginePatchVersion = field("EnginePatchVersion")
    ParameterGroupName = field("ParameterGroupName")
    ParameterGroupStatus = field("ParameterGroupStatus")

    @cached_property
    def SecurityGroups(self):  # pragma: no cover
        return SecurityGroupMembership.make_many(self.boto3_raw_data["SecurityGroups"])

    SubnetGroupName = field("SubnetGroupName")
    TLSEnabled = field("TLSEnabled")
    KmsKeyId = field("KmsKeyId")
    ARN = field("ARN")
    SnsTopicArn = field("SnsTopicArn")
    SnsTopicStatus = field("SnsTopicStatus")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    MaintenanceWindow = field("MaintenanceWindow")
    SnapshotWindow = field("SnapshotWindow")
    ACLName = field("ACLName")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    DataTiering = field("DataTiering")
    NetworkType = field("NetworkType")
    IpDiscovery = field("IpDiscovery")

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
class Snapshot:
    boto3_raw_data: "type_defs.SnapshotTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    Source = field("Source")
    KmsKeyId = field("KmsKeyId")
    ARN = field("ARN")

    @cached_property
    def ClusterConfiguration(self):  # pragma: no cover
        return ClusterConfiguration.make_one(
            self.boto3_raw_data["ClusterConfiguration"]
        )

    DataTiering = field("DataTiering")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnapshotTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateClusterResponse:
    boto3_raw_data: "type_defs.BatchUpdateClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProcessedClusters(self):  # pragma: no cover
        return Cluster.make_many(self.boto3_raw_data["ProcessedClusters"])

    @cached_property
    def UnprocessedClusters(self):  # pragma: no cover
        return UnprocessedCluster.make_many(self.boto3_raw_data["UnprocessedClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateClusterResponseTypeDef"]
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
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

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
class DeleteClusterResponse:
    boto3_raw_data: "type_defs.DeleteClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClustersResponse:
    boto3_raw_data: "type_defs.DescribeClustersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Clusters(self):  # pragma: no cover
        return Cluster.make_many(self.boto3_raw_data["Clusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClustersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClustersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverShardResponse:
    boto3_raw_data: "type_defs.FailoverShardResponseTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverShardResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverShardResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterResponse:
    boto3_raw_data: "type_defs.UpdateClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySnapshotResponse:
    boto3_raw_data: "type_defs.CopySnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopySnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopySnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotResponse:
    boto3_raw_data: "type_defs.CreateSnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotResponse:
    boto3_raw_data: "type_defs.DeleteSnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsResponse:
    boto3_raw_data: "type_defs.DescribeSnapshotsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Snapshots(self):  # pragma: no cover
        return Snapshot.make_many(self.boto3_raw_data["Snapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
