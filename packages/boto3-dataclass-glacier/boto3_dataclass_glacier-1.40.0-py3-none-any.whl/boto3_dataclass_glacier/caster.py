# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_glacier import type_defs as bs_td


class GLACIERCaster:

    def abort_multipart_upload(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def abort_vault_lock(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def add_tags_to_vault(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def complete_multipart_upload(
        self,
        res: "bs_td.ArchiveCreationOutputTypeDef",
    ) -> "dc_td.ArchiveCreationOutput":
        return dc_td.ArchiveCreationOutput.make_one(res)

    def complete_vault_lock(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_vault(
        self,
        res: "bs_td.CreateVaultOutputTypeDef",
    ) -> "dc_td.CreateVaultOutput":
        return dc_td.CreateVaultOutput.make_one(res)

    def delete_archive(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vault(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vault_access_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vault_notifications(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_job(
        self,
        res: "bs_td.GlacierJobDescriptionResponseTypeDef",
    ) -> "dc_td.GlacierJobDescriptionResponse":
        return dc_td.GlacierJobDescriptionResponse.make_one(res)

    def describe_vault(
        self,
        res: "bs_td.DescribeVaultResponseTypeDef",
    ) -> "dc_td.DescribeVaultResponse":
        return dc_td.DescribeVaultResponse.make_one(res)

    def get_data_retrieval_policy(
        self,
        res: "bs_td.GetDataRetrievalPolicyOutputTypeDef",
    ) -> "dc_td.GetDataRetrievalPolicyOutput":
        return dc_td.GetDataRetrievalPolicyOutput.make_one(res)

    def get_job_output(
        self,
        res: "bs_td.GetJobOutputOutputTypeDef",
    ) -> "dc_td.GetJobOutputOutput":
        return dc_td.GetJobOutputOutput.make_one(res)

    def get_vault_access_policy(
        self,
        res: "bs_td.GetVaultAccessPolicyOutputTypeDef",
    ) -> "dc_td.GetVaultAccessPolicyOutput":
        return dc_td.GetVaultAccessPolicyOutput.make_one(res)

    def get_vault_lock(
        self,
        res: "bs_td.GetVaultLockOutputTypeDef",
    ) -> "dc_td.GetVaultLockOutput":
        return dc_td.GetVaultLockOutput.make_one(res)

    def get_vault_notifications(
        self,
        res: "bs_td.GetVaultNotificationsOutputTypeDef",
    ) -> "dc_td.GetVaultNotificationsOutput":
        return dc_td.GetVaultNotificationsOutput.make_one(res)

    def initiate_job(
        self,
        res: "bs_td.InitiateJobOutputTypeDef",
    ) -> "dc_td.InitiateJobOutput":
        return dc_td.InitiateJobOutput.make_one(res)

    def initiate_multipart_upload(
        self,
        res: "bs_td.InitiateMultipartUploadOutputTypeDef",
    ) -> "dc_td.InitiateMultipartUploadOutput":
        return dc_td.InitiateMultipartUploadOutput.make_one(res)

    def initiate_vault_lock(
        self,
        res: "bs_td.InitiateVaultLockOutputTypeDef",
    ) -> "dc_td.InitiateVaultLockOutput":
        return dc_td.InitiateVaultLockOutput.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsOutputTypeDef",
    ) -> "dc_td.ListJobsOutput":
        return dc_td.ListJobsOutput.make_one(res)

    def list_multipart_uploads(
        self,
        res: "bs_td.ListMultipartUploadsOutputTypeDef",
    ) -> "dc_td.ListMultipartUploadsOutput":
        return dc_td.ListMultipartUploadsOutput.make_one(res)

    def list_parts(
        self,
        res: "bs_td.ListPartsOutputTypeDef",
    ) -> "dc_td.ListPartsOutput":
        return dc_td.ListPartsOutput.make_one(res)

    def list_provisioned_capacity(
        self,
        res: "bs_td.ListProvisionedCapacityOutputTypeDef",
    ) -> "dc_td.ListProvisionedCapacityOutput":
        return dc_td.ListProvisionedCapacityOutput.make_one(res)

    def list_tags_for_vault(
        self,
        res: "bs_td.ListTagsForVaultOutputTypeDef",
    ) -> "dc_td.ListTagsForVaultOutput":
        return dc_td.ListTagsForVaultOutput.make_one(res)

    def list_vaults(
        self,
        res: "bs_td.ListVaultsOutputTypeDef",
    ) -> "dc_td.ListVaultsOutput":
        return dc_td.ListVaultsOutput.make_one(res)

    def purchase_provisioned_capacity(
        self,
        res: "bs_td.PurchaseProvisionedCapacityOutputTypeDef",
    ) -> "dc_td.PurchaseProvisionedCapacityOutput":
        return dc_td.PurchaseProvisionedCapacityOutput.make_one(res)

    def remove_tags_from_vault(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_data_retrieval_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_vault_access_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_vault_notifications(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def upload_archive(
        self,
        res: "bs_td.ArchiveCreationOutputTypeDef",
    ) -> "dc_td.ArchiveCreationOutput":
        return dc_td.ArchiveCreationOutput.make_one(res)

    def upload_multipart_part(
        self,
        res: "bs_td.UploadMultipartPartOutputTypeDef",
    ) -> "dc_td.UploadMultipartPartOutput":
        return dc_td.UploadMultipartPartOutput.make_one(res)


glacier_caster = GLACIERCaster()
