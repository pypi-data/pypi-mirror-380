# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_s3tables import type_defs as bs_td


class S3TABLESCaster:

    def create_namespace(
        self,
        res: "bs_td.CreateNamespaceResponseTypeDef",
    ) -> "dc_td.CreateNamespaceResponse":
        return dc_td.CreateNamespaceResponse.make_one(res)

    def create_table(
        self,
        res: "bs_td.CreateTableResponseTypeDef",
    ) -> "dc_td.CreateTableResponse":
        return dc_td.CreateTableResponse.make_one(res)

    def create_table_bucket(
        self,
        res: "bs_td.CreateTableBucketResponseTypeDef",
    ) -> "dc_td.CreateTableBucketResponse":
        return dc_td.CreateTableBucketResponse.make_one(res)

    def delete_namespace(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_table(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_table_bucket(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_table_bucket_encryption(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_table_bucket_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_table_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_namespace(
        self,
        res: "bs_td.GetNamespaceResponseTypeDef",
    ) -> "dc_td.GetNamespaceResponse":
        return dc_td.GetNamespaceResponse.make_one(res)

    def get_table(
        self,
        res: "bs_td.GetTableResponseTypeDef",
    ) -> "dc_td.GetTableResponse":
        return dc_td.GetTableResponse.make_one(res)

    def get_table_bucket(
        self,
        res: "bs_td.GetTableBucketResponseTypeDef",
    ) -> "dc_td.GetTableBucketResponse":
        return dc_td.GetTableBucketResponse.make_one(res)

    def get_table_bucket_encryption(
        self,
        res: "bs_td.GetTableBucketEncryptionResponseTypeDef",
    ) -> "dc_td.GetTableBucketEncryptionResponse":
        return dc_td.GetTableBucketEncryptionResponse.make_one(res)

    def get_table_bucket_maintenance_configuration(
        self,
        res: "bs_td.GetTableBucketMaintenanceConfigurationResponseTypeDef",
    ) -> "dc_td.GetTableBucketMaintenanceConfigurationResponse":
        return dc_td.GetTableBucketMaintenanceConfigurationResponse.make_one(res)

    def get_table_bucket_policy(
        self,
        res: "bs_td.GetTableBucketPolicyResponseTypeDef",
    ) -> "dc_td.GetTableBucketPolicyResponse":
        return dc_td.GetTableBucketPolicyResponse.make_one(res)

    def get_table_encryption(
        self,
        res: "bs_td.GetTableEncryptionResponseTypeDef",
    ) -> "dc_td.GetTableEncryptionResponse":
        return dc_td.GetTableEncryptionResponse.make_one(res)

    def get_table_maintenance_configuration(
        self,
        res: "bs_td.GetTableMaintenanceConfigurationResponseTypeDef",
    ) -> "dc_td.GetTableMaintenanceConfigurationResponse":
        return dc_td.GetTableMaintenanceConfigurationResponse.make_one(res)

    def get_table_maintenance_job_status(
        self,
        res: "bs_td.GetTableMaintenanceJobStatusResponseTypeDef",
    ) -> "dc_td.GetTableMaintenanceJobStatusResponse":
        return dc_td.GetTableMaintenanceJobStatusResponse.make_one(res)

    def get_table_metadata_location(
        self,
        res: "bs_td.GetTableMetadataLocationResponseTypeDef",
    ) -> "dc_td.GetTableMetadataLocationResponse":
        return dc_td.GetTableMetadataLocationResponse.make_one(res)

    def get_table_policy(
        self,
        res: "bs_td.GetTablePolicyResponseTypeDef",
    ) -> "dc_td.GetTablePolicyResponse":
        return dc_td.GetTablePolicyResponse.make_one(res)

    def list_namespaces(
        self,
        res: "bs_td.ListNamespacesResponseTypeDef",
    ) -> "dc_td.ListNamespacesResponse":
        return dc_td.ListNamespacesResponse.make_one(res)

    def list_table_buckets(
        self,
        res: "bs_td.ListTableBucketsResponseTypeDef",
    ) -> "dc_td.ListTableBucketsResponse":
        return dc_td.ListTableBucketsResponse.make_one(res)

    def list_tables(
        self,
        res: "bs_td.ListTablesResponseTypeDef",
    ) -> "dc_td.ListTablesResponse":
        return dc_td.ListTablesResponse.make_one(res)

    def put_table_bucket_encryption(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_table_bucket_maintenance_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_table_bucket_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_table_maintenance_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_table_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def rename_table(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_table_metadata_location(
        self,
        res: "bs_td.UpdateTableMetadataLocationResponseTypeDef",
    ) -> "dc_td.UpdateTableMetadataLocationResponse":
        return dc_td.UpdateTableMetadataLocationResponse.make_one(res)


s3tables_caster = S3TABLESCaster()
