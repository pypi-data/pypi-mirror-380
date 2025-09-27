# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_grafana import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssertionAttributes:
    boto3_raw_data: "type_defs.AssertionAttributesTypeDef" = dataclasses.field()

    email = field("email")
    groups = field("groups")
    login = field("login")
    name = field("name")
    org = field("org")
    role = field("role")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssertionAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssertionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateLicenseRequest:
    boto3_raw_data: "type_defs.AssociateLicenseRequestTypeDef" = dataclasses.field()

    licenseType = field("licenseType")
    workspaceId = field("workspaceId")
    grafanaToken = field("grafanaToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateLicenseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateLicenseRequestTypeDef"]
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
class AwsSsoAuthentication:
    boto3_raw_data: "type_defs.AwsSsoAuthenticationTypeDef" = dataclasses.field()

    ssoClientId = field("ssoClientId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsSsoAuthenticationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsSsoAuthenticationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationSummary:
    boto3_raw_data: "type_defs.AuthenticationSummaryTypeDef" = dataclasses.field()

    providers = field("providers")
    samlConfigurationStatus = field("samlConfigurationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceApiKeyRequest:
    boto3_raw_data: "type_defs.CreateWorkspaceApiKeyRequestTypeDef" = (
        dataclasses.field()
    )

    keyName = field("keyName")
    keyRole = field("keyRole")
    secondsToLive = field("secondsToLive")
    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspaceApiKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceApiKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceServiceAccountRequest:
    boto3_raw_data: "type_defs.CreateWorkspaceServiceAccountRequestTypeDef" = (
        dataclasses.field()
    )

    grafanaRole = field("grafanaRole")
    name = field("name")
    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateWorkspaceServiceAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceServiceAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceServiceAccountTokenRequest:
    boto3_raw_data: "type_defs.CreateWorkspaceServiceAccountTokenRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    secondsToLive = field("secondsToLive")
    serviceAccountId = field("serviceAccountId")
    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateWorkspaceServiceAccountTokenRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceServiceAccountTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceAccountTokenSummaryWithKey:
    boto3_raw_data: "type_defs.ServiceAccountTokenSummaryWithKeyTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    key = field("key")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceAccountTokenSummaryWithKeyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceAccountTokenSummaryWithKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceApiKeyRequest:
    boto3_raw_data: "type_defs.DeleteWorkspaceApiKeyRequestTypeDef" = (
        dataclasses.field()
    )

    keyName = field("keyName")
    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkspaceApiKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceApiKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceRequest:
    boto3_raw_data: "type_defs.DeleteWorkspaceRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceServiceAccountRequest:
    boto3_raw_data: "type_defs.DeleteWorkspaceServiceAccountRequestTypeDef" = (
        dataclasses.field()
    )

    serviceAccountId = field("serviceAccountId")
    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteWorkspaceServiceAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceServiceAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceServiceAccountTokenRequest:
    boto3_raw_data: "type_defs.DeleteWorkspaceServiceAccountTokenRequestTypeDef" = (
        dataclasses.field()
    )

    serviceAccountId = field("serviceAccountId")
    tokenId = field("tokenId")
    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteWorkspaceServiceAccountTokenRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceServiceAccountTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceAuthenticationRequest:
    boto3_raw_data: "type_defs.DescribeWorkspaceAuthenticationRequestTypeDef" = (
        dataclasses.field()
    )

    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceAuthenticationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceAuthenticationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeWorkspaceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceRequest:
    boto3_raw_data: "type_defs.DescribeWorkspaceRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateLicenseRequest:
    boto3_raw_data: "type_defs.DisassociateLicenseRequestTypeDef" = dataclasses.field()

    licenseType = field("licenseType")
    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateLicenseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateLicenseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdpMetadata:
    boto3_raw_data: "type_defs.IdpMetadataTypeDef" = dataclasses.field()

    url = field("url")
    xml = field("xml")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdpMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdpMetadataTypeDef"]]
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
class ListPermissionsRequest:
    boto3_raw_data: "type_defs.ListPermissionsRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    groupId = field("groupId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    userId = field("userId")
    userType = field("userType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPermissionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionsRequestTypeDef"]
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
class ListVersionsRequest:
    boto3_raw_data: "type_defs.ListVersionsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspaceServiceAccountTokensRequest:
    boto3_raw_data: "type_defs.ListWorkspaceServiceAccountTokensRequestTypeDef" = (
        dataclasses.field()
    )

    serviceAccountId = field("serviceAccountId")
    workspaceId = field("workspaceId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkspaceServiceAccountTokensRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspaceServiceAccountTokensRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceAccountTokenSummary:
    boto3_raw_data: "type_defs.ServiceAccountTokenSummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    expiresAt = field("expiresAt")
    id = field("id")
    name = field("name")
    lastUsedAt = field("lastUsedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceAccountTokenSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceAccountTokenSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspaceServiceAccountsRequest:
    boto3_raw_data: "type_defs.ListWorkspaceServiceAccountsRequestTypeDef" = (
        dataclasses.field()
    )

    workspaceId = field("workspaceId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkspaceServiceAccountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspaceServiceAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceAccountSummary:
    boto3_raw_data: "type_defs.ServiceAccountSummaryTypeDef" = dataclasses.field()

    grafanaRole = field("grafanaRole")
    id = field("id")
    isDisabled = field("isDisabled")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceAccountSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceAccountSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspacesRequest:
    boto3_raw_data: "type_defs.ListWorkspacesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkspacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAccessConfigurationOutput:
    boto3_raw_data: "type_defs.NetworkAccessConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    prefixListIds = field("prefixListIds")
    vpceIds = field("vpceIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NetworkAccessConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAccessConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAccessConfiguration:
    boto3_raw_data: "type_defs.NetworkAccessConfigurationTypeDef" = dataclasses.field()

    prefixListIds = field("prefixListIds")
    vpceIds = field("vpceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkAccessConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAccessConfigurationTypeDef"]
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

    id = field("id")
    type = field("type")

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
class RoleValuesOutput:
    boto3_raw_data: "type_defs.RoleValuesOutputTypeDef" = dataclasses.field()

    admin = field("admin")
    editor = field("editor")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoleValuesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoleValuesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoleValues:
    boto3_raw_data: "type_defs.RoleValuesTypeDef" = dataclasses.field()

    admin = field("admin")
    editor = field("editor")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoleValuesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoleValuesTypeDef"]]
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
class UpdateWorkspaceConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateWorkspaceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    configuration = field("configuration")
    workspaceId = field("workspaceId")
    grafanaVersion = field("grafanaVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateWorkspaceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspaceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigurationOutput:
    boto3_raw_data: "type_defs.VpcConfigurationOutputTypeDef" = dataclasses.field()

    securityGroupIds = field("securityGroupIds")
    subnetIds = field("subnetIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfiguration:
    boto3_raw_data: "type_defs.VpcConfigurationTypeDef" = dataclasses.field()

    securityGroupIds = field("securityGroupIds")
    subnetIds = field("subnetIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceApiKeyResponse:
    boto3_raw_data: "type_defs.CreateWorkspaceApiKeyResponseTypeDef" = (
        dataclasses.field()
    )

    key = field("key")
    keyName = field("keyName")
    workspaceId = field("workspaceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkspaceApiKeyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceApiKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceServiceAccountResponse:
    boto3_raw_data: "type_defs.CreateWorkspaceServiceAccountResponseTypeDef" = (
        dataclasses.field()
    )

    grafanaRole = field("grafanaRole")
    id = field("id")
    name = field("name")
    workspaceId = field("workspaceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateWorkspaceServiceAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceServiceAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceApiKeyResponse:
    boto3_raw_data: "type_defs.DeleteWorkspaceApiKeyResponseTypeDef" = (
        dataclasses.field()
    )

    keyName = field("keyName")
    workspaceId = field("workspaceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteWorkspaceApiKeyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceApiKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceServiceAccountResponse:
    boto3_raw_data: "type_defs.DeleteWorkspaceServiceAccountResponseTypeDef" = (
        dataclasses.field()
    )

    serviceAccountId = field("serviceAccountId")
    workspaceId = field("workspaceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteWorkspaceServiceAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceServiceAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceServiceAccountTokenResponse:
    boto3_raw_data: "type_defs.DeleteWorkspaceServiceAccountTokenResponseTypeDef" = (
        dataclasses.field()
    )

    serviceAccountId = field("serviceAccountId")
    tokenId = field("tokenId")
    workspaceId = field("workspaceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteWorkspaceServiceAccountTokenResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceServiceAccountTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeWorkspaceConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    configuration = field("configuration")
    grafanaVersion = field("grafanaVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceConfigurationResponseTypeDef"]
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
class ListVersionsResponse:
    boto3_raw_data: "type_defs.ListVersionsResponseTypeDef" = dataclasses.field()

    grafanaVersions = field("grafanaVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceSummary:
    boto3_raw_data: "type_defs.WorkspaceSummaryTypeDef" = dataclasses.field()

    @cached_property
    def authentication(self):  # pragma: no cover
        return AuthenticationSummary.make_one(self.boto3_raw_data["authentication"])

    created = field("created")
    endpoint = field("endpoint")
    grafanaVersion = field("grafanaVersion")
    id = field("id")
    modified = field("modified")
    status = field("status")
    description = field("description")
    grafanaToken = field("grafanaToken")
    licenseType = field("licenseType")
    name = field("name")
    notificationDestinations = field("notificationDestinations")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkspaceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceServiceAccountTokenResponse:
    boto3_raw_data: "type_defs.CreateWorkspaceServiceAccountTokenResponseTypeDef" = (
        dataclasses.field()
    )

    serviceAccountId = field("serviceAccountId")

    @cached_property
    def serviceAccountToken(self):  # pragma: no cover
        return ServiceAccountTokenSummaryWithKey.make_one(
            self.boto3_raw_data["serviceAccountToken"]
        )

    workspaceId = field("workspaceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateWorkspaceServiceAccountTokenResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceServiceAccountTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionsRequestPaginate:
    boto3_raw_data: "type_defs.ListPermissionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    workspaceId = field("workspaceId")
    groupId = field("groupId")
    userId = field("userId")
    userType = field("userType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPermissionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListVersionsRequestPaginateTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVersionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspaceServiceAccountTokensRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListWorkspaceServiceAccountTokensRequestPaginateTypeDef"
    ) = dataclasses.field()

    serviceAccountId = field("serviceAccountId")
    workspaceId = field("workspaceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkspaceServiceAccountTokensRequestPaginateTypeDef"
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
                "type_defs.ListWorkspaceServiceAccountTokensRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspaceServiceAccountsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkspaceServiceAccountsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    workspaceId = field("workspaceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkspaceServiceAccountsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspaceServiceAccountsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspacesRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkspacesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkspacesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspacesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspaceServiceAccountTokensResponse:
    boto3_raw_data: "type_defs.ListWorkspaceServiceAccountTokensResponseTypeDef" = (
        dataclasses.field()
    )

    serviceAccountId = field("serviceAccountId")

    @cached_property
    def serviceAccountTokens(self):  # pragma: no cover
        return ServiceAccountTokenSummary.make_many(
            self.boto3_raw_data["serviceAccountTokens"]
        )

    workspaceId = field("workspaceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkspaceServiceAccountTokensResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspaceServiceAccountTokensResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspaceServiceAccountsResponse:
    boto3_raw_data: "type_defs.ListWorkspaceServiceAccountsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceAccounts(self):  # pragma: no cover
        return ServiceAccountSummary.make_many(self.boto3_raw_data["serviceAccounts"])

    workspaceId = field("workspaceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkspaceServiceAccountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspaceServiceAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionEntry:
    boto3_raw_data: "type_defs.PermissionEntryTypeDef" = dataclasses.field()

    role = field("role")

    @cached_property
    def user(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["user"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PermissionEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstructionOutput:
    boto3_raw_data: "type_defs.UpdateInstructionOutputTypeDef" = dataclasses.field()

    action = field("action")
    role = field("role")

    @cached_property
    def users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["users"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInstructionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInstructionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstruction:
    boto3_raw_data: "type_defs.UpdateInstructionTypeDef" = dataclasses.field()

    action = field("action")
    role = field("role")

    @cached_property
    def users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["users"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateInstructionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInstructionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamlConfigurationOutput:
    boto3_raw_data: "type_defs.SamlConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def idpMetadata(self):  # pragma: no cover
        return IdpMetadata.make_one(self.boto3_raw_data["idpMetadata"])

    allowedOrganizations = field("allowedOrganizations")

    @cached_property
    def assertionAttributes(self):  # pragma: no cover
        return AssertionAttributes.make_one(self.boto3_raw_data["assertionAttributes"])

    loginValidityDuration = field("loginValidityDuration")

    @cached_property
    def roleValues(self):  # pragma: no cover
        return RoleValuesOutput.make_one(self.boto3_raw_data["roleValues"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SamlConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamlConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamlConfiguration:
    boto3_raw_data: "type_defs.SamlConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def idpMetadata(self):  # pragma: no cover
        return IdpMetadata.make_one(self.boto3_raw_data["idpMetadata"])

    allowedOrganizations = field("allowedOrganizations")

    @cached_property
    def assertionAttributes(self):  # pragma: no cover
        return AssertionAttributes.make_one(self.boto3_raw_data["assertionAttributes"])

    loginValidityDuration = field("loginValidityDuration")

    @cached_property
    def roleValues(self):  # pragma: no cover
        return RoleValues.make_one(self.boto3_raw_data["roleValues"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SamlConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamlConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceDescription:
    boto3_raw_data: "type_defs.WorkspaceDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def authentication(self):  # pragma: no cover
        return AuthenticationSummary.make_one(self.boto3_raw_data["authentication"])

    created = field("created")
    dataSources = field("dataSources")
    endpoint = field("endpoint")
    grafanaVersion = field("grafanaVersion")
    id = field("id")
    modified = field("modified")
    status = field("status")
    accountAccessType = field("accountAccessType")
    description = field("description")
    freeTrialConsumed = field("freeTrialConsumed")
    freeTrialExpiration = field("freeTrialExpiration")
    grafanaToken = field("grafanaToken")
    licenseExpiration = field("licenseExpiration")
    licenseType = field("licenseType")
    name = field("name")

    @cached_property
    def networkAccessControl(self):  # pragma: no cover
        return NetworkAccessConfigurationOutput.make_one(
            self.boto3_raw_data["networkAccessControl"]
        )

    notificationDestinations = field("notificationDestinations")
    organizationRoleName = field("organizationRoleName")
    organizationalUnits = field("organizationalUnits")
    permissionType = field("permissionType")
    stackSetName = field("stackSetName")
    tags = field("tags")

    @cached_property
    def vpcConfiguration(self):  # pragma: no cover
        return VpcConfigurationOutput.make_one(self.boto3_raw_data["vpcConfiguration"])

    workspaceRoleArn = field("workspaceRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspaceDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspacesResponse:
    boto3_raw_data: "type_defs.ListWorkspacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def workspaces(self):  # pragma: no cover
        return WorkspaceSummary.make_many(self.boto3_raw_data["workspaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkspacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionsResponse:
    boto3_raw_data: "type_defs.ListPermissionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def permissions(self):  # pragma: no cover
        return PermissionEntry.make_many(self.boto3_raw_data["permissions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPermissionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateError:
    boto3_raw_data: "type_defs.UpdateErrorTypeDef" = dataclasses.field()

    @cached_property
    def causedBy(self):  # pragma: no cover
        return UpdateInstructionOutput.make_one(self.boto3_raw_data["causedBy"])

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamlAuthentication:
    boto3_raw_data: "type_defs.SamlAuthenticationTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def configuration(self):  # pragma: no cover
        return SamlConfigurationOutput.make_one(self.boto3_raw_data["configuration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SamlAuthenticationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamlAuthenticationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateLicenseResponse:
    boto3_raw_data: "type_defs.AssociateLicenseResponseTypeDef" = dataclasses.field()

    @cached_property
    def workspace(self):  # pragma: no cover
        return WorkspaceDescription.make_one(self.boto3_raw_data["workspace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateLicenseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateLicenseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceResponse:
    boto3_raw_data: "type_defs.CreateWorkspaceResponseTypeDef" = dataclasses.field()

    @cached_property
    def workspace(self):  # pragma: no cover
        return WorkspaceDescription.make_one(self.boto3_raw_data["workspace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceResponse:
    boto3_raw_data: "type_defs.DeleteWorkspaceResponseTypeDef" = dataclasses.field()

    @cached_property
    def workspace(self):  # pragma: no cover
        return WorkspaceDescription.make_one(self.boto3_raw_data["workspace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceResponse:
    boto3_raw_data: "type_defs.DescribeWorkspaceResponseTypeDef" = dataclasses.field()

    @cached_property
    def workspace(self):  # pragma: no cover
        return WorkspaceDescription.make_one(self.boto3_raw_data["workspace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateLicenseResponse:
    boto3_raw_data: "type_defs.DisassociateLicenseResponseTypeDef" = dataclasses.field()

    @cached_property
    def workspace(self):  # pragma: no cover
        return WorkspaceDescription.make_one(self.boto3_raw_data["workspace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateLicenseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateLicenseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkspaceResponse:
    boto3_raw_data: "type_defs.UpdateWorkspaceResponseTypeDef" = dataclasses.field()

    @cached_property
    def workspace(self):  # pragma: no cover
        return WorkspaceDescription.make_one(self.boto3_raw_data["workspace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceRequest:
    boto3_raw_data: "type_defs.CreateWorkspaceRequestTypeDef" = dataclasses.field()

    accountAccessType = field("accountAccessType")
    authenticationProviders = field("authenticationProviders")
    permissionType = field("permissionType")
    clientToken = field("clientToken")
    configuration = field("configuration")
    grafanaVersion = field("grafanaVersion")
    networkAccessControl = field("networkAccessControl")
    organizationRoleName = field("organizationRoleName")
    stackSetName = field("stackSetName")
    tags = field("tags")
    vpcConfiguration = field("vpcConfiguration")
    workspaceDataSources = field("workspaceDataSources")
    workspaceDescription = field("workspaceDescription")
    workspaceName = field("workspaceName")
    workspaceNotificationDestinations = field("workspaceNotificationDestinations")
    workspaceOrganizationalUnits = field("workspaceOrganizationalUnits")
    workspaceRoleArn = field("workspaceRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkspaceRequest:
    boto3_raw_data: "type_defs.UpdateWorkspaceRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    accountAccessType = field("accountAccessType")
    networkAccessControl = field("networkAccessControl")
    organizationRoleName = field("organizationRoleName")
    permissionType = field("permissionType")
    removeNetworkAccessConfiguration = field("removeNetworkAccessConfiguration")
    removeVpcConfiguration = field("removeVpcConfiguration")
    stackSetName = field("stackSetName")
    vpcConfiguration = field("vpcConfiguration")
    workspaceDataSources = field("workspaceDataSources")
    workspaceDescription = field("workspaceDescription")
    workspaceName = field("workspaceName")
    workspaceNotificationDestinations = field("workspaceNotificationDestinations")
    workspaceOrganizationalUnits = field("workspaceOrganizationalUnits")
    workspaceRoleArn = field("workspaceRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePermissionsResponse:
    boto3_raw_data: "type_defs.UpdatePermissionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def errors(self):  # pragma: no cover
        return UpdateError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePermissionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePermissionsRequest:
    boto3_raw_data: "type_defs.UpdatePermissionsRequestTypeDef" = dataclasses.field()

    updateInstructionBatch = field("updateInstructionBatch")
    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePermissionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationDescription:
    boto3_raw_data: "type_defs.AuthenticationDescriptionTypeDef" = dataclasses.field()

    providers = field("providers")

    @cached_property
    def awsSso(self):  # pragma: no cover
        return AwsSsoAuthentication.make_one(self.boto3_raw_data["awsSso"])

    @cached_property
    def saml(self):  # pragma: no cover
        return SamlAuthentication.make_one(self.boto3_raw_data["saml"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkspaceAuthenticationRequest:
    boto3_raw_data: "type_defs.UpdateWorkspaceAuthenticationRequestTypeDef" = (
        dataclasses.field()
    )

    authenticationProviders = field("authenticationProviders")
    workspaceId = field("workspaceId")
    samlConfiguration = field("samlConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateWorkspaceAuthenticationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspaceAuthenticationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceAuthenticationResponse:
    boto3_raw_data: "type_defs.DescribeWorkspaceAuthenticationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def authentication(self):  # pragma: no cover
        return AuthenticationDescription.make_one(self.boto3_raw_data["authentication"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceAuthenticationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceAuthenticationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkspaceAuthenticationResponse:
    boto3_raw_data: "type_defs.UpdateWorkspaceAuthenticationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def authentication(self):  # pragma: no cover
        return AuthenticationDescription.make_one(self.boto3_raw_data["authentication"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateWorkspaceAuthenticationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspaceAuthenticationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
