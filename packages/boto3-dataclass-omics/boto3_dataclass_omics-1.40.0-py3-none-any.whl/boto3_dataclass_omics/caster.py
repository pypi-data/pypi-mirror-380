# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_omics import type_defs as bs_td


class OMICSCaster:

    def accept_share(
        self,
        res: "bs_td.AcceptShareResponseTypeDef",
    ) -> "dc_td.AcceptShareResponse":
        return dc_td.AcceptShareResponse.make_one(res)

    def batch_delete_read_set(
        self,
        res: "bs_td.BatchDeleteReadSetResponseTypeDef",
    ) -> "dc_td.BatchDeleteReadSetResponse":
        return dc_td.BatchDeleteReadSetResponse.make_one(res)

    def cancel_run(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def complete_multipart_read_set_upload(
        self,
        res: "bs_td.CompleteMultipartReadSetUploadResponseTypeDef",
    ) -> "dc_td.CompleteMultipartReadSetUploadResponse":
        return dc_td.CompleteMultipartReadSetUploadResponse.make_one(res)

    def create_annotation_store(
        self,
        res: "bs_td.CreateAnnotationStoreResponseTypeDef",
    ) -> "dc_td.CreateAnnotationStoreResponse":
        return dc_td.CreateAnnotationStoreResponse.make_one(res)

    def create_annotation_store_version(
        self,
        res: "bs_td.CreateAnnotationStoreVersionResponseTypeDef",
    ) -> "dc_td.CreateAnnotationStoreVersionResponse":
        return dc_td.CreateAnnotationStoreVersionResponse.make_one(res)

    def create_multipart_read_set_upload(
        self,
        res: "bs_td.CreateMultipartReadSetUploadResponseTypeDef",
    ) -> "dc_td.CreateMultipartReadSetUploadResponse":
        return dc_td.CreateMultipartReadSetUploadResponse.make_one(res)

    def create_reference_store(
        self,
        res: "bs_td.CreateReferenceStoreResponseTypeDef",
    ) -> "dc_td.CreateReferenceStoreResponse":
        return dc_td.CreateReferenceStoreResponse.make_one(res)

    def create_run_cache(
        self,
        res: "bs_td.CreateRunCacheResponseTypeDef",
    ) -> "dc_td.CreateRunCacheResponse":
        return dc_td.CreateRunCacheResponse.make_one(res)

    def create_run_group(
        self,
        res: "bs_td.CreateRunGroupResponseTypeDef",
    ) -> "dc_td.CreateRunGroupResponse":
        return dc_td.CreateRunGroupResponse.make_one(res)

    def create_sequence_store(
        self,
        res: "bs_td.CreateSequenceStoreResponseTypeDef",
    ) -> "dc_td.CreateSequenceStoreResponse":
        return dc_td.CreateSequenceStoreResponse.make_one(res)

    def create_share(
        self,
        res: "bs_td.CreateShareResponseTypeDef",
    ) -> "dc_td.CreateShareResponse":
        return dc_td.CreateShareResponse.make_one(res)

    def create_variant_store(
        self,
        res: "bs_td.CreateVariantStoreResponseTypeDef",
    ) -> "dc_td.CreateVariantStoreResponse":
        return dc_td.CreateVariantStoreResponse.make_one(res)

    def create_workflow(
        self,
        res: "bs_td.CreateWorkflowResponseTypeDef",
    ) -> "dc_td.CreateWorkflowResponse":
        return dc_td.CreateWorkflowResponse.make_one(res)

    def create_workflow_version(
        self,
        res: "bs_td.CreateWorkflowVersionResponseTypeDef",
    ) -> "dc_td.CreateWorkflowVersionResponse":
        return dc_td.CreateWorkflowVersionResponse.make_one(res)

    def delete_annotation_store(
        self,
        res: "bs_td.DeleteAnnotationStoreResponseTypeDef",
    ) -> "dc_td.DeleteAnnotationStoreResponse":
        return dc_td.DeleteAnnotationStoreResponse.make_one(res)

    def delete_annotation_store_versions(
        self,
        res: "bs_td.DeleteAnnotationStoreVersionsResponseTypeDef",
    ) -> "dc_td.DeleteAnnotationStoreVersionsResponse":
        return dc_td.DeleteAnnotationStoreVersionsResponse.make_one(res)

    def delete_run(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_run_cache(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_run_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_share(
        self,
        res: "bs_td.DeleteShareResponseTypeDef",
    ) -> "dc_td.DeleteShareResponse":
        return dc_td.DeleteShareResponse.make_one(res)

    def delete_variant_store(
        self,
        res: "bs_td.DeleteVariantStoreResponseTypeDef",
    ) -> "dc_td.DeleteVariantStoreResponse":
        return dc_td.DeleteVariantStoreResponse.make_one(res)

    def delete_workflow(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_workflow_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_annotation_import_job(
        self,
        res: "bs_td.GetAnnotationImportResponseTypeDef",
    ) -> "dc_td.GetAnnotationImportResponse":
        return dc_td.GetAnnotationImportResponse.make_one(res)

    def get_annotation_store(
        self,
        res: "bs_td.GetAnnotationStoreResponseTypeDef",
    ) -> "dc_td.GetAnnotationStoreResponse":
        return dc_td.GetAnnotationStoreResponse.make_one(res)

    def get_annotation_store_version(
        self,
        res: "bs_td.GetAnnotationStoreVersionResponseTypeDef",
    ) -> "dc_td.GetAnnotationStoreVersionResponse":
        return dc_td.GetAnnotationStoreVersionResponse.make_one(res)

    def get_read_set(
        self,
        res: "bs_td.GetReadSetResponseTypeDef",
    ) -> "dc_td.GetReadSetResponse":
        return dc_td.GetReadSetResponse.make_one(res)

    def get_read_set_activation_job(
        self,
        res: "bs_td.GetReadSetActivationJobResponseTypeDef",
    ) -> "dc_td.GetReadSetActivationJobResponse":
        return dc_td.GetReadSetActivationJobResponse.make_one(res)

    def get_read_set_export_job(
        self,
        res: "bs_td.GetReadSetExportJobResponseTypeDef",
    ) -> "dc_td.GetReadSetExportJobResponse":
        return dc_td.GetReadSetExportJobResponse.make_one(res)

    def get_read_set_import_job(
        self,
        res: "bs_td.GetReadSetImportJobResponseTypeDef",
    ) -> "dc_td.GetReadSetImportJobResponse":
        return dc_td.GetReadSetImportJobResponse.make_one(res)

    def get_read_set_metadata(
        self,
        res: "bs_td.GetReadSetMetadataResponseTypeDef",
    ) -> "dc_td.GetReadSetMetadataResponse":
        return dc_td.GetReadSetMetadataResponse.make_one(res)

    def get_reference(
        self,
        res: "bs_td.GetReferenceResponseTypeDef",
    ) -> "dc_td.GetReferenceResponse":
        return dc_td.GetReferenceResponse.make_one(res)

    def get_reference_import_job(
        self,
        res: "bs_td.GetReferenceImportJobResponseTypeDef",
    ) -> "dc_td.GetReferenceImportJobResponse":
        return dc_td.GetReferenceImportJobResponse.make_one(res)

    def get_reference_metadata(
        self,
        res: "bs_td.GetReferenceMetadataResponseTypeDef",
    ) -> "dc_td.GetReferenceMetadataResponse":
        return dc_td.GetReferenceMetadataResponse.make_one(res)

    def get_reference_store(
        self,
        res: "bs_td.GetReferenceStoreResponseTypeDef",
    ) -> "dc_td.GetReferenceStoreResponse":
        return dc_td.GetReferenceStoreResponse.make_one(res)

    def get_run(
        self,
        res: "bs_td.GetRunResponseTypeDef",
    ) -> "dc_td.GetRunResponse":
        return dc_td.GetRunResponse.make_one(res)

    def get_run_cache(
        self,
        res: "bs_td.GetRunCacheResponseTypeDef",
    ) -> "dc_td.GetRunCacheResponse":
        return dc_td.GetRunCacheResponse.make_one(res)

    def get_run_group(
        self,
        res: "bs_td.GetRunGroupResponseTypeDef",
    ) -> "dc_td.GetRunGroupResponse":
        return dc_td.GetRunGroupResponse.make_one(res)

    def get_run_task(
        self,
        res: "bs_td.GetRunTaskResponseTypeDef",
    ) -> "dc_td.GetRunTaskResponse":
        return dc_td.GetRunTaskResponse.make_one(res)

    def get_s3_access_policy(
        self,
        res: "bs_td.GetS3AccessPolicyResponseTypeDef",
    ) -> "dc_td.GetS3AccessPolicyResponse":
        return dc_td.GetS3AccessPolicyResponse.make_one(res)

    def get_sequence_store(
        self,
        res: "bs_td.GetSequenceStoreResponseTypeDef",
    ) -> "dc_td.GetSequenceStoreResponse":
        return dc_td.GetSequenceStoreResponse.make_one(res)

    def get_share(
        self,
        res: "bs_td.GetShareResponseTypeDef",
    ) -> "dc_td.GetShareResponse":
        return dc_td.GetShareResponse.make_one(res)

    def get_variant_import_job(
        self,
        res: "bs_td.GetVariantImportResponseTypeDef",
    ) -> "dc_td.GetVariantImportResponse":
        return dc_td.GetVariantImportResponse.make_one(res)

    def get_variant_store(
        self,
        res: "bs_td.GetVariantStoreResponseTypeDef",
    ) -> "dc_td.GetVariantStoreResponse":
        return dc_td.GetVariantStoreResponse.make_one(res)

    def get_workflow(
        self,
        res: "bs_td.GetWorkflowResponseTypeDef",
    ) -> "dc_td.GetWorkflowResponse":
        return dc_td.GetWorkflowResponse.make_one(res)

    def get_workflow_version(
        self,
        res: "bs_td.GetWorkflowVersionResponseTypeDef",
    ) -> "dc_td.GetWorkflowVersionResponse":
        return dc_td.GetWorkflowVersionResponse.make_one(res)

    def list_annotation_import_jobs(
        self,
        res: "bs_td.ListAnnotationImportJobsResponseTypeDef",
    ) -> "dc_td.ListAnnotationImportJobsResponse":
        return dc_td.ListAnnotationImportJobsResponse.make_one(res)

    def list_annotation_store_versions(
        self,
        res: "bs_td.ListAnnotationStoreVersionsResponseTypeDef",
    ) -> "dc_td.ListAnnotationStoreVersionsResponse":
        return dc_td.ListAnnotationStoreVersionsResponse.make_one(res)

    def list_annotation_stores(
        self,
        res: "bs_td.ListAnnotationStoresResponseTypeDef",
    ) -> "dc_td.ListAnnotationStoresResponse":
        return dc_td.ListAnnotationStoresResponse.make_one(res)

    def list_multipart_read_set_uploads(
        self,
        res: "bs_td.ListMultipartReadSetUploadsResponseTypeDef",
    ) -> "dc_td.ListMultipartReadSetUploadsResponse":
        return dc_td.ListMultipartReadSetUploadsResponse.make_one(res)

    def list_read_set_activation_jobs(
        self,
        res: "bs_td.ListReadSetActivationJobsResponseTypeDef",
    ) -> "dc_td.ListReadSetActivationJobsResponse":
        return dc_td.ListReadSetActivationJobsResponse.make_one(res)

    def list_read_set_export_jobs(
        self,
        res: "bs_td.ListReadSetExportJobsResponseTypeDef",
    ) -> "dc_td.ListReadSetExportJobsResponse":
        return dc_td.ListReadSetExportJobsResponse.make_one(res)

    def list_read_set_import_jobs(
        self,
        res: "bs_td.ListReadSetImportJobsResponseTypeDef",
    ) -> "dc_td.ListReadSetImportJobsResponse":
        return dc_td.ListReadSetImportJobsResponse.make_one(res)

    def list_read_set_upload_parts(
        self,
        res: "bs_td.ListReadSetUploadPartsResponseTypeDef",
    ) -> "dc_td.ListReadSetUploadPartsResponse":
        return dc_td.ListReadSetUploadPartsResponse.make_one(res)

    def list_read_sets(
        self,
        res: "bs_td.ListReadSetsResponseTypeDef",
    ) -> "dc_td.ListReadSetsResponse":
        return dc_td.ListReadSetsResponse.make_one(res)

    def list_reference_import_jobs(
        self,
        res: "bs_td.ListReferenceImportJobsResponseTypeDef",
    ) -> "dc_td.ListReferenceImportJobsResponse":
        return dc_td.ListReferenceImportJobsResponse.make_one(res)

    def list_reference_stores(
        self,
        res: "bs_td.ListReferenceStoresResponseTypeDef",
    ) -> "dc_td.ListReferenceStoresResponse":
        return dc_td.ListReferenceStoresResponse.make_one(res)

    def list_references(
        self,
        res: "bs_td.ListReferencesResponseTypeDef",
    ) -> "dc_td.ListReferencesResponse":
        return dc_td.ListReferencesResponse.make_one(res)

    def list_run_caches(
        self,
        res: "bs_td.ListRunCachesResponseTypeDef",
    ) -> "dc_td.ListRunCachesResponse":
        return dc_td.ListRunCachesResponse.make_one(res)

    def list_run_groups(
        self,
        res: "bs_td.ListRunGroupsResponseTypeDef",
    ) -> "dc_td.ListRunGroupsResponse":
        return dc_td.ListRunGroupsResponse.make_one(res)

    def list_run_tasks(
        self,
        res: "bs_td.ListRunTasksResponseTypeDef",
    ) -> "dc_td.ListRunTasksResponse":
        return dc_td.ListRunTasksResponse.make_one(res)

    def list_runs(
        self,
        res: "bs_td.ListRunsResponseTypeDef",
    ) -> "dc_td.ListRunsResponse":
        return dc_td.ListRunsResponse.make_one(res)

    def list_sequence_stores(
        self,
        res: "bs_td.ListSequenceStoresResponseTypeDef",
    ) -> "dc_td.ListSequenceStoresResponse":
        return dc_td.ListSequenceStoresResponse.make_one(res)

    def list_shares(
        self,
        res: "bs_td.ListSharesResponseTypeDef",
    ) -> "dc_td.ListSharesResponse":
        return dc_td.ListSharesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_variant_import_jobs(
        self,
        res: "bs_td.ListVariantImportJobsResponseTypeDef",
    ) -> "dc_td.ListVariantImportJobsResponse":
        return dc_td.ListVariantImportJobsResponse.make_one(res)

    def list_variant_stores(
        self,
        res: "bs_td.ListVariantStoresResponseTypeDef",
    ) -> "dc_td.ListVariantStoresResponse":
        return dc_td.ListVariantStoresResponse.make_one(res)

    def list_workflow_versions(
        self,
        res: "bs_td.ListWorkflowVersionsResponseTypeDef",
    ) -> "dc_td.ListWorkflowVersionsResponse":
        return dc_td.ListWorkflowVersionsResponse.make_one(res)

    def list_workflows(
        self,
        res: "bs_td.ListWorkflowsResponseTypeDef",
    ) -> "dc_td.ListWorkflowsResponse":
        return dc_td.ListWorkflowsResponse.make_one(res)

    def put_s3_access_policy(
        self,
        res: "bs_td.PutS3AccessPolicyResponseTypeDef",
    ) -> "dc_td.PutS3AccessPolicyResponse":
        return dc_td.PutS3AccessPolicyResponse.make_one(res)

    def start_annotation_import_job(
        self,
        res: "bs_td.StartAnnotationImportResponseTypeDef",
    ) -> "dc_td.StartAnnotationImportResponse":
        return dc_td.StartAnnotationImportResponse.make_one(res)

    def start_read_set_activation_job(
        self,
        res: "bs_td.StartReadSetActivationJobResponseTypeDef",
    ) -> "dc_td.StartReadSetActivationJobResponse":
        return dc_td.StartReadSetActivationJobResponse.make_one(res)

    def start_read_set_export_job(
        self,
        res: "bs_td.StartReadSetExportJobResponseTypeDef",
    ) -> "dc_td.StartReadSetExportJobResponse":
        return dc_td.StartReadSetExportJobResponse.make_one(res)

    def start_read_set_import_job(
        self,
        res: "bs_td.StartReadSetImportJobResponseTypeDef",
    ) -> "dc_td.StartReadSetImportJobResponse":
        return dc_td.StartReadSetImportJobResponse.make_one(res)

    def start_reference_import_job(
        self,
        res: "bs_td.StartReferenceImportJobResponseTypeDef",
    ) -> "dc_td.StartReferenceImportJobResponse":
        return dc_td.StartReferenceImportJobResponse.make_one(res)

    def start_run(
        self,
        res: "bs_td.StartRunResponseTypeDef",
    ) -> "dc_td.StartRunResponse":
        return dc_td.StartRunResponse.make_one(res)

    def start_variant_import_job(
        self,
        res: "bs_td.StartVariantImportResponseTypeDef",
    ) -> "dc_td.StartVariantImportResponse":
        return dc_td.StartVariantImportResponse.make_one(res)

    def update_annotation_store(
        self,
        res: "bs_td.UpdateAnnotationStoreResponseTypeDef",
    ) -> "dc_td.UpdateAnnotationStoreResponse":
        return dc_td.UpdateAnnotationStoreResponse.make_one(res)

    def update_annotation_store_version(
        self,
        res: "bs_td.UpdateAnnotationStoreVersionResponseTypeDef",
    ) -> "dc_td.UpdateAnnotationStoreVersionResponse":
        return dc_td.UpdateAnnotationStoreVersionResponse.make_one(res)

    def update_run_cache(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_run_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_sequence_store(
        self,
        res: "bs_td.UpdateSequenceStoreResponseTypeDef",
    ) -> "dc_td.UpdateSequenceStoreResponse":
        return dc_td.UpdateSequenceStoreResponse.make_one(res)

    def update_variant_store(
        self,
        res: "bs_td.UpdateVariantStoreResponseTypeDef",
    ) -> "dc_td.UpdateVariantStoreResponse":
        return dc_td.UpdateVariantStoreResponse.make_one(res)

    def update_workflow(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_workflow_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def upload_read_set_part(
        self,
        res: "bs_td.UploadReadSetPartResponseTypeDef",
    ) -> "dc_td.UploadReadSetPartResponse":
        return dc_td.UploadReadSetPartResponse.make_one(res)


omics_caster = OMICSCaster()
