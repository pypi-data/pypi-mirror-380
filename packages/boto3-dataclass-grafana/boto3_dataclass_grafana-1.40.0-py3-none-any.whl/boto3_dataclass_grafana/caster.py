# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_grafana import type_defs as bs_td


class GRAFANACaster:

    def associate_license(
        self,
        res: "bs_td.AssociateLicenseResponseTypeDef",
    ) -> "dc_td.AssociateLicenseResponse":
        return dc_td.AssociateLicenseResponse.make_one(res)

    def create_workspace(
        self,
        res: "bs_td.CreateWorkspaceResponseTypeDef",
    ) -> "dc_td.CreateWorkspaceResponse":
        return dc_td.CreateWorkspaceResponse.make_one(res)

    def create_workspace_api_key(
        self,
        res: "bs_td.CreateWorkspaceApiKeyResponseTypeDef",
    ) -> "dc_td.CreateWorkspaceApiKeyResponse":
        return dc_td.CreateWorkspaceApiKeyResponse.make_one(res)

    def create_workspace_service_account(
        self,
        res: "bs_td.CreateWorkspaceServiceAccountResponseTypeDef",
    ) -> "dc_td.CreateWorkspaceServiceAccountResponse":
        return dc_td.CreateWorkspaceServiceAccountResponse.make_one(res)

    def create_workspace_service_account_token(
        self,
        res: "bs_td.CreateWorkspaceServiceAccountTokenResponseTypeDef",
    ) -> "dc_td.CreateWorkspaceServiceAccountTokenResponse":
        return dc_td.CreateWorkspaceServiceAccountTokenResponse.make_one(res)

    def delete_workspace(
        self,
        res: "bs_td.DeleteWorkspaceResponseTypeDef",
    ) -> "dc_td.DeleteWorkspaceResponse":
        return dc_td.DeleteWorkspaceResponse.make_one(res)

    def delete_workspace_api_key(
        self,
        res: "bs_td.DeleteWorkspaceApiKeyResponseTypeDef",
    ) -> "dc_td.DeleteWorkspaceApiKeyResponse":
        return dc_td.DeleteWorkspaceApiKeyResponse.make_one(res)

    def delete_workspace_service_account(
        self,
        res: "bs_td.DeleteWorkspaceServiceAccountResponseTypeDef",
    ) -> "dc_td.DeleteWorkspaceServiceAccountResponse":
        return dc_td.DeleteWorkspaceServiceAccountResponse.make_one(res)

    def delete_workspace_service_account_token(
        self,
        res: "bs_td.DeleteWorkspaceServiceAccountTokenResponseTypeDef",
    ) -> "dc_td.DeleteWorkspaceServiceAccountTokenResponse":
        return dc_td.DeleteWorkspaceServiceAccountTokenResponse.make_one(res)

    def describe_workspace(
        self,
        res: "bs_td.DescribeWorkspaceResponseTypeDef",
    ) -> "dc_td.DescribeWorkspaceResponse":
        return dc_td.DescribeWorkspaceResponse.make_one(res)

    def describe_workspace_authentication(
        self,
        res: "bs_td.DescribeWorkspaceAuthenticationResponseTypeDef",
    ) -> "dc_td.DescribeWorkspaceAuthenticationResponse":
        return dc_td.DescribeWorkspaceAuthenticationResponse.make_one(res)

    def describe_workspace_configuration(
        self,
        res: "bs_td.DescribeWorkspaceConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeWorkspaceConfigurationResponse":
        return dc_td.DescribeWorkspaceConfigurationResponse.make_one(res)

    def disassociate_license(
        self,
        res: "bs_td.DisassociateLicenseResponseTypeDef",
    ) -> "dc_td.DisassociateLicenseResponse":
        return dc_td.DisassociateLicenseResponse.make_one(res)

    def list_permissions(
        self,
        res: "bs_td.ListPermissionsResponseTypeDef",
    ) -> "dc_td.ListPermissionsResponse":
        return dc_td.ListPermissionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_versions(
        self,
        res: "bs_td.ListVersionsResponseTypeDef",
    ) -> "dc_td.ListVersionsResponse":
        return dc_td.ListVersionsResponse.make_one(res)

    def list_workspace_service_account_tokens(
        self,
        res: "bs_td.ListWorkspaceServiceAccountTokensResponseTypeDef",
    ) -> "dc_td.ListWorkspaceServiceAccountTokensResponse":
        return dc_td.ListWorkspaceServiceAccountTokensResponse.make_one(res)

    def list_workspace_service_accounts(
        self,
        res: "bs_td.ListWorkspaceServiceAccountsResponseTypeDef",
    ) -> "dc_td.ListWorkspaceServiceAccountsResponse":
        return dc_td.ListWorkspaceServiceAccountsResponse.make_one(res)

    def list_workspaces(
        self,
        res: "bs_td.ListWorkspacesResponseTypeDef",
    ) -> "dc_td.ListWorkspacesResponse":
        return dc_td.ListWorkspacesResponse.make_one(res)

    def update_permissions(
        self,
        res: "bs_td.UpdatePermissionsResponseTypeDef",
    ) -> "dc_td.UpdatePermissionsResponse":
        return dc_td.UpdatePermissionsResponse.make_one(res)

    def update_workspace(
        self,
        res: "bs_td.UpdateWorkspaceResponseTypeDef",
    ) -> "dc_td.UpdateWorkspaceResponse":
        return dc_td.UpdateWorkspaceResponse.make_one(res)

    def update_workspace_authentication(
        self,
        res: "bs_td.UpdateWorkspaceAuthenticationResponseTypeDef",
    ) -> "dc_td.UpdateWorkspaceAuthenticationResponse":
        return dc_td.UpdateWorkspaceAuthenticationResponse.make_one(res)


grafana_caster = GRAFANACaster()
