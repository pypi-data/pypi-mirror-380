from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AccountId = str
Boolean = bool
EncryptionConfigurationKmsKeyArnString = str
ErrorMessage = str
ListNamespacesLimit = int
ListNamespacesRequestPrefixString = str
ListTableBucketsLimit = int
ListTableBucketsRequestPrefixString = str
ListTablesLimit = int
ListTablesRequestPrefixString = str
MetadataLocation = str
NamespaceId = str
NamespaceName = str
NextToken = str
PositiveInteger = int
ResourcePolicy = str
String = str
TableARN = str
TableBucketARN = str
TableBucketId = str
TableBucketName = str
TableName = str
VersionToken = str
WarehouseLocation = str


class IcebergCompactionStrategy(StrEnum):
    auto = "auto"
    binpack = "binpack"
    sort = "sort"
    z_order = "z-order"


class JobStatus(StrEnum):
    Not_Yet_Run = "Not_Yet_Run"
    Successful = "Successful"
    Failed = "Failed"
    Disabled = "Disabled"


class MaintenanceStatus(StrEnum):
    enabled = "enabled"
    disabled = "disabled"


class OpenTableFormat(StrEnum):
    ICEBERG = "ICEBERG"


class SSEAlgorithm(StrEnum):
    AES256 = "AES256"
    aws_kms = "aws:kms"


class TableBucketMaintenanceType(StrEnum):
    icebergUnreferencedFileRemoval = "icebergUnreferencedFileRemoval"


class TableBucketType(StrEnum):
    customer = "customer"
    aws = "aws"


class TableMaintenanceJobType(StrEnum):
    icebergCompaction = "icebergCompaction"
    icebergSnapshotManagement = "icebergSnapshotManagement"
    icebergUnreferencedFileRemoval = "icebergUnreferencedFileRemoval"


class TableMaintenanceType(StrEnum):
    icebergCompaction = "icebergCompaction"
    icebergSnapshotManagement = "icebergSnapshotManagement"


class TableType(StrEnum):
    customer = "customer"
    aws = "aws"


class AccessDeniedException(ServiceException):
    """The action cannot be performed because you do not have the required
    permission.
    """

    code: str = "AccessDeniedException"
    sender_fault: bool = True
    status_code: int = 403


class BadRequestException(ServiceException):
    """The request is invalid or malformed."""

    code: str = "BadRequestException"
    sender_fault: bool = True
    status_code: int = 400


class ConflictException(ServiceException):
    """The request failed because there is a conflict with a previous write.
    You can retry the request.
    """

    code: str = "ConflictException"
    sender_fault: bool = True
    status_code: int = 409


class ForbiddenException(ServiceException):
    """The caller isn't authorized to make the request."""

    code: str = "ForbiddenException"
    sender_fault: bool = True
    status_code: int = 403


class InternalServerErrorException(ServiceException):
    """The request failed due to an internal server error."""

    code: str = "InternalServerErrorException"
    sender_fault: bool = False
    status_code: int = 500


class NotFoundException(ServiceException):
    """The request was rejected because the specified resource could not be
    found.
    """

    code: str = "NotFoundException"
    sender_fault: bool = True
    status_code: int = 404


class TooManyRequestsException(ServiceException):
    """The limit on the number of requests per second was exceeded."""

    code: str = "TooManyRequestsException"
    sender_fault: bool = True
    status_code: int = 429


CreateNamespaceRequestNamespaceList = List[NamespaceName]


class CreateNamespaceRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: CreateNamespaceRequestNamespaceList


NamespaceList = List[NamespaceName]


class CreateNamespaceResponse(TypedDict, total=False):
    tableBucketARN: TableBucketARN
    namespace: NamespaceList


class EncryptionConfiguration(TypedDict, total=False):
    """Configuration specifying how data should be encrypted. This structure
    defines the encryption algorithm and optional KMS key to be used for
    server-side encryption.
    """

    sseAlgorithm: SSEAlgorithm
    kmsKeyArn: Optional[EncryptionConfigurationKmsKeyArnString]


class CreateTableBucketRequest(ServiceRequest):
    name: TableBucketName
    encryptionConfiguration: Optional[EncryptionConfiguration]


class CreateTableBucketResponse(TypedDict, total=False):
    arn: TableBucketARN


class SchemaField(TypedDict, total=False):
    name: String
    type: String
    required: Optional[Boolean]


SchemaFieldList = List[SchemaField]


