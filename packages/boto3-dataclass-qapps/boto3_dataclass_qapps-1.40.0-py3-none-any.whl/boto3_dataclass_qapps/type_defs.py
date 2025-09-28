# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_qapps import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssociateLibraryItemReviewInput:
    boto3_raw_data: "type_defs.AssociateLibraryItemReviewInputTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    libraryItemId = field("libraryItemId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateLibraryItemReviewInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateLibraryItemReviewInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateQAppWithUserInput:
    boto3_raw_data: "type_defs.AssociateQAppWithUserInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    appId = field("appId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateQAppWithUserInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateQAppWithUserInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateCategoryInputCategory:
    boto3_raw_data: "type_defs.BatchCreateCategoryInputCategoryTypeDef" = (
        dataclasses.field()
    )

    title = field("title")
    id = field("id")
    color = field("color")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchCreateCategoryInputCategoryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateCategoryInputCategoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteCategoryInput:
    boto3_raw_data: "type_defs.BatchDeleteCategoryInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    categories = field("categories")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteCategoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteCategoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CategoryInput:
    boto3_raw_data: "type_defs.CategoryInputTypeDef" = dataclasses.field()

    id = field("id")
    title = field("title")
    color = field("color")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CategoryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CategoryInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileUploadCardInput:
    boto3_raw_data: "type_defs.FileUploadCardInputTypeDef" = dataclasses.field()

    title = field("title")
    id = field("id")
    type = field("type")
    filename = field("filename")
    fileId = field("fileId")
    allowOverride = field("allowOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileUploadCardInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileUploadCardInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QPluginCardInput:
    boto3_raw_data: "type_defs.QPluginCardInputTypeDef" = dataclasses.field()

    title = field("title")
    id = field("id")
    type = field("type")
    prompt = field("prompt")
    pluginId = field("pluginId")
    actionIdentifier = field("actionIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QPluginCardInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QPluginCardInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextInputCardInput:
    boto3_raw_data: "type_defs.TextInputCardInputTypeDef" = dataclasses.field()

    title = field("title")
    id = field("id")
    type = field("type")
    placeholder = field("placeholder")
    defaultValue = field("defaultValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextInputCardInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextInputCardInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Submission:
    boto3_raw_data: "type_defs.SubmissionTypeDef" = dataclasses.field()

    value = field("value")
    submissionId = field("submissionId")
    timestamp = field("timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubmissionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubmissionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileUploadCard:
    boto3_raw_data: "type_defs.FileUploadCardTypeDef" = dataclasses.field()

    id = field("id")
    title = field("title")
    dependencies = field("dependencies")
    type = field("type")
    filename = field("filename")
    fileId = field("fileId")
    allowOverride = field("allowOverride")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileUploadCardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileUploadCardTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QPluginCard:
    boto3_raw_data: "type_defs.QPluginCardTypeDef" = dataclasses.field()

    id = field("id")
    title = field("title")
    dependencies = field("dependencies")
    type = field("type")
    prompt = field("prompt")
    pluginType = field("pluginType")
    pluginId = field("pluginId")
    actionIdentifier = field("actionIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QPluginCardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QPluginCardTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextInputCard:
    boto3_raw_data: "type_defs.TextInputCardTypeDef" = dataclasses.field()

    id = field("id")
    title = field("title")
    dependencies = field("dependencies")
    type = field("type")
    placeholder = field("placeholder")
    defaultValue = field("defaultValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextInputCardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextInputCardTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmissionMutation:
    boto3_raw_data: "type_defs.SubmissionMutationTypeDef" = dataclasses.field()

    submissionId = field("submissionId")
    mutationType = field("mutationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubmissionMutationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmissionMutationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Category:
    boto3_raw_data: "type_defs.CategoryTypeDef" = dataclasses.field()

    id = field("id")
    title = field("title")
    color = field("color")
    appCount = field("appCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CategoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CategoryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationMessage:
    boto3_raw_data: "type_defs.ConversationMessageTypeDef" = dataclasses.field()

    body = field("body")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConversationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLibraryItemInput:
    boto3_raw_data: "type_defs.CreateLibraryItemInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    appId = field("appId")
    appVersion = field("appVersion")
    categories = field("categories")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLibraryItemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLibraryItemInputTypeDef"]
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
class CreatePresignedUrlInput:
    boto3_raw_data: "type_defs.CreatePresignedUrlInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    cardId = field("cardId")
    appId = field("appId")
    fileContentsSha256 = field("fileContentsSha256")
    fileName = field("fileName")
    scope = field("scope")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePresignedUrlInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePresignedUrlInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLibraryItemInput:
    boto3_raw_data: "type_defs.DeleteLibraryItemInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    libraryItemId = field("libraryItemId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLibraryItemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLibraryItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQAppInput:
    boto3_raw_data: "type_defs.DeleteQAppInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    appId = field("appId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteQAppInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteQAppInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQAppPermissionsInput:
    boto3_raw_data: "type_defs.DescribeQAppPermissionsInputTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    appId = field("appId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeQAppPermissionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQAppPermissionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateLibraryItemReviewInput:
    boto3_raw_data: "type_defs.DisassociateLibraryItemReviewInputTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    libraryItemId = field("libraryItemId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateLibraryItemReviewInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateLibraryItemReviewInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateQAppFromUserInput:
    boto3_raw_data: "type_defs.DisassociateQAppFromUserInputTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    appId = field("appId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateQAppFromUserInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateQAppFromUserInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeValueOutput:
    boto3_raw_data: "type_defs.DocumentAttributeValueOutputTypeDef" = (
        dataclasses.field()
    )

    stringValue = field("stringValue")
    stringListValue = field("stringListValue")
    longValue = field("longValue")
    dateValue = field("dateValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportQAppSessionDataInput:
    boto3_raw_data: "type_defs.ExportQAppSessionDataInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportQAppSessionDataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportQAppSessionDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputCardMetadataOutput:
    boto3_raw_data: "type_defs.FormInputCardMetadataOutputTypeDef" = dataclasses.field()

    schema = field("schema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FormInputCardMetadataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormInputCardMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputCardMetadata:
    boto3_raw_data: "type_defs.FormInputCardMetadataTypeDef" = dataclasses.field()

    schema = field("schema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FormInputCardMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormInputCardMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLibraryItemInput:
    boto3_raw_data: "type_defs.GetLibraryItemInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    libraryItemId = field("libraryItemId")
    appId = field("appId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLibraryItemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLibraryItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQAppInput:
    boto3_raw_data: "type_defs.GetQAppInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    appId = field("appId")
    appVersion = field("appVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQAppInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetQAppInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQAppSessionInput:
    boto3_raw_data: "type_defs.GetQAppSessionInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQAppSessionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQAppSessionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQAppSessionMetadataInput:
    boto3_raw_data: "type_defs.GetQAppSessionMetadataInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQAppSessionMetadataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQAppSessionMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionSharingConfiguration:
    boto3_raw_data: "type_defs.SessionSharingConfigurationTypeDef" = dataclasses.field()

    enabled = field("enabled")
    acceptResponses = field("acceptResponses")
    revealCards = field("revealCards")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionSharingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionSharingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportDocumentInput:
    boto3_raw_data: "type_defs.ImportDocumentInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    cardId = field("cardId")
    appId = field("appId")
    fileContentsBase64 = field("fileContentsBase64")
    fileName = field("fileName")
    scope = field("scope")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportDocumentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDocumentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCategoriesInput:
    boto3_raw_data: "type_defs.ListCategoriesInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCategoriesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCategoriesInputTypeDef"]
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
class ListLibraryItemsInput:
    boto3_raw_data: "type_defs.ListLibraryItemsInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    limit = field("limit")
    nextToken = field("nextToken")
    categoryId = field("categoryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLibraryItemsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLibraryItemsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQAppSessionDataInput:
    boto3_raw_data: "type_defs.ListQAppSessionDataInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQAppSessionDataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQAppSessionDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQAppsInput:
    boto3_raw_data: "type_defs.ListQAppsInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    limit = field("limit")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListQAppsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListQAppsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserAppItem:
    boto3_raw_data: "type_defs.UserAppItemTypeDef" = dataclasses.field()

    appId = field("appId")
    appArn = field("appArn")
    title = field("title")
    createdAt = field("createdAt")
    description = field("description")
    canEdit = field("canEdit")
    status = field("status")
    isVerified = field("isVerified")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserAppItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserAppItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceARN = field("resourceARN")

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
class PermissionInput:
    boto3_raw_data: "type_defs.PermissionInputTypeDef" = dataclasses.field()

    action = field("action")
    principal = field("principal")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PermissionInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrincipalOutput:
    boto3_raw_data: "type_defs.PrincipalOutputTypeDef" = dataclasses.field()

    userId = field("userId")
    userType = field("userType")
    email = field("email")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrincipalOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrincipalOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    userId = field("userId")

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
class StopQAppSessionInput:
    boto3_raw_data: "type_defs.StopQAppSessionInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopQAppSessionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopQAppSessionInputTypeDef"]
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

    resourceARN = field("resourceARN")
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

    resourceARN = field("resourceARN")
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
class UpdateLibraryItemInput:
    boto3_raw_data: "type_defs.UpdateLibraryItemInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    libraryItemId = field("libraryItemId")
    status = field("status")
    categories = field("categories")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLibraryItemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLibraryItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLibraryItemMetadataInput:
    boto3_raw_data: "type_defs.UpdateLibraryItemMetadataInputTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    libraryItemId = field("libraryItemId")
    isVerified = field("isVerified")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLibraryItemMetadataInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLibraryItemMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateCategoryInput:
    boto3_raw_data: "type_defs.BatchCreateCategoryInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")

    @cached_property
    def categories(self):  # pragma: no cover
        return BatchCreateCategoryInputCategory.make_many(
            self.boto3_raw_data["categories"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchCreateCategoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateCategoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateCategoryInput:
    boto3_raw_data: "type_defs.BatchUpdateCategoryInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")

    @cached_property
    def categories(self):  # pragma: no cover
        return CategoryInput.make_many(self.boto3_raw_data["categories"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateCategoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateCategoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CardStatus:
    boto3_raw_data: "type_defs.CardStatusTypeDef" = dataclasses.field()

    currentState = field("currentState")
    currentValue = field("currentValue")

    @cached_property
    def submissions(self):  # pragma: no cover
        return Submission.make_many(self.boto3_raw_data["submissions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CardStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CardStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CardValue:
    boto3_raw_data: "type_defs.CardValueTypeDef" = dataclasses.field()

    cardId = field("cardId")
    value = field("value")

    @cached_property
    def submissionMutation(self):  # pragma: no cover
        return SubmissionMutation.make_one(self.boto3_raw_data["submissionMutation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CardValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CardValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LibraryItemMember:
    boto3_raw_data: "type_defs.LibraryItemMemberTypeDef" = dataclasses.field()

    libraryItemId = field("libraryItemId")
    appId = field("appId")
    appVersion = field("appVersion")

    @cached_property
    def categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["categories"])

    status = field("status")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    ratingCount = field("ratingCount")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    isRatedByUser = field("isRatedByUser")
    userCount = field("userCount")
    isVerified = field("isVerified")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LibraryItemMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LibraryItemMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictQAppInputOptions:
    boto3_raw_data: "type_defs.PredictQAppInputOptionsTypeDef" = dataclasses.field()

    @cached_property
    def conversation(self):  # pragma: no cover
        return ConversationMessage.make_many(self.boto3_raw_data["conversation"])

    problemStatement = field("problemStatement")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictQAppInputOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictQAppInputOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLibraryItemOutput:
    boto3_raw_data: "type_defs.CreateLibraryItemOutputTypeDef" = dataclasses.field()

    libraryItemId = field("libraryItemId")
    status = field("status")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    ratingCount = field("ratingCount")
    isVerified = field("isVerified")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLibraryItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLibraryItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePresignedUrlOutput:
    boto3_raw_data: "type_defs.CreatePresignedUrlOutputTypeDef" = dataclasses.field()

    fileId = field("fileId")
    presignedUrl = field("presignedUrl")
    presignedUrlFields = field("presignedUrlFields")
    presignedUrlExpiration = field("presignedUrlExpiration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePresignedUrlOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePresignedUrlOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQAppOutput:
    boto3_raw_data: "type_defs.CreateQAppOutputTypeDef" = dataclasses.field()

    appId = field("appId")
    appArn = field("appArn")
    title = field("title")
    description = field("description")
    initialPrompt = field("initialPrompt")
    appVersion = field("appVersion")
    status = field("status")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    requiredCapabilities = field("requiredCapabilities")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateQAppOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQAppOutputTypeDef"]
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
class ExportQAppSessionDataOutput:
    boto3_raw_data: "type_defs.ExportQAppSessionDataOutputTypeDef" = dataclasses.field()

    csvFileLink = field("csvFileLink")
    expiresAt = field("expiresAt")
    sessionArn = field("sessionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportQAppSessionDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportQAppSessionDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLibraryItemOutput:
    boto3_raw_data: "type_defs.GetLibraryItemOutputTypeDef" = dataclasses.field()

    libraryItemId = field("libraryItemId")
    appId = field("appId")
    appVersion = field("appVersion")

    @cached_property
    def categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["categories"])

    status = field("status")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    ratingCount = field("ratingCount")
    isRatedByUser = field("isRatedByUser")
    userCount = field("userCount")
    isVerified = field("isVerified")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLibraryItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLibraryItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportDocumentOutput:
    boto3_raw_data: "type_defs.ImportDocumentOutputTypeDef" = dataclasses.field()

    fileId = field("fileId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportDocumentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDocumentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCategoriesOutput:
    boto3_raw_data: "type_defs.ListCategoriesOutputTypeDef" = dataclasses.field()

    @cached_property
    def categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["categories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCategoriesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCategoriesOutputTypeDef"]
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
class StartQAppSessionOutput:
    boto3_raw_data: "type_defs.StartQAppSessionOutputTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    sessionArn = field("sessionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartQAppSessionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQAppSessionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLibraryItemOutput:
    boto3_raw_data: "type_defs.UpdateLibraryItemOutputTypeDef" = dataclasses.field()

    libraryItemId = field("libraryItemId")
    appId = field("appId")
    appVersion = field("appVersion")

    @cached_property
    def categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["categories"])

    status = field("status")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    ratingCount = field("ratingCount")
    isRatedByUser = field("isRatedByUser")
    userCount = field("userCount")
    isVerified = field("isVerified")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLibraryItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLibraryItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQAppOutput:
    boto3_raw_data: "type_defs.UpdateQAppOutputTypeDef" = dataclasses.field()

    appId = field("appId")
    appArn = field("appArn")
    title = field("title")
    description = field("description")
    initialPrompt = field("initialPrompt")
    appVersion = field("appVersion")
    status = field("status")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    requiredCapabilities = field("requiredCapabilities")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateQAppOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQAppOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQAppSessionOutput:
    boto3_raw_data: "type_defs.UpdateQAppSessionOutputTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    sessionArn = field("sessionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQAppSessionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQAppSessionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeOutput:
    boto3_raw_data: "type_defs.DocumentAttributeOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def value(self):  # pragma: no cover
        return DocumentAttributeValueOutput.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeValue:
    boto3_raw_data: "type_defs.DocumentAttributeValueTypeDef" = dataclasses.field()

    stringValue = field("stringValue")
    stringListValue = field("stringListValue")
    longValue = field("longValue")
    dateValue = field("dateValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputCardInputOutput:
    boto3_raw_data: "type_defs.FormInputCardInputOutputTypeDef" = dataclasses.field()

    title = field("title")
    id = field("id")
    type = field("type")

    @cached_property
    def metadata(self):  # pragma: no cover
        return FormInputCardMetadataOutput.make_one(self.boto3_raw_data["metadata"])

    computeMode = field("computeMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FormInputCardInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormInputCardInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputCard:
    boto3_raw_data: "type_defs.FormInputCardTypeDef" = dataclasses.field()

    id = field("id")
    title = field("title")
    dependencies = field("dependencies")
    type = field("type")

    @cached_property
    def metadata(self):  # pragma: no cover
        return FormInputCardMetadataOutput.make_one(self.boto3_raw_data["metadata"])

    computeMode = field("computeMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormInputCardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormInputCardTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputCardInput:
    boto3_raw_data: "type_defs.FormInputCardInputTypeDef" = dataclasses.field()

    title = field("title")
    id = field("id")
    type = field("type")

    @cached_property
    def metadata(self):  # pragma: no cover
        return FormInputCardMetadata.make_one(self.boto3_raw_data["metadata"])

    computeMode = field("computeMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FormInputCardInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormInputCardInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQAppSessionMetadataOutput:
    boto3_raw_data: "type_defs.GetQAppSessionMetadataOutputTypeDef" = (
        dataclasses.field()
    )

    sessionId = field("sessionId")
    sessionArn = field("sessionArn")
    sessionName = field("sessionName")

    @cached_property
    def sharingConfiguration(self):  # pragma: no cover
        return SessionSharingConfiguration.make_one(
            self.boto3_raw_data["sharingConfiguration"]
        )

    sessionOwner = field("sessionOwner")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQAppSessionMetadataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQAppSessionMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQAppSessionMetadataInput:
    boto3_raw_data: "type_defs.UpdateQAppSessionMetadataInputTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    sessionId = field("sessionId")

    @cached_property
    def sharingConfiguration(self):  # pragma: no cover
        return SessionSharingConfiguration.make_one(
            self.boto3_raw_data["sharingConfiguration"]
        )

    sessionName = field("sessionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateQAppSessionMetadataInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQAppSessionMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQAppSessionMetadataOutput:
    boto3_raw_data: "type_defs.UpdateQAppSessionMetadataOutputTypeDef" = (
        dataclasses.field()
    )

    sessionId = field("sessionId")
    sessionArn = field("sessionArn")
    sessionName = field("sessionName")

    @cached_property
    def sharingConfiguration(self):  # pragma: no cover
        return SessionSharingConfiguration.make_one(
            self.boto3_raw_data["sharingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateQAppSessionMetadataOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQAppSessionMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLibraryItemsInputPaginate:
    boto3_raw_data: "type_defs.ListLibraryItemsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    categoryId = field("categoryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLibraryItemsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLibraryItemsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQAppsInputPaginate:
    boto3_raw_data: "type_defs.ListQAppsInputPaginateTypeDef" = dataclasses.field()

    instanceId = field("instanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQAppsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQAppsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQAppsOutput:
    boto3_raw_data: "type_defs.ListQAppsOutputTypeDef" = dataclasses.field()

    @cached_property
    def apps(self):  # pragma: no cover
        return UserAppItem.make_many(self.boto3_raw_data["apps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListQAppsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListQAppsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQAppPermissionsInput:
    boto3_raw_data: "type_defs.UpdateQAppPermissionsInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    appId = field("appId")

    @cached_property
    def grantPermissions(self):  # pragma: no cover
        return PermissionInput.make_many(self.boto3_raw_data["grantPermissions"])

    @cached_property
    def revokePermissions(self):  # pragma: no cover
        return PermissionInput.make_many(self.boto3_raw_data["revokePermissions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQAppPermissionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQAppPermissionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionOutput:
    boto3_raw_data: "type_defs.PermissionOutputTypeDef" = dataclasses.field()

    action = field("action")

    @cached_property
    def principal(self):  # pragma: no cover
        return PrincipalOutput.make_one(self.boto3_raw_data["principal"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PermissionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QAppSessionData:
    boto3_raw_data: "type_defs.QAppSessionDataTypeDef" = dataclasses.field()

    cardId = field("cardId")

    @cached_property
    def user(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["user"])

    value = field("value")
    submissionId = field("submissionId")
    timestamp = field("timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QAppSessionDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QAppSessionDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQAppSessionOutput:
    boto3_raw_data: "type_defs.GetQAppSessionOutputTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    sessionArn = field("sessionArn")
    sessionName = field("sessionName")
    appVersion = field("appVersion")
    latestPublishedAppVersion = field("latestPublishedAppVersion")
    status = field("status")
    cardStatus = field("cardStatus")
    userIsHost = field("userIsHost")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQAppSessionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQAppSessionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQAppSessionInput:
    boto3_raw_data: "type_defs.StartQAppSessionInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    appId = field("appId")
    appVersion = field("appVersion")

    @cached_property
    def initialValues(self):  # pragma: no cover
        return CardValue.make_many(self.boto3_raw_data["initialValues"])

    sessionId = field("sessionId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartQAppSessionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQAppSessionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQAppSessionInput:
    boto3_raw_data: "type_defs.UpdateQAppSessionInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    sessionId = field("sessionId")

    @cached_property
    def values(self):  # pragma: no cover
        return CardValue.make_many(self.boto3_raw_data["values"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQAppSessionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQAppSessionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLibraryItemsOutput:
    boto3_raw_data: "type_defs.ListLibraryItemsOutputTypeDef" = dataclasses.field()

    @cached_property
    def libraryItems(self):  # pragma: no cover
        return LibraryItemMember.make_many(self.boto3_raw_data["libraryItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLibraryItemsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLibraryItemsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictQAppInput:
    boto3_raw_data: "type_defs.PredictQAppInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")

    @cached_property
    def options(self):  # pragma: no cover
        return PredictQAppInputOptions.make_one(self.boto3_raw_data["options"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictQAppInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictQAppInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeFilterOutput:
    boto3_raw_data: "type_defs.AttributeFilterOutputTypeDef" = dataclasses.field()

    andAllFilters = field("andAllFilters")
    orAllFilters = field("orAllFilters")
    notFilter = field("notFilter")

    @cached_property
    def equalsTo(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["equalsTo"])

    @cached_property
    def containsAll(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["containsAll"])

    @cached_property
    def containsAny(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["containsAny"])

    @cached_property
    def greaterThan(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["greaterThan"])

    @cached_property
    def greaterThanOrEquals(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(
            self.boto3_raw_data["greaterThanOrEquals"]
        )

    @cached_property
    def lessThan(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["lessThan"])

    @cached_property
    def lessThanOrEquals(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["lessThanOrEquals"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttribute:
    boto3_raw_data: "type_defs.DocumentAttributeTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def value(self):  # pragma: no cover
        return DocumentAttributeValue.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQAppPermissionsOutput:
    boto3_raw_data: "type_defs.DescribeQAppPermissionsOutputTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    appId = field("appId")

    @cached_property
    def permissions(self):  # pragma: no cover
        return PermissionOutput.make_many(self.boto3_raw_data["permissions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeQAppPermissionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQAppPermissionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQAppPermissionsOutput:
    boto3_raw_data: "type_defs.UpdateQAppPermissionsOutputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    appId = field("appId")

    @cached_property
    def permissions(self):  # pragma: no cover
        return PermissionOutput.make_many(self.boto3_raw_data["permissions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQAppPermissionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQAppPermissionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQAppSessionDataOutput:
    boto3_raw_data: "type_defs.ListQAppSessionDataOutputTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    sessionArn = field("sessionArn")

    @cached_property
    def sessionData(self):  # pragma: no cover
        return QAppSessionData.make_many(self.boto3_raw_data["sessionData"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQAppSessionDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQAppSessionDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QQueryCardInputOutput:
    boto3_raw_data: "type_defs.QQueryCardInputOutputTypeDef" = dataclasses.field()

    title = field("title")
    id = field("id")
    type = field("type")
    prompt = field("prompt")
    outputSource = field("outputSource")

    @cached_property
    def attributeFilter(self):  # pragma: no cover
        return AttributeFilterOutput.make_one(self.boto3_raw_data["attributeFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QQueryCardInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QQueryCardInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QQueryCard:
    boto3_raw_data: "type_defs.QQueryCardTypeDef" = dataclasses.field()

    id = field("id")
    title = field("title")
    dependencies = field("dependencies")
    type = field("type")
    prompt = field("prompt")
    outputSource = field("outputSource")

    @cached_property
    def attributeFilter(self):  # pragma: no cover
        return AttributeFilterOutput.make_one(self.boto3_raw_data["attributeFilter"])

    memoryReferences = field("memoryReferences")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QQueryCardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QQueryCardTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeFilter:
    boto3_raw_data: "type_defs.AttributeFilterTypeDef" = dataclasses.field()

    andAllFilters = field("andAllFilters")
    orAllFilters = field("orAllFilters")
    notFilter = field("notFilter")

    @cached_property
    def equalsTo(self):  # pragma: no cover
        return DocumentAttribute.make_one(self.boto3_raw_data["equalsTo"])

    @cached_property
    def containsAll(self):  # pragma: no cover
        return DocumentAttribute.make_one(self.boto3_raw_data["containsAll"])

    @cached_property
    def containsAny(self):  # pragma: no cover
        return DocumentAttribute.make_one(self.boto3_raw_data["containsAny"])

    @cached_property
    def greaterThan(self):  # pragma: no cover
        return DocumentAttribute.make_one(self.boto3_raw_data["greaterThan"])

    @cached_property
    def greaterThanOrEquals(self):  # pragma: no cover
        return DocumentAttribute.make_one(self.boto3_raw_data["greaterThanOrEquals"])

    @cached_property
    def lessThan(self):  # pragma: no cover
        return DocumentAttribute.make_one(self.boto3_raw_data["lessThan"])

    @cached_property
    def lessThanOrEquals(self):  # pragma: no cover
        return DocumentAttribute.make_one(self.boto3_raw_data["lessThanOrEquals"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CardInputOutput:
    boto3_raw_data: "type_defs.CardInputOutputTypeDef" = dataclasses.field()

    @cached_property
    def textInput(self):  # pragma: no cover
        return TextInputCardInput.make_one(self.boto3_raw_data["textInput"])

    @cached_property
    def qQuery(self):  # pragma: no cover
        return QQueryCardInputOutput.make_one(self.boto3_raw_data["qQuery"])

    @cached_property
    def qPlugin(self):  # pragma: no cover
        return QPluginCardInput.make_one(self.boto3_raw_data["qPlugin"])

    @cached_property
    def fileUpload(self):  # pragma: no cover
        return FileUploadCardInput.make_one(self.boto3_raw_data["fileUpload"])

    @cached_property
    def formInput(self):  # pragma: no cover
        return FormInputCardInputOutput.make_one(self.boto3_raw_data["formInput"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CardInputOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CardInputOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Card:
    boto3_raw_data: "type_defs.CardTypeDef" = dataclasses.field()

    @cached_property
    def textInput(self):  # pragma: no cover
        return TextInputCard.make_one(self.boto3_raw_data["textInput"])

    @cached_property
    def qQuery(self):  # pragma: no cover
        return QQueryCard.make_one(self.boto3_raw_data["qQuery"])

    @cached_property
    def qPlugin(self):  # pragma: no cover
        return QPluginCard.make_one(self.boto3_raw_data["qPlugin"])

    @cached_property
    def fileUpload(self):  # pragma: no cover
        return FileUploadCard.make_one(self.boto3_raw_data["fileUpload"])

    @cached_property
    def formInput(self):  # pragma: no cover
        return FormInputCard.make_one(self.boto3_raw_data["formInput"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CardTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QQueryCardInput:
    boto3_raw_data: "type_defs.QQueryCardInputTypeDef" = dataclasses.field()

    title = field("title")
    id = field("id")
    type = field("type")
    prompt = field("prompt")
    outputSource = field("outputSource")

    @cached_property
    def attributeFilter(self):  # pragma: no cover
        return AttributeFilter.make_one(self.boto3_raw_data["attributeFilter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QQueryCardInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QQueryCardInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppDefinitionInputOutput:
    boto3_raw_data: "type_defs.AppDefinitionInputOutputTypeDef" = dataclasses.field()

    @cached_property
    def cards(self):  # pragma: no cover
        return CardInputOutput.make_many(self.boto3_raw_data["cards"])

    initialPrompt = field("initialPrompt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppDefinitionInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppDefinitionInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppDefinition:
    boto3_raw_data: "type_defs.AppDefinitionTypeDef" = dataclasses.field()

    appDefinitionVersion = field("appDefinitionVersion")

    @cached_property
    def cards(self):  # pragma: no cover
        return Card.make_many(self.boto3_raw_data["cards"])

    canEdit = field("canEdit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CardInput:
    boto3_raw_data: "type_defs.CardInputTypeDef" = dataclasses.field()

    @cached_property
    def textInput(self):  # pragma: no cover
        return TextInputCardInput.make_one(self.boto3_raw_data["textInput"])

    @cached_property
    def qQuery(self):  # pragma: no cover
        return QQueryCardInput.make_one(self.boto3_raw_data["qQuery"])

    @cached_property
    def qPlugin(self):  # pragma: no cover
        return QPluginCardInput.make_one(self.boto3_raw_data["qPlugin"])

    @cached_property
    def fileUpload(self):  # pragma: no cover
        return FileUploadCardInput.make_one(self.boto3_raw_data["fileUpload"])

    @cached_property
    def formInput(self):  # pragma: no cover
        return FormInputCardInput.make_one(self.boto3_raw_data["formInput"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CardInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CardInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictAppDefinition:
    boto3_raw_data: "type_defs.PredictAppDefinitionTypeDef" = dataclasses.field()

    title = field("title")

    @cached_property
    def appDefinition(self):  # pragma: no cover
        return AppDefinitionInputOutput.make_one(self.boto3_raw_data["appDefinition"])

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictAppDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictAppDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQAppOutput:
    boto3_raw_data: "type_defs.GetQAppOutputTypeDef" = dataclasses.field()

    appId = field("appId")
    appArn = field("appArn")
    title = field("title")
    description = field("description")
    initialPrompt = field("initialPrompt")
    appVersion = field("appVersion")
    status = field("status")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    requiredCapabilities = field("requiredCapabilities")

    @cached_property
    def appDefinition(self):  # pragma: no cover
        return AppDefinition.make_one(self.boto3_raw_data["appDefinition"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQAppOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetQAppOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppDefinitionInput:
    boto3_raw_data: "type_defs.AppDefinitionInputTypeDef" = dataclasses.field()

    @cached_property
    def cards(self):  # pragma: no cover
        return CardInput.make_many(self.boto3_raw_data["cards"])

    initialPrompt = field("initialPrompt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppDefinitionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictQAppOutput:
    boto3_raw_data: "type_defs.PredictQAppOutputTypeDef" = dataclasses.field()

    @cached_property
    def app(self):  # pragma: no cover
        return PredictAppDefinition.make_one(self.boto3_raw_data["app"])

    problemStatement = field("problemStatement")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictQAppOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictQAppOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQAppInput:
    boto3_raw_data: "type_defs.CreateQAppInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    title = field("title")
    appDefinition = field("appDefinition")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateQAppInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateQAppInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQAppInput:
    boto3_raw_data: "type_defs.UpdateQAppInputTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    appId = field("appId")
    title = field("title")
    description = field("description")
    appDefinition = field("appDefinition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateQAppInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateQAppInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
