# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_timestream_write import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BatchLoadProgressReport:
    boto3_raw_data: "type_defs.BatchLoadProgressReportTypeDef" = dataclasses.field()

    RecordsProcessed = field("RecordsProcessed")
    RecordsIngested = field("RecordsIngested")
    ParseFailures = field("ParseFailures")
    RecordIngestionFailures = field("RecordIngestionFailures")
    FileFailures = field("FileFailures")
    BytesMetered = field("BytesMetered")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchLoadProgressReportTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchLoadProgressReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchLoadTask:
    boto3_raw_data: "type_defs.BatchLoadTaskTypeDef" = dataclasses.field()

    TaskId = field("TaskId")
    TaskStatus = field("TaskStatus")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")
    ResumableUntil = field("ResumableUntil")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchLoadTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchLoadTaskTypeDef"]],
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
class Database:
    boto3_raw_data: "type_defs.DatabaseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    DatabaseName = field("DatabaseName")
    TableCount = field("TableCount")
    KmsKeyId = field("KmsKeyId")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatabaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatabaseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetentionProperties:
    boto3_raw_data: "type_defs.RetentionPropertiesTypeDef" = dataclasses.field()

    MemoryStoreRetentionPeriodInHours = field("MemoryStoreRetentionPeriodInHours")
    MagneticStoreRetentionPeriodInDays = field("MagneticStoreRetentionPeriodInDays")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetentionPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetentionPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CsvConfiguration:
    boto3_raw_data: "type_defs.CsvConfigurationTypeDef" = dataclasses.field()

    ColumnSeparator = field("ColumnSeparator")
    EscapeChar = field("EscapeChar")
    QuoteChar = field("QuoteChar")
    NullValue = field("NullValue")
    TrimWhiteSpace = field("TrimWhiteSpace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CsvConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CsvConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataModelS3Configuration:
    boto3_raw_data: "type_defs.DataModelS3ConfigurationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectKey = field("ObjectKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataModelS3ConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataModelS3ConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionMapping:
    boto3_raw_data: "type_defs.DimensionMappingTypeDef" = dataclasses.field()

    SourceColumn = field("SourceColumn")
    DestinationColumn = field("DestinationColumn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceS3Configuration:
    boto3_raw_data: "type_defs.DataSourceS3ConfigurationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectKeyPrefix = field("ObjectKeyPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceS3ConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceS3ConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatabaseRequest:
    boto3_raw_data: "type_defs.DeleteDatabaseRequestTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatabaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatabaseRequestTypeDef"]
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

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")

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
class DescribeBatchLoadTaskRequest:
    boto3_raw_data: "type_defs.DescribeBatchLoadTaskRequestTypeDef" = (
        dataclasses.field()
    )

    TaskId = field("TaskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBatchLoadTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBatchLoadTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatabaseRequest:
    boto3_raw_data: "type_defs.DescribeDatabaseRequestTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatabaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Endpoint:
    boto3_raw_data: "type_defs.EndpointTypeDef" = dataclasses.field()

    Address = field("Address")
    CachePeriodInMinutes = field("CachePeriodInMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableRequest:
    boto3_raw_data: "type_defs.DescribeTableRequestTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dimension:
    boto3_raw_data: "type_defs.DimensionTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")
    DimensionValueType = field("DimensionValueType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchLoadTasksRequest:
    boto3_raw_data: "type_defs.ListBatchLoadTasksRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    TaskStatus = field("TaskStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBatchLoadTasksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchLoadTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatabasesRequest:
    boto3_raw_data: "type_defs.ListDatabasesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatabasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatabasesRequestTypeDef"]
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

    DatabaseName = field("DatabaseName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

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
class S3Configuration:
    boto3_raw_data: "type_defs.S3ConfigurationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectKeyPrefix = field("ObjectKeyPrefix")
    EncryptionOption = field("EncryptionOption")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeasureValue:
    boto3_raw_data: "type_defs.MeasureValueTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MeasureValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MeasureValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiMeasureAttributeMapping:
    boto3_raw_data: "type_defs.MultiMeasureAttributeMappingTypeDef" = (
        dataclasses.field()
    )

    SourceColumn = field("SourceColumn")
    TargetMultiMeasureAttributeName = field("TargetMultiMeasureAttributeName")
    MeasureValueType = field("MeasureValueType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiMeasureAttributeMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiMeasureAttributeMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartitionKey:
    boto3_raw_data: "type_defs.PartitionKeyTypeDef" = dataclasses.field()

    Type = field("Type")
    Name = field("Name")
    EnforcementInRecord = field("EnforcementInRecord")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartitionKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PartitionKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordsIngested:
    boto3_raw_data: "type_defs.RecordsIngestedTypeDef" = dataclasses.field()

    Total = field("Total")
    MemoryStore = field("MemoryStore")
    MagneticStore = field("MagneticStore")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordsIngestedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordsIngestedTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportS3Configuration:
    boto3_raw_data: "type_defs.ReportS3ConfigurationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectKeyPrefix = field("ObjectKeyPrefix")
    EncryptionOption = field("EncryptionOption")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportS3ConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportS3ConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeBatchLoadTaskRequest:
    boto3_raw_data: "type_defs.ResumeBatchLoadTaskRequestTypeDef" = dataclasses.field()

    TaskId = field("TaskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeBatchLoadTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeBatchLoadTaskRequestTypeDef"]
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
class UpdateDatabaseRequest:
    boto3_raw_data: "type_defs.UpdateDatabaseRequestTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatabaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBatchLoadTaskResponse:
    boto3_raw_data: "type_defs.CreateBatchLoadTaskResponseTypeDef" = dataclasses.field()

    TaskId = field("TaskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBatchLoadTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBatchLoadTaskResponseTypeDef"]
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
class ListBatchLoadTasksResponse:
    boto3_raw_data: "type_defs.ListBatchLoadTasksResponseTypeDef" = dataclasses.field()

    @cached_property
    def BatchLoadTasks(self):  # pragma: no cover
        return BatchLoadTask.make_many(self.boto3_raw_data["BatchLoadTasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBatchLoadTasksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchLoadTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatabaseRequest:
    boto3_raw_data: "type_defs.CreateDatabaseRequestTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatabaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatabaseRequestTypeDef"]
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
class CreateDatabaseResponse:
    boto3_raw_data: "type_defs.CreateDatabaseResponseTypeDef" = dataclasses.field()

    @cached_property
    def Database(self):  # pragma: no cover
        return Database.make_one(self.boto3_raw_data["Database"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatabaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatabaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatabaseResponse:
    boto3_raw_data: "type_defs.DescribeDatabaseResponseTypeDef" = dataclasses.field()

    @cached_property
    def Database(self):  # pragma: no cover
        return Database.make_one(self.boto3_raw_data["Database"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatabaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatabaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatabasesResponse:
    boto3_raw_data: "type_defs.ListDatabasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Databases(self):  # pragma: no cover
        return Database.make_many(self.boto3_raw_data["Databases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatabasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatabasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDatabaseResponse:
    boto3_raw_data: "type_defs.UpdateDatabaseResponseTypeDef" = dataclasses.field()

    @cached_property
    def Database(self):  # pragma: no cover
        return Database.make_one(self.boto3_raw_data["Database"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatabaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatabaseResponseTypeDef"]
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
    def DataSourceS3Configuration(self):  # pragma: no cover
        return DataSourceS3Configuration.make_one(
            self.boto3_raw_data["DataSourceS3Configuration"]
        )

    DataFormat = field("DataFormat")

    @cached_property
    def CsvConfiguration(self):  # pragma: no cover
        return CsvConfiguration.make_one(self.boto3_raw_data["CsvConfiguration"])

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
class DescribeEndpointsResponse:
    boto3_raw_data: "type_defs.DescribeEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return Endpoint.make_many(self.boto3_raw_data["Endpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MagneticStoreRejectedDataLocation:
    boto3_raw_data: "type_defs.MagneticStoreRejectedDataLocationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3Configuration.make_one(self.boto3_raw_data["S3Configuration"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MagneticStoreRejectedDataLocationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MagneticStoreRejectedDataLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Record:
    boto3_raw_data: "type_defs.RecordTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    MeasureName = field("MeasureName")
    MeasureValue = field("MeasureValue")
    MeasureValueType = field("MeasureValueType")
    Time = field("Time")
    TimeUnit = field("TimeUnit")
    Version = field("Version")

    @cached_property
    def MeasureValues(self):  # pragma: no cover
        return MeasureValue.make_many(self.boto3_raw_data["MeasureValues"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MixedMeasureMappingOutput:
    boto3_raw_data: "type_defs.MixedMeasureMappingOutputTypeDef" = dataclasses.field()

    MeasureValueType = field("MeasureValueType")
    MeasureName = field("MeasureName")
    SourceColumn = field("SourceColumn")
    TargetMeasureName = field("TargetMeasureName")

    @cached_property
    def MultiMeasureAttributeMappings(self):  # pragma: no cover
        return MultiMeasureAttributeMapping.make_many(
            self.boto3_raw_data["MultiMeasureAttributeMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MixedMeasureMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MixedMeasureMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MixedMeasureMapping:
    boto3_raw_data: "type_defs.MixedMeasureMappingTypeDef" = dataclasses.field()

    MeasureValueType = field("MeasureValueType")
    MeasureName = field("MeasureName")
    SourceColumn = field("SourceColumn")
    TargetMeasureName = field("TargetMeasureName")

    @cached_property
    def MultiMeasureAttributeMappings(self):  # pragma: no cover
        return MultiMeasureAttributeMapping.make_many(
            self.boto3_raw_data["MultiMeasureAttributeMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MixedMeasureMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MixedMeasureMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiMeasureMappingsOutput:
    boto3_raw_data: "type_defs.MultiMeasureMappingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def MultiMeasureAttributeMappings(self):  # pragma: no cover
        return MultiMeasureAttributeMapping.make_many(
            self.boto3_raw_data["MultiMeasureAttributeMappings"]
        )

    TargetMultiMeasureName = field("TargetMultiMeasureName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiMeasureMappingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiMeasureMappingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiMeasureMappings:
    boto3_raw_data: "type_defs.MultiMeasureMappingsTypeDef" = dataclasses.field()

    @cached_property
    def MultiMeasureAttributeMappings(self):  # pragma: no cover
        return MultiMeasureAttributeMapping.make_many(
            self.boto3_raw_data["MultiMeasureAttributeMappings"]
        )

    TargetMultiMeasureName = field("TargetMultiMeasureName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiMeasureMappingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiMeasureMappingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaOutput:
    boto3_raw_data: "type_defs.SchemaOutputTypeDef" = dataclasses.field()

    @cached_property
    def CompositePartitionKey(self):  # pragma: no cover
        return PartitionKey.make_many(self.boto3_raw_data["CompositePartitionKey"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchemaOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schema:
    boto3_raw_data: "type_defs.SchemaTypeDef" = dataclasses.field()

    @cached_property
    def CompositePartitionKey(self):  # pragma: no cover
        return PartitionKey.make_many(self.boto3_raw_data["CompositePartitionKey"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchemaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteRecordsResponse:
    boto3_raw_data: "type_defs.WriteRecordsResponseTypeDef" = dataclasses.field()

    @cached_property
    def RecordsIngested(self):  # pragma: no cover
        return RecordsIngested.make_one(self.boto3_raw_data["RecordsIngested"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WriteRecordsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteRecordsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportConfiguration:
    boto3_raw_data: "type_defs.ReportConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ReportS3Configuration(self):  # pragma: no cover
        return ReportS3Configuration.make_one(
            self.boto3_raw_data["ReportS3Configuration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MagneticStoreWriteProperties:
    boto3_raw_data: "type_defs.MagneticStoreWritePropertiesTypeDef" = (
        dataclasses.field()
    )

    EnableMagneticStoreWrites = field("EnableMagneticStoreWrites")

    @cached_property
    def MagneticStoreRejectedDataLocation(self):  # pragma: no cover
        return MagneticStoreRejectedDataLocation.make_one(
            self.boto3_raw_data["MagneticStoreRejectedDataLocation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MagneticStoreWritePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MagneticStoreWritePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteRecordsRequest:
    boto3_raw_data: "type_defs.WriteRecordsRequestTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")

    @cached_property
    def Records(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["Records"])

    @cached_property
    def CommonAttributes(self):  # pragma: no cover
        return Record.make_one(self.boto3_raw_data["CommonAttributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WriteRecordsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteRecordsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataModelOutput:
    boto3_raw_data: "type_defs.DataModelOutputTypeDef" = dataclasses.field()

    @cached_property
    def DimensionMappings(self):  # pragma: no cover
        return DimensionMapping.make_many(self.boto3_raw_data["DimensionMappings"])

    TimeColumn = field("TimeColumn")
    TimeUnit = field("TimeUnit")

    @cached_property
    def MultiMeasureMappings(self):  # pragma: no cover
        return MultiMeasureMappingsOutput.make_one(
            self.boto3_raw_data["MultiMeasureMappings"]
        )

    @cached_property
    def MixedMeasureMappings(self):  # pragma: no cover
        return MixedMeasureMappingOutput.make_many(
            self.boto3_raw_data["MixedMeasureMappings"]
        )

    MeasureNameColumn = field("MeasureNameColumn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataModelOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataModelOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataModel:
    boto3_raw_data: "type_defs.DataModelTypeDef" = dataclasses.field()

    @cached_property
    def DimensionMappings(self):  # pragma: no cover
        return DimensionMapping.make_many(self.boto3_raw_data["DimensionMappings"])

    TimeColumn = field("TimeColumn")
    TimeUnit = field("TimeUnit")

    @cached_property
    def MultiMeasureMappings(self):  # pragma: no cover
        return MultiMeasureMappings.make_one(
            self.boto3_raw_data["MultiMeasureMappings"]
        )

    @cached_property
    def MixedMeasureMappings(self):  # pragma: no cover
        return MixedMeasureMapping.make_many(
            self.boto3_raw_data["MixedMeasureMappings"]
        )

    MeasureNameColumn = field("MeasureNameColumn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataModelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Table:
    boto3_raw_data: "type_defs.TableTypeDef" = dataclasses.field()

    Arn = field("Arn")
    TableName = field("TableName")
    DatabaseName = field("DatabaseName")
    TableStatus = field("TableStatus")

    @cached_property
    def RetentionProperties(self):  # pragma: no cover
        return RetentionProperties.make_one(self.boto3_raw_data["RetentionProperties"])

    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def MagneticStoreWriteProperties(self):  # pragma: no cover
        return MagneticStoreWriteProperties.make_one(
            self.boto3_raw_data["MagneticStoreWriteProperties"]
        )

    @cached_property
    def Schema(self):  # pragma: no cover
        return SchemaOutput.make_one(self.boto3_raw_data["Schema"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataModelConfigurationOutput:
    boto3_raw_data: "type_defs.DataModelConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DataModel(self):  # pragma: no cover
        return DataModelOutput.make_one(self.boto3_raw_data["DataModel"])

    @cached_property
    def DataModelS3Configuration(self):  # pragma: no cover
        return DataModelS3Configuration.make_one(
            self.boto3_raw_data["DataModelS3Configuration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataModelConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataModelConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataModelConfiguration:
    boto3_raw_data: "type_defs.DataModelConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def DataModel(self):  # pragma: no cover
        return DataModel.make_one(self.boto3_raw_data["DataModel"])

    @cached_property
    def DataModelS3Configuration(self):  # pragma: no cover
        return DataModelS3Configuration.make_one(
            self.boto3_raw_data["DataModelS3Configuration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataModelConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataModelConfigurationTypeDef"]
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

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")

    @cached_property
    def RetentionProperties(self):  # pragma: no cover
        return RetentionProperties.make_one(self.boto3_raw_data["RetentionProperties"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def MagneticStoreWriteProperties(self):  # pragma: no cover
        return MagneticStoreWriteProperties.make_one(
            self.boto3_raw_data["MagneticStoreWriteProperties"]
        )

    Schema = field("Schema")

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


@dataclasses.dataclass(frozen=True)
class UpdateTableRequest:
    boto3_raw_data: "type_defs.UpdateTableRequestTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")

    @cached_property
    def RetentionProperties(self):  # pragma: no cover
        return RetentionProperties.make_one(self.boto3_raw_data["RetentionProperties"])

    @cached_property
    def MagneticStoreWriteProperties(self):  # pragma: no cover
        return MagneticStoreWriteProperties.make_one(
            self.boto3_raw_data["MagneticStoreWriteProperties"]
        )

    Schema = field("Schema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableRequestTypeDef"]
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

    @cached_property
    def Table(self):  # pragma: no cover
        return Table.make_one(self.boto3_raw_data["Table"])

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
class DescribeTableResponse:
    boto3_raw_data: "type_defs.DescribeTableResponseTypeDef" = dataclasses.field()

    @cached_property
    def Table(self):  # pragma: no cover
        return Table.make_one(self.boto3_raw_data["Table"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTableResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableResponseTypeDef"]
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
    def Tables(self):  # pragma: no cover
        return Table.make_many(self.boto3_raw_data["Tables"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class UpdateTableResponse:
    boto3_raw_data: "type_defs.UpdateTableResponseTypeDef" = dataclasses.field()

    @cached_property
    def Table(self):  # pragma: no cover
        return Table.make_one(self.boto3_raw_data["Table"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTableResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchLoadTaskDescription:
    boto3_raw_data: "type_defs.BatchLoadTaskDescriptionTypeDef" = dataclasses.field()

    TaskId = field("TaskId")
    ErrorMessage = field("ErrorMessage")

    @cached_property
    def DataSourceConfiguration(self):  # pragma: no cover
        return DataSourceConfiguration.make_one(
            self.boto3_raw_data["DataSourceConfiguration"]
        )

    @cached_property
    def ProgressReport(self):  # pragma: no cover
        return BatchLoadProgressReport.make_one(self.boto3_raw_data["ProgressReport"])

    @cached_property
    def ReportConfiguration(self):  # pragma: no cover
        return ReportConfiguration.make_one(self.boto3_raw_data["ReportConfiguration"])

    @cached_property
    def DataModelConfiguration(self):  # pragma: no cover
        return DataModelConfigurationOutput.make_one(
            self.boto3_raw_data["DataModelConfiguration"]
        )

    TargetDatabaseName = field("TargetDatabaseName")
    TargetTableName = field("TargetTableName")
    TaskStatus = field("TaskStatus")
    RecordVersion = field("RecordVersion")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")
    ResumableUntil = field("ResumableUntil")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchLoadTaskDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchLoadTaskDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBatchLoadTaskResponse:
    boto3_raw_data: "type_defs.DescribeBatchLoadTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BatchLoadTaskDescription(self):  # pragma: no cover
        return BatchLoadTaskDescription.make_one(
            self.boto3_raw_data["BatchLoadTaskDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBatchLoadTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBatchLoadTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBatchLoadTaskRequest:
    boto3_raw_data: "type_defs.CreateBatchLoadTaskRequestTypeDef" = dataclasses.field()

    @cached_property
    def DataSourceConfiguration(self):  # pragma: no cover
        return DataSourceConfiguration.make_one(
            self.boto3_raw_data["DataSourceConfiguration"]
        )

    @cached_property
    def ReportConfiguration(self):  # pragma: no cover
        return ReportConfiguration.make_one(self.boto3_raw_data["ReportConfiguration"])

    TargetDatabaseName = field("TargetDatabaseName")
    TargetTableName = field("TargetTableName")
    ClientToken = field("ClientToken")
    DataModelConfiguration = field("DataModelConfiguration")
    RecordVersion = field("RecordVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBatchLoadTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBatchLoadTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