class IcebergSchema(TypedDict, total=False):
    """Contains details about the schema for an Iceberg table."""

    fields: SchemaFieldList


class IcebergMetadata(TypedDict, total=False):
    """Contains details about the metadata for an Iceberg table."""

    schema: IcebergSchema


class TableMetadata(TypedDict, total=False):
    """Contains details about the table metadata."""

    iceberg: Optional[IcebergMetadata]


class CreateTableRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName
    format: OpenTableFormat
    metadata: Optional[TableMetadata]
    encryptionConfiguration: Optional[EncryptionConfiguration]


class CreateTableResponse(TypedDict, total=False):
    tableARN: TableARN
    versionToken: VersionToken


class DeleteNamespaceRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName


class DeleteTableBucketEncryptionRequest(ServiceRequest):
    tableBucketARN: TableBucketARN


class DeleteTableBucketPolicyRequest(ServiceRequest):
    tableBucketARN: TableBucketARN


class DeleteTableBucketRequest(ServiceRequest):
    tableBucketARN: TableBucketARN


class DeleteTablePolicyRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName


class DeleteTableRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName
    versionToken: Optional[VersionToken]


class GetNamespaceRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName


SyntheticTimestamp_date_time = datetime


class GetNamespaceResponse(TypedDict, total=False):
    namespace: NamespaceList
    createdAt: SyntheticTimestamp_date_time
    createdBy: AccountId
    ownerAccountId: AccountId
    namespaceId: Optional[NamespaceId]
    tableBucketId: Optional[TableBucketId]


class GetTableBucketEncryptionRequest(ServiceRequest):
    tableBucketARN: TableBucketARN


class GetTableBucketEncryptionResponse(TypedDict, total=False):
    encryptionConfiguration: EncryptionConfiguration


class GetTableBucketMaintenanceConfigurationRequest(ServiceRequest):
    tableBucketARN: TableBucketARN


class IcebergUnreferencedFileRemovalSettings(TypedDict, total=False):
    """Contains details about the unreferenced file removal settings for an
    Iceberg table bucket.
    """

    unreferencedDays: Optional[PositiveInteger]
    nonCurrentDays: Optional[PositiveInteger]


class TableBucketMaintenanceSettings(TypedDict, total=False):
    """Contains details about the maintenance settings for the table bucket."""

    icebergUnreferencedFileRemoval: Optional[IcebergUnreferencedFileRemovalSettings]


class TableBucketMaintenanceConfigurationValue(TypedDict, total=False):
    """Details about the values that define the maintenance configuration for a
    table bucket.
    """

    status: Optional[MaintenanceStatus]
    settings: Optional[TableBucketMaintenanceSettings]


TableBucketMaintenanceConfiguration = Dict[
    TableBucketMaintenanceType, TableBucketMaintenanceConfigurationValue
]


class GetTableBucketMaintenanceConfigurationResponse(TypedDict, total=False):
    tableBucketARN: TableBucketARN
    configuration: TableBucketMaintenanceConfiguration


class GetTableBucketPolicyRequest(ServiceRequest):
    tableBucketARN: TableBucketARN


class GetTableBucketPolicyResponse(TypedDict, total=False):
    resourcePolicy: ResourcePolicy


class GetTableBucketRequest(ServiceRequest):
    tableBucketARN: TableBucketARN


class GetTableBucketResponse(TypedDict, total=False):
    arn: TableBucketARN
    name: TableBucketName
    ownerAccountId: AccountId
    createdAt: SyntheticTimestamp_date_time
    tableBucketId: Optional[TableBucketId]
    type: Optional[TableBucketType]


class GetTableEncryptionRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName


class GetTableEncryptionResponse(TypedDict, total=False):
    encryptionConfiguration: EncryptionConfiguration


class GetTableMaintenanceConfigurationRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName


class IcebergSnapshotManagementSettings(TypedDict, total=False):
    """Contains details about the snapshot management settings for an Iceberg
    table. The oldest snapshot expires when its age exceeds the
    ``maxSnapshotAgeHours`` and the total number of snapshots exceeds the
    value for the minimum number of snapshots to keep
    ``minSnapshotsToKeep``.
    """

    minSnapshotsToKeep: Optional[PositiveInteger]
    maxSnapshotAgeHours: Optional[PositiveInteger]


