# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workdocs import type_defs as bs_td


class WORKDOCSCaster:

    def abort_document_version_upload(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def activate_user(
        self,
        res: "bs_td.ActivateUserResponseTypeDef",
    ) -> "dc_td.ActivateUserResponse":
        return dc_td.ActivateUserResponse.make_one(res)

    def add_resource_permissions(
        self,
        res: "bs_td.AddResourcePermissionsResponseTypeDef",
    ) -> "dc_td.AddResourcePermissionsResponse":
        return dc_td.AddResourcePermissionsResponse.make_one(res)

    def create_comment(
        self,
        res: "bs_td.CreateCommentResponseTypeDef",
    ) -> "dc_td.CreateCommentResponse":
        return dc_td.CreateCommentResponse.make_one(res)

    def create_folder(
        self,
        res: "bs_td.CreateFolderResponseTypeDef",
    ) -> "dc_td.CreateFolderResponse":
        return dc_td.CreateFolderResponse.make_one(res)

    def create_notification_subscription(
        self,
        res: "bs_td.CreateNotificationSubscriptionResponseTypeDef",
    ) -> "dc_td.CreateNotificationSubscriptionResponse":
        return dc_td.CreateNotificationSubscriptionResponse.make_one(res)

    def create_user(
        self,
        res: "bs_td.CreateUserResponseTypeDef",
    ) -> "dc_td.CreateUserResponse":
        return dc_td.CreateUserResponse.make_one(res)

    def deactivate_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_comment(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_document(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_document_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_folder(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_folder_contents(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_notification_subscription(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_activities(
        self,
        res: "bs_td.DescribeActivitiesResponseTypeDef",
    ) -> "dc_td.DescribeActivitiesResponse":
        return dc_td.DescribeActivitiesResponse.make_one(res)

    def describe_comments(
        self,
        res: "bs_td.DescribeCommentsResponseTypeDef",
    ) -> "dc_td.DescribeCommentsResponse":
        return dc_td.DescribeCommentsResponse.make_one(res)

    def describe_document_versions(
        self,
        res: "bs_td.DescribeDocumentVersionsResponseTypeDef",
    ) -> "dc_td.DescribeDocumentVersionsResponse":
        return dc_td.DescribeDocumentVersionsResponse.make_one(res)

    def describe_folder_contents(
        self,
        res: "bs_td.DescribeFolderContentsResponseTypeDef",
    ) -> "dc_td.DescribeFolderContentsResponse":
        return dc_td.DescribeFolderContentsResponse.make_one(res)

    def describe_groups(
        self,
        res: "bs_td.DescribeGroupsResponseTypeDef",
    ) -> "dc_td.DescribeGroupsResponse":
        return dc_td.DescribeGroupsResponse.make_one(res)

    def describe_notification_subscriptions(
        self,
        res: "bs_td.DescribeNotificationSubscriptionsResponseTypeDef",
    ) -> "dc_td.DescribeNotificationSubscriptionsResponse":
        return dc_td.DescribeNotificationSubscriptionsResponse.make_one(res)

    def describe_resource_permissions(
        self,
        res: "bs_td.DescribeResourcePermissionsResponseTypeDef",
    ) -> "dc_td.DescribeResourcePermissionsResponse":
        return dc_td.DescribeResourcePermissionsResponse.make_one(res)

    def describe_root_folders(
        self,
        res: "bs_td.DescribeRootFoldersResponseTypeDef",
    ) -> "dc_td.DescribeRootFoldersResponse":
        return dc_td.DescribeRootFoldersResponse.make_one(res)

    def describe_users(
        self,
        res: "bs_td.DescribeUsersResponseTypeDef",
    ) -> "dc_td.DescribeUsersResponse":
        return dc_td.DescribeUsersResponse.make_one(res)

    def get_current_user(
        self,
        res: "bs_td.GetCurrentUserResponseTypeDef",
    ) -> "dc_td.GetCurrentUserResponse":
        return dc_td.GetCurrentUserResponse.make_one(res)

    def get_document(
        self,
        res: "bs_td.GetDocumentResponseTypeDef",
    ) -> "dc_td.GetDocumentResponse":
        return dc_td.GetDocumentResponse.make_one(res)

    def get_document_path(
        self,
        res: "bs_td.GetDocumentPathResponseTypeDef",
    ) -> "dc_td.GetDocumentPathResponse":
        return dc_td.GetDocumentPathResponse.make_one(res)

    def get_document_version(
        self,
        res: "bs_td.GetDocumentVersionResponseTypeDef",
    ) -> "dc_td.GetDocumentVersionResponse":
        return dc_td.GetDocumentVersionResponse.make_one(res)

    def get_folder(
        self,
        res: "bs_td.GetFolderResponseTypeDef",
    ) -> "dc_td.GetFolderResponse":
        return dc_td.GetFolderResponse.make_one(res)

    def get_folder_path(
        self,
        res: "bs_td.GetFolderPathResponseTypeDef",
    ) -> "dc_td.GetFolderPathResponse":
        return dc_td.GetFolderPathResponse.make_one(res)

    def get_resources(
        self,
        res: "bs_td.GetResourcesResponseTypeDef",
    ) -> "dc_td.GetResourcesResponse":
        return dc_td.GetResourcesResponse.make_one(res)

    def initiate_document_version_upload(
        self,
        res: "bs_td.InitiateDocumentVersionUploadResponseTypeDef",
    ) -> "dc_td.InitiateDocumentVersionUploadResponse":
        return dc_td.InitiateDocumentVersionUploadResponse.make_one(res)

    def remove_all_resource_permissions(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_resource_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def restore_document_versions(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def search_resources(
        self,
        res: "bs_td.SearchResourcesResponseTypeDef",
    ) -> "dc_td.SearchResourcesResponse":
        return dc_td.SearchResourcesResponse.make_one(res)

    def update_document(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_document_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_folder(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_user(
        self,
        res: "bs_td.UpdateUserResponseTypeDef",
    ) -> "dc_td.UpdateUserResponse":
        return dc_td.UpdateUserResponse.make_one(res)


workdocs_caster = WORKDOCSCaster()
