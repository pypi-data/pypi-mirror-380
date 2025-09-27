# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_keyspacesstreams import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class GetRecordsInput:
    boto3_raw_data: "type_defs.GetRecordsInputTypeDef" = dataclasses.field()

    shardIterator = field("shardIterator")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRecordsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRecordsInputTypeDef"]],
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
class GetShardIteratorInput:
    boto3_raw_data: "type_defs.GetShardIteratorInputTypeDef" = dataclasses.field()

    streamArn = field("streamArn")
    shardId = field("shardId")
    shardIteratorType = field("shardIteratorType")
    sequenceNumber = field("sequenceNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetShardIteratorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetShardIteratorInputTypeDef"]
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
class ShardFilter:
    boto3_raw_data: "type_defs.ShardFilterTypeDef" = dataclasses.field()

    type = field("type")
    shardId = field("shardId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShardFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShardFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyspacesMetadata:
    boto3_raw_data: "type_defs.KeyspacesMetadataTypeDef" = dataclasses.field()

    expirationTime = field("expirationTime")
    writeTime = field("writeTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyspacesMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyspacesMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsInput:
    boto3_raw_data: "type_defs.ListStreamsInputTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")
    tableName = field("tableName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStreamsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stream:
    boto3_raw_data: "type_defs.StreamTypeDef" = dataclasses.field()

    streamArn = field("streamArn")
    keyspaceName = field("keyspaceName")
    tableName = field("tableName")
    streamLabel = field("streamLabel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SequenceNumberRange:
    boto3_raw_data: "type_defs.SequenceNumberRangeTypeDef" = dataclasses.field()

    startingSequenceNumber = field("startingSequenceNumber")
    endingSequenceNumber = field("endingSequenceNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SequenceNumberRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SequenceNumberRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetShardIteratorOutput:
    boto3_raw_data: "type_defs.GetShardIteratorOutputTypeDef" = dataclasses.field()

    shardIterator = field("shardIterator")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetShardIteratorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetShardIteratorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsInputPaginate:
    boto3_raw_data: "type_defs.ListStreamsInputPaginateTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")
    tableName = field("tableName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStreamsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStreamInputPaginate:
    boto3_raw_data: "type_defs.GetStreamInputPaginateTypeDef" = dataclasses.field()

    streamArn = field("streamArn")

    @cached_property
    def shardFilter(self):  # pragma: no cover
        return ShardFilter.make_one(self.boto3_raw_data["shardFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStreamInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStreamInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStreamInput:
    boto3_raw_data: "type_defs.GetStreamInputTypeDef" = dataclasses.field()

    streamArn = field("streamArn")
    maxResults = field("maxResults")

    @cached_property
    def shardFilter(self):  # pragma: no cover
        return ShardFilter.make_one(self.boto3_raw_data["shardFilter"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStreamInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetStreamInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyspacesCellMapDefinition:
    boto3_raw_data: "type_defs.KeyspacesCellMapDefinitionTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @cached_property
    def metadata(self):  # pragma: no cover
        return KeyspacesMetadata.make_one(self.boto3_raw_data["metadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeyspacesCellMapDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyspacesCellMapDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyspacesCell:
    boto3_raw_data: "type_defs.KeyspacesCellTypeDef" = dataclasses.field()

    value = field("value")

    @cached_property
    def metadata(self):  # pragma: no cover
        return KeyspacesMetadata.make_one(self.boto3_raw_data["metadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyspacesCellTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyspacesCellTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsOutput:
    boto3_raw_data: "type_defs.ListStreamsOutputTypeDef" = dataclasses.field()

    @cached_property
    def streams(self):  # pragma: no cover
        return Stream.make_many(self.boto3_raw_data["streams"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStreamsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Shard:
    boto3_raw_data: "type_defs.ShardTypeDef" = dataclasses.field()

    shardId = field("shardId")

    @cached_property
    def sequenceNumberRange(self):  # pragma: no cover
        return SequenceNumberRange.make_one(self.boto3_raw_data["sequenceNumberRange"])

    parentShardIds = field("parentShardIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShardTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyspacesCellValue:
    boto3_raw_data: "type_defs.KeyspacesCellValueTypeDef" = dataclasses.field()

    asciiT = field("asciiT")
    bigintT = field("bigintT")
    blobT = field("blobT")
    boolT = field("boolT")
    counterT = field("counterT")
    dateT = field("dateT")
    decimalT = field("decimalT")
    doubleT = field("doubleT")
    floatT = field("floatT")
    inetT = field("inetT")
    intT = field("intT")

    @cached_property
    def listT(self):  # pragma: no cover
        return KeyspacesCell.make_many(self.boto3_raw_data["listT"])

    @cached_property
    def mapT(self):  # pragma: no cover
        return KeyspacesCellMapDefinition.make_many(self.boto3_raw_data["mapT"])

    @cached_property
    def setT(self):  # pragma: no cover
        return KeyspacesCell.make_many(self.boto3_raw_data["setT"])

    smallintT = field("smallintT")
    textT = field("textT")
    timeT = field("timeT")
    timestampT = field("timestampT")
    timeuuidT = field("timeuuidT")
    tinyintT = field("tinyintT")

    @cached_property
    def tupleT(self):  # pragma: no cover
        return KeyspacesCell.make_many(self.boto3_raw_data["tupleT"])

    uuidT = field("uuidT")
    varcharT = field("varcharT")
    varintT = field("varintT")
    udtT = field("udtT")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeyspacesCellValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyspacesCellValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyspacesRow:
    boto3_raw_data: "type_defs.KeyspacesRowTypeDef" = dataclasses.field()

    valueCells = field("valueCells")
    staticCells = field("staticCells")

    @cached_property
    def rowMetadata(self):  # pragma: no cover
        return KeyspacesMetadata.make_one(self.boto3_raw_data["rowMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyspacesRowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyspacesRowTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStreamOutput:
    boto3_raw_data: "type_defs.GetStreamOutputTypeDef" = dataclasses.field()

    streamArn = field("streamArn")
    streamLabel = field("streamLabel")
    streamStatus = field("streamStatus")
    streamViewType = field("streamViewType")
    creationRequestDateTime = field("creationRequestDateTime")
    keyspaceName = field("keyspaceName")
    tableName = field("tableName")

    @cached_property
    def shards(self):  # pragma: no cover
        return Shard.make_many(self.boto3_raw_data["shards"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStreamOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetStreamOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Record:
    boto3_raw_data: "type_defs.RecordTypeDef" = dataclasses.field()

    eventVersion = field("eventVersion")
    createdAt = field("createdAt")
    origin = field("origin")
    partitionKeys = field("partitionKeys")
    clusteringKeys = field("clusteringKeys")

    @cached_property
    def newImage(self):  # pragma: no cover
        return KeyspacesRow.make_one(self.boto3_raw_data["newImage"])

    @cached_property
    def oldImage(self):  # pragma: no cover
        return KeyspacesRow.make_one(self.boto3_raw_data["oldImage"])

    sequenceNumber = field("sequenceNumber")

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
class GetRecordsOutput:
    boto3_raw_data: "type_defs.GetRecordsOutputTypeDef" = dataclasses.field()

    @cached_property
    def changeRecords(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["changeRecords"])

    nextShardIterator = field("nextShardIterator")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRecordsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecordsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