class IcebergCompactionSettings(TypedDict, total=False):
    """Contains details about the compaction settings for an Iceberg table."""

    targetFileSizeMB: Optional[PositiveInteger]
    strategy: Optional[IcebergCompactionStrategy]


class TableMaintenanceSettings(TypedDict, total=False):
    """Contains details about maintenance settings for the table."""

    icebergCompaction: Optional[IcebergCompactionSettings]
    icebergSnapshotManagement: Optional[IcebergSnapshotManagementSettings]


class TableMaintenanceConfigurationValue(TypedDict, total=False):
    """Contains the values that define a maintenance configuration for a table."""

    status: Optional[MaintenanceStatus]
    settings: Optional[TableMaintenanceSettings]


TableMaintenanceConfiguration = Dict[TableMaintenanceType, TableMaintenanceConfigurationValue]


class GetTableMaintenanceConfigurationResponse(TypedDict, total=False):
    tableARN: TableARN
    configuration: TableMaintenanceConfiguration


class GetTableMaintenanceJobStatusRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName


class TableMaintenanceJobStatusValue(TypedDict, total=False):
    """Details about the status of a maintenance job."""

    status: JobStatus
    lastRunTimestamp: Optional[SyntheticTimestamp_date_time]
    failureMessage: Optional[String]


TableMaintenanceJobStatus = Dict[TableMaintenanceJobType, TableMaintenanceJobStatusValue]


class GetTableMaintenanceJobStatusResponse(TypedDict, total=False):
    tableARN: TableARN
    status: TableMaintenanceJobStatus


class GetTableMetadataLocationRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName


class GetTableMetadataLocationResponse(TypedDict, total=False):
    versionToken: VersionToken
    metadataLocation: Optional[MetadataLocation]
    warehouseLocation: WarehouseLocation


class GetTablePolicyRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName


class GetTablePolicyResponse(TypedDict, total=False):
    resourcePolicy: ResourcePolicy


class GetTableRequest(ServiceRequest):
    tableBucketARN: Optional[TableBucketARN]
    namespace: Optional[NamespaceName]
    name: Optional[TableName]
    tableArn: Optional[TableARN]


class GetTableResponse(TypedDict, total=False):
    name: TableName
    type: TableType
    tableARN: TableARN
    namespace: NamespaceList
    namespaceId: Optional[NamespaceId]
    versionToken: VersionToken
    metadataLocation: Optional[MetadataLocation]
    warehouseLocation: WarehouseLocation
    createdAt: SyntheticTimestamp_date_time
    createdBy: AccountId
    managedByService: Optional[String]
    modifiedAt: SyntheticTimestamp_date_time
    modifiedBy: AccountId
    ownerAccountId: AccountId
    format: OpenTableFormat
    tableBucketId: Optional[TableBucketId]


class ListNamespacesRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    prefix: Optional[ListNamespacesRequestPrefixString]
    continuationToken: Optional[NextToken]
    maxNamespaces: Optional[ListNamespacesLimit]


class NamespaceSummary(TypedDict, total=False):
    """Contains details about a namespace."""

    namespace: NamespaceList
    createdAt: SyntheticTimestamp_date_time
    createdBy: AccountId
    ownerAccountId: AccountId
    namespaceId: Optional[NamespaceId]
    tableBucketId: Optional[TableBucketId]


NamespaceSummaryList = List[NamespaceSummary]


class ListNamespacesResponse(TypedDict, total=False):
    namespaces: NamespaceSummaryList
    continuationToken: Optional[NextToken]


class ListTableBucketsRequest(TypedDict, total=False):
    prefix: Optional[ListTableBucketsRequestPrefixString]
    continuationToken: Optional[NextToken]
    maxBuckets: Optional[ListTableBucketsLimit]
    type: Optional[TableBucketType]


class TableBucketSummary(TypedDict, total=False):
    arn: TableBucketARN
    name: TableBucketName
    ownerAccountId: AccountId
    createdAt: SyntheticTimestamp_date_time
    tableBucketId: Optional[TableBucketId]
    type: Optional[TableBucketType]


TableBucketSummaryList = List[TableBucketSummary]


class ListTableBucketsResponse(TypedDict, total=False):
    tableBuckets: TableBucketSummaryList
    continuationToken: Optional[NextToken]


class ListTablesRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: Optional[NamespaceName]
    prefix: Optional[ListTablesRequestPrefixString]
    continuationToken: Optional[NextToken]
    maxTables: Optional[ListTablesLimit]


