# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_omics import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AbortMultipartReadSetUploadRequest:
    boto3_raw_data: "type_defs.AbortMultipartReadSetUploadRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    uploadId = field("uploadId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AbortMultipartReadSetUploadRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortMultipartReadSetUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptShareRequest:
    boto3_raw_data: "type_defs.AcceptShareRequestTypeDef" = dataclasses.field()

    shareId = field("shareId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptShareRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptShareRequestTypeDef"]
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
class ActivateReadSetJobItem:
    boto3_raw_data: "type_defs.ActivateReadSetJobItemTypeDef" = dataclasses.field()

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")
    status = field("status")
    creationTime = field("creationTime")
    completionTime = field("completionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivateReadSetJobItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateReadSetJobItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateReadSetSourceItem:
    boto3_raw_data: "type_defs.ActivateReadSetSourceItemTypeDef" = dataclasses.field()

    readSetId = field("readSetId")
    status = field("status")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivateReadSetSourceItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateReadSetSourceItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnnotationImportItemDetail:
    boto3_raw_data: "type_defs.AnnotationImportItemDetailTypeDef" = dataclasses.field()

    source = field("source")
    jobStatus = field("jobStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnnotationImportItemDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnnotationImportItemDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnnotationImportItemSource:
    boto3_raw_data: "type_defs.AnnotationImportItemSourceTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnnotationImportItemSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnnotationImportItemSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnnotationImportJobItem:
    boto3_raw_data: "type_defs.AnnotationImportJobItemTypeDef" = dataclasses.field()

    id = field("id")
    destinationName = field("destinationName")
    versionName = field("versionName")
    roleArn = field("roleArn")
    status = field("status")
    creationTime = field("creationTime")
    updateTime = field("updateTime")
    completionTime = field("completionTime")
    runLeftNormalization = field("runLeftNormalization")
    annotationFields = field("annotationFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnnotationImportJobItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnnotationImportJobItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceItem:
    boto3_raw_data: "type_defs.ReferenceItemTypeDef" = dataclasses.field()

    referenceArn = field("referenceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReferenceItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReferenceItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SseConfig:
    boto3_raw_data: "type_defs.SseConfigTypeDef" = dataclasses.field()

    type = field("type")
    keyArn = field("keyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SseConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SseConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnnotationStoreVersionItem:
    boto3_raw_data: "type_defs.AnnotationStoreVersionItemTypeDef" = dataclasses.field()

    storeId = field("storeId")
    id = field("id")
    status = field("status")
    versionArn = field("versionArn")
    name = field("name")
    versionName = field("versionName")
    description = field("description")
    creationTime = field("creationTime")
    updateTime = field("updateTime")
    statusMessage = field("statusMessage")
    versionSizeBytes = field("versionSizeBytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnnotationStoreVersionItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnnotationStoreVersionItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteReadSetRequest:
    boto3_raw_data: "type_defs.BatchDeleteReadSetRequestTypeDef" = dataclasses.field()

    ids = field("ids")
    sequenceStoreId = field("sequenceStoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteReadSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteReadSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadSetBatchError:
    boto3_raw_data: "type_defs.ReadSetBatchErrorTypeDef" = dataclasses.field()

    id = field("id")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadSetBatchErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReadSetBatchErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelAnnotationImportRequest:
    boto3_raw_data: "type_defs.CancelAnnotationImportRequestTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelAnnotationImportRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelAnnotationImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelRunRequest:
    boto3_raw_data: "type_defs.CancelRunRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelRunRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelVariantImportRequest:
    boto3_raw_data: "type_defs.CancelVariantImportRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelVariantImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelVariantImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteReadSetUploadPartListItem:
    boto3_raw_data: "type_defs.CompleteReadSetUploadPartListItemTypeDef" = (
        dataclasses.field()
    )

    partNumber = field("partNumber")
    partSource = field("partSource")
    checksum = field("checksum")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompleteReadSetUploadPartListItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteReadSetUploadPartListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageMapping:
    boto3_raw_data: "type_defs.ImageMappingTypeDef" = dataclasses.field()

    sourceImage = field("sourceImage")
    destinationImage = field("destinationImage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistryMapping:
    boto3_raw_data: "type_defs.RegistryMappingTypeDef" = dataclasses.field()

    upstreamRegistryUrl = field("upstreamRegistryUrl")
    ecrRepositoryPrefix = field("ecrRepositoryPrefix")
    upstreamRepositoryPrefix = field("upstreamRepositoryPrefix")
    ecrAccountId = field("ecrAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegistryMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegistryMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultipartReadSetUploadRequest:
    boto3_raw_data: "type_defs.CreateMultipartReadSetUploadRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    sourceFileType = field("sourceFileType")
    subjectId = field("subjectId")
    sampleId = field("sampleId")
    name = field("name")
    clientToken = field("clientToken")
    generatedFrom = field("generatedFrom")
    referenceArn = field("referenceArn")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMultipartReadSetUploadRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultipartReadSetUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRunCacheRequest:
    boto3_raw_data: "type_defs.CreateRunCacheRequestTypeDef" = dataclasses.field()

    cacheS3Location = field("cacheS3Location")
    requestId = field("requestId")
    cacheBehavior = field("cacheBehavior")
    description = field("description")
    name = field("name")
    tags = field("tags")
    cacheBucketOwnerId = field("cacheBucketOwnerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRunCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRunCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRunGroupRequest:
    boto3_raw_data: "type_defs.CreateRunGroupRequestTypeDef" = dataclasses.field()

    requestId = field("requestId")
    name = field("name")
    maxCpus = field("maxCpus")
    maxRuns = field("maxRuns")
    maxDuration = field("maxDuration")
    tags = field("tags")
    maxGpus = field("maxGpus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRunGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRunGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessConfig:
    boto3_raw_data: "type_defs.S3AccessConfigTypeDef" = dataclasses.field()

    accessLogLocation = field("accessLogLocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3AccessConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3AccessConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SequenceStoreS3Access:
    boto3_raw_data: "type_defs.SequenceStoreS3AccessTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")
    s3AccessPointArn = field("s3AccessPointArn")
    accessLogLocation = field("accessLogLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SequenceStoreS3AccessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SequenceStoreS3AccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateShareRequest:
    boto3_raw_data: "type_defs.CreateShareRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    principalSubscriber = field("principalSubscriber")
    shareName = field("shareName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateShareRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateShareRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowParameter:
    boto3_raw_data: "type_defs.WorkflowParameterTypeDef" = dataclasses.field()

    description = field("description")
    optional = field("optional")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceReference:
    boto3_raw_data: "type_defs.SourceReferenceTypeDef" = dataclasses.field()

    type = field("type")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnnotationStoreRequest:
    boto3_raw_data: "type_defs.DeleteAnnotationStoreRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    force = field("force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAnnotationStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnnotationStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnnotationStoreVersionsRequest:
    boto3_raw_data: "type_defs.DeleteAnnotationStoreVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    versions = field("versions")
    force = field("force")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAnnotationStoreVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnnotationStoreVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersionDeleteError:
    boto3_raw_data: "type_defs.VersionDeleteErrorTypeDef" = dataclasses.field()

    versionName = field("versionName")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VersionDeleteErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VersionDeleteErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReferenceRequest:
    boto3_raw_data: "type_defs.DeleteReferenceRequestTypeDef" = dataclasses.field()

    id = field("id")
    referenceStoreId = field("referenceStoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReferenceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReferenceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReferenceStoreRequest:
    boto3_raw_data: "type_defs.DeleteReferenceStoreRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReferenceStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReferenceStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRunCacheRequest:
    boto3_raw_data: "type_defs.DeleteRunCacheRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRunCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRunCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRunGroupRequest:
    boto3_raw_data: "type_defs.DeleteRunGroupRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRunGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRunGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRunRequest:
    boto3_raw_data: "type_defs.DeleteRunRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRunRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteS3AccessPolicyRequest:
    boto3_raw_data: "type_defs.DeleteS3AccessPolicyRequestTypeDef" = dataclasses.field()

    s3AccessPointArn = field("s3AccessPointArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteS3AccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteS3AccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSequenceStoreRequest:
    boto3_raw_data: "type_defs.DeleteSequenceStoreRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSequenceStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSequenceStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteShareRequest:
    boto3_raw_data: "type_defs.DeleteShareRequestTypeDef" = dataclasses.field()

    shareId = field("shareId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteShareRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteShareRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVariantStoreRequest:
    boto3_raw_data: "type_defs.DeleteVariantStoreRequestTypeDef" = dataclasses.field()

    name = field("name")
    force = field("force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVariantStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVariantStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkflowRequest:
    boto3_raw_data: "type_defs.DeleteWorkflowRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkflowVersionRequest:
    boto3_raw_data: "type_defs.DeleteWorkflowVersionRequestTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    versionName = field("versionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkflowVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkflowVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ETag:
    boto3_raw_data: "type_defs.ETagTypeDef" = dataclasses.field()

    algorithm = field("algorithm")
    source1 = field("source1")
    source2 = field("source2")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ETagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ETagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportReadSetDetail:
    boto3_raw_data: "type_defs.ExportReadSetDetailTypeDef" = dataclasses.field()

    id = field("id")
    status = field("status")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportReadSetDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportReadSetDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportReadSetJobDetail:
    boto3_raw_data: "type_defs.ExportReadSetJobDetailTypeDef" = dataclasses.field()

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")
    destination = field("destination")
    status = field("status")
    creationTime = field("creationTime")
    completionTime = field("completionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportReadSetJobDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportReadSetJobDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportReadSet:
    boto3_raw_data: "type_defs.ExportReadSetTypeDef" = dataclasses.field()

    readSetId = field("readSetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportReadSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportReadSetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadSetS3Access:
    boto3_raw_data: "type_defs.ReadSetS3AccessTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadSetS3AccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReadSetS3AccessTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    resourceArns = field("resourceArns")
    status = field("status")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VcfOptions:
    boto3_raw_data: "type_defs.VcfOptionsTypeDef" = dataclasses.field()

    ignoreQualField = field("ignoreQualField")
    ignoreFilterField = field("ignoreFilterField")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VcfOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VcfOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationImportRequest:
    boto3_raw_data: "type_defs.GetAnnotationImportRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnnotationImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationStoreRequest:
    boto3_raw_data: "type_defs.GetAnnotationStoreRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnnotationStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationStoreVersionRequest:
    boto3_raw_data: "type_defs.GetAnnotationStoreVersionRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    versionName = field("versionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAnnotationStoreVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationStoreVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetActivationJobRequest:
    boto3_raw_data: "type_defs.GetReadSetActivationJobRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReadSetActivationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetActivationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetExportJobRequest:
    boto3_raw_data: "type_defs.GetReadSetExportJobRequestTypeDef" = dataclasses.field()

    sequenceStoreId = field("sequenceStoreId")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReadSetExportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetImportJobRequest:
    boto3_raw_data: "type_defs.GetReadSetImportJobRequestTypeDef" = dataclasses.field()

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReadSetImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetMetadataRequest:
    boto3_raw_data: "type_defs.GetReadSetMetadataRequestTypeDef" = dataclasses.field()

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReadSetMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SequenceInformation:
    boto3_raw_data: "type_defs.SequenceInformationTypeDef" = dataclasses.field()

    totalReadCount = field("totalReadCount")
    totalBaseCount = field("totalBaseCount")
    generatedFrom = field("generatedFrom")
    alignment = field("alignment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SequenceInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SequenceInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetRequest:
    boto3_raw_data: "type_defs.GetReadSetRequestTypeDef" = dataclasses.field()

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")
    partNumber = field("partNumber")
    file = field("file")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetReadSetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReferenceImportJobRequest:
    boto3_raw_data: "type_defs.GetReferenceImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    referenceStoreId = field("referenceStoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReferenceImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReferenceImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportReferenceSourceItem:
    boto3_raw_data: "type_defs.ImportReferenceSourceItemTypeDef" = dataclasses.field()

    status = field("status")
    sourceFile = field("sourceFile")
    statusMessage = field("statusMessage")
    name = field("name")
    description = field("description")
    tags = field("tags")
    referenceId = field("referenceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportReferenceSourceItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportReferenceSourceItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReferenceMetadataRequest:
    boto3_raw_data: "type_defs.GetReferenceMetadataRequestTypeDef" = dataclasses.field()

    id = field("id")
    referenceStoreId = field("referenceStoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReferenceMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReferenceMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReferenceRequest:
    boto3_raw_data: "type_defs.GetReferenceRequestTypeDef" = dataclasses.field()

    id = field("id")
    referenceStoreId = field("referenceStoreId")
    partNumber = field("partNumber")
    range = field("range")
    file = field("file")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReferenceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReferenceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReferenceStoreRequest:
    boto3_raw_data: "type_defs.GetReferenceStoreRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReferenceStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReferenceStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunCacheRequest:
    boto3_raw_data: "type_defs.GetRunCacheRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRunCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRunCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunGroupRequest:
    boto3_raw_data: "type_defs.GetRunGroupRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRunGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRunGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunRequest:
    boto3_raw_data: "type_defs.GetRunRequestTypeDef" = dataclasses.field()

    id = field("id")
    export = field("export")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRunRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRunRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunLogLocation:
    boto3_raw_data: "type_defs.RunLogLocationTypeDef" = dataclasses.field()

    engineLogStream = field("engineLogStream")
    runLogStream = field("runLogStream")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunLogLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RunLogLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunTaskRequest:
    boto3_raw_data: "type_defs.GetRunTaskRequestTypeDef" = dataclasses.field()

    id = field("id")
    taskId = field("taskId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRunTaskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRunTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageDetails:
    boto3_raw_data: "type_defs.ImageDetailsTypeDef" = dataclasses.field()

    image = field("image")
    imageDigest = field("imageDigest")
    sourceImage = field("sourceImage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetS3AccessPolicyRequest:
    boto3_raw_data: "type_defs.GetS3AccessPolicyRequestTypeDef" = dataclasses.field()

    s3AccessPointArn = field("s3AccessPointArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetS3AccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetS3AccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSequenceStoreRequest:
    boto3_raw_data: "type_defs.GetSequenceStoreRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSequenceStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSequenceStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetShareRequest:
    boto3_raw_data: "type_defs.GetShareRequestTypeDef" = dataclasses.field()

    shareId = field("shareId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetShareRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetShareRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareDetails:
    boto3_raw_data: "type_defs.ShareDetailsTypeDef" = dataclasses.field()

    shareId = field("shareId")
    resourceArn = field("resourceArn")
    resourceId = field("resourceId")
    principalSubscriber = field("principalSubscriber")
    ownerId = field("ownerId")
    status = field("status")
    statusMessage = field("statusMessage")
    shareName = field("shareName")
    creationTime = field("creationTime")
    updateTime = field("updateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShareDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShareDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVariantImportRequest:
    boto3_raw_data: "type_defs.GetVariantImportRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVariantImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVariantImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariantImportItemDetail:
    boto3_raw_data: "type_defs.VariantImportItemDetailTypeDef" = dataclasses.field()

    source = field("source")
    jobStatus = field("jobStatus")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VariantImportItemDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VariantImportItemDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVariantStoreRequest:
    boto3_raw_data: "type_defs.GetVariantStoreRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVariantStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVariantStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowRequest:
    boto3_raw_data: "type_defs.GetWorkflowRequestTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    export = field("export")
    workflowOwnerId = field("workflowOwnerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowVersionRequest:
    boto3_raw_data: "type_defs.GetWorkflowVersionRequestTypeDef" = dataclasses.field()

    workflowId = field("workflowId")
    versionName = field("versionName")
    type = field("type")
    export = field("export")
    workflowOwnerId = field("workflowOwnerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportReadSetJobItem:
    boto3_raw_data: "type_defs.ImportReadSetJobItemTypeDef" = dataclasses.field()

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")
    roleArn = field("roleArn")
    status = field("status")
    creationTime = field("creationTime")
    completionTime = field("completionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportReadSetJobItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportReadSetJobItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceFiles:
    boto3_raw_data: "type_defs.SourceFilesTypeDef" = dataclasses.field()

    source1 = field("source1")
    source2 = field("source2")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceFilesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceFilesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportReferenceJobItem:
    boto3_raw_data: "type_defs.ImportReferenceJobItemTypeDef" = dataclasses.field()

    id = field("id")
    referenceStoreId = field("referenceStoreId")
    roleArn = field("roleArn")
    status = field("status")
    creationTime = field("creationTime")
    completionTime = field("completionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportReferenceJobItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportReferenceJobItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationImportJobsFilter:
    boto3_raw_data: "type_defs.ListAnnotationImportJobsFilterTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    storeName = field("storeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnnotationImportJobsFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationImportJobsFilterTypeDef"]
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
class ListAnnotationStoreVersionsFilter:
    boto3_raw_data: "type_defs.ListAnnotationStoreVersionsFilterTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnnotationStoreVersionsFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationStoreVersionsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationStoresFilter:
    boto3_raw_data: "type_defs.ListAnnotationStoresFilterTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnnotationStoresFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationStoresFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultipartReadSetUploadsRequest:
    boto3_raw_data: "type_defs.ListMultipartReadSetUploadsRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMultipartReadSetUploadsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultipartReadSetUploadsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultipartReadSetUploadListItem:
    boto3_raw_data: "type_defs.MultipartReadSetUploadListItemTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    uploadId = field("uploadId")
    sourceFileType = field("sourceFileType")
    subjectId = field("subjectId")
    sampleId = field("sampleId")
    generatedFrom = field("generatedFrom")
    referenceArn = field("referenceArn")
    creationTime = field("creationTime")
    name = field("name")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MultipartReadSetUploadListItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultipartReadSetUploadListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadSetUploadPartListItem:
    boto3_raw_data: "type_defs.ReadSetUploadPartListItemTypeDef" = dataclasses.field()

    partNumber = field("partNumber")
    partSize = field("partSize")
    partSource = field("partSource")
    checksum = field("checksum")
    creationTime = field("creationTime")
    lastUpdatedTime = field("lastUpdatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReadSetUploadPartListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReadSetUploadPartListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceListItem:
    boto3_raw_data: "type_defs.ReferenceListItemTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    referenceStoreId = field("referenceStoreId")
    md5 = field("md5")
    creationTime = field("creationTime")
    updateTime = field("updateTime")
    status = field("status")
    name = field("name")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReferenceListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunCachesRequest:
    boto3_raw_data: "type_defs.ListRunCachesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    startingToken = field("startingToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRunCachesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunCachesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunCacheListItem:
    boto3_raw_data: "type_defs.RunCacheListItemTypeDef" = dataclasses.field()

    arn = field("arn")
    cacheBehavior = field("cacheBehavior")
    cacheS3Uri = field("cacheS3Uri")
    creationTime = field("creationTime")
    id = field("id")
    name = field("name")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunCacheListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunCacheListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunGroupsRequest:
    boto3_raw_data: "type_defs.ListRunGroupsRequestTypeDef" = dataclasses.field()

    name = field("name")
    startingToken = field("startingToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRunGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunGroupListItem:
    boto3_raw_data: "type_defs.RunGroupListItemTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    name = field("name")
    maxCpus = field("maxCpus")
    maxRuns = field("maxRuns")
    maxDuration = field("maxDuration")
    creationTime = field("creationTime")
    maxGpus = field("maxGpus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunGroupListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunGroupListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunTasksRequest:
    boto3_raw_data: "type_defs.ListRunTasksRequestTypeDef" = dataclasses.field()

    id = field("id")
    status = field("status")
    startingToken = field("startingToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRunTasksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskListItem:
    boto3_raw_data: "type_defs.TaskListItemTypeDef" = dataclasses.field()

    taskId = field("taskId")
    status = field("status")
    name = field("name")
    cpus = field("cpus")
    cacheHit = field("cacheHit")
    cacheS3Uri = field("cacheS3Uri")
    memory = field("memory")
    creationTime = field("creationTime")
    startTime = field("startTime")
    stopTime = field("stopTime")
    gpus = field("gpus")
    instanceType = field("instanceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskListItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunsRequest:
    boto3_raw_data: "type_defs.ListRunsRequestTypeDef" = dataclasses.field()

    name = field("name")
    runGroupId = field("runGroupId")
    startingToken = field("startingToken")
    maxResults = field("maxResults")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRunsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListRunsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunListItem:
    boto3_raw_data: "type_defs.RunListItemTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    status = field("status")
    workflowId = field("workflowId")
    name = field("name")
    priority = field("priority")
    storageCapacity = field("storageCapacity")
    creationTime = field("creationTime")
    startTime = field("startTime")
    stopTime = field("stopTime")
    storageType = field("storageType")
    workflowVersionName = field("workflowVersionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RunListItemTypeDef"]]
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
class ListVariantImportJobsFilter:
    boto3_raw_data: "type_defs.ListVariantImportJobsFilterTypeDef" = dataclasses.field()

    status = field("status")
    storeName = field("storeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVariantImportJobsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVariantImportJobsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariantImportJobItem:
    boto3_raw_data: "type_defs.VariantImportJobItemTypeDef" = dataclasses.field()

    id = field("id")
    destinationName = field("destinationName")
    roleArn = field("roleArn")
    status = field("status")
    creationTime = field("creationTime")
    updateTime = field("updateTime")
    completionTime = field("completionTime")
    runLeftNormalization = field("runLeftNormalization")
    annotationFields = field("annotationFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VariantImportJobItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VariantImportJobItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVariantStoresFilter:
    boto3_raw_data: "type_defs.ListVariantStoresFilterTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVariantStoresFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVariantStoresFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowVersionsRequest:
    boto3_raw_data: "type_defs.ListWorkflowVersionsRequestTypeDef" = dataclasses.field()

    workflowId = field("workflowId")
    type = field("type")
    workflowOwnerId = field("workflowOwnerId")
    startingToken = field("startingToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowVersionListItem:
    boto3_raw_data: "type_defs.WorkflowVersionListItemTypeDef" = dataclasses.field()

    arn = field("arn")
    workflowId = field("workflowId")
    versionName = field("versionName")
    description = field("description")
    status = field("status")
    type = field("type")
    digest = field("digest")
    creationTime = field("creationTime")
    metadata = field("metadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowVersionListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowVersionListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsRequest:
    boto3_raw_data: "type_defs.ListWorkflowsRequestTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    startingToken = field("startingToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowListItem:
    boto3_raw_data: "type_defs.WorkflowListItemTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    name = field("name")
    status = field("status")
    type = field("type")
    digest = field("digest")
    creationTime = field("creationTime")
    metadata = field("metadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutS3AccessPolicyRequest:
    boto3_raw_data: "type_defs.PutS3AccessPolicyRequestTypeDef" = dataclasses.field()

    s3AccessPointArn = field("s3AccessPointArn")
    s3AccessPolicy = field("s3AccessPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutS3AccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutS3AccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadOptions:
    boto3_raw_data: "type_defs.ReadOptionsTypeDef" = dataclasses.field()

    sep = field("sep")
    encoding = field("encoding")
    quote = field("quote")
    quoteAll = field("quoteAll")
    escape = field("escape")
    escapeQuotes = field("escapeQuotes")
    comment = field("comment")
    header = field("header")
    lineSep = field("lineSep")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReadOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReadSetActivationJobSourceItem:
    boto3_raw_data: "type_defs.StartReadSetActivationJobSourceItemTypeDef" = (
        dataclasses.field()
    )

    readSetId = field("readSetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartReadSetActivationJobSourceItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReadSetActivationJobSourceItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReferenceImportJobSourceItem:
    boto3_raw_data: "type_defs.StartReferenceImportJobSourceItemTypeDef" = (
        dataclasses.field()
    )

    sourceFile = field("sourceFile")
    name = field("name")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartReferenceImportJobSourceItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReferenceImportJobSourceItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRunRequest:
    boto3_raw_data: "type_defs.StartRunRequestTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    outputUri = field("outputUri")
    requestId = field("requestId")
    workflowId = field("workflowId")
    workflowType = field("workflowType")
    runId = field("runId")
    name = field("name")
    cacheId = field("cacheId")
    cacheBehavior = field("cacheBehavior")
    runGroupId = field("runGroupId")
    priority = field("priority")
    parameters = field("parameters")
    storageCapacity = field("storageCapacity")
    logLevel = field("logLevel")
    tags = field("tags")
    retentionMode = field("retentionMode")
    storageType = field("storageType")
    workflowOwnerId = field("workflowOwnerId")
    workflowVersionName = field("workflowVersionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartRunRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartRunRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariantImportItemSource:
    boto3_raw_data: "type_defs.VariantImportItemSourceTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VariantImportItemSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VariantImportItemSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TsvStoreOptionsOutput:
    boto3_raw_data: "type_defs.TsvStoreOptionsOutputTypeDef" = dataclasses.field()

    annotationType = field("annotationType")
    formatToHeader = field("formatToHeader")
    schema = field("schema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TsvStoreOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TsvStoreOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TsvStoreOptions:
    boto3_raw_data: "type_defs.TsvStoreOptionsTypeDef" = dataclasses.field()

    annotationType = field("annotationType")
    formatToHeader = field("formatToHeader")
    schema = field("schema")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TsvStoreOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TsvStoreOptionsTypeDef"]],
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
class TsvVersionOptionsOutput:
    boto3_raw_data: "type_defs.TsvVersionOptionsOutputTypeDef" = dataclasses.field()

    annotationType = field("annotationType")
    formatToHeader = field("formatToHeader")
    schema = field("schema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TsvVersionOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TsvVersionOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TsvVersionOptions:
    boto3_raw_data: "type_defs.TsvVersionOptionsTypeDef" = dataclasses.field()

    annotationType = field("annotationType")
    formatToHeader = field("formatToHeader")
    schema = field("schema")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TsvVersionOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TsvVersionOptionsTypeDef"]
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
class UpdateAnnotationStoreRequest:
    boto3_raw_data: "type_defs.UpdateAnnotationStoreRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAnnotationStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnnotationStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnnotationStoreVersionRequest:
    boto3_raw_data: "type_defs.UpdateAnnotationStoreVersionRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    versionName = field("versionName")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAnnotationStoreVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnnotationStoreVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRunCacheRequest:
    boto3_raw_data: "type_defs.UpdateRunCacheRequestTypeDef" = dataclasses.field()

    id = field("id")
    cacheBehavior = field("cacheBehavior")
    description = field("description")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRunCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRunCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRunGroupRequest:
    boto3_raw_data: "type_defs.UpdateRunGroupRequestTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    maxCpus = field("maxCpus")
    maxRuns = field("maxRuns")
    maxDuration = field("maxDuration")
    maxGpus = field("maxGpus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRunGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRunGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVariantStoreRequest:
    boto3_raw_data: "type_defs.UpdateVariantStoreRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVariantStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVariantStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkflowRequest:
    boto3_raw_data: "type_defs.UpdateWorkflowRequestTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    storageType = field("storageType")
    storageCapacity = field("storageCapacity")
    readmeMarkdown = field("readmeMarkdown")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkflowVersionRequest:
    boto3_raw_data: "type_defs.UpdateWorkflowVersionRequestTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    versionName = field("versionName")
    description = field("description")
    storageType = field("storageType")
    storageCapacity = field("storageCapacity")
    readmeMarkdown = field("readmeMarkdown")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkflowVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkflowVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptShareResponse:
    boto3_raw_data: "type_defs.AcceptShareResponseTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptShareResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptShareResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteMultipartReadSetUploadResponse:
    boto3_raw_data: "type_defs.CompleteMultipartReadSetUploadResponseTypeDef" = (
        dataclasses.field()
    )

    readSetId = field("readSetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompleteMultipartReadSetUploadResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteMultipartReadSetUploadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultipartReadSetUploadResponse:
    boto3_raw_data: "type_defs.CreateMultipartReadSetUploadResponseTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    uploadId = field("uploadId")
    sourceFileType = field("sourceFileType")
    subjectId = field("subjectId")
    sampleId = field("sampleId")
    generatedFrom = field("generatedFrom")
    referenceArn = field("referenceArn")
    name = field("name")
    description = field("description")
    tags = field("tags")
    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMultipartReadSetUploadResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultipartReadSetUploadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRunCacheResponse:
    boto3_raw_data: "type_defs.CreateRunCacheResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    status = field("status")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRunCacheResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRunCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRunGroupResponse:
    boto3_raw_data: "type_defs.CreateRunGroupResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRunGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRunGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateShareResponse:
    boto3_raw_data: "type_defs.CreateShareResponseTypeDef" = dataclasses.field()

    shareId = field("shareId")
    status = field("status")
    shareName = field("shareName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateShareResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateShareResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowResponse:
    boto3_raw_data: "type_defs.CreateWorkflowResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    status = field("status")
    tags = field("tags")
    uuid = field("uuid")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkflowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowVersionResponse:
    boto3_raw_data: "type_defs.CreateWorkflowVersionResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    workflowId = field("workflowId")
    versionName = field("versionName")
    status = field("status")
    tags = field("tags")
    uuid = field("uuid")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkflowVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnnotationStoreResponse:
    boto3_raw_data: "type_defs.DeleteAnnotationStoreResponseTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAnnotationStoreResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnnotationStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteShareResponse:
    boto3_raw_data: "type_defs.DeleteShareResponseTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteShareResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteShareResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVariantStoreResponse:
    boto3_raw_data: "type_defs.DeleteVariantStoreResponseTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVariantStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVariantStoreResponseTypeDef"]
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
class GetReadSetResponse:
    boto3_raw_data: "type_defs.GetReadSetResponseTypeDef" = dataclasses.field()

    payload = field("payload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReadSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReferenceResponse:
    boto3_raw_data: "type_defs.GetReferenceResponseTypeDef" = dataclasses.field()

    payload = field("payload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReferenceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReferenceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunCacheResponse:
    boto3_raw_data: "type_defs.GetRunCacheResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    cacheBehavior = field("cacheBehavior")
    cacheBucketOwnerId = field("cacheBucketOwnerId")
    cacheS3Uri = field("cacheS3Uri")
    creationTime = field("creationTime")
    description = field("description")
    id = field("id")
    name = field("name")
    status = field("status")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRunCacheResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRunCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunGroupResponse:
    boto3_raw_data: "type_defs.GetRunGroupResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    name = field("name")
    maxCpus = field("maxCpus")
    maxRuns = field("maxRuns")
    maxDuration = field("maxDuration")
    creationTime = field("creationTime")
    tags = field("tags")
    maxGpus = field("maxGpus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRunGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRunGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetS3AccessPolicyResponse:
    boto3_raw_data: "type_defs.GetS3AccessPolicyResponseTypeDef" = dataclasses.field()

    s3AccessPointArn = field("s3AccessPointArn")
    storeId = field("storeId")
    storeType = field("storeType")
    updateTime = field("updateTime")
    s3AccessPolicy = field("s3AccessPolicy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetS3AccessPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetS3AccessPolicyResponseTypeDef"]
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
class PutS3AccessPolicyResponse:
    boto3_raw_data: "type_defs.PutS3AccessPolicyResponseTypeDef" = dataclasses.field()

    s3AccessPointArn = field("s3AccessPointArn")
    storeId = field("storeId")
    storeType = field("storeType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutS3AccessPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutS3AccessPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAnnotationImportResponse:
    boto3_raw_data: "type_defs.StartAnnotationImportResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartAnnotationImportResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAnnotationImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReadSetActivationJobResponse:
    boto3_raw_data: "type_defs.StartReadSetActivationJobResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")
    status = field("status")
    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartReadSetActivationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReadSetActivationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReadSetExportJobResponse:
    boto3_raw_data: "type_defs.StartReadSetExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")
    destination = field("destination")
    status = field("status")
    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartReadSetExportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReadSetExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReadSetImportJobResponse:
    boto3_raw_data: "type_defs.StartReadSetImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")
    roleArn = field("roleArn")
    status = field("status")
    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartReadSetImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReadSetImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReferenceImportJobResponse:
    boto3_raw_data: "type_defs.StartReferenceImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    referenceStoreId = field("referenceStoreId")
    roleArn = field("roleArn")
    status = field("status")
    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartReferenceImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReferenceImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRunResponse:
    boto3_raw_data: "type_defs.StartRunResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    status = field("status")
    tags = field("tags")
    uuid = field("uuid")
    runOutputUri = field("runOutputUri")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartRunResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartVariantImportResponse:
    boto3_raw_data: "type_defs.StartVariantImportResponseTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartVariantImportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartVariantImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnnotationStoreVersionResponse:
    boto3_raw_data: "type_defs.UpdateAnnotationStoreVersionResponseTypeDef" = (
        dataclasses.field()
    )

    storeId = field("storeId")
    id = field("id")
    status = field("status")
    name = field("name")
    versionName = field("versionName")
    description = field("description")
    creationTime = field("creationTime")
    updateTime = field("updateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAnnotationStoreVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnnotationStoreVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadReadSetPartResponse:
    boto3_raw_data: "type_defs.UploadReadSetPartResponseTypeDef" = dataclasses.field()

    checksum = field("checksum")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadReadSetPartResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadReadSetPartResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateReadSetFilter:
    boto3_raw_data: "type_defs.ActivateReadSetFilterTypeDef" = dataclasses.field()

    status = field("status")
    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivateReadSetFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateReadSetFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportReadSetFilter:
    boto3_raw_data: "type_defs.ExportReadSetFilterTypeDef" = dataclasses.field()

    status = field("status")
    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportReadSetFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportReadSetFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportReadSetFilter:
    boto3_raw_data: "type_defs.ImportReadSetFilterTypeDef" = dataclasses.field()

    status = field("status")
    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportReadSetFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportReadSetFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportReferenceFilter:
    boto3_raw_data: "type_defs.ImportReferenceFilterTypeDef" = dataclasses.field()

    status = field("status")
    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportReferenceFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportReferenceFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadSetFilter:
    boto3_raw_data: "type_defs.ReadSetFilterTypeDef" = dataclasses.field()

    name = field("name")
    status = field("status")
    referenceArn = field("referenceArn")
    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")
    sampleId = field("sampleId")
    subjectId = field("subjectId")
    generatedFrom = field("generatedFrom")
    creationType = field("creationType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadSetFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReadSetFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadSetUploadPartListFilter:
    boto3_raw_data: "type_defs.ReadSetUploadPartListFilterTypeDef" = dataclasses.field()

    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReadSetUploadPartListFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReadSetUploadPartListFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceFilter:
    boto3_raw_data: "type_defs.ReferenceFilterTypeDef" = dataclasses.field()

    name = field("name")
    md5 = field("md5")
    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReferenceFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReferenceFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceStoreFilter:
    boto3_raw_data: "type_defs.ReferenceStoreFilterTypeDef" = dataclasses.field()

    name = field("name")
    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReferenceStoreFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceStoreFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SequenceStoreFilter:
    boto3_raw_data: "type_defs.SequenceStoreFilterTypeDef" = dataclasses.field()

    name = field("name")
    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")
    status = field("status")
    updatedAfter = field("updatedAfter")
    updatedBefore = field("updatedBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SequenceStoreFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SequenceStoreFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetActivationJobsResponse:
    boto3_raw_data: "type_defs.ListReadSetActivationJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def activationJobs(self):  # pragma: no cover
        return ActivateReadSetJobItem.make_many(self.boto3_raw_data["activationJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReadSetActivationJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetActivationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetActivationJobResponse:
    boto3_raw_data: "type_defs.GetReadSetActivationJobResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")
    status = field("status")
    statusMessage = field("statusMessage")
    creationTime = field("creationTime")
    completionTime = field("completionTime")

    @cached_property
    def sources(self):  # pragma: no cover
        return ActivateReadSetSourceItem.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReadSetActivationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetActivationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationImportJobsResponse:
    boto3_raw_data: "type_defs.ListAnnotationImportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def annotationImportJobs(self):  # pragma: no cover
        return AnnotationImportJobItem.make_many(
            self.boto3_raw_data["annotationImportJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnnotationImportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVariantStoreResponse:
    boto3_raw_data: "type_defs.CreateVariantStoreResponseTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def reference(self):  # pragma: no cover
        return ReferenceItem.make_one(self.boto3_raw_data["reference"])

    status = field("status")
    name = field("name")
    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVariantStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVariantStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVariantStoreResponse:
    boto3_raw_data: "type_defs.UpdateVariantStoreResponseTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def reference(self):  # pragma: no cover
        return ReferenceItem.make_one(self.boto3_raw_data["reference"])

    status = field("status")
    name = field("name")
    description = field("description")
    creationTime = field("creationTime")
    updateTime = field("updateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVariantStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVariantStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnnotationStoreItem:
    boto3_raw_data: "type_defs.AnnotationStoreItemTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def reference(self):  # pragma: no cover
        return ReferenceItem.make_one(self.boto3_raw_data["reference"])

    status = field("status")
    storeArn = field("storeArn")
    name = field("name")
    storeFormat = field("storeFormat")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    creationTime = field("creationTime")
    updateTime = field("updateTime")
    statusMessage = field("statusMessage")
    storeSizeBytes = field("storeSizeBytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnnotationStoreItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnnotationStoreItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReferenceStoreRequest:
    boto3_raw_data: "type_defs.CreateReferenceStoreRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    tags = field("tags")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReferenceStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReferenceStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReferenceStoreResponse:
    boto3_raw_data: "type_defs.CreateReferenceStoreResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReferenceStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReferenceStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVariantStoreRequest:
    boto3_raw_data: "type_defs.CreateVariantStoreRequestTypeDef" = dataclasses.field()

    @cached_property
    def reference(self):  # pragma: no cover
        return ReferenceItem.make_one(self.boto3_raw_data["reference"])

    name = field("name")
    description = field("description")
    tags = field("tags")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVariantStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVariantStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReferenceStoreResponse:
    boto3_raw_data: "type_defs.GetReferenceStoreResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReferenceStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReferenceStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVariantStoreResponse:
    boto3_raw_data: "type_defs.GetVariantStoreResponseTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def reference(self):  # pragma: no cover
        return ReferenceItem.make_one(self.boto3_raw_data["reference"])

    status = field("status")
    storeArn = field("storeArn")
    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    creationTime = field("creationTime")
    updateTime = field("updateTime")
    tags = field("tags")
    statusMessage = field("statusMessage")
    storeSizeBytes = field("storeSizeBytes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVariantStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVariantStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceStoreDetail:
    boto3_raw_data: "type_defs.ReferenceStoreDetailTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    creationTime = field("creationTime")
    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReferenceStoreDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceStoreDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SequenceStoreDetail:
    boto3_raw_data: "type_defs.SequenceStoreDetailTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    creationTime = field("creationTime")
    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    fallbackLocation = field("fallbackLocation")
    eTagAlgorithmFamily = field("eTagAlgorithmFamily")
    status = field("status")
    statusMessage = field("statusMessage")
    updateTime = field("updateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SequenceStoreDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SequenceStoreDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariantStoreItem:
    boto3_raw_data: "type_defs.VariantStoreItemTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def reference(self):  # pragma: no cover
        return ReferenceItem.make_one(self.boto3_raw_data["reference"])

    status = field("status")
    storeArn = field("storeArn")
    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    creationTime = field("creationTime")
    updateTime = field("updateTime")
    statusMessage = field("statusMessage")
    storeSizeBytes = field("storeSizeBytes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VariantStoreItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VariantStoreItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationStoreVersionsResponse:
    boto3_raw_data: "type_defs.ListAnnotationStoreVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def annotationStoreVersions(self):  # pragma: no cover
        return AnnotationStoreVersionItem.make_many(
            self.boto3_raw_data["annotationStoreVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnnotationStoreVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationStoreVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteReadSetResponse:
    boto3_raw_data: "type_defs.BatchDeleteReadSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def errors(self):  # pragma: no cover
        return ReadSetBatchError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteReadSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteReadSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadReadSetPartRequest:
    boto3_raw_data: "type_defs.UploadReadSetPartRequestTypeDef" = dataclasses.field()

    sequenceStoreId = field("sequenceStoreId")
    uploadId = field("uploadId")
    partSource = field("partSource")
    partNumber = field("partNumber")
    payload = field("payload")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadReadSetPartRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadReadSetPartRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteMultipartReadSetUploadRequest:
    boto3_raw_data: "type_defs.CompleteMultipartReadSetUploadRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    uploadId = field("uploadId")

    @cached_property
    def parts(self):  # pragma: no cover
        return CompleteReadSetUploadPartListItem.make_many(self.boto3_raw_data["parts"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompleteMultipartReadSetUploadRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteMultipartReadSetUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerRegistryMapOutput:
    boto3_raw_data: "type_defs.ContainerRegistryMapOutputTypeDef" = dataclasses.field()

    @cached_property
    def registryMappings(self):  # pragma: no cover
        return RegistryMapping.make_many(self.boto3_raw_data["registryMappings"])

    @cached_property
    def imageMappings(self):  # pragma: no cover
        return ImageMapping.make_many(self.boto3_raw_data["imageMappings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerRegistryMapOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerRegistryMapOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerRegistryMap:
    boto3_raw_data: "type_defs.ContainerRegistryMapTypeDef" = dataclasses.field()

    @cached_property
    def registryMappings(self):  # pragma: no cover
        return RegistryMapping.make_many(self.boto3_raw_data["registryMappings"])

    @cached_property
    def imageMappings(self):  # pragma: no cover
        return ImageMapping.make_many(self.boto3_raw_data["imageMappings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerRegistryMapTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerRegistryMapTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSequenceStoreRequest:
    boto3_raw_data: "type_defs.CreateSequenceStoreRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    tags = field("tags")
    clientToken = field("clientToken")
    fallbackLocation = field("fallbackLocation")
    eTagAlgorithmFamily = field("eTagAlgorithmFamily")
    propagatedSetLevelTags = field("propagatedSetLevelTags")

    @cached_property
    def s3AccessConfig(self):  # pragma: no cover
        return S3AccessConfig.make_one(self.boto3_raw_data["s3AccessConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSequenceStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSequenceStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSequenceStoreRequest:
    boto3_raw_data: "type_defs.UpdateSequenceStoreRequestTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    clientToken = field("clientToken")
    fallbackLocation = field("fallbackLocation")
    propagatedSetLevelTags = field("propagatedSetLevelTags")

    @cached_property
    def s3AccessConfig(self):  # pragma: no cover
        return S3AccessConfig.make_one(self.boto3_raw_data["s3AccessConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSequenceStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSequenceStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSequenceStoreResponse:
    boto3_raw_data: "type_defs.CreateSequenceStoreResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    creationTime = field("creationTime")
    fallbackLocation = field("fallbackLocation")
    eTagAlgorithmFamily = field("eTagAlgorithmFamily")
    status = field("status")
    statusMessage = field("statusMessage")
    propagatedSetLevelTags = field("propagatedSetLevelTags")

    @cached_property
    def s3Access(self):  # pragma: no cover
        return SequenceStoreS3Access.make_one(self.boto3_raw_data["s3Access"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSequenceStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSequenceStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSequenceStoreResponse:
    boto3_raw_data: "type_defs.GetSequenceStoreResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    creationTime = field("creationTime")
    fallbackLocation = field("fallbackLocation")

    @cached_property
    def s3Access(self):  # pragma: no cover
        return SequenceStoreS3Access.make_one(self.boto3_raw_data["s3Access"])

    eTagAlgorithmFamily = field("eTagAlgorithmFamily")
    status = field("status")
    statusMessage = field("statusMessage")
    propagatedSetLevelTags = field("propagatedSetLevelTags")
    updateTime = field("updateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSequenceStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSequenceStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSequenceStoreResponse:
    boto3_raw_data: "type_defs.UpdateSequenceStoreResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    creationTime = field("creationTime")
    updateTime = field("updateTime")
    propagatedSetLevelTags = field("propagatedSetLevelTags")
    status = field("status")
    statusMessage = field("statusMessage")
    fallbackLocation = field("fallbackLocation")

    @cached_property
    def s3Access(self):  # pragma: no cover
        return SequenceStoreS3Access.make_one(self.boto3_raw_data["s3Access"])

    eTagAlgorithmFamily = field("eTagAlgorithmFamily")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSequenceStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSequenceStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefinitionRepositoryDetails:
    boto3_raw_data: "type_defs.DefinitionRepositoryDetailsTypeDef" = dataclasses.field()

    connectionArn = field("connectionArn")
    fullRepositoryId = field("fullRepositoryId")

    @cached_property
    def sourceReference(self):  # pragma: no cover
        return SourceReference.make_one(self.boto3_raw_data["sourceReference"])

    providerType = field("providerType")
    providerEndpoint = field("providerEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefinitionRepositoryDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefinitionRepositoryDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefinitionRepository:
    boto3_raw_data: "type_defs.DefinitionRepositoryTypeDef" = dataclasses.field()

    connectionArn = field("connectionArn")
    fullRepositoryId = field("fullRepositoryId")

    @cached_property
    def sourceReference(self):  # pragma: no cover
        return SourceReference.make_one(self.boto3_raw_data["sourceReference"])

    excludeFilePatterns = field("excludeFilePatterns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefinitionRepositoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefinitionRepositoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnnotationStoreVersionsResponse:
    boto3_raw_data: "type_defs.DeleteAnnotationStoreVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return VersionDeleteError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAnnotationStoreVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnnotationStoreVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetExportJobResponse:
    boto3_raw_data: "type_defs.GetReadSetExportJobResponseTypeDef" = dataclasses.field()

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")
    destination = field("destination")
    status = field("status")
    statusMessage = field("statusMessage")
    creationTime = field("creationTime")
    completionTime = field("completionTime")

    @cached_property
    def readSets(self):  # pragma: no cover
        return ExportReadSetDetail.make_many(self.boto3_raw_data["readSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReadSetExportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetExportJobsResponse:
    boto3_raw_data: "type_defs.ListReadSetExportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def exportJobs(self):  # pragma: no cover
        return ExportReadSetJobDetail.make_many(self.boto3_raw_data["exportJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReadSetExportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReadSetExportJobRequest:
    boto3_raw_data: "type_defs.StartReadSetExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    destination = field("destination")
    roleArn = field("roleArn")

    @cached_property
    def sources(self):  # pragma: no cover
        return ExportReadSet.make_many(self.boto3_raw_data["sources"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReadSetExportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReadSetExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileInformation:
    boto3_raw_data: "type_defs.FileInformationTypeDef" = dataclasses.field()

    totalParts = field("totalParts")
    partSize = field("partSize")
    contentLength = field("contentLength")

    @cached_property
    def s3Access(self):  # pragma: no cover
        return ReadSetS3Access.make_one(self.boto3_raw_data["s3Access"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileInformationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSharesRequest:
    boto3_raw_data: "type_defs.ListSharesRequestTypeDef" = dataclasses.field()

    resourceOwner = field("resourceOwner")

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListSharesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSharesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationImportRequestWait:
    boto3_raw_data: "type_defs.GetAnnotationImportRequestWaitTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAnnotationImportRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationImportRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationStoreRequestWaitExtra:
    boto3_raw_data: "type_defs.GetAnnotationStoreRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAnnotationStoreRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationStoreRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationStoreRequestWait:
    boto3_raw_data: "type_defs.GetAnnotationStoreRequestWaitTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAnnotationStoreRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationStoreRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationStoreVersionRequestWaitExtra:
    boto3_raw_data: "type_defs.GetAnnotationStoreVersionRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    versionName = field("versionName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAnnotationStoreVersionRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationStoreVersionRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationStoreVersionRequestWait:
    boto3_raw_data: "type_defs.GetAnnotationStoreVersionRequestWaitTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    versionName = field("versionName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAnnotationStoreVersionRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationStoreVersionRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetActivationJobRequestWait:
    boto3_raw_data: "type_defs.GetReadSetActivationJobRequestWaitTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReadSetActivationJobRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetActivationJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetExportJobRequestWait:
    boto3_raw_data: "type_defs.GetReadSetExportJobRequestWaitTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    id = field("id")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReadSetExportJobRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetExportJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetImportJobRequestWait:
    boto3_raw_data: "type_defs.GetReadSetImportJobRequestWaitTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReadSetImportJobRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetImportJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReferenceImportJobRequestWait:
    boto3_raw_data: "type_defs.GetReferenceImportJobRequestWaitTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    referenceStoreId = field("referenceStoreId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReferenceImportJobRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReferenceImportJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunRequestWaitExtra:
    boto3_raw_data: "type_defs.GetRunRequestWaitExtraTypeDef" = dataclasses.field()

    id = field("id")
    export = field("export")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRunRequestWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRunRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunRequestWait:
    boto3_raw_data: "type_defs.GetRunRequestWaitTypeDef" = dataclasses.field()

    id = field("id")
    export = field("export")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRunRequestWaitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRunRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunTaskRequestWaitExtra:
    boto3_raw_data: "type_defs.GetRunTaskRequestWaitExtraTypeDef" = dataclasses.field()

    id = field("id")
    taskId = field("taskId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRunTaskRequestWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRunTaskRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunTaskRequestWait:
    boto3_raw_data: "type_defs.GetRunTaskRequestWaitTypeDef" = dataclasses.field()

    id = field("id")
    taskId = field("taskId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRunTaskRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRunTaskRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVariantImportRequestWait:
    boto3_raw_data: "type_defs.GetVariantImportRequestWaitTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVariantImportRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVariantImportRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVariantStoreRequestWaitExtra:
    boto3_raw_data: "type_defs.GetVariantStoreRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVariantStoreRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVariantStoreRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVariantStoreRequestWait:
    boto3_raw_data: "type_defs.GetVariantStoreRequestWaitTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVariantStoreRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVariantStoreRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowRequestWait:
    boto3_raw_data: "type_defs.GetWorkflowRequestWaitTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    export = field("export")
    workflowOwnerId = field("workflowOwnerId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowVersionRequestWait:
    boto3_raw_data: "type_defs.GetWorkflowVersionRequestWaitTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    versionName = field("versionName")
    type = field("type")
    export = field("export")
    workflowOwnerId = field("workflowOwnerId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetWorkflowVersionRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowVersionRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadSetListItem:
    boto3_raw_data: "type_defs.ReadSetListItemTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    sequenceStoreId = field("sequenceStoreId")
    status = field("status")
    fileType = field("fileType")
    creationTime = field("creationTime")
    subjectId = field("subjectId")
    sampleId = field("sampleId")
    name = field("name")
    description = field("description")
    referenceArn = field("referenceArn")

    @cached_property
    def sequenceInformation(self):  # pragma: no cover
        return SequenceInformation.make_one(self.boto3_raw_data["sequenceInformation"])

    statusMessage = field("statusMessage")
    creationType = field("creationType")

    @cached_property
    def etag(self):  # pragma: no cover
        return ETag.make_one(self.boto3_raw_data["etag"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadSetListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReadSetListItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReferenceImportJobResponse:
    boto3_raw_data: "type_defs.GetReferenceImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    referenceStoreId = field("referenceStoreId")
    roleArn = field("roleArn")
    status = field("status")
    statusMessage = field("statusMessage")
    creationTime = field("creationTime")
    completionTime = field("completionTime")

    @cached_property
    def sources(self):  # pragma: no cover
        return ImportReferenceSourceItem.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReferenceImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReferenceImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunResponse:
    boto3_raw_data: "type_defs.GetRunResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    cacheId = field("cacheId")
    cacheBehavior = field("cacheBehavior")
    engineVersion = field("engineVersion")
    status = field("status")
    workflowId = field("workflowId")
    workflowType = field("workflowType")
    runId = field("runId")
    roleArn = field("roleArn")
    name = field("name")
    runGroupId = field("runGroupId")
    priority = field("priority")
    definition = field("definition")
    digest = field("digest")
    parameters = field("parameters")
    storageCapacity = field("storageCapacity")
    outputUri = field("outputUri")
    logLevel = field("logLevel")
    resourceDigests = field("resourceDigests")
    startedBy = field("startedBy")
    creationTime = field("creationTime")
    startTime = field("startTime")
    stopTime = field("stopTime")
    statusMessage = field("statusMessage")
    tags = field("tags")
    accelerators = field("accelerators")
    retentionMode = field("retentionMode")
    failureReason = field("failureReason")

    @cached_property
    def logLocation(self):  # pragma: no cover
        return RunLogLocation.make_one(self.boto3_raw_data["logLocation"])

    uuid = field("uuid")
    runOutputUri = field("runOutputUri")
    storageType = field("storageType")
    workflowOwnerId = field("workflowOwnerId")
    workflowVersionName = field("workflowVersionName")
    workflowUuid = field("workflowUuid")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRunResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRunResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRunTaskResponse:
    boto3_raw_data: "type_defs.GetRunTaskResponseTypeDef" = dataclasses.field()

    taskId = field("taskId")
    status = field("status")
    name = field("name")
    cpus = field("cpus")
    cacheHit = field("cacheHit")
    cacheS3Uri = field("cacheS3Uri")
    memory = field("memory")
    creationTime = field("creationTime")
    startTime = field("startTime")
    stopTime = field("stopTime")
    statusMessage = field("statusMessage")
    logStream = field("logStream")
    gpus = field("gpus")
    instanceType = field("instanceType")
    failureReason = field("failureReason")

    @cached_property
    def imageDetails(self):  # pragma: no cover
        return ImageDetails.make_one(self.boto3_raw_data["imageDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRunTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRunTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetShareResponse:
    boto3_raw_data: "type_defs.GetShareResponseTypeDef" = dataclasses.field()

    @cached_property
    def share(self):  # pragma: no cover
        return ShareDetails.make_one(self.boto3_raw_data["share"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetShareResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetShareResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSharesResponse:
    boto3_raw_data: "type_defs.ListSharesResponseTypeDef" = dataclasses.field()

    @cached_property
    def shares(self):  # pragma: no cover
        return ShareDetails.make_many(self.boto3_raw_data["shares"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSharesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSharesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVariantImportResponse:
    boto3_raw_data: "type_defs.GetVariantImportResponseTypeDef" = dataclasses.field()

    id = field("id")
    destinationName = field("destinationName")
    roleArn = field("roleArn")
    status = field("status")
    statusMessage = field("statusMessage")
    creationTime = field("creationTime")
    updateTime = field("updateTime")
    completionTime = field("completionTime")

    @cached_property
    def items(self):  # pragma: no cover
        return VariantImportItemDetail.make_many(self.boto3_raw_data["items"])

    runLeftNormalization = field("runLeftNormalization")
    annotationFields = field("annotationFields")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVariantImportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVariantImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetImportJobsResponse:
    boto3_raw_data: "type_defs.ListReadSetImportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def importJobs(self):  # pragma: no cover
        return ImportReadSetJobItem.make_many(self.boto3_raw_data["importJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReadSetImportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportReadSetSourceItem:
    boto3_raw_data: "type_defs.ImportReadSetSourceItemTypeDef" = dataclasses.field()

    @cached_property
    def sourceFiles(self):  # pragma: no cover
        return SourceFiles.make_one(self.boto3_raw_data["sourceFiles"])

    sourceFileType = field("sourceFileType")
    status = field("status")
    subjectId = field("subjectId")
    sampleId = field("sampleId")
    statusMessage = field("statusMessage")
    generatedFrom = field("generatedFrom")
    referenceArn = field("referenceArn")
    name = field("name")
    description = field("description")
    tags = field("tags")
    readSetId = field("readSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportReadSetSourceItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportReadSetSourceItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReadSetImportJobSourceItem:
    boto3_raw_data: "type_defs.StartReadSetImportJobSourceItemTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceFiles(self):  # pragma: no cover
        return SourceFiles.make_one(self.boto3_raw_data["sourceFiles"])

    sourceFileType = field("sourceFileType")
    subjectId = field("subjectId")
    sampleId = field("sampleId")
    generatedFrom = field("generatedFrom")
    referenceArn = field("referenceArn")
    name = field("name")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartReadSetImportJobSourceItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReadSetImportJobSourceItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReferenceImportJobsResponse:
    boto3_raw_data: "type_defs.ListReferenceImportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def importJobs(self):  # pragma: no cover
        return ImportReferenceJobItem.make_many(self.boto3_raw_data["importJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReferenceImportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReferenceImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationImportJobsRequest:
    boto3_raw_data: "type_defs.ListAnnotationImportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    ids = field("ids")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListAnnotationImportJobsFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnnotationImportJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListAnnotationImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ids = field("ids")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListAnnotationImportJobsFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnnotationImportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultipartReadSetUploadsRequestPaginate:
    boto3_raw_data: "type_defs.ListMultipartReadSetUploadsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMultipartReadSetUploadsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultipartReadSetUploadsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunCachesRequestPaginate:
    boto3_raw_data: "type_defs.ListRunCachesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRunCachesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunCachesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListRunGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRunGroupsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunTasksRequestPaginate:
    boto3_raw_data: "type_defs.ListRunTasksRequestPaginateTypeDef" = dataclasses.field()

    id = field("id")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRunTasksRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunTasksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunsRequestPaginate:
    boto3_raw_data: "type_defs.ListRunsRequestPaginateTypeDef" = dataclasses.field()

    name = field("name")
    runGroupId = field("runGroupId")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRunsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSharesRequestPaginate:
    boto3_raw_data: "type_defs.ListSharesRequestPaginateTypeDef" = dataclasses.field()

    resourceOwner = field("resourceOwner")

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSharesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSharesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkflowVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    type = field("type")
    workflowOwnerId = field("workflowOwnerId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkflowVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkflowsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    name = field("name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationStoreVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAnnotationStoreVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListAnnotationStoreVersionsFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnnotationStoreVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationStoreVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationStoreVersionsRequest:
    boto3_raw_data: "type_defs.ListAnnotationStoreVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListAnnotationStoreVersionsFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnnotationStoreVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationStoreVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationStoresRequestPaginate:
    boto3_raw_data: "type_defs.ListAnnotationStoresRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ids = field("ids")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListAnnotationStoresFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnnotationStoresRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationStoresRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationStoresRequest:
    boto3_raw_data: "type_defs.ListAnnotationStoresRequestTypeDef" = dataclasses.field()

    ids = field("ids")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListAnnotationStoresFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnnotationStoresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationStoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultipartReadSetUploadsResponse:
    boto3_raw_data: "type_defs.ListMultipartReadSetUploadsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def uploads(self):  # pragma: no cover
        return MultipartReadSetUploadListItem.make_many(self.boto3_raw_data["uploads"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMultipartReadSetUploadsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultipartReadSetUploadsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetUploadPartsResponse:
    boto3_raw_data: "type_defs.ListReadSetUploadPartsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def parts(self):  # pragma: no cover
        return ReadSetUploadPartListItem.make_many(self.boto3_raw_data["parts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReadSetUploadPartsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetUploadPartsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReferencesResponse:
    boto3_raw_data: "type_defs.ListReferencesResponseTypeDef" = dataclasses.field()

    @cached_property
    def references(self):  # pragma: no cover
        return ReferenceListItem.make_many(self.boto3_raw_data["references"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReferencesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunCachesResponse:
    boto3_raw_data: "type_defs.ListRunCachesResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return RunCacheListItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRunCachesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunCachesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunGroupsResponse:
    boto3_raw_data: "type_defs.ListRunGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return RunGroupListItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRunGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunTasksResponse:
    boto3_raw_data: "type_defs.ListRunTasksResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return TaskListItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRunTasksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRunsResponse:
    boto3_raw_data: "type_defs.ListRunsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return RunListItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRunsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVariantImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListVariantImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ids = field("ids")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListVariantImportJobsFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVariantImportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVariantImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVariantImportJobsRequest:
    boto3_raw_data: "type_defs.ListVariantImportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    ids = field("ids")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListVariantImportJobsFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVariantImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVariantImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVariantImportJobsResponse:
    boto3_raw_data: "type_defs.ListVariantImportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def variantImportJobs(self):  # pragma: no cover
        return VariantImportJobItem.make_many(self.boto3_raw_data["variantImportJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVariantImportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVariantImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVariantStoresRequestPaginate:
    boto3_raw_data: "type_defs.ListVariantStoresRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ids = field("ids")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListVariantStoresFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVariantStoresRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVariantStoresRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVariantStoresRequest:
    boto3_raw_data: "type_defs.ListVariantStoresRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    ids = field("ids")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListVariantStoresFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVariantStoresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVariantStoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowVersionsResponse:
    boto3_raw_data: "type_defs.ListWorkflowVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return WorkflowVersionListItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsResponse:
    boto3_raw_data: "type_defs.ListWorkflowsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return WorkflowListItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TsvOptions:
    boto3_raw_data: "type_defs.TsvOptionsTypeDef" = dataclasses.field()

    @cached_property
    def readOptions(self):  # pragma: no cover
        return ReadOptions.make_one(self.boto3_raw_data["readOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TsvOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TsvOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReadSetActivationJobRequest:
    boto3_raw_data: "type_defs.StartReadSetActivationJobRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")

    @cached_property
    def sources(self):  # pragma: no cover
        return StartReadSetActivationJobSourceItem.make_many(
            self.boto3_raw_data["sources"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartReadSetActivationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReadSetActivationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReferenceImportJobRequest:
    boto3_raw_data: "type_defs.StartReferenceImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    referenceStoreId = field("referenceStoreId")
    roleArn = field("roleArn")

    @cached_property
    def sources(self):  # pragma: no cover
        return StartReferenceImportJobSourceItem.make_many(
            self.boto3_raw_data["sources"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartReferenceImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReferenceImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartVariantImportRequest:
    boto3_raw_data: "type_defs.StartVariantImportRequestTypeDef" = dataclasses.field()

    destinationName = field("destinationName")
    roleArn = field("roleArn")

    @cached_property
    def items(self):  # pragma: no cover
        return VariantImportItemSource.make_many(self.boto3_raw_data["items"])

    runLeftNormalization = field("runLeftNormalization")
    annotationFields = field("annotationFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartVariantImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartVariantImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StoreOptionsOutput:
    boto3_raw_data: "type_defs.StoreOptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def tsvStoreOptions(self):  # pragma: no cover
        return TsvStoreOptionsOutput.make_one(self.boto3_raw_data["tsvStoreOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StoreOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StoreOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StoreOptions:
    boto3_raw_data: "type_defs.StoreOptionsTypeDef" = dataclasses.field()

    @cached_property
    def tsvStoreOptions(self):  # pragma: no cover
        return TsvStoreOptions.make_one(self.boto3_raw_data["tsvStoreOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StoreOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StoreOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersionOptionsOutput:
    boto3_raw_data: "type_defs.VersionOptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def tsvVersionOptions(self):  # pragma: no cover
        return TsvVersionOptionsOutput.make_one(
            self.boto3_raw_data["tsvVersionOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VersionOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VersionOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersionOptions:
    boto3_raw_data: "type_defs.VersionOptionsTypeDef" = dataclasses.field()

    @cached_property
    def tsvVersionOptions(self):  # pragma: no cover
        return TsvVersionOptions.make_one(self.boto3_raw_data["tsvVersionOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VersionOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VersionOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetActivationJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListReadSetActivationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")

    @cached_property
    def filter(self):  # pragma: no cover
        return ActivateReadSetFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReadSetActivationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetActivationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetActivationJobsRequest:
    boto3_raw_data: "type_defs.ListReadSetActivationJobsRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ActivateReadSetFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReadSetActivationJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetActivationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetExportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListReadSetExportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")

    @cached_property
    def filter(self):  # pragma: no cover
        return ExportReadSetFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReadSetExportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetExportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetExportJobsRequest:
    boto3_raw_data: "type_defs.ListReadSetExportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ExportReadSetFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReadSetExportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListReadSetImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")

    @cached_property
    def filter(self):  # pragma: no cover
        return ImportReadSetFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReadSetImportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetImportJobsRequest:
    boto3_raw_data: "type_defs.ListReadSetImportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ImportReadSetFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReadSetImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReferenceImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListReferenceImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    referenceStoreId = field("referenceStoreId")

    @cached_property
    def filter(self):  # pragma: no cover
        return ImportReferenceFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReferenceImportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReferenceImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReferenceImportJobsRequest:
    boto3_raw_data: "type_defs.ListReferenceImportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    referenceStoreId = field("referenceStoreId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ImportReferenceFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReferenceImportJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReferenceImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListReadSetsRequestPaginateTypeDef" = dataclasses.field()

    sequenceStoreId = field("sequenceStoreId")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReadSetFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReadSetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetsRequest:
    boto3_raw_data: "type_defs.ListReadSetsRequestTypeDef" = dataclasses.field()

    sequenceStoreId = field("sequenceStoreId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReadSetFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReadSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetUploadPartsRequestPaginate:
    boto3_raw_data: "type_defs.ListReadSetUploadPartsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    uploadId = field("uploadId")
    partSource = field("partSource")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReadSetUploadPartListFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReadSetUploadPartsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetUploadPartsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetUploadPartsRequest:
    boto3_raw_data: "type_defs.ListReadSetUploadPartsRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    uploadId = field("uploadId")
    partSource = field("partSource")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReadSetUploadPartListFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReadSetUploadPartsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetUploadPartsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReferencesRequestPaginate:
    boto3_raw_data: "type_defs.ListReferencesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    referenceStoreId = field("referenceStoreId")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReferenceFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReferencesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReferencesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReferencesRequest:
    boto3_raw_data: "type_defs.ListReferencesRequestTypeDef" = dataclasses.field()

    referenceStoreId = field("referenceStoreId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReferenceFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReferencesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReferenceStoresRequestPaginate:
    boto3_raw_data: "type_defs.ListReferenceStoresRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return ReferenceStoreFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReferenceStoresRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReferenceStoresRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReferenceStoresRequest:
    boto3_raw_data: "type_defs.ListReferenceStoresRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReferenceStoreFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReferenceStoresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReferenceStoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSequenceStoresRequestPaginate:
    boto3_raw_data: "type_defs.ListSequenceStoresRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return SequenceStoreFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSequenceStoresRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSequenceStoresRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSequenceStoresRequest:
    boto3_raw_data: "type_defs.ListSequenceStoresRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filter(self):  # pragma: no cover
        return SequenceStoreFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSequenceStoresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSequenceStoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnnotationStoresResponse:
    boto3_raw_data: "type_defs.ListAnnotationStoresResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def annotationStores(self):  # pragma: no cover
        return AnnotationStoreItem.make_many(self.boto3_raw_data["annotationStores"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnnotationStoresResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnnotationStoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReferenceStoresResponse:
    boto3_raw_data: "type_defs.ListReferenceStoresResponseTypeDef" = dataclasses.field()

    @cached_property
    def referenceStores(self):  # pragma: no cover
        return ReferenceStoreDetail.make_many(self.boto3_raw_data["referenceStores"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReferenceStoresResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReferenceStoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSequenceStoresResponse:
    boto3_raw_data: "type_defs.ListSequenceStoresResponseTypeDef" = dataclasses.field()

    @cached_property
    def sequenceStores(self):  # pragma: no cover
        return SequenceStoreDetail.make_many(self.boto3_raw_data["sequenceStores"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSequenceStoresResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSequenceStoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVariantStoresResponse:
    boto3_raw_data: "type_defs.ListVariantStoresResponseTypeDef" = dataclasses.field()

    @cached_property
    def variantStores(self):  # pragma: no cover
        return VariantStoreItem.make_many(self.boto3_raw_data["variantStores"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVariantStoresResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVariantStoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowResponse:
    boto3_raw_data: "type_defs.GetWorkflowResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    status = field("status")
    type = field("type")
    name = field("name")
    description = field("description")
    engine = field("engine")
    definition = field("definition")
    main = field("main")
    digest = field("digest")
    parameterTemplate = field("parameterTemplate")
    storageCapacity = field("storageCapacity")
    creationTime = field("creationTime")
    statusMessage = field("statusMessage")
    tags = field("tags")
    metadata = field("metadata")
    accelerators = field("accelerators")
    storageType = field("storageType")
    uuid = field("uuid")

    @cached_property
    def containerRegistryMap(self):  # pragma: no cover
        return ContainerRegistryMapOutput.make_one(
            self.boto3_raw_data["containerRegistryMap"]
        )

    readme = field("readme")

    @cached_property
    def definitionRepositoryDetails(self):  # pragma: no cover
        return DefinitionRepositoryDetails.make_one(
            self.boto3_raw_data["definitionRepositoryDetails"]
        )

    readmePath = field("readmePath")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowVersionResponse:
    boto3_raw_data: "type_defs.GetWorkflowVersionResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    workflowId = field("workflowId")
    versionName = field("versionName")
    accelerators = field("accelerators")
    creationTime = field("creationTime")
    description = field("description")
    definition = field("definition")
    digest = field("digest")
    engine = field("engine")
    main = field("main")
    metadata = field("metadata")
    parameterTemplate = field("parameterTemplate")
    status = field("status")
    statusMessage = field("statusMessage")
    storageType = field("storageType")
    storageCapacity = field("storageCapacity")
    type = field("type")
    tags = field("tags")
    uuid = field("uuid")
    workflowBucketOwnerId = field("workflowBucketOwnerId")

    @cached_property
    def containerRegistryMap(self):  # pragma: no cover
        return ContainerRegistryMapOutput.make_one(
            self.boto3_raw_data["containerRegistryMap"]
        )

    readme = field("readme")

    @cached_property
    def definitionRepositoryDetails(self):  # pragma: no cover
        return DefinitionRepositoryDetails.make_one(
            self.boto3_raw_data["definitionRepositoryDetails"]
        )

    readmePath = field("readmePath")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadSetFiles:
    boto3_raw_data: "type_defs.ReadSetFilesTypeDef" = dataclasses.field()

    @cached_property
    def source1(self):  # pragma: no cover
        return FileInformation.make_one(self.boto3_raw_data["source1"])

    @cached_property
    def source2(self):  # pragma: no cover
        return FileInformation.make_one(self.boto3_raw_data["source2"])

    @cached_property
    def index(self):  # pragma: no cover
        return FileInformation.make_one(self.boto3_raw_data["index"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadSetFilesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReadSetFilesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceFiles:
    boto3_raw_data: "type_defs.ReferenceFilesTypeDef" = dataclasses.field()

    @cached_property
    def source(self):  # pragma: no cover
        return FileInformation.make_one(self.boto3_raw_data["source"])

    @cached_property
    def index(self):  # pragma: no cover
        return FileInformation.make_one(self.boto3_raw_data["index"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReferenceFilesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReferenceFilesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReadSetsResponse:
    boto3_raw_data: "type_defs.ListReadSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def readSets(self):  # pragma: no cover
        return ReadSetListItem.make_many(self.boto3_raw_data["readSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReadSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReadSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetImportJobResponse:
    boto3_raw_data: "type_defs.GetReadSetImportJobResponseTypeDef" = dataclasses.field()

    id = field("id")
    sequenceStoreId = field("sequenceStoreId")
    roleArn = field("roleArn")
    status = field("status")
    statusMessage = field("statusMessage")
    creationTime = field("creationTime")
    completionTime = field("completionTime")

    @cached_property
    def sources(self):  # pragma: no cover
        return ImportReadSetSourceItem.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReadSetImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReadSetImportJobRequest:
    boto3_raw_data: "type_defs.StartReadSetImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    sequenceStoreId = field("sequenceStoreId")
    roleArn = field("roleArn")

    @cached_property
    def sources(self):  # pragma: no cover
        return StartReadSetImportJobSourceItem.make_many(self.boto3_raw_data["sources"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReadSetImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReadSetImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormatOptions:
    boto3_raw_data: "type_defs.FormatOptionsTypeDef" = dataclasses.field()

    @cached_property
    def tsvOptions(self):  # pragma: no cover
        return TsvOptions.make_one(self.boto3_raw_data["tsvOptions"])

    @cached_property
    def vcfOptions(self):  # pragma: no cover
        return VcfOptions.make_one(self.boto3_raw_data["vcfOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormatOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormatOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnnotationStoreResponse:
    boto3_raw_data: "type_defs.CreateAnnotationStoreResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def reference(self):  # pragma: no cover
        return ReferenceItem.make_one(self.boto3_raw_data["reference"])

    storeFormat = field("storeFormat")

    @cached_property
    def storeOptions(self):  # pragma: no cover
        return StoreOptionsOutput.make_one(self.boto3_raw_data["storeOptions"])

    status = field("status")
    name = field("name")
    versionName = field("versionName")
    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAnnotationStoreResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnnotationStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationStoreResponse:
    boto3_raw_data: "type_defs.GetAnnotationStoreResponseTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def reference(self):  # pragma: no cover
        return ReferenceItem.make_one(self.boto3_raw_data["reference"])

    status = field("status")
    storeArn = field("storeArn")
    name = field("name")
    description = field("description")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    creationTime = field("creationTime")
    updateTime = field("updateTime")
    tags = field("tags")

    @cached_property
    def storeOptions(self):  # pragma: no cover
        return StoreOptionsOutput.make_one(self.boto3_raw_data["storeOptions"])

    storeFormat = field("storeFormat")
    statusMessage = field("statusMessage")
    storeSizeBytes = field("storeSizeBytes")
    numVersions = field("numVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnnotationStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnnotationStoreResponse:
    boto3_raw_data: "type_defs.UpdateAnnotationStoreResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def reference(self):  # pragma: no cover
        return ReferenceItem.make_one(self.boto3_raw_data["reference"])

    status = field("status")
    name = field("name")
    description = field("description")
    creationTime = field("creationTime")
    updateTime = field("updateTime")

    @cached_property
    def storeOptions(self):  # pragma: no cover
        return StoreOptionsOutput.make_one(self.boto3_raw_data["storeOptions"])

    storeFormat = field("storeFormat")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAnnotationStoreResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnnotationStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnnotationStoreVersionResponse:
    boto3_raw_data: "type_defs.CreateAnnotationStoreVersionResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    versionName = field("versionName")
    storeId = field("storeId")

    @cached_property
    def versionOptions(self):  # pragma: no cover
        return VersionOptionsOutput.make_one(self.boto3_raw_data["versionOptions"])

    name = field("name")
    status = field("status")
    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAnnotationStoreVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnnotationStoreVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationStoreVersionResponse:
    boto3_raw_data: "type_defs.GetAnnotationStoreVersionResponseTypeDef" = (
        dataclasses.field()
    )

    storeId = field("storeId")
    id = field("id")
    status = field("status")
    versionArn = field("versionArn")
    name = field("name")
    versionName = field("versionName")
    description = field("description")
    creationTime = field("creationTime")
    updateTime = field("updateTime")
    tags = field("tags")

    @cached_property
    def versionOptions(self):  # pragma: no cover
        return VersionOptionsOutput.make_one(self.boto3_raw_data["versionOptions"])

    statusMessage = field("statusMessage")
    versionSizeBytes = field("versionSizeBytes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAnnotationStoreVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationStoreVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowRequest:
    boto3_raw_data: "type_defs.CreateWorkflowRequestTypeDef" = dataclasses.field()

    requestId = field("requestId")
    name = field("name")
    description = field("description")
    engine = field("engine")
    definitionZip = field("definitionZip")
    definitionUri = field("definitionUri")
    main = field("main")
    parameterTemplate = field("parameterTemplate")
    storageCapacity = field("storageCapacity")
    tags = field("tags")
    accelerators = field("accelerators")
    storageType = field("storageType")
    containerRegistryMap = field("containerRegistryMap")
    containerRegistryMapUri = field("containerRegistryMapUri")
    readmeMarkdown = field("readmeMarkdown")
    parameterTemplatePath = field("parameterTemplatePath")
    readmePath = field("readmePath")

    @cached_property
    def definitionRepository(self):  # pragma: no cover
        return DefinitionRepository.make_one(
            self.boto3_raw_data["definitionRepository"]
        )

    workflowBucketOwnerId = field("workflowBucketOwnerId")
    readmeUri = field("readmeUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowVersionRequest:
    boto3_raw_data: "type_defs.CreateWorkflowVersionRequestTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    versionName = field("versionName")
    requestId = field("requestId")
    definitionZip = field("definitionZip")
    definitionUri = field("definitionUri")
    accelerators = field("accelerators")
    description = field("description")
    engine = field("engine")
    main = field("main")
    parameterTemplate = field("parameterTemplate")
    storageType = field("storageType")
    storageCapacity = field("storageCapacity")
    tags = field("tags")
    workflowBucketOwnerId = field("workflowBucketOwnerId")
    containerRegistryMap = field("containerRegistryMap")
    containerRegistryMapUri = field("containerRegistryMapUri")
    readmeMarkdown = field("readmeMarkdown")
    parameterTemplatePath = field("parameterTemplatePath")
    readmePath = field("readmePath")

    @cached_property
    def definitionRepository(self):  # pragma: no cover
        return DefinitionRepository.make_one(
            self.boto3_raw_data["definitionRepository"]
        )

    readmeUri = field("readmeUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkflowVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReadSetMetadataResponse:
    boto3_raw_data: "type_defs.GetReadSetMetadataResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    sequenceStoreId = field("sequenceStoreId")
    subjectId = field("subjectId")
    sampleId = field("sampleId")
    status = field("status")
    name = field("name")
    description = field("description")
    fileType = field("fileType")
    creationTime = field("creationTime")

    @cached_property
    def sequenceInformation(self):  # pragma: no cover
        return SequenceInformation.make_one(self.boto3_raw_data["sequenceInformation"])

    referenceArn = field("referenceArn")

    @cached_property
    def files(self):  # pragma: no cover
        return ReadSetFiles.make_one(self.boto3_raw_data["files"])

    statusMessage = field("statusMessage")
    creationType = field("creationType")

    @cached_property
    def etag(self):  # pragma: no cover
        return ETag.make_one(self.boto3_raw_data["etag"])

    creationJobId = field("creationJobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReadSetMetadataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReadSetMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReferenceMetadataResponse:
    boto3_raw_data: "type_defs.GetReferenceMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    referenceStoreId = field("referenceStoreId")
    md5 = field("md5")
    status = field("status")
    name = field("name")
    description = field("description")
    creationTime = field("creationTime")
    updateTime = field("updateTime")

    @cached_property
    def files(self):  # pragma: no cover
        return ReferenceFiles.make_one(self.boto3_raw_data["files"])

    creationType = field("creationType")
    creationJobId = field("creationJobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReferenceMetadataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReferenceMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnnotationImportResponse:
    boto3_raw_data: "type_defs.GetAnnotationImportResponseTypeDef" = dataclasses.field()

    id = field("id")
    destinationName = field("destinationName")
    versionName = field("versionName")
    roleArn = field("roleArn")
    status = field("status")
    statusMessage = field("statusMessage")
    creationTime = field("creationTime")
    updateTime = field("updateTime")
    completionTime = field("completionTime")

    @cached_property
    def items(self):  # pragma: no cover
        return AnnotationImportItemDetail.make_many(self.boto3_raw_data["items"])

    runLeftNormalization = field("runLeftNormalization")

    @cached_property
    def formatOptions(self):  # pragma: no cover
        return FormatOptions.make_one(self.boto3_raw_data["formatOptions"])

    annotationFields = field("annotationFields")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnnotationImportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnnotationImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAnnotationImportRequest:
    boto3_raw_data: "type_defs.StartAnnotationImportRequestTypeDef" = (
        dataclasses.field()
    )

    destinationName = field("destinationName")
    roleArn = field("roleArn")

    @cached_property
    def items(self):  # pragma: no cover
        return AnnotationImportItemSource.make_many(self.boto3_raw_data["items"])

    versionName = field("versionName")

    @cached_property
    def formatOptions(self):  # pragma: no cover
        return FormatOptions.make_one(self.boto3_raw_data["formatOptions"])

    runLeftNormalization = field("runLeftNormalization")
    annotationFields = field("annotationFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAnnotationImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAnnotationImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnnotationStoreRequest:
    boto3_raw_data: "type_defs.CreateAnnotationStoreRequestTypeDef" = (
        dataclasses.field()
    )

    storeFormat = field("storeFormat")

    @cached_property
    def reference(self):  # pragma: no cover
        return ReferenceItem.make_one(self.boto3_raw_data["reference"])

    name = field("name")
    description = field("description")
    tags = field("tags")
    versionName = field("versionName")

    @cached_property
    def sseConfig(self):  # pragma: no cover
        return SseConfig.make_one(self.boto3_raw_data["sseConfig"])

    storeOptions = field("storeOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAnnotationStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnnotationStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnnotationStoreVersionRequest:
    boto3_raw_data: "type_defs.CreateAnnotationStoreVersionRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    versionName = field("versionName")
    description = field("description")
    versionOptions = field("versionOptions")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAnnotationStoreVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnnotationStoreVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
