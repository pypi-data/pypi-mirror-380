# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_medical_imaging import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CopyDestinationImageSetProperties:
    boto3_raw_data: "type_defs.CopyDestinationImageSetPropertiesTypeDef" = (
        dataclasses.field()
    )

    imageSetId = field("imageSetId")
    latestVersionId = field("latestVersionId")
    imageSetState = field("imageSetState")
    imageSetWorkflowStatus = field("imageSetWorkflowStatus")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    imageSetArn = field("imageSetArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CopyDestinationImageSetPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDestinationImageSetPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDestinationImageSet:
    boto3_raw_data: "type_defs.CopyDestinationImageSetTypeDef" = dataclasses.field()

    imageSetId = field("imageSetId")
    latestVersionId = field("latestVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDestinationImageSetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDestinationImageSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySourceImageSetProperties:
    boto3_raw_data: "type_defs.CopySourceImageSetPropertiesTypeDef" = (
        dataclasses.field()
    )

    imageSetId = field("imageSetId")
    latestVersionId = field("latestVersionId")
    imageSetState = field("imageSetState")
    imageSetWorkflowStatus = field("imageSetWorkflowStatus")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    imageSetArn = field("imageSetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopySourceImageSetPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopySourceImageSetPropertiesTypeDef"]
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
class MetadataCopies:
    boto3_raw_data: "type_defs.MetadataCopiesTypeDef" = dataclasses.field()

    copiableAttributes = field("copiableAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataCopiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetadataCopiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatastoreRequest:
    boto3_raw_data: "type_defs.CreateDatastoreRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    datastoreName = field("datastoreName")
    tags = field("tags")
    kmsKeyArn = field("kmsKeyArn")
    lambdaAuthorizerArn = field("lambdaAuthorizerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatastoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatastoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DICOMImportJobProperties:
    boto3_raw_data: "type_defs.DICOMImportJobPropertiesTypeDef" = dataclasses.field()

    jobId = field("jobId")
    jobName = field("jobName")
    jobStatus = field("jobStatus")
    datastoreId = field("datastoreId")
    dataAccessRoleArn = field("dataAccessRoleArn")
    inputS3Uri = field("inputS3Uri")
    outputS3Uri = field("outputS3Uri")
    endedAt = field("endedAt")
    submittedAt = field("submittedAt")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DICOMImportJobPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DICOMImportJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DICOMImportJobSummary:
    boto3_raw_data: "type_defs.DICOMImportJobSummaryTypeDef" = dataclasses.field()

    jobId = field("jobId")
    jobName = field("jobName")
    jobStatus = field("jobStatus")
    datastoreId = field("datastoreId")
    dataAccessRoleArn = field("dataAccessRoleArn")
    endedAt = field("endedAt")
    submittedAt = field("submittedAt")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DICOMImportJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DICOMImportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DICOMStudyDateAndTime:
    boto3_raw_data: "type_defs.DICOMStudyDateAndTimeTypeDef" = dataclasses.field()

    DICOMStudyDate = field("DICOMStudyDate")
    DICOMStudyTime = field("DICOMStudyTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DICOMStudyDateAndTimeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DICOMStudyDateAndTimeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DICOMTags:
    boto3_raw_data: "type_defs.DICOMTagsTypeDef" = dataclasses.field()

    DICOMPatientId = field("DICOMPatientId")
    DICOMPatientName = field("DICOMPatientName")
    DICOMPatientBirthDate = field("DICOMPatientBirthDate")
    DICOMPatientSex = field("DICOMPatientSex")
    DICOMStudyInstanceUID = field("DICOMStudyInstanceUID")
    DICOMStudyId = field("DICOMStudyId")
    DICOMStudyDescription = field("DICOMStudyDescription")
    DICOMNumberOfStudyRelatedSeries = field("DICOMNumberOfStudyRelatedSeries")
    DICOMNumberOfStudyRelatedInstances = field("DICOMNumberOfStudyRelatedInstances")
    DICOMAccessionNumber = field("DICOMAccessionNumber")
    DICOMSeriesInstanceUID = field("DICOMSeriesInstanceUID")
    DICOMSeriesModality = field("DICOMSeriesModality")
    DICOMSeriesBodyPart = field("DICOMSeriesBodyPart")
    DICOMSeriesNumber = field("DICOMSeriesNumber")
    DICOMStudyDate = field("DICOMStudyDate")
    DICOMStudyTime = field("DICOMStudyTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DICOMTagsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DICOMTagsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreProperties:
    boto3_raw_data: "type_defs.DatastorePropertiesTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    datastoreName = field("datastoreName")
    datastoreStatus = field("datastoreStatus")
    kmsKeyArn = field("kmsKeyArn")
    lambdaAuthorizerArn = field("lambdaAuthorizerArn")
    datastoreArn = field("datastoreArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatastorePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastorePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreSummary:
    boto3_raw_data: "type_defs.DatastoreSummaryTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    datastoreName = field("datastoreName")
    datastoreStatus = field("datastoreStatus")
    datastoreArn = field("datastoreArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatastoreSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastoreSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatastoreRequest:
    boto3_raw_data: "type_defs.DeleteDatastoreRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatastoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatastoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImageSetRequest:
    boto3_raw_data: "type_defs.DeleteImageSetRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    imageSetId = field("imageSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImageSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImageSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDICOMImportJobRequest:
    boto3_raw_data: "type_defs.GetDICOMImportJobRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDICOMImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDICOMImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDatastoreRequest:
    boto3_raw_data: "type_defs.GetDatastoreRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDatastoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDatastoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageFrameInformation:
    boto3_raw_data: "type_defs.ImageFrameInformationTypeDef" = dataclasses.field()

    imageFrameId = field("imageFrameId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageFrameInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageFrameInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageSetMetadataRequest:
    boto3_raw_data: "type_defs.GetImageSetMetadataRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    imageSetId = field("imageSetId")
    versionId = field("versionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImageSetMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageSetMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageSetRequest:
    boto3_raw_data: "type_defs.GetImageSetRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    imageSetId = field("imageSetId")
    versionId = field("versionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImageSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Overrides:
    boto3_raw_data: "type_defs.OverridesTypeDef" = dataclasses.field()

    forced = field("forced")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OverridesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OverridesTypeDef"]]
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
class ListDICOMImportJobsRequest:
    boto3_raw_data: "type_defs.ListDICOMImportJobsRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    jobStatus = field("jobStatus")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDICOMImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDICOMImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatastoresRequest:
    boto3_raw_data: "type_defs.ListDatastoresRequestTypeDef" = dataclasses.field()

    datastoreStatus = field("datastoreStatus")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatastoresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatastoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageSetVersionsRequest:
    boto3_raw_data: "type_defs.ListImageSetVersionsRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    imageSetId = field("imageSetId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImageSetVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageSetVersionsRequestTypeDef"]
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
class Sort:
    boto3_raw_data: "type_defs.SortTypeDef" = dataclasses.field()

    sortOrder = field("sortOrder")
    sortField = field("sortField")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDICOMImportJobRequest:
    boto3_raw_data: "type_defs.StartDICOMImportJobRequestTypeDef" = dataclasses.field()

    dataAccessRoleArn = field("dataAccessRoleArn")
    clientToken = field("clientToken")
    datastoreId = field("datastoreId")
    inputS3Uri = field("inputS3Uri")
    outputS3Uri = field("outputS3Uri")
    jobName = field("jobName")
    inputOwnerAccountId = field("inputOwnerAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDICOMImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDICOMImportJobRequestTypeDef"]
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
class DICOMUpdates:
    boto3_raw_data: "type_defs.DICOMUpdatesTypeDef" = dataclasses.field()

    removableAttributes = field("removableAttributes")
    updatableAttributes = field("updatableAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DICOMUpdatesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DICOMUpdatesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyImageSetResponse:
    boto3_raw_data: "type_defs.CopyImageSetResponseTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")

    @cached_property
    def sourceImageSetProperties(self):  # pragma: no cover
        return CopySourceImageSetProperties.make_one(
            self.boto3_raw_data["sourceImageSetProperties"]
        )

    @cached_property
    def destinationImageSetProperties(self):  # pragma: no cover
        return CopyDestinationImageSetProperties.make_one(
            self.boto3_raw_data["destinationImageSetProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyImageSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyImageSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatastoreResponse:
    boto3_raw_data: "type_defs.CreateDatastoreResponseTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    datastoreStatus = field("datastoreStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatastoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatastoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatastoreResponse:
    boto3_raw_data: "type_defs.DeleteDatastoreResponseTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    datastoreStatus = field("datastoreStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatastoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatastoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImageSetResponse:
    boto3_raw_data: "type_defs.DeleteImageSetResponseTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    imageSetId = field("imageSetId")
    imageSetState = field("imageSetState")
    imageSetWorkflowStatus = field("imageSetWorkflowStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImageSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImageSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageFrameResponse:
    boto3_raw_data: "type_defs.GetImageFrameResponseTypeDef" = dataclasses.field()

    imageFrameBlob = field("imageFrameBlob")
    contentType = field("contentType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImageFrameResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageFrameResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageSetMetadataResponse:
    boto3_raw_data: "type_defs.GetImageSetMetadataResponseTypeDef" = dataclasses.field()

    imageSetMetadataBlob = field("imageSetMetadataBlob")
    contentType = field("contentType")
    contentEncoding = field("contentEncoding")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImageSetMetadataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageSetMetadataResponseTypeDef"]
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
class StartDICOMImportJobResponse:
    boto3_raw_data: "type_defs.StartDICOMImportJobResponseTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    jobId = field("jobId")
    jobStatus = field("jobStatus")
    submittedAt = field("submittedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDICOMImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDICOMImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateImageSetMetadataResponse:
    boto3_raw_data: "type_defs.UpdateImageSetMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    datastoreId = field("datastoreId")
    imageSetId = field("imageSetId")
    latestVersionId = field("latestVersionId")
    imageSetState = field("imageSetState")
    imageSetWorkflowStatus = field("imageSetWorkflowStatus")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateImageSetMetadataResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateImageSetMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySourceImageSetInformation:
    boto3_raw_data: "type_defs.CopySourceImageSetInformationTypeDef" = (
        dataclasses.field()
    )

    latestVersionId = field("latestVersionId")

    @cached_property
    def DICOMCopies(self):  # pragma: no cover
        return MetadataCopies.make_one(self.boto3_raw_data["DICOMCopies"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CopySourceImageSetInformationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopySourceImageSetInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDICOMImportJobResponse:
    boto3_raw_data: "type_defs.GetDICOMImportJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobProperties(self):  # pragma: no cover
        return DICOMImportJobProperties.make_one(self.boto3_raw_data["jobProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDICOMImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDICOMImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDICOMImportJobsResponse:
    boto3_raw_data: "type_defs.ListDICOMImportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobSummaries(self):  # pragma: no cover
        return DICOMImportJobSummary.make_many(self.boto3_raw_data["jobSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDICOMImportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDICOMImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageSetsMetadataSummary:
    boto3_raw_data: "type_defs.ImageSetsMetadataSummaryTypeDef" = dataclasses.field()

    imageSetId = field("imageSetId")
    version = field("version")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def DICOMTags(self):  # pragma: no cover
        return DICOMTags.make_one(self.boto3_raw_data["DICOMTags"])

    isPrimary = field("isPrimary")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageSetsMetadataSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageSetsMetadataSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDatastoreResponse:
    boto3_raw_data: "type_defs.GetDatastoreResponseTypeDef" = dataclasses.field()

    @cached_property
    def datastoreProperties(self):  # pragma: no cover
        return DatastoreProperties.make_one(self.boto3_raw_data["datastoreProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDatastoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDatastoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatastoresResponse:
    boto3_raw_data: "type_defs.ListDatastoresResponseTypeDef" = dataclasses.field()

    @cached_property
    def datastoreSummaries(self):  # pragma: no cover
        return DatastoreSummary.make_many(self.boto3_raw_data["datastoreSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatastoresResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatastoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageFrameRequest:
    boto3_raw_data: "type_defs.GetImageFrameRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    imageSetId = field("imageSetId")

    @cached_property
    def imageFrameInformation(self):  # pragma: no cover
        return ImageFrameInformation.make_one(
            self.boto3_raw_data["imageFrameInformation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImageFrameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageFrameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageSetResponse:
    boto3_raw_data: "type_defs.GetImageSetResponseTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    imageSetId = field("imageSetId")
    versionId = field("versionId")
    imageSetState = field("imageSetState")
    imageSetWorkflowStatus = field("imageSetWorkflowStatus")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    deletedAt = field("deletedAt")
    message = field("message")
    imageSetArn = field("imageSetArn")

    @cached_property
    def overrides(self):  # pragma: no cover
        return Overrides.make_one(self.boto3_raw_data["overrides"])

    isPrimary = field("isPrimary")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImageSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageSetProperties:
    boto3_raw_data: "type_defs.ImageSetPropertiesTypeDef" = dataclasses.field()

    imageSetId = field("imageSetId")
    versionId = field("versionId")
    imageSetState = field("imageSetState")
    ImageSetWorkflowStatus = field("ImageSetWorkflowStatus")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    deletedAt = field("deletedAt")
    message = field("message")

    @cached_property
    def overrides(self):  # pragma: no cover
        return Overrides.make_one(self.boto3_raw_data["overrides"])

    isPrimary = field("isPrimary")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageSetPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageSetPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDICOMImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListDICOMImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datastoreId = field("datastoreId")
    jobStatus = field("jobStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDICOMImportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDICOMImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatastoresRequestPaginate:
    boto3_raw_data: "type_defs.ListDatastoresRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datastoreStatus = field("datastoreStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDatastoresRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatastoresRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageSetVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListImageSetVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datastoreId = field("datastoreId")
    imageSetId = field("imageSetId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImageSetVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageSetVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchByAttributeValue:
    boto3_raw_data: "type_defs.SearchByAttributeValueTypeDef" = dataclasses.field()

    DICOMPatientId = field("DICOMPatientId")
    DICOMAccessionNumber = field("DICOMAccessionNumber")
    DICOMStudyId = field("DICOMStudyId")
    DICOMStudyInstanceUID = field("DICOMStudyInstanceUID")
    DICOMSeriesInstanceUID = field("DICOMSeriesInstanceUID")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def DICOMStudyDateAndTime(self):  # pragma: no cover
        return DICOMStudyDateAndTime.make_one(
            self.boto3_raw_data["DICOMStudyDateAndTime"]
        )

    isPrimary = field("isPrimary")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchByAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchByAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataUpdates:
    boto3_raw_data: "type_defs.MetadataUpdatesTypeDef" = dataclasses.field()

    @cached_property
    def DICOMUpdates(self):  # pragma: no cover
        return DICOMUpdates.make_one(self.boto3_raw_data["DICOMUpdates"])

    revertToVersionId = field("revertToVersionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataUpdatesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetadataUpdatesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyImageSetInformation:
    boto3_raw_data: "type_defs.CopyImageSetInformationTypeDef" = dataclasses.field()

    @cached_property
    def sourceImageSet(self):  # pragma: no cover
        return CopySourceImageSetInformation.make_one(
            self.boto3_raw_data["sourceImageSet"]
        )

    @cached_property
    def destinationImageSet(self):  # pragma: no cover
        return CopyDestinationImageSet.make_one(
            self.boto3_raw_data["destinationImageSet"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyImageSetInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyImageSetInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchImageSetsResponse:
    boto3_raw_data: "type_defs.SearchImageSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def imageSetsMetadataSummaries(self):  # pragma: no cover
        return ImageSetsMetadataSummary.make_many(
            self.boto3_raw_data["imageSetsMetadataSummaries"]
        )

    @cached_property
    def sort(self):  # pragma: no cover
        return Sort.make_one(self.boto3_raw_data["sort"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchImageSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchImageSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageSetVersionsResponse:
    boto3_raw_data: "type_defs.ListImageSetVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def imageSetPropertiesList(self):  # pragma: no cover
        return ImageSetProperties.make_many(
            self.boto3_raw_data["imageSetPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImageSetVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageSetVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchFilter:
    boto3_raw_data: "type_defs.SearchFilterTypeDef" = dataclasses.field()

    @cached_property
    def values(self):  # pragma: no cover
        return SearchByAttributeValue.make_many(self.boto3_raw_data["values"])

    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateImageSetMetadataRequest:
    boto3_raw_data: "type_defs.UpdateImageSetMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    datastoreId = field("datastoreId")
    imageSetId = field("imageSetId")
    latestVersionId = field("latestVersionId")

    @cached_property
    def updateImageSetMetadataUpdates(self):  # pragma: no cover
        return MetadataUpdates.make_one(
            self.boto3_raw_data["updateImageSetMetadataUpdates"]
        )

    force = field("force")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateImageSetMetadataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateImageSetMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyImageSetRequest:
    boto3_raw_data: "type_defs.CopyImageSetRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")
    sourceImageSetId = field("sourceImageSetId")

    @cached_property
    def copyImageSetInformation(self):  # pragma: no cover
        return CopyImageSetInformation.make_one(
            self.boto3_raw_data["copyImageSetInformation"]
        )

    force = field("force")
    promoteToPrimary = field("promoteToPrimary")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyImageSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyImageSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchCriteria:
    boto3_raw_data: "type_defs.SearchCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return SearchFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def sort(self):  # pragma: no cover
        return Sort.make_one(self.boto3_raw_data["sort"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchImageSetsRequestPaginate:
    boto3_raw_data: "type_defs.SearchImageSetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datastoreId = field("datastoreId")

    @cached_property
    def searchCriteria(self):  # pragma: no cover
        return SearchCriteria.make_one(self.boto3_raw_data["searchCriteria"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchImageSetsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchImageSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchImageSetsRequest:
    boto3_raw_data: "type_defs.SearchImageSetsRequestTypeDef" = dataclasses.field()

    datastoreId = field("datastoreId")

    @cached_property
    def searchCriteria(self):  # pragma: no cover
        return SearchCriteria.make_one(self.boto3_raw_data["searchCriteria"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchImageSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchImageSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