class TableSummary(TypedDict, total=False):
    namespace: NamespaceList
    name: TableName
    type: TableType
    tableARN: TableARN
    createdAt: SyntheticTimestamp_date_time
    modifiedAt: SyntheticTimestamp_date_time
    namespaceId: Optional[NamespaceId]
    tableBucketId: Optional[TableBucketId]


TableSummaryList = List[TableSummary]


class ListTablesResponse(TypedDict, total=False):
    tables: TableSummaryList
    continuationToken: Optional[NextToken]


class PutTableBucketEncryptionRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    encryptionConfiguration: EncryptionConfiguration


class PutTableBucketMaintenanceConfigurationRequest(TypedDict, total=False):
    tableBucketARN: TableBucketARN
    type: TableBucketMaintenanceType
    value: TableBucketMaintenanceConfigurationValue


class PutTableBucketPolicyRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    resourcePolicy: ResourcePolicy


class PutTableMaintenanceConfigurationRequest(TypedDict, total=False):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName
    type: TableMaintenanceType
    value: TableMaintenanceConfigurationValue


class PutTablePolicyRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName
    resourcePolicy: ResourcePolicy


class RenameTableRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName
    newNamespaceName: Optional[NamespaceName]
    newName: Optional[TableName]
    versionToken: Optional[VersionToken]


class UpdateTableMetadataLocationRequest(ServiceRequest):
    tableBucketARN: TableBucketARN
    namespace: NamespaceName
    name: TableName
    versionToken: VersionToken
    metadataLocation: MetadataLocation


class UpdateTableMetadataLocationResponse(TypedDict, total=False):
    name: TableName
    tableARN: TableARN
    namespace: NamespaceList
    versionToken: VersionToken
    metadataLocation: MetadataLocation


