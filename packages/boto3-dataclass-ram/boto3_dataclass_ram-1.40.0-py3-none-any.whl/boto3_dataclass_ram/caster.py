# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ram import type_defs as bs_td


class RAMCaster:

    def accept_resource_share_invitation(
        self,
        res: "bs_td.AcceptResourceShareInvitationResponseTypeDef",
    ) -> "dc_td.AcceptResourceShareInvitationResponse":
        return dc_td.AcceptResourceShareInvitationResponse.make_one(res)

    def associate_resource_share(
        self,
        res: "bs_td.AssociateResourceShareResponseTypeDef",
    ) -> "dc_td.AssociateResourceShareResponse":
        return dc_td.AssociateResourceShareResponse.make_one(res)

    def associate_resource_share_permission(
        self,
        res: "bs_td.AssociateResourceSharePermissionResponseTypeDef",
    ) -> "dc_td.AssociateResourceSharePermissionResponse":
        return dc_td.AssociateResourceSharePermissionResponse.make_one(res)

    def create_permission(
        self,
        res: "bs_td.CreatePermissionResponseTypeDef",
    ) -> "dc_td.CreatePermissionResponse":
        return dc_td.CreatePermissionResponse.make_one(res)

    def create_permission_version(
        self,
        res: "bs_td.CreatePermissionVersionResponseTypeDef",
    ) -> "dc_td.CreatePermissionVersionResponse":
        return dc_td.CreatePermissionVersionResponse.make_one(res)

    def create_resource_share(
        self,
        res: "bs_td.CreateResourceShareResponseTypeDef",
    ) -> "dc_td.CreateResourceShareResponse":
        return dc_td.CreateResourceShareResponse.make_one(res)

    def delete_permission(
        self,
        res: "bs_td.DeletePermissionResponseTypeDef",
    ) -> "dc_td.DeletePermissionResponse":
        return dc_td.DeletePermissionResponse.make_one(res)

    def delete_permission_version(
        self,
        res: "bs_td.DeletePermissionVersionResponseTypeDef",
    ) -> "dc_td.DeletePermissionVersionResponse":
        return dc_td.DeletePermissionVersionResponse.make_one(res)

    def delete_resource_share(
        self,
        res: "bs_td.DeleteResourceShareResponseTypeDef",
    ) -> "dc_td.DeleteResourceShareResponse":
        return dc_td.DeleteResourceShareResponse.make_one(res)

    def disassociate_resource_share(
        self,
        res: "bs_td.DisassociateResourceShareResponseTypeDef",
    ) -> "dc_td.DisassociateResourceShareResponse":
        return dc_td.DisassociateResourceShareResponse.make_one(res)

    def disassociate_resource_share_permission(
        self,
        res: "bs_td.DisassociateResourceSharePermissionResponseTypeDef",
    ) -> "dc_td.DisassociateResourceSharePermissionResponse":
        return dc_td.DisassociateResourceSharePermissionResponse.make_one(res)

    def enable_sharing_with_aws_organization(
        self,
        res: "bs_td.EnableSharingWithAwsOrganizationResponseTypeDef",
    ) -> "dc_td.EnableSharingWithAwsOrganizationResponse":
        return dc_td.EnableSharingWithAwsOrganizationResponse.make_one(res)

    def get_permission(
        self,
        res: "bs_td.GetPermissionResponseTypeDef",
    ) -> "dc_td.GetPermissionResponse":
        return dc_td.GetPermissionResponse.make_one(res)

    def get_resource_policies(
        self,
        res: "bs_td.GetResourcePoliciesResponseTypeDef",
    ) -> "dc_td.GetResourcePoliciesResponse":
        return dc_td.GetResourcePoliciesResponse.make_one(res)

    def get_resource_share_associations(
        self,
        res: "bs_td.GetResourceShareAssociationsResponseTypeDef",
    ) -> "dc_td.GetResourceShareAssociationsResponse":
        return dc_td.GetResourceShareAssociationsResponse.make_one(res)

    def get_resource_share_invitations(
        self,
        res: "bs_td.GetResourceShareInvitationsResponseTypeDef",
    ) -> "dc_td.GetResourceShareInvitationsResponse":
        return dc_td.GetResourceShareInvitationsResponse.make_one(res)

    def get_resource_shares(
        self,
        res: "bs_td.GetResourceSharesResponseTypeDef",
    ) -> "dc_td.GetResourceSharesResponse":
        return dc_td.GetResourceSharesResponse.make_one(res)

    def list_pending_invitation_resources(
        self,
        res: "bs_td.ListPendingInvitationResourcesResponseTypeDef",
    ) -> "dc_td.ListPendingInvitationResourcesResponse":
        return dc_td.ListPendingInvitationResourcesResponse.make_one(res)

    def list_permission_associations(
        self,
        res: "bs_td.ListPermissionAssociationsResponseTypeDef",
    ) -> "dc_td.ListPermissionAssociationsResponse":
        return dc_td.ListPermissionAssociationsResponse.make_one(res)

    def list_permission_versions(
        self,
        res: "bs_td.ListPermissionVersionsResponseTypeDef",
    ) -> "dc_td.ListPermissionVersionsResponse":
        return dc_td.ListPermissionVersionsResponse.make_one(res)

    def list_permissions(
        self,
        res: "bs_td.ListPermissionsResponseTypeDef",
    ) -> "dc_td.ListPermissionsResponse":
        return dc_td.ListPermissionsResponse.make_one(res)

    def list_principals(
        self,
        res: "bs_td.ListPrincipalsResponseTypeDef",
    ) -> "dc_td.ListPrincipalsResponse":
        return dc_td.ListPrincipalsResponse.make_one(res)

    def list_replace_permission_associations_work(
        self,
        res: "bs_td.ListReplacePermissionAssociationsWorkResponseTypeDef",
    ) -> "dc_td.ListReplacePermissionAssociationsWorkResponse":
        return dc_td.ListReplacePermissionAssociationsWorkResponse.make_one(res)

    def list_resource_share_permissions(
        self,
        res: "bs_td.ListResourceSharePermissionsResponseTypeDef",
    ) -> "dc_td.ListResourceSharePermissionsResponse":
        return dc_td.ListResourceSharePermissionsResponse.make_one(res)

    def list_resource_types(
        self,
        res: "bs_td.ListResourceTypesResponseTypeDef",
    ) -> "dc_td.ListResourceTypesResponse":
        return dc_td.ListResourceTypesResponse.make_one(res)

    def list_resources(
        self,
        res: "bs_td.ListResourcesResponseTypeDef",
    ) -> "dc_td.ListResourcesResponse":
        return dc_td.ListResourcesResponse.make_one(res)

    def promote_permission_created_from_policy(
        self,
        res: "bs_td.PromotePermissionCreatedFromPolicyResponseTypeDef",
    ) -> "dc_td.PromotePermissionCreatedFromPolicyResponse":
        return dc_td.PromotePermissionCreatedFromPolicyResponse.make_one(res)

    def promote_resource_share_created_from_policy(
        self,
        res: "bs_td.PromoteResourceShareCreatedFromPolicyResponseTypeDef",
    ) -> "dc_td.PromoteResourceShareCreatedFromPolicyResponse":
        return dc_td.PromoteResourceShareCreatedFromPolicyResponse.make_one(res)

    def reject_resource_share_invitation(
        self,
        res: "bs_td.RejectResourceShareInvitationResponseTypeDef",
    ) -> "dc_td.RejectResourceShareInvitationResponse":
        return dc_td.RejectResourceShareInvitationResponse.make_one(res)

    def replace_permission_associations(
        self,
        res: "bs_td.ReplacePermissionAssociationsResponseTypeDef",
    ) -> "dc_td.ReplacePermissionAssociationsResponse":
        return dc_td.ReplacePermissionAssociationsResponse.make_one(res)

    def set_default_permission_version(
        self,
        res: "bs_td.SetDefaultPermissionVersionResponseTypeDef",
    ) -> "dc_td.SetDefaultPermissionVersionResponse":
        return dc_td.SetDefaultPermissionVersionResponse.make_one(res)

    def update_resource_share(
        self,
        res: "bs_td.UpdateResourceShareResponseTypeDef",
    ) -> "dc_td.UpdateResourceShareResponse":
        return dc_td.UpdateResourceShareResponse.make_one(res)


ram_caster = RAMCaster()
