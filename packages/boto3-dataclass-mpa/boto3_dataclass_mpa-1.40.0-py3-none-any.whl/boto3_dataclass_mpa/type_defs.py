# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mpa import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class MofNApprovalStrategy:
    boto3_raw_data: "type_defs.MofNApprovalStrategyTypeDef" = dataclasses.field()

    MinApprovalsRequired = field("MinApprovalsRequired")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MofNApprovalStrategyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MofNApprovalStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApprovalTeamRequestApprover:
    boto3_raw_data: "type_defs.ApprovalTeamRequestApproverTypeDef" = dataclasses.field()

    PrimaryIdentityId = field("PrimaryIdentityId")
    PrimaryIdentitySourceArn = field("PrimaryIdentitySourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApprovalTeamRequestApproverTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApprovalTeamRequestApproverTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelSessionRequest:
    boto3_raw_data: "type_defs.CancelSessionRequestTypeDef" = dataclasses.field()

    SessionArn = field("SessionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyReference:
    boto3_raw_data: "type_defs.PolicyReferenceTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyReferenceTypeDef"]],
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
class DeleteIdentitySourceRequest:
    boto3_raw_data: "type_defs.DeleteIdentitySourceRequestTypeDef" = dataclasses.field()

    IdentitySourceArn = field("IdentitySourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdentitySourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentitySourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInactiveApprovalTeamVersionRequest:
    boto3_raw_data: "type_defs.DeleteInactiveApprovalTeamVersionRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    VersionId = field("VersionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteInactiveApprovalTeamVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInactiveApprovalTeamVersionRequestTypeDef"]
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

    FieldName = field("FieldName")
    Operator = field("Operator")
    Value = field("Value")

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
class GetApprovalTeamRequest:
    boto3_raw_data: "type_defs.GetApprovalTeamRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApprovalTeamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApprovalTeamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApprovalTeamResponseApprover:
    boto3_raw_data: "type_defs.GetApprovalTeamResponseApproverTypeDef" = (
        dataclasses.field()
    )

    ApproverId = field("ApproverId")
    ResponseTime = field("ResponseTime")
    PrimaryIdentityId = field("PrimaryIdentityId")
    PrimaryIdentitySourceArn = field("PrimaryIdentitySourceArn")
    PrimaryIdentityStatus = field("PrimaryIdentityStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetApprovalTeamResponseApproverTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApprovalTeamResponseApproverTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentitySourceRequest:
    boto3_raw_data: "type_defs.GetIdentitySourceRequestTypeDef" = dataclasses.field()

    IdentitySourceArn = field("IdentitySourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdentitySourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentitySourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyVersionRequest:
    boto3_raw_data: "type_defs.GetPolicyVersionRequestTypeDef" = dataclasses.field()

    PolicyVersionArn = field("PolicyVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyVersion:
    boto3_raw_data: "type_defs.PolicyVersionTypeDef" = dataclasses.field()

    Arn = field("Arn")
    PolicyArn = field("PolicyArn")
    VersionId = field("VersionId")
    PolicyType = field("PolicyType")
    IsDefault = field("IsDefault")
    Name = field("Name")
    Status = field("Status")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")
    Document = field("Document")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyRequest:
    boto3_raw_data: "type_defs.GetResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    PolicyName = field("PolicyName")
    PolicyType = field("PolicyType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionRequest:
    boto3_raw_data: "type_defs.GetSessionRequestTypeDef" = dataclasses.field()

    SessionArn = field("SessionArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSessionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionResponseApproverResponse:
    boto3_raw_data: "type_defs.GetSessionResponseApproverResponseTypeDef" = (
        dataclasses.field()
    )

    ApproverId = field("ApproverId")
    IdentitySourceArn = field("IdentitySourceArn")
    IdentityId = field("IdentityId")
    Response = field("Response")
    ResponseTime = field("ResponseTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSessionResponseApproverResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionResponseApproverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamIdentityCenterForGet:
    boto3_raw_data: "type_defs.IamIdentityCenterForGetTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    ApprovalPortalUrl = field("ApprovalPortalUrl")
    Region = field("Region")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamIdentityCenterForGetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamIdentityCenterForGetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamIdentityCenterForList:
    boto3_raw_data: "type_defs.IamIdentityCenterForListTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    ApprovalPortalUrl = field("ApprovalPortalUrl")
    Region = field("Region")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamIdentityCenterForListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamIdentityCenterForListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamIdentityCenter:
    boto3_raw_data: "type_defs.IamIdentityCenterTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IamIdentityCenterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamIdentityCenterTypeDef"]
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
class ListApprovalTeamsRequest:
    boto3_raw_data: "type_defs.ListApprovalTeamsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApprovalTeamsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApprovalTeamsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentitySourcesRequest:
    boto3_raw_data: "type_defs.ListIdentitySourcesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentitySourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitySourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesRequest:
    boto3_raw_data: "type_defs.ListPoliciesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Policy:
    boto3_raw_data: "type_defs.PolicyTypeDef" = dataclasses.field()

    Arn = field("Arn")
    DefaultVersion = field("DefaultVersion")
    PolicyType = field("PolicyType")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyVersionsRequest:
    boto3_raw_data: "type_defs.ListPolicyVersionsRequestTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyVersionSummary:
    boto3_raw_data: "type_defs.PolicyVersionSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    PolicyArn = field("PolicyArn")
    VersionId = field("VersionId")
    PolicyType = field("PolicyType")
    IsDefault = field("IsDefault")
    Name = field("Name")
    Status = field("Status")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcePoliciesRequest:
    boto3_raw_data: "type_defs.ListResourcePoliciesRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourcePoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcePoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcePoliciesResponseResourcePolicy:
    boto3_raw_data: "type_defs.ListResourcePoliciesResponseResourcePolicyTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")
    PolicyType = field("PolicyType")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourcePoliciesResponseResourcePolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcePoliciesResponseResourcePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsResponseSession:
    boto3_raw_data: "type_defs.ListSessionsResponseSessionTypeDef" = dataclasses.field()

    SessionArn = field("SessionArn")
    ApprovalTeamName = field("ApprovalTeamName")
    ApprovalTeamArn = field("ApprovalTeamArn")
    InitiationTime = field("InitiationTime")
    ExpirationTime = field("ExpirationTime")
    CompletionTime = field("CompletionTime")
    Description = field("Description")
    ActionName = field("ActionName")
    ProtectedResourceArn = field("ProtectedResourceArn")
    RequesterServicePrincipal = field("RequesterServicePrincipal")
    RequesterPrincipalArn = field("RequesterPrincipalArn")
    RequesterRegion = field("RequesterRegion")
    RequesterAccountId = field("RequesterAccountId")
    Status = field("Status")
    StatusCode = field("StatusCode")
    StatusMessage = field("StatusMessage")
    ActionCompletionStrategy = field("ActionCompletionStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsResponseSessionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsResponseSessionTypeDef"]
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
class StartActiveApprovalTeamDeletionRequest:
    boto3_raw_data: "type_defs.StartActiveApprovalTeamDeletionRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    PendingWindowDays = field("PendingWindowDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartActiveApprovalTeamDeletionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartActiveApprovalTeamDeletionRequestTypeDef"]
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
class ApprovalStrategyResponse:
    boto3_raw_data: "type_defs.ApprovalStrategyResponseTypeDef" = dataclasses.field()

    @cached_property
    def MofN(self):  # pragma: no cover
        return MofNApprovalStrategy.make_one(self.boto3_raw_data["MofN"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApprovalStrategyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApprovalStrategyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApprovalStrategy:
    boto3_raw_data: "type_defs.ApprovalStrategyTypeDef" = dataclasses.field()

    @cached_property
    def MofN(self):  # pragma: no cover
        return MofNApprovalStrategy.make_one(self.boto3_raw_data["MofN"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApprovalStrategyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApprovalStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApprovalTeamResponse:
    boto3_raw_data: "type_defs.CreateApprovalTeamResponseTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    Arn = field("Arn")
    Name = field("Name")
    VersionId = field("VersionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApprovalTeamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApprovalTeamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdentitySourceResponse:
    boto3_raw_data: "type_defs.CreateIdentitySourceResponseTypeDef" = (
        dataclasses.field()
    )

    IdentitySourceType = field("IdentitySourceType")
    IdentitySourceArn = field("IdentitySourceArn")
    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIdentitySourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentitySourceResponseTypeDef"]
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
class GetResourcePolicyResponse:
    boto3_raw_data: "type_defs.GetResourcePolicyResponseTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    PolicyType = field("PolicyType")
    PolicyVersionArn = field("PolicyVersionArn")
    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyResponseTypeDef"]
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
class StartActiveApprovalTeamDeletionResponse:
    boto3_raw_data: "type_defs.StartActiveApprovalTeamDeletionResponseTypeDef" = (
        dataclasses.field()
    )

    DeletionCompletionTime = field("DeletionCompletionTime")
    DeletionStartTime = field("DeletionStartTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartActiveApprovalTeamDeletionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartActiveApprovalTeamDeletionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApprovalTeamResponse:
    boto3_raw_data: "type_defs.UpdateApprovalTeamResponseTypeDef" = dataclasses.field()

    VersionId = field("VersionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApprovalTeamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApprovalTeamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsRequest:
    boto3_raw_data: "type_defs.ListSessionsRequestTypeDef" = dataclasses.field()

    ApprovalTeamArn = field("ApprovalTeamArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyVersionResponse:
    boto3_raw_data: "type_defs.GetPolicyVersionResponseTypeDef" = dataclasses.field()

    @cached_property
    def PolicyVersion(self):  # pragma: no cover
        return PolicyVersion.make_one(self.boto3_raw_data["PolicyVersion"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentitySourceParametersForGet:
    boto3_raw_data: "type_defs.IdentitySourceParametersForGetTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IamIdentityCenter(self):  # pragma: no cover
        return IamIdentityCenterForGet.make_one(
            self.boto3_raw_data["IamIdentityCenter"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdentitySourceParametersForGetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentitySourceParametersForGetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentitySourceParametersForList:
    boto3_raw_data: "type_defs.IdentitySourceParametersForListTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IamIdentityCenter(self):  # pragma: no cover
        return IamIdentityCenterForList.make_one(
            self.boto3_raw_data["IamIdentityCenter"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdentitySourceParametersForListTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentitySourceParametersForListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentitySourceParameters:
    boto3_raw_data: "type_defs.IdentitySourceParametersTypeDef" = dataclasses.field()

    @cached_property
    def IamIdentityCenter(self):  # pragma: no cover
        return IamIdentityCenter.make_one(self.boto3_raw_data["IamIdentityCenter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentitySourceParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentitySourceParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApprovalTeamsRequestPaginate:
    boto3_raw_data: "type_defs.ListApprovalTeamsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApprovalTeamsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApprovalTeamsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentitySourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListIdentitySourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdentitySourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitySourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListPoliciesRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListPolicyVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPolicyVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcePoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListResourcePoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourcePoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcePoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSessionsRequestPaginateTypeDef" = dataclasses.field()

    ApprovalTeamArn = field("ApprovalTeamArn")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesResponse:
    boto3_raw_data: "type_defs.ListPoliciesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Policies(self):  # pragma: no cover
        return Policy.make_many(self.boto3_raw_data["Policies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyVersionsResponse:
    boto3_raw_data: "type_defs.ListPolicyVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def PolicyVersions(self):  # pragma: no cover
        return PolicyVersionSummary.make_many(self.boto3_raw_data["PolicyVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcePoliciesResponse:
    boto3_raw_data: "type_defs.ListResourcePoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourcePolicies(self):  # pragma: no cover
        return ListResourcePoliciesResponseResourcePolicy.make_many(
            self.boto3_raw_data["ResourcePolicies"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourcePoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcePoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsResponse:
    boto3_raw_data: "type_defs.ListSessionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Sessions(self):  # pragma: no cover
        return ListSessionsResponseSession.make_many(self.boto3_raw_data["Sessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionResponse:
    boto3_raw_data: "type_defs.GetSessionResponseTypeDef" = dataclasses.field()

    SessionArn = field("SessionArn")
    ApprovalTeamArn = field("ApprovalTeamArn")
    ApprovalTeamName = field("ApprovalTeamName")
    ProtectedResourceArn = field("ProtectedResourceArn")

    @cached_property
    def ApprovalStrategy(self):  # pragma: no cover
        return ApprovalStrategyResponse.make_one(
            self.boto3_raw_data["ApprovalStrategy"]
        )

    NumberOfApprovers = field("NumberOfApprovers")
    InitiationTime = field("InitiationTime")
    ExpirationTime = field("ExpirationTime")
    CompletionTime = field("CompletionTime")
    Description = field("Description")
    Metadata = field("Metadata")
    Status = field("Status")
    StatusCode = field("StatusCode")
    StatusMessage = field("StatusMessage")
    ExecutionStatus = field("ExecutionStatus")
    ActionName = field("ActionName")
    RequesterServicePrincipal = field("RequesterServicePrincipal")
    RequesterPrincipalArn = field("RequesterPrincipalArn")
    RequesterAccountId = field("RequesterAccountId")
    RequesterRegion = field("RequesterRegion")
    RequesterComment = field("RequesterComment")
    ActionCompletionStrategy = field("ActionCompletionStrategy")

    @cached_property
    def ApproverResponses(self):  # pragma: no cover
        return GetSessionResponseApproverResponse.make_many(
            self.boto3_raw_data["ApproverResponses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApprovalTeamsResponseApprovalTeam:
    boto3_raw_data: "type_defs.ListApprovalTeamsResponseApprovalTeamTypeDef" = (
        dataclasses.field()
    )

    CreationTime = field("CreationTime")

    @cached_property
    def ApprovalStrategy(self):  # pragma: no cover
        return ApprovalStrategyResponse.make_one(
            self.boto3_raw_data["ApprovalStrategy"]
        )

    NumberOfApprovers = field("NumberOfApprovers")
    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    Status = field("Status")
    StatusCode = field("StatusCode")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApprovalTeamsResponseApprovalTeamTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApprovalTeamsResponseApprovalTeamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingUpdate:
    boto3_raw_data: "type_defs.PendingUpdateTypeDef" = dataclasses.field()

    VersionId = field("VersionId")
    Description = field("Description")

    @cached_property
    def ApprovalStrategy(self):  # pragma: no cover
        return ApprovalStrategyResponse.make_one(
            self.boto3_raw_data["ApprovalStrategy"]
        )

    NumberOfApprovers = field("NumberOfApprovers")
    Status = field("Status")
    StatusCode = field("StatusCode")
    StatusMessage = field("StatusMessage")

    @cached_property
    def Approvers(self):  # pragma: no cover
        return GetApprovalTeamResponseApprover.make_many(
            self.boto3_raw_data["Approvers"]
        )

    UpdateInitiationTime = field("UpdateInitiationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PendingUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PendingUpdateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApprovalTeamRequest:
    boto3_raw_data: "type_defs.CreateApprovalTeamRequestTypeDef" = dataclasses.field()

    @cached_property
    def ApprovalStrategy(self):  # pragma: no cover
        return ApprovalStrategy.make_one(self.boto3_raw_data["ApprovalStrategy"])

    @cached_property
    def Approvers(self):  # pragma: no cover
        return ApprovalTeamRequestApprover.make_many(self.boto3_raw_data["Approvers"])

    Description = field("Description")

    @cached_property
    def Policies(self):  # pragma: no cover
        return PolicyReference.make_many(self.boto3_raw_data["Policies"])

    Name = field("Name")
    ClientToken = field("ClientToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApprovalTeamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApprovalTeamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApprovalTeamRequest:
    boto3_raw_data: "type_defs.UpdateApprovalTeamRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ApprovalStrategy(self):  # pragma: no cover
        return ApprovalStrategy.make_one(self.boto3_raw_data["ApprovalStrategy"])

    @cached_property
    def Approvers(self):  # pragma: no cover
        return ApprovalTeamRequestApprover.make_many(self.boto3_raw_data["Approvers"])

    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApprovalTeamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApprovalTeamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentitySourceResponse:
    boto3_raw_data: "type_defs.GetIdentitySourceResponseTypeDef" = dataclasses.field()

    IdentitySourceType = field("IdentitySourceType")

    @cached_property
    def IdentitySourceParameters(self):  # pragma: no cover
        return IdentitySourceParametersForGet.make_one(
            self.boto3_raw_data["IdentitySourceParameters"]
        )

    IdentitySourceArn = field("IdentitySourceArn")
    CreationTime = field("CreationTime")
    Status = field("Status")
    StatusCode = field("StatusCode")
    StatusMessage = field("StatusMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdentitySourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentitySourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentitySourceForList:
    boto3_raw_data: "type_defs.IdentitySourceForListTypeDef" = dataclasses.field()

    IdentitySourceType = field("IdentitySourceType")

    @cached_property
    def IdentitySourceParameters(self):  # pragma: no cover
        return IdentitySourceParametersForList.make_one(
            self.boto3_raw_data["IdentitySourceParameters"]
        )

    IdentitySourceArn = field("IdentitySourceArn")
    CreationTime = field("CreationTime")
    Status = field("Status")
    StatusCode = field("StatusCode")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentitySourceForListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentitySourceForListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdentitySourceRequest:
    boto3_raw_data: "type_defs.CreateIdentitySourceRequestTypeDef" = dataclasses.field()

    @cached_property
    def IdentitySourceParameters(self):  # pragma: no cover
        return IdentitySourceParameters.make_one(
            self.boto3_raw_data["IdentitySourceParameters"]
        )

    ClientToken = field("ClientToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIdentitySourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentitySourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApprovalTeamsResponse:
    boto3_raw_data: "type_defs.ListApprovalTeamsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApprovalTeams(self):  # pragma: no cover
        return ListApprovalTeamsResponseApprovalTeam.make_many(
            self.boto3_raw_data["ApprovalTeams"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApprovalTeamsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApprovalTeamsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApprovalTeamResponse:
    boto3_raw_data: "type_defs.GetApprovalTeamResponseTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")

    @cached_property
    def ApprovalStrategy(self):  # pragma: no cover
        return ApprovalStrategyResponse.make_one(
            self.boto3_raw_data["ApprovalStrategy"]
        )

    NumberOfApprovers = field("NumberOfApprovers")

    @cached_property
    def Approvers(self):  # pragma: no cover
        return GetApprovalTeamResponseApprover.make_many(
            self.boto3_raw_data["Approvers"]
        )

    Arn = field("Arn")
    Description = field("Description")
    Name = field("Name")
    Status = field("Status")
    StatusCode = field("StatusCode")
    StatusMessage = field("StatusMessage")
    UpdateSessionArn = field("UpdateSessionArn")
    VersionId = field("VersionId")

    @cached_property
    def Policies(self):  # pragma: no cover
        return PolicyReference.make_many(self.boto3_raw_data["Policies"])

    LastUpdateTime = field("LastUpdateTime")

    @cached_property
    def PendingUpdate(self):  # pragma: no cover
        return PendingUpdate.make_one(self.boto3_raw_data["PendingUpdate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApprovalTeamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApprovalTeamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentitySourcesResponse:
    boto3_raw_data: "type_defs.ListIdentitySourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def IdentitySources(self):  # pragma: no cover
        return IdentitySourceForList.make_many(self.boto3_raw_data["IdentitySources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentitySourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitySourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
