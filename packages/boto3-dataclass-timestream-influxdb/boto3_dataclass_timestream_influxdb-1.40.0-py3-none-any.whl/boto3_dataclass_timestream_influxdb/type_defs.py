# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_timestream_influxdb import type_defs


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
class DbClusterSummary:
    boto3_raw_data: "type_defs.DbClusterSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    endpoint = field("endpoint")
    readerEndpoint = field("readerEndpoint")
    port = field("port")
    deploymentType = field("deploymentType")
    dbInstanceType = field("dbInstanceType")
    networkType = field("networkType")
    dbStorageType = field("dbStorageType")
    allocatedStorage = field("allocatedStorage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DbClusterSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DbClusterSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbInstanceForClusterSummary:
    boto3_raw_data: "type_defs.DbInstanceForClusterSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    endpoint = field("endpoint")
    port = field("port")
    networkType = field("networkType")
    dbInstanceType = field("dbInstanceType")
    dbStorageType = field("dbStorageType")
    allocatedStorage = field("allocatedStorage")
    deploymentType = field("deploymentType")
    instanceMode = field("instanceMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DbInstanceForClusterSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DbInstanceForClusterSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbInstanceSummary:
    boto3_raw_data: "type_defs.DbInstanceSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    endpoint = field("endpoint")
    port = field("port")
    networkType = field("networkType")
    dbInstanceType = field("dbInstanceType")
    dbStorageType = field("dbStorageType")
    allocatedStorage = field("allocatedStorage")
    deploymentType = field("deploymentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DbInstanceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DbInstanceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbParameterGroupSummary:
    boto3_raw_data: "type_defs.DbParameterGroupSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DbParameterGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DbParameterGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDbClusterInput:
    boto3_raw_data: "type_defs.DeleteDbClusterInputTypeDef" = dataclasses.field()

    dbClusterId = field("dbClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDbClusterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDbClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDbInstanceInput:
    boto3_raw_data: "type_defs.DeleteDbInstanceInputTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDbInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDbInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Duration:
    boto3_raw_data: "type_defs.DurationTypeDef" = dataclasses.field()

    durationType = field("durationType")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DurationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDbClusterInput:
    boto3_raw_data: "type_defs.GetDbClusterInputTypeDef" = dataclasses.field()

    dbClusterId = field("dbClusterId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDbClusterInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDbClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDbInstanceInput:
    boto3_raw_data: "type_defs.GetDbInstanceInputTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDbInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDbInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDbParameterGroupInput:
    boto3_raw_data: "type_defs.GetDbParameterGroupInputTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDbParameterGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDbParameterGroupInputTypeDef"]
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
class ListDbClustersInput:
    boto3_raw_data: "type_defs.ListDbClustersInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbClustersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbClustersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbInstancesForClusterInput:
    boto3_raw_data: "type_defs.ListDbInstancesForClusterInputTypeDef" = (
        dataclasses.field()
    )

    dbClusterId = field("dbClusterId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDbInstancesForClusterInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbInstancesForClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbInstancesInput:
    boto3_raw_data: "type_defs.ListDbInstancesInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbParameterGroupsInput:
    boto3_raw_data: "type_defs.ListDbParameterGroupsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbParameterGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbParameterGroupsInputTypeDef"]
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

    resourceArn = field("resourceArn")

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

    bucketName = field("bucketName")
    enabled = field("enabled")

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tags = field("tags")

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
    tagKeys = field("tagKeys")

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
class CreateDbClusterOutput:
    boto3_raw_data: "type_defs.CreateDbClusterOutputTypeDef" = dataclasses.field()

    dbClusterId = field("dbClusterId")
    dbClusterStatus = field("dbClusterStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDbClusterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDbClusterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDbClusterOutput:
    boto3_raw_data: "type_defs.DeleteDbClusterOutputTypeDef" = dataclasses.field()

    dbClusterStatus = field("dbClusterStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDbClusterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDbClusterOutputTypeDef"]
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
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    tags = field("tags")

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
class UpdateDbClusterOutput:
    boto3_raw_data: "type_defs.UpdateDbClusterOutputTypeDef" = dataclasses.field()

    dbClusterStatus = field("dbClusterStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDbClusterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDbClusterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbClustersOutput:
    boto3_raw_data: "type_defs.ListDbClustersOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return DbClusterSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbClustersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbClustersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbInstancesForClusterOutput:
    boto3_raw_data: "type_defs.ListDbInstancesForClusterOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return DbInstanceForClusterSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDbInstancesForClusterOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbInstancesForClusterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbInstancesOutput:
    boto3_raw_data: "type_defs.ListDbInstancesOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return DbInstanceSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbInstancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbParameterGroupsOutput:
    boto3_raw_data: "type_defs.ListDbParameterGroupsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return DbParameterGroupSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbParameterGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbParameterGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InfluxDBv2Parameters:
    boto3_raw_data: "type_defs.InfluxDBv2ParametersTypeDef" = dataclasses.field()

    fluxLogEnabled = field("fluxLogEnabled")
    logLevel = field("logLevel")
    noTasks = field("noTasks")
    queryConcurrency = field("queryConcurrency")
    queryQueueSize = field("queryQueueSize")
    tracingType = field("tracingType")
    metricsDisabled = field("metricsDisabled")

    @cached_property
    def httpIdleTimeout(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["httpIdleTimeout"])

    @cached_property
    def httpReadHeaderTimeout(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["httpReadHeaderTimeout"])

    @cached_property
    def httpReadTimeout(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["httpReadTimeout"])

    @cached_property
    def httpWriteTimeout(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["httpWriteTimeout"])

    influxqlMaxSelectBuckets = field("influxqlMaxSelectBuckets")
    influxqlMaxSelectPoint = field("influxqlMaxSelectPoint")
    influxqlMaxSelectSeries = field("influxqlMaxSelectSeries")
    pprofDisabled = field("pprofDisabled")
    queryInitialMemoryBytes = field("queryInitialMemoryBytes")
    queryMaxMemoryBytes = field("queryMaxMemoryBytes")
    queryMemoryBytes = field("queryMemoryBytes")
    sessionLength = field("sessionLength")
    sessionRenewDisabled = field("sessionRenewDisabled")
    storageCacheMaxMemorySize = field("storageCacheMaxMemorySize")
    storageCacheSnapshotMemorySize = field("storageCacheSnapshotMemorySize")

    @cached_property
    def storageCacheSnapshotWriteColdDuration(self):  # pragma: no cover
        return Duration.make_one(
            self.boto3_raw_data["storageCacheSnapshotWriteColdDuration"]
        )

    @cached_property
    def storageCompactFullWriteColdDuration(self):  # pragma: no cover
        return Duration.make_one(
            self.boto3_raw_data["storageCompactFullWriteColdDuration"]
        )

    storageCompactThroughputBurst = field("storageCompactThroughputBurst")
    storageMaxConcurrentCompactions = field("storageMaxConcurrentCompactions")
    storageMaxIndexLogFileSize = field("storageMaxIndexLogFileSize")
    storageNoValidateFieldSize = field("storageNoValidateFieldSize")

    @cached_property
    def storageRetentionCheckInterval(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["storageRetentionCheckInterval"])

    storageSeriesFileMaxConcurrentSnapshotCompactions = field(
        "storageSeriesFileMaxConcurrentSnapshotCompactions"
    )
    storageSeriesIdSetCacheSize = field("storageSeriesIdSetCacheSize")
    storageWalMaxConcurrentWrites = field("storageWalMaxConcurrentWrites")

    @cached_property
    def storageWalMaxWriteDelay(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["storageWalMaxWriteDelay"])

    uiDisabled = field("uiDisabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InfluxDBv2ParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InfluxDBv2ParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbClustersInputPaginate:
    boto3_raw_data: "type_defs.ListDbClustersInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbClustersInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbClustersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbInstancesForClusterInputPaginate:
    boto3_raw_data: "type_defs.ListDbInstancesForClusterInputPaginateTypeDef" = (
        dataclasses.field()
    )

    dbClusterId = field("dbClusterId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDbInstancesForClusterInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbInstancesForClusterInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbInstancesInputPaginate:
    boto3_raw_data: "type_defs.ListDbInstancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDbInstancesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDbParameterGroupsInputPaginate:
    boto3_raw_data: "type_defs.ListDbParameterGroupsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDbParameterGroupsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDbParameterGroupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogDeliveryConfiguration:
    boto3_raw_data: "type_defs.LogDeliveryConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return S3Configuration.make_one(self.boto3_raw_data["s3Configuration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogDeliveryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogDeliveryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Parameters:
    boto3_raw_data: "type_defs.ParametersTypeDef" = dataclasses.field()

    @cached_property
    def InfluxDBv2(self):  # pragma: no cover
        return InfluxDBv2Parameters.make_one(self.boto3_raw_data["InfluxDBv2"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParametersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDbClusterInput:
    boto3_raw_data: "type_defs.CreateDbClusterInputTypeDef" = dataclasses.field()

    name = field("name")
    password = field("password")
    dbInstanceType = field("dbInstanceType")
    allocatedStorage = field("allocatedStorage")
    vpcSubnetIds = field("vpcSubnetIds")
    vpcSecurityGroupIds = field("vpcSecurityGroupIds")
    deploymentType = field("deploymentType")
    username = field("username")
    organization = field("organization")
    bucket = field("bucket")
    port = field("port")
    dbParameterGroupIdentifier = field("dbParameterGroupIdentifier")
    dbStorageType = field("dbStorageType")
    networkType = field("networkType")
    publiclyAccessible = field("publiclyAccessible")
    failoverMode = field("failoverMode")

    @cached_property
    def logDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_one(
            self.boto3_raw_data["logDeliveryConfiguration"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDbClusterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDbClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDbInstanceInput:
    boto3_raw_data: "type_defs.CreateDbInstanceInputTypeDef" = dataclasses.field()

    name = field("name")
    password = field("password")
    dbInstanceType = field("dbInstanceType")
    vpcSubnetIds = field("vpcSubnetIds")
    vpcSecurityGroupIds = field("vpcSecurityGroupIds")
    allocatedStorage = field("allocatedStorage")
    username = field("username")
    organization = field("organization")
    bucket = field("bucket")
    publiclyAccessible = field("publiclyAccessible")
    dbStorageType = field("dbStorageType")
    dbParameterGroupIdentifier = field("dbParameterGroupIdentifier")
    deploymentType = field("deploymentType")

    @cached_property
    def logDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_one(
            self.boto3_raw_data["logDeliveryConfiguration"]
        )

    tags = field("tags")
    port = field("port")
    networkType = field("networkType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDbInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDbInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDbInstanceOutput:
    boto3_raw_data: "type_defs.CreateDbInstanceOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    endpoint = field("endpoint")
    port = field("port")
    networkType = field("networkType")
    dbInstanceType = field("dbInstanceType")
    dbStorageType = field("dbStorageType")
    allocatedStorage = field("allocatedStorage")
    deploymentType = field("deploymentType")
    vpcSubnetIds = field("vpcSubnetIds")
    publiclyAccessible = field("publiclyAccessible")
    vpcSecurityGroupIds = field("vpcSecurityGroupIds")
    dbParameterGroupIdentifier = field("dbParameterGroupIdentifier")
    availabilityZone = field("availabilityZone")
    secondaryAvailabilityZone = field("secondaryAvailabilityZone")

    @cached_property
    def logDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_one(
            self.boto3_raw_data["logDeliveryConfiguration"]
        )

    influxAuthParametersSecretArn = field("influxAuthParametersSecretArn")
    dbClusterId = field("dbClusterId")
    instanceMode = field("instanceMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDbInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDbInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDbInstanceOutput:
    boto3_raw_data: "type_defs.DeleteDbInstanceOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    endpoint = field("endpoint")
    port = field("port")
    networkType = field("networkType")
    dbInstanceType = field("dbInstanceType")
    dbStorageType = field("dbStorageType")
    allocatedStorage = field("allocatedStorage")
    deploymentType = field("deploymentType")
    vpcSubnetIds = field("vpcSubnetIds")
    publiclyAccessible = field("publiclyAccessible")
    vpcSecurityGroupIds = field("vpcSecurityGroupIds")
    dbParameterGroupIdentifier = field("dbParameterGroupIdentifier")
    availabilityZone = field("availabilityZone")
    secondaryAvailabilityZone = field("secondaryAvailabilityZone")

    @cached_property
    def logDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_one(
            self.boto3_raw_data["logDeliveryConfiguration"]
        )

    influxAuthParametersSecretArn = field("influxAuthParametersSecretArn")
    dbClusterId = field("dbClusterId")
    instanceMode = field("instanceMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDbInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDbInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDbClusterOutput:
    boto3_raw_data: "type_defs.GetDbClusterOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    endpoint = field("endpoint")
    readerEndpoint = field("readerEndpoint")
    port = field("port")
    deploymentType = field("deploymentType")
    dbInstanceType = field("dbInstanceType")
    networkType = field("networkType")
    dbStorageType = field("dbStorageType")
    allocatedStorage = field("allocatedStorage")
    publiclyAccessible = field("publiclyAccessible")
    dbParameterGroupIdentifier = field("dbParameterGroupIdentifier")

    @cached_property
    def logDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_one(
            self.boto3_raw_data["logDeliveryConfiguration"]
        )

    influxAuthParametersSecretArn = field("influxAuthParametersSecretArn")
    vpcSubnetIds = field("vpcSubnetIds")
    vpcSecurityGroupIds = field("vpcSecurityGroupIds")
    failoverMode = field("failoverMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDbClusterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDbClusterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDbInstanceOutput:
    boto3_raw_data: "type_defs.GetDbInstanceOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    endpoint = field("endpoint")
    port = field("port")
    networkType = field("networkType")
    dbInstanceType = field("dbInstanceType")
    dbStorageType = field("dbStorageType")
    allocatedStorage = field("allocatedStorage")
    deploymentType = field("deploymentType")
    vpcSubnetIds = field("vpcSubnetIds")
    publiclyAccessible = field("publiclyAccessible")
    vpcSecurityGroupIds = field("vpcSecurityGroupIds")
    dbParameterGroupIdentifier = field("dbParameterGroupIdentifier")
    availabilityZone = field("availabilityZone")
    secondaryAvailabilityZone = field("secondaryAvailabilityZone")

    @cached_property
    def logDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_one(
            self.boto3_raw_data["logDeliveryConfiguration"]
        )

    influxAuthParametersSecretArn = field("influxAuthParametersSecretArn")
    dbClusterId = field("dbClusterId")
    instanceMode = field("instanceMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDbInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDbInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDbClusterInput:
    boto3_raw_data: "type_defs.UpdateDbClusterInputTypeDef" = dataclasses.field()

    dbClusterId = field("dbClusterId")

    @cached_property
    def logDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_one(
            self.boto3_raw_data["logDeliveryConfiguration"]
        )

    dbParameterGroupIdentifier = field("dbParameterGroupIdentifier")
    port = field("port")
    dbInstanceType = field("dbInstanceType")
    failoverMode = field("failoverMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDbClusterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDbClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDbInstanceInput:
    boto3_raw_data: "type_defs.UpdateDbInstanceInputTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @cached_property
    def logDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_one(
            self.boto3_raw_data["logDeliveryConfiguration"]
        )

    dbParameterGroupIdentifier = field("dbParameterGroupIdentifier")
    port = field("port")
    dbInstanceType = field("dbInstanceType")
    deploymentType = field("deploymentType")
    dbStorageType = field("dbStorageType")
    allocatedStorage = field("allocatedStorage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDbInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDbInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDbInstanceOutput:
    boto3_raw_data: "type_defs.UpdateDbInstanceOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    endpoint = field("endpoint")
    port = field("port")
    networkType = field("networkType")
    dbInstanceType = field("dbInstanceType")
    dbStorageType = field("dbStorageType")
    allocatedStorage = field("allocatedStorage")
    deploymentType = field("deploymentType")
    vpcSubnetIds = field("vpcSubnetIds")
    publiclyAccessible = field("publiclyAccessible")
    vpcSecurityGroupIds = field("vpcSecurityGroupIds")
    dbParameterGroupIdentifier = field("dbParameterGroupIdentifier")
    availabilityZone = field("availabilityZone")
    secondaryAvailabilityZone = field("secondaryAvailabilityZone")

    @cached_property
    def logDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_one(
            self.boto3_raw_data["logDeliveryConfiguration"]
        )

    influxAuthParametersSecretArn = field("influxAuthParametersSecretArn")
    dbClusterId = field("dbClusterId")
    instanceMode = field("instanceMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDbInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDbInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDbParameterGroupInput:
    boto3_raw_data: "type_defs.CreateDbParameterGroupInputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def parameters(self):  # pragma: no cover
        return Parameters.make_one(self.boto3_raw_data["parameters"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDbParameterGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDbParameterGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDbParameterGroupOutput:
    boto3_raw_data: "type_defs.CreateDbParameterGroupOutputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    arn = field("arn")
    description = field("description")

    @cached_property
    def parameters(self):  # pragma: no cover
        return Parameters.make_one(self.boto3_raw_data["parameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDbParameterGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDbParameterGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDbParameterGroupOutput:
    boto3_raw_data: "type_defs.GetDbParameterGroupOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    description = field("description")

    @cached_property
    def parameters(self):  # pragma: no cover
        return Parameters.make_one(self.boto3_raw_data["parameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDbParameterGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDbParameterGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
