# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workspaces import type_defs as bs_td


class WORKSPACESCaster:

    def accept_account_link_invitation(
        self,
        res: "bs_td.AcceptAccountLinkInvitationResultTypeDef",
    ) -> "dc_td.AcceptAccountLinkInvitationResult":
        return dc_td.AcceptAccountLinkInvitationResult.make_one(res)

    def associate_connection_alias(
        self,
        res: "bs_td.AssociateConnectionAliasResultTypeDef",
    ) -> "dc_td.AssociateConnectionAliasResult":
        return dc_td.AssociateConnectionAliasResult.make_one(res)

    def associate_workspace_application(
        self,
        res: "bs_td.AssociateWorkspaceApplicationResultTypeDef",
    ) -> "dc_td.AssociateWorkspaceApplicationResult":
        return dc_td.AssociateWorkspaceApplicationResult.make_one(res)

    def copy_workspace_image(
        self,
        res: "bs_td.CopyWorkspaceImageResultTypeDef",
    ) -> "dc_td.CopyWorkspaceImageResult":
        return dc_td.CopyWorkspaceImageResult.make_one(res)

    def create_account_link_invitation(
        self,
        res: "bs_td.CreateAccountLinkInvitationResultTypeDef",
    ) -> "dc_td.CreateAccountLinkInvitationResult":
        return dc_td.CreateAccountLinkInvitationResult.make_one(res)

    def create_connect_client_add_in(
        self,
        res: "bs_td.CreateConnectClientAddInResultTypeDef",
    ) -> "dc_td.CreateConnectClientAddInResult":
        return dc_td.CreateConnectClientAddInResult.make_one(res)

    def create_connection_alias(
        self,
        res: "bs_td.CreateConnectionAliasResultTypeDef",
    ) -> "dc_td.CreateConnectionAliasResult":
        return dc_td.CreateConnectionAliasResult.make_one(res)

    def create_ip_group(
        self,
        res: "bs_td.CreateIpGroupResultTypeDef",
    ) -> "dc_td.CreateIpGroupResult":
        return dc_td.CreateIpGroupResult.make_one(res)

    def create_standby_workspaces(
        self,
        res: "bs_td.CreateStandbyWorkspacesResultTypeDef",
    ) -> "dc_td.CreateStandbyWorkspacesResult":
        return dc_td.CreateStandbyWorkspacesResult.make_one(res)

    def create_updated_workspace_image(
        self,
        res: "bs_td.CreateUpdatedWorkspaceImageResultTypeDef",
    ) -> "dc_td.CreateUpdatedWorkspaceImageResult":
        return dc_td.CreateUpdatedWorkspaceImageResult.make_one(res)

    def create_workspace_bundle(
        self,
        res: "bs_td.CreateWorkspaceBundleResultTypeDef",
    ) -> "dc_td.CreateWorkspaceBundleResult":
        return dc_td.CreateWorkspaceBundleResult.make_one(res)

    def create_workspace_image(
        self,
        res: "bs_td.CreateWorkspaceImageResultTypeDef",
    ) -> "dc_td.CreateWorkspaceImageResult":
        return dc_td.CreateWorkspaceImageResult.make_one(res)

    def create_workspaces(
        self,
        res: "bs_td.CreateWorkspacesResultTypeDef",
    ) -> "dc_td.CreateWorkspacesResult":
        return dc_td.CreateWorkspacesResult.make_one(res)

    def create_workspaces_pool(
        self,
        res: "bs_td.CreateWorkspacesPoolResultTypeDef",
    ) -> "dc_td.CreateWorkspacesPoolResult":
        return dc_td.CreateWorkspacesPoolResult.make_one(res)

    def delete_account_link_invitation(
        self,
        res: "bs_td.DeleteAccountLinkInvitationResultTypeDef",
    ) -> "dc_td.DeleteAccountLinkInvitationResult":
        return dc_td.DeleteAccountLinkInvitationResult.make_one(res)

    def deploy_workspace_applications(
        self,
        res: "bs_td.DeployWorkspaceApplicationsResultTypeDef",
    ) -> "dc_td.DeployWorkspaceApplicationsResult":
        return dc_td.DeployWorkspaceApplicationsResult.make_one(res)

    def describe_account(
        self,
        res: "bs_td.DescribeAccountResultTypeDef",
    ) -> "dc_td.DescribeAccountResult":
        return dc_td.DescribeAccountResult.make_one(res)

    def describe_account_modifications(
        self,
        res: "bs_td.DescribeAccountModificationsResultTypeDef",
    ) -> "dc_td.DescribeAccountModificationsResult":
        return dc_td.DescribeAccountModificationsResult.make_one(res)

    def describe_application_associations(
        self,
        res: "bs_td.DescribeApplicationAssociationsResultTypeDef",
    ) -> "dc_td.DescribeApplicationAssociationsResult":
        return dc_td.DescribeApplicationAssociationsResult.make_one(res)

    def describe_applications(
        self,
        res: "bs_td.DescribeApplicationsResultTypeDef",
    ) -> "dc_td.DescribeApplicationsResult":
        return dc_td.DescribeApplicationsResult.make_one(res)

    def describe_bundle_associations(
        self,
        res: "bs_td.DescribeBundleAssociationsResultTypeDef",
    ) -> "dc_td.DescribeBundleAssociationsResult":
        return dc_td.DescribeBundleAssociationsResult.make_one(res)

    def describe_client_branding(
        self,
        res: "bs_td.DescribeClientBrandingResultTypeDef",
    ) -> "dc_td.DescribeClientBrandingResult":
        return dc_td.DescribeClientBrandingResult.make_one(res)

    def describe_client_properties(
        self,
        res: "bs_td.DescribeClientPropertiesResultTypeDef",
    ) -> "dc_td.DescribeClientPropertiesResult":
        return dc_td.DescribeClientPropertiesResult.make_one(res)

    def describe_connect_client_add_ins(
        self,
        res: "bs_td.DescribeConnectClientAddInsResultTypeDef",
    ) -> "dc_td.DescribeConnectClientAddInsResult":
        return dc_td.DescribeConnectClientAddInsResult.make_one(res)

    def describe_connection_alias_permissions(
        self,
        res: "bs_td.DescribeConnectionAliasPermissionsResultTypeDef",
    ) -> "dc_td.DescribeConnectionAliasPermissionsResult":
        return dc_td.DescribeConnectionAliasPermissionsResult.make_one(res)

    def describe_connection_aliases(
        self,
        res: "bs_td.DescribeConnectionAliasesResultTypeDef",
    ) -> "dc_td.DescribeConnectionAliasesResult":
        return dc_td.DescribeConnectionAliasesResult.make_one(res)

    def describe_custom_workspace_image_import(
        self,
        res: "bs_td.DescribeCustomWorkspaceImageImportResultTypeDef",
    ) -> "dc_td.DescribeCustomWorkspaceImageImportResult":
        return dc_td.DescribeCustomWorkspaceImageImportResult.make_one(res)

    def describe_image_associations(
        self,
        res: "bs_td.DescribeImageAssociationsResultTypeDef",
    ) -> "dc_td.DescribeImageAssociationsResult":
        return dc_td.DescribeImageAssociationsResult.make_one(res)

    def describe_ip_groups(
        self,
        res: "bs_td.DescribeIpGroupsResultTypeDef",
    ) -> "dc_td.DescribeIpGroupsResult":
        return dc_td.DescribeIpGroupsResult.make_one(res)

    def describe_tags(
        self,
        res: "bs_td.DescribeTagsResultTypeDef",
    ) -> "dc_td.DescribeTagsResult":
        return dc_td.DescribeTagsResult.make_one(res)

    def describe_workspace_associations(
        self,
        res: "bs_td.DescribeWorkspaceAssociationsResultTypeDef",
    ) -> "dc_td.DescribeWorkspaceAssociationsResult":
        return dc_td.DescribeWorkspaceAssociationsResult.make_one(res)

    def describe_workspace_bundles(
        self,
        res: "bs_td.DescribeWorkspaceBundlesResultTypeDef",
    ) -> "dc_td.DescribeWorkspaceBundlesResult":
        return dc_td.DescribeWorkspaceBundlesResult.make_one(res)

    def describe_workspace_directories(
        self,
        res: "bs_td.DescribeWorkspaceDirectoriesResultTypeDef",
    ) -> "dc_td.DescribeWorkspaceDirectoriesResult":
        return dc_td.DescribeWorkspaceDirectoriesResult.make_one(res)

    def describe_workspace_image_permissions(
        self,
        res: "bs_td.DescribeWorkspaceImagePermissionsResultTypeDef",
    ) -> "dc_td.DescribeWorkspaceImagePermissionsResult":
        return dc_td.DescribeWorkspaceImagePermissionsResult.make_one(res)

    def describe_workspace_images(
        self,
        res: "bs_td.DescribeWorkspaceImagesResultTypeDef",
    ) -> "dc_td.DescribeWorkspaceImagesResult":
        return dc_td.DescribeWorkspaceImagesResult.make_one(res)

    def describe_workspace_snapshots(
        self,
        res: "bs_td.DescribeWorkspaceSnapshotsResultTypeDef",
    ) -> "dc_td.DescribeWorkspaceSnapshotsResult":
        return dc_td.DescribeWorkspaceSnapshotsResult.make_one(res)

    def describe_workspaces(
        self,
        res: "bs_td.DescribeWorkspacesResultTypeDef",
    ) -> "dc_td.DescribeWorkspacesResult":
        return dc_td.DescribeWorkspacesResult.make_one(res)

    def describe_workspaces_connection_status(
        self,
        res: "bs_td.DescribeWorkspacesConnectionStatusResultTypeDef",
    ) -> "dc_td.DescribeWorkspacesConnectionStatusResult":
        return dc_td.DescribeWorkspacesConnectionStatusResult.make_one(res)

    def describe_workspaces_pool_sessions(
        self,
        res: "bs_td.DescribeWorkspacesPoolSessionsResultTypeDef",
    ) -> "dc_td.DescribeWorkspacesPoolSessionsResult":
        return dc_td.DescribeWorkspacesPoolSessionsResult.make_one(res)

    def describe_workspaces_pools(
        self,
        res: "bs_td.DescribeWorkspacesPoolsResultTypeDef",
    ) -> "dc_td.DescribeWorkspacesPoolsResult":
        return dc_td.DescribeWorkspacesPoolsResult.make_one(res)

    def disassociate_workspace_application(
        self,
        res: "bs_td.DisassociateWorkspaceApplicationResultTypeDef",
    ) -> "dc_td.DisassociateWorkspaceApplicationResult":
        return dc_td.DisassociateWorkspaceApplicationResult.make_one(res)

    def get_account_link(
        self,
        res: "bs_td.GetAccountLinkResultTypeDef",
    ) -> "dc_td.GetAccountLinkResult":
        return dc_td.GetAccountLinkResult.make_one(res)

    def import_client_branding(
        self,
        res: "bs_td.ImportClientBrandingResultTypeDef",
    ) -> "dc_td.ImportClientBrandingResult":
        return dc_td.ImportClientBrandingResult.make_one(res)

    def import_custom_workspace_image(
        self,
        res: "bs_td.ImportCustomWorkspaceImageResultTypeDef",
    ) -> "dc_td.ImportCustomWorkspaceImageResult":
        return dc_td.ImportCustomWorkspaceImageResult.make_one(res)

    def import_workspace_image(
        self,
        res: "bs_td.ImportWorkspaceImageResultTypeDef",
    ) -> "dc_td.ImportWorkspaceImageResult":
        return dc_td.ImportWorkspaceImageResult.make_one(res)

    def list_account_links(
        self,
        res: "bs_td.ListAccountLinksResultTypeDef",
    ) -> "dc_td.ListAccountLinksResult":
        return dc_td.ListAccountLinksResult.make_one(res)

    def list_available_management_cidr_ranges(
        self,
        res: "bs_td.ListAvailableManagementCidrRangesResultTypeDef",
    ) -> "dc_td.ListAvailableManagementCidrRangesResult":
        return dc_td.ListAvailableManagementCidrRangesResult.make_one(res)

    def migrate_workspace(
        self,
        res: "bs_td.MigrateWorkspaceResultTypeDef",
    ) -> "dc_td.MigrateWorkspaceResult":
        return dc_td.MigrateWorkspaceResult.make_one(res)

    def modify_account(
        self,
        res: "bs_td.ModifyAccountResultTypeDef",
    ) -> "dc_td.ModifyAccountResult":
        return dc_td.ModifyAccountResult.make_one(res)

    def reboot_workspaces(
        self,
        res: "bs_td.RebootWorkspacesResultTypeDef",
    ) -> "dc_td.RebootWorkspacesResult":
        return dc_td.RebootWorkspacesResult.make_one(res)

    def rebuild_workspaces(
        self,
        res: "bs_td.RebuildWorkspacesResultTypeDef",
    ) -> "dc_td.RebuildWorkspacesResult":
        return dc_td.RebuildWorkspacesResult.make_one(res)

    def register_workspace_directory(
        self,
        res: "bs_td.RegisterWorkspaceDirectoryResultTypeDef",
    ) -> "dc_td.RegisterWorkspaceDirectoryResult":
        return dc_td.RegisterWorkspaceDirectoryResult.make_one(res)

    def reject_account_link_invitation(
        self,
        res: "bs_td.RejectAccountLinkInvitationResultTypeDef",
    ) -> "dc_td.RejectAccountLinkInvitationResult":
        return dc_td.RejectAccountLinkInvitationResult.make_one(res)

    def start_workspaces(
        self,
        res: "bs_td.StartWorkspacesResultTypeDef",
    ) -> "dc_td.StartWorkspacesResult":
        return dc_td.StartWorkspacesResult.make_one(res)

    def stop_workspaces(
        self,
        res: "bs_td.StopWorkspacesResultTypeDef",
    ) -> "dc_td.StopWorkspacesResult":
        return dc_td.StopWorkspacesResult.make_one(res)

    def terminate_workspaces(
        self,
        res: "bs_td.TerminateWorkspacesResultTypeDef",
    ) -> "dc_td.TerminateWorkspacesResult":
        return dc_td.TerminateWorkspacesResult.make_one(res)

    def update_workspaces_pool(
        self,
        res: "bs_td.UpdateWorkspacesPoolResultTypeDef",
    ) -> "dc_td.UpdateWorkspacesPoolResult":
        return dc_td.UpdateWorkspacesPoolResult.make_one(res)


workspaces_caster = WORKSPACESCaster()
