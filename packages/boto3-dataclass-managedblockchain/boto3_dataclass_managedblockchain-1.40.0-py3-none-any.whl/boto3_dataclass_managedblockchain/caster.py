# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_managedblockchain import type_defs as bs_td


class MANAGEDBLOCKCHAINCaster:

    def create_accessor(
        self,
        res: "bs_td.CreateAccessorOutputTypeDef",
    ) -> "dc_td.CreateAccessorOutput":
        return dc_td.CreateAccessorOutput.make_one(res)

    def create_member(
        self,
        res: "bs_td.CreateMemberOutputTypeDef",
    ) -> "dc_td.CreateMemberOutput":
        return dc_td.CreateMemberOutput.make_one(res)

    def create_network(
        self,
        res: "bs_td.CreateNetworkOutputTypeDef",
    ) -> "dc_td.CreateNetworkOutput":
        return dc_td.CreateNetworkOutput.make_one(res)

    def create_node(
        self,
        res: "bs_td.CreateNodeOutputTypeDef",
    ) -> "dc_td.CreateNodeOutput":
        return dc_td.CreateNodeOutput.make_one(res)

    def create_proposal(
        self,
        res: "bs_td.CreateProposalOutputTypeDef",
    ) -> "dc_td.CreateProposalOutput":
        return dc_td.CreateProposalOutput.make_one(res)

    def get_accessor(
        self,
        res: "bs_td.GetAccessorOutputTypeDef",
    ) -> "dc_td.GetAccessorOutput":
        return dc_td.GetAccessorOutput.make_one(res)

    def get_member(
        self,
        res: "bs_td.GetMemberOutputTypeDef",
    ) -> "dc_td.GetMemberOutput":
        return dc_td.GetMemberOutput.make_one(res)

    def get_network(
        self,
        res: "bs_td.GetNetworkOutputTypeDef",
    ) -> "dc_td.GetNetworkOutput":
        return dc_td.GetNetworkOutput.make_one(res)

    def get_node(
        self,
        res: "bs_td.GetNodeOutputTypeDef",
    ) -> "dc_td.GetNodeOutput":
        return dc_td.GetNodeOutput.make_one(res)

    def get_proposal(
        self,
        res: "bs_td.GetProposalOutputTypeDef",
    ) -> "dc_td.GetProposalOutput":
        return dc_td.GetProposalOutput.make_one(res)

    def list_accessors(
        self,
        res: "bs_td.ListAccessorsOutputTypeDef",
    ) -> "dc_td.ListAccessorsOutput":
        return dc_td.ListAccessorsOutput.make_one(res)

    def list_invitations(
        self,
        res: "bs_td.ListInvitationsOutputTypeDef",
    ) -> "dc_td.ListInvitationsOutput":
        return dc_td.ListInvitationsOutput.make_one(res)

    def list_members(
        self,
        res: "bs_td.ListMembersOutputTypeDef",
    ) -> "dc_td.ListMembersOutput":
        return dc_td.ListMembersOutput.make_one(res)

    def list_networks(
        self,
        res: "bs_td.ListNetworksOutputTypeDef",
    ) -> "dc_td.ListNetworksOutput":
        return dc_td.ListNetworksOutput.make_one(res)

    def list_nodes(
        self,
        res: "bs_td.ListNodesOutputTypeDef",
    ) -> "dc_td.ListNodesOutput":
        return dc_td.ListNodesOutput.make_one(res)

    def list_proposal_votes(
        self,
        res: "bs_td.ListProposalVotesOutputTypeDef",
    ) -> "dc_td.ListProposalVotesOutput":
        return dc_td.ListProposalVotesOutput.make_one(res)

    def list_proposals(
        self,
        res: "bs_td.ListProposalsOutputTypeDef",
    ) -> "dc_td.ListProposalsOutput":
        return dc_td.ListProposalsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)


managedblockchain_caster = MANAGEDBLOCKCHAINCaster()
