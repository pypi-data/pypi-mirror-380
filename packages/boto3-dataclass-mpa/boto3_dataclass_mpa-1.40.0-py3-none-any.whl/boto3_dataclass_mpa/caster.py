# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mpa import type_defs as bs_td


class MPACaster:

    def create_approval_team(
        self,
        res: "bs_td.CreateApprovalTeamResponseTypeDef",
    ) -> "dc_td.CreateApprovalTeamResponse":
        return dc_td.CreateApprovalTeamResponse.make_one(res)

    def create_identity_source(
        self,
        res: "bs_td.CreateIdentitySourceResponseTypeDef",
    ) -> "dc_td.CreateIdentitySourceResponse":
        return dc_td.CreateIdentitySourceResponse.make_one(res)

    def delete_identity_source(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_approval_team(
        self,
        res: "bs_td.GetApprovalTeamResponseTypeDef",
    ) -> "dc_td.GetApprovalTeamResponse":
        return dc_td.GetApprovalTeamResponse.make_one(res)

    def get_identity_source(
        self,
        res: "bs_td.GetIdentitySourceResponseTypeDef",
    ) -> "dc_td.GetIdentitySourceResponse":
        return dc_td.GetIdentitySourceResponse.make_one(res)

    def get_policy_version(
        self,
        res: "bs_td.GetPolicyVersionResponseTypeDef",
    ) -> "dc_td.GetPolicyVersionResponse":
        return dc_td.GetPolicyVersionResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def get_session(
        self,
        res: "bs_td.GetSessionResponseTypeDef",
    ) -> "dc_td.GetSessionResponse":
        return dc_td.GetSessionResponse.make_one(res)

    def list_approval_teams(
        self,
        res: "bs_td.ListApprovalTeamsResponseTypeDef",
    ) -> "dc_td.ListApprovalTeamsResponse":
        return dc_td.ListApprovalTeamsResponse.make_one(res)

    def list_identity_sources(
        self,
        res: "bs_td.ListIdentitySourcesResponseTypeDef",
    ) -> "dc_td.ListIdentitySourcesResponse":
        return dc_td.ListIdentitySourcesResponse.make_one(res)

    def list_policies(
        self,
        res: "bs_td.ListPoliciesResponseTypeDef",
    ) -> "dc_td.ListPoliciesResponse":
        return dc_td.ListPoliciesResponse.make_one(res)

    def list_policy_versions(
        self,
        res: "bs_td.ListPolicyVersionsResponseTypeDef",
    ) -> "dc_td.ListPolicyVersionsResponse":
        return dc_td.ListPolicyVersionsResponse.make_one(res)

    def list_resource_policies(
        self,
        res: "bs_td.ListResourcePoliciesResponseTypeDef",
    ) -> "dc_td.ListResourcePoliciesResponse":
        return dc_td.ListResourcePoliciesResponse.make_one(res)

    def list_sessions(
        self,
        res: "bs_td.ListSessionsResponseTypeDef",
    ) -> "dc_td.ListSessionsResponse":
        return dc_td.ListSessionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_active_approval_team_deletion(
        self,
        res: "bs_td.StartActiveApprovalTeamDeletionResponseTypeDef",
    ) -> "dc_td.StartActiveApprovalTeamDeletionResponse":
        return dc_td.StartActiveApprovalTeamDeletionResponse.make_one(res)

    def update_approval_team(
        self,
        res: "bs_td.UpdateApprovalTeamResponseTypeDef",
    ) -> "dc_td.UpdateApprovalTeamResponse":
        return dc_td.UpdateApprovalTeamResponse.make_one(res)


mpa_caster = MPACaster()
