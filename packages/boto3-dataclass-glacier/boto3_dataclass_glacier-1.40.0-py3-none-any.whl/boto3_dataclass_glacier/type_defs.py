# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_glacier import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AbortMultipartUploadInput:
    boto3_raw_data: "type_defs.AbortMultipartUploadInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    uploadId = field("uploadId")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AbortMultipartUploadInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortMultipartUploadInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AbortVaultLockInput:
    boto3_raw_data: "type_defs.AbortVaultLockInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AbortVaultLockInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortVaultLockInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsToVaultInput:
    boto3_raw_data: "type_defs.AddTagsToVaultInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddTagsToVaultInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTagsToVaultInputTypeDef"]
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
class CSVInput:
    boto3_raw_data: "type_defs.CSVInputTypeDef" = dataclasses.field()

    FileHeaderInfo = field("FileHeaderInfo")
    Comments = field("Comments")
    QuoteEscapeCharacter = field("QuoteEscapeCharacter")
    RecordDelimiter = field("RecordDelimiter")
    FieldDelimiter = field("FieldDelimiter")
    QuoteCharacter = field("QuoteCharacter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CSVInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CSVInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CSVOutput:
    boto3_raw_data: "type_defs.CSVOutputTypeDef" = dataclasses.field()

    QuoteFields = field("QuoteFields")
    QuoteEscapeCharacter = field("QuoteEscapeCharacter")
    RecordDelimiter = field("RecordDelimiter")
    FieldDelimiter = field("FieldDelimiter")
    QuoteCharacter = field("QuoteCharacter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CSVOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CSVOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteMultipartUploadInputMultipartUploadComplete:
    boto3_raw_data: (
        "type_defs.CompleteMultipartUploadInputMultipartUploadCompleteTypeDef"
    ) = dataclasses.field()

    archiveSize = field("archiveSize")
    checksum = field("checksum")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompleteMultipartUploadInputMultipartUploadCompleteTypeDef"
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
                "type_defs.CompleteMultipartUploadInputMultipartUploadCompleteTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteMultipartUploadInput:
    boto3_raw_data: "type_defs.CompleteMultipartUploadInputTypeDef" = (
        dataclasses.field()
    )

    vaultName = field("vaultName")
    uploadId = field("uploadId")
    accountId = field("accountId")
    archiveSize = field("archiveSize")
    checksum = field("checksum")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompleteMultipartUploadInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteMultipartUploadInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteVaultLockInput:
    boto3_raw_data: "type_defs.CompleteVaultLockInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    lockId = field("lockId")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompleteVaultLockInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteVaultLockInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVaultInputAccountCreateVault:
    boto3_raw_data: "type_defs.CreateVaultInputAccountCreateVaultTypeDef" = (
        dataclasses.field()
    )

    vaultName = field("vaultName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVaultInputAccountCreateVaultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVaultInputAccountCreateVaultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVaultInputServiceResourceCreateVault:
    boto3_raw_data: "type_defs.CreateVaultInputServiceResourceCreateVaultTypeDef" = (
        dataclasses.field()
    )

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVaultInputServiceResourceCreateVaultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVaultInputServiceResourceCreateVaultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVaultInput:
    boto3_raw_data: "type_defs.CreateVaultInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateVaultInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataRetrievalRule:
    boto3_raw_data: "type_defs.DataRetrievalRuleTypeDef" = dataclasses.field()

    Strategy = field("Strategy")
    BytesPerHour = field("BytesPerHour")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataRetrievalRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataRetrievalRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteArchiveInput:
    boto3_raw_data: "type_defs.DeleteArchiveInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    archiveId = field("archiveId")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteArchiveInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteArchiveInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVaultAccessPolicyInput:
    boto3_raw_data: "type_defs.DeleteVaultAccessPolicyInputTypeDef" = (
        dataclasses.field()
    )

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVaultAccessPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVaultAccessPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVaultInput:
    boto3_raw_data: "type_defs.DeleteVaultInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteVaultInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVaultNotificationsInput:
    boto3_raw_data: "type_defs.DeleteVaultNotificationsInputTypeDef" = (
        dataclasses.field()
    )

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVaultNotificationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVaultNotificationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobInput:
    boto3_raw_data: "type_defs.DescribeJobInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    jobId = field("jobId")
    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeJobInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVaultInput:
    boto3_raw_data: "type_defs.DescribeVaultInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVaultInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVaultInputTypeDef"]
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
class DescribeVaultOutput:
    boto3_raw_data: "type_defs.DescribeVaultOutputTypeDef" = dataclasses.field()

    VaultARN = field("VaultARN")
    VaultName = field("VaultName")
    CreationDate = field("CreationDate")
    LastInventoryDate = field("LastInventoryDate")
    NumberOfArchives = field("NumberOfArchives")
    SizeInBytes = field("SizeInBytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVaultOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVaultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Encryption:
    boto3_raw_data: "type_defs.EncryptionTypeDef" = dataclasses.field()

    EncryptionType = field("EncryptionType")
    KMSKeyId = field("KMSKeyId")
    KMSContext = field("KMSContext")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncryptionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataRetrievalPolicyInput:
    boto3_raw_data: "type_defs.GetDataRetrievalPolicyInputTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataRetrievalPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataRetrievalPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobOutputInputJobGetOutput:
    boto3_raw_data: "type_defs.GetJobOutputInputJobGetOutputTypeDef" = (
        dataclasses.field()
    )

    range = field("range")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetJobOutputInputJobGetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobOutputInputJobGetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobOutputInput:
    boto3_raw_data: "type_defs.GetJobOutputInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    jobId = field("jobId")
    accountId = field("accountId")
    range = field("range")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobOutputInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobOutputInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVaultAccessPolicyInput:
    boto3_raw_data: "type_defs.GetVaultAccessPolicyInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVaultAccessPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVaultAccessPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VaultAccessPolicy:
    boto3_raw_data: "type_defs.VaultAccessPolicyTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VaultAccessPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VaultAccessPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVaultLockInput:
    boto3_raw_data: "type_defs.GetVaultLockInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetVaultLockInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVaultLockInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVaultNotificationsInput:
    boto3_raw_data: "type_defs.GetVaultNotificationsInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVaultNotificationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVaultNotificationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VaultNotificationConfigOutput:
    boto3_raw_data: "type_defs.VaultNotificationConfigOutputTypeDef" = (
        dataclasses.field()
    )

    SNSTopic = field("SNSTopic")
    Events = field("Events")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VaultNotificationConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VaultNotificationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryRetrievalJobDescription:
    boto3_raw_data: "type_defs.InventoryRetrievalJobDescriptionTypeDef" = (
        dataclasses.field()
    )

    Format = field("Format")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InventoryRetrievalJobDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryRetrievalJobDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Grantee:
    boto3_raw_data: "type_defs.GranteeTypeDef" = dataclasses.field()

    Type = field("Type")
    DisplayName = field("DisplayName")
    URI = field("URI")
    ID = field("ID")
    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GranteeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GranteeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateMultipartUploadInput:
    boto3_raw_data: "type_defs.InitiateMultipartUploadInputTypeDef" = (
        dataclasses.field()
    )

    vaultName = field("vaultName")
    accountId = field("accountId")
    archiveDescription = field("archiveDescription")
    partSize = field("partSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitiateMultipartUploadInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateMultipartUploadInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateMultipartUploadInputVaultInitiateMultipartUpload:
    boto3_raw_data: (
        "type_defs.InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef"
    ) = dataclasses.field()

    archiveDescription = field("archiveDescription")
    partSize = field("partSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef"
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
                "type_defs.InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VaultLockPolicy:
    boto3_raw_data: "type_defs.VaultLockPolicyTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VaultLockPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VaultLockPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryRetrievalJobInput:
    boto3_raw_data: "type_defs.InventoryRetrievalJobInputTypeDef" = dataclasses.field()

    StartDate = field("StartDate")
    EndDate = field("EndDate")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryRetrievalJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryRetrievalJobInputTypeDef"]
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
class ListJobsInput:
    boto3_raw_data: "type_defs.ListJobsInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")
    limit = field("limit")
    marker = field("marker")
    statuscode = field("statuscode")
    completed = field("completed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultipartUploadsInput:
    boto3_raw_data: "type_defs.ListMultipartUploadsInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")
    marker = field("marker")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMultipartUploadsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultipartUploadsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadListElement:
    boto3_raw_data: "type_defs.UploadListElementTypeDef" = dataclasses.field()

    MultipartUploadId = field("MultipartUploadId")
    VaultARN = field("VaultARN")
    ArchiveDescription = field("ArchiveDescription")
    PartSizeInBytes = field("PartSizeInBytes")
    CreationDate = field("CreationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UploadListElementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadListElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartsInputMultipartUploadParts:
    boto3_raw_data: "type_defs.ListPartsInputMultipartUploadPartsTypeDef" = (
        dataclasses.field()
    )

    marker = field("marker")
    limit = field("limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPartsInputMultipartUploadPartsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartsInputMultipartUploadPartsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartsInput:
    boto3_raw_data: "type_defs.ListPartsInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    uploadId = field("uploadId")
    accountId = field("accountId")
    marker = field("marker")
    limit = field("limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListPartsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListPartsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartListElement:
    boto3_raw_data: "type_defs.PartListElementTypeDef" = dataclasses.field()

    RangeInBytes = field("RangeInBytes")
    SHA256TreeHash = field("SHA256TreeHash")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartListElementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PartListElementTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedCapacityInput:
    boto3_raw_data: "type_defs.ListProvisionedCapacityInputTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProvisionedCapacityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisionedCapacityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedCapacityDescription:
    boto3_raw_data: "type_defs.ProvisionedCapacityDescriptionTypeDef" = (
        dataclasses.field()
    )

    CapacityId = field("CapacityId")
    StartDate = field("StartDate")
    ExpirationDate = field("ExpirationDate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisionedCapacityDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedCapacityDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForVaultInput:
    boto3_raw_data: "type_defs.ListTagsForVaultInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForVaultInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVaultsInput:
    boto3_raw_data: "type_defs.ListVaultsInputTypeDef" = dataclasses.field()

    accountId = field("accountId")
    marker = field("marker")
    limit = field("limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListVaultsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListVaultsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseProvisionedCapacityInput:
    boto3_raw_data: "type_defs.PurchaseProvisionedCapacityInputTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PurchaseProvisionedCapacityInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseProvisionedCapacityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsFromVaultInput:
    boto3_raw_data: "type_defs.RemoveTagsFromVaultInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveTagsFromVaultInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsFromVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VaultNotificationConfig:
    boto3_raw_data: "type_defs.VaultNotificationConfigTypeDef" = dataclasses.field()

    SNSTopic = field("SNSTopic")
    Events = field("Events")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VaultNotificationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VaultNotificationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveCreationOutput:
    boto3_raw_data: "type_defs.ArchiveCreationOutputTypeDef" = dataclasses.field()

    location = field("location")
    checksum = field("checksum")
    archiveId = field("archiveId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveCreationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveCreationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVaultOutput:
    boto3_raw_data: "type_defs.CreateVaultOutputTypeDef" = dataclasses.field()

    location = field("location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateVaultOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVaultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVaultResponse:
    boto3_raw_data: "type_defs.DescribeVaultResponseTypeDef" = dataclasses.field()

    VaultARN = field("VaultARN")
    VaultName = field("VaultName")
    CreationDate = field("CreationDate")
    LastInventoryDate = field("LastInventoryDate")
    NumberOfArchives = field("NumberOfArchives")
    SizeInBytes = field("SizeInBytes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVaultResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVaultResponseTypeDef"]
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
class GetJobOutputOutput:
    boto3_raw_data: "type_defs.GetJobOutputOutputTypeDef" = dataclasses.field()

    body = field("body")
    checksum = field("checksum")
    status = field("status")
    contentRange = field("contentRange")
    acceptRanges = field("acceptRanges")
    contentType = field("contentType")
    archiveDescription = field("archiveDescription")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobOutputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobOutputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVaultLockOutput:
    boto3_raw_data: "type_defs.GetVaultLockOutputTypeDef" = dataclasses.field()

    Policy = field("Policy")
    State = field("State")
    ExpirationDate = field("ExpirationDate")
    CreationDate = field("CreationDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVaultLockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVaultLockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateJobOutput:
    boto3_raw_data: "type_defs.InitiateJobOutputTypeDef" = dataclasses.field()

    location = field("location")
    jobId = field("jobId")
    jobOutputPath = field("jobOutputPath")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InitiateJobOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateMultipartUploadOutput:
    boto3_raw_data: "type_defs.InitiateMultipartUploadOutputTypeDef" = (
        dataclasses.field()
    )

    location = field("location")
    uploadId = field("uploadId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InitiateMultipartUploadOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateMultipartUploadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateVaultLockOutput:
    boto3_raw_data: "type_defs.InitiateVaultLockOutputTypeDef" = dataclasses.field()

    lockId = field("lockId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitiateVaultLockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateVaultLockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForVaultOutput:
    boto3_raw_data: "type_defs.ListTagsForVaultOutputTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForVaultOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForVaultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseProvisionedCapacityOutput:
    boto3_raw_data: "type_defs.PurchaseProvisionedCapacityOutputTypeDef" = (
        dataclasses.field()
    )

    capacityId = field("capacityId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseProvisionedCapacityOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseProvisionedCapacityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadMultipartPartOutput:
    boto3_raw_data: "type_defs.UploadMultipartPartOutputTypeDef" = dataclasses.field()

    checksum = field("checksum")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadMultipartPartOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadMultipartPartOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadArchiveInput:
    boto3_raw_data: "type_defs.UploadArchiveInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")
    archiveDescription = field("archiveDescription")
    checksum = field("checksum")
    body = field("body")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadArchiveInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadArchiveInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadArchiveInputVaultUploadArchive:
    boto3_raw_data: "type_defs.UploadArchiveInputVaultUploadArchiveTypeDef" = (
        dataclasses.field()
    )

    archiveDescription = field("archiveDescription")
    checksum = field("checksum")
    body = field("body")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UploadArchiveInputVaultUploadArchiveTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadArchiveInputVaultUploadArchiveTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadMultipartPartInputMultipartUploadUploadPart:
    boto3_raw_data: (
        "type_defs.UploadMultipartPartInputMultipartUploadUploadPartTypeDef"
    ) = dataclasses.field()

    checksum = field("checksum")
    range = field("range")
    body = field("body")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UploadMultipartPartInputMultipartUploadUploadPartTypeDef"
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
                "type_defs.UploadMultipartPartInputMultipartUploadUploadPartTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadMultipartPartInput:
    boto3_raw_data: "type_defs.UploadMultipartPartInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    uploadId = field("uploadId")
    accountId = field("accountId")
    checksum = field("checksum")
    range = field("range")
    body = field("body")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadMultipartPartInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadMultipartPartInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSerialization:
    boto3_raw_data: "type_defs.InputSerializationTypeDef" = dataclasses.field()

    @cached_property
    def csv(self):  # pragma: no cover
        return CSVInput.make_one(self.boto3_raw_data["csv"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputSerializationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSerializationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputSerialization:
    boto3_raw_data: "type_defs.OutputSerializationTypeDef" = dataclasses.field()

    @cached_property
    def csv(self):  # pragma: no cover
        return CSVOutput.make_one(self.boto3_raw_data["csv"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputSerializationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputSerializationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataRetrievalPolicyOutput:
    boto3_raw_data: "type_defs.DataRetrievalPolicyOutputTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return DataRetrievalRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataRetrievalPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataRetrievalPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataRetrievalPolicy:
    boto3_raw_data: "type_defs.DataRetrievalPolicyTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return DataRetrievalRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataRetrievalPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataRetrievalPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVaultInputWaitExtra:
    boto3_raw_data: "type_defs.DescribeVaultInputWaitExtraTypeDef" = dataclasses.field()

    accountId = field("accountId")
    vaultName = field("vaultName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVaultInputWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVaultInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVaultInputWait:
    boto3_raw_data: "type_defs.DescribeVaultInputWaitTypeDef" = dataclasses.field()

    accountId = field("accountId")
    vaultName = field("vaultName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVaultInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVaultInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVaultsOutput:
    boto3_raw_data: "type_defs.ListVaultsOutputTypeDef" = dataclasses.field()

    @cached_property
    def VaultList(self):  # pragma: no cover
        return DescribeVaultOutput.make_many(self.boto3_raw_data["VaultList"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListVaultsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVaultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVaultAccessPolicyOutput:
    boto3_raw_data: "type_defs.GetVaultAccessPolicyOutputTypeDef" = dataclasses.field()

    @cached_property
    def policy(self):  # pragma: no cover
        return VaultAccessPolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVaultAccessPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVaultAccessPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetVaultAccessPolicyInput:
    boto3_raw_data: "type_defs.SetVaultAccessPolicyInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @cached_property
    def policy(self):  # pragma: no cover
        return VaultAccessPolicy.make_one(self.boto3_raw_data["policy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetVaultAccessPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetVaultAccessPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVaultNotificationsOutput:
    boto3_raw_data: "type_defs.GetVaultNotificationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def vaultNotificationConfig(self):  # pragma: no cover
        return VaultNotificationConfigOutput.make_one(
            self.boto3_raw_data["vaultNotificationConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVaultNotificationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVaultNotificationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Grant:
    boto3_raw_data: "type_defs.GrantTypeDef" = dataclasses.field()

    @cached_property
    def Grantee(self):  # pragma: no cover
        return Grantee.make_one(self.boto3_raw_data["Grantee"])

    Permission = field("Permission")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrantTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateVaultLockInput:
    boto3_raw_data: "type_defs.InitiateVaultLockInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @cached_property
    def policy(self):  # pragma: no cover
        return VaultLockPolicy.make_one(self.boto3_raw_data["policy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitiateVaultLockInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateVaultLockInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsInputPaginate:
    boto3_raw_data: "type_defs.ListJobsInputPaginateTypeDef" = dataclasses.field()

    accountId = field("accountId")
    vaultName = field("vaultName")
    statuscode = field("statuscode")
    completed = field("completed")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultipartUploadsInputPaginate:
    boto3_raw_data: "type_defs.ListMultipartUploadsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    vaultName = field("vaultName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMultipartUploadsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultipartUploadsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartsInputPaginate:
    boto3_raw_data: "type_defs.ListPartsInputPaginateTypeDef" = dataclasses.field()

    accountId = field("accountId")
    vaultName = field("vaultName")
    uploadId = field("uploadId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPartsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVaultsInputPaginate:
    boto3_raw_data: "type_defs.ListVaultsInputPaginateTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVaultsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVaultsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultipartUploadsOutput:
    boto3_raw_data: "type_defs.ListMultipartUploadsOutputTypeDef" = dataclasses.field()

    @cached_property
    def UploadsList(self):  # pragma: no cover
        return UploadListElement.make_many(self.boto3_raw_data["UploadsList"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMultipartUploadsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultipartUploadsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartsOutput:
    boto3_raw_data: "type_defs.ListPartsOutputTypeDef" = dataclasses.field()

    MultipartUploadId = field("MultipartUploadId")
    VaultARN = field("VaultARN")
    ArchiveDescription = field("ArchiveDescription")
    PartSizeInBytes = field("PartSizeInBytes")
    CreationDate = field("CreationDate")

    @cached_property
    def Parts(self):  # pragma: no cover
        return PartListElement.make_many(self.boto3_raw_data["Parts"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListPartsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListPartsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedCapacityOutput:
    boto3_raw_data: "type_defs.ListProvisionedCapacityOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisionedCapacityList(self):  # pragma: no cover
        return ProvisionedCapacityDescription.make_many(
            self.boto3_raw_data["ProvisionedCapacityList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProvisionedCapacityOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisionedCapacityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectParameters:
    boto3_raw_data: "type_defs.SelectParametersTypeDef" = dataclasses.field()

    @cached_property
    def InputSerialization(self):  # pragma: no cover
        return InputSerialization.make_one(self.boto3_raw_data["InputSerialization"])

    ExpressionType = field("ExpressionType")
    Expression = field("Expression")

    @cached_property
    def OutputSerialization(self):  # pragma: no cover
        return OutputSerialization.make_one(self.boto3_raw_data["OutputSerialization"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SelectParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataRetrievalPolicyOutput:
    boto3_raw_data: "type_defs.GetDataRetrievalPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Policy(self):  # pragma: no cover
        return DataRetrievalPolicyOutput.make_one(self.boto3_raw_data["Policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataRetrievalPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataRetrievalPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3LocationOutput:
    boto3_raw_data: "type_defs.S3LocationOutputTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    Prefix = field("Prefix")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    CannedACL = field("CannedACL")

    @cached_property
    def AccessControlList(self):  # pragma: no cover
        return Grant.make_many(self.boto3_raw_data["AccessControlList"])

    Tagging = field("Tagging")
    UserMetadata = field("UserMetadata")
    StorageClass = field("StorageClass")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3LocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    Prefix = field("Prefix")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    CannedACL = field("CannedACL")

    @cached_property
    def AccessControlList(self):  # pragma: no cover
        return Grant.make_many(self.boto3_raw_data["AccessControlList"])

    Tagging = field("Tagging")
    UserMetadata = field("UserMetadata")
    StorageClass = field("StorageClass")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetVaultNotificationsInputNotificationSet:
    boto3_raw_data: "type_defs.SetVaultNotificationsInputNotificationSetTypeDef" = (
        dataclasses.field()
    )

    vaultNotificationConfig = field("vaultNotificationConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetVaultNotificationsInputNotificationSetTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetVaultNotificationsInputNotificationSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetVaultNotificationsInput:
    boto3_raw_data: "type_defs.SetVaultNotificationsInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")
    vaultNotificationConfig = field("vaultNotificationConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetVaultNotificationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetVaultNotificationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDataRetrievalPolicyInput:
    boto3_raw_data: "type_defs.SetDataRetrievalPolicyInputTypeDef" = dataclasses.field()

    accountId = field("accountId")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetDataRetrievalPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDataRetrievalPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputLocationOutput:
    boto3_raw_data: "type_defs.OutputLocationOutputTypeDef" = dataclasses.field()

    @cached_property
    def S3(self):  # pragma: no cover
        return S3LocationOutput.make_one(self.boto3_raw_data["S3"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputLocationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputLocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlacierJobDescriptionResponse:
    boto3_raw_data: "type_defs.GlacierJobDescriptionResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobDescription = field("JobDescription")
    Action = field("Action")
    ArchiveId = field("ArchiveId")
    VaultARN = field("VaultARN")
    CreationDate = field("CreationDate")
    Completed = field("Completed")
    StatusCode = field("StatusCode")
    StatusMessage = field("StatusMessage")
    ArchiveSizeInBytes = field("ArchiveSizeInBytes")
    InventorySizeInBytes = field("InventorySizeInBytes")
    SNSTopic = field("SNSTopic")
    CompletionDate = field("CompletionDate")
    SHA256TreeHash = field("SHA256TreeHash")
    ArchiveSHA256TreeHash = field("ArchiveSHA256TreeHash")
    RetrievalByteRange = field("RetrievalByteRange")
    Tier = field("Tier")

    @cached_property
    def InventoryRetrievalParameters(self):  # pragma: no cover
        return InventoryRetrievalJobDescription.make_one(
            self.boto3_raw_data["InventoryRetrievalParameters"]
        )

    JobOutputPath = field("JobOutputPath")

    @cached_property
    def SelectParameters(self):  # pragma: no cover
        return SelectParameters.make_one(self.boto3_raw_data["SelectParameters"])

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return OutputLocationOutput.make_one(self.boto3_raw_data["OutputLocation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GlacierJobDescriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlacierJobDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlacierJobDescription:
    boto3_raw_data: "type_defs.GlacierJobDescriptionTypeDef" = dataclasses.field()

    JobId = field("JobId")
    JobDescription = field("JobDescription")
    Action = field("Action")
    ArchiveId = field("ArchiveId")
    VaultARN = field("VaultARN")
    CreationDate = field("CreationDate")
    Completed = field("Completed")
    StatusCode = field("StatusCode")
    StatusMessage = field("StatusMessage")
    ArchiveSizeInBytes = field("ArchiveSizeInBytes")
    InventorySizeInBytes = field("InventorySizeInBytes")
    SNSTopic = field("SNSTopic")
    CompletionDate = field("CompletionDate")
    SHA256TreeHash = field("SHA256TreeHash")
    ArchiveSHA256TreeHash = field("ArchiveSHA256TreeHash")
    RetrievalByteRange = field("RetrievalByteRange")
    Tier = field("Tier")

    @cached_property
    def InventoryRetrievalParameters(self):  # pragma: no cover
        return InventoryRetrievalJobDescription.make_one(
            self.boto3_raw_data["InventoryRetrievalParameters"]
        )

    JobOutputPath = field("JobOutputPath")

    @cached_property
    def SelectParameters(self):  # pragma: no cover
        return SelectParameters.make_one(self.boto3_raw_data["SelectParameters"])

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return OutputLocationOutput.make_one(self.boto3_raw_data["OutputLocation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlacierJobDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlacierJobDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputLocation:
    boto3_raw_data: "type_defs.OutputLocationTypeDef" = dataclasses.field()

    S3 = field("S3")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsOutput:
    boto3_raw_data: "type_defs.ListJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def JobList(self):  # pragma: no cover
        return GlacierJobDescription.make_many(self.boto3_raw_data["JobList"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobParameters:
    boto3_raw_data: "type_defs.JobParametersTypeDef" = dataclasses.field()

    Format = field("Format")
    Type = field("Type")
    ArchiveId = field("ArchiveId")
    Description = field("Description")
    SNSTopic = field("SNSTopic")
    RetrievalByteRange = field("RetrievalByteRange")
    Tier = field("Tier")

    @cached_property
    def InventoryRetrievalParameters(self):  # pragma: no cover
        return InventoryRetrievalJobInput.make_one(
            self.boto3_raw_data["InventoryRetrievalParameters"]
        )

    @cached_property
    def SelectParameters(self):  # pragma: no cover
        return SelectParameters.make_one(self.boto3_raw_data["SelectParameters"])

    OutputLocation = field("OutputLocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateJobInput:
    boto3_raw_data: "type_defs.InitiateJobInputTypeDef" = dataclasses.field()

    vaultName = field("vaultName")
    accountId = field("accountId")

    @cached_property
    def jobParameters(self):  # pragma: no cover
        return JobParameters.make_one(self.boto3_raw_data["jobParameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InitiateJobInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
