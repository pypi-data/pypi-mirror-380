# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_s3tables import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CreateNamespaceRequest:
    boto3_raw_data: "type_defs.CreateNamespaceRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNamespaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNamespaceRequestTypeDef"]
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
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    sseAlgorithm = field("sseAlgorithm")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNamespaceRequest:
    boto3_raw_data: "type_defs.DeleteNamespaceRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNamespaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTableBucketEncryptionRequest:
    boto3_raw_data: "type_defs.DeleteTableBucketEncryptionRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTableBucketEncryptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTableBucketEncryptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTableBucketPolicyRequest:
    boto3_raw_data: "type_defs.DeleteTableBucketPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteTableBucketPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTableBucketPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTableBucketRequest:
    boto3_raw_data: "type_defs.DeleteTableBucketRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTableBucketRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTableBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTablePolicyRequest:
    boto3_raw_data: "type_defs.DeleteTablePolicyRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTablePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTablePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTableRequest:
    boto3_raw_data: "type_defs.DeleteTableRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")
    versionToken = field("versionToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTableRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNamespaceRequest:
    boto3_raw_data: "type_defs.GetNamespaceRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNamespaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableBucketEncryptionRequest:
    boto3_raw_data: "type_defs.GetTableBucketEncryptionRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTableBucketEncryptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableBucketEncryptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableBucketMaintenanceConfigurationRequest:
    boto3_raw_data: "type_defs.GetTableBucketMaintenanceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTableBucketMaintenanceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableBucketMaintenanceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableBucketPolicyRequest:
    boto3_raw_data: "type_defs.GetTableBucketPolicyRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableBucketPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableBucketPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableBucketRequest:
    boto3_raw_data: "type_defs.GetTableBucketRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableBucketRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableEncryptionRequest:
    boto3_raw_data: "type_defs.GetTableEncryptionRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableEncryptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableEncryptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableMaintenanceConfigurationRequest:
    boto3_raw_data: "type_defs.GetTableMaintenanceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTableMaintenanceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableMaintenanceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableMaintenanceJobStatusRequest:
    boto3_raw_data: "type_defs.GetTableMaintenanceJobStatusRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTableMaintenanceJobStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableMaintenanceJobStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableMaintenanceJobStatusValue:
    boto3_raw_data: "type_defs.TableMaintenanceJobStatusValueTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    lastRunTimestamp = field("lastRunTimestamp")
    failureMessage = field("failureMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TableMaintenanceJobStatusValueTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableMaintenanceJobStatusValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableMetadataLocationRequest:
    boto3_raw_data: "type_defs.GetTableMetadataLocationRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTableMetadataLocationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableMetadataLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTablePolicyRequest:
    boto3_raw_data: "type_defs.GetTablePolicyRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTablePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTablePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableRequest:
    boto3_raw_data: "type_defs.GetTableRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")
    tableArn = field("tableArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTableRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTableRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IcebergCompactionSettings:
    boto3_raw_data: "type_defs.IcebergCompactionSettingsTypeDef" = dataclasses.field()

    targetFileSizeMB = field("targetFileSizeMB")
    strategy = field("strategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IcebergCompactionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IcebergCompactionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaField:
    boto3_raw_data: "type_defs.SchemaFieldTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    required = field("required")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchemaFieldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IcebergSnapshotManagementSettings:
    boto3_raw_data: "type_defs.IcebergSnapshotManagementSettingsTypeDef" = (
        dataclasses.field()
    )

    minSnapshotsToKeep = field("minSnapshotsToKeep")
    maxSnapshotAgeHours = field("maxSnapshotAgeHours")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IcebergSnapshotManagementSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IcebergSnapshotManagementSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IcebergUnreferencedFileRemovalSettings:
    boto3_raw_data: "type_defs.IcebergUnreferencedFileRemovalSettingsTypeDef" = (
        dataclasses.field()
    )

    unreferencedDays = field("unreferencedDays")
    nonCurrentDays = field("nonCurrentDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IcebergUnreferencedFileRemovalSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IcebergUnreferencedFileRemovalSettingsTypeDef"]
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
class ListNamespacesRequest:
    boto3_raw_data: "type_defs.ListNamespacesRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    prefix = field("prefix")
    continuationToken = field("continuationToken")
    maxNamespaces = field("maxNamespaces")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNamespacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNamespacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NamespaceSummary:
    boto3_raw_data: "type_defs.NamespaceSummaryTypeDef" = dataclasses.field()

    namespace = field("namespace")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    ownerAccountId = field("ownerAccountId")
    namespaceId = field("namespaceId")
    tableBucketId = field("tableBucketId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NamespaceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NamespaceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableBucketsRequest:
    boto3_raw_data: "type_defs.ListTableBucketsRequestTypeDef" = dataclasses.field()

    prefix = field("prefix")
    continuationToken = field("continuationToken")
    maxBuckets = field("maxBuckets")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTableBucketsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableBucketsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableBucketSummary:
    boto3_raw_data: "type_defs.TableBucketSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    ownerAccountId = field("ownerAccountId")
    createdAt = field("createdAt")
    tableBucketId = field("tableBucketId")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableBucketSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableBucketSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTablesRequest:
    boto3_raw_data: "type_defs.ListTablesRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    prefix = field("prefix")
    continuationToken = field("continuationToken")
    maxTables = field("maxTables")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTablesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTablesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableSummary:
    boto3_raw_data: "type_defs.TableSummaryTypeDef" = dataclasses.field()

    namespace = field("namespace")
    name = field("name")
    type = field("type")
    tableARN = field("tableARN")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    namespaceId = field("namespaceId")
    tableBucketId = field("tableBucketId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTableBucketPolicyRequest:
    boto3_raw_data: "type_defs.PutTableBucketPolicyRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    resourcePolicy = field("resourcePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTableBucketPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTableBucketPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTablePolicyRequest:
    boto3_raw_data: "type_defs.PutTablePolicyRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")
    resourcePolicy = field("resourcePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTablePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTablePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenameTableRequest:
    boto3_raw_data: "type_defs.RenameTableRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")
    newNamespaceName = field("newNamespaceName")
    newName = field("newName")
    versionToken = field("versionToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RenameTableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RenameTableRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTableMetadataLocationRequest:
    boto3_raw_data: "type_defs.UpdateTableMetadataLocationRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")
    versionToken = field("versionToken")
    metadataLocation = field("metadataLocation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTableMetadataLocationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableMetadataLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNamespaceResponse:
    boto3_raw_data: "type_defs.CreateNamespaceResponseTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNamespaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTableBucketResponse:
    boto3_raw_data: "type_defs.CreateTableBucketResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTableBucketResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTableBucketResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTableResponse:
    boto3_raw_data: "type_defs.CreateTableResponseTypeDef" = dataclasses.field()

    tableARN = field("tableARN")
    versionToken = field("versionToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTableResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTableResponseTypeDef"]
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
class GetNamespaceResponse:
    boto3_raw_data: "type_defs.GetNamespaceResponseTypeDef" = dataclasses.field()

    namespace = field("namespace")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    ownerAccountId = field("ownerAccountId")
    namespaceId = field("namespaceId")
    tableBucketId = field("tableBucketId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNamespaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableBucketPolicyResponse:
    boto3_raw_data: "type_defs.GetTableBucketPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    resourcePolicy = field("resourcePolicy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableBucketPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableBucketPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableBucketResponse:
    boto3_raw_data: "type_defs.GetTableBucketResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    ownerAccountId = field("ownerAccountId")
    createdAt = field("createdAt")
    tableBucketId = field("tableBucketId")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableBucketResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableBucketResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableMetadataLocationResponse:
    boto3_raw_data: "type_defs.GetTableMetadataLocationResponseTypeDef" = (
        dataclasses.field()
    )

    versionToken = field("versionToken")
    metadataLocation = field("metadataLocation")
    warehouseLocation = field("warehouseLocation")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTableMetadataLocationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableMetadataLocationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTablePolicyResponse:
    boto3_raw_data: "type_defs.GetTablePolicyResponseTypeDef" = dataclasses.field()

    resourcePolicy = field("resourcePolicy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTablePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTablePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableResponse:
    boto3_raw_data: "type_defs.GetTableResponseTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    tableARN = field("tableARN")
    namespace = field("namespace")
    namespaceId = field("namespaceId")
    versionToken = field("versionToken")
    metadataLocation = field("metadataLocation")
    warehouseLocation = field("warehouseLocation")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    managedByService = field("managedByService")
    modifiedAt = field("modifiedAt")
    modifiedBy = field("modifiedBy")
    ownerAccountId = field("ownerAccountId")
    format = field("format")
    tableBucketId = field("tableBucketId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTableResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTableMetadataLocationResponse:
    boto3_raw_data: "type_defs.UpdateTableMetadataLocationResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    tableARN = field("tableARN")
    namespace = field("namespace")
    versionToken = field("versionToken")
    metadataLocation = field("metadataLocation")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTableMetadataLocationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableMetadataLocationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTableBucketRequest:
    boto3_raw_data: "type_defs.CreateTableBucketRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTableBucketRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTableBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableBucketEncryptionResponse:
    boto3_raw_data: "type_defs.GetTableBucketEncryptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTableBucketEncryptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableBucketEncryptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableEncryptionResponse:
    boto3_raw_data: "type_defs.GetTableEncryptionResponseTypeDef" = dataclasses.field()

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableEncryptionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableEncryptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTableBucketEncryptionRequest:
    boto3_raw_data: "type_defs.PutTableBucketEncryptionRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutTableBucketEncryptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTableBucketEncryptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableMaintenanceJobStatusResponse:
    boto3_raw_data: "type_defs.GetTableMaintenanceJobStatusResponseTypeDef" = (
        dataclasses.field()
    )

    tableARN = field("tableARN")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTableMaintenanceJobStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableMaintenanceJobStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IcebergSchema:
    boto3_raw_data: "type_defs.IcebergSchemaTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return SchemaField.make_many(self.boto3_raw_data["fields"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IcebergSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IcebergSchemaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableMaintenanceSettings:
    boto3_raw_data: "type_defs.TableMaintenanceSettingsTypeDef" = dataclasses.field()

    @cached_property
    def icebergCompaction(self):  # pragma: no cover
        return IcebergCompactionSettings.make_one(
            self.boto3_raw_data["icebergCompaction"]
        )

    @cached_property
    def icebergSnapshotManagement(self):  # pragma: no cover
        return IcebergSnapshotManagementSettings.make_one(
            self.boto3_raw_data["icebergSnapshotManagement"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableMaintenanceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableMaintenanceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableBucketMaintenanceSettings:
    boto3_raw_data: "type_defs.TableBucketMaintenanceSettingsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def icebergUnreferencedFileRemoval(self):  # pragma: no cover
        return IcebergUnreferencedFileRemovalSettings.make_one(
            self.boto3_raw_data["icebergUnreferencedFileRemoval"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TableBucketMaintenanceSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableBucketMaintenanceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNamespacesRequestPaginate:
    boto3_raw_data: "type_defs.ListNamespacesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")
    prefix = field("prefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNamespacesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNamespacesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableBucketsRequestPaginate:
    boto3_raw_data: "type_defs.ListTableBucketsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    prefix = field("prefix")
    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTableBucketsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableBucketsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTablesRequestPaginate:
    boto3_raw_data: "type_defs.ListTablesRequestPaginateTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    prefix = field("prefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTablesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTablesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNamespacesResponse:
    boto3_raw_data: "type_defs.ListNamespacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def namespaces(self):  # pragma: no cover
        return NamespaceSummary.make_many(self.boto3_raw_data["namespaces"])

    continuationToken = field("continuationToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNamespacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNamespacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableBucketsResponse:
    boto3_raw_data: "type_defs.ListTableBucketsResponseTypeDef" = dataclasses.field()

    @cached_property
    def tableBuckets(self):  # pragma: no cover
        return TableBucketSummary.make_many(self.boto3_raw_data["tableBuckets"])

    continuationToken = field("continuationToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTableBucketsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableBucketsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTablesResponse:
    boto3_raw_data: "type_defs.ListTablesResponseTypeDef" = dataclasses.field()

    @cached_property
    def tables(self):  # pragma: no cover
        return TableSummary.make_many(self.boto3_raw_data["tables"])

    continuationToken = field("continuationToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTablesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTablesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IcebergMetadata:
    boto3_raw_data: "type_defs.IcebergMetadataTypeDef" = dataclasses.field()

    @cached_property
    def schema(self):  # pragma: no cover
        return IcebergSchema.make_one(self.boto3_raw_data["schema"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IcebergMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IcebergMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableMaintenanceConfigurationValue:
    boto3_raw_data: "type_defs.TableMaintenanceConfigurationValueTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def settings(self):  # pragma: no cover
        return TableMaintenanceSettings.make_one(self.boto3_raw_data["settings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TableMaintenanceConfigurationValueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableMaintenanceConfigurationValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableBucketMaintenanceConfigurationValue:
    boto3_raw_data: "type_defs.TableBucketMaintenanceConfigurationValueTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def settings(self):  # pragma: no cover
        return TableBucketMaintenanceSettings.make_one(self.boto3_raw_data["settings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TableBucketMaintenanceConfigurationValueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableBucketMaintenanceConfigurationValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableMetadata:
    boto3_raw_data: "type_defs.TableMetadataTypeDef" = dataclasses.field()

    @cached_property
    def iceberg(self):  # pragma: no cover
        return IcebergMetadata.make_one(self.boto3_raw_data["iceberg"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableMaintenanceConfigurationResponse:
    boto3_raw_data: "type_defs.GetTableMaintenanceConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    tableARN = field("tableARN")
    configuration = field("configuration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTableMaintenanceConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableMaintenanceConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTableMaintenanceConfigurationRequest:
    boto3_raw_data: "type_defs.PutTableMaintenanceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")
    type = field("type")

    @cached_property
    def value(self):  # pragma: no cover
        return TableMaintenanceConfigurationValue.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutTableMaintenanceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTableMaintenanceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableBucketMaintenanceConfigurationResponse:
    boto3_raw_data: (
        "type_defs.GetTableBucketMaintenanceConfigurationResponseTypeDef"
    ) = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    configuration = field("configuration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTableBucketMaintenanceConfigurationResponseTypeDef"
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
                "type_defs.GetTableBucketMaintenanceConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTableBucketMaintenanceConfigurationRequest:
    boto3_raw_data: "type_defs.PutTableBucketMaintenanceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    tableBucketARN = field("tableBucketARN")
    type = field("type")

    @cached_property
    def value(self):  # pragma: no cover
        return TableBucketMaintenanceConfigurationValue.make_one(
            self.boto3_raw_data["value"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutTableBucketMaintenanceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTableBucketMaintenanceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTableRequest:
    boto3_raw_data: "type_defs.CreateTableRequestTypeDef" = dataclasses.field()

    tableBucketARN = field("tableBucketARN")
    namespace = field("namespace")
    name = field("name")
    format = field("format")

    @cached_property
    def metadata(self):  # pragma: no cover
        return TableMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTableRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
