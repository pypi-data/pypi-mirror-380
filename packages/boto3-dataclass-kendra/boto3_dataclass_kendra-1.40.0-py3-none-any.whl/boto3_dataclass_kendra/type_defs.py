# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kendra import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessControlConfigurationSummary:
    boto3_raw_data: "type_defs.AccessControlConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AccessControlConfigurationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlListConfiguration:
    boto3_raw_data: "type_defs.AccessControlListConfigurationTypeDef" = (
        dataclasses.field()
    )

    KeyPath = field("KeyPath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AccessControlListConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlListConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AclConfiguration:
    boto3_raw_data: "type_defs.AclConfigurationTypeDef" = dataclasses.field()

    AllowedGroupsColumnName = field("AllowedGroupsColumnName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AclConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AclConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceToIndexFieldMapping:
    boto3_raw_data: "type_defs.DataSourceToIndexFieldMappingTypeDef" = (
        dataclasses.field()
    )

    DataSourceFieldName = field("DataSourceFieldName")
    IndexFieldName = field("IndexFieldName")
    DateFieldFormat = field("DateFieldFormat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataSourceToIndexFieldMappingTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceToIndexFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceVpcConfigurationOutput:
    boto3_raw_data: "type_defs.DataSourceVpcConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataSourceVpcConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceVpcConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Path:
    boto3_raw_data: "type_defs.S3PathTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3PathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3PathTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceVpcConfiguration:
    boto3_raw_data: "type_defs.DataSourceVpcConfigurationTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceVpcConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceVpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityConfiguration:
    boto3_raw_data: "type_defs.EntityConfigurationTypeDef" = dataclasses.field()

    EntityId = field("EntityId")
    EntityType = field("EntityType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedEntity:
    boto3_raw_data: "type_defs.FailedEntityTypeDef" = dataclasses.field()

    EntityId = field("EntityId")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailedEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailedEntityTypeDef"]],
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
class EntityPersonaConfiguration:
    boto3_raw_data: "type_defs.EntityPersonaConfigurationTypeDef" = dataclasses.field()

    EntityId = field("EntityId")
    Persona = field("Persona")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityPersonaConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityPersonaConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestableConfig:
    boto3_raw_data: "type_defs.SuggestableConfigTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    Suggestable = field("Suggestable")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestableConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuggestableConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BasicAuthenticationConfiguration:
    boto3_raw_data: "type_defs.BasicAuthenticationConfigurationTypeDef" = (
        dataclasses.field()
    )

    Host = field("Host")
    Port = field("Port")
    Credentials = field("Credentials")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BasicAuthenticationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BasicAuthenticationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceSyncJobMetricTarget:
    boto3_raw_data: "type_defs.DataSourceSyncJobMetricTargetTypeDef" = (
        dataclasses.field()
    )

    DataSourceId = field("DataSourceId")
    DataSourceSyncJobId = field("DataSourceSyncJobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataSourceSyncJobMetricTargetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceSyncJobMetricTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDocumentResponseFailedDocument:
    boto3_raw_data: "type_defs.BatchDeleteDocumentResponseFailedDocumentTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    DataSourceId = field("DataSourceId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteDocumentResponseFailedDocumentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDocumentResponseFailedDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteFeaturedResultsSetError:
    boto3_raw_data: "type_defs.BatchDeleteFeaturedResultsSetErrorTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteFeaturedResultsSetErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteFeaturedResultsSetErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteFeaturedResultsSetRequest:
    boto3_raw_data: "type_defs.BatchDeleteFeaturedResultsSetRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    FeaturedResultsSetIds = field("FeaturedResultsSetIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteFeaturedResultsSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteFeaturedResultsSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDocumentStatusResponseError:
    boto3_raw_data: "type_defs.BatchGetDocumentStatusResponseErrorTypeDef" = (
        dataclasses.field()
    )

    DocumentId = field("DocumentId")
    DataSourceId = field("DataSourceId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetDocumentStatusResponseErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDocumentStatusResponseErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Status:
    boto3_raw_data: "type_defs.StatusTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    DocumentStatus = field("DocumentStatus")
    FailureCode = field("FailureCode")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutDocumentResponseFailedDocument:
    boto3_raw_data: "type_defs.BatchPutDocumentResponseFailedDocumentTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    DataSourceId = field("DataSourceId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchPutDocumentResponseFailedDocumentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutDocumentResponseFailedDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityUnitsConfiguration:
    boto3_raw_data: "type_defs.CapacityUnitsConfigurationTypeDef" = dataclasses.field()

    StorageCapacityUnits = field("StorageCapacityUnits")
    QueryCapacityUnits = field("QueryCapacityUnits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityUnitsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityUnitsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClearQuerySuggestionsRequest:
    boto3_raw_data: "type_defs.ClearQuerySuggestionsRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClearQuerySuggestionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClearQuerySuggestionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpandConfiguration:
    boto3_raw_data: "type_defs.ExpandConfigurationTypeDef" = dataclasses.field()

    MaxResultItemsToExpand = field("MaxResultItemsToExpand")
    MaxExpandedResultsPerItem = field("MaxExpandedResultsPerItem")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpandConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpandConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SortingConfiguration:
    boto3_raw_data: "type_defs.SortingConfigurationTypeDef" = dataclasses.field()

    DocumentAttributeKey = field("DocumentAttributeKey")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SortingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SortingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceAttachmentToIndexFieldMapping:
    boto3_raw_data: "type_defs.ConfluenceAttachmentToIndexFieldMappingTypeDef" = (
        dataclasses.field()
    )

    DataSourceFieldName = field("DataSourceFieldName")
    DateFieldFormat = field("DateFieldFormat")
    IndexFieldName = field("IndexFieldName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluenceAttachmentToIndexFieldMappingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceAttachmentToIndexFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceBlogToIndexFieldMapping:
    boto3_raw_data: "type_defs.ConfluenceBlogToIndexFieldMappingTypeDef" = (
        dataclasses.field()
    )

    DataSourceFieldName = field("DataSourceFieldName")
    DateFieldFormat = field("DateFieldFormat")
    IndexFieldName = field("IndexFieldName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluenceBlogToIndexFieldMappingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceBlogToIndexFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProxyConfiguration:
    boto3_raw_data: "type_defs.ProxyConfigurationTypeDef" = dataclasses.field()

    Host = field("Host")
    Port = field("Port")
    Credentials = field("Credentials")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProxyConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProxyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluencePageToIndexFieldMapping:
    boto3_raw_data: "type_defs.ConfluencePageToIndexFieldMappingTypeDef" = (
        dataclasses.field()
    )

    DataSourceFieldName = field("DataSourceFieldName")
    DateFieldFormat = field("DateFieldFormat")
    IndexFieldName = field("IndexFieldName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluencePageToIndexFieldMappingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluencePageToIndexFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceSpaceToIndexFieldMapping:
    boto3_raw_data: "type_defs.ConfluenceSpaceToIndexFieldMappingTypeDef" = (
        dataclasses.field()
    )

    DataSourceFieldName = field("DataSourceFieldName")
    DateFieldFormat = field("DateFieldFormat")
    IndexFieldName = field("IndexFieldName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluenceSpaceToIndexFieldMappingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceSpaceToIndexFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionConfiguration:
    boto3_raw_data: "type_defs.ConnectionConfigurationTypeDef" = dataclasses.field()

    DatabaseHost = field("DatabaseHost")
    DatabasePort = field("DatabasePort")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    SecretArn = field("SecretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentSourceConfigurationOutput:
    boto3_raw_data: "type_defs.ContentSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    DataSourceIds = field("DataSourceIds")
    FaqIds = field("FaqIds")
    DirectPutContent = field("DirectPutContent")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContentSourceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentSourceConfiguration:
    boto3_raw_data: "type_defs.ContentSourceConfigurationTypeDef" = dataclasses.field()

    DataSourceIds = field("DataSourceIds")
    FaqIds = field("FaqIds")
    DirectPutContent = field("DirectPutContent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Correction:
    boto3_raw_data: "type_defs.CorrectionTypeDef" = dataclasses.field()

    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")
    Term = field("Term")
    CorrectedTerm = field("CorrectedTerm")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CorrectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CorrectionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Principal:
    boto3_raw_data: "type_defs.PrincipalTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Access = field("Access")
    DataSourceId = field("DataSourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrincipalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrincipalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturedDocument:
    boto3_raw_data: "type_defs.FeaturedDocumentTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FeaturedDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturedDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryptionConfiguration:
    boto3_raw_data: "type_defs.ServerSideEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerSideEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserGroupResolutionConfiguration:
    boto3_raw_data: "type_defs.UserGroupResolutionConfigurationTypeDef" = (
        dataclasses.field()
    )

    UserGroupResolutionMode = field("UserGroupResolutionMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UserGroupResolutionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserGroupResolutionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateConfigurationOutput:
    boto3_raw_data: "type_defs.TemplateConfigurationOutputTypeDef" = dataclasses.field()

    Template = field("Template")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateConfiguration:
    boto3_raw_data: "type_defs.TemplateConfigurationTypeDef" = dataclasses.field()

    Template = field("Template")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceGroup:
    boto3_raw_data: "type_defs.DataSourceGroupTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    DataSourceId = field("DataSourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceSummary:
    boto3_raw_data: "type_defs.DataSourceSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Type = field("Type")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    Status = field("Status")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceSyncJobMetrics:
    boto3_raw_data: "type_defs.DataSourceSyncJobMetricsTypeDef" = dataclasses.field()

    DocumentsAdded = field("DocumentsAdded")
    DocumentsModified = field("DocumentsModified")
    DocumentsDeleted = field("DocumentsDeleted")
    DocumentsFailed = field("DocumentsFailed")
    DocumentsScanned = field("DocumentsScanned")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceSyncJobMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceSyncJobMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlConfiguration:
    boto3_raw_data: "type_defs.SqlConfigurationTypeDef" = dataclasses.field()

    QueryIdentifiersEnclosingOption = field("QueryIdentifiersEnclosingOption")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SqlConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqlConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessControlConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteAccessControlConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccessControlConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessControlConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSourceRequest:
    boto3_raw_data: "type_defs.DeleteDataSourceRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExperienceRequest:
    boto3_raw_data: "type_defs.DeleteExperienceRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteExperienceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExperienceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFaqRequest:
    boto3_raw_data: "type_defs.DeleteFaqRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFaqRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFaqRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIndexRequest:
    boto3_raw_data: "type_defs.DeleteIndexRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePrincipalMappingRequest:
    boto3_raw_data: "type_defs.DeletePrincipalMappingRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    GroupId = field("GroupId")
    DataSourceId = field("DataSourceId")
    OrderingId = field("OrderingId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePrincipalMappingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePrincipalMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQuerySuggestionsBlockListRequest:
    boto3_raw_data: "type_defs.DeleteQuerySuggestionsBlockListRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteQuerySuggestionsBlockListRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQuerySuggestionsBlockListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteThesaurusRequest:
    boto3_raw_data: "type_defs.DeleteThesaurusRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteThesaurusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteThesaurusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessControlConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeAccessControlConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccessControlConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessControlConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSourceRequest:
    boto3_raw_data: "type_defs.DescribeDataSourceRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExperienceRequest:
    boto3_raw_data: "type_defs.DescribeExperienceRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExperienceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExperienceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperienceEndpoint:
    boto3_raw_data: "type_defs.ExperienceEndpointTypeDef" = dataclasses.field()

    EndpointType = field("EndpointType")
    Endpoint = field("Endpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperienceEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperienceEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFaqRequest:
    boto3_raw_data: "type_defs.DescribeFaqRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFaqRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFaqRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFeaturedResultsSetRequest:
    boto3_raw_data: "type_defs.DescribeFeaturedResultsSetRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    FeaturedResultsSetId = field("FeaturedResultsSetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFeaturedResultsSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFeaturedResultsSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturedDocumentMissing:
    boto3_raw_data: "type_defs.FeaturedDocumentMissingTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeaturedDocumentMissingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturedDocumentMissingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturedDocumentWithMetadata:
    boto3_raw_data: "type_defs.FeaturedDocumentWithMetadataTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Title = field("Title")
    URI = field("URI")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeaturedDocumentWithMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturedDocumentWithMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIndexRequest:
    boto3_raw_data: "type_defs.DescribeIndexRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePrincipalMappingRequest:
    boto3_raw_data: "type_defs.DescribePrincipalMappingRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    GroupId = field("GroupId")
    DataSourceId = field("DataSourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePrincipalMappingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePrincipalMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupOrderingIdSummary:
    boto3_raw_data: "type_defs.GroupOrderingIdSummaryTypeDef" = dataclasses.field()

    Status = field("Status")
    LastUpdatedAt = field("LastUpdatedAt")
    ReceivedAt = field("ReceivedAt")
    OrderingId = field("OrderingId")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GroupOrderingIdSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupOrderingIdSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQuerySuggestionsBlockListRequest:
    boto3_raw_data: "type_defs.DescribeQuerySuggestionsBlockListRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeQuerySuggestionsBlockListRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQuerySuggestionsBlockListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQuerySuggestionsConfigRequest:
    boto3_raw_data: "type_defs.DescribeQuerySuggestionsConfigRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeQuerySuggestionsConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQuerySuggestionsConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThesaurusRequest:
    boto3_raw_data: "type_defs.DescribeThesaurusRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThesaurusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThesaurusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePersonasFromEntitiesRequest:
    boto3_raw_data: "type_defs.DisassociatePersonasFromEntitiesRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IndexId = field("IndexId")
    EntityIds = field("EntityIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociatePersonasFromEntitiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociatePersonasFromEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeValueOutput:
    boto3_raw_data: "type_defs.DocumentAttributeValueOutputTypeDef" = (
        dataclasses.field()
    )

    StringValue = field("StringValue")
    StringListValue = field("StringListValue")
    LongValue = field("LongValue")
    DateValue = field("DateValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelevanceOutput:
    boto3_raw_data: "type_defs.RelevanceOutputTypeDef" = dataclasses.field()

    Freshness = field("Freshness")
    Importance = field("Importance")
    Duration = field("Duration")
    RankOrder = field("RankOrder")
    ValueImportanceMap = field("ValueImportanceMap")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelevanceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelevanceOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Search:
    boto3_raw_data: "type_defs.SearchTypeDef" = dataclasses.field()

    Facetable = field("Facetable")
    Searchable = field("Searchable")
    Displayable = field("Displayable")
    Sortable = field("Sortable")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentsMetadataConfiguration:
    boto3_raw_data: "type_defs.DocumentsMetadataConfigurationTypeDef" = (
        dataclasses.field()
    )

    S3Prefix = field("S3Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentsMetadataConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentsMetadataConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityDisplayData:
    boto3_raw_data: "type_defs.EntityDisplayDataTypeDef" = dataclasses.field()

    UserName = field("UserName")
    GroupName = field("GroupName")
    IdentifiedUserName = field("IdentifiedUserName")
    FirstName = field("FirstName")
    LastName = field("LastName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityDisplayDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityDisplayDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserIdentityConfiguration:
    boto3_raw_data: "type_defs.UserIdentityConfigurationTypeDef" = dataclasses.field()

    IdentityAttributeName = field("IdentityAttributeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserIdentityConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserIdentityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Facet:
    boto3_raw_data: "type_defs.FacetTypeDef" = dataclasses.field()

    DocumentAttributeKey = field("DocumentAttributeKey")
    Facets = field("Facets")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FacetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FacetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaqStatistics:
    boto3_raw_data: "type_defs.FaqStatisticsTypeDef" = dataclasses.field()

    IndexedQuestionAnswersCount = field("IndexedQuestionAnswersCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FaqStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FaqStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FaqSummary:
    boto3_raw_data: "type_defs.FaqSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Status = field("Status")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    FileFormat = field("FileFormat")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FaqSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FaqSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturedResultsSetSummary:
    boto3_raw_data: "type_defs.FeaturedResultsSetSummaryTypeDef" = dataclasses.field()

    FeaturedResultsSetId = field("FeaturedResultsSetId")
    FeaturedResultsSetName = field("FeaturedResultsSetName")
    Status = field("Status")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    CreationTimestamp = field("CreationTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeaturedResultsSetSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturedResultsSetSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSnapshotsRequest:
    boto3_raw_data: "type_defs.GetSnapshotsRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    Interval = field("Interval")
    MetricType = field("MetricType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSnapshotsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeRangeOutput:
    boto3_raw_data: "type_defs.TimeRangeOutputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeRangeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeRangeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitHubDocumentCrawlProperties:
    boto3_raw_data: "type_defs.GitHubDocumentCrawlPropertiesTypeDef" = (
        dataclasses.field()
    )

    CrawlRepositoryDocuments = field("CrawlRepositoryDocuments")
    CrawlIssue = field("CrawlIssue")
    CrawlIssueComment = field("CrawlIssueComment")
    CrawlIssueCommentAttachment = field("CrawlIssueCommentAttachment")
    CrawlPullRequest = field("CrawlPullRequest")
    CrawlPullRequestComment = field("CrawlPullRequestComment")
    CrawlPullRequestCommentAttachment = field("CrawlPullRequestCommentAttachment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GitHubDocumentCrawlPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitHubDocumentCrawlPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SaaSConfiguration:
    boto3_raw_data: "type_defs.SaaSConfigurationTypeDef" = dataclasses.field()

    OrganizationName = field("OrganizationName")
    HostUrl = field("HostUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SaaSConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SaaSConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberGroup:
    boto3_raw_data: "type_defs.MemberGroupTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    DataSourceId = field("DataSourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberUser:
    boto3_raw_data: "type_defs.MemberUserTypeDef" = dataclasses.field()

    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupSummary:
    boto3_raw_data: "type_defs.GroupSummaryTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    OrderingId = field("OrderingId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Highlight:
    boto3_raw_data: "type_defs.HighlightTypeDef" = dataclasses.field()

    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")
    TopAnswer = field("TopAnswer")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HighlightTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HighlightTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexConfigurationSummary:
    boto3_raw_data: "type_defs.IndexConfigurationSummaryTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    Status = field("Status")
    Name = field("Name")
    Id = field("Id")
    Edition = field("Edition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IndexConfigurationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextDocumentStatistics:
    boto3_raw_data: "type_defs.TextDocumentStatisticsTypeDef" = dataclasses.field()

    IndexedTextDocumentsCount = field("IndexedTextDocumentsCount")
    IndexedTextBytes = field("IndexedTextBytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextDocumentStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextDocumentStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JsonTokenTypeConfiguration:
    boto3_raw_data: "type_defs.JsonTokenTypeConfigurationTypeDef" = dataclasses.field()

    UserNameAttributeField = field("UserNameAttributeField")
    GroupAttributeField = field("GroupAttributeField")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JsonTokenTypeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JsonTokenTypeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JwtTokenTypeConfiguration:
    boto3_raw_data: "type_defs.JwtTokenTypeConfigurationTypeDef" = dataclasses.field()

    KeyLocation = field("KeyLocation")
    URL = field("URL")
    SecretManagerArn = field("SecretManagerArn")
    UserNameAttributeField = field("UserNameAttributeField")
    GroupAttributeField = field("GroupAttributeField")
    Issuer = field("Issuer")
    ClaimRegex = field("ClaimRegex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JwtTokenTypeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JwtTokenTypeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessControlConfigurationsRequest:
    boto3_raw_data: "type_defs.ListAccessControlConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessControlConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessControlConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesRequest:
    boto3_raw_data: "type_defs.ListDataSourcesRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntityPersonasRequest:
    boto3_raw_data: "type_defs.ListEntityPersonasRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntityPersonasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntityPersonasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PersonasSummary:
    boto3_raw_data: "type_defs.PersonasSummaryTypeDef" = dataclasses.field()

    EntityId = field("EntityId")
    Persona = field("Persona")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PersonasSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PersonasSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperienceEntitiesRequest:
    boto3_raw_data: "type_defs.ListExperienceEntitiesRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IndexId = field("IndexId")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExperienceEntitiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperienceEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperiencesRequest:
    boto3_raw_data: "type_defs.ListExperiencesRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExperiencesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperiencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFaqsRequest:
    boto3_raw_data: "type_defs.ListFaqsRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFaqsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListFaqsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFeaturedResultsSetsRequest:
    boto3_raw_data: "type_defs.ListFeaturedResultsSetsRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFeaturedResultsSetsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFeaturedResultsSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsOlderThanOrderingIdRequest:
    boto3_raw_data: "type_defs.ListGroupsOlderThanOrderingIdRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    OrderingId = field("OrderingId")
    DataSourceId = field("DataSourceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGroupsOlderThanOrderingIdRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsOlderThanOrderingIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndicesRequest:
    boto3_raw_data: "type_defs.ListIndicesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQuerySuggestionsBlockListsRequest:
    boto3_raw_data: "type_defs.ListQuerySuggestionsBlockListsRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQuerySuggestionsBlockListsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQuerySuggestionsBlockListsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuerySuggestionsBlockListSummary:
    boto3_raw_data: "type_defs.QuerySuggestionsBlockListSummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Name = field("Name")
    Status = field("Status")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    ItemCount = field("ItemCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QuerySuggestionsBlockListSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuerySuggestionsBlockListSummaryTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class ListThesauriRequest:
    boto3_raw_data: "type_defs.ListThesauriRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThesauriRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThesauriRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThesaurusSummary:
    boto3_raw_data: "type_defs.ThesaurusSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Status = field("Status")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThesaurusSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThesaurusSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpellCorrectionConfiguration:
    boto3_raw_data: "type_defs.SpellCorrectionConfigurationTypeDef" = (
        dataclasses.field()
    )

    IncludeQuerySpellCheckSuggestions = field("IncludeQuerySpellCheckSuggestions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpellCorrectionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpellCorrectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScoreAttributes:
    boto3_raw_data: "type_defs.ScoreAttributesTypeDef" = dataclasses.field()

    ScoreConfidence = field("ScoreConfidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScoreAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScoreAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Warning:
    boto3_raw_data: "type_defs.WarningTypeDef" = dataclasses.field()

    Message = field("Message")
    Code = field("Code")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WarningTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WarningTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelevanceFeedback:
    boto3_raw_data: "type_defs.RelevanceFeedbackTypeDef" = dataclasses.field()

    ResultId = field("ResultId")
    RelevanceValue = field("RelevanceValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelevanceFeedbackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelevanceFeedbackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Relevance:
    boto3_raw_data: "type_defs.RelevanceTypeDef" = dataclasses.field()

    Freshness = field("Freshness")
    Importance = field("Importance")
    Duration = field("Duration")
    RankOrder = field("RankOrder")
    ValueImportanceMap = field("ValueImportanceMap")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelevanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelevanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SeedUrlConfigurationOutput:
    boto3_raw_data: "type_defs.SeedUrlConfigurationOutputTypeDef" = dataclasses.field()

    SeedUrls = field("SeedUrls")
    WebCrawlerMode = field("WebCrawlerMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SeedUrlConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SeedUrlConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SeedUrlConfiguration:
    boto3_raw_data: "type_defs.SeedUrlConfigurationTypeDef" = dataclasses.field()

    SeedUrls = field("SeedUrls")
    WebCrawlerMode = field("WebCrawlerMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SeedUrlConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SeedUrlConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SiteMapsConfigurationOutput:
    boto3_raw_data: "type_defs.SiteMapsConfigurationOutputTypeDef" = dataclasses.field()

    SiteMaps = field("SiteMaps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SiteMapsConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SiteMapsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SiteMapsConfiguration:
    boto3_raw_data: "type_defs.SiteMapsConfigurationTypeDef" = dataclasses.field()

    SiteMaps = field("SiteMaps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SiteMapsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SiteMapsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataSourceSyncJobRequest:
    boto3_raw_data: "type_defs.StartDataSourceSyncJobRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDataSourceSyncJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataSourceSyncJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDataSourceSyncJobRequest:
    boto3_raw_data: "type_defs.StopDataSourceSyncJobRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IndexId = field("IndexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDataSourceSyncJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDataSourceSyncJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestionHighlight:
    boto3_raw_data: "type_defs.SuggestionHighlightTypeDef" = dataclasses.field()

    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuggestionHighlightTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuggestionHighlightTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableCell:
    boto3_raw_data: "type_defs.TableCellTypeDef" = dataclasses.field()

    Value = field("Value")
    TopAnswer = field("TopAnswer")
    Highlighted = field("Highlighted")
    Header = field("Header")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableCellTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableCellTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    TagKeys = field("TagKeys")

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
class ColumnConfigurationOutput:
    boto3_raw_data: "type_defs.ColumnConfigurationOutputTypeDef" = dataclasses.field()

    DocumentIdColumnName = field("DocumentIdColumnName")
    DocumentDataColumnName = field("DocumentDataColumnName")
    ChangeDetectingColumns = field("ChangeDetectingColumns")
    DocumentTitleColumnName = field("DocumentTitleColumnName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ColumnConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnConfiguration:
    boto3_raw_data: "type_defs.ColumnConfigurationTypeDef" = dataclasses.field()

    DocumentIdColumnName = field("DocumentIdColumnName")
    DocumentDataColumnName = field("DocumentDataColumnName")
    ChangeDetectingColumns = field("ChangeDetectingColumns")
    DocumentTitleColumnName = field("DocumentTitleColumnName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ColumnConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GoogleDriveConfigurationOutput:
    boto3_raw_data: "type_defs.GoogleDriveConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    SecretArn = field("SecretArn")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    ExcludeMimeTypes = field("ExcludeMimeTypes")
    ExcludeUserAccounts = field("ExcludeUserAccounts")
    ExcludeSharedDrives = field("ExcludeSharedDrives")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GoogleDriveConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GoogleDriveConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GoogleDriveConfiguration:
    boto3_raw_data: "type_defs.GoogleDriveConfigurationTypeDef" = dataclasses.field()

    SecretArn = field("SecretArn")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    ExcludeMimeTypes = field("ExcludeMimeTypes")
    ExcludeUserAccounts = field("ExcludeUserAccounts")
    ExcludeSharedDrives = field("ExcludeSharedDrives")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GoogleDriveConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GoogleDriveConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceChatterFeedConfigurationOutput:
    boto3_raw_data: "type_defs.SalesforceChatterFeedConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    DocumentDataFieldName = field("DocumentDataFieldName")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    IncludeFilterTypes = field("IncludeFilterTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceChatterFeedConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceChatterFeedConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceChatterFeedConfiguration:
    boto3_raw_data: "type_defs.SalesforceChatterFeedConfigurationTypeDef" = (
        dataclasses.field()
    )

    DocumentDataFieldName = field("DocumentDataFieldName")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    IncludeFilterTypes = field("IncludeFilterTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceChatterFeedConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceChatterFeedConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceCustomKnowledgeArticleTypeConfigurationOutput:
    boto3_raw_data: (
        "type_defs.SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef"
    ) = dataclasses.field()

    Name = field("Name")
    DocumentDataFieldName = field("DocumentDataFieldName")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef"
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
                "type_defs.SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceCustomKnowledgeArticleTypeConfiguration:
    boto3_raw_data: (
        "type_defs.SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef"
    ) = dataclasses.field()

    Name = field("Name")
    DocumentDataFieldName = field("DocumentDataFieldName")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef"
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
                "type_defs.SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceStandardKnowledgeArticleTypeConfigurationOutput:
    boto3_raw_data: (
        "type_defs.SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef"
    ) = dataclasses.field()

    DocumentDataFieldName = field("DocumentDataFieldName")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef"
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
                "type_defs.SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceStandardKnowledgeArticleTypeConfiguration:
    boto3_raw_data: (
        "type_defs.SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef"
    ) = dataclasses.field()

    DocumentDataFieldName = field("DocumentDataFieldName")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef"
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
                "type_defs.SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceStandardObjectAttachmentConfigurationOutput:
    boto3_raw_data: (
        "type_defs.SalesforceStandardObjectAttachmentConfigurationOutputTypeDef"
    ) = dataclasses.field()

    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceStandardObjectAttachmentConfigurationOutputTypeDef"
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
                "type_defs.SalesforceStandardObjectAttachmentConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceStandardObjectAttachmentConfiguration:
    boto3_raw_data: (
        "type_defs.SalesforceStandardObjectAttachmentConfigurationTypeDef"
    ) = dataclasses.field()

    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceStandardObjectAttachmentConfigurationTypeDef"
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
                "type_defs.SalesforceStandardObjectAttachmentConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceStandardObjectConfigurationOutput:
    boto3_raw_data: "type_defs.SalesforceStandardObjectConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    DocumentDataFieldName = field("DocumentDataFieldName")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceStandardObjectConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceStandardObjectConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceStandardObjectConfiguration:
    boto3_raw_data: "type_defs.SalesforceStandardObjectConfigurationTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    DocumentDataFieldName = field("DocumentDataFieldName")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceStandardObjectConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceStandardObjectConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNowKnowledgeArticleConfigurationOutput:
    boto3_raw_data: "type_defs.ServiceNowKnowledgeArticleConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    DocumentDataFieldName = field("DocumentDataFieldName")
    CrawlAttachments = field("CrawlAttachments")
    IncludeAttachmentFilePatterns = field("IncludeAttachmentFilePatterns")
    ExcludeAttachmentFilePatterns = field("ExcludeAttachmentFilePatterns")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    FilterQuery = field("FilterQuery")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceNowKnowledgeArticleConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNowKnowledgeArticleConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNowKnowledgeArticleConfiguration:
    boto3_raw_data: "type_defs.ServiceNowKnowledgeArticleConfigurationTypeDef" = (
        dataclasses.field()
    )

    DocumentDataFieldName = field("DocumentDataFieldName")
    CrawlAttachments = field("CrawlAttachments")
    IncludeAttachmentFilePatterns = field("IncludeAttachmentFilePatterns")
    ExcludeAttachmentFilePatterns = field("ExcludeAttachmentFilePatterns")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    FilterQuery = field("FilterQuery")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceNowKnowledgeArticleConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNowKnowledgeArticleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNowServiceCatalogConfigurationOutput:
    boto3_raw_data: "type_defs.ServiceNowServiceCatalogConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    DocumentDataFieldName = field("DocumentDataFieldName")
    CrawlAttachments = field("CrawlAttachments")
    IncludeAttachmentFilePatterns = field("IncludeAttachmentFilePatterns")
    ExcludeAttachmentFilePatterns = field("ExcludeAttachmentFilePatterns")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceNowServiceCatalogConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNowServiceCatalogConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNowServiceCatalogConfiguration:
    boto3_raw_data: "type_defs.ServiceNowServiceCatalogConfigurationTypeDef" = (
        dataclasses.field()
    )

    DocumentDataFieldName = field("DocumentDataFieldName")
    CrawlAttachments = field("CrawlAttachments")
    IncludeAttachmentFilePatterns = field("IncludeAttachmentFilePatterns")
    ExcludeAttachmentFilePatterns = field("ExcludeAttachmentFilePatterns")
    DocumentTitleFieldName = field("DocumentTitleFieldName")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceNowServiceCatalogConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNowServiceCatalogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkDocsConfigurationOutput:
    boto3_raw_data: "type_defs.WorkDocsConfigurationOutputTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    CrawlComments = field("CrawlComments")
    UseChangeLog = field("UseChangeLog")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkDocsConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkDocsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkDocsConfiguration:
    boto3_raw_data: "type_defs.WorkDocsConfigurationTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    CrawlComments = field("CrawlComments")
    UseChangeLog = field("UseChangeLog")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkDocsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkDocsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BoxConfigurationOutput:
    boto3_raw_data: "type_defs.BoxConfigurationOutputTypeDef" = dataclasses.field()

    EnterpriseId = field("EnterpriseId")
    SecretArn = field("SecretArn")
    UseChangeLog = field("UseChangeLog")
    CrawlComments = field("CrawlComments")
    CrawlTasks = field("CrawlTasks")
    CrawlWebLinks = field("CrawlWebLinks")

    @cached_property
    def FileFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FileFieldMappings"]
        )

    @cached_property
    def TaskFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["TaskFieldMappings"]
        )

    @cached_property
    def CommentFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["CommentFieldMappings"]
        )

    @cached_property
    def WebLinkFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["WebLinkFieldMappings"]
        )

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BoxConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BoxConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FsxConfigurationOutput:
    boto3_raw_data: "type_defs.FsxConfigurationOutputTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    FileSystemType = field("FileSystemType")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    SecretArn = field("SecretArn")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FsxConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FsxConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JiraConfigurationOutput:
    boto3_raw_data: "type_defs.JiraConfigurationOutputTypeDef" = dataclasses.field()

    JiraAccountUrl = field("JiraAccountUrl")
    SecretArn = field("SecretArn")
    UseChangeLog = field("UseChangeLog")
    Project = field("Project")
    IssueType = field("IssueType")
    Status = field("Status")
    IssueSubEntityFilter = field("IssueSubEntityFilter")

    @cached_property
    def AttachmentFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["AttachmentFieldMappings"]
        )

    @cached_property
    def CommentFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["CommentFieldMappings"]
        )

    @cached_property
    def IssueFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["IssueFieldMappings"]
        )

    @cached_property
    def ProjectFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["ProjectFieldMappings"]
        )

    @cached_property
    def WorkLogFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["WorkLogFieldMappings"]
        )

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JiraConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JiraConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuipConfigurationOutput:
    boto3_raw_data: "type_defs.QuipConfigurationOutputTypeDef" = dataclasses.field()

    Domain = field("Domain")
    SecretArn = field("SecretArn")
    CrawlFileComments = field("CrawlFileComments")
    CrawlChatRooms = field("CrawlChatRooms")
    CrawlAttachments = field("CrawlAttachments")
    FolderIds = field("FolderIds")

    @cached_property
    def ThreadFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["ThreadFieldMappings"]
        )

    @cached_property
    def MessageFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["MessageFieldMappings"]
        )

    @cached_property
    def AttachmentFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["AttachmentFieldMappings"]
        )

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuipConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuipConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlackConfigurationOutput:
    boto3_raw_data: "type_defs.SlackConfigurationOutputTypeDef" = dataclasses.field()

    TeamId = field("TeamId")
    SecretArn = field("SecretArn")
    SlackEntityList = field("SlackEntityList")
    SinceCrawlDate = field("SinceCrawlDate")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    UseChangeLog = field("UseChangeLog")
    CrawlBotMessage = field("CrawlBotMessage")
    ExcludeArchived = field("ExcludeArchived")
    LookBackPeriod = field("LookBackPeriod")
    PrivateChannelFilter = field("PrivateChannelFilter")
    PublicChannelFilter = field("PublicChannelFilter")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlackConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlackConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlfrescoConfigurationOutput:
    boto3_raw_data: "type_defs.AlfrescoConfigurationOutputTypeDef" = dataclasses.field()

    SiteUrl = field("SiteUrl")
    SiteId = field("SiteId")
    SecretArn = field("SecretArn")

    @cached_property
    def SslCertificateS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SslCertificateS3Path"])

    CrawlSystemFolders = field("CrawlSystemFolders")
    CrawlComments = field("CrawlComments")
    EntityFilter = field("EntityFilter")

    @cached_property
    def DocumentLibraryFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["DocumentLibraryFieldMappings"]
        )

    @cached_property
    def BlogFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["BlogFieldMappings"]
        )

    @cached_property
    def WikiFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["WikiFieldMappings"]
        )

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlfrescoConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlfrescoConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnPremiseConfiguration:
    boto3_raw_data: "type_defs.OnPremiseConfigurationTypeDef" = dataclasses.field()

    HostUrl = field("HostUrl")
    OrganizationName = field("OrganizationName")

    @cached_property
    def SslCertificateS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SslCertificateS3Path"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OnPremiseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnPremiseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OneDriveUsersOutput:
    boto3_raw_data: "type_defs.OneDriveUsersOutputTypeDef" = dataclasses.field()

    OneDriveUserList = field("OneDriveUserList")

    @cached_property
    def OneDriveUserS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["OneDriveUserS3Path"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OneDriveUsersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OneDriveUsersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OneDriveUsers:
    boto3_raw_data: "type_defs.OneDriveUsersTypeDef" = dataclasses.field()

    OneDriveUserList = field("OneDriveUserList")

    @cached_property
    def OneDriveUserS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["OneDriveUserS3Path"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OneDriveUsersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OneDriveUsersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQuerySuggestionsBlockListRequest:
    boto3_raw_data: "type_defs.UpdateQuerySuggestionsBlockListRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    Id = field("Id")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def SourceS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SourceS3Path"])

    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateQuerySuggestionsBlockListRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQuerySuggestionsBlockListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThesaurusRequest:
    boto3_raw_data: "type_defs.UpdateThesaurusRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")
    Name = field("Name")
    Description = field("Description")
    RoleArn = field("RoleArn")

    @cached_property
    def SourceS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SourceS3Path"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThesaurusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThesaurusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlfrescoConfiguration:
    boto3_raw_data: "type_defs.AlfrescoConfigurationTypeDef" = dataclasses.field()

    SiteUrl = field("SiteUrl")
    SiteId = field("SiteId")
    SecretArn = field("SecretArn")

    @cached_property
    def SslCertificateS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SslCertificateS3Path"])

    CrawlSystemFolders = field("CrawlSystemFolders")
    CrawlComments = field("CrawlComments")
    EntityFilter = field("EntityFilter")

    @cached_property
    def DocumentLibraryFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["DocumentLibraryFieldMappings"]
        )

    @cached_property
    def BlogFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["BlogFieldMappings"]
        )

    @cached_property
    def WikiFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["WikiFieldMappings"]
        )

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlfrescoConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlfrescoConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BoxConfiguration:
    boto3_raw_data: "type_defs.BoxConfigurationTypeDef" = dataclasses.field()

    EnterpriseId = field("EnterpriseId")
    SecretArn = field("SecretArn")
    UseChangeLog = field("UseChangeLog")
    CrawlComments = field("CrawlComments")
    CrawlTasks = field("CrawlTasks")
    CrawlWebLinks = field("CrawlWebLinks")

    @cached_property
    def FileFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FileFieldMappings"]
        )

    @cached_property
    def TaskFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["TaskFieldMappings"]
        )

    @cached_property
    def CommentFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["CommentFieldMappings"]
        )

    @cached_property
    def WebLinkFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["WebLinkFieldMappings"]
        )

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BoxConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BoxConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FsxConfiguration:
    boto3_raw_data: "type_defs.FsxConfigurationTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    FileSystemType = field("FileSystemType")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    SecretArn = field("SecretArn")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FsxConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FsxConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JiraConfiguration:
    boto3_raw_data: "type_defs.JiraConfigurationTypeDef" = dataclasses.field()

    JiraAccountUrl = field("JiraAccountUrl")
    SecretArn = field("SecretArn")
    UseChangeLog = field("UseChangeLog")
    Project = field("Project")
    IssueType = field("IssueType")
    Status = field("Status")
    IssueSubEntityFilter = field("IssueSubEntityFilter")

    @cached_property
    def AttachmentFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["AttachmentFieldMappings"]
        )

    @cached_property
    def CommentFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["CommentFieldMappings"]
        )

    @cached_property
    def IssueFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["IssueFieldMappings"]
        )

    @cached_property
    def ProjectFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["ProjectFieldMappings"]
        )

    @cached_property
    def WorkLogFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["WorkLogFieldMappings"]
        )

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JiraConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JiraConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuipConfiguration:
    boto3_raw_data: "type_defs.QuipConfigurationTypeDef" = dataclasses.field()

    Domain = field("Domain")
    SecretArn = field("SecretArn")
    CrawlFileComments = field("CrawlFileComments")
    CrawlChatRooms = field("CrawlChatRooms")
    CrawlAttachments = field("CrawlAttachments")
    FolderIds = field("FolderIds")

    @cached_property
    def ThreadFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["ThreadFieldMappings"]
        )

    @cached_property
    def MessageFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["MessageFieldMappings"]
        )

    @cached_property
    def AttachmentFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["AttachmentFieldMappings"]
        )

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QuipConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuipConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlackConfiguration:
    boto3_raw_data: "type_defs.SlackConfigurationTypeDef" = dataclasses.field()

    TeamId = field("TeamId")
    SecretArn = field("SecretArn")
    SlackEntityList = field("SlackEntityList")
    SinceCrawlDate = field("SinceCrawlDate")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    UseChangeLog = field("UseChangeLog")
    CrawlBotMessage = field("CrawlBotMessage")
    ExcludeArchived = field("ExcludeArchived")
    LookBackPeriod = field("LookBackPeriod")
    PrivateChannelFilter = field("PrivateChannelFilter")
    PublicChannelFilter = field("PublicChannelFilter")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlackConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlackConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateEntitiesToExperienceRequest:
    boto3_raw_data: "type_defs.AssociateEntitiesToExperienceRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IndexId = field("IndexId")

    @cached_property
    def EntityList(self):  # pragma: no cover
        return EntityConfiguration.make_many(self.boto3_raw_data["EntityList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateEntitiesToExperienceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateEntitiesToExperienceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateEntitiesFromExperienceRequest:
    boto3_raw_data: "type_defs.DisassociateEntitiesFromExperienceRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IndexId = field("IndexId")

    @cached_property
    def EntityList(self):  # pragma: no cover
        return EntityConfiguration.make_many(self.boto3_raw_data["EntityList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateEntitiesFromExperienceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateEntitiesFromExperienceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateEntitiesToExperienceResponse:
    boto3_raw_data: "type_defs.AssociateEntitiesToExperienceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedEntityList(self):  # pragma: no cover
        return FailedEntity.make_many(self.boto3_raw_data["FailedEntityList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateEntitiesToExperienceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateEntitiesToExperienceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePersonasToEntitiesResponse:
    boto3_raw_data: "type_defs.AssociatePersonasToEntitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedEntityList(self):  # pragma: no cover
        return FailedEntity.make_many(self.boto3_raw_data["FailedEntityList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociatePersonasToEntitiesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePersonasToEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessControlConfigurationResponse:
    boto3_raw_data: "type_defs.CreateAccessControlConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccessControlConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessControlConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceResponse:
    boto3_raw_data: "type_defs.CreateDataSourceResponseTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExperienceResponse:
    boto3_raw_data: "type_defs.CreateExperienceResponseTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExperienceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExperienceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFaqResponse:
    boto3_raw_data: "type_defs.CreateFaqResponseTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFaqResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFaqResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIndexResponse:
    boto3_raw_data: "type_defs.CreateIndexResponseTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQuerySuggestionsBlockListResponse:
    boto3_raw_data: "type_defs.CreateQuerySuggestionsBlockListResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateQuerySuggestionsBlockListResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQuerySuggestionsBlockListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThesaurusResponse:
    boto3_raw_data: "type_defs.CreateThesaurusResponseTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThesaurusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThesaurusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFaqResponse:
    boto3_raw_data: "type_defs.DescribeFaqResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")
    Name = field("Name")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def S3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["S3Path"])

    Status = field("Status")
    RoleArn = field("RoleArn")
    ErrorMessage = field("ErrorMessage")
    FileFormat = field("FileFormat")
    LanguageCode = field("LanguageCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFaqResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFaqResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQuerySuggestionsBlockListResponse:
    boto3_raw_data: "type_defs.DescribeQuerySuggestionsBlockListResponseTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    Status = field("Status")
    ErrorMessage = field("ErrorMessage")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def SourceS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SourceS3Path"])

    ItemCount = field("ItemCount")
    FileSizeBytes = field("FileSizeBytes")
    RoleArn = field("RoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeQuerySuggestionsBlockListResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQuerySuggestionsBlockListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThesaurusResponse:
    boto3_raw_data: "type_defs.DescribeThesaurusResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")
    Name = field("Name")
    Description = field("Description")
    Status = field("Status")
    ErrorMessage = field("ErrorMessage")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    RoleArn = field("RoleArn")

    @cached_property
    def SourceS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SourceS3Path"])

    FileSizeBytes = field("FileSizeBytes")
    TermCount = field("TermCount")
    SynonymRuleCount = field("SynonymRuleCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThesaurusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThesaurusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateEntitiesFromExperienceResponse:
    boto3_raw_data: "type_defs.DisassociateEntitiesFromExperienceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedEntityList(self):  # pragma: no cover
        return FailedEntity.make_many(self.boto3_raw_data["FailedEntityList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateEntitiesFromExperienceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateEntitiesFromExperienceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePersonasFromEntitiesResponse:
    boto3_raw_data: "type_defs.DisassociatePersonasFromEntitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedEntityList(self):  # pragma: no cover
        return FailedEntity.make_many(self.boto3_raw_data["FailedEntityList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociatePersonasFromEntitiesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociatePersonasFromEntitiesResponseTypeDef"]
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
class ListAccessControlConfigurationsResponse:
    boto3_raw_data: "type_defs.ListAccessControlConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessControlConfigurations(self):  # pragma: no cover
        return AccessControlConfigurationSummary.make_many(
            self.boto3_raw_data["AccessControlConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessControlConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessControlConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataSourceSyncJobResponse:
    boto3_raw_data: "type_defs.StartDataSourceSyncJobResponseTypeDef" = (
        dataclasses.field()
    )

    ExecutionId = field("ExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDataSourceSyncJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataSourceSyncJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePersonasToEntitiesRequest:
    boto3_raw_data: "type_defs.AssociatePersonasToEntitiesRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IndexId = field("IndexId")

    @cached_property
    def Personas(self):  # pragma: no cover
        return EntityPersonaConfiguration.make_many(self.boto3_raw_data["Personas"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociatePersonasToEntitiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePersonasToEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeSuggestionsDescribeConfig:
    boto3_raw_data: "type_defs.AttributeSuggestionsDescribeConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SuggestableConfigList(self):  # pragma: no cover
        return SuggestableConfig.make_many(self.boto3_raw_data["SuggestableConfigList"])

    AttributeSuggestionsMode = field("AttributeSuggestionsMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttributeSuggestionsDescribeConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeSuggestionsDescribeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeSuggestionsUpdateConfig:
    boto3_raw_data: "type_defs.AttributeSuggestionsUpdateConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SuggestableConfigList(self):  # pragma: no cover
        return SuggestableConfig.make_many(self.boto3_raw_data["SuggestableConfigList"])

    AttributeSuggestionsMode = field("AttributeSuggestionsMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AttributeSuggestionsUpdateConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeSuggestionsUpdateConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationConfigurationOutput:
    boto3_raw_data: "type_defs.AuthenticationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BasicAuthentication(self):  # pragma: no cover
        return BasicAuthenticationConfiguration.make_many(
            self.boto3_raw_data["BasicAuthentication"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthenticationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationConfiguration:
    boto3_raw_data: "type_defs.AuthenticationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def BasicAuthentication(self):  # pragma: no cover
        return BasicAuthenticationConfiguration.make_many(
            self.boto3_raw_data["BasicAuthentication"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDocumentRequest:
    boto3_raw_data: "type_defs.BatchDeleteDocumentRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    DocumentIdList = field("DocumentIdList")

    @cached_property
    def DataSourceSyncJobMetricTarget(self):  # pragma: no cover
        return DataSourceSyncJobMetricTarget.make_one(
            self.boto3_raw_data["DataSourceSyncJobMetricTarget"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDocumentResponse:
    boto3_raw_data: "type_defs.BatchDeleteDocumentResponseTypeDef" = dataclasses.field()

    @cached_property
    def FailedDocuments(self):  # pragma: no cover
        return BatchDeleteDocumentResponseFailedDocument.make_many(
            self.boto3_raw_data["FailedDocuments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteDocumentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteFeaturedResultsSetResponse:
    boto3_raw_data: "type_defs.BatchDeleteFeaturedResultsSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchDeleteFeaturedResultsSetError.make_many(
            self.boto3_raw_data["Errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteFeaturedResultsSetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteFeaturedResultsSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDocumentStatusResponse:
    boto3_raw_data: "type_defs.BatchGetDocumentStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchGetDocumentStatusResponseError.make_many(
            self.boto3_raw_data["Errors"]
        )

    @cached_property
    def DocumentStatusList(self):  # pragma: no cover
        return Status.make_many(self.boto3_raw_data["DocumentStatusList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetDocumentStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDocumentStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutDocumentResponse:
    boto3_raw_data: "type_defs.BatchPutDocumentResponseTypeDef" = dataclasses.field()

    @cached_property
    def FailedDocuments(self):  # pragma: no cover
        return BatchPutDocumentResponseFailedDocument.make_many(
            self.boto3_raw_data["FailedDocuments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutDocumentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClickFeedback:
    boto3_raw_data: "type_defs.ClickFeedbackTypeDef" = dataclasses.field()

    ResultId = field("ResultId")
    ClickTime = field("ClickTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClickFeedbackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClickFeedbackTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeValue:
    boto3_raw_data: "type_defs.DocumentAttributeValueTypeDef" = dataclasses.field()

    StringValue = field("StringValue")
    StringListValue = field("StringListValue")
    LongValue = field("LongValue")
    DateValue = field("DateValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeRange:
    boto3_raw_data: "type_defs.TimeRangeTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollapseConfiguration:
    boto3_raw_data: "type_defs.CollapseConfigurationTypeDef" = dataclasses.field()

    DocumentAttributeKey = field("DocumentAttributeKey")

    @cached_property
    def SortingConfigurations(self):  # pragma: no cover
        return SortingConfiguration.make_many(
            self.boto3_raw_data["SortingConfigurations"]
        )

    MissingAttributeKeyStrategy = field("MissingAttributeKeyStrategy")
    Expand = field("Expand")

    @cached_property
    def ExpandConfiguration(self):  # pragma: no cover
        return ExpandConfiguration.make_one(self.boto3_raw_data["ExpandConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CollapseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollapseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceAttachmentConfigurationOutput:
    boto3_raw_data: "type_defs.ConfluenceAttachmentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    CrawlAttachments = field("CrawlAttachments")

    @cached_property
    def AttachmentFieldMappings(self):  # pragma: no cover
        return ConfluenceAttachmentToIndexFieldMapping.make_many(
            self.boto3_raw_data["AttachmentFieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluenceAttachmentConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceAttachmentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceAttachmentConfiguration:
    boto3_raw_data: "type_defs.ConfluenceAttachmentConfigurationTypeDef" = (
        dataclasses.field()
    )

    CrawlAttachments = field("CrawlAttachments")

    @cached_property
    def AttachmentFieldMappings(self):  # pragma: no cover
        return ConfluenceAttachmentToIndexFieldMapping.make_many(
            self.boto3_raw_data["AttachmentFieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluenceAttachmentConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceAttachmentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceBlogConfigurationOutput:
    boto3_raw_data: "type_defs.ConfluenceBlogConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BlogFieldMappings(self):  # pragma: no cover
        return ConfluenceBlogToIndexFieldMapping.make_many(
            self.boto3_raw_data["BlogFieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluenceBlogConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceBlogConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceBlogConfiguration:
    boto3_raw_data: "type_defs.ConfluenceBlogConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def BlogFieldMappings(self):  # pragma: no cover
        return ConfluenceBlogToIndexFieldMapping.make_many(
            self.boto3_raw_data["BlogFieldMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfluenceBlogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceBlogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SharePointConfigurationOutput:
    boto3_raw_data: "type_defs.SharePointConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    SharePointVersion = field("SharePointVersion")
    Urls = field("Urls")
    SecretArn = field("SecretArn")
    CrawlAttachments = field("CrawlAttachments")
    UseChangeLog = field("UseChangeLog")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    DocumentTitleFieldName = field("DocumentTitleFieldName")
    DisableLocalGroups = field("DisableLocalGroups")

    @cached_property
    def SslCertificateS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SslCertificateS3Path"])

    AuthenticationType = field("AuthenticationType")

    @cached_property
    def ProxyConfiguration(self):  # pragma: no cover
        return ProxyConfiguration.make_one(self.boto3_raw_data["ProxyConfiguration"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SharePointConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SharePointConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SharePointConfiguration:
    boto3_raw_data: "type_defs.SharePointConfigurationTypeDef" = dataclasses.field()

    SharePointVersion = field("SharePointVersion")
    Urls = field("Urls")
    SecretArn = field("SecretArn")
    CrawlAttachments = field("CrawlAttachments")
    UseChangeLog = field("UseChangeLog")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    DocumentTitleFieldName = field("DocumentTitleFieldName")
    DisableLocalGroups = field("DisableLocalGroups")

    @cached_property
    def SslCertificateS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SslCertificateS3Path"])

    AuthenticationType = field("AuthenticationType")

    @cached_property
    def ProxyConfiguration(self):  # pragma: no cover
        return ProxyConfiguration.make_one(self.boto3_raw_data["ProxyConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SharePointConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SharePointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluencePageConfigurationOutput:
    boto3_raw_data: "type_defs.ConfluencePageConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PageFieldMappings(self):  # pragma: no cover
        return ConfluencePageToIndexFieldMapping.make_many(
            self.boto3_raw_data["PageFieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluencePageConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluencePageConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluencePageConfiguration:
    boto3_raw_data: "type_defs.ConfluencePageConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def PageFieldMappings(self):  # pragma: no cover
        return ConfluencePageToIndexFieldMapping.make_many(
            self.boto3_raw_data["PageFieldMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfluencePageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluencePageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceSpaceConfigurationOutput:
    boto3_raw_data: "type_defs.ConfluenceSpaceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    CrawlPersonalSpaces = field("CrawlPersonalSpaces")
    CrawlArchivedSpaces = field("CrawlArchivedSpaces")
    IncludeSpaces = field("IncludeSpaces")
    ExcludeSpaces = field("ExcludeSpaces")

    @cached_property
    def SpaceFieldMappings(self):  # pragma: no cover
        return ConfluenceSpaceToIndexFieldMapping.make_many(
            self.boto3_raw_data["SpaceFieldMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluenceSpaceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceSpaceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceSpaceConfiguration:
    boto3_raw_data: "type_defs.ConfluenceSpaceConfigurationTypeDef" = (
        dataclasses.field()
    )

    CrawlPersonalSpaces = field("CrawlPersonalSpaces")
    CrawlArchivedSpaces = field("CrawlArchivedSpaces")
    IncludeSpaces = field("IncludeSpaces")
    ExcludeSpaces = field("ExcludeSpaces")

    @cached_property
    def SpaceFieldMappings(self):  # pragma: no cover
        return ConfluenceSpaceToIndexFieldMapping.make_many(
            self.boto3_raw_data["SpaceFieldMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfluenceSpaceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceSpaceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpellCorrectedQuery:
    boto3_raw_data: "type_defs.SpellCorrectedQueryTypeDef" = dataclasses.field()

    SuggestedQueryText = field("SuggestedQueryText")

    @cached_property
    def Corrections(self):  # pragma: no cover
        return Correction.make_many(self.boto3_raw_data["Corrections"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpellCorrectedQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpellCorrectedQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchicalPrincipalOutput:
    boto3_raw_data: "type_defs.HierarchicalPrincipalOutputTypeDef" = dataclasses.field()

    @cached_property
    def PrincipalList(self):  # pragma: no cover
        return Principal.make_many(self.boto3_raw_data["PrincipalList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HierarchicalPrincipalOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchicalPrincipalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchicalPrincipal:
    boto3_raw_data: "type_defs.HierarchicalPrincipalTypeDef" = dataclasses.field()

    @cached_property
    def PrincipalList(self):  # pragma: no cover
        return Principal.make_many(self.boto3_raw_data["PrincipalList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HierarchicalPrincipalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchicalPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFaqRequest:
    boto3_raw_data: "type_defs.CreateFaqRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    Name = field("Name")

    @cached_property
    def S3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["S3Path"])

    RoleArn = field("RoleArn")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    FileFormat = field("FileFormat")
    ClientToken = field("ClientToken")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFaqRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFaqRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQuerySuggestionsBlockListRequest:
    boto3_raw_data: "type_defs.CreateQuerySuggestionsBlockListRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    Name = field("Name")

    @cached_property
    def SourceS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SourceS3Path"])

    RoleArn = field("RoleArn")
    Description = field("Description")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateQuerySuggestionsBlockListRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQuerySuggestionsBlockListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThesaurusRequest:
    boto3_raw_data: "type_defs.CreateThesaurusRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    Name = field("Name")
    RoleArn = field("RoleArn")

    @cached_property
    def SourceS3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["SourceS3Path"])

    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThesaurusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThesaurusRequestTypeDef"]
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

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateFeaturedResultsSetRequest:
    boto3_raw_data: "type_defs.CreateFeaturedResultsSetRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    FeaturedResultsSetName = field("FeaturedResultsSetName")
    Description = field("Description")
    ClientToken = field("ClientToken")
    Status = field("Status")
    QueryTexts = field("QueryTexts")

    @cached_property
    def FeaturedDocuments(self):  # pragma: no cover
        return FeaturedDocument.make_many(self.boto3_raw_data["FeaturedDocuments"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFeaturedResultsSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFeaturedResultsSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturedResultsSet:
    boto3_raw_data: "type_defs.FeaturedResultsSetTypeDef" = dataclasses.field()

    FeaturedResultsSetId = field("FeaturedResultsSetId")
    FeaturedResultsSetName = field("FeaturedResultsSetName")
    Description = field("Description")
    Status = field("Status")
    QueryTexts = field("QueryTexts")

    @cached_property
    def FeaturedDocuments(self):  # pragma: no cover
        return FeaturedDocument.make_many(self.boto3_raw_data["FeaturedDocuments"])

    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    CreationTimestamp = field("CreationTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeaturedResultsSetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturedResultsSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFeaturedResultsSetRequest:
    boto3_raw_data: "type_defs.UpdateFeaturedResultsSetRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    FeaturedResultsSetId = field("FeaturedResultsSetId")
    FeaturedResultsSetName = field("FeaturedResultsSetName")
    Description = field("Description")
    Status = field("Status")
    QueryTexts = field("QueryTexts")

    @cached_property
    def FeaturedDocuments(self):  # pragma: no cover
        return FeaturedDocument.make_many(self.boto3_raw_data["FeaturedDocuments"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFeaturedResultsSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFeaturedResultsSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserContext:
    boto3_raw_data: "type_defs.UserContextTypeDef" = dataclasses.field()

    Token = field("Token")
    UserId = field("UserId")
    Groups = field("Groups")

    @cached_property
    def DataSourceGroups(self):  # pragma: no cover
        return DataSourceGroup.make_many(self.boto3_raw_data["DataSourceGroups"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserContextTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesResponse:
    boto3_raw_data: "type_defs.ListDataSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def SummaryItems(self):  # pragma: no cover
        return DataSourceSummary.make_many(self.boto3_raw_data["SummaryItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceSyncJob:
    boto3_raw_data: "type_defs.DataSourceSyncJobTypeDef" = dataclasses.field()

    ExecutionId = field("ExecutionId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Status = field("Status")
    ErrorMessage = field("ErrorMessage")
    ErrorCode = field("ErrorCode")
    DataSourceErrorCode = field("DataSourceErrorCode")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return DataSourceSyncJobMetrics.make_one(self.boto3_raw_data["Metrics"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceSyncJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceSyncJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperiencesSummary:
    boto3_raw_data: "type_defs.ExperiencesSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    CreatedAt = field("CreatedAt")
    Status = field("Status")

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return ExperienceEndpoint.make_many(self.boto3_raw_data["Endpoints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperiencesSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperiencesSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFeaturedResultsSetResponse:
    boto3_raw_data: "type_defs.DescribeFeaturedResultsSetResponseTypeDef" = (
        dataclasses.field()
    )

    FeaturedResultsSetId = field("FeaturedResultsSetId")
    FeaturedResultsSetName = field("FeaturedResultsSetName")
    Description = field("Description")
    Status = field("Status")
    QueryTexts = field("QueryTexts")

    @cached_property
    def FeaturedDocumentsWithMetadata(self):  # pragma: no cover
        return FeaturedDocumentWithMetadata.make_many(
            self.boto3_raw_data["FeaturedDocumentsWithMetadata"]
        )

    @cached_property
    def FeaturedDocumentsMissing(self):  # pragma: no cover
        return FeaturedDocumentMissing.make_many(
            self.boto3_raw_data["FeaturedDocumentsMissing"]
        )

    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFeaturedResultsSetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFeaturedResultsSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePrincipalMappingResponse:
    boto3_raw_data: "type_defs.DescribePrincipalMappingResponseTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    DataSourceId = field("DataSourceId")
    GroupId = field("GroupId")

    @cached_property
    def GroupOrderingIdSummaries(self):  # pragma: no cover
        return GroupOrderingIdSummary.make_many(
            self.boto3_raw_data["GroupOrderingIdSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePrincipalMappingResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePrincipalMappingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeConditionOutput:
    boto3_raw_data: "type_defs.DocumentAttributeConditionOutputTypeDef" = (
        dataclasses.field()
    )

    ConditionDocumentAttributeKey = field("ConditionDocumentAttributeKey")
    Operator = field("Operator")

    @cached_property
    def ConditionOnValue(self):  # pragma: no cover
        return DocumentAttributeValueOutput.make_one(
            self.boto3_raw_data["ConditionOnValue"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentAttributeConditionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeOutput:
    boto3_raw_data: "type_defs.DocumentAttributeOutputTypeDef" = dataclasses.field()

    Key = field("Key")

    @cached_property
    def Value(self):  # pragma: no cover
        return DocumentAttributeValueOutput.make_one(self.boto3_raw_data["Value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeTargetOutput:
    boto3_raw_data: "type_defs.DocumentAttributeTargetOutputTypeDef" = (
        dataclasses.field()
    )

    TargetDocumentAttributeKey = field("TargetDocumentAttributeKey")
    TargetDocumentAttributeValueDeletion = field("TargetDocumentAttributeValueDeletion")

    @cached_property
    def TargetDocumentAttributeValue(self):  # pragma: no cover
        return DocumentAttributeValueOutput.make_one(
            self.boto3_raw_data["TargetDocumentAttributeValue"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentAttributeTargetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeValueCountPair:
    boto3_raw_data: "type_defs.DocumentAttributeValueCountPairTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentAttributeValue(self):  # pragma: no cover
        return DocumentAttributeValueOutput.make_one(
            self.boto3_raw_data["DocumentAttributeValue"]
        )

    Count = field("Count")
    FacetResults = field("FacetResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentAttributeValueCountPairTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeValueCountPairTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentMetadataConfigurationOutput:
    boto3_raw_data: "type_defs.DocumentMetadataConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Type = field("Type")

    @cached_property
    def Relevance(self):  # pragma: no cover
        return RelevanceOutput.make_one(self.boto3_raw_data["Relevance"])

    @cached_property
    def Search(self):  # pragma: no cover
        return Search.make_one(self.boto3_raw_data["Search"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentMetadataConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentMetadataConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataSourceConfigurationOutput:
    boto3_raw_data: "type_defs.S3DataSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    BucketName = field("BucketName")
    InclusionPrefixes = field("InclusionPrefixes")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def DocumentsMetadataConfiguration(self):  # pragma: no cover
        return DocumentsMetadataConfiguration.make_one(
            self.boto3_raw_data["DocumentsMetadataConfiguration"]
        )

    @cached_property
    def AccessControlListConfiguration(self):  # pragma: no cover
        return AccessControlListConfiguration.make_one(
            self.boto3_raw_data["AccessControlListConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3DataSourceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DataSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataSourceConfiguration:
    boto3_raw_data: "type_defs.S3DataSourceConfigurationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    InclusionPrefixes = field("InclusionPrefixes")
    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def DocumentsMetadataConfiguration(self):  # pragma: no cover
        return DocumentsMetadataConfiguration.make_one(
            self.boto3_raw_data["DocumentsMetadataConfiguration"]
        )

    @cached_property
    def AccessControlListConfiguration(self):  # pragma: no cover
        return AccessControlListConfiguration.make_one(
            self.boto3_raw_data["AccessControlListConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DataSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DataSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperienceEntitiesSummary:
    boto3_raw_data: "type_defs.ExperienceEntitiesSummaryTypeDef" = dataclasses.field()

    EntityId = field("EntityId")
    EntityType = field("EntityType")

    @cached_property
    def DisplayData(self):  # pragma: no cover
        return EntityDisplayData.make_one(self.boto3_raw_data["DisplayData"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperienceEntitiesSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperienceEntitiesSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperienceConfigurationOutput:
    boto3_raw_data: "type_defs.ExperienceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContentSourceConfiguration(self):  # pragma: no cover
        return ContentSourceConfigurationOutput.make_one(
            self.boto3_raw_data["ContentSourceConfiguration"]
        )

    @cached_property
    def UserIdentityConfiguration(self):  # pragma: no cover
        return UserIdentityConfiguration.make_one(
            self.boto3_raw_data["UserIdentityConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExperienceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperienceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperienceConfiguration:
    boto3_raw_data: "type_defs.ExperienceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ContentSourceConfiguration(self):  # pragma: no cover
        return ContentSourceConfiguration.make_one(
            self.boto3_raw_data["ContentSourceConfiguration"]
        )

    @cached_property
    def UserIdentityConfiguration(self):  # pragma: no cover
        return UserIdentityConfiguration.make_one(
            self.boto3_raw_data["UserIdentityConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperienceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperienceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFaqsResponse:
    boto3_raw_data: "type_defs.ListFaqsResponseTypeDef" = dataclasses.field()

    @cached_property
    def FaqSummaryItems(self):  # pragma: no cover
        return FaqSummary.make_many(self.boto3_raw_data["FaqSummaryItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFaqsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFaqsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFeaturedResultsSetsResponse:
    boto3_raw_data: "type_defs.ListFeaturedResultsSetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FeaturedResultsSetSummaryItems(self):  # pragma: no cover
        return FeaturedResultsSetSummary.make_many(
            self.boto3_raw_data["FeaturedResultsSetSummaryItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFeaturedResultsSetsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFeaturedResultsSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSnapshotsResponse:
    boto3_raw_data: "type_defs.GetSnapshotsResponseTypeDef" = dataclasses.field()

    @cached_property
    def SnapShotTimeFilter(self):  # pragma: no cover
        return TimeRangeOutput.make_one(self.boto3_raw_data["SnapShotTimeFilter"])

    SnapshotsDataHeader = field("SnapshotsDataHeader")
    SnapshotsData = field("SnapshotsData")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSnapshotsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSnapshotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupMembers:
    boto3_raw_data: "type_defs.GroupMembersTypeDef" = dataclasses.field()

    @cached_property
    def MemberGroups(self):  # pragma: no cover
        return MemberGroup.make_many(self.boto3_raw_data["MemberGroups"])

    @cached_property
    def MemberUsers(self):  # pragma: no cover
        return MemberUser.make_many(self.boto3_raw_data["MemberUsers"])

    @cached_property
    def S3PathforGroupMembers(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["S3PathforGroupMembers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupMembersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupMembersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsOlderThanOrderingIdResponse:
    boto3_raw_data: "type_defs.ListGroupsOlderThanOrderingIdResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GroupsSummaries(self):  # pragma: no cover
        return GroupSummary.make_many(self.boto3_raw_data["GroupsSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGroupsOlderThanOrderingIdResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsOlderThanOrderingIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextWithHighlights:
    boto3_raw_data: "type_defs.TextWithHighlightsTypeDef" = dataclasses.field()

    Text = field("Text")

    @cached_property
    def Highlights(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Highlights"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextWithHighlightsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextWithHighlightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndicesResponse:
    boto3_raw_data: "type_defs.ListIndicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def IndexConfigurationSummaryItems(self):  # pragma: no cover
        return IndexConfigurationSummary.make_many(
            self.boto3_raw_data["IndexConfigurationSummaryItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexStatistics:
    boto3_raw_data: "type_defs.IndexStatisticsTypeDef" = dataclasses.field()

    @cached_property
    def FaqStatistics(self):  # pragma: no cover
        return FaqStatistics.make_one(self.boto3_raw_data["FaqStatistics"])

    @cached_property
    def TextDocumentStatistics(self):  # pragma: no cover
        return TextDocumentStatistics.make_one(
            self.boto3_raw_data["TextDocumentStatistics"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserTokenConfiguration:
    boto3_raw_data: "type_defs.UserTokenConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def JwtTokenTypeConfiguration(self):  # pragma: no cover
        return JwtTokenTypeConfiguration.make_one(
            self.boto3_raw_data["JwtTokenTypeConfiguration"]
        )

    @cached_property
    def JsonTokenTypeConfiguration(self):  # pragma: no cover
        return JsonTokenTypeConfiguration.make_one(
            self.boto3_raw_data["JsonTokenTypeConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserTokenConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserTokenConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntityPersonasResponse:
    boto3_raw_data: "type_defs.ListEntityPersonasResponseTypeDef" = dataclasses.field()

    @cached_property
    def SummaryItems(self):  # pragma: no cover
        return PersonasSummary.make_many(self.boto3_raw_data["SummaryItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntityPersonasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntityPersonasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQuerySuggestionsBlockListsResponse:
    boto3_raw_data: "type_defs.ListQuerySuggestionsBlockListsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BlockListSummaryItems(self):  # pragma: no cover
        return QuerySuggestionsBlockListSummary.make_many(
            self.boto3_raw_data["BlockListSummaryItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQuerySuggestionsBlockListsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQuerySuggestionsBlockListsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThesauriResponse:
    boto3_raw_data: "type_defs.ListThesauriResponseTypeDef" = dataclasses.field()

    @cached_property
    def ThesaurusSummaryItems(self):  # pragma: no cover
        return ThesaurusSummary.make_many(self.boto3_raw_data["ThesaurusSummaryItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThesauriResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThesauriResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UrlsOutput:
    boto3_raw_data: "type_defs.UrlsOutputTypeDef" = dataclasses.field()

    @cached_property
    def SeedUrlConfiguration(self):  # pragma: no cover
        return SeedUrlConfigurationOutput.make_one(
            self.boto3_raw_data["SeedUrlConfiguration"]
        )

    @cached_property
    def SiteMapsConfiguration(self):  # pragma: no cover
        return SiteMapsConfigurationOutput.make_one(
            self.boto3_raw_data["SiteMapsConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UrlsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UrlsOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Urls:
    boto3_raw_data: "type_defs.UrlsTypeDef" = dataclasses.field()

    @cached_property
    def SeedUrlConfiguration(self):  # pragma: no cover
        return SeedUrlConfiguration.make_one(
            self.boto3_raw_data["SeedUrlConfiguration"]
        )

    @cached_property
    def SiteMapsConfiguration(self):  # pragma: no cover
        return SiteMapsConfiguration.make_one(
            self.boto3_raw_data["SiteMapsConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UrlsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UrlsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestionTextWithHighlights:
    boto3_raw_data: "type_defs.SuggestionTextWithHighlightsTypeDef" = (
        dataclasses.field()
    )

    Text = field("Text")

    @cached_property
    def Highlights(self):  # pragma: no cover
        return SuggestionHighlight.make_many(self.boto3_raw_data["Highlights"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuggestionTextWithHighlightsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuggestionTextWithHighlightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableRow:
    boto3_raw_data: "type_defs.TableRowTypeDef" = dataclasses.field()

    @cached_property
    def Cells(self):  # pragma: no cover
        return TableCell.make_many(self.boto3_raw_data["Cells"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableRowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableRowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseConfigurationOutput:
    boto3_raw_data: "type_defs.DatabaseConfigurationOutputTypeDef" = dataclasses.field()

    DatabaseEngineType = field("DatabaseEngineType")

    @cached_property
    def ConnectionConfiguration(self):  # pragma: no cover
        return ConnectionConfiguration.make_one(
            self.boto3_raw_data["ConnectionConfiguration"]
        )

    @cached_property
    def ColumnConfiguration(self):  # pragma: no cover
        return ColumnConfigurationOutput.make_one(
            self.boto3_raw_data["ColumnConfiguration"]
        )

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @cached_property
    def AclConfiguration(self):  # pragma: no cover
        return AclConfiguration.make_one(self.boto3_raw_data["AclConfiguration"])

    @cached_property
    def SqlConfiguration(self):  # pragma: no cover
        return SqlConfiguration.make_one(self.boto3_raw_data["SqlConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseConfiguration:
    boto3_raw_data: "type_defs.DatabaseConfigurationTypeDef" = dataclasses.field()

    DatabaseEngineType = field("DatabaseEngineType")

    @cached_property
    def ConnectionConfiguration(self):  # pragma: no cover
        return ConnectionConfiguration.make_one(
            self.boto3_raw_data["ConnectionConfiguration"]
        )

    @cached_property
    def ColumnConfiguration(self):  # pragma: no cover
        return ColumnConfiguration.make_one(self.boto3_raw_data["ColumnConfiguration"])

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @cached_property
    def AclConfiguration(self):  # pragma: no cover
        return AclConfiguration.make_one(self.boto3_raw_data["AclConfiguration"])

    @cached_property
    def SqlConfiguration(self):  # pragma: no cover
        return SqlConfiguration.make_one(self.boto3_raw_data["SqlConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceKnowledgeArticleConfigurationOutput:
    boto3_raw_data: "type_defs.SalesforceKnowledgeArticleConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    IncludedStates = field("IncludedStates")

    @cached_property
    def StandardKnowledgeArticleTypeConfiguration(self):  # pragma: no cover
        return SalesforceStandardKnowledgeArticleTypeConfigurationOutput.make_one(
            self.boto3_raw_data["StandardKnowledgeArticleTypeConfiguration"]
        )

    @cached_property
    def CustomKnowledgeArticleTypeConfigurations(self):  # pragma: no cover
        return SalesforceCustomKnowledgeArticleTypeConfigurationOutput.make_many(
            self.boto3_raw_data["CustomKnowledgeArticleTypeConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceKnowledgeArticleConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceKnowledgeArticleConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceKnowledgeArticleConfiguration:
    boto3_raw_data: "type_defs.SalesforceKnowledgeArticleConfigurationTypeDef" = (
        dataclasses.field()
    )

    IncludedStates = field("IncludedStates")

    @cached_property
    def StandardKnowledgeArticleTypeConfiguration(self):  # pragma: no cover
        return SalesforceStandardKnowledgeArticleTypeConfiguration.make_one(
            self.boto3_raw_data["StandardKnowledgeArticleTypeConfiguration"]
        )

    @cached_property
    def CustomKnowledgeArticleTypeConfigurations(self):  # pragma: no cover
        return SalesforceCustomKnowledgeArticleTypeConfiguration.make_many(
            self.boto3_raw_data["CustomKnowledgeArticleTypeConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceKnowledgeArticleConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceKnowledgeArticleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNowConfigurationOutput:
    boto3_raw_data: "type_defs.ServiceNowConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    HostUrl = field("HostUrl")
    SecretArn = field("SecretArn")
    ServiceNowBuildVersion = field("ServiceNowBuildVersion")

    @cached_property
    def KnowledgeArticleConfiguration(self):  # pragma: no cover
        return ServiceNowKnowledgeArticleConfigurationOutput.make_one(
            self.boto3_raw_data["KnowledgeArticleConfiguration"]
        )

    @cached_property
    def ServiceCatalogConfiguration(self):  # pragma: no cover
        return ServiceNowServiceCatalogConfigurationOutput.make_one(
            self.boto3_raw_data["ServiceCatalogConfiguration"]
        )

    AuthenticationType = field("AuthenticationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServiceNowConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNowConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNowConfiguration:
    boto3_raw_data: "type_defs.ServiceNowConfigurationTypeDef" = dataclasses.field()

    HostUrl = field("HostUrl")
    SecretArn = field("SecretArn")
    ServiceNowBuildVersion = field("ServiceNowBuildVersion")

    @cached_property
    def KnowledgeArticleConfiguration(self):  # pragma: no cover
        return ServiceNowKnowledgeArticleConfiguration.make_one(
            self.boto3_raw_data["KnowledgeArticleConfiguration"]
        )

    @cached_property
    def ServiceCatalogConfiguration(self):  # pragma: no cover
        return ServiceNowServiceCatalogConfiguration.make_one(
            self.boto3_raw_data["ServiceCatalogConfiguration"]
        )

    AuthenticationType = field("AuthenticationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceNowConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNowConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitHubConfigurationOutput:
    boto3_raw_data: "type_defs.GitHubConfigurationOutputTypeDef" = dataclasses.field()

    SecretArn = field("SecretArn")

    @cached_property
    def SaaSConfiguration(self):  # pragma: no cover
        return SaaSConfiguration.make_one(self.boto3_raw_data["SaaSConfiguration"])

    @cached_property
    def OnPremiseConfiguration(self):  # pragma: no cover
        return OnPremiseConfiguration.make_one(
            self.boto3_raw_data["OnPremiseConfiguration"]
        )

    Type = field("Type")
    UseChangeLog = field("UseChangeLog")

    @cached_property
    def GitHubDocumentCrawlProperties(self):  # pragma: no cover
        return GitHubDocumentCrawlProperties.make_one(
            self.boto3_raw_data["GitHubDocumentCrawlProperties"]
        )

    RepositoryFilter = field("RepositoryFilter")
    InclusionFolderNamePatterns = field("InclusionFolderNamePatterns")
    InclusionFileTypePatterns = field("InclusionFileTypePatterns")
    InclusionFileNamePatterns = field("InclusionFileNamePatterns")
    ExclusionFolderNamePatterns = field("ExclusionFolderNamePatterns")
    ExclusionFileTypePatterns = field("ExclusionFileTypePatterns")
    ExclusionFileNamePatterns = field("ExclusionFileNamePatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @cached_property
    def GitHubRepositoryConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubRepositoryConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubCommitConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubCommitConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubIssueDocumentConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubIssueDocumentConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubIssueCommentConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubIssueCommentConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubIssueAttachmentConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubIssueAttachmentConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubPullRequestCommentConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubPullRequestCommentConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubPullRequestDocumentConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubPullRequestDocumentConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubPullRequestDocumentAttachmentConfigurationFieldMappings(
        self,
    ):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data[
                "GitHubPullRequestDocumentAttachmentConfigurationFieldMappings"
            ]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitHubConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitHubConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitHubConfiguration:
    boto3_raw_data: "type_defs.GitHubConfigurationTypeDef" = dataclasses.field()

    SecretArn = field("SecretArn")

    @cached_property
    def SaaSConfiguration(self):  # pragma: no cover
        return SaaSConfiguration.make_one(self.boto3_raw_data["SaaSConfiguration"])

    @cached_property
    def OnPremiseConfiguration(self):  # pragma: no cover
        return OnPremiseConfiguration.make_one(
            self.boto3_raw_data["OnPremiseConfiguration"]
        )

    Type = field("Type")
    UseChangeLog = field("UseChangeLog")

    @cached_property
    def GitHubDocumentCrawlProperties(self):  # pragma: no cover
        return GitHubDocumentCrawlProperties.make_one(
            self.boto3_raw_data["GitHubDocumentCrawlProperties"]
        )

    RepositoryFilter = field("RepositoryFilter")
    InclusionFolderNamePatterns = field("InclusionFolderNamePatterns")
    InclusionFileTypePatterns = field("InclusionFileTypePatterns")
    InclusionFileNamePatterns = field("InclusionFileNamePatterns")
    ExclusionFolderNamePatterns = field("ExclusionFolderNamePatterns")
    ExclusionFileTypePatterns = field("ExclusionFileTypePatterns")
    ExclusionFileNamePatterns = field("ExclusionFileNamePatterns")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @cached_property
    def GitHubRepositoryConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubRepositoryConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubCommitConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubCommitConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubIssueDocumentConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubIssueDocumentConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubIssueCommentConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubIssueCommentConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubIssueAttachmentConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubIssueAttachmentConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubPullRequestCommentConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubPullRequestCommentConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubPullRequestDocumentConfigurationFieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["GitHubPullRequestDocumentConfigurationFieldMappings"]
        )

    @cached_property
    def GitHubPullRequestDocumentAttachmentConfigurationFieldMappings(
        self,
    ):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data[
                "GitHubPullRequestDocumentAttachmentConfigurationFieldMappings"
            ]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitHubConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitHubConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OneDriveConfigurationOutput:
    boto3_raw_data: "type_defs.OneDriveConfigurationOutputTypeDef" = dataclasses.field()

    TenantDomain = field("TenantDomain")
    SecretArn = field("SecretArn")

    @cached_property
    def OneDriveUsers(self):  # pragma: no cover
        return OneDriveUsersOutput.make_one(self.boto3_raw_data["OneDriveUsers"])

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    DisableLocalGroups = field("DisableLocalGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OneDriveConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OneDriveConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OneDriveConfiguration:
    boto3_raw_data: "type_defs.OneDriveConfigurationTypeDef" = dataclasses.field()

    TenantDomain = field("TenantDomain")
    SecretArn = field("SecretArn")

    @cached_property
    def OneDriveUsers(self):  # pragma: no cover
        return OneDriveUsers.make_one(self.boto3_raw_data["OneDriveUsers"])

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def FieldMappings(self):  # pragma: no cover
        return DataSourceToIndexFieldMapping.make_many(
            self.boto3_raw_data["FieldMappings"]
        )

    DisableLocalGroups = field("DisableLocalGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OneDriveConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OneDriveConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQuerySuggestionsConfigResponse:
    boto3_raw_data: "type_defs.DescribeQuerySuggestionsConfigResponseTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    Status = field("Status")
    QueryLogLookBackWindowInDays = field("QueryLogLookBackWindowInDays")
    IncludeQueriesWithoutUserInformation = field("IncludeQueriesWithoutUserInformation")
    MinimumNumberOfQueryingUsers = field("MinimumNumberOfQueryingUsers")
    MinimumQueryCount = field("MinimumQueryCount")
    LastSuggestionsBuildTime = field("LastSuggestionsBuildTime")
    LastClearTime = field("LastClearTime")
    TotalSuggestionsCount = field("TotalSuggestionsCount")

    @cached_property
    def AttributeSuggestionsConfig(self):  # pragma: no cover
        return AttributeSuggestionsDescribeConfig.make_one(
            self.boto3_raw_data["AttributeSuggestionsConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeQuerySuggestionsConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQuerySuggestionsConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQuerySuggestionsConfigRequest:
    boto3_raw_data: "type_defs.UpdateQuerySuggestionsConfigRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    Mode = field("Mode")
    QueryLogLookBackWindowInDays = field("QueryLogLookBackWindowInDays")
    IncludeQueriesWithoutUserInformation = field("IncludeQueriesWithoutUserInformation")
    MinimumNumberOfQueryingUsers = field("MinimumNumberOfQueryingUsers")
    MinimumQueryCount = field("MinimumQueryCount")

    @cached_property
    def AttributeSuggestionsConfig(self):  # pragma: no cover
        return AttributeSuggestionsUpdateConfig.make_one(
            self.boto3_raw_data["AttributeSuggestionsConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateQuerySuggestionsConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQuerySuggestionsConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitFeedbackRequest:
    boto3_raw_data: "type_defs.SubmitFeedbackRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    QueryId = field("QueryId")

    @cached_property
    def ClickFeedbackItems(self):  # pragma: no cover
        return ClickFeedback.make_many(self.boto3_raw_data["ClickFeedbackItems"])

    @cached_property
    def RelevanceFeedbackItems(self):  # pragma: no cover
        return RelevanceFeedback.make_many(
            self.boto3_raw_data["RelevanceFeedbackItems"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubmitFeedbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeCondition:
    boto3_raw_data: "type_defs.DocumentAttributeConditionTypeDef" = dataclasses.field()

    ConditionDocumentAttributeKey = field("ConditionDocumentAttributeKey")
    Operator = field("Operator")

    @cached_property
    def ConditionOnValue(self):  # pragma: no cover
        return DocumentAttributeValue.make_one(self.boto3_raw_data["ConditionOnValue"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeTarget:
    boto3_raw_data: "type_defs.DocumentAttributeTargetTypeDef" = dataclasses.field()

    TargetDocumentAttributeKey = field("TargetDocumentAttributeKey")
    TargetDocumentAttributeValueDeletion = field("TargetDocumentAttributeValueDeletion")

    @cached_property
    def TargetDocumentAttributeValue(self):  # pragma: no cover
        return DocumentAttributeValue.make_one(
            self.boto3_raw_data["TargetDocumentAttributeValue"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceConfigurationOutput:
    boto3_raw_data: "type_defs.ConfluenceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    ServerUrl = field("ServerUrl")
    SecretArn = field("SecretArn")
    Version = field("Version")

    @cached_property
    def SpaceConfiguration(self):  # pragma: no cover
        return ConfluenceSpaceConfigurationOutput.make_one(
            self.boto3_raw_data["SpaceConfiguration"]
        )

    @cached_property
    def PageConfiguration(self):  # pragma: no cover
        return ConfluencePageConfigurationOutput.make_one(
            self.boto3_raw_data["PageConfiguration"]
        )

    @cached_property
    def BlogConfiguration(self):  # pragma: no cover
        return ConfluenceBlogConfigurationOutput.make_one(
            self.boto3_raw_data["BlogConfiguration"]
        )

    @cached_property
    def AttachmentConfiguration(self):  # pragma: no cover
        return ConfluenceAttachmentConfigurationOutput.make_one(
            self.boto3_raw_data["AttachmentConfiguration"]
        )

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def ProxyConfiguration(self):  # pragma: no cover
        return ProxyConfiguration.make_one(self.boto3_raw_data["ProxyConfiguration"])

    AuthenticationType = field("AuthenticationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfluenceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceConfiguration:
    boto3_raw_data: "type_defs.ConfluenceConfigurationTypeDef" = dataclasses.field()

    ServerUrl = field("ServerUrl")
    SecretArn = field("SecretArn")
    Version = field("Version")

    @cached_property
    def SpaceConfiguration(self):  # pragma: no cover
        return ConfluenceSpaceConfiguration.make_one(
            self.boto3_raw_data["SpaceConfiguration"]
        )

    @cached_property
    def PageConfiguration(self):  # pragma: no cover
        return ConfluencePageConfiguration.make_one(
            self.boto3_raw_data["PageConfiguration"]
        )

    @cached_property
    def BlogConfiguration(self):  # pragma: no cover
        return ConfluenceBlogConfiguration.make_one(
            self.boto3_raw_data["BlogConfiguration"]
        )

    @cached_property
    def AttachmentConfiguration(self):  # pragma: no cover
        return ConfluenceAttachmentConfiguration.make_one(
            self.boto3_raw_data["AttachmentConfiguration"]
        )

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    InclusionPatterns = field("InclusionPatterns")
    ExclusionPatterns = field("ExclusionPatterns")

    @cached_property
    def ProxyConfiguration(self):  # pragma: no cover
        return ProxyConfiguration.make_one(self.boto3_raw_data["ProxyConfiguration"])

    AuthenticationType = field("AuthenticationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfluenceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessControlConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeAccessControlConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Description = field("Description")
    ErrorMessage = field("ErrorMessage")

    @cached_property
    def AccessControlList(self):  # pragma: no cover
        return Principal.make_many(self.boto3_raw_data["AccessControlList"])

    @cached_property
    def HierarchicalAccessControlList(self):  # pragma: no cover
        return HierarchicalPrincipalOutput.make_many(
            self.boto3_raw_data["HierarchicalAccessControlList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccessControlConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessControlConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFeaturedResultsSetResponse:
    boto3_raw_data: "type_defs.CreateFeaturedResultsSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FeaturedResultsSet(self):  # pragma: no cover
        return FeaturedResultsSet.make_one(self.boto3_raw_data["FeaturedResultsSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFeaturedResultsSetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFeaturedResultsSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFeaturedResultsSetResponse:
    boto3_raw_data: "type_defs.UpdateFeaturedResultsSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FeaturedResultsSet(self):  # pragma: no cover
        return FeaturedResultsSet.make_one(self.boto3_raw_data["FeaturedResultsSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFeaturedResultsSetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFeaturedResultsSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceSyncJobsResponse:
    boto3_raw_data: "type_defs.ListDataSourceSyncJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def History(self):  # pragma: no cover
        return DataSourceSyncJob.make_many(self.boto3_raw_data["History"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSourceSyncJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceSyncJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperiencesResponse:
    boto3_raw_data: "type_defs.ListExperiencesResponseTypeDef" = dataclasses.field()

    @cached_property
    def SummaryItems(self):  # pragma: no cover
        return ExperiencesSummary.make_many(self.boto3_raw_data["SummaryItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExperiencesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperiencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HookConfigurationOutput:
    boto3_raw_data: "type_defs.HookConfigurationOutputTypeDef" = dataclasses.field()

    LambdaArn = field("LambdaArn")
    S3Bucket = field("S3Bucket")

    @cached_property
    def InvocationCondition(self):  # pragma: no cover
        return DocumentAttributeConditionOutput.make_one(
            self.boto3_raw_data["InvocationCondition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HookConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HookConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveResultItem:
    boto3_raw_data: "type_defs.RetrieveResultItemTypeDef" = dataclasses.field()

    Id = field("Id")
    DocumentId = field("DocumentId")
    DocumentTitle = field("DocumentTitle")
    Content = field("Content")
    DocumentURI = field("DocumentURI")

    @cached_property
    def DocumentAttributes(self):  # pragma: no cover
        return DocumentAttributeOutput.make_many(
            self.boto3_raw_data["DocumentAttributes"]
        )

    @cached_property
    def ScoreAttributes(self):  # pragma: no cover
        return ScoreAttributes.make_one(self.boto3_raw_data["ScoreAttributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceDocument:
    boto3_raw_data: "type_defs.SourceDocumentTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    SuggestionAttributes = field("SuggestionAttributes")

    @cached_property
    def AdditionalAttributes(self):  # pragma: no cover
        return DocumentAttributeOutput.make_many(
            self.boto3_raw_data["AdditionalAttributes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceDocumentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineCustomDocumentEnrichmentConfigurationOutput:
    boto3_raw_data: (
        "type_defs.InlineCustomDocumentEnrichmentConfigurationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Condition(self):  # pragma: no cover
        return DocumentAttributeConditionOutput.make_one(
            self.boto3_raw_data["Condition"]
        )

    @cached_property
    def Target(self):  # pragma: no cover
        return DocumentAttributeTargetOutput.make_one(self.boto3_raw_data["Target"])

    DocumentContentDeletion = field("DocumentContentDeletion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InlineCustomDocumentEnrichmentConfigurationOutputTypeDef"
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
                "type_defs.InlineCustomDocumentEnrichmentConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FacetResult:
    boto3_raw_data: "type_defs.FacetResultTypeDef" = dataclasses.field()

    DocumentAttributeKey = field("DocumentAttributeKey")
    DocumentAttributeValueType = field("DocumentAttributeValueType")

    @cached_property
    def DocumentAttributeValueCountPairs(self):  # pragma: no cover
        return DocumentAttributeValueCountPair.make_many(
            self.boto3_raw_data["DocumentAttributeValueCountPairs"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FacetResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FacetResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperienceEntitiesResponse:
    boto3_raw_data: "type_defs.ListExperienceEntitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SummaryItems(self):  # pragma: no cover
        return ExperienceEntitiesSummary.make_many(self.boto3_raw_data["SummaryItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExperienceEntitiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperienceEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExperienceResponse:
    boto3_raw_data: "type_defs.DescribeExperienceResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")
    Name = field("Name")

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return ExperienceEndpoint.make_many(self.boto3_raw_data["Endpoints"])

    @cached_property
    def Configuration(self):  # pragma: no cover
        return ExperienceConfigurationOutput.make_one(
            self.boto3_raw_data["Configuration"]
        )

    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    Description = field("Description")
    Status = field("Status")
    RoleArn = field("RoleArn")
    ErrorMessage = field("ErrorMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExperienceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExperienceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPrincipalMappingRequest:
    boto3_raw_data: "type_defs.PutPrincipalMappingRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    GroupId = field("GroupId")

    @cached_property
    def GroupMembers(self):  # pragma: no cover
        return GroupMembers.make_one(self.boto3_raw_data["GroupMembers"])

    DataSourceId = field("DataSourceId")
    OrderingId = field("OrderingId")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPrincipalMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPrincipalMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalResultAttributeValue:
    boto3_raw_data: "type_defs.AdditionalResultAttributeValueTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TextWithHighlightsValue(self):  # pragma: no cover
        return TextWithHighlights.make_one(
            self.boto3_raw_data["TextWithHighlightsValue"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdditionalResultAttributeValueTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalResultAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpandedResultItem:
    boto3_raw_data: "type_defs.ExpandedResultItemTypeDef" = dataclasses.field()

    Id = field("Id")
    DocumentId = field("DocumentId")

    @cached_property
    def DocumentTitle(self):  # pragma: no cover
        return TextWithHighlights.make_one(self.boto3_raw_data["DocumentTitle"])

    @cached_property
    def DocumentExcerpt(self):  # pragma: no cover
        return TextWithHighlights.make_one(self.boto3_raw_data["DocumentExcerpt"])

    DocumentURI = field("DocumentURI")

    @cached_property
    def DocumentAttributes(self):  # pragma: no cover
        return DocumentAttributeOutput.make_many(
            self.boto3_raw_data["DocumentAttributes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpandedResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpandedResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIndexRequest:
    boto3_raw_data: "type_defs.CreateIndexRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RoleArn = field("RoleArn")
    Edition = field("Edition")

    @cached_property
    def ServerSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["ServerSideEncryptionConfiguration"]
        )

    Description = field("Description")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def UserTokenConfigurations(self):  # pragma: no cover
        return UserTokenConfiguration.make_many(
            self.boto3_raw_data["UserTokenConfigurations"]
        )

    UserContextPolicy = field("UserContextPolicy")

    @cached_property
    def UserGroupResolutionConfiguration(self):  # pragma: no cover
        return UserGroupResolutionConfiguration.make_one(
            self.boto3_raw_data["UserGroupResolutionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIndexResponse:
    boto3_raw_data: "type_defs.DescribeIndexResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Edition = field("Edition")
    RoleArn = field("RoleArn")

    @cached_property
    def ServerSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["ServerSideEncryptionConfiguration"]
        )

    Status = field("Status")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def DocumentMetadataConfigurations(self):  # pragma: no cover
        return DocumentMetadataConfigurationOutput.make_many(
            self.boto3_raw_data["DocumentMetadataConfigurations"]
        )

    @cached_property
    def IndexStatistics(self):  # pragma: no cover
        return IndexStatistics.make_one(self.boto3_raw_data["IndexStatistics"])

    ErrorMessage = field("ErrorMessage")

    @cached_property
    def CapacityUnits(self):  # pragma: no cover
        return CapacityUnitsConfiguration.make_one(self.boto3_raw_data["CapacityUnits"])

    @cached_property
    def UserTokenConfigurations(self):  # pragma: no cover
        return UserTokenConfiguration.make_many(
            self.boto3_raw_data["UserTokenConfigurations"]
        )

    UserContextPolicy = field("UserContextPolicy")

    @cached_property
    def UserGroupResolutionConfiguration(self):  # pragma: no cover
        return UserGroupResolutionConfiguration.make_one(
            self.boto3_raw_data["UserGroupResolutionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentMetadataConfiguration:
    boto3_raw_data: "type_defs.DocumentMetadataConfigurationTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Type = field("Type")
    Relevance = field("Relevance")

    @cached_property
    def Search(self):  # pragma: no cover
        return Search.make_one(self.boto3_raw_data["Search"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentMetadataConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentMetadataConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentRelevanceConfiguration:
    boto3_raw_data: "type_defs.DocumentRelevanceConfigurationTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Relevance = field("Relevance")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentRelevanceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentRelevanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebCrawlerConfigurationOutput:
    boto3_raw_data: "type_defs.WebCrawlerConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Urls(self):  # pragma: no cover
        return UrlsOutput.make_one(self.boto3_raw_data["Urls"])

    CrawlDepth = field("CrawlDepth")
    MaxLinksPerPage = field("MaxLinksPerPage")
    MaxContentSizePerPageInMegaBytes = field("MaxContentSizePerPageInMegaBytes")
    MaxUrlsPerMinuteCrawlRate = field("MaxUrlsPerMinuteCrawlRate")
    UrlInclusionPatterns = field("UrlInclusionPatterns")
    UrlExclusionPatterns = field("UrlExclusionPatterns")

    @cached_property
    def ProxyConfiguration(self):  # pragma: no cover
        return ProxyConfiguration.make_one(self.boto3_raw_data["ProxyConfiguration"])

    @cached_property
    def AuthenticationConfiguration(self):  # pragma: no cover
        return AuthenticationConfigurationOutput.make_one(
            self.boto3_raw_data["AuthenticationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WebCrawlerConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebCrawlerConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebCrawlerConfiguration:
    boto3_raw_data: "type_defs.WebCrawlerConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def Urls(self):  # pragma: no cover
        return Urls.make_one(self.boto3_raw_data["Urls"])

    CrawlDepth = field("CrawlDepth")
    MaxLinksPerPage = field("MaxLinksPerPage")
    MaxContentSizePerPageInMegaBytes = field("MaxContentSizePerPageInMegaBytes")
    MaxUrlsPerMinuteCrawlRate = field("MaxUrlsPerMinuteCrawlRate")
    UrlInclusionPatterns = field("UrlInclusionPatterns")
    UrlExclusionPatterns = field("UrlExclusionPatterns")

    @cached_property
    def ProxyConfiguration(self):  # pragma: no cover
        return ProxyConfiguration.make_one(self.boto3_raw_data["ProxyConfiguration"])

    @cached_property
    def AuthenticationConfiguration(self):  # pragma: no cover
        return AuthenticationConfiguration.make_one(
            self.boto3_raw_data["AuthenticationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebCrawlerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebCrawlerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestionValue:
    boto3_raw_data: "type_defs.SuggestionValueTypeDef" = dataclasses.field()

    @cached_property
    def Text(self):  # pragma: no cover
        return SuggestionTextWithHighlights.make_one(self.boto3_raw_data["Text"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestionValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestionValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableExcerpt:
    boto3_raw_data: "type_defs.TableExcerptTypeDef" = dataclasses.field()

    @cached_property
    def Rows(self):  # pragma: no cover
        return TableRow.make_many(self.boto3_raw_data["Rows"])

    TotalNumberOfRows = field("TotalNumberOfRows")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableExcerptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableExcerptTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceConfigurationOutput:
    boto3_raw_data: "type_defs.SalesforceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    ServerUrl = field("ServerUrl")
    SecretArn = field("SecretArn")

    @cached_property
    def StandardObjectConfigurations(self):  # pragma: no cover
        return SalesforceStandardObjectConfigurationOutput.make_many(
            self.boto3_raw_data["StandardObjectConfigurations"]
        )

    @cached_property
    def KnowledgeArticleConfiguration(self):  # pragma: no cover
        return SalesforceKnowledgeArticleConfigurationOutput.make_one(
            self.boto3_raw_data["KnowledgeArticleConfiguration"]
        )

    @cached_property
    def ChatterFeedConfiguration(self):  # pragma: no cover
        return SalesforceChatterFeedConfigurationOutput.make_one(
            self.boto3_raw_data["ChatterFeedConfiguration"]
        )

    CrawlAttachments = field("CrawlAttachments")

    @cached_property
    def StandardObjectAttachmentConfiguration(self):  # pragma: no cover
        return SalesforceStandardObjectAttachmentConfigurationOutput.make_one(
            self.boto3_raw_data["StandardObjectAttachmentConfiguration"]
        )

    IncludeAttachmentFilePatterns = field("IncludeAttachmentFilePatterns")
    ExcludeAttachmentFilePatterns = field("ExcludeAttachmentFilePatterns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SalesforceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceConfiguration:
    boto3_raw_data: "type_defs.SalesforceConfigurationTypeDef" = dataclasses.field()

    ServerUrl = field("ServerUrl")
    SecretArn = field("SecretArn")

    @cached_property
    def StandardObjectConfigurations(self):  # pragma: no cover
        return SalesforceStandardObjectConfiguration.make_many(
            self.boto3_raw_data["StandardObjectConfigurations"]
        )

    @cached_property
    def KnowledgeArticleConfiguration(self):  # pragma: no cover
        return SalesforceKnowledgeArticleConfiguration.make_one(
            self.boto3_raw_data["KnowledgeArticleConfiguration"]
        )

    @cached_property
    def ChatterFeedConfiguration(self):  # pragma: no cover
        return SalesforceChatterFeedConfiguration.make_one(
            self.boto3_raw_data["ChatterFeedConfiguration"]
        )

    CrawlAttachments = field("CrawlAttachments")

    @cached_property
    def StandardObjectAttachmentConfiguration(self):  # pragma: no cover
        return SalesforceStandardObjectAttachmentConfiguration.make_one(
            self.boto3_raw_data["StandardObjectAttachmentConfiguration"]
        )

    IncludeAttachmentFilePatterns = field("IncludeAttachmentFilePatterns")
    ExcludeAttachmentFilePatterns = field("ExcludeAttachmentFilePatterns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SalesforceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HookConfiguration:
    boto3_raw_data: "type_defs.HookConfigurationTypeDef" = dataclasses.field()

    LambdaArn = field("LambdaArn")
    S3Bucket = field("S3Bucket")

    @cached_property
    def InvocationCondition(self):  # pragma: no cover
        return DocumentAttributeCondition.make_one(
            self.boto3_raw_data["InvocationCondition"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HookConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HookConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineCustomDocumentEnrichmentConfiguration:
    boto3_raw_data: "type_defs.InlineCustomDocumentEnrichmentConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Condition(self):  # pragma: no cover
        return DocumentAttributeCondition.make_one(self.boto3_raw_data["Condition"])

    @cached_property
    def Target(self):  # pragma: no cover
        return DocumentAttributeTarget.make_one(self.boto3_raw_data["Target"])

    DocumentContentDeletion = field("DocumentContentDeletion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InlineCustomDocumentEnrichmentConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineCustomDocumentEnrichmentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttribute:
    boto3_raw_data: "type_defs.DocumentAttributeTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceSyncJobsRequest:
    boto3_raw_data: "type_defs.ListDataSourceSyncJobsRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IndexId = field("IndexId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    StartTimeFilter = field("StartTimeFilter")
    StatusFilter = field("StatusFilter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSourceSyncJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceSyncJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessControlConfigurationRequest:
    boto3_raw_data: "type_defs.CreateAccessControlConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def AccessControlList(self):  # pragma: no cover
        return Principal.make_many(self.boto3_raw_data["AccessControlList"])

    HierarchicalAccessControlList = field("HierarchicalAccessControlList")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccessControlConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessControlConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessControlConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateAccessControlConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")
    Id = field("Id")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def AccessControlList(self):  # pragma: no cover
        return Principal.make_many(self.boto3_raw_data["AccessControlList"])

    HierarchicalAccessControlList = field("HierarchicalAccessControlList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccessControlConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessControlConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveResult:
    boto3_raw_data: "type_defs.RetrieveResultTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @cached_property
    def ResultItems(self):  # pragma: no cover
        return RetrieveResultItem.make_many(self.boto3_raw_data["ResultItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetrieveResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetrieveResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDocumentEnrichmentConfigurationOutput:
    boto3_raw_data: "type_defs.CustomDocumentEnrichmentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InlineConfigurations(self):  # pragma: no cover
        return InlineCustomDocumentEnrichmentConfigurationOutput.make_many(
            self.boto3_raw_data["InlineConfigurations"]
        )

    @cached_property
    def PreExtractionHookConfiguration(self):  # pragma: no cover
        return HookConfigurationOutput.make_one(
            self.boto3_raw_data["PreExtractionHookConfiguration"]
        )

    @cached_property
    def PostExtractionHookConfiguration(self):  # pragma: no cover
        return HookConfigurationOutput.make_one(
            self.boto3_raw_data["PostExtractionHookConfiguration"]
        )

    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomDocumentEnrichmentConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDocumentEnrichmentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExperienceRequest:
    boto3_raw_data: "type_defs.CreateExperienceRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    IndexId = field("IndexId")
    RoleArn = field("RoleArn")
    Configuration = field("Configuration")
    Description = field("Description")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExperienceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExperienceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExperienceRequest:
    boto3_raw_data: "type_defs.UpdateExperienceRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")
    Name = field("Name")
    RoleArn = field("RoleArn")
    Configuration = field("Configuration")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateExperienceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExperienceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalResultAttribute:
    boto3_raw_data: "type_defs.AdditionalResultAttributeTypeDef" = dataclasses.field()

    Key = field("Key")
    ValueType = field("ValueType")

    @cached_property
    def Value(self):  # pragma: no cover
        return AdditionalResultAttributeValue.make_one(self.boto3_raw_data["Value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdditionalResultAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalResultAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollapsedResultDetail:
    boto3_raw_data: "type_defs.CollapsedResultDetailTypeDef" = dataclasses.field()

    @cached_property
    def DocumentAttribute(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(
            self.boto3_raw_data["DocumentAttribute"]
        )

    @cached_property
    def ExpandedResults(self):  # pragma: no cover
        return ExpandedResultItem.make_many(self.boto3_raw_data["ExpandedResults"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CollapsedResultDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollapsedResultDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Suggestion:
    boto3_raw_data: "type_defs.SuggestionTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def Value(self):  # pragma: no cover
        return SuggestionValue.make_one(self.boto3_raw_data["Value"])

    @cached_property
    def SourceDocuments(self):  # pragma: no cover
        return SourceDocument.make_many(self.boto3_raw_data["SourceDocuments"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfigurationOutput:
    boto3_raw_data: "type_defs.DataSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    @cached_property
    def SharePointConfiguration(self):  # pragma: no cover
        return SharePointConfigurationOutput.make_one(
            self.boto3_raw_data["SharePointConfiguration"]
        )

    @cached_property
    def DatabaseConfiguration(self):  # pragma: no cover
        return DatabaseConfigurationOutput.make_one(
            self.boto3_raw_data["DatabaseConfiguration"]
        )

    @cached_property
    def SalesforceConfiguration(self):  # pragma: no cover
        return SalesforceConfigurationOutput.make_one(
            self.boto3_raw_data["SalesforceConfiguration"]
        )

    @cached_property
    def OneDriveConfiguration(self):  # pragma: no cover
        return OneDriveConfigurationOutput.make_one(
            self.boto3_raw_data["OneDriveConfiguration"]
        )

    @cached_property
    def ServiceNowConfiguration(self):  # pragma: no cover
        return ServiceNowConfigurationOutput.make_one(
            self.boto3_raw_data["ServiceNowConfiguration"]
        )

    @cached_property
    def ConfluenceConfiguration(self):  # pragma: no cover
        return ConfluenceConfigurationOutput.make_one(
            self.boto3_raw_data["ConfluenceConfiguration"]
        )

    @cached_property
    def GoogleDriveConfiguration(self):  # pragma: no cover
        return GoogleDriveConfigurationOutput.make_one(
            self.boto3_raw_data["GoogleDriveConfiguration"]
        )

    @cached_property
    def WebCrawlerConfiguration(self):  # pragma: no cover
        return WebCrawlerConfigurationOutput.make_one(
            self.boto3_raw_data["WebCrawlerConfiguration"]
        )

    @cached_property
    def WorkDocsConfiguration(self):  # pragma: no cover
        return WorkDocsConfigurationOutput.make_one(
            self.boto3_raw_data["WorkDocsConfiguration"]
        )

    @cached_property
    def FsxConfiguration(self):  # pragma: no cover
        return FsxConfigurationOutput.make_one(self.boto3_raw_data["FsxConfiguration"])

    @cached_property
    def SlackConfiguration(self):  # pragma: no cover
        return SlackConfigurationOutput.make_one(
            self.boto3_raw_data["SlackConfiguration"]
        )

    @cached_property
    def BoxConfiguration(self):  # pragma: no cover
        return BoxConfigurationOutput.make_one(self.boto3_raw_data["BoxConfiguration"])

    @cached_property
    def QuipConfiguration(self):  # pragma: no cover
        return QuipConfigurationOutput.make_one(
            self.boto3_raw_data["QuipConfiguration"]
        )

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return JiraConfigurationOutput.make_one(
            self.boto3_raw_data["JiraConfiguration"]
        )

    @cached_property
    def GitHubConfiguration(self):  # pragma: no cover
        return GitHubConfigurationOutput.make_one(
            self.boto3_raw_data["GitHubConfiguration"]
        )

    @cached_property
    def AlfrescoConfiguration(self):  # pragma: no cover
        return AlfrescoConfigurationOutput.make_one(
            self.boto3_raw_data["AlfrescoConfiguration"]
        )

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfigurationOutput.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataSourceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfiguration:
    boto3_raw_data: "type_defs.DataSourceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DataSourceConfiguration.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    @cached_property
    def SharePointConfiguration(self):  # pragma: no cover
        return SharePointConfiguration.make_one(
            self.boto3_raw_data["SharePointConfiguration"]
        )

    @cached_property
    def DatabaseConfiguration(self):  # pragma: no cover
        return DatabaseConfiguration.make_one(
            self.boto3_raw_data["DatabaseConfiguration"]
        )

    @cached_property
    def SalesforceConfiguration(self):  # pragma: no cover
        return SalesforceConfiguration.make_one(
            self.boto3_raw_data["SalesforceConfiguration"]
        )

    @cached_property
    def OneDriveConfiguration(self):  # pragma: no cover
        return OneDriveConfiguration.make_one(
            self.boto3_raw_data["OneDriveConfiguration"]
        )

    @cached_property
    def ServiceNowConfiguration(self):  # pragma: no cover
        return ServiceNowConfiguration.make_one(
            self.boto3_raw_data["ServiceNowConfiguration"]
        )

    @cached_property
    def ConfluenceConfiguration(self):  # pragma: no cover
        return ConfluenceConfiguration.make_one(
            self.boto3_raw_data["ConfluenceConfiguration"]
        )

    @cached_property
    def GoogleDriveConfiguration(self):  # pragma: no cover
        return GoogleDriveConfiguration.make_one(
            self.boto3_raw_data["GoogleDriveConfiguration"]
        )

    @cached_property
    def WebCrawlerConfiguration(self):  # pragma: no cover
        return WebCrawlerConfiguration.make_one(
            self.boto3_raw_data["WebCrawlerConfiguration"]
        )

    @cached_property
    def WorkDocsConfiguration(self):  # pragma: no cover
        return WorkDocsConfiguration.make_one(
            self.boto3_raw_data["WorkDocsConfiguration"]
        )

    @cached_property
    def FsxConfiguration(self):  # pragma: no cover
        return FsxConfiguration.make_one(self.boto3_raw_data["FsxConfiguration"])

    @cached_property
    def SlackConfiguration(self):  # pragma: no cover
        return SlackConfiguration.make_one(self.boto3_raw_data["SlackConfiguration"])

    @cached_property
    def BoxConfiguration(self):  # pragma: no cover
        return BoxConfiguration.make_one(self.boto3_raw_data["BoxConfiguration"])

    @cached_property
    def QuipConfiguration(self):  # pragma: no cover
        return QuipConfiguration.make_one(self.boto3_raw_data["QuipConfiguration"])

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return JiraConfiguration.make_one(self.boto3_raw_data["JiraConfiguration"])

    @cached_property
    def GitHubConfiguration(self):  # pragma: no cover
        return GitHubConfiguration.make_one(self.boto3_raw_data["GitHubConfiguration"])

    @cached_property
    def AlfrescoConfiguration(self):  # pragma: no cover
        return AlfrescoConfiguration.make_one(
            self.boto3_raw_data["AlfrescoConfiguration"]
        )

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfiguration.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDocumentEnrichmentConfiguration:
    boto3_raw_data: "type_defs.CustomDocumentEnrichmentConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InlineConfigurations(self):  # pragma: no cover
        return InlineCustomDocumentEnrichmentConfiguration.make_many(
            self.boto3_raw_data["InlineConfigurations"]
        )

    @cached_property
    def PreExtractionHookConfiguration(self):  # pragma: no cover
        return HookConfiguration.make_one(
            self.boto3_raw_data["PreExtractionHookConfiguration"]
        )

    @cached_property
    def PostExtractionHookConfiguration(self):  # pragma: no cover
        return HookConfiguration.make_one(
            self.boto3_raw_data["PostExtractionHookConfiguration"]
        )

    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomDocumentEnrichmentConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDocumentEnrichmentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturedResultsItem:
    boto3_raw_data: "type_defs.FeaturedResultsItemTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")

    @cached_property
    def AdditionalAttributes(self):  # pragma: no cover
        return AdditionalResultAttribute.make_many(
            self.boto3_raw_data["AdditionalAttributes"]
        )

    DocumentId = field("DocumentId")

    @cached_property
    def DocumentTitle(self):  # pragma: no cover
        return TextWithHighlights.make_one(self.boto3_raw_data["DocumentTitle"])

    @cached_property
    def DocumentExcerpt(self):  # pragma: no cover
        return TextWithHighlights.make_one(self.boto3_raw_data["DocumentExcerpt"])

    DocumentURI = field("DocumentURI")

    @cached_property
    def DocumentAttributes(self):  # pragma: no cover
        return DocumentAttributeOutput.make_many(
            self.boto3_raw_data["DocumentAttributes"]
        )

    FeedbackToken = field("FeedbackToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeaturedResultsItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturedResultsItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryResultItem:
    boto3_raw_data: "type_defs.QueryResultItemTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")
    Format = field("Format")

    @cached_property
    def AdditionalAttributes(self):  # pragma: no cover
        return AdditionalResultAttribute.make_many(
            self.boto3_raw_data["AdditionalAttributes"]
        )

    DocumentId = field("DocumentId")

    @cached_property
    def DocumentTitle(self):  # pragma: no cover
        return TextWithHighlights.make_one(self.boto3_raw_data["DocumentTitle"])

    @cached_property
    def DocumentExcerpt(self):  # pragma: no cover
        return TextWithHighlights.make_one(self.boto3_raw_data["DocumentExcerpt"])

    DocumentURI = field("DocumentURI")

    @cached_property
    def DocumentAttributes(self):  # pragma: no cover
        return DocumentAttributeOutput.make_many(
            self.boto3_raw_data["DocumentAttributes"]
        )

    @cached_property
    def ScoreAttributes(self):  # pragma: no cover
        return ScoreAttributes.make_one(self.boto3_raw_data["ScoreAttributes"])

    FeedbackToken = field("FeedbackToken")

    @cached_property
    def TableExcerpt(self):  # pragma: no cover
        return TableExcerpt.make_one(self.boto3_raw_data["TableExcerpt"])

    @cached_property
    def CollapsedResultDetail(self):  # pragma: no cover
        return CollapsedResultDetail.make_one(
            self.boto3_raw_data["CollapsedResultDetail"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryResultItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryResultItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIndexRequest:
    boto3_raw_data: "type_defs.UpdateIndexRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    RoleArn = field("RoleArn")
    Description = field("Description")
    DocumentMetadataConfigurationUpdates = field("DocumentMetadataConfigurationUpdates")

    @cached_property
    def CapacityUnits(self):  # pragma: no cover
        return CapacityUnitsConfiguration.make_one(self.boto3_raw_data["CapacityUnits"])

    @cached_property
    def UserTokenConfigurations(self):  # pragma: no cover
        return UserTokenConfiguration.make_many(
            self.boto3_raw_data["UserTokenConfigurations"]
        )

    UserContextPolicy = field("UserContextPolicy")

    @cached_property
    def UserGroupResolutionConfiguration(self):  # pragma: no cover
        return UserGroupResolutionConfiguration.make_one(
            self.boto3_raw_data["UserGroupResolutionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQuerySuggestionsResponse:
    boto3_raw_data: "type_defs.GetQuerySuggestionsResponseTypeDef" = dataclasses.field()

    QuerySuggestionsId = field("QuerySuggestionsId")

    @cached_property
    def Suggestions(self):  # pragma: no cover
        return Suggestion.make_many(self.boto3_raw_data["Suggestions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQuerySuggestionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQuerySuggestionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSourceResponse:
    boto3_raw_data: "type_defs.DescribeDataSourceResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")
    Name = field("Name")
    Type = field("Type")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return DataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["Configuration"]
        )

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    Description = field("Description")
    Status = field("Status")
    Schedule = field("Schedule")
    RoleArn = field("RoleArn")
    ErrorMessage = field("ErrorMessage")
    LanguageCode = field("LanguageCode")

    @cached_property
    def CustomDocumentEnrichmentConfiguration(self):  # pragma: no cover
        return CustomDocumentEnrichmentConfigurationOutput.make_one(
            self.boto3_raw_data["CustomDocumentEnrichmentConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeFilter:
    boto3_raw_data: "type_defs.AttributeFilterTypeDef" = dataclasses.field()

    AndAllFilters = field("AndAllFilters")
    OrAllFilters = field("OrAllFilters")
    NotFilter = field("NotFilter")
    EqualsTo = field("EqualsTo")
    ContainsAll = field("ContainsAll")
    ContainsAny = field("ContainsAny")
    GreaterThan = field("GreaterThan")
    GreaterThanOrEquals = field("GreaterThanOrEquals")
    LessThan = field("LessThan")
    LessThanOrEquals = field("LessThanOrEquals")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentInfo:
    boto3_raw_data: "type_defs.DocumentInfoTypeDef" = dataclasses.field()

    DocumentId = field("DocumentId")
    Attributes = field("Attributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Document:
    boto3_raw_data: "type_defs.DocumentTypeDef" = dataclasses.field()

    Id = field("Id")
    Title = field("Title")
    Blob = field("Blob")

    @cached_property
    def S3Path(self):  # pragma: no cover
        return S3Path.make_one(self.boto3_raw_data["S3Path"])

    Attributes = field("Attributes")

    @cached_property
    def AccessControlList(self):  # pragma: no cover
        return Principal.make_many(self.boto3_raw_data["AccessControlList"])

    HierarchicalAccessControlList = field("HierarchicalAccessControlList")
    ContentType = field("ContentType")
    AccessControlConfigurationId = field("AccessControlConfigurationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryResult:
    boto3_raw_data: "type_defs.QueryResultTypeDef" = dataclasses.field()

    QueryId = field("QueryId")

    @cached_property
    def ResultItems(self):  # pragma: no cover
        return QueryResultItem.make_many(self.boto3_raw_data["ResultItems"])

    @cached_property
    def FacetResults(self):  # pragma: no cover
        return FacetResult.make_many(self.boto3_raw_data["FacetResults"])

    TotalNumberOfResults = field("TotalNumberOfResults")

    @cached_property
    def Warnings(self):  # pragma: no cover
        return Warning.make_many(self.boto3_raw_data["Warnings"])

    @cached_property
    def SpellCorrectedQueries(self):  # pragma: no cover
        return SpellCorrectedQuery.make_many(
            self.boto3_raw_data["SpellCorrectedQueries"]
        )

    @cached_property
    def FeaturedResultsItems(self):  # pragma: no cover
        return FeaturedResultsItem.make_many(
            self.boto3_raw_data["FeaturedResultsItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceRequest:
    boto3_raw_data: "type_defs.CreateDataSourceRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    IndexId = field("IndexId")
    Type = field("Type")
    Configuration = field("Configuration")
    VpcConfiguration = field("VpcConfiguration")
    Description = field("Description")
    Schedule = field("Schedule")
    RoleArn = field("RoleArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")
    LanguageCode = field("LanguageCode")
    CustomDocumentEnrichmentConfiguration = field(
        "CustomDocumentEnrichmentConfiguration"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSourceRequest:
    boto3_raw_data: "type_defs.UpdateDataSourceRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IndexId = field("IndexId")
    Name = field("Name")
    Configuration = field("Configuration")
    VpcConfiguration = field("VpcConfiguration")
    Description = field("Description")
    Schedule = field("Schedule")
    RoleArn = field("RoleArn")
    LanguageCode = field("LanguageCode")
    CustomDocumentEnrichmentConfiguration = field(
        "CustomDocumentEnrichmentConfiguration"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeSuggestionsGetConfig:
    boto3_raw_data: "type_defs.AttributeSuggestionsGetConfigTypeDef" = (
        dataclasses.field()
    )

    SuggestionAttributes = field("SuggestionAttributes")
    AdditionalResponseAttributes = field("AdditionalResponseAttributes")

    @cached_property
    def AttributeFilter(self):  # pragma: no cover
        return AttributeFilter.make_one(self.boto3_raw_data["AttributeFilter"])

    @cached_property
    def UserContext(self):  # pragma: no cover
        return UserContext.make_one(self.boto3_raw_data["UserContext"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AttributeSuggestionsGetConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeSuggestionsGetConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryRequest:
    boto3_raw_data: "type_defs.QueryRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    QueryText = field("QueryText")

    @cached_property
    def AttributeFilter(self):  # pragma: no cover
        return AttributeFilter.make_one(self.boto3_raw_data["AttributeFilter"])

    @cached_property
    def Facets(self):  # pragma: no cover
        return Facet.make_many(self.boto3_raw_data["Facets"])

    RequestedDocumentAttributes = field("RequestedDocumentAttributes")
    QueryResultTypeFilter = field("QueryResultTypeFilter")

    @cached_property
    def DocumentRelevanceOverrideConfigurations(self):  # pragma: no cover
        return DocumentRelevanceConfiguration.make_many(
            self.boto3_raw_data["DocumentRelevanceOverrideConfigurations"]
        )

    PageNumber = field("PageNumber")
    PageSize = field("PageSize")

    @cached_property
    def SortingConfiguration(self):  # pragma: no cover
        return SortingConfiguration.make_one(
            self.boto3_raw_data["SortingConfiguration"]
        )

    @cached_property
    def SortingConfigurations(self):  # pragma: no cover
        return SortingConfiguration.make_many(
            self.boto3_raw_data["SortingConfigurations"]
        )

    @cached_property
    def UserContext(self):  # pragma: no cover
        return UserContext.make_one(self.boto3_raw_data["UserContext"])

    VisitorId = field("VisitorId")

    @cached_property
    def SpellCorrectionConfiguration(self):  # pragma: no cover
        return SpellCorrectionConfiguration.make_one(
            self.boto3_raw_data["SpellCorrectionConfiguration"]
        )

    @cached_property
    def CollapseConfiguration(self):  # pragma: no cover
        return CollapseConfiguration.make_one(
            self.boto3_raw_data["CollapseConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveRequest:
    boto3_raw_data: "type_defs.RetrieveRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    QueryText = field("QueryText")

    @cached_property
    def AttributeFilter(self):  # pragma: no cover
        return AttributeFilter.make_one(self.boto3_raw_data["AttributeFilter"])

    RequestedDocumentAttributes = field("RequestedDocumentAttributes")

    @cached_property
    def DocumentRelevanceOverrideConfigurations(self):  # pragma: no cover
        return DocumentRelevanceConfiguration.make_many(
            self.boto3_raw_data["DocumentRelevanceOverrideConfigurations"]
        )

    PageNumber = field("PageNumber")
    PageSize = field("PageSize")

    @cached_property
    def UserContext(self):  # pragma: no cover
        return UserContext.make_one(self.boto3_raw_data["UserContext"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetrieveRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetrieveRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDocumentStatusRequest:
    boto3_raw_data: "type_defs.BatchGetDocumentStatusRequestTypeDef" = (
        dataclasses.field()
    )

    IndexId = field("IndexId")

    @cached_property
    def DocumentInfoList(self):  # pragma: no cover
        return DocumentInfo.make_many(self.boto3_raw_data["DocumentInfoList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetDocumentStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDocumentStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutDocumentRequest:
    boto3_raw_data: "type_defs.BatchPutDocumentRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")

    @cached_property
    def Documents(self):  # pragma: no cover
        return Document.make_many(self.boto3_raw_data["Documents"])

    RoleArn = field("RoleArn")
    CustomDocumentEnrichmentConfiguration = field(
        "CustomDocumentEnrichmentConfiguration"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQuerySuggestionsRequest:
    boto3_raw_data: "type_defs.GetQuerySuggestionsRequestTypeDef" = dataclasses.field()

    IndexId = field("IndexId")
    QueryText = field("QueryText")
    MaxSuggestionsCount = field("MaxSuggestionsCount")
    SuggestionTypes = field("SuggestionTypes")

    @cached_property
    def AttributeSuggestionsConfig(self):  # pragma: no cover
        return AttributeSuggestionsGetConfig.make_one(
            self.boto3_raw_data["AttributeSuggestionsConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQuerySuggestionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQuerySuggestionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
