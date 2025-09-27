# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_keyspaces import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class TargetTrackingScalingPolicyConfiguration:
    boto3_raw_data: "type_defs.TargetTrackingScalingPolicyConfigurationTypeDef" = (
        dataclasses.field()
    )

    targetValue = field("targetValue")
    disableScaleIn = field("disableScaleIn")
    scaleInCooldown = field("scaleInCooldown")
    scaleOutCooldown = field("scaleOutCooldown")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetTrackingScalingPolicyConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingScalingPolicyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacitySpecificationSummary:
    boto3_raw_data: "type_defs.CapacitySpecificationSummaryTypeDef" = (
        dataclasses.field()
    )

    throughputMode = field("throughputMode")
    readCapacityUnits = field("readCapacityUnits")
    writeCapacityUnits = field("writeCapacityUnits")
    lastUpdateToPayPerRequestTimestamp = field("lastUpdateToPayPerRequestTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacitySpecificationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacitySpecificationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacitySpecification:
    boto3_raw_data: "type_defs.CapacitySpecificationTypeDef" = dataclasses.field()

    throughputMode = field("throughputMode")
    readCapacityUnits = field("readCapacityUnits")
    writeCapacityUnits = field("writeCapacityUnits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacitySpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacitySpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CdcSpecificationSummary:
    boto3_raw_data: "type_defs.CdcSpecificationSummaryTypeDef" = dataclasses.field()

    status = field("status")
    viewType = field("viewType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CdcSpecificationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CdcSpecificationSummaryTypeDef"]
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

    key = field("key")
    value = field("value")

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
class ClientSideTimestamps:
    boto3_raw_data: "type_defs.ClientSideTimestampsTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientSideTimestampsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientSideTimestampsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusteringKey:
    boto3_raw_data: "type_defs.ClusteringKeyTypeDef" = dataclasses.field()

    name = field("name")
    orderBy = field("orderBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusteringKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusteringKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnDefinition:
    boto3_raw_data: "type_defs.ColumnDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Comment:
    boto3_raw_data: "type_defs.CommentTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationSpecification:
    boto3_raw_data: "type_defs.ReplicationSpecificationTypeDef" = dataclasses.field()

    replicationStrategy = field("replicationStrategy")
    regionList = field("regionList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationSpecificationTypeDef"]
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
class EncryptionSpecification:
    boto3_raw_data: "type_defs.EncryptionSpecificationTypeDef" = dataclasses.field()

    type = field("type")
    kmsKeyIdentifier = field("kmsKeyIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PointInTimeRecovery:
    boto3_raw_data: "type_defs.PointInTimeRecoveryTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PointInTimeRecoveryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PointInTimeRecoveryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeToLive:
    boto3_raw_data: "type_defs.TimeToLiveTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeToLiveTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeToLiveTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldDefinition:
    boto3_raw_data: "type_defs.FieldDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeyspaceRequest:
    boto3_raw_data: "type_defs.DeleteKeyspaceRequestTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKeyspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeyspaceRequestTypeDef"]
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

    keyspaceName = field("keyspaceName")
    tableName = field("tableName")

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
class DeleteTypeRequest:
    boto3_raw_data: "type_defs.DeleteTypeRequestTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")
    typeName = field("typeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTypeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyspaceRequest:
    boto3_raw_data: "type_defs.GetKeyspaceRequestTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationGroupStatus:
    boto3_raw_data: "type_defs.ReplicationGroupStatusTypeDef" = dataclasses.field()

    region = field("region")
    keyspaceStatus = field("keyspaceStatus")
    tablesReplicationProgress = field("tablesReplicationProgress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationGroupStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationGroupStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableAutoScalingSettingsRequest:
    boto3_raw_data: "type_defs.GetTableAutoScalingSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    keyspaceName = field("keyspaceName")
    tableName = field("tableName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTableAutoScalingSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableAutoScalingSettingsRequestTypeDef"]
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

    keyspaceName = field("keyspaceName")
    tableName = field("tableName")

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
class PointInTimeRecoverySummary:
    boto3_raw_data: "type_defs.PointInTimeRecoverySummaryTypeDef" = dataclasses.field()

    status = field("status")
    earliestRestorableTimestamp = field("earliestRestorableTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PointInTimeRecoverySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PointInTimeRecoverySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTypeRequest:
    boto3_raw_data: "type_defs.GetTypeRequestTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")
    typeName = field("typeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTypeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTypeRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyspaceSummary:
    boto3_raw_data: "type_defs.KeyspaceSummaryTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")
    resourceArn = field("resourceArn")
    replicationStrategy = field("replicationStrategy")
    replicationRegions = field("replicationRegions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyspaceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyspaceSummaryTypeDef"]],
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
class ListKeyspacesRequest:
    boto3_raw_data: "type_defs.ListKeyspacesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyspacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyspacesRequestTypeDef"]
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

    keyspaceName = field("keyspaceName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

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

    keyspaceName = field("keyspaceName")
    tableName = field("tableName")
    resourceArn = field("resourceArn")

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
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

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
class ListTypesRequest:
    boto3_raw_data: "type_defs.ListTypesRequestTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTypesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypesRequestTypeDef"]
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

    name = field("name")

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
class StaticColumn:
    boto3_raw_data: "type_defs.StaticColumnTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StaticColumnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StaticColumnTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingPolicy:
    boto3_raw_data: "type_defs.AutoScalingPolicyTypeDef" = dataclasses.field()

    @cached_property
    def targetTrackingScalingPolicyConfiguration(self):  # pragma: no cover
        return TargetTrackingScalingPolicyConfiguration.make_one(
            self.boto3_raw_data["targetTrackingScalingPolicyConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoScalingPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaSpecificationSummary:
    boto3_raw_data: "type_defs.ReplicaSpecificationSummaryTypeDef" = dataclasses.field()

    region = field("region")
    status = field("status")

    @cached_property
    def capacitySpecification(self):  # pragma: no cover
        return CapacitySpecificationSummary.make_one(
            self.boto3_raw_data["capacitySpecification"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicaSpecificationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaSpecificationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CdcSpecification:
    boto3_raw_data: "type_defs.CdcSpecificationTypeDef" = dataclasses.field()

    status = field("status")
    viewType = field("viewType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    propagateTags = field("propagateTags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CdcSpecificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CdcSpecificationTypeDef"]
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

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class CreateKeyspaceRequest:
    boto3_raw_data: "type_defs.CreateKeyspaceRequestTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def replicationSpecification(self):  # pragma: no cover
        return ReplicationSpecification.make_one(
            self.boto3_raw_data["replicationSpecification"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKeyspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKeyspaceRequest:
    boto3_raw_data: "type_defs.UpdateKeyspaceRequestTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")

    @cached_property
    def replicationSpecification(self):  # pragma: no cover
        return ReplicationSpecification.make_one(
            self.boto3_raw_data["replicationSpecification"]
        )

    @cached_property
    def clientSideTimestamps(self):  # pragma: no cover
        return ClientSideTimestamps.make_one(
            self.boto3_raw_data["clientSideTimestamps"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKeyspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKeyspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyspaceResponse:
    boto3_raw_data: "type_defs.CreateKeyspaceResponseTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKeyspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyspaceResponseTypeDef"]
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

    resourceArn = field("resourceArn")

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
class CreateTypeResponse:
    boto3_raw_data: "type_defs.CreateTypeResponseTypeDef" = dataclasses.field()

    keyspaceArn = field("keyspaceArn")
    typeName = field("typeName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTypeResponse:
    boto3_raw_data: "type_defs.DeleteTypeResponseTypeDef" = dataclasses.field()

    keyspaceArn = field("keyspaceArn")
    typeName = field("typeName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTypeResponseTypeDef"]
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
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

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
class ListTypesResponse:
    boto3_raw_data: "type_defs.ListTypesResponseTypeDef" = dataclasses.field()

    types = field("types")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTypesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTableResponse:
    boto3_raw_data: "type_defs.RestoreTableResponseTypeDef" = dataclasses.field()

    restoredTableARN = field("restoredTableARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreTableResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKeyspaceResponse:
    boto3_raw_data: "type_defs.UpdateKeyspaceResponseTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKeyspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKeyspaceResponseTypeDef"]
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

    resourceArn = field("resourceArn")

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
class CreateTypeRequest:
    boto3_raw_data: "type_defs.CreateTypeRequestTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")
    typeName = field("typeName")

    @cached_property
    def fieldDefinitions(self):  # pragma: no cover
        return FieldDefinition.make_many(self.boto3_raw_data["fieldDefinitions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTypeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTypeResponse:
    boto3_raw_data: "type_defs.GetTypeResponseTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")
    typeName = field("typeName")

    @cached_property
    def fieldDefinitions(self):  # pragma: no cover
        return FieldDefinition.make_many(self.boto3_raw_data["fieldDefinitions"])

    lastModifiedTimestamp = field("lastModifiedTimestamp")
    status = field("status")
    directReferringTables = field("directReferringTables")
    directParentTypes = field("directParentTypes")
    maxNestingDepth = field("maxNestingDepth")
    keyspaceArn = field("keyspaceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTypeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTypeResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyspaceResponse:
    boto3_raw_data: "type_defs.GetKeyspaceResponseTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")
    resourceArn = field("resourceArn")
    replicationStrategy = field("replicationStrategy")
    replicationRegions = field("replicationRegions")

    @cached_property
    def replicationGroupStatuses(self):  # pragma: no cover
        return ReplicationGroupStatus.make_many(
            self.boto3_raw_data["replicationGroupStatuses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyspaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyspacesResponse:
    boto3_raw_data: "type_defs.ListKeyspacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def keyspaces(self):  # pragma: no cover
        return KeyspaceSummary.make_many(self.boto3_raw_data["keyspaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyspacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyspacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyspacesRequestPaginate:
    boto3_raw_data: "type_defs.ListKeyspacesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyspacesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyspacesRequestPaginateTypeDef"]
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

    keyspaceName = field("keyspaceName")

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
class ListTagsForResourceRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTagsForResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypesRequestPaginate:
    boto3_raw_data: "type_defs.ListTypesRequestPaginateTypeDef" = dataclasses.field()

    keyspaceName = field("keyspaceName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTypesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypesRequestPaginateTypeDef"]
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

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

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
class SchemaDefinitionOutput:
    boto3_raw_data: "type_defs.SchemaDefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def allColumns(self):  # pragma: no cover
        return ColumnDefinition.make_many(self.boto3_raw_data["allColumns"])

    @cached_property
    def partitionKeys(self):  # pragma: no cover
        return PartitionKey.make_many(self.boto3_raw_data["partitionKeys"])

    @cached_property
    def clusteringKeys(self):  # pragma: no cover
        return ClusteringKey.make_many(self.boto3_raw_data["clusteringKeys"])

    @cached_property
    def staticColumns(self):  # pragma: no cover
        return StaticColumn.make_many(self.boto3_raw_data["staticColumns"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaDefinition:
    boto3_raw_data: "type_defs.SchemaDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def allColumns(self):  # pragma: no cover
        return ColumnDefinition.make_many(self.boto3_raw_data["allColumns"])

    @cached_property
    def partitionKeys(self):  # pragma: no cover
        return PartitionKey.make_many(self.boto3_raw_data["partitionKeys"])

    @cached_property
    def clusteringKeys(self):  # pragma: no cover
        return ClusteringKey.make_many(self.boto3_raw_data["clusteringKeys"])

    @cached_property
    def staticColumns(self):  # pragma: no cover
        return StaticColumn.make_many(self.boto3_raw_data["staticColumns"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingSettings:
    boto3_raw_data: "type_defs.AutoScalingSettingsTypeDef" = dataclasses.field()

    autoScalingDisabled = field("autoScalingDisabled")
    minimumUnits = field("minimumUnits")
    maximumUnits = field("maximumUnits")

    @cached_property
    def scalingPolicy(self):  # pragma: no cover
        return AutoScalingPolicy.make_one(self.boto3_raw_data["scalingPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingSettingsTypeDef"]
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

    keyspaceName = field("keyspaceName")
    tableName = field("tableName")
    resourceArn = field("resourceArn")
    creationTimestamp = field("creationTimestamp")
    status = field("status")

    @cached_property
    def schemaDefinition(self):  # pragma: no cover
        return SchemaDefinitionOutput.make_one(self.boto3_raw_data["schemaDefinition"])

    @cached_property
    def capacitySpecification(self):  # pragma: no cover
        return CapacitySpecificationSummary.make_one(
            self.boto3_raw_data["capacitySpecification"]
        )

    @cached_property
    def encryptionSpecification(self):  # pragma: no cover
        return EncryptionSpecification.make_one(
            self.boto3_raw_data["encryptionSpecification"]
        )

    @cached_property
    def pointInTimeRecovery(self):  # pragma: no cover
        return PointInTimeRecoverySummary.make_one(
            self.boto3_raw_data["pointInTimeRecovery"]
        )

    @cached_property
    def ttl(self):  # pragma: no cover
        return TimeToLive.make_one(self.boto3_raw_data["ttl"])

    defaultTimeToLive = field("defaultTimeToLive")

    @cached_property
    def comment(self):  # pragma: no cover
        return Comment.make_one(self.boto3_raw_data["comment"])

    @cached_property
    def clientSideTimestamps(self):  # pragma: no cover
        return ClientSideTimestamps.make_one(
            self.boto3_raw_data["clientSideTimestamps"]
        )

    @cached_property
    def replicaSpecifications(self):  # pragma: no cover
        return ReplicaSpecificationSummary.make_many(
            self.boto3_raw_data["replicaSpecifications"]
        )

    latestStreamArn = field("latestStreamArn")

    @cached_property
    def cdcSpecification(self):  # pragma: no cover
        return CdcSpecificationSummary.make_one(self.boto3_raw_data["cdcSpecification"])

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
class AutoScalingSpecification:
    boto3_raw_data: "type_defs.AutoScalingSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def writeCapacityAutoScaling(self):  # pragma: no cover
        return AutoScalingSettings.make_one(
            self.boto3_raw_data["writeCapacityAutoScaling"]
        )

    @cached_property
    def readCapacityAutoScaling(self):  # pragma: no cover
        return AutoScalingSettings.make_one(
            self.boto3_raw_data["readCapacityAutoScaling"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaSpecification:
    boto3_raw_data: "type_defs.ReplicaSpecificationTypeDef" = dataclasses.field()

    region = field("region")
    readCapacityUnits = field("readCapacityUnits")

    @cached_property
    def readCapacityAutoScaling(self):  # pragma: no cover
        return AutoScalingSettings.make_one(
            self.boto3_raw_data["readCapacityAutoScaling"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicaSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaAutoScalingSpecification:
    boto3_raw_data: "type_defs.ReplicaAutoScalingSpecificationTypeDef" = (
        dataclasses.field()
    )

    region = field("region")

    @cached_property
    def autoScalingSpecification(self):  # pragma: no cover
        return AutoScalingSpecification.make_one(
            self.boto3_raw_data["autoScalingSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicaAutoScalingSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaAutoScalingSpecificationTypeDef"]
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

    keyspaceName = field("keyspaceName")
    tableName = field("tableName")
    schemaDefinition = field("schemaDefinition")

    @cached_property
    def comment(self):  # pragma: no cover
        return Comment.make_one(self.boto3_raw_data["comment"])

    @cached_property
    def capacitySpecification(self):  # pragma: no cover
        return CapacitySpecification.make_one(
            self.boto3_raw_data["capacitySpecification"]
        )

    @cached_property
    def encryptionSpecification(self):  # pragma: no cover
        return EncryptionSpecification.make_one(
            self.boto3_raw_data["encryptionSpecification"]
        )

    @cached_property
    def pointInTimeRecovery(self):  # pragma: no cover
        return PointInTimeRecovery.make_one(self.boto3_raw_data["pointInTimeRecovery"])

    @cached_property
    def ttl(self):  # pragma: no cover
        return TimeToLive.make_one(self.boto3_raw_data["ttl"])

    defaultTimeToLive = field("defaultTimeToLive")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def clientSideTimestamps(self):  # pragma: no cover
        return ClientSideTimestamps.make_one(
            self.boto3_raw_data["clientSideTimestamps"]
        )

    @cached_property
    def autoScalingSpecification(self):  # pragma: no cover
        return AutoScalingSpecification.make_one(
            self.boto3_raw_data["autoScalingSpecification"]
        )

    @cached_property
    def replicaSpecifications(self):  # pragma: no cover
        return ReplicaSpecification.make_many(
            self.boto3_raw_data["replicaSpecifications"]
        )

    @cached_property
    def cdcSpecification(self):  # pragma: no cover
        return CdcSpecification.make_one(self.boto3_raw_data["cdcSpecification"])

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
class RestoreTableRequest:
    boto3_raw_data: "type_defs.RestoreTableRequestTypeDef" = dataclasses.field()

    sourceKeyspaceName = field("sourceKeyspaceName")
    sourceTableName = field("sourceTableName")
    targetKeyspaceName = field("targetKeyspaceName")
    targetTableName = field("targetTableName")
    restoreTimestamp = field("restoreTimestamp")

    @cached_property
    def capacitySpecificationOverride(self):  # pragma: no cover
        return CapacitySpecification.make_one(
            self.boto3_raw_data["capacitySpecificationOverride"]
        )

    @cached_property
    def encryptionSpecificationOverride(self):  # pragma: no cover
        return EncryptionSpecification.make_one(
            self.boto3_raw_data["encryptionSpecificationOverride"]
        )

    @cached_property
    def pointInTimeRecoveryOverride(self):  # pragma: no cover
        return PointInTimeRecovery.make_one(
            self.boto3_raw_data["pointInTimeRecoveryOverride"]
        )

    @cached_property
    def tagsOverride(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tagsOverride"])

    @cached_property
    def autoScalingSpecification(self):  # pragma: no cover
        return AutoScalingSpecification.make_one(
            self.boto3_raw_data["autoScalingSpecification"]
        )

    @cached_property
    def replicaSpecifications(self):  # pragma: no cover
        return ReplicaSpecification.make_many(
            self.boto3_raw_data["replicaSpecifications"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreTableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableRequestTypeDef"]
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

    keyspaceName = field("keyspaceName")
    tableName = field("tableName")

    @cached_property
    def addColumns(self):  # pragma: no cover
        return ColumnDefinition.make_many(self.boto3_raw_data["addColumns"])

    @cached_property
    def capacitySpecification(self):  # pragma: no cover
        return CapacitySpecification.make_one(
            self.boto3_raw_data["capacitySpecification"]
        )

    @cached_property
    def encryptionSpecification(self):  # pragma: no cover
        return EncryptionSpecification.make_one(
            self.boto3_raw_data["encryptionSpecification"]
        )

    @cached_property
    def pointInTimeRecovery(self):  # pragma: no cover
        return PointInTimeRecovery.make_one(self.boto3_raw_data["pointInTimeRecovery"])

    @cached_property
    def ttl(self):  # pragma: no cover
        return TimeToLive.make_one(self.boto3_raw_data["ttl"])

    defaultTimeToLive = field("defaultTimeToLive")

    @cached_property
    def clientSideTimestamps(self):  # pragma: no cover
        return ClientSideTimestamps.make_one(
            self.boto3_raw_data["clientSideTimestamps"]
        )

    @cached_property
    def autoScalingSpecification(self):  # pragma: no cover
        return AutoScalingSpecification.make_one(
            self.boto3_raw_data["autoScalingSpecification"]
        )

    @cached_property
    def replicaSpecifications(self):  # pragma: no cover
        return ReplicaSpecification.make_many(
            self.boto3_raw_data["replicaSpecifications"]
        )

    @cached_property
    def cdcSpecification(self):  # pragma: no cover
        return CdcSpecification.make_one(self.boto3_raw_data["cdcSpecification"])

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
class GetTableAutoScalingSettingsResponse:
    boto3_raw_data: "type_defs.GetTableAutoScalingSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    keyspaceName = field("keyspaceName")
    tableName = field("tableName")
    resourceArn = field("resourceArn")

    @cached_property
    def autoScalingSpecification(self):  # pragma: no cover
        return AutoScalingSpecification.make_one(
            self.boto3_raw_data["autoScalingSpecification"]
        )

    @cached_property
    def replicaSpecifications(self):  # pragma: no cover
        return ReplicaAutoScalingSpecification.make_many(
            self.boto3_raw_data["replicaSpecifications"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTableAutoScalingSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableAutoScalingSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