class S3TablesApi:
    service = "s3tables"
    version = "2018-05-10"

    @handler("CreateNamespace")
    def create_namespace(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: CreateNamespaceRequestNamespaceList,
        **kwargs,
    ) -> CreateNamespaceResponse:
        """Creates a namespace. A namespace is a logical grouping of tables within
        your table bucket, which you can use to organize tables. For more
        information, see `Create a
        namespace <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-create.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:CreateNamespace`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket to create the
        namespace in.
        :param namespace: A name for the namespace.
        :returns: CreateNamespaceResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("CreateTable")
    def create_table(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        format: OpenTableFormat,
        metadata: TableMetadata | None = None,
        encryption_configuration: EncryptionConfiguration | None = None,
        **kwargs,
    ) -> CreateTableResponse:
        """Creates a new table associated with the given namespace in a table
        bucket. For more information, see `Creating an Amazon S3
        table <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-create.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           -  You must have the ``s3tables:CreateTable`` permission to use this
              operation.

           -  If you use this operation with the optional ``metadata`` request
              parameter you must have the ``s3tables:PutTableData`` permission.

           -  If you use this operation with the optional
              ``encryptionConfiguration`` request parameter you must have the
              ``s3tables:PutTableEncryption`` permission.

           Additionally, If you choose SSE-KMS encryption you must grant the S3
           Tables maintenance principal access to your KMS key. For more
           information, see `Permissions requirements for S3 Tables SSE-KMS
           encryption <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html>`__.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket to create the table
        in.
        :param namespace: The namespace to associated with the table.
        :param name: The name for the table.
        :param format: The format for the table.
        :param metadata: The metadata for the table.
        :param encryption_configuration: The encryption configuration to use for the table.
        :returns: CreateTableResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("CreateTableBucket")
    def create_table_bucket(
        self,
        context: RequestContext,
        name: TableBucketName,
        encryption_configuration: EncryptionConfiguration | None = None,
        **kwargs,
    ) -> CreateTableBucketResponse:
        """Creates a table bucket. For more information, see `Creating a table
        bucket <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           -  You must have the ``s3tables:CreateTableBucket`` permission to use
              this operation.

           -  If you use this operation with the optional
              ``encryptionConfiguration`` parameter you must have the
              ``s3tables:PutTableBucketEncryption`` permission.

        :param name: The name for the table bucket.
        :param encryption_configuration: The encryption configuration to use for the table bucket.
        :returns: CreateTableBucketResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("DeleteNamespace")
    def delete_namespace(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        **kwargs,
    ) -> None:
        """Deletes a namespace. For more information, see `Delete a
        namespace <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-delete.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:DeleteNamespace`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket associated with the
        namespace.
        :param namespace: The name of the namespace.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("DeleteTable")
    def delete_table(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        version_token: VersionToken | None = None,
        **kwargs,
    ) -> None:
        """Deletes a table. For more information, see `Deleting an Amazon S3
        table <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-delete.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:DeleteTable`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket that contains the
        table.
        :param namespace: The namespace associated with the table.
        :param name: The name of the table.
        :param version_token: The version token of the table.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("DeleteTableBucket")
    def delete_table_bucket(
        self, context: RequestContext, table_bucket_arn: TableBucketARN, **kwargs
    ) -> None:
        """Deletes a table bucket. For more information, see `Deleting a table
        bucket <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-delete.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:DeleteTableBucket`` permission to use
           this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("DeleteTableBucketEncryption")
    def delete_table_bucket_encryption(
        self, context: RequestContext, table_bucket_arn: TableBucketARN, **kwargs
    ) -> None:
        """Deletes the encryption configuration for a table bucket.

        Permissions
           You must have the ``s3tables:DeleteTableBucketEncryption`` permission
           to use this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("DeleteTableBucketPolicy")
    def delete_table_bucket_policy(
        self, context: RequestContext, table_bucket_arn: TableBucketARN, **kwargs
    ) -> None:
        """Deletes a table bucket policy. For more information, see `Deleting a
        table bucket
        policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-delete>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:DeleteTableBucketPolicy`` permission to
           use this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("DeleteTablePolicy")
    def delete_table_policy(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        **kwargs,
    ) -> None:
        """Deletes a table policy. For more information, see `Deleting a table
        policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-table-policy.html#table-policy-delete>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:DeleteTablePolicy`` permission to use
           this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket that contains the
        table.
        :param namespace: The namespace associated with the table.
        :param name: The table name.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetNamespace")
    def get_namespace(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        **kwargs,
    ) -> GetNamespaceResponse:
        """Gets details about a namespace. For more information, see `Table
        namespaces <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:GetNamespace`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :param namespace: The name of the namespace.
        :returns: GetNamespaceResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetTable")
    def get_table(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN | None = None,
        namespace: NamespaceName | None = None,
        name: TableName | None = None,
        table_arn: TableARN | None = None,
        **kwargs,
    ) -> GetTableResponse:
        """Gets details about a table. For more information, see `S3
        Tables <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:GetTable`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket associated with the
        table.
        :param namespace: The name of the namespace the table is associated with.
        :param name: The name of the table.
        :param table_arn: The Amazon Resource Name (ARN) of the table.
        :returns: GetTableResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetTableBucket")
    def get_table_bucket(
        self, context: RequestContext, table_bucket_arn: TableBucketARN, **kwargs
    ) -> GetTableBucketResponse:
        """Gets details on a table bucket. For more information, see `Viewing
        details about an Amazon S3 table
        bucket <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-details.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:GetTableBucket`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :returns: GetTableBucketResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetTableBucketEncryption")
    def get_table_bucket_encryption(
        self, context: RequestContext, table_bucket_arn: TableBucketARN, **kwargs
    ) -> GetTableBucketEncryptionResponse:
        """Gets the encryption configuration for a table bucket.

        Permissions
           You must have the ``s3tables:GetTableBucketEncryption`` permission to
           use this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :returns: GetTableBucketEncryptionResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetTableBucketMaintenanceConfiguration")
    def get_table_bucket_maintenance_configuration(
        self, context: RequestContext, table_bucket_arn: TableBucketARN, **kwargs
    ) -> GetTableBucketMaintenanceConfigurationResponse:
        """Gets details about a maintenance configuration for a given table bucket.
        For more information, see `Amazon S3 table bucket
        maintenance <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:GetTableBucketMaintenanceConfiguration``
           permission to use this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket associated with the
        maintenance configuration.
        :returns: GetTableBucketMaintenanceConfigurationResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetTableBucketPolicy")
    def get_table_bucket_policy(
        self, context: RequestContext, table_bucket_arn: TableBucketARN, **kwargs
    ) -> GetTableBucketPolicyResponse:
        """Gets details about a table bucket policy. For more information, see
        `Viewing a table bucket
        policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-get>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:GetTableBucketPolicy`` permission to use
           this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :returns: GetTableBucketPolicyResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetTableEncryption")
    def get_table_encryption(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        **kwargs,
    ) -> GetTableEncryptionResponse:
        """Gets the encryption configuration for a table.

        Permissions
           You must have the ``s3tables:GetTableEncryption`` permission to use
           this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket containing the table.
        :param namespace: The namespace associated with the table.
        :param name: The name of the table.
        :returns: GetTableEncryptionResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetTableMaintenanceConfiguration")
    def get_table_maintenance_configuration(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        **kwargs,
    ) -> GetTableMaintenanceConfigurationResponse:
        """Gets details about the maintenance configuration of a table. For more
        information, see `S3 Tables
        maintenance <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           -  You must have the ``s3tables:GetTableMaintenanceConfiguration``
              permission to use this operation.

           -  You must have the ``s3tables:GetTableData`` permission to use set
              the compaction strategy to ``sort`` or ``zorder``.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :param namespace: The namespace associated with the table.
        :param name: The name of the table.
        :returns: GetTableMaintenanceConfigurationResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetTableMaintenanceJobStatus")
    def get_table_maintenance_job_status(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        **kwargs,
    ) -> GetTableMaintenanceJobStatusResponse:
        """Gets the status of a maintenance job for a table. For more information,
        see `S3 Tables
        maintenance <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:GetTableMaintenanceJobStatus``
           permission to use this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :param namespace: The name of the namespace the table is associated with.
        :param name: The name of the maintenance job.
        :returns: GetTableMaintenanceJobStatusResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetTableMetadataLocation")
    def get_table_metadata_location(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        **kwargs,
    ) -> GetTableMetadataLocationResponse:
        """Gets the location of the table metadata.

        Permissions
           You must have the ``s3tables:GetTableMetadataLocation`` permission to
           use this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :param namespace: The namespace of the table.
        :param name: The name of the table.
        :returns: GetTableMetadataLocationResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("GetTablePolicy")
    def get_table_policy(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        **kwargs,
    ) -> GetTablePolicyResponse:
        """Gets details about a table policy. For more information, see `Viewing a
        table
        policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-table-policy.html#table-policy-get>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:GetTablePolicy`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket that contains the
        table.
        :param namespace: The namespace associated with the table.
        :param name: The name of the table.
        :returns: GetTablePolicyResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("ListNamespaces")
    def list_namespaces(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        prefix: ListNamespacesRequestPrefixString | None = None,
        continuation_token: NextToken | None = None,
        max_namespaces: ListNamespacesLimit | None = None,
        **kwargs,
    ) -> ListNamespacesResponse:
        """Lists the namespaces within a table bucket. For more information, see
        `Table
        namespaces <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:ListNamespaces`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :param prefix: The prefix of the namespaces.
        :param continuation_token: ``ContinuationToken`` indicates to Amazon S3 that the list is being
        continued on this bucket with a token.
        :param max_namespaces: The maximum number of namespaces to return in the list.
        :returns: ListNamespacesResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("ListTableBuckets", expand=False)
    def list_table_buckets(
        self, context: RequestContext, request: ListTableBucketsRequest, **kwargs
    ) -> ListTableBucketsResponse:
        """Lists table buckets for your account. For more information, see `S3
        Table
        buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:ListTableBuckets`` permission to use
           this operation.

        :param prefix: The prefix of the table buckets.
        :param continuation_token: ``ContinuationToken`` indicates to Amazon S3 that the list is being
        continued on this bucket with a token.
        :param max_buckets: The maximum number of table buckets to return in the list.
        :param type: The type of table buckets to filter by in the list.
        :returns: ListTableBucketsResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("ListTables")
    def list_tables(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName | None = None,
        prefix: ListTablesRequestPrefixString | None = None,
        continuation_token: NextToken | None = None,
        max_tables: ListTablesLimit | None = None,
        **kwargs,
    ) -> ListTablesResponse:
        """List tables in the given table bucket. For more information, see `S3
        Tables <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:ListTables`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon resource Name (ARN) of the table bucket.
        :param namespace: The namespace of the tables.
        :param prefix: The prefix of the tables.
        :param continuation_token: ``ContinuationToken`` indicates to Amazon S3 that the list is being
        continued on this bucket with a token.
        :param max_tables: The maximum number of tables to return.
        :returns: ListTablesResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("PutTableBucketEncryption")
    def put_table_bucket_encryption(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        encryption_configuration: EncryptionConfiguration,
        **kwargs,
    ) -> None:
        """Sets the encryption configuration for a table bucket.

        Permissions
           You must have the ``s3tables:PutTableBucketEncryption`` permission to
           use this operation.

           If you choose SSE-KMS encryption you must grant the S3 Tables
           maintenance principal access to your KMS key. For more information,
           see `Permissions requirements for S3 Tables SSE-KMS
           encryption <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html>`__
           in the *Amazon Simple Storage Service User Guide*.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :param encryption_configuration: The encryption configuration to apply to the table bucket.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("PutTableBucketMaintenanceConfiguration", expand=False)
    def put_table_bucket_maintenance_configuration(
        self,
        context: RequestContext,
        request: PutTableBucketMaintenanceConfigurationRequest,
        **kwargs,
    ) -> None:
        """Creates a new maintenance configuration or replaces an existing
        maintenance configuration for a table bucket. For more information, see
        `Amazon S3 table bucket
        maintenance <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:PutTableBucketMaintenanceConfiguration``
           permission to use this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket associated with the
        maintenance configuration.
        :param type: The type of the maintenance configuration.
        :param value: Defines the values of the maintenance configuration for the table
        bucket.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("PutTableBucketPolicy")
    def put_table_bucket_policy(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        resource_policy: ResourcePolicy,
        **kwargs,
    ) -> None:
        """Creates a new maintenance configuration or replaces an existing table
        bucket policy for a table bucket. For more information, see `Adding a
        table bucket
        policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-add>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:PutTableBucketPolicy`` permission to use
           this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :param resource_policy: The ``JSON`` that defines the policy.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("PutTableMaintenanceConfiguration", expand=False)
    def put_table_maintenance_configuration(
        self, context: RequestContext, request: PutTableMaintenanceConfigurationRequest, **kwargs
    ) -> None:
        """Creates a new maintenance configuration or replaces an existing
        maintenance configuration for a table. For more information, see `S3
        Tables
        maintenance <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:PutTableMaintenanceConfiguration``
           permission to use this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table associated with the
        maintenance configuration.
        :param namespace: The namespace of the table.
        :param name: The name of the maintenance configuration.
        :param type: The type of the maintenance configuration.
        :param value: Defines the values of the maintenance configuration for the table.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("PutTablePolicy")
    def put_table_policy(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        resource_policy: ResourcePolicy,
        **kwargs,
    ) -> None:
        """Creates a new maintenance configuration or replaces an existing table
        policy for a table. For more information, see `Adding a table
        policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-table-policy.html#table-policy-add>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:PutTablePolicy`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket that contains the
        table.
        :param namespace: The namespace associated with the table.
        :param name: The name of the table.
        :param resource_policy: The ``JSON`` that defines the policy.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("RenameTable")
    def rename_table(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        new_namespace_name: NamespaceName | None = None,
        new_name: TableName | None = None,
        version_token: VersionToken | None = None,
        **kwargs,
    ) -> None:
        """Renames a table or a namespace. For more information, see `S3
        Tables <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html>`__
        in the *Amazon Simple Storage Service User Guide*.

        Permissions
           You must have the ``s3tables:RenameTable`` permission to use this
           operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :param namespace: The namespace associated with the table.
        :param name: The current name of the table.
        :param new_namespace_name: The new name for the namespace.
        :param new_name: The new name for the table.
        :param version_token: The version token of the table.
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("UpdateTableMetadataLocation")
    def update_table_metadata_location(
        self,
        context: RequestContext,
        table_bucket_arn: TableBucketARN,
        namespace: NamespaceName,
        name: TableName,
        version_token: VersionToken,
        metadata_location: MetadataLocation,
        **kwargs,
    ) -> UpdateTableMetadataLocationResponse:
        """Updates the metadata location for a table. The metadata location of a
        table must be an S3 URI that begins with the table's warehouse location.
        The metadata location for an Apache Iceberg table must end with
        ``.metadata.json``, or if the metadata file is Gzip-compressed,
        ``.metadata.json.gz``.

        Permissions
           You must have the ``s3tables:UpdateTableMetadataLocation`` permission
           to use this operation.

        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        :param namespace: The namespace of the table.
        :param name: The name of the table.
        :param version_token: The version token of the table.
        :param metadata_location: The new metadata location for the table.
        :returns: UpdateTableMetadataLocationResponse
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        :raises BadRequestException:
        """
        raise NotImplementedError
