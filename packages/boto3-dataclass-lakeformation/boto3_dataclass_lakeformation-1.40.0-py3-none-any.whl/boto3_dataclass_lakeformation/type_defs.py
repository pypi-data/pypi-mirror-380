# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lakeformation import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class AddObjectInput:
    boto3_raw_data: "type_defs.AddObjectInputTypeDef" = dataclasses.field()

    Uri = field("Uri")
    ETag = field("ETag")
    Size = field("Size")
    PartitionValues = field("PartitionValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddObjectInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddObjectInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeDecoratedRoleWithSAMLRequest:
    boto3_raw_data: "type_defs.AssumeDecoratedRoleWithSAMLRequestTypeDef" = (
        dataclasses.field()
    )

    SAMLAssertion = field("SAMLAssertion")
    RoleArn = field("RoleArn")
    PrincipalArn = field("PrincipalArn")
    DurationSeconds = field("DurationSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssumeDecoratedRoleWithSAMLRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeDecoratedRoleWithSAMLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditContext:
    boto3_raw_data: "type_defs.AuditContextTypeDef" = dataclasses.field()

    AdditionalAuditContext = field("AdditionalAuditContext")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuditContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuditContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetail:
    boto3_raw_data: "type_defs.ErrorDetailTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Condition:
    boto3_raw_data: "type_defs.ConditionTypeDef" = dataclasses.field()

    Expression = field("Expression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakePrincipal:
    boto3_raw_data: "type_defs.DataLakePrincipalTypeDef" = dataclasses.field()

    DataLakePrincipalIdentifier = field("DataLakePrincipalIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataLakePrincipalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakePrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelTransactionRequest:
    boto3_raw_data: "type_defs.CancelTransactionRequestTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelTransactionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelTransactionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CatalogResource:
    boto3_raw_data: "type_defs.CatalogResourceTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CatalogResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CatalogResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagPairOutput:
    boto3_raw_data: "type_defs.LFTagPairOutputTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    TagValues = field("TagValues")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LFTagPairOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LFTagPairOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnWildcardOutput:
    boto3_raw_data: "type_defs.ColumnWildcardOutputTypeDef" = dataclasses.field()

    ExcludedColumnNames = field("ExcludedColumnNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ColumnWildcardOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnWildcardOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnWildcard:
    boto3_raw_data: "type_defs.ColumnWildcardTypeDef" = dataclasses.field()

    ExcludedColumnNames = field("ExcludedColumnNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnWildcardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnWildcardTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommitTransactionRequest:
    boto3_raw_data: "type_defs.CommitTransactionRequestTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommitTransactionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommitTransactionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLFTagRequest:
    boto3_raw_data: "type_defs.CreateLFTagRequestTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    TagValues = field("TagValues")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLFTagRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLFTagRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RowFilterOutput:
    boto3_raw_data: "type_defs.RowFilterOutputTypeDef" = dataclasses.field()

    FilterExpression = field("FilterExpression")
    AllRowsWildcard = field("AllRowsWildcard")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowFilterOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataCellsFilterResource:
    boto3_raw_data: "type_defs.DataCellsFilterResourceTypeDef" = dataclasses.field()

    TableCatalogId = field("TableCatalogId")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataCellsFilterResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataCellsFilterResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RowFilter:
    boto3_raw_data: "type_defs.RowFilterTypeDef" = dataclasses.field()

    FilterExpression = field("FilterExpression")
    AllRowsWildcard = field("AllRowsWildcard")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLocationResource:
    boto3_raw_data: "type_defs.DataLocationResourceTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLocationResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLocationResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseResource:
    boto3_raw_data: "type_defs.DatabaseResourceTypeDef" = dataclasses.field()

    Name = field("Name")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatabaseResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataCellsFilterRequest:
    boto3_raw_data: "type_defs.DeleteDataCellsFilterRequestTypeDef" = (
        dataclasses.field()
    )

    TableCatalogId = field("TableCatalogId")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataCellsFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataCellsFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLFTagExpressionRequest:
    boto3_raw_data: "type_defs.DeleteLFTagExpressionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLFTagExpressionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLFTagExpressionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLFTagRequest:
    boto3_raw_data: "type_defs.DeleteLFTagRequestTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLFTagRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLFTagRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLakeFormationIdentityCenterConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DeleteLakeFormationIdentityCenterConfigurationRequestTypeDef"
    ) = dataclasses.field()

    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteLakeFormationIdentityCenterConfigurationRequestTypeDef"
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
                "type_defs.DeleteLakeFormationIdentityCenterConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectInput:
    boto3_raw_data: "type_defs.DeleteObjectInputTypeDef" = dataclasses.field()

    Uri = field("Uri")
    ETag = field("ETag")
    PartitionValues = field("PartitionValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteObjectInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualObject:
    boto3_raw_data: "type_defs.VirtualObjectTypeDef" = dataclasses.field()

    Uri = field("Uri")
    ETag = field("ETag")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VirtualObjectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterResourceRequest:
    boto3_raw_data: "type_defs.DeregisterResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLakeFormationIdentityCenterConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DescribeLakeFormationIdentityCenterConfigurationRequestTypeDef"
    ) = dataclasses.field()

    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLakeFormationIdentityCenterConfigurationRequestTypeDef"
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
                "type_defs.DescribeLakeFormationIdentityCenterConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalFilteringConfigurationOutput:
    boto3_raw_data: "type_defs.ExternalFilteringConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    AuthorizedTargets = field("AuthorizedTargets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExternalFilteringConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalFilteringConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceRequest:
    boto3_raw_data: "type_defs.DescribeResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceInfo:
    boto3_raw_data: "type_defs.ResourceInfoTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    RoleArn = field("RoleArn")
    LastModified = field("LastModified")
    WithFederation = field("WithFederation")
    HybridAccessEnabled = field("HybridAccessEnabled")
    WithPrivilegedAccess = field("WithPrivilegedAccess")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTransactionRequest:
    boto3_raw_data: "type_defs.DescribeTransactionRequestTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTransactionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTransactionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransactionDescription:
    boto3_raw_data: "type_defs.TransactionDescriptionTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")
    TransactionStatus = field("TransactionStatus")
    TransactionStartTime = field("TransactionStartTime")
    TransactionEndTime = field("TransactionEndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransactionDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransactionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetailsMap:
    boto3_raw_data: "type_defs.DetailsMapTypeDef" = dataclasses.field()

    ResourceShare = field("ResourceShare")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetailsMapTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetailsMapTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionStatistics:
    boto3_raw_data: "type_defs.ExecutionStatisticsTypeDef" = dataclasses.field()

    AverageExecutionTimeMillis = field("AverageExecutionTimeMillis")
    DataScannedBytes = field("DataScannedBytes")
    WorkUnitsExecutedCount = field("WorkUnitsExecutedCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutionStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtendTransactionRequest:
    boto3_raw_data: "type_defs.ExtendTransactionRequestTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtendTransactionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtendTransactionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalFilteringConfiguration:
    boto3_raw_data: "type_defs.ExternalFilteringConfigurationTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    AuthorizedTargets = field("AuthorizedTargets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExternalFilteringConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalFilteringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCondition:
    boto3_raw_data: "type_defs.FilterConditionTypeDef" = dataclasses.field()

    Field = field("Field")
    ComparisonOperator = field("ComparisonOperator")
    StringValueList = field("StringValueList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataCellsFilterRequest:
    boto3_raw_data: "type_defs.GetDataCellsFilterRequestTypeDef" = dataclasses.field()

    TableCatalogId = field("TableCatalogId")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataCellsFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataCellsFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeSettingsRequest:
    boto3_raw_data: "type_defs.GetDataLakeSettingsRequestTypeDef" = dataclasses.field()

    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataLakeSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEffectivePermissionsForPathRequest:
    boto3_raw_data: "type_defs.GetEffectivePermissionsForPathRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    CatalogId = field("CatalogId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEffectivePermissionsForPathRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEffectivePermissionsForPathRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLFTagExpressionRequest:
    boto3_raw_data: "type_defs.GetLFTagExpressionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLFTagExpressionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLFTagExpressionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagOutput:
    boto3_raw_data: "type_defs.LFTagOutputTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    TagValues = field("TagValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LFTagOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LFTagOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLFTagRequest:
    boto3_raw_data: "type_defs.GetLFTagRequestTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLFTagRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetLFTagRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStateRequest:
    boto3_raw_data: "type_defs.GetQueryStateRequestTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStatisticsRequest:
    boto3_raw_data: "type_defs.GetQueryStatisticsRequestTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryStatisticsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlanningStatistics:
    boto3_raw_data: "type_defs.PlanningStatisticsTypeDef" = dataclasses.field()

    EstimatedDataToScanBytes = field("EstimatedDataToScanBytes")
    PlanningTimeMillis = field("PlanningTimeMillis")
    QueueTimeMillis = field("QueueTimeMillis")
    WorkUnitsGeneratedCount = field("WorkUnitsGeneratedCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlanningStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlanningStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartitionValueList:
    boto3_raw_data: "type_defs.PartitionValueListTypeDef" = dataclasses.field()

    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PartitionValueListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartitionValueListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkUnitResultsRequest:
    boto3_raw_data: "type_defs.GetWorkUnitResultsRequestTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    WorkUnitId = field("WorkUnitId")
    WorkUnitToken = field("WorkUnitToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkUnitResultsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkUnitResultsRequestTypeDef"]
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
class GetWorkUnitsRequest:
    boto3_raw_data: "type_defs.GetWorkUnitsRequestTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkUnitsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkUnitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkUnitRange:
    boto3_raw_data: "type_defs.WorkUnitRangeTypeDef" = dataclasses.field()

    WorkUnitIdMax = field("WorkUnitIdMax")
    WorkUnitIdMin = field("WorkUnitIdMin")
    WorkUnitToken = field("WorkUnitToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkUnitRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkUnitRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagExpressionResource:
    boto3_raw_data: "type_defs.LFTagExpressionResourceTypeDef" = dataclasses.field()

    Name = field("Name")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LFTagExpressionResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LFTagExpressionResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagKeyResourceOutput:
    boto3_raw_data: "type_defs.LFTagKeyResourceOutputTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    TagValues = field("TagValues")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LFTagKeyResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LFTagKeyResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagKeyResource:
    boto3_raw_data: "type_defs.LFTagKeyResourceTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    TagValues = field("TagValues")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LFTagKeyResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LFTagKeyResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagPair:
    boto3_raw_data: "type_defs.LFTagPairTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    TagValues = field("TagValues")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LFTagPairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LFTagPairTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTag:
    boto3_raw_data: "type_defs.LFTagTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    TagValues = field("TagValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LFTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LFTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLFTagExpressionsRequest:
    boto3_raw_data: "type_defs.ListLFTagExpressionsRequestTypeDef" = dataclasses.field()

    CatalogId = field("CatalogId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLFTagExpressionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLFTagExpressionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLFTagsRequest:
    boto3_raw_data: "type_defs.ListLFTagsRequestTypeDef" = dataclasses.field()

    CatalogId = field("CatalogId")
    ResourceShareType = field("ResourceShareType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListLFTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLFTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableStorageOptimizersRequest:
    boto3_raw_data: "type_defs.ListTableStorageOptimizersRequestTypeDef" = (
        dataclasses.field()
    )

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    CatalogId = field("CatalogId")
    StorageOptimizerType = field("StorageOptimizerType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTableStorageOptimizersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableStorageOptimizersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageOptimizer:
    boto3_raw_data: "type_defs.StorageOptimizerTypeDef" = dataclasses.field()

    StorageOptimizerType = field("StorageOptimizerType")
    Config = field("Config")
    ErrorMessage = field("ErrorMessage")
    Warnings = field("Warnings")
    LastRunDetails = field("LastRunDetails")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageOptimizerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageOptimizerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransactionsRequest:
    boto3_raw_data: "type_defs.ListTransactionsRequestTypeDef" = dataclasses.field()

    CatalogId = field("CatalogId")
    StatusFilter = field("StatusFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTransactionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransactionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableObject:
    boto3_raw_data: "type_defs.TableObjectTypeDef" = dataclasses.field()

    Uri = field("Uri")
    ETag = field("ETag")
    Size = field("Size")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterResourceRequest:
    boto3_raw_data: "type_defs.RegisterResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    UseServiceLinkedRole = field("UseServiceLinkedRole")
    RoleArn = field("RoleArn")
    WithFederation = field("WithFederation")
    HybridAccessEnabled = field("HybridAccessEnabled")
    WithPrivilegedAccess = field("WithPrivilegedAccess")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableResourceOutput:
    boto3_raw_data: "type_defs.TableResourceOutputTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    CatalogId = field("CatalogId")
    Name = field("Name")
    TableWildcard = field("TableWildcard")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTransactionRequest:
    boto3_raw_data: "type_defs.StartTransactionRequestTypeDef" = dataclasses.field()

    TransactionType = field("TransactionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTransactionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTransactionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableResource:
    boto3_raw_data: "type_defs.TableResourceTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    CatalogId = field("CatalogId")
    Name = field("Name")
    TableWildcard = field("TableWildcard")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLFTagRequest:
    boto3_raw_data: "type_defs.UpdateLFTagRequestTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    CatalogId = field("CatalogId")
    TagValuesToDelete = field("TagValuesToDelete")
    TagValuesToAdd = field("TagValuesToAdd")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLFTagRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLFTagRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceRequest:
    boto3_raw_data: "type_defs.UpdateResourceRequestTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    ResourceArn = field("ResourceArn")
    WithFederation = field("WithFederation")
    HybridAccessEnabled = field("HybridAccessEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTableStorageOptimizerRequest:
    boto3_raw_data: "type_defs.UpdateTableStorageOptimizerRequestTypeDef" = (
        dataclasses.field()
    )

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    StorageOptimizerConfig = field("StorageOptimizerConfig")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTableStorageOptimizerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableStorageOptimizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeDecoratedRoleWithSAMLResponse:
    boto3_raw_data: "type_defs.AssumeDecoratedRoleWithSAMLResponseTypeDef" = (
        dataclasses.field()
    )

    AccessKeyId = field("AccessKeyId")
    SecretAccessKey = field("SecretAccessKey")
    SessionToken = field("SessionToken")
    Expiration = field("Expiration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssumeDecoratedRoleWithSAMLResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeDecoratedRoleWithSAMLResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommitTransactionResponse:
    boto3_raw_data: "type_defs.CommitTransactionResponseTypeDef" = dataclasses.field()

    TransactionStatus = field("TransactionStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommitTransactionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommitTransactionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLakeFormationIdentityCenterConfigurationResponse:
    boto3_raw_data: (
        "type_defs.CreateLakeFormationIdentityCenterConfigurationResponseTypeDef"
    ) = dataclasses.field()

    ApplicationArn = field("ApplicationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLakeFormationIdentityCenterConfigurationResponseTypeDef"
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
                "type_defs.CreateLakeFormationIdentityCenterConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakePrincipalResponse:
    boto3_raw_data: "type_defs.GetDataLakePrincipalResponseTypeDef" = (
        dataclasses.field()
    )

    Identity = field("Identity")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataLakePrincipalResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakePrincipalResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLFTagResponse:
    boto3_raw_data: "type_defs.GetLFTagResponseTypeDef" = dataclasses.field()

    CatalogId = field("CatalogId")
    TagKey = field("TagKey")
    TagValues = field("TagValues")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLFTagResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLFTagResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStateResponse:
    boto3_raw_data: "type_defs.GetQueryStateResponseTypeDef" = dataclasses.field()

    Error = field("Error")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryStateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemporaryGluePartitionCredentialsResponse:
    boto3_raw_data: "type_defs.GetTemporaryGluePartitionCredentialsResponseTypeDef" = (
        dataclasses.field()
    )

    AccessKeyId = field("AccessKeyId")
    SecretAccessKey = field("SecretAccessKey")
    SessionToken = field("SessionToken")
    Expiration = field("Expiration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTemporaryGluePartitionCredentialsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemporaryGluePartitionCredentialsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemporaryGlueTableCredentialsResponse:
    boto3_raw_data: "type_defs.GetTemporaryGlueTableCredentialsResponseTypeDef" = (
        dataclasses.field()
    )

    AccessKeyId = field("AccessKeyId")
    SecretAccessKey = field("SecretAccessKey")
    SessionToken = field("SessionToken")
    Expiration = field("Expiration")
    VendedS3Path = field("VendedS3Path")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTemporaryGlueTableCredentialsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemporaryGlueTableCredentialsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkUnitResultsResponse:
    boto3_raw_data: "type_defs.GetWorkUnitResultsResponseTypeDef" = dataclasses.field()

    ResultStream = field("ResultStream")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkUnitResultsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkUnitResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryPlanningResponse:
    boto3_raw_data: "type_defs.StartQueryPlanningResponseTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartQueryPlanningResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryPlanningResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTransactionResponse:
    boto3_raw_data: "type_defs.StartTransactionResponseTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTransactionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTransactionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTableStorageOptimizerResponse:
    boto3_raw_data: "type_defs.UpdateTableStorageOptimizerResponseTypeDef" = (
        dataclasses.field()
    )

    Result = field("Result")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTableStorageOptimizerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableStorageOptimizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrincipalPermissionsOutput:
    boto3_raw_data: "type_defs.PrincipalPermissionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    Permissions = field("Permissions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrincipalPermissionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrincipalPermissionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrincipalPermissions:
    boto3_raw_data: "type_defs.PrincipalPermissionsTypeDef" = dataclasses.field()

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    Permissions = field("Permissions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrincipalPermissionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrincipalPermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnLFTag:
    boto3_raw_data: "type_defs.ColumnLFTagTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def LFTags(self):  # pragma: no cover
        return LFTagPairOutput.make_many(self.boto3_raw_data["LFTags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnLFTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnLFTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagError:
    boto3_raw_data: "type_defs.LFTagErrorTypeDef" = dataclasses.field()

    @cached_property
    def LFTag(self):  # pragma: no cover
        return LFTagPairOutput.make_one(self.boto3_raw_data["LFTag"])

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LFTagErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LFTagErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLFTagsResponse:
    boto3_raw_data: "type_defs.ListLFTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def LFTags(self):  # pragma: no cover
        return LFTagPairOutput.make_many(self.boto3_raw_data["LFTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLFTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLFTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableWithColumnsResourceOutput:
    boto3_raw_data: "type_defs.TableWithColumnsResourceOutputTypeDef" = (
        dataclasses.field()
    )

    DatabaseName = field("DatabaseName")
    Name = field("Name")
    CatalogId = field("CatalogId")
    ColumnNames = field("ColumnNames")

    @cached_property
    def ColumnWildcard(self):  # pragma: no cover
        return ColumnWildcardOutput.make_one(self.boto3_raw_data["ColumnWildcard"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TableWithColumnsResourceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableWithColumnsResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataCellsFilterOutput:
    boto3_raw_data: "type_defs.DataCellsFilterOutputTypeDef" = dataclasses.field()

    TableCatalogId = field("TableCatalogId")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    Name = field("Name")

    @cached_property
    def RowFilter(self):  # pragma: no cover
        return RowFilterOutput.make_one(self.boto3_raw_data["RowFilter"])

    ColumnNames = field("ColumnNames")

    @cached_property
    def ColumnWildcard(self):  # pragma: no cover
        return ColumnWildcardOutput.make_one(self.boto3_raw_data["ColumnWildcard"])

    VersionId = field("VersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataCellsFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataCellsFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataCellsFilter:
    boto3_raw_data: "type_defs.DataCellsFilterTypeDef" = dataclasses.field()

    TableCatalogId = field("TableCatalogId")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    Name = field("Name")

    @cached_property
    def RowFilter(self):  # pragma: no cover
        return RowFilter.make_one(self.boto3_raw_data["RowFilter"])

    ColumnNames = field("ColumnNames")

    @cached_property
    def ColumnWildcard(self):  # pragma: no cover
        return ColumnWildcard.make_one(self.boto3_raw_data["ColumnWildcard"])

    VersionId = field("VersionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataCellsFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataCellsFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaggedDatabase:
    boto3_raw_data: "type_defs.TaggedDatabaseTypeDef" = dataclasses.field()

    @cached_property
    def Database(self):  # pragma: no cover
        return DatabaseResource.make_one(self.boto3_raw_data["Database"])

    @cached_property
    def LFTags(self):  # pragma: no cover
        return LFTagPairOutput.make_many(self.boto3_raw_data["LFTags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaggedDatabaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaggedDatabaseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteOperation:
    boto3_raw_data: "type_defs.WriteOperationTypeDef" = dataclasses.field()

    @cached_property
    def AddObject(self):  # pragma: no cover
        return AddObjectInput.make_one(self.boto3_raw_data["AddObject"])

    @cached_property
    def DeleteObject(self):  # pragma: no cover
        return DeleteObjectInput.make_one(self.boto3_raw_data["DeleteObject"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WriteOperationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WriteOperationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectsOnCancelRequest:
    boto3_raw_data: "type_defs.DeleteObjectsOnCancelRequestTypeDef" = (
        dataclasses.field()
    )

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    TransactionId = field("TransactionId")

    @cached_property
    def Objects(self):  # pragma: no cover
        return VirtualObject.make_many(self.boto3_raw_data["Objects"])

    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteObjectsOnCancelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectsOnCancelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLakeFormationIdentityCenterConfigurationResponse:
    boto3_raw_data: (
        "type_defs.DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef"
    ) = dataclasses.field()

    CatalogId = field("CatalogId")
    InstanceArn = field("InstanceArn")
    ApplicationArn = field("ApplicationArn")

    @cached_property
    def ExternalFiltering(self):  # pragma: no cover
        return ExternalFilteringConfigurationOutput.make_one(
            self.boto3_raw_data["ExternalFiltering"]
        )

    @cached_property
    def ShareRecipients(self):  # pragma: no cover
        return DataLakePrincipal.make_many(self.boto3_raw_data["ShareRecipients"])

    ResourceShare = field("ResourceShare")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef"
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
                "type_defs.DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceResponse:
    boto3_raw_data: "type_defs.DescribeResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceInfo(self):  # pragma: no cover
        return ResourceInfo.make_one(self.boto3_raw_data["ResourceInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesResponse:
    boto3_raw_data: "type_defs.ListResourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceInfoList(self):  # pragma: no cover
        return ResourceInfo.make_many(self.boto3_raw_data["ResourceInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTransactionResponse:
    boto3_raw_data: "type_defs.DescribeTransactionResponseTypeDef" = dataclasses.field()

    @cached_property
    def TransactionDescription(self):  # pragma: no cover
        return TransactionDescription.make_one(
            self.boto3_raw_data["TransactionDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTransactionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTransactionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransactionsResponse:
    boto3_raw_data: "type_defs.ListTransactionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Transactions(self):  # pragma: no cover
        return TransactionDescription.make_many(self.boto3_raw_data["Transactions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTransactionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransactionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesRequest:
    boto3_raw_data: "type_defs.ListResourcesRequestTypeDef" = dataclasses.field()

    @cached_property
    def FilterConditionList(self):  # pragma: no cover
        return FilterCondition.make_many(self.boto3_raw_data["FilterConditionList"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLFTagExpressionResponse:
    boto3_raw_data: "type_defs.GetLFTagExpressionResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    CatalogId = field("CatalogId")

    @cached_property
    def Expression(self):  # pragma: no cover
        return LFTagOutput.make_many(self.boto3_raw_data["Expression"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLFTagExpressionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLFTagExpressionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagExpression:
    boto3_raw_data: "type_defs.LFTagExpressionTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    CatalogId = field("CatalogId")

    @cached_property
    def Expression(self):  # pragma: no cover
        return LFTagOutput.make_many(self.boto3_raw_data["Expression"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LFTagExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LFTagExpressionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagPolicyResourceOutput:
    boto3_raw_data: "type_defs.LFTagPolicyResourceOutputTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    CatalogId = field("CatalogId")

    @cached_property
    def Expression(self):  # pragma: no cover
        return LFTagOutput.make_many(self.boto3_raw_data["Expression"])

    ExpressionName = field("ExpressionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LFTagPolicyResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LFTagPolicyResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStatisticsResponse:
    boto3_raw_data: "type_defs.GetQueryStatisticsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ExecutionStatistics(self):  # pragma: no cover
        return ExecutionStatistics.make_one(self.boto3_raw_data["ExecutionStatistics"])

    @cached_property
    def PlanningStatistics(self):  # pragma: no cover
        return PlanningStatistics.make_one(self.boto3_raw_data["PlanningStatistics"])

    QuerySubmissionTime = field("QuerySubmissionTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryStatisticsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableObjectsRequest:
    boto3_raw_data: "type_defs.GetTableObjectsRequestTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    CatalogId = field("CatalogId")
    TransactionId = field("TransactionId")
    QueryAsOfTime = field("QueryAsOfTime")
    PartitionPredicate = field("PartitionPredicate")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableObjectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableObjectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryPlanningContext:
    boto3_raw_data: "type_defs.QueryPlanningContextTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    CatalogId = field("CatalogId")
    QueryAsOfTime = field("QueryAsOfTime")
    QueryParameters = field("QueryParameters")
    TransactionId = field("TransactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryPlanningContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryPlanningContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuerySessionContext:
    boto3_raw_data: "type_defs.QuerySessionContextTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    QueryStartTime = field("QueryStartTime")
    ClusterId = field("ClusterId")
    QueryAuthorizationId = field("QueryAuthorizationId")
    AdditionalContext = field("AdditionalContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuerySessionContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuerySessionContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemporaryGluePartitionCredentialsRequest:
    boto3_raw_data: "type_defs.GetTemporaryGluePartitionCredentialsRequestTypeDef" = (
        dataclasses.field()
    )

    TableArn = field("TableArn")

    @cached_property
    def Partition(self):  # pragma: no cover
        return PartitionValueList.make_one(self.boto3_raw_data["Partition"])

    Permissions = field("Permissions")
    DurationSeconds = field("DurationSeconds")

    @cached_property
    def AuditContext(self):  # pragma: no cover
        return AuditContext.make_one(self.boto3_raw_data["AuditContext"])

    SupportedPermissionTypes = field("SupportedPermissionTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTemporaryGluePartitionCredentialsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemporaryGluePartitionCredentialsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkUnitsRequestPaginate:
    boto3_raw_data: "type_defs.GetWorkUnitsRequestPaginateTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkUnitsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkUnitsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLFTagExpressionsRequestPaginate:
    boto3_raw_data: "type_defs.ListLFTagExpressionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CatalogId = field("CatalogId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLFTagExpressionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLFTagExpressionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLFTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListLFTagsRequestPaginateTypeDef" = dataclasses.field()

    CatalogId = field("CatalogId")
    ResourceShareType = field("ResourceShareType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLFTagsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLFTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkUnitsResponse:
    boto3_raw_data: "type_defs.GetWorkUnitsResponseTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @cached_property
    def WorkUnitRanges(self):  # pragma: no cover
        return WorkUnitRange.make_many(self.boto3_raw_data["WorkUnitRanges"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkUnitsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkUnitsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableStorageOptimizersResponse:
    boto3_raw_data: "type_defs.ListTableStorageOptimizersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StorageOptimizerList(self):  # pragma: no cover
        return StorageOptimizer.make_many(self.boto3_raw_data["StorageOptimizerList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTableStorageOptimizersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableStorageOptimizersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartitionObjects:
    boto3_raw_data: "type_defs.PartitionObjectsTypeDef" = dataclasses.field()

    PartitionValues = field("PartitionValues")

    @cached_property
    def Objects(self):  # pragma: no cover
        return TableObject.make_many(self.boto3_raw_data["Objects"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartitionObjectsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartitionObjectsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeSettingsOutput:
    boto3_raw_data: "type_defs.DataLakeSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def DataLakeAdmins(self):  # pragma: no cover
        return DataLakePrincipal.make_many(self.boto3_raw_data["DataLakeAdmins"])

    @cached_property
    def ReadOnlyAdmins(self):  # pragma: no cover
        return DataLakePrincipal.make_many(self.boto3_raw_data["ReadOnlyAdmins"])

    @cached_property
    def CreateDatabaseDefaultPermissions(self):  # pragma: no cover
        return PrincipalPermissionsOutput.make_many(
            self.boto3_raw_data["CreateDatabaseDefaultPermissions"]
        )

    @cached_property
    def CreateTableDefaultPermissions(self):  # pragma: no cover
        return PrincipalPermissionsOutput.make_many(
            self.boto3_raw_data["CreateTableDefaultPermissions"]
        )

    Parameters = field("Parameters")
    TrustedResourceOwners = field("TrustedResourceOwners")
    AllowExternalDataFiltering = field("AllowExternalDataFiltering")
    AllowFullTableExternalDataAccess = field("AllowFullTableExternalDataAccess")

    @cached_property
    def ExternalDataFilteringAllowList(self):  # pragma: no cover
        return DataLakePrincipal.make_many(
            self.boto3_raw_data["ExternalDataFilteringAllowList"]
        )

    AuthorizedSessionTagValueList = field("AuthorizedSessionTagValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeSettings:
    boto3_raw_data: "type_defs.DataLakeSettingsTypeDef" = dataclasses.field()

    @cached_property
    def DataLakeAdmins(self):  # pragma: no cover
        return DataLakePrincipal.make_many(self.boto3_raw_data["DataLakeAdmins"])

    @cached_property
    def ReadOnlyAdmins(self):  # pragma: no cover
        return DataLakePrincipal.make_many(self.boto3_raw_data["ReadOnlyAdmins"])

    @cached_property
    def CreateDatabaseDefaultPermissions(self):  # pragma: no cover
        return PrincipalPermissions.make_many(
            self.boto3_raw_data["CreateDatabaseDefaultPermissions"]
        )

    @cached_property
    def CreateTableDefaultPermissions(self):  # pragma: no cover
        return PrincipalPermissions.make_many(
            self.boto3_raw_data["CreateTableDefaultPermissions"]
        )

    Parameters = field("Parameters")
    TrustedResourceOwners = field("TrustedResourceOwners")
    AllowExternalDataFiltering = field("AllowExternalDataFiltering")
    AllowFullTableExternalDataAccess = field("AllowFullTableExternalDataAccess")

    @cached_property
    def ExternalDataFilteringAllowList(self):  # pragma: no cover
        return DataLakePrincipal.make_many(
            self.boto3_raw_data["ExternalDataFilteringAllowList"]
        )

    AuthorizedSessionTagValueList = field("AuthorizedSessionTagValueList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataLakeSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceLFTagsResponse:
    boto3_raw_data: "type_defs.GetResourceLFTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def LFTagOnDatabase(self):  # pragma: no cover
        return LFTagPairOutput.make_many(self.boto3_raw_data["LFTagOnDatabase"])

    @cached_property
    def LFTagsOnTable(self):  # pragma: no cover
        return LFTagPairOutput.make_many(self.boto3_raw_data["LFTagsOnTable"])

    @cached_property
    def LFTagsOnColumns(self):  # pragma: no cover
        return ColumnLFTag.make_many(self.boto3_raw_data["LFTagsOnColumns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceLFTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceLFTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaggedTable:
    boto3_raw_data: "type_defs.TaggedTableTypeDef" = dataclasses.field()

    @cached_property
    def Table(self):  # pragma: no cover
        return TableResourceOutput.make_one(self.boto3_raw_data["Table"])

    @cached_property
    def LFTagOnDatabase(self):  # pragma: no cover
        return LFTagPairOutput.make_many(self.boto3_raw_data["LFTagOnDatabase"])

    @cached_property
    def LFTagsOnTable(self):  # pragma: no cover
        return LFTagPairOutput.make_many(self.boto3_raw_data["LFTagsOnTable"])

    @cached_property
    def LFTagsOnColumns(self):  # pragma: no cover
        return ColumnLFTag.make_many(self.boto3_raw_data["LFTagsOnColumns"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaggedTableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaggedTableTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddLFTagsToResourceResponse:
    boto3_raw_data: "type_defs.AddLFTagsToResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Failures(self):  # pragma: no cover
        return LFTagError.make_many(self.boto3_raw_data["Failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddLFTagsToResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddLFTagsToResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveLFTagsFromResourceResponse:
    boto3_raw_data: "type_defs.RemoveLFTagsFromResourceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Failures(self):  # pragma: no cover
        return LFTagError.make_many(self.boto3_raw_data["Failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveLFTagsFromResourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveLFTagsFromResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableWithColumnsResource:
    boto3_raw_data: "type_defs.TableWithColumnsResourceTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    Name = field("Name")
    CatalogId = field("CatalogId")
    ColumnNames = field("ColumnNames")
    ColumnWildcard = field("ColumnWildcard")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableWithColumnsResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableWithColumnsResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataCellsFilterResponse:
    boto3_raw_data: "type_defs.GetDataCellsFilterResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataCellsFilter(self):  # pragma: no cover
        return DataCellsFilterOutput.make_one(self.boto3_raw_data["DataCellsFilter"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataCellsFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataCellsFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataCellsFilterResponse:
    boto3_raw_data: "type_defs.ListDataCellsFilterResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataCellsFilters(self):  # pragma: no cover
        return DataCellsFilterOutput.make_many(self.boto3_raw_data["DataCellsFilters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataCellsFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataCellsFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchDatabasesByLFTagsResponse:
    boto3_raw_data: "type_defs.SearchDatabasesByLFTagsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DatabaseList(self):  # pragma: no cover
        return TaggedDatabase.make_many(self.boto3_raw_data["DatabaseList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchDatabasesByLFTagsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchDatabasesByLFTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTableObjectsRequest:
    boto3_raw_data: "type_defs.UpdateTableObjectsRequestTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")

    @cached_property
    def WriteOperations(self):  # pragma: no cover
        return WriteOperation.make_many(self.boto3_raw_data["WriteOperations"])

    CatalogId = field("CatalogId")
    TransactionId = field("TransactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTableObjectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableObjectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLakeFormationIdentityCenterConfigurationRequest:
    boto3_raw_data: (
        "type_defs.CreateLakeFormationIdentityCenterConfigurationRequestTypeDef"
    ) = dataclasses.field()

    CatalogId = field("CatalogId")
    InstanceArn = field("InstanceArn")
    ExternalFiltering = field("ExternalFiltering")

    @cached_property
    def ShareRecipients(self):  # pragma: no cover
        return DataLakePrincipal.make_many(self.boto3_raw_data["ShareRecipients"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLakeFormationIdentityCenterConfigurationRequestTypeDef"
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
                "type_defs.CreateLakeFormationIdentityCenterConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLakeFormationIdentityCenterConfigurationRequest:
    boto3_raw_data: (
        "type_defs.UpdateLakeFormationIdentityCenterConfigurationRequestTypeDef"
    ) = dataclasses.field()

    CatalogId = field("CatalogId")

    @cached_property
    def ShareRecipients(self):  # pragma: no cover
        return DataLakePrincipal.make_many(self.boto3_raw_data["ShareRecipients"])

    ApplicationStatus = field("ApplicationStatus")
    ExternalFiltering = field("ExternalFiltering")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLakeFormationIdentityCenterConfigurationRequestTypeDef"
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
                "type_defs.UpdateLakeFormationIdentityCenterConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLFTagExpressionsResponse:
    boto3_raw_data: "type_defs.ListLFTagExpressionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LFTagExpressions(self):  # pragma: no cover
        return LFTagExpression.make_many(self.boto3_raw_data["LFTagExpressions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLFTagExpressionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLFTagExpressionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceOutput:
    boto3_raw_data: "type_defs.ResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def Catalog(self):  # pragma: no cover
        return CatalogResource.make_one(self.boto3_raw_data["Catalog"])

    @cached_property
    def Database(self):  # pragma: no cover
        return DatabaseResource.make_one(self.boto3_raw_data["Database"])

    @cached_property
    def Table(self):  # pragma: no cover
        return TableResourceOutput.make_one(self.boto3_raw_data["Table"])

    @cached_property
    def TableWithColumns(self):  # pragma: no cover
        return TableWithColumnsResourceOutput.make_one(
            self.boto3_raw_data["TableWithColumns"]
        )

    @cached_property
    def DataLocation(self):  # pragma: no cover
        return DataLocationResource.make_one(self.boto3_raw_data["DataLocation"])

    @cached_property
    def DataCellsFilter(self):  # pragma: no cover
        return DataCellsFilterResource.make_one(self.boto3_raw_data["DataCellsFilter"])

    @cached_property
    def LFTag(self):  # pragma: no cover
        return LFTagKeyResourceOutput.make_one(self.boto3_raw_data["LFTag"])

    @cached_property
    def LFTagPolicy(self):  # pragma: no cover
        return LFTagPolicyResourceOutput.make_one(self.boto3_raw_data["LFTagPolicy"])

    @cached_property
    def LFTagExpression(self):  # pragma: no cover
        return LFTagExpressionResource.make_one(self.boto3_raw_data["LFTagExpression"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryPlanningRequest:
    boto3_raw_data: "type_defs.StartQueryPlanningRequestTypeDef" = dataclasses.field()

    @cached_property
    def QueryPlanningContext(self):  # pragma: no cover
        return QueryPlanningContext.make_one(
            self.boto3_raw_data["QueryPlanningContext"]
        )

    QueryString = field("QueryString")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartQueryPlanningRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryPlanningRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemporaryGlueTableCredentialsRequest:
    boto3_raw_data: "type_defs.GetTemporaryGlueTableCredentialsRequestTypeDef" = (
        dataclasses.field()
    )

    TableArn = field("TableArn")
    Permissions = field("Permissions")
    DurationSeconds = field("DurationSeconds")

    @cached_property
    def AuditContext(self):  # pragma: no cover
        return AuditContext.make_one(self.boto3_raw_data["AuditContext"])

    SupportedPermissionTypes = field("SupportedPermissionTypes")
    S3Path = field("S3Path")

    @cached_property
    def QuerySessionContext(self):  # pragma: no cover
        return QuerySessionContext.make_one(self.boto3_raw_data["QuerySessionContext"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTemporaryGlueTableCredentialsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemporaryGlueTableCredentialsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLFTagExpressionRequest:
    boto3_raw_data: "type_defs.CreateLFTagExpressionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Expression = field("Expression")
    Description = field("Description")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLFTagExpressionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLFTagExpressionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagPolicyResource:
    boto3_raw_data: "type_defs.LFTagPolicyResourceTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    CatalogId = field("CatalogId")
    Expression = field("Expression")
    ExpressionName = field("ExpressionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LFTagPolicyResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LFTagPolicyResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchDatabasesByLFTagsRequestPaginate:
    boto3_raw_data: "type_defs.SearchDatabasesByLFTagsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Expression = field("Expression")
    CatalogId = field("CatalogId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchDatabasesByLFTagsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchDatabasesByLFTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchDatabasesByLFTagsRequest:
    boto3_raw_data: "type_defs.SearchDatabasesByLFTagsRequestTypeDef" = (
        dataclasses.field()
    )

    Expression = field("Expression")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchDatabasesByLFTagsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchDatabasesByLFTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTablesByLFTagsRequestPaginate:
    boto3_raw_data: "type_defs.SearchTablesByLFTagsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Expression = field("Expression")
    CatalogId = field("CatalogId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchTablesByLFTagsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTablesByLFTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTablesByLFTagsRequest:
    boto3_raw_data: "type_defs.SearchTablesByLFTagsRequestTypeDef" = dataclasses.field()

    Expression = field("Expression")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchTablesByLFTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTablesByLFTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLFTagExpressionRequest:
    boto3_raw_data: "type_defs.UpdateLFTagExpressionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Expression = field("Expression")
    Description = field("Description")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLFTagExpressionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLFTagExpressionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableObjectsResponse:
    boto3_raw_data: "type_defs.GetTableObjectsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Objects(self):  # pragma: no cover
        return PartitionObjects.make_many(self.boto3_raw_data["Objects"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableObjectsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableObjectsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataCellsFilterRequestPaginate:
    boto3_raw_data: "type_defs.ListDataCellsFilterRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Table = field("Table")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataCellsFilterRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataCellsFilterRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataCellsFilterRequest:
    boto3_raw_data: "type_defs.ListDataCellsFilterRequestTypeDef" = dataclasses.field()

    Table = field("Table")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataCellsFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataCellsFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeSettingsResponse:
    boto3_raw_data: "type_defs.GetDataLakeSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataLakeSettings(self):  # pragma: no cover
        return DataLakeSettingsOutput.make_one(self.boto3_raw_data["DataLakeSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataLakeSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTablesByLFTagsResponse:
    boto3_raw_data: "type_defs.SearchTablesByLFTagsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TableList(self):  # pragma: no cover
        return TaggedTable.make_many(self.boto3_raw_data["TableList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchTablesByLFTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTablesByLFTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataCellsFilterRequest:
    boto3_raw_data: "type_defs.CreateDataCellsFilterRequestTypeDef" = (
        dataclasses.field()
    )

    TableData = field("TableData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataCellsFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataCellsFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataCellsFilterRequest:
    boto3_raw_data: "type_defs.UpdateDataCellsFilterRequestTypeDef" = (
        dataclasses.field()
    )

    TableData = field("TableData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataCellsFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataCellsFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPermissionsRequestEntryOutput:
    boto3_raw_data: "type_defs.BatchPermissionsRequestEntryOutputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    @cached_property
    def Resource(self):  # pragma: no cover
        return ResourceOutput.make_one(self.boto3_raw_data["Resource"])

    Permissions = field("Permissions")

    @cached_property
    def Condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["Condition"])

    PermissionsWithGrantOption = field("PermissionsWithGrantOption")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchPermissionsRequestEntryOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPermissionsRequestEntryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LakeFormationOptInsInfo:
    boto3_raw_data: "type_defs.LakeFormationOptInsInfoTypeDef" = dataclasses.field()

    @cached_property
    def Resource(self):  # pragma: no cover
        return ResourceOutput.make_one(self.boto3_raw_data["Resource"])

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    @cached_property
    def Condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["Condition"])

    LastModified = field("LastModified")
    LastUpdatedBy = field("LastUpdatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LakeFormationOptInsInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LakeFormationOptInsInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrincipalResourcePermissions:
    boto3_raw_data: "type_defs.PrincipalResourcePermissionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    @cached_property
    def Resource(self):  # pragma: no cover
        return ResourceOutput.make_one(self.boto3_raw_data["Resource"])

    @cached_property
    def Condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["Condition"])

    Permissions = field("Permissions")
    PermissionsWithGrantOption = field("PermissionsWithGrantOption")

    @cached_property
    def AdditionalDetails(self):  # pragma: no cover
        return DetailsMap.make_one(self.boto3_raw_data["AdditionalDetails"])

    LastUpdated = field("LastUpdated")
    LastUpdatedBy = field("LastUpdatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrincipalResourcePermissionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrincipalResourcePermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDataLakeSettingsRequest:
    boto3_raw_data: "type_defs.PutDataLakeSettingsRequestTypeDef" = dataclasses.field()

    DataLakeSettings = field("DataLakeSettings")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDataLakeSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDataLakeSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPermissionsFailureEntry:
    boto3_raw_data: "type_defs.BatchPermissionsFailureEntryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RequestEntry(self):  # pragma: no cover
        return BatchPermissionsRequestEntryOutput.make_one(
            self.boto3_raw_data["RequestEntry"]
        )

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPermissionsFailureEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPermissionsFailureEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLakeFormationOptInsResponse:
    boto3_raw_data: "type_defs.ListLakeFormationOptInsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LakeFormationOptInsInfoList(self):  # pragma: no cover
        return LakeFormationOptInsInfo.make_many(
            self.boto3_raw_data["LakeFormationOptInsInfoList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLakeFormationOptInsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLakeFormationOptInsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEffectivePermissionsForPathResponse:
    boto3_raw_data: "type_defs.GetEffectivePermissionsForPathResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Permissions(self):  # pragma: no cover
        return PrincipalResourcePermissions.make_many(
            self.boto3_raw_data["Permissions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEffectivePermissionsForPathResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEffectivePermissionsForPathResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionsResponse:
    boto3_raw_data: "type_defs.ListPermissionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def PrincipalResourcePermissions(self):  # pragma: no cover
        return PrincipalResourcePermissions.make_many(
            self.boto3_raw_data["PrincipalResourcePermissions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPermissionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    @cached_property
    def Catalog(self):  # pragma: no cover
        return CatalogResource.make_one(self.boto3_raw_data["Catalog"])

    @cached_property
    def Database(self):  # pragma: no cover
        return DatabaseResource.make_one(self.boto3_raw_data["Database"])

    Table = field("Table")
    TableWithColumns = field("TableWithColumns")

    @cached_property
    def DataLocation(self):  # pragma: no cover
        return DataLocationResource.make_one(self.boto3_raw_data["DataLocation"])

    @cached_property
    def DataCellsFilter(self):  # pragma: no cover
        return DataCellsFilterResource.make_one(self.boto3_raw_data["DataCellsFilter"])

    LFTag = field("LFTag")
    LFTagPolicy = field("LFTagPolicy")

    @cached_property
    def LFTagExpression(self):  # pragma: no cover
        return LFTagExpressionResource.make_one(self.boto3_raw_data["LFTagExpression"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGrantPermissionsResponse:
    boto3_raw_data: "type_defs.BatchGrantPermissionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Failures(self):  # pragma: no cover
        return BatchPermissionsFailureEntry.make_many(self.boto3_raw_data["Failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGrantPermissionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGrantPermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchRevokePermissionsResponse:
    boto3_raw_data: "type_defs.BatchRevokePermissionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Failures(self):  # pragma: no cover
        return BatchPermissionsFailureEntry.make_many(self.boto3_raw_data["Failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchRevokePermissionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchRevokePermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddLFTagsToResourceRequest:
    boto3_raw_data: "type_defs.AddLFTagsToResourceRequestTypeDef" = dataclasses.field()

    Resource = field("Resource")
    LFTags = field("LFTags")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddLFTagsToResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddLFTagsToResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPermissionsRequestEntry:
    boto3_raw_data: "type_defs.BatchPermissionsRequestEntryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    Resource = field("Resource")
    Permissions = field("Permissions")

    @cached_property
    def Condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["Condition"])

    PermissionsWithGrantOption = field("PermissionsWithGrantOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPermissionsRequestEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPermissionsRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLakeFormationOptInRequest:
    boto3_raw_data: "type_defs.CreateLakeFormationOptInRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    Resource = field("Resource")

    @cached_property
    def Condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["Condition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLakeFormationOptInRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLakeFormationOptInRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLakeFormationOptInRequest:
    boto3_raw_data: "type_defs.DeleteLakeFormationOptInRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    Resource = field("Resource")

    @cached_property
    def Condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["Condition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteLakeFormationOptInRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLakeFormationOptInRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceLFTagsRequest:
    boto3_raw_data: "type_defs.GetResourceLFTagsRequestTypeDef" = dataclasses.field()

    Resource = field("Resource")
    CatalogId = field("CatalogId")
    ShowAssignedLFTags = field("ShowAssignedLFTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceLFTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceLFTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantPermissionsRequest:
    boto3_raw_data: "type_defs.GrantPermissionsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    Resource = field("Resource")
    Permissions = field("Permissions")
    CatalogId = field("CatalogId")

    @cached_property
    def Condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["Condition"])

    PermissionsWithGrantOption = field("PermissionsWithGrantOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrantPermissionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrantPermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLakeFormationOptInsRequest:
    boto3_raw_data: "type_defs.ListLakeFormationOptInsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    Resource = field("Resource")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLakeFormationOptInsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLakeFormationOptInsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionsRequest:
    boto3_raw_data: "type_defs.ListPermissionsRequestTypeDef" = dataclasses.field()

    CatalogId = field("CatalogId")

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    ResourceType = field("ResourceType")
    Resource = field("Resource")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    IncludeRelated = field("IncludeRelated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPermissionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveLFTagsFromResourceRequest:
    boto3_raw_data: "type_defs.RemoveLFTagsFromResourceRequestTypeDef" = (
        dataclasses.field()
    )

    Resource = field("Resource")
    LFTags = field("LFTags")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveLFTagsFromResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveLFTagsFromResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokePermissionsRequest:
    boto3_raw_data: "type_defs.RevokePermissionsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Principal(self):  # pragma: no cover
        return DataLakePrincipal.make_one(self.boto3_raw_data["Principal"])

    Resource = field("Resource")
    Permissions = field("Permissions")
    CatalogId = field("CatalogId")

    @cached_property
    def Condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["Condition"])

    PermissionsWithGrantOption = field("PermissionsWithGrantOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokePermissionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGrantPermissionsRequest:
    boto3_raw_data: "type_defs.BatchGrantPermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    Entries = field("Entries")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGrantPermissionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGrantPermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchRevokePermissionsRequest:
    boto3_raw_data: "type_defs.BatchRevokePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    Entries = field("Entries")
    CatalogId = field("CatalogId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchRevokePermissionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchRevokePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
