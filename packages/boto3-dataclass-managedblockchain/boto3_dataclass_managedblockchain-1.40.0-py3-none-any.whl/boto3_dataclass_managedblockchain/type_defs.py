# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_managedblockchain import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessorSummary:
    boto3_raw_data: "type_defs.AccessorSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")
    Status = field("Status")
    CreationDate = field("CreationDate")
    Arn = field("Arn")
    NetworkType = field("NetworkType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessorSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Accessor:
    boto3_raw_data: "type_defs.AccessorTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")
    BillingToken = field("BillingToken")
    Status = field("Status")
    CreationDate = field("CreationDate")
    Arn = field("Arn")
    Tags = field("Tags")
    NetworkType = field("NetworkType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApprovalThresholdPolicy:
    boto3_raw_data: "type_defs.ApprovalThresholdPolicyTypeDef" = dataclasses.field()

    ThresholdPercentage = field("ThresholdPercentage")
    ProposalDurationInHours = field("ProposalDurationInHours")
    ThresholdComparator = field("ThresholdComparator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApprovalThresholdPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApprovalThresholdPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessorInput:
    boto3_raw_data: "type_defs.CreateAccessorInputTypeDef" = dataclasses.field()

    ClientRequestToken = field("ClientRequestToken")
    AccessorType = field("AccessorType")
    Tags = field("Tags")
    NetworkType = field("NetworkType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessorInputTypeDef"]
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
class DeleteAccessorInput:
    boto3_raw_data: "type_defs.DeleteAccessorInputTypeDef" = dataclasses.field()

    AccessorId = field("AccessorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccessorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMemberInput:
    boto3_raw_data: "type_defs.DeleteMemberInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    MemberId = field("MemberId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteMemberInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMemberInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNodeInput:
    boto3_raw_data: "type_defs.DeleteNodeInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    NodeId = field("NodeId")
    MemberId = field("MemberId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteNodeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteNodeInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessorInput:
    boto3_raw_data: "type_defs.GetAccessorInputTypeDef" = dataclasses.field()

    AccessorId = field("AccessorId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAccessorInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemberInput:
    boto3_raw_data: "type_defs.GetMemberInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    MemberId = field("MemberId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMemberInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetMemberInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkInput:
    boto3_raw_data: "type_defs.GetNetworkInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetNetworkInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetNetworkInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNodeInput:
    boto3_raw_data: "type_defs.GetNodeInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    NodeId = field("NodeId")
    MemberId = field("MemberId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetNodeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetNodeInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProposalInput:
    boto3_raw_data: "type_defs.GetProposalInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    ProposalId = field("ProposalId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetProposalInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProposalInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkSummary:
    boto3_raw_data: "type_defs.NetworkSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    Framework = field("Framework")
    FrameworkVersion = field("FrameworkVersion")
    Status = field("Status")
    CreationDate = field("CreationDate")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InviteAction:
    boto3_raw_data: "type_defs.InviteActionTypeDef" = dataclasses.field()

    Principal = field("Principal")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InviteActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InviteActionTypeDef"]],
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
class ListAccessorsInput:
    boto3_raw_data: "type_defs.ListAccessorsInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    NetworkType = field("NetworkType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessorsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvitationsInput:
    boto3_raw_data: "type_defs.ListInvitationsInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvitationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvitationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersInput:
    boto3_raw_data: "type_defs.ListMembersInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    Name = field("Name")
    Status = field("Status")
    IsOwned = field("IsOwned")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMembersInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberSummary:
    boto3_raw_data: "type_defs.MemberSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    Status = field("Status")
    CreationDate = field("CreationDate")
    IsOwned = field("IsOwned")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNetworksInput:
    boto3_raw_data: "type_defs.ListNetworksInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Framework = field("Framework")
    Status = field("Status")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListNetworksInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNetworksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesInput:
    boto3_raw_data: "type_defs.ListNodesInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    MemberId = field("MemberId")
    Status = field("Status")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListNodesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListNodesInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeSummary:
    boto3_raw_data: "type_defs.NodeSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Status = field("Status")
    CreationDate = field("CreationDate")
    AvailabilityZone = field("AvailabilityZone")
    InstanceType = field("InstanceType")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProposalVotesInput:
    boto3_raw_data: "type_defs.ListProposalVotesInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    ProposalId = field("ProposalId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProposalVotesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProposalVotesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoteSummary:
    boto3_raw_data: "type_defs.VoteSummaryTypeDef" = dataclasses.field()

    Vote = field("Vote")
    MemberName = field("MemberName")
    MemberId = field("MemberId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VoteSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VoteSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProposalsInput:
    boto3_raw_data: "type_defs.ListProposalsInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProposalsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProposalsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProposalSummary:
    boto3_raw_data: "type_defs.ProposalSummaryTypeDef" = dataclasses.field()

    ProposalId = field("ProposalId")
    Description = field("Description")
    ProposedByMemberId = field("ProposedByMemberId")
    ProposedByMemberName = field("ProposedByMemberName")
    Status = field("Status")
    CreationDate = field("CreationDate")
    ExpirationDate = field("ExpirationDate")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProposalSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProposalSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

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
class LogConfiguration:
    boto3_raw_data: "type_defs.LogConfigurationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

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
class MemberFabricAttributes:
    boto3_raw_data: "type_defs.MemberFabricAttributesTypeDef" = dataclasses.field()

    AdminUsername = field("AdminUsername")
    CaEndpoint = field("CaEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemberFabricAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberFabricAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberFabricConfiguration:
    boto3_raw_data: "type_defs.MemberFabricConfigurationTypeDef" = dataclasses.field()

    AdminUsername = field("AdminUsername")
    AdminPassword = field("AdminPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemberFabricConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberFabricConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkEthereumAttributes:
    boto3_raw_data: "type_defs.NetworkEthereumAttributesTypeDef" = dataclasses.field()

    ChainId = field("ChainId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkEthereumAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkEthereumAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFabricAttributes:
    boto3_raw_data: "type_defs.NetworkFabricAttributesTypeDef" = dataclasses.field()

    OrderingServiceEndpoint = field("OrderingServiceEndpoint")
    Edition = field("Edition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkFabricAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFabricAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFabricConfiguration:
    boto3_raw_data: "type_defs.NetworkFabricConfigurationTypeDef" = dataclasses.field()

    Edition = field("Edition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkFabricConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFabricConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeEthereumAttributes:
    boto3_raw_data: "type_defs.NodeEthereumAttributesTypeDef" = dataclasses.field()

    HttpEndpoint = field("HttpEndpoint")
    WebSocketEndpoint = field("WebSocketEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeEthereumAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeEthereumAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeFabricAttributes:
    boto3_raw_data: "type_defs.NodeFabricAttributesTypeDef" = dataclasses.field()

    PeerEndpoint = field("PeerEndpoint")
    PeerEventEndpoint = field("PeerEventEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeFabricAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeFabricAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAction:
    boto3_raw_data: "type_defs.RemoveActionTypeDef" = dataclasses.field()

    MemberId = field("MemberId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemoveActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RemoveActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectInvitationInput:
    boto3_raw_data: "type_defs.RejectInvitationInputTypeDef" = dataclasses.field()

    InvitationId = field("InvitationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectInvitationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectInvitationInputTypeDef"]
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
class VoteOnProposalInput:
    boto3_raw_data: "type_defs.VoteOnProposalInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    ProposalId = field("ProposalId")
    VoterMemberId = field("VoterMemberId")
    Vote = field("Vote")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoteOnProposalInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoteOnProposalInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VotingPolicy:
    boto3_raw_data: "type_defs.VotingPolicyTypeDef" = dataclasses.field()

    @cached_property
    def ApprovalThresholdPolicy(self):  # pragma: no cover
        return ApprovalThresholdPolicy.make_one(
            self.boto3_raw_data["ApprovalThresholdPolicy"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VotingPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VotingPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessorOutput:
    boto3_raw_data: "type_defs.CreateAccessorOutputTypeDef" = dataclasses.field()

    AccessorId = field("AccessorId")
    BillingToken = field("BillingToken")
    NetworkType = field("NetworkType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMemberOutput:
    boto3_raw_data: "type_defs.CreateMemberOutputTypeDef" = dataclasses.field()

    MemberId = field("MemberId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMemberOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMemberOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNetworkOutput:
    boto3_raw_data: "type_defs.CreateNetworkOutputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    MemberId = field("MemberId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNetworkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNetworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNodeOutput:
    boto3_raw_data: "type_defs.CreateNodeOutputTypeDef" = dataclasses.field()

    NodeId = field("NodeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateNodeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProposalOutput:
    boto3_raw_data: "type_defs.CreateProposalOutputTypeDef" = dataclasses.field()

    ProposalId = field("ProposalId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProposalOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProposalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessorOutput:
    boto3_raw_data: "type_defs.GetAccessorOutputTypeDef" = dataclasses.field()

    @cached_property
    def Accessor(self):  # pragma: no cover
        return Accessor.make_one(self.boto3_raw_data["Accessor"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAccessorOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessorsOutput:
    boto3_raw_data: "type_defs.ListAccessorsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Accessors(self):  # pragma: no cover
        return AccessorSummary.make_many(self.boto3_raw_data["Accessors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessorsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessorsOutputTypeDef"]
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

    Tags = field("Tags")

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
class Invitation:
    boto3_raw_data: "type_defs.InvitationTypeDef" = dataclasses.field()

    InvitationId = field("InvitationId")
    CreationDate = field("CreationDate")
    ExpirationDate = field("ExpirationDate")
    Status = field("Status")

    @cached_property
    def NetworkSummary(self):  # pragma: no cover
        return NetworkSummary.make_one(self.boto3_raw_data["NetworkSummary"])

    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvitationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InvitationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNetworksOutput:
    boto3_raw_data: "type_defs.ListNetworksOutputTypeDef" = dataclasses.field()

    @cached_property
    def Networks(self):  # pragma: no cover
        return NetworkSummary.make_many(self.boto3_raw_data["Networks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNetworksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNetworksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessorsInputPaginate:
    boto3_raw_data: "type_defs.ListAccessorsInputPaginateTypeDef" = dataclasses.field()

    NetworkType = field("NetworkType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessorsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessorsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersOutput:
    boto3_raw_data: "type_defs.ListMembersOutputTypeDef" = dataclasses.field()

    @cached_property
    def Members(self):  # pragma: no cover
        return MemberSummary.make_many(self.boto3_raw_data["Members"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMembersOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesOutput:
    boto3_raw_data: "type_defs.ListNodesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Nodes(self):  # pragma: no cover
        return NodeSummary.make_many(self.boto3_raw_data["Nodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListNodesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListNodesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProposalVotesOutput:
    boto3_raw_data: "type_defs.ListProposalVotesOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProposalVotes(self):  # pragma: no cover
        return VoteSummary.make_many(self.boto3_raw_data["ProposalVotes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProposalVotesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProposalVotesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProposalsOutput:
    boto3_raw_data: "type_defs.ListProposalsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Proposals(self):  # pragma: no cover
        return ProposalSummary.make_many(self.boto3_raw_data["Proposals"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProposalsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProposalsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogConfigurations:
    boto3_raw_data: "type_defs.LogConfigurationsTypeDef" = dataclasses.field()

    @cached_property
    def Cloudwatch(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["Cloudwatch"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogConfigurationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberFrameworkAttributes:
    boto3_raw_data: "type_defs.MemberFrameworkAttributesTypeDef" = dataclasses.field()

    @cached_property
    def Fabric(self):  # pragma: no cover
        return MemberFabricAttributes.make_one(self.boto3_raw_data["Fabric"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemberFrameworkAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberFrameworkAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberFrameworkConfiguration:
    boto3_raw_data: "type_defs.MemberFrameworkConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Fabric(self):  # pragma: no cover
        return MemberFabricConfiguration.make_one(self.boto3_raw_data["Fabric"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemberFrameworkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberFrameworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFrameworkAttributes:
    boto3_raw_data: "type_defs.NetworkFrameworkAttributesTypeDef" = dataclasses.field()

    @cached_property
    def Fabric(self):  # pragma: no cover
        return NetworkFabricAttributes.make_one(self.boto3_raw_data["Fabric"])

    @cached_property
    def Ethereum(self):  # pragma: no cover
        return NetworkEthereumAttributes.make_one(self.boto3_raw_data["Ethereum"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkFrameworkAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFrameworkAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFrameworkConfiguration:
    boto3_raw_data: "type_defs.NetworkFrameworkConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Fabric(self):  # pragma: no cover
        return NetworkFabricConfiguration.make_one(self.boto3_raw_data["Fabric"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NetworkFrameworkConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFrameworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeFrameworkAttributes:
    boto3_raw_data: "type_defs.NodeFrameworkAttributesTypeDef" = dataclasses.field()

    @cached_property
    def Fabric(self):  # pragma: no cover
        return NodeFabricAttributes.make_one(self.boto3_raw_data["Fabric"])

    @cached_property
    def Ethereum(self):  # pragma: no cover
        return NodeEthereumAttributes.make_one(self.boto3_raw_data["Ethereum"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeFrameworkAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeFrameworkAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProposalActionsOutput:
    boto3_raw_data: "type_defs.ProposalActionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Invitations(self):  # pragma: no cover
        return InviteAction.make_many(self.boto3_raw_data["Invitations"])

    @cached_property
    def Removals(self):  # pragma: no cover
        return RemoveAction.make_many(self.boto3_raw_data["Removals"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProposalActionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProposalActionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProposalActions:
    boto3_raw_data: "type_defs.ProposalActionsTypeDef" = dataclasses.field()

    @cached_property
    def Invitations(self):  # pragma: no cover
        return InviteAction.make_many(self.boto3_raw_data["Invitations"])

    @cached_property
    def Removals(self):  # pragma: no cover
        return RemoveAction.make_many(self.boto3_raw_data["Removals"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProposalActionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProposalActionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvitationsOutput:
    boto3_raw_data: "type_defs.ListInvitationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Invitations(self):  # pragma: no cover
        return Invitation.make_many(self.boto3_raw_data["Invitations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvitationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvitationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberFabricLogPublishingConfiguration:
    boto3_raw_data: "type_defs.MemberFabricLogPublishingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CaLogs(self):  # pragma: no cover
        return LogConfigurations.make_one(self.boto3_raw_data["CaLogs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MemberFabricLogPublishingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberFabricLogPublishingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeFabricLogPublishingConfiguration:
    boto3_raw_data: "type_defs.NodeFabricLogPublishingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChaincodeLogs(self):  # pragma: no cover
        return LogConfigurations.make_one(self.boto3_raw_data["ChaincodeLogs"])

    @cached_property
    def PeerLogs(self):  # pragma: no cover
        return LogConfigurations.make_one(self.boto3_raw_data["PeerLogs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NodeFabricLogPublishingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeFabricLogPublishingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Network:
    boto3_raw_data: "type_defs.NetworkTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    Framework = field("Framework")
    FrameworkVersion = field("FrameworkVersion")

    @cached_property
    def FrameworkAttributes(self):  # pragma: no cover
        return NetworkFrameworkAttributes.make_one(
            self.boto3_raw_data["FrameworkAttributes"]
        )

    VpcEndpointServiceName = field("VpcEndpointServiceName")

    @cached_property
    def VotingPolicy(self):  # pragma: no cover
        return VotingPolicy.make_one(self.boto3_raw_data["VotingPolicy"])

    Status = field("Status")
    CreationDate = field("CreationDate")
    Tags = field("Tags")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Proposal:
    boto3_raw_data: "type_defs.ProposalTypeDef" = dataclasses.field()

    ProposalId = field("ProposalId")
    NetworkId = field("NetworkId")
    Description = field("Description")

    @cached_property
    def Actions(self):  # pragma: no cover
        return ProposalActionsOutput.make_one(self.boto3_raw_data["Actions"])

    ProposedByMemberId = field("ProposedByMemberId")
    ProposedByMemberName = field("ProposedByMemberName")
    Status = field("Status")
    CreationDate = field("CreationDate")
    ExpirationDate = field("ExpirationDate")
    YesVoteCount = field("YesVoteCount")
    NoVoteCount = field("NoVoteCount")
    OutstandingVoteCount = field("OutstandingVoteCount")
    Tags = field("Tags")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProposalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProposalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberLogPublishingConfiguration:
    boto3_raw_data: "type_defs.MemberLogPublishingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Fabric(self):  # pragma: no cover
        return MemberFabricLogPublishingConfiguration.make_one(
            self.boto3_raw_data["Fabric"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MemberLogPublishingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberLogPublishingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeLogPublishingConfiguration:
    boto3_raw_data: "type_defs.NodeLogPublishingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Fabric(self):  # pragma: no cover
        return NodeFabricLogPublishingConfiguration.make_one(
            self.boto3_raw_data["Fabric"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NodeLogPublishingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeLogPublishingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkOutput:
    boto3_raw_data: "type_defs.GetNetworkOutputTypeDef" = dataclasses.field()

    @cached_property
    def Network(self):  # pragma: no cover
        return Network.make_one(self.boto3_raw_data["Network"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetNetworkOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProposalOutput:
    boto3_raw_data: "type_defs.GetProposalOutputTypeDef" = dataclasses.field()

    @cached_property
    def Proposal(self):  # pragma: no cover
        return Proposal.make_one(self.boto3_raw_data["Proposal"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetProposalOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProposalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProposalInput:
    boto3_raw_data: "type_defs.CreateProposalInputTypeDef" = dataclasses.field()

    ClientRequestToken = field("ClientRequestToken")
    NetworkId = field("NetworkId")
    MemberId = field("MemberId")
    Actions = field("Actions")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProposalInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProposalInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberConfiguration:
    boto3_raw_data: "type_defs.MemberConfigurationTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def FrameworkConfiguration(self):  # pragma: no cover
        return MemberFrameworkConfiguration.make_one(
            self.boto3_raw_data["FrameworkConfiguration"]
        )

    Description = field("Description")

    @cached_property
    def LogPublishingConfiguration(self):  # pragma: no cover
        return MemberLogPublishingConfiguration.make_one(
            self.boto3_raw_data["LogPublishingConfiguration"]
        )

    Tags = field("Tags")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemberConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Member:
    boto3_raw_data: "type_defs.MemberTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    Id = field("Id")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def FrameworkAttributes(self):  # pragma: no cover
        return MemberFrameworkAttributes.make_one(
            self.boto3_raw_data["FrameworkAttributes"]
        )

    @cached_property
    def LogPublishingConfiguration(self):  # pragma: no cover
        return MemberLogPublishingConfiguration.make_one(
            self.boto3_raw_data["LogPublishingConfiguration"]
        )

    Status = field("Status")
    CreationDate = field("CreationDate")
    Tags = field("Tags")
    Arn = field("Arn")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMemberInput:
    boto3_raw_data: "type_defs.UpdateMemberInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    MemberId = field("MemberId")

    @cached_property
    def LogPublishingConfiguration(self):  # pragma: no cover
        return MemberLogPublishingConfiguration.make_one(
            self.boto3_raw_data["LogPublishingConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateMemberInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMemberInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeConfiguration:
    boto3_raw_data: "type_defs.NodeConfigurationTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")
    AvailabilityZone = field("AvailabilityZone")

    @cached_property
    def LogPublishingConfiguration(self):  # pragma: no cover
        return NodeLogPublishingConfiguration.make_one(
            self.boto3_raw_data["LogPublishingConfiguration"]
        )

    StateDB = field("StateDB")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeConfigurationTypeDef"]
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

    NetworkId = field("NetworkId")
    MemberId = field("MemberId")
    Id = field("Id")
    InstanceType = field("InstanceType")
    AvailabilityZone = field("AvailabilityZone")

    @cached_property
    def FrameworkAttributes(self):  # pragma: no cover
        return NodeFrameworkAttributes.make_one(
            self.boto3_raw_data["FrameworkAttributes"]
        )

    @cached_property
    def LogPublishingConfiguration(self):  # pragma: no cover
        return NodeLogPublishingConfiguration.make_one(
            self.boto3_raw_data["LogPublishingConfiguration"]
        )

    StateDB = field("StateDB")
    Status = field("Status")
    CreationDate = field("CreationDate")
    Tags = field("Tags")
    Arn = field("Arn")
    KmsKeyArn = field("KmsKeyArn")

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
class UpdateNodeInput:
    boto3_raw_data: "type_defs.UpdateNodeInputTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    NodeId = field("NodeId")
    MemberId = field("MemberId")

    @cached_property
    def LogPublishingConfiguration(self):  # pragma: no cover
        return NodeLogPublishingConfiguration.make_one(
            self.boto3_raw_data["LogPublishingConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateNodeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateNodeInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMemberInput:
    boto3_raw_data: "type_defs.CreateMemberInputTypeDef" = dataclasses.field()

    ClientRequestToken = field("ClientRequestToken")
    InvitationId = field("InvitationId")
    NetworkId = field("NetworkId")

    @cached_property
    def MemberConfiguration(self):  # pragma: no cover
        return MemberConfiguration.make_one(self.boto3_raw_data["MemberConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateMemberInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMemberInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNetworkInput:
    boto3_raw_data: "type_defs.CreateNetworkInputTypeDef" = dataclasses.field()

    ClientRequestToken = field("ClientRequestToken")
    Name = field("Name")
    Framework = field("Framework")
    FrameworkVersion = field("FrameworkVersion")

    @cached_property
    def VotingPolicy(self):  # pragma: no cover
        return VotingPolicy.make_one(self.boto3_raw_data["VotingPolicy"])

    @cached_property
    def MemberConfiguration(self):  # pragma: no cover
        return MemberConfiguration.make_one(self.boto3_raw_data["MemberConfiguration"])

    Description = field("Description")

    @cached_property
    def FrameworkConfiguration(self):  # pragma: no cover
        return NetworkFrameworkConfiguration.make_one(
            self.boto3_raw_data["FrameworkConfiguration"]
        )

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNetworkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNetworkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemberOutput:
    boto3_raw_data: "type_defs.GetMemberOutputTypeDef" = dataclasses.field()

    @cached_property
    def Member(self):  # pragma: no cover
        return Member.make_one(self.boto3_raw_data["Member"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMemberOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetMemberOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNodeInput:
    boto3_raw_data: "type_defs.CreateNodeInputTypeDef" = dataclasses.field()

    ClientRequestToken = field("ClientRequestToken")
    NetworkId = field("NetworkId")

    @cached_property
    def NodeConfiguration(self):  # pragma: no cover
        return NodeConfiguration.make_one(self.boto3_raw_data["NodeConfiguration"])

    MemberId = field("MemberId")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateNodeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateNodeInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNodeOutput:
    boto3_raw_data: "type_defs.GetNodeOutputTypeDef" = dataclasses.field()

    @cached_property
    def Node(self):  # pragma: no cover
        return Node.make_one(self.boto3_raw_data["Node"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetNodeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetNodeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
