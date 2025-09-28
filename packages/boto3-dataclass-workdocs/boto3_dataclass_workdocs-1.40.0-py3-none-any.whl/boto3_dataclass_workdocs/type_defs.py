# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workdocs import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AbortDocumentVersionUploadRequest:
    boto3_raw_data: "type_defs.AbortDocumentVersionUploadRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentId = field("DocumentId")
    VersionId = field("VersionId")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AbortDocumentVersionUploadRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortDocumentVersionUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateUserRequest:
    boto3_raw_data: "type_defs.ActivateUserRequestTypeDef" = dataclasses.field()

    UserId = field("UserId")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivateUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateUserRequestTypeDef"]
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
class UserMetadata:
    boto3_raw_data: "type_defs.UserMetadataTypeDef" = dataclasses.field()

    Id = field("Id")
    Username = field("Username")
    GivenName = field("GivenName")
    Surname = field("Surname")
    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationOptions:
    boto3_raw_data: "type_defs.NotificationOptionsTypeDef" = dataclasses.field()

    SendEmail = field("SendEmail")
    EmailMessage = field("EmailMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SharePrincipal:
    boto3_raw_data: "type_defs.SharePrincipalTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")
    Role = field("Role")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SharePrincipalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SharePrincipalTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareResult:
    boto3_raw_data: "type_defs.ShareResultTypeDef" = dataclasses.field()

    PrincipalId = field("PrincipalId")
    InviteePrincipalId = field("InviteePrincipalId")
    Role = field("Role")
    Status = field("Status")
    ShareId = field("ShareId")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShareResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShareResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCommentRequest:
    boto3_raw_data: "type_defs.CreateCommentRequestTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    VersionId = field("VersionId")
    Text = field("Text")
    AuthenticationToken = field("AuthenticationToken")
    ParentId = field("ParentId")
    ThreadId = field("ThreadId")
    Visibility = field("Visibility")
    NotifyCollaborators = field("NotifyCollaborators")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCommentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCommentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomMetadataRequest:
    boto3_raw_data: "type_defs.CreateCustomMetadataRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    CustomMetadata = field("CustomMetadata")
    AuthenticationToken = field("AuthenticationToken")
    VersionId = field("VersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFolderRequest:
    boto3_raw_data: "type_defs.CreateFolderRequestTypeDef" = dataclasses.field()

    ParentFolderId = field("ParentFolderId")
    AuthenticationToken = field("AuthenticationToken")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFolderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFolderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FolderMetadata:
    boto3_raw_data: "type_defs.FolderMetadataTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    CreatorId = field("CreatorId")
    ParentFolderId = field("ParentFolderId")
    CreatedTimestamp = field("CreatedTimestamp")
    ModifiedTimestamp = field("ModifiedTimestamp")
    ResourceState = field("ResourceState")
    Signature = field("Signature")
    Labels = field("Labels")
    Size = field("Size")
    LatestVersionSize = field("LatestVersionSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FolderMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FolderMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLabelsRequest:
    boto3_raw_data: "type_defs.CreateLabelsRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    Labels = field("Labels")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLabelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLabelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNotificationSubscriptionRequest:
    boto3_raw_data: "type_defs.CreateNotificationSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    Endpoint = field("Endpoint")
    Protocol = field("Protocol")
    SubscriptionType = field("SubscriptionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateNotificationSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNotificationSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subscription:
    boto3_raw_data: "type_defs.SubscriptionTypeDef" = dataclasses.field()

    SubscriptionId = field("SubscriptionId")
    EndPoint = field("EndPoint")
    Protocol = field("Protocol")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubscriptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageRuleType:
    boto3_raw_data: "type_defs.StorageRuleTypeTypeDef" = dataclasses.field()

    StorageAllocatedInBytes = field("StorageAllocatedInBytes")
    StorageType = field("StorageType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageRuleTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StorageRuleTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateUserRequest:
    boto3_raw_data: "type_defs.DeactivateUserRequestTypeDef" = dataclasses.field()

    UserId = field("UserId")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeactivateUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCommentRequest:
    boto3_raw_data: "type_defs.DeleteCommentRequestTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    VersionId = field("VersionId")
    CommentId = field("CommentId")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCommentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCommentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomMetadataRequest:
    boto3_raw_data: "type_defs.DeleteCustomMetadataRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    AuthenticationToken = field("AuthenticationToken")
    VersionId = field("VersionId")
    Keys = field("Keys")
    DeleteAll = field("DeleteAll")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCustomMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDocumentRequest:
    boto3_raw_data: "type_defs.DeleteDocumentRequestTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDocumentVersionRequest:
    boto3_raw_data: "type_defs.DeleteDocumentVersionRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentId = field("DocumentId")
    VersionId = field("VersionId")
    DeletePriorVersions = field("DeletePriorVersions")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDocumentVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDocumentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFolderContentsRequest:
    boto3_raw_data: "type_defs.DeleteFolderContentsRequestTypeDef" = dataclasses.field()

    FolderId = field("FolderId")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFolderContentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFolderContentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFolderRequest:
    boto3_raw_data: "type_defs.DeleteFolderRequestTypeDef" = dataclasses.field()

    FolderId = field("FolderId")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFolderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFolderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLabelsRequest:
    boto3_raw_data: "type_defs.DeleteLabelsRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    AuthenticationToken = field("AuthenticationToken")
    Labels = field("Labels")
    DeleteAll = field("DeleteAll")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLabelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLabelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNotificationSubscriptionRequest:
    boto3_raw_data: "type_defs.DeleteNotificationSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    SubscriptionId = field("SubscriptionId")
    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteNotificationSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNotificationSubscriptionRequestTypeDef"]
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

    UserId = field("UserId")
    AuthenticationToken = field("AuthenticationToken")

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
class DescribeCommentsRequest:
    boto3_raw_data: "type_defs.DescribeCommentsRequestTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    VersionId = field("VersionId")
    AuthenticationToken = field("AuthenticationToken")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCommentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCommentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDocumentVersionsRequest:
    boto3_raw_data: "type_defs.DescribeDocumentVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentId = field("DocumentId")
    AuthenticationToken = field("AuthenticationToken")
    Marker = field("Marker")
    Limit = field("Limit")
    Include = field("Include")
    Fields = field("Fields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDocumentVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentVersionMetadata:
    boto3_raw_data: "type_defs.DocumentVersionMetadataTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    ContentType = field("ContentType")
    Size = field("Size")
    Signature = field("Signature")
    Status = field("Status")
    CreatedTimestamp = field("CreatedTimestamp")
    ModifiedTimestamp = field("ModifiedTimestamp")
    ContentCreatedTimestamp = field("ContentCreatedTimestamp")
    ContentModifiedTimestamp = field("ContentModifiedTimestamp")
    CreatorId = field("CreatorId")
    Thumbnail = field("Thumbnail")
    Source = field("Source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentVersionMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentVersionMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFolderContentsRequest:
    boto3_raw_data: "type_defs.DescribeFolderContentsRequestTypeDef" = (
        dataclasses.field()
    )

    FolderId = field("FolderId")
    AuthenticationToken = field("AuthenticationToken")
    Sort = field("Sort")
    Order = field("Order")
    Limit = field("Limit")
    Marker = field("Marker")
    Type = field("Type")
    Include = field("Include")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFolderContentsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFolderContentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGroupsRequest:
    boto3_raw_data: "type_defs.DescribeGroupsRequestTypeDef" = dataclasses.field()

    SearchQuery = field("SearchQuery")
    AuthenticationToken = field("AuthenticationToken")
    OrganizationId = field("OrganizationId")
    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupMetadata:
    boto3_raw_data: "type_defs.GroupMetadataTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationSubscriptionsRequest:
    boto3_raw_data: "type_defs.DescribeNotificationSubscriptionsRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationSubscriptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotificationSubscriptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePermissionsRequest:
    boto3_raw_data: "type_defs.DescribeResourcePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    AuthenticationToken = field("AuthenticationToken")
    PrincipalId = field("PrincipalId")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeResourcePermissionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRootFoldersRequest:
    boto3_raw_data: "type_defs.DescribeRootFoldersRequestTypeDef" = dataclasses.field()

    AuthenticationToken = field("AuthenticationToken")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRootFoldersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRootFoldersRequestTypeDef"]
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

    AuthenticationToken = field("AuthenticationToken")
    OrganizationId = field("OrganizationId")
    UserIds = field("UserIds")
    Query = field("Query")
    Include = field("Include")
    Order = field("Order")
    Sort = field("Sort")
    Marker = field("Marker")
    Limit = field("Limit")
    Fields = field("Fields")

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
class LongRangeType:
    boto3_raw_data: "type_defs.LongRangeTypeTypeDef" = dataclasses.field()

    StartValue = field("StartValue")
    EndValue = field("EndValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LongRangeTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LongRangeTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPrincipalType:
    boto3_raw_data: "type_defs.SearchPrincipalTypeTypeDef" = dataclasses.field()

    Id = field("Id")
    Roles = field("Roles")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchPrincipalTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPrincipalTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCurrentUserRequest:
    boto3_raw_data: "type_defs.GetCurrentUserRequestTypeDef" = dataclasses.field()

    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCurrentUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCurrentUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentPathRequest:
    boto3_raw_data: "type_defs.GetDocumentPathRequestTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    AuthenticationToken = field("AuthenticationToken")
    Limit = field("Limit")
    Fields = field("Fields")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentPathRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentPathRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentRequest:
    boto3_raw_data: "type_defs.GetDocumentRequestTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    AuthenticationToken = field("AuthenticationToken")
    IncludeCustomMetadata = field("IncludeCustomMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentVersionRequest:
    boto3_raw_data: "type_defs.GetDocumentVersionRequestTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    VersionId = field("VersionId")
    AuthenticationToken = field("AuthenticationToken")
    Fields = field("Fields")
    IncludeCustomMetadata = field("IncludeCustomMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFolderPathRequest:
    boto3_raw_data: "type_defs.GetFolderPathRequestTypeDef" = dataclasses.field()

    FolderId = field("FolderId")
    AuthenticationToken = field("AuthenticationToken")
    Limit = field("Limit")
    Fields = field("Fields")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFolderPathRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFolderPathRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFolderRequest:
    boto3_raw_data: "type_defs.GetFolderRequestTypeDef" = dataclasses.field()

    FolderId = field("FolderId")
    AuthenticationToken = field("AuthenticationToken")
    IncludeCustomMetadata = field("IncludeCustomMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFolderRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFolderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcesRequest:
    boto3_raw_data: "type_defs.GetResourcesRequestTypeDef" = dataclasses.field()

    AuthenticationToken = field("AuthenticationToken")
    UserId = field("UserId")
    CollectionType = field("CollectionType")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadMetadata:
    boto3_raw_data: "type_defs.UploadMetadataTypeDef" = dataclasses.field()

    UploadUrl = field("UploadUrl")
    SignedHeaders = field("SignedHeaders")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UploadMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UploadMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionInfo:
    boto3_raw_data: "type_defs.PermissionInfoTypeDef" = dataclasses.field()

    Role = field("Role")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PermissionInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAllResourcePermissionsRequest:
    boto3_raw_data: "type_defs.RemoveAllResourcePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveAllResourcePermissionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAllResourcePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveResourcePermissionRequest:
    boto3_raw_data: "type_defs.RemoveResourcePermissionRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    PrincipalId = field("PrincipalId")
    AuthenticationToken = field("AuthenticationToken")
    PrincipalType = field("PrincipalType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveResourcePermissionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveResourcePermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourcePathComponent:
    boto3_raw_data: "type_defs.ResourcePathComponentTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourcePathComponentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourcePathComponentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDocumentVersionsRequest:
    boto3_raw_data: "type_defs.RestoreDocumentVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentId = field("DocumentId")
    AuthenticationToken = field("AuthenticationToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreDocumentVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDocumentVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSortResult:
    boto3_raw_data: "type_defs.SearchSortResultTypeDef" = dataclasses.field()

    Field = field("Field")
    Order = field("Order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchSortResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSortResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDocumentRequest:
    boto3_raw_data: "type_defs.UpdateDocumentRequestTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    AuthenticationToken = field("AuthenticationToken")
    Name = field("Name")
    ParentFolderId = field("ParentFolderId")
    ResourceState = field("ResourceState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDocumentVersionRequest:
    boto3_raw_data: "type_defs.UpdateDocumentVersionRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentId = field("DocumentId")
    VersionId = field("VersionId")
    AuthenticationToken = field("AuthenticationToken")
    VersionStatus = field("VersionStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDocumentVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDocumentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFolderRequest:
    boto3_raw_data: "type_defs.UpdateFolderRequestTypeDef" = dataclasses.field()

    FolderId = field("FolderId")
    AuthenticationToken = field("AuthenticationToken")
    Name = field("Name")
    ParentFolderId = field("ParentFolderId")
    ResourceState = field("ResourceState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFolderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFolderRequestTypeDef"]
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
class ResourceMetadata:
    boto3_raw_data: "type_defs.ResourceMetadataTypeDef" = dataclasses.field()

    Type = field("Type")
    Name = field("Name")
    OriginalName = field("OriginalName")
    Id = field("Id")
    VersionId = field("VersionId")

    @cached_property
    def Owner(self):  # pragma: no cover
        return UserMetadata.make_one(self.boto3_raw_data["Owner"])

    ParentId = field("ParentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddResourcePermissionsRequest:
    boto3_raw_data: "type_defs.AddResourcePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")

    @cached_property
    def Principals(self):  # pragma: no cover
        return SharePrincipal.make_many(self.boto3_raw_data["Principals"])

    AuthenticationToken = field("AuthenticationToken")

    @cached_property
    def NotificationOptions(self):  # pragma: no cover
        return NotificationOptions.make_one(self.boto3_raw_data["NotificationOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddResourcePermissionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddResourcePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddResourcePermissionsResponse:
    boto3_raw_data: "type_defs.AddResourcePermissionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ShareResults(self):  # pragma: no cover
        return ShareResult.make_many(self.boto3_raw_data["ShareResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddResourcePermissionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddResourcePermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFolderResponse:
    boto3_raw_data: "type_defs.CreateFolderResponseTypeDef" = dataclasses.field()

    @cached_property
    def Metadata(self):  # pragma: no cover
        return FolderMetadata.make_one(self.boto3_raw_data["Metadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFolderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFolderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRootFoldersResponse:
    boto3_raw_data: "type_defs.DescribeRootFoldersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Folders(self):  # pragma: no cover
        return FolderMetadata.make_many(self.boto3_raw_data["Folders"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRootFoldersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRootFoldersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFolderResponse:
    boto3_raw_data: "type_defs.GetFolderResponseTypeDef" = dataclasses.field()

    @cached_property
    def Metadata(self):  # pragma: no cover
        return FolderMetadata.make_one(self.boto3_raw_data["Metadata"])

    CustomMetadata = field("CustomMetadata")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFolderResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFolderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNotificationSubscriptionResponse:
    boto3_raw_data: "type_defs.CreateNotificationSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Subscription(self):  # pragma: no cover
        return Subscription.make_one(self.boto3_raw_data["Subscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateNotificationSubscriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNotificationSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationSubscriptionsResponse:
    boto3_raw_data: "type_defs.DescribeNotificationSubscriptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Subscriptions(self):  # pragma: no cover
        return Subscription.make_many(self.boto3_raw_data["Subscriptions"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationSubscriptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotificationSubscriptionsResponseTypeDef"]
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

    Username = field("Username")
    GivenName = field("GivenName")
    Surname = field("Surname")
    Password = field("Password")
    OrganizationId = field("OrganizationId")
    EmailAddress = field("EmailAddress")
    TimeZoneId = field("TimeZoneId")

    @cached_property
    def StorageRule(self):  # pragma: no cover
        return StorageRuleType.make_one(self.boto3_raw_data["StorageRule"])

    AuthenticationToken = field("AuthenticationToken")

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
class UpdateUserRequest:
    boto3_raw_data: "type_defs.UpdateUserRequestTypeDef" = dataclasses.field()

    UserId = field("UserId")
    AuthenticationToken = field("AuthenticationToken")
    GivenName = field("GivenName")
    Surname = field("Surname")
    Type = field("Type")

    @cached_property
    def StorageRule(self):  # pragma: no cover
        return StorageRuleType.make_one(self.boto3_raw_data["StorageRule"])

    TimeZoneId = field("TimeZoneId")
    Locale = field("Locale")
    GrantPoweruserPrivileges = field("GrantPoweruserPrivileges")

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
class UserStorageMetadata:
    boto3_raw_data: "type_defs.UserStorageMetadataTypeDef" = dataclasses.field()

    StorageUtilizedInBytes = field("StorageUtilizedInBytes")

    @cached_property
    def StorageRule(self):  # pragma: no cover
        return StorageRuleType.make_one(self.boto3_raw_data["StorageRule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserStorageMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserStorageMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateRangeType:
    boto3_raw_data: "type_defs.DateRangeTypeTypeDef" = dataclasses.field()

    StartValue = field("StartValue")
    EndValue = field("EndValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateRangeTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateRangeTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActivitiesRequest:
    boto3_raw_data: "type_defs.DescribeActivitiesRequestTypeDef" = dataclasses.field()

    AuthenticationToken = field("AuthenticationToken")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    OrganizationId = field("OrganizationId")
    ActivityTypes = field("ActivityTypes")
    ResourceId = field("ResourceId")
    UserId = field("UserId")
    IncludeIndirectActivities = field("IncludeIndirectActivities")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeActivitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActivitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateDocumentVersionUploadRequest:
    boto3_raw_data: "type_defs.InitiateDocumentVersionUploadRequestTypeDef" = (
        dataclasses.field()
    )

    AuthenticationToken = field("AuthenticationToken")
    Id = field("Id")
    Name = field("Name")
    ContentCreatedTimestamp = field("ContentCreatedTimestamp")
    ContentModifiedTimestamp = field("ContentModifiedTimestamp")
    ContentType = field("ContentType")
    DocumentSizeInBytes = field("DocumentSizeInBytes")
    ParentFolderId = field("ParentFolderId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InitiateDocumentVersionUploadRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateDocumentVersionUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActivitiesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeActivitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AuthenticationToken = field("AuthenticationToken")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    OrganizationId = field("OrganizationId")
    ActivityTypes = field("ActivityTypes")
    ResourceId = field("ResourceId")
    UserId = field("UserId")
    IncludeIndirectActivities = field("IncludeIndirectActivities")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeActivitiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActivitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCommentsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeCommentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DocumentId = field("DocumentId")
    VersionId = field("VersionId")
    AuthenticationToken = field("AuthenticationToken")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCommentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCommentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDocumentVersionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDocumentVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DocumentId = field("DocumentId")
    AuthenticationToken = field("AuthenticationToken")
    Include = field("Include")
    Fields = field("Fields")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDocumentVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFolderContentsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeFolderContentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FolderId = field("FolderId")
    AuthenticationToken = field("AuthenticationToken")
    Sort = field("Sort")
    Order = field("Order")
    Type = field("Type")
    Include = field("Include")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFolderContentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFolderContentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGroupsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SearchQuery = field("SearchQuery")
    AuthenticationToken = field("AuthenticationToken")
    OrganizationId = field("OrganizationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationSubscriptionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeNotificationSubscriptionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    OrganizationId = field("OrganizationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationSubscriptionsRequestPaginateTypeDef"
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
                "type_defs.DescribeNotificationSubscriptionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePermissionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeResourcePermissionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    AuthenticationToken = field("AuthenticationToken")
    PrincipalId = field("PrincipalId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeResourcePermissionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePermissionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRootFoldersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeRootFoldersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AuthenticationToken = field("AuthenticationToken")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRootFoldersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRootFoldersRequestPaginateTypeDef"]
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

    AuthenticationToken = field("AuthenticationToken")
    OrganizationId = field("OrganizationId")
    UserIds = field("UserIds")
    Query = field("Query")
    Include = field("Include")
    Order = field("Order")
    Sort = field("Sort")
    Fields = field("Fields")

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
class DescribeDocumentVersionsResponse:
    boto3_raw_data: "type_defs.DescribeDocumentVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentVersions(self):  # pragma: no cover
        return DocumentVersionMetadata.make_many(
            self.boto3_raw_data["DocumentVersions"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDocumentVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentMetadata:
    boto3_raw_data: "type_defs.DocumentMetadataTypeDef" = dataclasses.field()

    Id = field("Id")
    CreatorId = field("CreatorId")
    ParentFolderId = field("ParentFolderId")
    CreatedTimestamp = field("CreatedTimestamp")
    ModifiedTimestamp = field("ModifiedTimestamp")

    @cached_property
    def LatestVersionMetadata(self):  # pragma: no cover
        return DocumentVersionMetadata.make_one(
            self.boto3_raw_data["LatestVersionMetadata"]
        )

    ResourceState = field("ResourceState")
    Labels = field("Labels")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentVersionResponse:
    boto3_raw_data: "type_defs.GetDocumentVersionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Metadata(self):  # pragma: no cover
        return DocumentVersionMetadata.make_one(self.boto3_raw_data["Metadata"])

    CustomMetadata = field("CustomMetadata")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGroupsResponse:
    boto3_raw_data: "type_defs.DescribeGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupMetadata.make_many(self.boto3_raw_data["Groups"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Participants:
    boto3_raw_data: "type_defs.ParticipantsTypeDef" = dataclasses.field()

    @cached_property
    def Users(self):  # pragma: no cover
        return UserMetadata.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupMetadata.make_many(self.boto3_raw_data["Groups"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParticipantsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParticipantsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Principal:
    boto3_raw_data: "type_defs.PrincipalTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")

    @cached_property
    def Roles(self):  # pragma: no cover
        return PermissionInfo.make_many(self.boto3_raw_data["Roles"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrincipalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrincipalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourcePath:
    boto3_raw_data: "type_defs.ResourcePathTypeDef" = dataclasses.field()

    @cached_property
    def Components(self):  # pragma: no cover
        return ResourcePathComponent.make_many(self.boto3_raw_data["Components"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourcePathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourcePathTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    Id = field("Id")
    Username = field("Username")
    EmailAddress = field("EmailAddress")
    GivenName = field("GivenName")
    Surname = field("Surname")
    OrganizationId = field("OrganizationId")
    RootFolderId = field("RootFolderId")
    RecycleBinFolderId = field("RecycleBinFolderId")
    Status = field("Status")
    Type = field("Type")
    CreatedTimestamp = field("CreatedTimestamp")
    ModifiedTimestamp = field("ModifiedTimestamp")
    TimeZoneId = field("TimeZoneId")
    Locale = field("Locale")

    @cached_property
    def Storage(self):  # pragma: no cover
        return UserStorageMetadata.make_one(self.boto3_raw_data["Storage"])

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
class Filters:
    boto3_raw_data: "type_defs.FiltersTypeDef" = dataclasses.field()

    TextLocales = field("TextLocales")
    ContentCategories = field("ContentCategories")
    ResourceTypes = field("ResourceTypes")
    Labels = field("Labels")

    @cached_property
    def Principals(self):  # pragma: no cover
        return SearchPrincipalType.make_many(self.boto3_raw_data["Principals"])

    AncestorIds = field("AncestorIds")
    SearchCollectionTypes = field("SearchCollectionTypes")

    @cached_property
    def SizeRange(self):  # pragma: no cover
        return LongRangeType.make_one(self.boto3_raw_data["SizeRange"])

    @cached_property
    def CreatedRange(self):  # pragma: no cover
        return DateRangeType.make_one(self.boto3_raw_data["CreatedRange"])

    @cached_property
    def ModifiedRange(self):  # pragma: no cover
        return DateRangeType.make_one(self.boto3_raw_data["ModifiedRange"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FiltersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFolderContentsResponse:
    boto3_raw_data: "type_defs.DescribeFolderContentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Folders(self):  # pragma: no cover
        return FolderMetadata.make_many(self.boto3_raw_data["Folders"])

    @cached_property
    def Documents(self):  # pragma: no cover
        return DocumentMetadata.make_many(self.boto3_raw_data["Documents"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFolderContentsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFolderContentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentResponse:
    boto3_raw_data: "type_defs.GetDocumentResponseTypeDef" = dataclasses.field()

    @cached_property
    def Metadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["Metadata"])

    CustomMetadata = field("CustomMetadata")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcesResponse:
    boto3_raw_data: "type_defs.GetResourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Folders(self):  # pragma: no cover
        return FolderMetadata.make_many(self.boto3_raw_data["Folders"])

    @cached_property
    def Documents(self):  # pragma: no cover
        return DocumentMetadata.make_many(self.boto3_raw_data["Documents"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateDocumentVersionUploadResponse:
    boto3_raw_data: "type_defs.InitiateDocumentVersionUploadResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["Metadata"])

    @cached_property
    def UploadMetadata(self):  # pragma: no cover
        return UploadMetadata.make_one(self.boto3_raw_data["UploadMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InitiateDocumentVersionUploadResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateDocumentVersionUploadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePermissionsResponse:
    boto3_raw_data: "type_defs.DescribeResourcePermissionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Principals(self):  # pragma: no cover
        return Principal.make_many(self.boto3_raw_data["Principals"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeResourcePermissionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentPathResponse:
    boto3_raw_data: "type_defs.GetDocumentPathResponseTypeDef" = dataclasses.field()

    @cached_property
    def Path(self):  # pragma: no cover
        return ResourcePath.make_one(self.boto3_raw_data["Path"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentPathResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentPathResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFolderPathResponse:
    boto3_raw_data: "type_defs.GetFolderPathResponseTypeDef" = dataclasses.field()

    @cached_property
    def Path(self):  # pragma: no cover
        return ResourcePath.make_one(self.boto3_raw_data["Path"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFolderPathResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFolderPathResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateUserResponse:
    boto3_raw_data: "type_defs.ActivateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommentMetadata:
    boto3_raw_data: "type_defs.CommentMetadataTypeDef" = dataclasses.field()

    CommentId = field("CommentId")

    @cached_property
    def Contributor(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["Contributor"])

    CreatedTimestamp = field("CreatedTimestamp")
    CommentStatus = field("CommentStatus")
    RecipientId = field("RecipientId")
    ContributorId = field("ContributorId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommentMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommentMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Comment:
    boto3_raw_data: "type_defs.CommentTypeDef" = dataclasses.field()

    CommentId = field("CommentId")
    ParentId = field("ParentId")
    ThreadId = field("ThreadId")
    Text = field("Text")

    @cached_property
    def Contributor(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["Contributor"])

    CreatedTimestamp = field("CreatedTimestamp")
    Status = field("Status")
    Visibility = field("Visibility")
    RecipientId = field("RecipientId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommentTypeDef"]]
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
class DescribeUsersResponse:
    boto3_raw_data: "type_defs.DescribeUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["Users"])

    TotalNumberOfUsers = field("TotalNumberOfUsers")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

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
class GetCurrentUserResponse:
    boto3_raw_data: "type_defs.GetCurrentUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCurrentUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCurrentUserResponseTypeDef"]
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
class SearchResourcesRequestPaginate:
    boto3_raw_data: "type_defs.SearchResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AuthenticationToken = field("AuthenticationToken")
    QueryText = field("QueryText")
    QueryScopes = field("QueryScopes")
    OrganizationId = field("OrganizationId")
    AdditionalResponseFields = field("AdditionalResponseFields")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def OrderBy(self):  # pragma: no cover
        return SearchSortResult.make_many(self.boto3_raw_data["OrderBy"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchResourcesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesRequest:
    boto3_raw_data: "type_defs.SearchResourcesRequestTypeDef" = dataclasses.field()

    AuthenticationToken = field("AuthenticationToken")
    QueryText = field("QueryText")
    QueryScopes = field("QueryScopes")
    OrganizationId = field("OrganizationId")
    AdditionalResponseFields = field("AdditionalResponseFields")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def OrderBy(self):  # pragma: no cover
        return SearchSortResult.make_many(self.boto3_raw_data["OrderBy"])

    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Activity:
    boto3_raw_data: "type_defs.ActivityTypeDef" = dataclasses.field()

    Type = field("Type")
    TimeStamp = field("TimeStamp")
    IsIndirectActivity = field("IsIndirectActivity")
    OrganizationId = field("OrganizationId")

    @cached_property
    def Initiator(self):  # pragma: no cover
        return UserMetadata.make_one(self.boto3_raw_data["Initiator"])

    @cached_property
    def Participants(self):  # pragma: no cover
        return Participants.make_one(self.boto3_raw_data["Participants"])

    @cached_property
    def ResourceMetadata(self):  # pragma: no cover
        return ResourceMetadata.make_one(self.boto3_raw_data["ResourceMetadata"])

    @cached_property
    def OriginalParent(self):  # pragma: no cover
        return ResourceMetadata.make_one(self.boto3_raw_data["OriginalParent"])

    @cached_property
    def CommentMetadata(self):  # pragma: no cover
        return CommentMetadata.make_one(self.boto3_raw_data["CommentMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseItem:
    boto3_raw_data: "type_defs.ResponseItemTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    WebUrl = field("WebUrl")

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    @cached_property
    def FolderMetadata(self):  # pragma: no cover
        return FolderMetadata.make_one(self.boto3_raw_data["FolderMetadata"])

    @cached_property
    def CommentMetadata(self):  # pragma: no cover
        return CommentMetadata.make_one(self.boto3_raw_data["CommentMetadata"])

    @cached_property
    def DocumentVersionMetadata(self):  # pragma: no cover
        return DocumentVersionMetadata.make_one(
            self.boto3_raw_data["DocumentVersionMetadata"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResponseItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCommentResponse:
    boto3_raw_data: "type_defs.CreateCommentResponseTypeDef" = dataclasses.field()

    @cached_property
    def Comment(self):  # pragma: no cover
        return Comment.make_one(self.boto3_raw_data["Comment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCommentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCommentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCommentsResponse:
    boto3_raw_data: "type_defs.DescribeCommentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Comments(self):  # pragma: no cover
        return Comment.make_many(self.boto3_raw_data["Comments"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCommentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCommentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActivitiesResponse:
    boto3_raw_data: "type_defs.DescribeActivitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserActivities(self):  # pragma: no cover
        return Activity.make_many(self.boto3_raw_data["UserActivities"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeActivitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActivitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesResponse:
    boto3_raw_data: "type_defs.SearchResourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ResponseItem.make_many(self.boto3_raw_data["Items"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
