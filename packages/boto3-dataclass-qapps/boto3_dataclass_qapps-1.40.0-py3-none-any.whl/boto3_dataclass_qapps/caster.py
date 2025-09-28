# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_qapps import type_defs as bs_td


class QAPPSCaster:

    def associate_library_item_review(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_q_app_with_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_create_category(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_delete_category(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_update_category(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_library_item(
        self,
        res: "bs_td.CreateLibraryItemOutputTypeDef",
    ) -> "dc_td.CreateLibraryItemOutput":
        return dc_td.CreateLibraryItemOutput.make_one(res)

    def create_presigned_url(
        self,
        res: "bs_td.CreatePresignedUrlOutputTypeDef",
    ) -> "dc_td.CreatePresignedUrlOutput":
        return dc_td.CreatePresignedUrlOutput.make_one(res)

    def create_q_app(
        self,
        res: "bs_td.CreateQAppOutputTypeDef",
    ) -> "dc_td.CreateQAppOutput":
        return dc_td.CreateQAppOutput.make_one(res)

    def delete_library_item(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_q_app(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_q_app_permissions(
        self,
        res: "bs_td.DescribeQAppPermissionsOutputTypeDef",
    ) -> "dc_td.DescribeQAppPermissionsOutput":
        return dc_td.DescribeQAppPermissionsOutput.make_one(res)

    def disassociate_library_item_review(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_q_app_from_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def export_q_app_session_data(
        self,
        res: "bs_td.ExportQAppSessionDataOutputTypeDef",
    ) -> "dc_td.ExportQAppSessionDataOutput":
        return dc_td.ExportQAppSessionDataOutput.make_one(res)

    def get_library_item(
        self,
        res: "bs_td.GetLibraryItemOutputTypeDef",
    ) -> "dc_td.GetLibraryItemOutput":
        return dc_td.GetLibraryItemOutput.make_one(res)

    def get_q_app(
        self,
        res: "bs_td.GetQAppOutputTypeDef",
    ) -> "dc_td.GetQAppOutput":
        return dc_td.GetQAppOutput.make_one(res)

    def get_q_app_session(
        self,
        res: "bs_td.GetQAppSessionOutputTypeDef",
    ) -> "dc_td.GetQAppSessionOutput":
        return dc_td.GetQAppSessionOutput.make_one(res)

    def get_q_app_session_metadata(
        self,
        res: "bs_td.GetQAppSessionMetadataOutputTypeDef",
    ) -> "dc_td.GetQAppSessionMetadataOutput":
        return dc_td.GetQAppSessionMetadataOutput.make_one(res)

    def import_document(
        self,
        res: "bs_td.ImportDocumentOutputTypeDef",
    ) -> "dc_td.ImportDocumentOutput":
        return dc_td.ImportDocumentOutput.make_one(res)

    def list_categories(
        self,
        res: "bs_td.ListCategoriesOutputTypeDef",
    ) -> "dc_td.ListCategoriesOutput":
        return dc_td.ListCategoriesOutput.make_one(res)

    def list_library_items(
        self,
        res: "bs_td.ListLibraryItemsOutputTypeDef",
    ) -> "dc_td.ListLibraryItemsOutput":
        return dc_td.ListLibraryItemsOutput.make_one(res)

    def list_q_app_session_data(
        self,
        res: "bs_td.ListQAppSessionDataOutputTypeDef",
    ) -> "dc_td.ListQAppSessionDataOutput":
        return dc_td.ListQAppSessionDataOutput.make_one(res)

    def list_q_apps(
        self,
        res: "bs_td.ListQAppsOutputTypeDef",
    ) -> "dc_td.ListQAppsOutput":
        return dc_td.ListQAppsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def predict_q_app(
        self,
        res: "bs_td.PredictQAppOutputTypeDef",
    ) -> "dc_td.PredictQAppOutput":
        return dc_td.PredictQAppOutput.make_one(res)

    def start_q_app_session(
        self,
        res: "bs_td.StartQAppSessionOutputTypeDef",
    ) -> "dc_td.StartQAppSessionOutput":
        return dc_td.StartQAppSessionOutput.make_one(res)

    def stop_q_app_session(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_library_item(
        self,
        res: "bs_td.UpdateLibraryItemOutputTypeDef",
    ) -> "dc_td.UpdateLibraryItemOutput":
        return dc_td.UpdateLibraryItemOutput.make_one(res)

    def update_library_item_metadata(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_q_app(
        self,
        res: "bs_td.UpdateQAppOutputTypeDef",
    ) -> "dc_td.UpdateQAppOutput":
        return dc_td.UpdateQAppOutput.make_one(res)

    def update_q_app_permissions(
        self,
        res: "bs_td.UpdateQAppPermissionsOutputTypeDef",
    ) -> "dc_td.UpdateQAppPermissionsOutput":
        return dc_td.UpdateQAppPermissionsOutput.make_one(res)

    def update_q_app_session(
        self,
        res: "bs_td.UpdateQAppSessionOutputTypeDef",
    ) -> "dc_td.UpdateQAppSessionOutput":
        return dc_td.UpdateQAppSessionOutput.make_one(res)

    def update_q_app_session_metadata(
        self,
        res: "bs_td.UpdateQAppSessionMetadataOutputTypeDef",
    ) -> "dc_td.UpdateQAppSessionMetadataOutput":
        return dc_td.UpdateQAppSessionMetadataOutput.make_one(res)


qapps_caster = QAPPSCaster()
