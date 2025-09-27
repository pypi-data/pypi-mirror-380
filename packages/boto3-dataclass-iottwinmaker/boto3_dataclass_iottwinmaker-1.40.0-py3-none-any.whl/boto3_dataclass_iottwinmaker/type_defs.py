# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iottwinmaker import type_defs


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
class BundleInformation:
    boto3_raw_data: "type_defs.BundleInformationTypeDef" = dataclasses.field()

    bundleNames = field("bundleNames")
    pricingTier = field("pricingTier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BundleInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BundleInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMetadataTransferJobRequest:
    boto3_raw_data: "type_defs.CancelMetadataTransferJobRequestTypeDef" = (
        dataclasses.field()
    )

    metadataTransferJobId = field("metadataTransferJobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelMetadataTransferJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMetadataTransferJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataTransferJobProgress:
    boto3_raw_data: "type_defs.MetadataTransferJobProgressTypeDef" = dataclasses.field()

    totalCount = field("totalCount")
    succeededCount = field("succeededCount")
    skippedCount = field("skippedCount")
    failedCount = field("failedCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataTransferJobProgressTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataTransferJobProgressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnDescription:
    boto3_raw_data: "type_defs.ColumnDescriptionTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentPropertyGroupRequest:
    boto3_raw_data: "type_defs.ComponentPropertyGroupRequestTypeDef" = (
        dataclasses.field()
    )

    groupType = field("groupType")
    propertyNames = field("propertyNames")
    updateType = field("updateType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComponentPropertyGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentPropertyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentPropertyGroupResponse:
    boto3_raw_data: "type_defs.ComponentPropertyGroupResponseTypeDef" = (
        dataclasses.field()
    )

    groupType = field("groupType")
    propertyNames = field("propertyNames")
    isInherited = field("isInherited")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComponentPropertyGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentPropertyGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositeComponentTypeRequest:
    boto3_raw_data: "type_defs.CompositeComponentTypeRequestTypeDef" = (
        dataclasses.field()
    )

    componentTypeId = field("componentTypeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CompositeComponentTypeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositeComponentTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositeComponentTypeResponse:
    boto3_raw_data: "type_defs.CompositeComponentTypeResponseTypeDef" = (
        dataclasses.field()
    )

    componentTypeId = field("componentTypeId")
    isInherited = field("isInherited")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CompositeComponentTypeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositeComponentTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyGroupRequest:
    boto3_raw_data: "type_defs.PropertyGroupRequestTypeDef" = dataclasses.field()

    groupType = field("groupType")
    propertyNames = field("propertyNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSceneRequest:
    boto3_raw_data: "type_defs.CreateSceneRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    sceneId = field("sceneId")
    contentLocation = field("contentLocation")
    description = field("description")
    capabilities = field("capabilities")
    tags = field("tags")
    sceneMetadata = field("sceneMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSceneRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSceneRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSyncJobRequest:
    boto3_raw_data: "type_defs.CreateSyncJobRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    syncSource = field("syncSource")
    syncRole = field("syncRole")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSyncJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSyncJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceRequest:
    boto3_raw_data: "type_defs.CreateWorkspaceRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    description = field("description")
    s3Location = field("s3Location")
    role = field("role")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunction:
    boto3_raw_data: "type_defs.LambdaFunctionTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaFunctionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Relationship:
    boto3_raw_data: "type_defs.RelationshipTypeDef" = dataclasses.field()

    targetComponentTypeId = field("targetComponentTypeId")
    relationshipType = field("relationshipType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelationshipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelationshipTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationshipValue:
    boto3_raw_data: "type_defs.RelationshipValueTypeDef" = dataclasses.field()

    targetEntityId = field("targetEntityId")
    targetComponentName = field("targetComponentName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelationshipValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationshipValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComponentTypeRequest:
    boto3_raw_data: "type_defs.DeleteComponentTypeRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    componentTypeId = field("componentTypeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteComponentTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComponentTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEntityRequest:
    boto3_raw_data: "type_defs.DeleteEntityRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    entityId = field("entityId")
    isRecursive = field("isRecursive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEntityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEntityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSceneRequest:
    boto3_raw_data: "type_defs.DeleteSceneRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    sceneId = field("sceneId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSceneRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSceneRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSyncJobRequest:
    boto3_raw_data: "type_defs.DeleteSyncJobRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    syncSource = field("syncSource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSyncJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSyncJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceRequest:
    boto3_raw_data: "type_defs.DeleteWorkspaceRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotTwinMakerDestinationConfiguration:
    boto3_raw_data: "type_defs.IotTwinMakerDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    workspace = field("workspace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IotTwinMakerDestinationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotTwinMakerDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationConfiguration:
    boto3_raw_data: "type_defs.S3DestinationConfigurationTypeDef" = dataclasses.field()

    location = field("location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityPropertyReferenceOutput:
    boto3_raw_data: "type_defs.EntityPropertyReferenceOutputTypeDef" = (
        dataclasses.field()
    )

    propertyName = field("propertyName")
    componentName = field("componentName")
    componentPath = field("componentPath")
    externalIdProperty = field("externalIdProperty")
    entityId = field("entityId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EntityPropertyReferenceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityPropertyReferenceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityPropertyReference:
    boto3_raw_data: "type_defs.EntityPropertyReferenceTypeDef" = dataclasses.field()

    propertyName = field("propertyName")
    componentName = field("componentName")
    componentPath = field("componentPath")
    externalIdProperty = field("externalIdProperty")
    entityId = field("entityId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityPropertyReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityPropertyReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetails:
    boto3_raw_data: "type_defs.ErrorDetailsTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteQueryRequest:
    boto3_raw_data: "type_defs.ExecuteQueryRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    queryStatement = field("queryStatement")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Row:
    boto3_raw_data: "type_defs.RowTypeDef" = dataclasses.field()

    rowData = field("rowData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterByAssetModel:
    boto3_raw_data: "type_defs.FilterByAssetModelTypeDef" = dataclasses.field()

    assetModelId = field("assetModelId")
    assetModelExternalId = field("assetModelExternalId")
    includeOffspring = field("includeOffspring")
    includeAssets = field("includeAssets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterByAssetModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterByAssetModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterByAsset:
    boto3_raw_data: "type_defs.FilterByAssetTypeDef" = dataclasses.field()

    assetId = field("assetId")
    assetExternalId = field("assetExternalId")
    includeOffspring = field("includeOffspring")
    includeAssetModel = field("includeAssetModel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterByAssetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterByAssetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterByComponentType:
    boto3_raw_data: "type_defs.FilterByComponentTypeTypeDef" = dataclasses.field()

    componentTypeId = field("componentTypeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterByComponentTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterByComponentTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterByEntity:
    boto3_raw_data: "type_defs.FilterByEntityTypeDef" = dataclasses.field()

    entityId = field("entityId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterByEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterByEntityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentTypeRequest:
    boto3_raw_data: "type_defs.GetComponentTypeRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    componentTypeId = field("componentTypeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyGroupResponse:
    boto3_raw_data: "type_defs.PropertyGroupResponseTypeDef" = dataclasses.field()

    groupType = field("groupType")
    propertyNames = field("propertyNames")
    isInherited = field("isInherited")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEntityRequest:
    boto3_raw_data: "type_defs.GetEntityRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    entityId = field("entityId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetEntityRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEntityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetadataTransferJobRequest:
    boto3_raw_data: "type_defs.GetMetadataTransferJobRequestTypeDef" = (
        dataclasses.field()
    )

    metadataTransferJobId = field("metadataTransferJobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMetadataTransferJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetadataTransferJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterpolationParameters:
    boto3_raw_data: "type_defs.InterpolationParametersTypeDef" = dataclasses.field()

    interpolationType = field("interpolationType")
    intervalInSeconds = field("intervalInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InterpolationParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterpolationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSceneRequest:
    boto3_raw_data: "type_defs.GetSceneRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    sceneId = field("sceneId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSceneRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetSceneRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SceneError:
    boto3_raw_data: "type_defs.SceneErrorTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SceneErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SceneErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSyncJobRequest:
    boto3_raw_data: "type_defs.GetSyncJobRequestTypeDef" = dataclasses.field()

    syncSource = field("syncSource")
    workspaceId = field("workspaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSyncJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSyncJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkspaceRequest:
    boto3_raw_data: "type_defs.GetWorkspaceRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentTypesFilter:
    boto3_raw_data: "type_defs.ListComponentTypesFilterTypeDef" = dataclasses.field()

    extendsFrom = field("extendsFrom")
    namespace = field("namespace")
    isAbstract = field("isAbstract")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentTypesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentTypesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsRequest:
    boto3_raw_data: "type_defs.ListComponentsRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    entityId = field("entityId")
    componentPath = field("componentPath")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesFilter:
    boto3_raw_data: "type_defs.ListEntitiesFilterTypeDef" = dataclasses.field()

    parentEntityId = field("parentEntityId")
    componentTypeId = field("componentTypeId")
    externalId = field("externalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntitiesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetadataTransferJobsFilter:
    boto3_raw_data: "type_defs.ListMetadataTransferJobsFilterTypeDef" = (
        dataclasses.field()
    )

    workspaceId = field("workspaceId")
    state = field("state")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMetadataTransferJobsFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetadataTransferJobsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPropertiesRequest:
    boto3_raw_data: "type_defs.ListPropertiesRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    entityId = field("entityId")
    componentName = field("componentName")
    componentPath = field("componentPath")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPropertiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScenesRequest:
    boto3_raw_data: "type_defs.ListScenesRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListScenesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScenesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SceneSummary:
    boto3_raw_data: "type_defs.SceneSummaryTypeDef" = dataclasses.field()

    sceneId = field("sceneId")
    contentLocation = field("contentLocation")
    arn = field("arn")
    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SceneSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SceneSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSyncJobsRequest:
    boto3_raw_data: "type_defs.ListSyncJobsRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSyncJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSyncJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncResourceFilter:
    boto3_raw_data: "type_defs.SyncResourceFilterTypeDef" = dataclasses.field()

    state = field("state")
    resourceType = field("resourceType")
    resourceId = field("resourceId")
    externalId = field("externalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SyncResourceFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SyncResourceFilterTypeDef"]
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

    resourceARN = field("resourceARN")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

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
class ListWorkspacesRequest:
    boto3_raw_data: "type_defs.ListWorkspacesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkspacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceSummary:
    boto3_raw_data: "type_defs.WorkspaceSummaryTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    arn = field("arn")
    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")
    description = field("description")
    linkedServices = field("linkedServices")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkspaceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderBy:
    boto3_raw_data: "type_defs.OrderByTypeDef" = dataclasses.field()

    propertyName = field("propertyName")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrderByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OrderByTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParentEntityUpdateRequest:
    boto3_raw_data: "type_defs.ParentEntityUpdateRequestTypeDef" = dataclasses.field()

    updateType = field("updateType")
    parentEntityId = field("parentEntityId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParentEntityUpdateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParentEntityUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SourceConfiguration:
    boto3_raw_data: "type_defs.S3SourceConfigurationTypeDef" = dataclasses.field()

    location = field("location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3SourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3SourceConfigurationTypeDef"]
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

    resourceARN = field("resourceARN")
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

    resourceARN = field("resourceARN")
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
class UpdatePricingPlanRequest:
    boto3_raw_data: "type_defs.UpdatePricingPlanRequestTypeDef" = dataclasses.field()

    pricingMode = field("pricingMode")
    bundleNames = field("bundleNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePricingPlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePricingPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSceneRequest:
    boto3_raw_data: "type_defs.UpdateSceneRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    sceneId = field("sceneId")
    contentLocation = field("contentLocation")
    description = field("description")
    capabilities = field("capabilities")
    sceneMetadata = field("sceneMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSceneRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSceneRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkspaceRequest:
    boto3_raw_data: "type_defs.UpdateWorkspaceRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    description = field("description")
    role = field("role")
    s3Location = field("s3Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComponentTypeResponse:
    boto3_raw_data: "type_defs.CreateComponentTypeResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    creationDateTime = field("creationDateTime")
    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComponentTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEntityResponse:
    boto3_raw_data: "type_defs.CreateEntityResponseTypeDef" = dataclasses.field()

    entityId = field("entityId")
    arn = field("arn")
    creationDateTime = field("creationDateTime")
    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEntityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEntityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSceneResponse:
    boto3_raw_data: "type_defs.CreateSceneResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    creationDateTime = field("creationDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSceneResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSceneResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSyncJobResponse:
    boto3_raw_data: "type_defs.CreateSyncJobResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    creationDateTime = field("creationDateTime")
    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSyncJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSyncJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceResponse:
    boto3_raw_data: "type_defs.CreateWorkspaceResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    creationDateTime = field("creationDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComponentTypeResponse:
    boto3_raw_data: "type_defs.DeleteComponentTypeResponseTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteComponentTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComponentTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEntityResponse:
    boto3_raw_data: "type_defs.DeleteEntityResponseTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEntityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEntityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSyncJobResponse:
    boto3_raw_data: "type_defs.DeleteSyncJobResponseTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSyncJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSyncJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceResponse:
    boto3_raw_data: "type_defs.DeleteWorkspaceResponseTypeDef" = dataclasses.field()

    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkspaceResponse:
    boto3_raw_data: "type_defs.GetWorkspaceResponseTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    arn = field("arn")
    description = field("description")
    linkedServices = field("linkedServices")
    s3Location = field("s3Location")
    role = field("role")
    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkspaceResponseTypeDef"]
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
class UpdateComponentTypeResponse:
    boto3_raw_data: "type_defs.UpdateComponentTypeResponseTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    arn = field("arn")
    componentTypeId = field("componentTypeId")
    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateComponentTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComponentTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEntityResponse:
    boto3_raw_data: "type_defs.UpdateEntityResponseTypeDef" = dataclasses.field()

    updateDateTime = field("updateDateTime")
    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEntityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEntityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSceneResponse:
    boto3_raw_data: "type_defs.UpdateSceneResponseTypeDef" = dataclasses.field()

    updateDateTime = field("updateDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSceneResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSceneResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkspaceResponse:
    boto3_raw_data: "type_defs.UpdateWorkspaceResponseTypeDef" = dataclasses.field()

    updateDateTime = field("updateDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkspaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PricingPlan:
    boto3_raw_data: "type_defs.PricingPlanTypeDef" = dataclasses.field()

    effectiveDateTime = field("effectiveDateTime")
    pricingMode = field("pricingMode")
    updateDateTime = field("updateDateTime")
    updateReason = field("updateReason")
    billableEntityCount = field("billableEntityCount")

    @cached_property
    def bundleInformation(self):  # pragma: no cover
        return BundleInformation.make_one(self.boto3_raw_data["bundleInformation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PricingPlanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PricingPlanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataConnector:
    boto3_raw_data: "type_defs.DataConnectorTypeDef" = dataclasses.field()

    @cached_property
    def lambda_(self):  # pragma: no cover
        return LambdaFunction.make_one(self.boto3_raw_data["lambda"])

    isNative = field("isNative")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataConnectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataConnectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataValueOutput:
    boto3_raw_data: "type_defs.DataValueOutputTypeDef" = dataclasses.field()

    booleanValue = field("booleanValue")
    doubleValue = field("doubleValue")
    integerValue = field("integerValue")
    longValue = field("longValue")
    stringValue = field("stringValue")
    listValue = field("listValue")
    mapValue = field("mapValue")

    @cached_property
    def relationshipValue(self):  # pragma: no cover
        return RelationshipValue.make_one(self.boto3_raw_data["relationshipValue"])

    expression = field("expression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataValueOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataValueOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataValue:
    boto3_raw_data: "type_defs.DataValueTypeDef" = dataclasses.field()

    booleanValue = field("booleanValue")
    doubleValue = field("doubleValue")
    integerValue = field("integerValue")
    longValue = field("longValue")
    stringValue = field("stringValue")
    listValue = field("listValue")
    mapValue = field("mapValue")

    @cached_property
    def relationshipValue(self):  # pragma: no cover
        return RelationshipValue.make_one(self.boto3_raw_data["relationshipValue"])

    expression = field("expression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationConfiguration:
    boto3_raw_data: "type_defs.DestinationConfigurationTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["s3Configuration"]
        )

    @cached_property
    def iotTwinMakerConfiguration(self):  # pragma: no cover
        return IotTwinMakerDestinationConfiguration.make_one(
            self.boto3_raw_data["iotTwinMakerConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataTransferJobStatus:
    boto3_raw_data: "type_defs.MetadataTransferJobStatusTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["error"])

    queuedPosition = field("queuedPosition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataTransferJobStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataTransferJobStatusTypeDef"]
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

    state = field("state")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["error"])

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
class SyncJobStatus:
    boto3_raw_data: "type_defs.SyncJobStatusTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SyncJobStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SyncJobStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncResourceStatus:
    boto3_raw_data: "type_defs.SyncResourceStatusTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SyncResourceStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SyncResourceStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteQueryResponse:
    boto3_raw_data: "type_defs.ExecuteQueryResponseTypeDef" = dataclasses.field()

    @cached_property
    def columnDescriptions(self):  # pragma: no cover
        return ColumnDescription.make_many(self.boto3_raw_data["columnDescriptions"])

    @cached_property
    def rows(self):  # pragma: no cover
        return Row.make_many(self.boto3_raw_data["rows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotSiteWiseSourceConfigurationFilter:
    boto3_raw_data: "type_defs.IotSiteWiseSourceConfigurationFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterByAssetModel(self):  # pragma: no cover
        return FilterByAssetModel.make_one(self.boto3_raw_data["filterByAssetModel"])

    @cached_property
    def filterByAsset(self):  # pragma: no cover
        return FilterByAsset.make_one(self.boto3_raw_data["filterByAsset"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IotSiteWiseSourceConfigurationFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotSiteWiseSourceConfigurationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotTwinMakerSourceConfigurationFilter:
    boto3_raw_data: "type_defs.IotTwinMakerSourceConfigurationFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterByComponentType(self):  # pragma: no cover
        return FilterByComponentType.make_one(
            self.boto3_raw_data["filterByComponentType"]
        )

    @cached_property
    def filterByEntity(self):  # pragma: no cover
        return FilterByEntity.make_one(self.boto3_raw_data["filterByEntity"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IotTwinMakerSourceConfigurationFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotTwinMakerSourceConfigurationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSceneResponse:
    boto3_raw_data: "type_defs.GetSceneResponseTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    sceneId = field("sceneId")
    contentLocation = field("contentLocation")
    arn = field("arn")
    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")
    description = field("description")
    capabilities = field("capabilities")
    sceneMetadata = field("sceneMetadata")
    generatedSceneMetadata = field("generatedSceneMetadata")

    @cached_property
    def error(self):  # pragma: no cover
        return SceneError.make_one(self.boto3_raw_data["error"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSceneResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSceneResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentTypesRequest:
    boto3_raw_data: "type_defs.ListComponentTypesRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListComponentTypesFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesRequest:
    boto3_raw_data: "type_defs.ListEntitiesRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListEntitiesFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetadataTransferJobsRequest:
    boto3_raw_data: "type_defs.ListMetadataTransferJobsRequestTypeDef" = (
        dataclasses.field()
    )

    sourceType = field("sourceType")
    destinationType = field("destinationType")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListMetadataTransferJobsFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMetadataTransferJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetadataTransferJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScenesResponse:
    boto3_raw_data: "type_defs.ListScenesResponseTypeDef" = dataclasses.field()

    @cached_property
    def sceneSummaries(self):  # pragma: no cover
        return SceneSummary.make_many(self.boto3_raw_data["sceneSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScenesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScenesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSyncResourcesRequest:
    boto3_raw_data: "type_defs.ListSyncResourcesRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    syncSource = field("syncSource")

    @cached_property
    def filters(self):  # pragma: no cover
        return SyncResourceFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSyncResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSyncResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkspacesResponse:
    boto3_raw_data: "type_defs.ListWorkspacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def workspaceSummaries(self):  # pragma: no cover
        return WorkspaceSummary.make_many(self.boto3_raw_data["workspaceSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkspacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkspacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPricingPlanResponse:
    boto3_raw_data: "type_defs.GetPricingPlanResponseTypeDef" = dataclasses.field()

    @cached_property
    def currentPricingPlan(self):  # pragma: no cover
        return PricingPlan.make_one(self.boto3_raw_data["currentPricingPlan"])

    @cached_property
    def pendingPricingPlan(self):  # pragma: no cover
        return PricingPlan.make_one(self.boto3_raw_data["pendingPricingPlan"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPricingPlanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPricingPlanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePricingPlanResponse:
    boto3_raw_data: "type_defs.UpdatePricingPlanResponseTypeDef" = dataclasses.field()

    @cached_property
    def currentPricingPlan(self):  # pragma: no cover
        return PricingPlan.make_one(self.boto3_raw_data["currentPricingPlan"])

    @cached_property
    def pendingPricingPlan(self):  # pragma: no cover
        return PricingPlan.make_one(self.boto3_raw_data["pendingPricingPlan"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePricingPlanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePricingPlanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionRequest:
    boto3_raw_data: "type_defs.FunctionRequestTypeDef" = dataclasses.field()

    requiredProperties = field("requiredProperties")
    scope = field("scope")

    @cached_property
    def implementedBy(self):  # pragma: no cover
        return DataConnector.make_one(self.boto3_raw_data["implementedBy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionResponse:
    boto3_raw_data: "type_defs.FunctionResponseTypeDef" = dataclasses.field()

    requiredProperties = field("requiredProperties")
    scope = field("scope")

    @cached_property
    def implementedBy(self):  # pragma: no cover
        return DataConnector.make_one(self.boto3_raw_data["implementedBy"])

    isInherited = field("isInherited")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataTypeOutput:
    boto3_raw_data: "type_defs.DataTypeOutputTypeDef" = dataclasses.field()

    type = field("type")
    nestedType = field("nestedType")

    @cached_property
    def allowedValues(self):  # pragma: no cover
        return DataValueOutput.make_many(self.boto3_raw_data["allowedValues"])

    unitOfMeasure = field("unitOfMeasure")

    @cached_property
    def relationship(self):  # pragma: no cover
        return Relationship.make_one(self.boto3_raw_data["relationship"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataTypeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataTypeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyLatestValue:
    boto3_raw_data: "type_defs.PropertyLatestValueTypeDef" = dataclasses.field()

    @cached_property
    def propertyReference(self):  # pragma: no cover
        return EntityPropertyReferenceOutput.make_one(
            self.boto3_raw_data["propertyReference"]
        )

    @cached_property
    def propertyValue(self):  # pragma: no cover
        return DataValueOutput.make_one(self.boto3_raw_data["propertyValue"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyLatestValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyLatestValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyValueOutput:
    boto3_raw_data: "type_defs.PropertyValueOutputTypeDef" = dataclasses.field()

    @cached_property
    def value(self):  # pragma: no cover
        return DataValueOutput.make_one(self.boto3_raw_data["value"])

    timestamp = field("timestamp")
    time = field("time")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMetadataTransferJobResponse:
    boto3_raw_data: "type_defs.CancelMetadataTransferJobResponseTypeDef" = (
        dataclasses.field()
    )

    metadataTransferJobId = field("metadataTransferJobId")
    arn = field("arn")
    updateDateTime = field("updateDateTime")

    @cached_property
    def status(self):  # pragma: no cover
        return MetadataTransferJobStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def progress(self):  # pragma: no cover
        return MetadataTransferJobProgress.make_one(self.boto3_raw_data["progress"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelMetadataTransferJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMetadataTransferJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMetadataTransferJobResponse:
    boto3_raw_data: "type_defs.CreateMetadataTransferJobResponseTypeDef" = (
        dataclasses.field()
    )

    metadataTransferJobId = field("metadataTransferJobId")
    arn = field("arn")
    creationDateTime = field("creationDateTime")

    @cached_property
    def status(self):  # pragma: no cover
        return MetadataTransferJobStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMetadataTransferJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMetadataTransferJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataTransferJobSummary:
    boto3_raw_data: "type_defs.MetadataTransferJobSummaryTypeDef" = dataclasses.field()

    metadataTransferJobId = field("metadataTransferJobId")
    arn = field("arn")
    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")

    @cached_property
    def status(self):  # pragma: no cover
        return MetadataTransferJobStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def progress(self):  # pragma: no cover
        return MetadataTransferJobProgress.make_one(self.boto3_raw_data["progress"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataTransferJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataTransferJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentSummary:
    boto3_raw_data: "type_defs.ComponentSummaryTypeDef" = dataclasses.field()

    componentName = field("componentName")
    componentTypeId = field("componentTypeId")

    @cached_property
    def status(self):  # pragma: no cover
        return Status.make_one(self.boto3_raw_data["status"])

    definedIn = field("definedIn")
    description = field("description")
    propertyGroups = field("propertyGroups")
    syncSource = field("syncSource")
    componentPath = field("componentPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentTypeSummary:
    boto3_raw_data: "type_defs.ComponentTypeSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    componentTypeId = field("componentTypeId")
    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")
    description = field("description")

    @cached_property
    def status(self):  # pragma: no cover
        return Status.make_one(self.boto3_raw_data["status"])

    componentTypeName = field("componentTypeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentTypeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentTypeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntitySummary:
    boto3_raw_data: "type_defs.EntitySummaryTypeDef" = dataclasses.field()

    entityId = field("entityId")
    entityName = field("entityName")
    arn = field("arn")

    @cached_property
    def status(self):  # pragma: no cover
        return Status.make_one(self.boto3_raw_data["status"])

    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")
    parentEntityId = field("parentEntityId")
    description = field("description")
    hasChildEntities = field("hasChildEntities")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntitySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntitySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSyncJobResponse:
    boto3_raw_data: "type_defs.GetSyncJobResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    workspaceId = field("workspaceId")
    syncSource = field("syncSource")
    syncRole = field("syncRole")

    @cached_property
    def status(self):  # pragma: no cover
        return SyncJobStatus.make_one(self.boto3_raw_data["status"])

    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSyncJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSyncJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncJobSummary:
    boto3_raw_data: "type_defs.SyncJobSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    workspaceId = field("workspaceId")
    syncSource = field("syncSource")

    @cached_property
    def status(self):  # pragma: no cover
        return SyncJobStatus.make_one(self.boto3_raw_data["status"])

    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SyncJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SyncJobSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncResourceSummary:
    boto3_raw_data: "type_defs.SyncResourceSummaryTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    externalId = field("externalId")
    resourceId = field("resourceId")

    @cached_property
    def status(self):  # pragma: no cover
        return SyncResourceStatus.make_one(self.boto3_raw_data["status"])

    updateDateTime = field("updateDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SyncResourceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SyncResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotSiteWiseSourceConfigurationOutput:
    boto3_raw_data: "type_defs.IotSiteWiseSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return IotSiteWiseSourceConfigurationFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IotSiteWiseSourceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotSiteWiseSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotSiteWiseSourceConfiguration:
    boto3_raw_data: "type_defs.IotSiteWiseSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return IotSiteWiseSourceConfigurationFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IotSiteWiseSourceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotSiteWiseSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotTwinMakerSourceConfigurationOutput:
    boto3_raw_data: "type_defs.IotTwinMakerSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    workspace = field("workspace")

    @cached_property
    def filters(self):  # pragma: no cover
        return IotTwinMakerSourceConfigurationFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IotTwinMakerSourceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotTwinMakerSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotTwinMakerSourceConfiguration:
    boto3_raw_data: "type_defs.IotTwinMakerSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    workspace = field("workspace")

    @cached_property
    def filters(self):  # pragma: no cover
        return IotTwinMakerSourceConfigurationFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IotTwinMakerSourceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotTwinMakerSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyDefinitionResponse:
    boto3_raw_data: "type_defs.PropertyDefinitionResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataType(self):  # pragma: no cover
        return DataTypeOutput.make_one(self.boto3_raw_data["dataType"])

    isTimeSeries = field("isTimeSeries")
    isRequiredInEntity = field("isRequiredInEntity")
    isExternalId = field("isExternalId")
    isStoredExternally = field("isStoredExternally")
    isImported = field("isImported")
    isFinal = field("isFinal")
    isInherited = field("isInherited")

    @cached_property
    def defaultValue(self):  # pragma: no cover
        return DataValueOutput.make_one(self.boto3_raw_data["defaultValue"])

    configuration = field("configuration")
    displayName = field("displayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyDefinitionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPropertyValueResponse:
    boto3_raw_data: "type_defs.GetPropertyValueResponseTypeDef" = dataclasses.field()

    propertyValues = field("propertyValues")
    tabularPropertyValues = field("tabularPropertyValues")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPropertyValueResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPropertyValueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyValueEntryOutput:
    boto3_raw_data: "type_defs.PropertyValueEntryOutputTypeDef" = dataclasses.field()

    @cached_property
    def entityPropertyReference(self):  # pragma: no cover
        return EntityPropertyReferenceOutput.make_one(
            self.boto3_raw_data["entityPropertyReference"]
        )

    @cached_property
    def propertyValues(self):  # pragma: no cover
        return PropertyValueOutput.make_many(self.boto3_raw_data["propertyValues"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyValueEntryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyValueEntryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyValueHistory:
    boto3_raw_data: "type_defs.PropertyValueHistoryTypeDef" = dataclasses.field()

    @cached_property
    def entityPropertyReference(self):  # pragma: no cover
        return EntityPropertyReferenceOutput.make_one(
            self.boto3_raw_data["entityPropertyReference"]
        )

    @cached_property
    def values(self):  # pragma: no cover
        return PropertyValueOutput.make_many(self.boto3_raw_data["values"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyValueHistoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyValueHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataType:
    boto3_raw_data: "type_defs.DataTypeTypeDef" = dataclasses.field()

    type = field("type")
    nestedType = field("nestedType")
    allowedValues = field("allowedValues")
    unitOfMeasure = field("unitOfMeasure")

    @cached_property
    def relationship(self):  # pragma: no cover
        return Relationship.make_one(self.boto3_raw_data["relationship"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyFilter:
    boto3_raw_data: "type_defs.PropertyFilterTypeDef" = dataclasses.field()

    propertyName = field("propertyName")
    operator = field("operator")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertyFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyValue:
    boto3_raw_data: "type_defs.PropertyValueTypeDef" = dataclasses.field()

    value = field("value")
    timestamp = field("timestamp")
    time = field("time")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertyValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetadataTransferJobsResponse:
    boto3_raw_data: "type_defs.ListMetadataTransferJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def metadataTransferJobSummaries(self):  # pragma: no cover
        return MetadataTransferJobSummary.make_many(
            self.boto3_raw_data["metadataTransferJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMetadataTransferJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetadataTransferJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsResponse:
    boto3_raw_data: "type_defs.ListComponentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def componentSummaries(self):  # pragma: no cover
        return ComponentSummary.make_many(self.boto3_raw_data["componentSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentTypesResponse:
    boto3_raw_data: "type_defs.ListComponentTypesResponseTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")

    @cached_property
    def componentTypeSummaries(self):  # pragma: no cover
        return ComponentTypeSummary.make_many(
            self.boto3_raw_data["componentTypeSummaries"]
        )

    maxResults = field("maxResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentTypesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesResponse:
    boto3_raw_data: "type_defs.ListEntitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def entitySummaries(self):  # pragma: no cover
        return EntitySummary.make_many(self.boto3_raw_data["entitySummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSyncJobsResponse:
    boto3_raw_data: "type_defs.ListSyncJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def syncJobSummaries(self):  # pragma: no cover
        return SyncJobSummary.make_many(self.boto3_raw_data["syncJobSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSyncJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSyncJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSyncResourcesResponse:
    boto3_raw_data: "type_defs.ListSyncResourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def syncResources(self):  # pragma: no cover
        return SyncResourceSummary.make_many(self.boto3_raw_data["syncResources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSyncResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSyncResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConfigurationOutput:
    boto3_raw_data: "type_defs.SourceConfigurationOutputTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return S3SourceConfiguration.make_one(self.boto3_raw_data["s3Configuration"])

    @cached_property
    def iotSiteWiseConfiguration(self):  # pragma: no cover
        return IotSiteWiseSourceConfigurationOutput.make_one(
            self.boto3_raw_data["iotSiteWiseConfiguration"]
        )

    @cached_property
    def iotTwinMakerConfiguration(self):  # pragma: no cover
        return IotTwinMakerSourceConfigurationOutput.make_one(
            self.boto3_raw_data["iotTwinMakerConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentTypeResponse:
    boto3_raw_data: "type_defs.GetComponentTypeResponseTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    isSingleton = field("isSingleton")
    componentTypeId = field("componentTypeId")
    description = field("description")
    propertyDefinitions = field("propertyDefinitions")
    extendsFrom = field("extendsFrom")
    functions = field("functions")
    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")
    arn = field("arn")
    isAbstract = field("isAbstract")
    isSchemaInitialized = field("isSchemaInitialized")

    @cached_property
    def status(self):  # pragma: no cover
        return Status.make_one(self.boto3_raw_data["status"])

    propertyGroups = field("propertyGroups")
    syncSource = field("syncSource")
    componentTypeName = field("componentTypeName")
    compositeComponentTypes = field("compositeComponentTypes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyResponse:
    boto3_raw_data: "type_defs.PropertyResponseTypeDef" = dataclasses.field()

    @cached_property
    def definition(self):  # pragma: no cover
        return PropertyDefinitionResponse.make_one(self.boto3_raw_data["definition"])

    @cached_property
    def value(self):  # pragma: no cover
        return DataValueOutput.make_one(self.boto3_raw_data["value"])

    areAllPropertyValuesReturned = field("areAllPropertyValuesReturned")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertySummary:
    boto3_raw_data: "type_defs.PropertySummaryTypeDef" = dataclasses.field()

    propertyName = field("propertyName")

    @cached_property
    def definition(self):  # pragma: no cover
        return PropertyDefinitionResponse.make_one(self.boto3_raw_data["definition"])

    @cached_property
    def value(self):  # pragma: no cover
        return DataValueOutput.make_one(self.boto3_raw_data["value"])

    areAllPropertyValuesReturned = field("areAllPropertyValuesReturned")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutPropertyError:
    boto3_raw_data: "type_defs.BatchPutPropertyErrorTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @cached_property
    def entry(self):  # pragma: no cover
        return PropertyValueEntryOutput.make_one(self.boto3_raw_data["entry"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutPropertyErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutPropertyErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPropertyValueHistoryResponse:
    boto3_raw_data: "type_defs.GetPropertyValueHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def propertyValues(self):  # pragma: no cover
        return PropertyValueHistory.make_many(self.boto3_raw_data["propertyValues"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPropertyValueHistoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPropertyValueHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPropertyValueHistoryRequest:
    boto3_raw_data: "type_defs.GetPropertyValueHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    workspaceId = field("workspaceId")
    selectedProperties = field("selectedProperties")
    entityId = field("entityId")
    componentName = field("componentName")
    componentPath = field("componentPath")
    componentTypeId = field("componentTypeId")

    @cached_property
    def propertyFilters(self):  # pragma: no cover
        return PropertyFilter.make_many(self.boto3_raw_data["propertyFilters"])

    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")

    @cached_property
    def interpolation(self):  # pragma: no cover
        return InterpolationParameters.make_one(self.boto3_raw_data["interpolation"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    orderByTime = field("orderByTime")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPropertyValueHistoryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPropertyValueHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TabularConditions:
    boto3_raw_data: "type_defs.TabularConditionsTypeDef" = dataclasses.field()

    @cached_property
    def orderBy(self):  # pragma: no cover
        return OrderBy.make_many(self.boto3_raw_data["orderBy"])

    @cached_property
    def propertyFilters(self):  # pragma: no cover
        return PropertyFilter.make_many(self.boto3_raw_data["propertyFilters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TabularConditionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TabularConditionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetadataTransferJobResponse:
    boto3_raw_data: "type_defs.GetMetadataTransferJobResponseTypeDef" = (
        dataclasses.field()
    )

    metadataTransferJobId = field("metadataTransferJobId")
    arn = field("arn")
    description = field("description")

    @cached_property
    def sources(self):  # pragma: no cover
        return SourceConfigurationOutput.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def destination(self):  # pragma: no cover
        return DestinationConfiguration.make_one(self.boto3_raw_data["destination"])

    metadataTransferJobRole = field("metadataTransferJobRole")
    reportUrl = field("reportUrl")
    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")

    @cached_property
    def status(self):  # pragma: no cover
        return MetadataTransferJobStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def progress(self):  # pragma: no cover
        return MetadataTransferJobProgress.make_one(self.boto3_raw_data["progress"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMetadataTransferJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetadataTransferJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConfiguration:
    boto3_raw_data: "type_defs.SourceConfigurationTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return S3SourceConfiguration.make_one(self.boto3_raw_data["s3Configuration"])

    iotSiteWiseConfiguration = field("iotSiteWiseConfiguration")
    iotTwinMakerConfiguration = field("iotTwinMakerConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentResponse:
    boto3_raw_data: "type_defs.ComponentResponseTypeDef" = dataclasses.field()

    componentName = field("componentName")
    description = field("description")
    componentTypeId = field("componentTypeId")

    @cached_property
    def status(self):  # pragma: no cover
        return Status.make_one(self.boto3_raw_data["status"])

    definedIn = field("definedIn")
    properties = field("properties")
    propertyGroups = field("propertyGroups")
    syncSource = field("syncSource")
    areAllPropertiesReturned = field("areAllPropertiesReturned")
    compositeComponents = field("compositeComponents")
    areAllCompositeComponentsReturned = field("areAllCompositeComponentsReturned")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPropertiesResponse:
    boto3_raw_data: "type_defs.ListPropertiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def propertySummaries(self):  # pragma: no cover
        return PropertySummary.make_many(self.boto3_raw_data["propertySummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPropertiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPropertiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutPropertyErrorEntry:
    boto3_raw_data: "type_defs.BatchPutPropertyErrorEntryTypeDef" = dataclasses.field()

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchPutPropertyError.make_many(self.boto3_raw_data["errors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutPropertyErrorEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutPropertyErrorEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyDefinitionRequest:
    boto3_raw_data: "type_defs.PropertyDefinitionRequestTypeDef" = dataclasses.field()

    dataType = field("dataType")
    isRequiredInEntity = field("isRequiredInEntity")
    isExternalId = field("isExternalId")
    isStoredExternally = field("isStoredExternally")
    isTimeSeries = field("isTimeSeries")
    defaultValue = field("defaultValue")
    configuration = field("configuration")
    displayName = field("displayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPropertyValueRequest:
    boto3_raw_data: "type_defs.GetPropertyValueRequestTypeDef" = dataclasses.field()

    selectedProperties = field("selectedProperties")
    workspaceId = field("workspaceId")
    componentName = field("componentName")
    componentPath = field("componentPath")
    componentTypeId = field("componentTypeId")
    entityId = field("entityId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    propertyGroupName = field("propertyGroupName")

    @cached_property
    def tabularConditions(self):  # pragma: no cover
        return TabularConditions.make_one(self.boto3_raw_data["tabularConditions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPropertyValueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPropertyValueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyValueEntry:
    boto3_raw_data: "type_defs.PropertyValueEntryTypeDef" = dataclasses.field()

    entityPropertyReference = field("entityPropertyReference")
    propertyValues = field("propertyValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyValueEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyValueEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEntityResponse:
    boto3_raw_data: "type_defs.GetEntityResponseTypeDef" = dataclasses.field()

    entityId = field("entityId")
    entityName = field("entityName")
    arn = field("arn")

    @cached_property
    def status(self):  # pragma: no cover
        return Status.make_one(self.boto3_raw_data["status"])

    workspaceId = field("workspaceId")
    description = field("description")
    components = field("components")
    parentEntityId = field("parentEntityId")
    hasChildEntities = field("hasChildEntities")
    creationDateTime = field("creationDateTime")
    updateDateTime = field("updateDateTime")
    syncSource = field("syncSource")
    areAllComponentsReturned = field("areAllComponentsReturned")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetEntityResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEntityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutPropertyValuesResponse:
    boto3_raw_data: "type_defs.BatchPutPropertyValuesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return BatchPutPropertyErrorEntry.make_many(self.boto3_raw_data["errorEntries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchPutPropertyValuesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutPropertyValuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComponentTypeRequest:
    boto3_raw_data: "type_defs.CreateComponentTypeRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    componentTypeId = field("componentTypeId")
    isSingleton = field("isSingleton")
    description = field("description")
    propertyDefinitions = field("propertyDefinitions")
    extendsFrom = field("extendsFrom")
    functions = field("functions")
    tags = field("tags")
    propertyGroups = field("propertyGroups")
    componentTypeName = field("componentTypeName")
    compositeComponentTypes = field("compositeComponentTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComponentTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyRequest:
    boto3_raw_data: "type_defs.PropertyRequestTypeDef" = dataclasses.field()

    @cached_property
    def definition(self):  # pragma: no cover
        return PropertyDefinitionRequest.make_one(self.boto3_raw_data["definition"])

    value = field("value")
    updateType = field("updateType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertyRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComponentTypeRequest:
    boto3_raw_data: "type_defs.UpdateComponentTypeRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    componentTypeId = field("componentTypeId")
    isSingleton = field("isSingleton")
    description = field("description")
    propertyDefinitions = field("propertyDefinitions")
    extendsFrom = field("extendsFrom")
    functions = field("functions")
    propertyGroups = field("propertyGroups")
    componentTypeName = field("componentTypeName")
    compositeComponentTypes = field("compositeComponentTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateComponentTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComponentTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMetadataTransferJobRequest:
    boto3_raw_data: "type_defs.CreateMetadataTransferJobRequestTypeDef" = (
        dataclasses.field()
    )

    sources = field("sources")

    @cached_property
    def destination(self):  # pragma: no cover
        return DestinationConfiguration.make_one(self.boto3_raw_data["destination"])

    metadataTransferJobId = field("metadataTransferJobId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMetadataTransferJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMetadataTransferJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentRequest:
    boto3_raw_data: "type_defs.ComponentRequestTypeDef" = dataclasses.field()

    description = field("description")
    componentTypeId = field("componentTypeId")
    properties = field("properties")
    propertyGroups = field("propertyGroups")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentUpdateRequest:
    boto3_raw_data: "type_defs.ComponentUpdateRequestTypeDef" = dataclasses.field()

    updateType = field("updateType")
    description = field("description")
    componentTypeId = field("componentTypeId")
    propertyUpdates = field("propertyUpdates")
    propertyGroupUpdates = field("propertyGroupUpdates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentUpdateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositeComponentRequest:
    boto3_raw_data: "type_defs.CompositeComponentRequestTypeDef" = dataclasses.field()

    description = field("description")
    properties = field("properties")
    propertyGroups = field("propertyGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompositeComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositeComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositeComponentUpdateRequest:
    boto3_raw_data: "type_defs.CompositeComponentUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    updateType = field("updateType")
    description = field("description")
    propertyUpdates = field("propertyUpdates")
    propertyGroupUpdates = field("propertyGroupUpdates")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CompositeComponentUpdateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositeComponentUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutPropertyValuesRequest:
    boto3_raw_data: "type_defs.BatchPutPropertyValuesRequestTypeDef" = (
        dataclasses.field()
    )

    workspaceId = field("workspaceId")
    entries = field("entries")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchPutPropertyValuesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutPropertyValuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEntityRequest:
    boto3_raw_data: "type_defs.CreateEntityRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    entityName = field("entityName")
    entityId = field("entityId")
    description = field("description")
    components = field("components")
    compositeComponents = field("compositeComponents")
    parentEntityId = field("parentEntityId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEntityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEntityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEntityRequest:
    boto3_raw_data: "type_defs.UpdateEntityRequestTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")
    entityId = field("entityId")
    entityName = field("entityName")
    description = field("description")
    componentUpdates = field("componentUpdates")
    compositeComponentUpdates = field("compositeComponentUpdates")

    @cached_property
    def parentEntityUpdate(self):  # pragma: no cover
        return ParentEntityUpdateRequest.make_one(
            self.boto3_raw_data["parentEntityUpdate"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEntityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEntityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
