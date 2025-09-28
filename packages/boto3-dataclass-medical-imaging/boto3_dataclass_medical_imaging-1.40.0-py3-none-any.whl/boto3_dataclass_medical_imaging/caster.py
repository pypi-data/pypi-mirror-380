# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_medical_imaging import type_defs as bs_td


class MEDICAL_IMAGINGCaster:

    def copy_image_set(
        self,
        res: "bs_td.CopyImageSetResponseTypeDef",
    ) -> "dc_td.CopyImageSetResponse":
        return dc_td.CopyImageSetResponse.make_one(res)

    def create_datastore(
        self,
        res: "bs_td.CreateDatastoreResponseTypeDef",
    ) -> "dc_td.CreateDatastoreResponse":
        return dc_td.CreateDatastoreResponse.make_one(res)

    def delete_datastore(
        self,
        res: "bs_td.DeleteDatastoreResponseTypeDef",
    ) -> "dc_td.DeleteDatastoreResponse":
        return dc_td.DeleteDatastoreResponse.make_one(res)

    def delete_image_set(
        self,
        res: "bs_td.DeleteImageSetResponseTypeDef",
    ) -> "dc_td.DeleteImageSetResponse":
        return dc_td.DeleteImageSetResponse.make_one(res)

    def get_dicom_import_job(
        self,
        res: "bs_td.GetDICOMImportJobResponseTypeDef",
    ) -> "dc_td.GetDICOMImportJobResponse":
        return dc_td.GetDICOMImportJobResponse.make_one(res)

    def get_datastore(
        self,
        res: "bs_td.GetDatastoreResponseTypeDef",
    ) -> "dc_td.GetDatastoreResponse":
        return dc_td.GetDatastoreResponse.make_one(res)

    def get_image_frame(
        self,
        res: "bs_td.GetImageFrameResponseTypeDef",
    ) -> "dc_td.GetImageFrameResponse":
        return dc_td.GetImageFrameResponse.make_one(res)

    def get_image_set(
        self,
        res: "bs_td.GetImageSetResponseTypeDef",
    ) -> "dc_td.GetImageSetResponse":
        return dc_td.GetImageSetResponse.make_one(res)

    def get_image_set_metadata(
        self,
        res: "bs_td.GetImageSetMetadataResponseTypeDef",
    ) -> "dc_td.GetImageSetMetadataResponse":
        return dc_td.GetImageSetMetadataResponse.make_one(res)

    def list_dicom_import_jobs(
        self,
        res: "bs_td.ListDICOMImportJobsResponseTypeDef",
    ) -> "dc_td.ListDICOMImportJobsResponse":
        return dc_td.ListDICOMImportJobsResponse.make_one(res)

    def list_datastores(
        self,
        res: "bs_td.ListDatastoresResponseTypeDef",
    ) -> "dc_td.ListDatastoresResponse":
        return dc_td.ListDatastoresResponse.make_one(res)

    def list_image_set_versions(
        self,
        res: "bs_td.ListImageSetVersionsResponseTypeDef",
    ) -> "dc_td.ListImageSetVersionsResponse":
        return dc_td.ListImageSetVersionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def search_image_sets(
        self,
        res: "bs_td.SearchImageSetsResponseTypeDef",
    ) -> "dc_td.SearchImageSetsResponse":
        return dc_td.SearchImageSetsResponse.make_one(res)

    def start_dicom_import_job(
        self,
        res: "bs_td.StartDICOMImportJobResponseTypeDef",
    ) -> "dc_td.StartDICOMImportJobResponse":
        return dc_td.StartDICOMImportJobResponse.make_one(res)

    def update_image_set_metadata(
        self,
        res: "bs_td.UpdateImageSetMetadataResponseTypeDef",
    ) -> "dc_td.UpdateImageSetMetadataResponse":
        return dc_td.UpdateImageSetMetadataResponse.make_one(res)


medical_imaging_caster = MEDICAL_IMAGINGCaster()
