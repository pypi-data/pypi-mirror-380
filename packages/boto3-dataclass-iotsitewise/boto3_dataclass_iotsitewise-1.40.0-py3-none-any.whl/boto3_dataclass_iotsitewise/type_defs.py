# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotsitewise import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessDeniedException:
    boto3_raw_data: "type_defs.AccessDeniedExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessDeniedExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessDeniedExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionDefinition:
    boto3_raw_data: "type_defs.ActionDefinitionTypeDef" = dataclasses.field()

    actionDefinitionId = field("actionDefinitionId")
    actionName = field("actionName")
    actionType = field("actionType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionPayload:
    boto3_raw_data: "type_defs.ActionPayloadTypeDef" = dataclasses.field()

    stringValue = field("stringValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionPayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionPayloadTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolveTo:
    boto3_raw_data: "type_defs.ResolveToTypeDef" = dataclasses.field()

    assetId = field("assetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResolveToTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResolveToTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetResource:
    boto3_raw_data: "type_defs.TargetResourceTypeDef" = dataclasses.field()

    assetId = field("assetId")
    computationModelId = field("computationModelId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Aggregates:
    boto3_raw_data: "type_defs.AggregatesTypeDef" = dataclasses.field()

    average = field("average")
    count = field("count")
    maximum = field("maximum")
    minimum = field("minimum")
    sum = field("sum")
    standardDeviation = field("standardDeviation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AggregatesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AggregatesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Alarms:
    boto3_raw_data: "type_defs.AlarmsTypeDef" = dataclasses.field()

    alarmRoleArn = field("alarmRoleArn")
    notificationLambdaArn = field("notificationLambdaArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetBindingValueFilter:
    boto3_raw_data: "type_defs.AssetBindingValueFilterTypeDef" = dataclasses.field()

    assetId = field("assetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetBindingValueFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetBindingValueFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetCompositeModelPathSegment:
    boto3_raw_data: "type_defs.AssetCompositeModelPathSegmentTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssetCompositeModelPathSegmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetCompositeModelPathSegmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetErrorDetails:
    boto3_raw_data: "type_defs.AssetErrorDetailsTypeDef" = dataclasses.field()

    assetId = field("assetId")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetErrorDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetHierarchyInfo:
    boto3_raw_data: "type_defs.AssetHierarchyInfoTypeDef" = dataclasses.field()

    parentAssetId = field("parentAssetId")
    childAssetId = field("childAssetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetHierarchyInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetHierarchyInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetHierarchy:
    boto3_raw_data: "type_defs.AssetHierarchyTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    externalId = field("externalId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetHierarchyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetHierarchyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelBindingValueFilter:
    boto3_raw_data: "type_defs.AssetModelBindingValueFilterTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetModelBindingValueFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelBindingValueFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelCompositeModelPathSegment:
    boto3_raw_data: "type_defs.AssetModelCompositeModelPathSegmentTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssetModelCompositeModelPathSegmentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelCompositeModelPathSegmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelHierarchyDefinition:
    boto3_raw_data: "type_defs.AssetModelHierarchyDefinitionTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    childAssetModelId = field("childAssetModelId")
    id = field("id")
    externalId = field("externalId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssetModelHierarchyDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelHierarchyDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelHierarchy:
    boto3_raw_data: "type_defs.AssetModelHierarchyTypeDef" = dataclasses.field()

    name = field("name")
    childAssetModelId = field("childAssetModelId")
    id = field("id")
    externalId = field("externalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetModelHierarchyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelHierarchyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelPropertyBindingValueFilter:
    boto3_raw_data: "type_defs.AssetModelPropertyBindingValueFilterTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    propertyId = field("propertyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssetModelPropertyBindingValueFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelPropertyBindingValueFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelPropertyBindingValue:
    boto3_raw_data: "type_defs.AssetModelPropertyBindingValueTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    propertyId = field("propertyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssetModelPropertyBindingValueTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelPropertyBindingValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelPropertyPathSegment:
    boto3_raw_data: "type_defs.AssetModelPropertyPathSegmentTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssetModelPropertyPathSegmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelPropertyPathSegmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterfaceSummary:
    boto3_raw_data: "type_defs.InterfaceSummaryTypeDef" = dataclasses.field()

    interfaceAssetModelId = field("interfaceAssetModelId")
    interfaceAssetModelPropertyId = field("interfaceAssetModelPropertyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InterfaceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterfaceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertyBindingValueFilter:
    boto3_raw_data: "type_defs.AssetPropertyBindingValueFilterTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    propertyId = field("propertyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssetPropertyBindingValueFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertyBindingValueFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertyBindingValue:
    boto3_raw_data: "type_defs.AssetPropertyBindingValueTypeDef" = dataclasses.field()

    assetId = field("assetId")
    propertyId = field("propertyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetPropertyBindingValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertyBindingValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertyPathSegment:
    boto3_raw_data: "type_defs.AssetPropertyPathSegmentTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetPropertyPathSegmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertyPathSegmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyNotification:
    boto3_raw_data: "type_defs.PropertyNotificationTypeDef" = dataclasses.field()

    topic = field("topic")
    state = field("state")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyNotificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyNotificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeInNanos:
    boto3_raw_data: "type_defs.TimeInNanosTypeDef" = dataclasses.field()

    timeInSeconds = field("timeInSeconds")
    offsetInNanos = field("offsetInNanos")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeInNanosTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeInNanosTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAssetsRequest:
    boto3_raw_data: "type_defs.AssociateAssetsRequestTypeDef" = dataclasses.field()

    assetId = field("assetId")
    hierarchyId = field("hierarchyId")
    childAssetId = field("childAssetId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateAssetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAssetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateTimeSeriesToAssetPropertyRequest:
    boto3_raw_data: "type_defs.AssociateTimeSeriesToAssetPropertyRequestTypeDef" = (
        dataclasses.field()
    )

    alias = field("alias")
    assetId = field("assetId")
    propertyId = field("propertyId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateTimeSeriesToAssetPropertyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateTimeSeriesToAssetPropertyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attribute:
    boto3_raw_data: "type_defs.AttributeTypeDef" = dataclasses.field()

    defaultValue = field("defaultValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateProjectAssetsRequest:
    boto3_raw_data: "type_defs.BatchAssociateProjectAssetsRequestTypeDef" = (
        dataclasses.field()
    )

    projectId = field("projectId")
    assetIds = field("assetIds")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateProjectAssetsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateProjectAssetsRequestTypeDef"]
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
class BatchDisassociateProjectAssetsRequest:
    boto3_raw_data: "type_defs.BatchDisassociateProjectAssetsRequestTypeDef" = (
        dataclasses.field()
    )

    projectId = field("projectId")
    assetIds = field("assetIds")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateProjectAssetsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisassociateProjectAssetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyAggregatesErrorEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyAggregatesErrorEntryTypeDef" = (
        dataclasses.field()
    )

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")
    entryId = field("entryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyAggregatesErrorEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyAggregatesErrorEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyAggregatesErrorInfo:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyAggregatesErrorInfoTypeDef" = (
        dataclasses.field()
    )

    errorCode = field("errorCode")
    errorTimestamp = field("errorTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyAggregatesErrorInfoTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyAggregatesErrorInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")
    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetAssetPropertyValueEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueErrorEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueErrorEntryTypeDef" = (
        dataclasses.field()
    )

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")
    entryId = field("entryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueErrorEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueErrorEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueErrorInfo:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueErrorInfoTypeDef" = (
        dataclasses.field()
    )

    errorCode = field("errorCode")
    errorTimestamp = field("errorTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueErrorInfoTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueErrorInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueHistoryErrorEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueHistoryErrorEntryTypeDef" = (
        dataclasses.field()
    )

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")
    entryId = field("entryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueHistoryErrorEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueHistoryErrorEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueHistoryErrorInfo:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueHistoryErrorInfoTypeDef" = (
        dataclasses.field()
    )

    errorCode = field("errorCode")
    errorTimestamp = field("errorTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueHistoryErrorInfoTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueHistoryErrorInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Content:
    boto3_raw_data: "type_defs.ContentTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnType:
    boto3_raw_data: "type_defs.ColumnTypeTypeDef" = dataclasses.field()

    scalarType = field("scalarType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositionRelationshipItem:
    boto3_raw_data: "type_defs.CompositionRelationshipItemTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompositionRelationshipItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositionRelationshipItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositionRelationshipSummary:
    boto3_raw_data: "type_defs.CompositionRelationshipSummaryTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    assetModelCompositeModelId = field("assetModelCompositeModelId")
    assetModelCompositeModelType = field("assetModelCompositeModelType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CompositionRelationshipSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositionRelationshipSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputationModelAnomalyDetectionConfiguration:
    boto3_raw_data: "type_defs.ComputationModelAnomalyDetectionConfigurationTypeDef" = (
        dataclasses.field()
    )

    inputProperties = field("inputProperties")
    resultProperty = field("resultProperty")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComputationModelAnomalyDetectionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputationModelAnomalyDetectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationErrorDetails:
    boto3_raw_data: "type_defs.ConfigurationErrorDetailsTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationErrorDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConflictingOperationException:
    boto3_raw_data: "type_defs.ConflictingOperationExceptionTypeDef" = (
        dataclasses.field()
    )

    message = field("message")
    resourceId = field("resourceId")
    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConflictingOperationExceptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConflictingOperationExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetRequest:
    boto3_raw_data: "type_defs.CreateAssetRequestTypeDef" = dataclasses.field()

    assetName = field("assetName")
    assetModelId = field("assetModelId")
    assetId = field("assetId")
    assetExternalId = field("assetExternalId")
    clientToken = field("clientToken")
    tags = field("tags")
    assetDescription = field("assetDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorReportLocation:
    boto3_raw_data: "type_defs.ErrorReportLocationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ErrorReportLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ErrorReportLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class File:
    boto3_raw_data: "type_defs.FileTypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")
    versionId = field("versionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDashboardRequest:
    boto3_raw_data: "type_defs.CreateDashboardRequestTypeDef" = dataclasses.field()

    projectId = field("projectId")
    dashboardName = field("dashboardName")
    dashboardDefinition = field("dashboardDefinition")
    dashboardDescription = field("dashboardDescription")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDashboardRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDashboardRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectRequest:
    boto3_raw_data: "type_defs.CreateProjectRequestTypeDef" = dataclasses.field()

    portalId = field("portalId")
    projectName = field("projectName")
    projectDescription = field("projectDescription")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CsvOutput:
    boto3_raw_data: "type_defs.CsvOutputTypeDef" = dataclasses.field()

    columnNames = field("columnNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CsvOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CsvOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Csv:
    boto3_raw_data: "type_defs.CsvTypeDef" = dataclasses.field()

    columnNames = field("columnNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CsvTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CsvTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerManagedS3Storage:
    boto3_raw_data: "type_defs.CustomerManagedS3StorageTypeDef" = dataclasses.field()

    s3ResourceArn = field("s3ResourceArn")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomerManagedS3StorageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerManagedS3StorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashboardSummary:
    boto3_raw_data: "type_defs.DashboardSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashboardSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashboardSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatumPaginator:
    boto3_raw_data: "type_defs.DatumPaginatorTypeDef" = dataclasses.field()

    scalarValue = field("scalarValue")
    arrayValue = field("arrayValue")
    rowValue = field("rowValue")
    nullValue = field("nullValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatumPaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatumPaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Datum:
    boto3_raw_data: "type_defs.DatumTypeDef" = dataclasses.field()

    scalarValue = field("scalarValue")
    arrayValue = field("arrayValue")
    rowValue = field("rowValue")
    nullValue = field("nullValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatumTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatumTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatumWaiter:
    boto3_raw_data: "type_defs.DatumWaiterTypeDef" = dataclasses.field()

    scalarValue = field("scalarValue")
    arrayValue = field("arrayValue")
    rowValue = field("rowValue")
    nullValue = field("nullValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatumWaiterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatumWaiterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessPolicyRequest:
    boto3_raw_data: "type_defs.DeleteAccessPolicyRequestTypeDef" = dataclasses.field()

    accessPolicyId = field("accessPolicyId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetModelCompositeModelRequest:
    boto3_raw_data: "type_defs.DeleteAssetModelCompositeModelRequestTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    assetModelCompositeModelId = field("assetModelCompositeModelId")
    clientToken = field("clientToken")
    ifMatch = field("ifMatch")
    ifNoneMatch = field("ifNoneMatch")
    matchForVersionType = field("matchForVersionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAssetModelCompositeModelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetModelCompositeModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetModelInterfaceRelationshipRequest:
    boto3_raw_data: "type_defs.DeleteAssetModelInterfaceRelationshipRequestTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    interfaceAssetModelId = field("interfaceAssetModelId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAssetModelInterfaceRelationshipRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetModelInterfaceRelationshipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetModelRequest:
    boto3_raw_data: "type_defs.DeleteAssetModelRequestTypeDef" = dataclasses.field()

    assetModelId = field("assetModelId")
    clientToken = field("clientToken")
    ifMatch = field("ifMatch")
    ifNoneMatch = field("ifNoneMatch")
    matchForVersionType = field("matchForVersionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssetModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetRequest:
    boto3_raw_data: "type_defs.DeleteAssetRequestTypeDef" = dataclasses.field()

    assetId = field("assetId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComputationModelRequest:
    boto3_raw_data: "type_defs.DeleteComputationModelRequestTypeDef" = (
        dataclasses.field()
    )

    computationModelId = field("computationModelId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteComputationModelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComputationModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDashboardRequest:
    boto3_raw_data: "type_defs.DeleteDashboardRequestTypeDef" = dataclasses.field()

    dashboardId = field("dashboardId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDashboardRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDashboardRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetRequest:
    boto3_raw_data: "type_defs.DeleteDatasetRequestTypeDef" = dataclasses.field()

    datasetId = field("datasetId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayRequest:
    boto3_raw_data: "type_defs.DeleteGatewayRequestTypeDef" = dataclasses.field()

    gatewayId = field("gatewayId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePortalRequest:
    boto3_raw_data: "type_defs.DeletePortalRequestTypeDef" = dataclasses.field()

    portalId = field("portalId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePortalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePortalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectRequest:
    boto3_raw_data: "type_defs.DeleteProjectRequestTypeDef" = dataclasses.field()

    projectId = field("projectId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTimeSeriesRequest:
    boto3_raw_data: "type_defs.DeleteTimeSeriesRequestTypeDef" = dataclasses.field()

    alias = field("alias")
    assetId = field("assetId")
    propertyId = field("propertyId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTimeSeriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTimeSeriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessPolicyRequest:
    boto3_raw_data: "type_defs.DescribeAccessPolicyRequestTypeDef" = dataclasses.field()

    accessPolicyId = field("accessPolicyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActionRequest:
    boto3_raw_data: "type_defs.DescribeActionRequestTypeDef" = dataclasses.field()

    actionId = field("actionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetCompositeModelRequest:
    boto3_raw_data: "type_defs.DescribeAssetCompositeModelRequestTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    assetCompositeModelId = field("assetCompositeModelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssetCompositeModelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetCompositeModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetModelCompositeModelRequest:
    boto3_raw_data: "type_defs.DescribeAssetModelCompositeModelRequestTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    assetModelCompositeModelId = field("assetModelCompositeModelId")
    assetModelVersion = field("assetModelVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssetModelCompositeModelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetModelCompositeModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetModelInterfaceRelationshipRequest:
    boto3_raw_data: (
        "type_defs.DescribeAssetModelInterfaceRelationshipRequestTypeDef"
    ) = dataclasses.field()

    assetModelId = field("assetModelId")
    interfaceAssetModelId = field("interfaceAssetModelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssetModelInterfaceRelationshipRequestTypeDef"
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
                "type_defs.DescribeAssetModelInterfaceRelationshipRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyMapping:
    boto3_raw_data: "type_defs.HierarchyMappingTypeDef" = dataclasses.field()

    assetModelHierarchyId = field("assetModelHierarchyId")
    interfaceAssetModelHierarchyId = field("interfaceAssetModelHierarchyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HierarchyMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchyMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyMapping:
    boto3_raw_data: "type_defs.PropertyMappingTypeDef" = dataclasses.field()

    assetModelPropertyId = field("assetModelPropertyId")
    interfaceAssetModelPropertyId = field("interfaceAssetModelPropertyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertyMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetModelRequest:
    boto3_raw_data: "type_defs.DescribeAssetModelRequestTypeDef" = dataclasses.field()

    assetModelId = field("assetModelId")
    excludeProperties = field("excludeProperties")
    assetModelVersion = field("assetModelVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAssetModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterfaceRelationship:
    boto3_raw_data: "type_defs.InterfaceRelationshipTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InterfaceRelationshipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterfaceRelationshipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetPropertyRequest:
    boto3_raw_data: "type_defs.DescribeAssetPropertyRequestTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    propertyId = field("propertyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAssetPropertyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetPropertyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetRequest:
    boto3_raw_data: "type_defs.DescribeAssetRequestTypeDef" = dataclasses.field()

    assetId = field("assetId")
    excludeProperties = field("excludeProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAssetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBulkImportJobRequest:
    boto3_raw_data: "type_defs.DescribeBulkImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBulkImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBulkImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComputationModelExecutionSummaryRequest:
    boto3_raw_data: (
        "type_defs.DescribeComputationModelExecutionSummaryRequestTypeDef"
    ) = dataclasses.field()

    computationModelId = field("computationModelId")
    resolveToResourceType = field("resolveToResourceType")
    resolveToResourceId = field("resolveToResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComputationModelExecutionSummaryRequestTypeDef"
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
                "type_defs.DescribeComputationModelExecutionSummaryRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComputationModelRequest:
    boto3_raw_data: "type_defs.DescribeComputationModelRequestTypeDef" = (
        dataclasses.field()
    )

    computationModelId = field("computationModelId")
    computationModelVersion = field("computationModelVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeComputationModelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComputationModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDashboardRequest:
    boto3_raw_data: "type_defs.DescribeDashboardRequestTypeDef" = dataclasses.field()

    dashboardId = field("dashboardId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDashboardRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDashboardRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetRequest:
    boto3_raw_data: "type_defs.DescribeDatasetRequestTypeDef" = dataclasses.field()

    datasetId = field("datasetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExecutionRequest:
    boto3_raw_data: "type_defs.DescribeExecutionRequestTypeDef" = dataclasses.field()

    executionId = field("executionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionStatus:
    boto3_raw_data: "type_defs.ExecutionStatusTypeDef" = dataclasses.field()

    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExecutionStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayCapabilityConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeGatewayCapabilityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    gatewayId = field("gatewayId")
    capabilityNamespace = field("capabilityNamespace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGatewayCapabilityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayCapabilityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayRequest:
    boto3_raw_data: "type_defs.DescribeGatewayRequestTypeDef" = dataclasses.field()

    gatewayId = field("gatewayId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayCapabilitySummary:
    boto3_raw_data: "type_defs.GatewayCapabilitySummaryTypeDef" = dataclasses.field()

    capabilityNamespace = field("capabilityNamespace")
    capabilitySyncStatus = field("capabilitySyncStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GatewayCapabilitySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayCapabilitySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingOptions:
    boto3_raw_data: "type_defs.LoggingOptionsTypeDef" = dataclasses.field()

    level = field("level")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePortalRequest:
    boto3_raw_data: "type_defs.DescribePortalRequestTypeDef" = dataclasses.field()

    portalId = field("portalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePortalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePortalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageLocation:
    boto3_raw_data: "type_defs.ImageLocationTypeDef" = dataclasses.field()

    id = field("id")
    url = field("url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortalTypeEntryOutput:
    boto3_raw_data: "type_defs.PortalTypeEntryOutputTypeDef" = dataclasses.field()

    portalTools = field("portalTools")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PortalTypeEntryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PortalTypeEntryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProjectRequest:
    boto3_raw_data: "type_defs.DescribeProjectRequestTypeDef" = dataclasses.field()

    projectId = field("projectId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetentionPeriod:
    boto3_raw_data: "type_defs.RetentionPeriodTypeDef" = dataclasses.field()

    numberOfDays = field("numberOfDays")
    unlimited = field("unlimited")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetentionPeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetentionPeriodTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WarmTierRetentionPeriod:
    boto3_raw_data: "type_defs.WarmTierRetentionPeriodTypeDef" = dataclasses.field()

    numberOfDays = field("numberOfDays")
    unlimited = field("unlimited")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WarmTierRetentionPeriodTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WarmTierRetentionPeriodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTimeSeriesRequest:
    boto3_raw_data: "type_defs.DescribeTimeSeriesRequestTypeDef" = dataclasses.field()

    alias = field("alias")
    assetId = field("assetId")
    propertyId = field("propertyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTimeSeriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTimeSeriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetailedError:
    boto3_raw_data: "type_defs.DetailedErrorTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetailedErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetailedErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAssetsRequest:
    boto3_raw_data: "type_defs.DisassociateAssetsRequestTypeDef" = dataclasses.field()

    assetId = field("assetId")
    hierarchyId = field("hierarchyId")
    childAssetId = field("childAssetId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateAssetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateAssetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateTimeSeriesFromAssetPropertyRequest:
    boto3_raw_data: (
        "type_defs.DisassociateTimeSeriesFromAssetPropertyRequestTypeDef"
    ) = dataclasses.field()

    alias = field("alias")
    assetId = field("assetId")
    propertyId = field("propertyId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateTimeSeriesFromAssetPropertyRequestTypeDef"
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
                "type_defs.DisassociateTimeSeriesFromAssetPropertyRequestTypeDef"
            ]
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
class ExecuteQueryRequest:
    boto3_raw_data: "type_defs.ExecuteQueryRequestTypeDef" = dataclasses.field()

    queryStatement = field("queryStatement")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    clientToken = field("clientToken")

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
class ForwardingConfig:
    boto3_raw_data: "type_defs.ForwardingConfigTypeDef" = dataclasses.field()

    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ForwardingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForwardingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Greengrass:
    boto3_raw_data: "type_defs.GreengrassTypeDef" = dataclasses.field()

    groupArn = field("groupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GreengrassTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GreengrassTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GreengrassV2:
    boto3_raw_data: "type_defs.GreengrassV2TypeDef" = dataclasses.field()

    coreDeviceThingName = field("coreDeviceThingName")
    coreDeviceOperatingSystem = field("coreDeviceOperatingSystem")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GreengrassV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GreengrassV2TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SiemensIE:
    boto3_raw_data: "type_defs.SiemensIETypeDef" = dataclasses.field()

    iotCoreThingName = field("iotCoreThingName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SiemensIETypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SiemensIETypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetPropertyValueRequest:
    boto3_raw_data: "type_defs.GetAssetPropertyValueRequestTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssetPropertyValueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetPropertyValueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInterpolatedAssetPropertyValuesRequest:
    boto3_raw_data: "type_defs.GetInterpolatedAssetPropertyValuesRequestTypeDef" = (
        dataclasses.field()
    )

    startTimeInSeconds = field("startTimeInSeconds")
    endTimeInSeconds = field("endTimeInSeconds")
    quality = field("quality")
    intervalInSeconds = field("intervalInSeconds")
    type = field("type")
    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")
    startTimeOffsetInNanos = field("startTimeOffsetInNanos")
    endTimeOffsetInNanos = field("endTimeOffsetInNanos")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    intervalWindowInSeconds = field("intervalWindowInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInterpolatedAssetPropertyValuesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInterpolatedAssetPropertyValuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupIdentity:
    boto3_raw_data: "type_defs.GroupIdentityTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupIdentityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IAMRoleIdentity:
    boto3_raw_data: "type_defs.IAMRoleIdentityTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IAMRoleIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IAMRoleIdentityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IAMUserIdentity:
    boto3_raw_data: "type_defs.IAMUserIdentityTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IAMUserIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IAMUserIdentityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserIdentity:
    boto3_raw_data: "type_defs.UserIdentityTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserIdentityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterfaceRelationshipSummary:
    boto3_raw_data: "type_defs.InterfaceRelationshipSummaryTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InterfaceRelationshipSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterfaceRelationshipSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalFailureException:
    boto3_raw_data: "type_defs.InternalFailureExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InternalFailureExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalFailureExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvalidRequestException:
    boto3_raw_data: "type_defs.InvalidRequestExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvalidRequestExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvalidRequestExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeAssistantRequest:
    boto3_raw_data: "type_defs.InvokeAssistantRequestTypeDef" = dataclasses.field()

    message = field("message")
    conversationId = field("conversationId")
    enableTrace = field("enableTrace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeAssistantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeAssistantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSummary:
    boto3_raw_data: "type_defs.JobSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KendraSourceDetail:
    boto3_raw_data: "type_defs.KendraSourceDetailTypeDef" = dataclasses.field()

    knowledgeBaseArn = field("knowledgeBaseArn")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KendraSourceDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KendraSourceDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LimitExceededException:
    boto3_raw_data: "type_defs.LimitExceededExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LimitExceededExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LimitExceededExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPoliciesRequest:
    boto3_raw_data: "type_defs.ListAccessPoliciesRequestTypeDef" = dataclasses.field()

    identityType = field("identityType")
    identityId = field("identityId")
    resourceType = field("resourceType")
    resourceId = field("resourceId")
    iamArn = field("iamArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActionsRequest:
    boto3_raw_data: "type_defs.ListActionsRequestTypeDef" = dataclasses.field()

    targetResourceType = field("targetResourceType")
    targetResourceId = field("targetResourceId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    resolveToResourceType = field("resolveToResourceType")
    resolveToResourceId = field("resolveToResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetModelCompositeModelsRequest:
    boto3_raw_data: "type_defs.ListAssetModelCompositeModelsRequestTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    assetModelVersion = field("assetModelVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssetModelCompositeModelsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetModelCompositeModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetModelPropertiesRequest:
    boto3_raw_data: "type_defs.ListAssetModelPropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    filter = field("filter")
    assetModelVersion = field("assetModelVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssetModelPropertiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetModelPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetModelsRequest:
    boto3_raw_data: "type_defs.ListAssetModelsRequestTypeDef" = dataclasses.field()

    assetModelTypes = field("assetModelTypes")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    assetModelVersion = field("assetModelVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetPropertiesRequest:
    boto3_raw_data: "type_defs.ListAssetPropertiesRequestTypeDef" = dataclasses.field()

    assetId = field("assetId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    filter = field("filter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetPropertiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetRelationshipsRequest:
    boto3_raw_data: "type_defs.ListAssetRelationshipsRequestTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    traversalType = field("traversalType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssetRelationshipsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetRelationshipsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetsRequest:
    boto3_raw_data: "type_defs.ListAssetsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    assetModelId = field("assetModelId")
    filter = field("filter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAssetsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedAssetsRequest:
    boto3_raw_data: "type_defs.ListAssociatedAssetsRequestTypeDef" = dataclasses.field()

    assetId = field("assetId")
    hierarchyId = field("hierarchyId")
    traversalDirection = field("traversalDirection")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociatedAssetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedAssetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBulkImportJobsRequest:
    boto3_raw_data: "type_defs.ListBulkImportJobsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    filter = field("filter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBulkImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBulkImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCompositionRelationshipsRequest:
    boto3_raw_data: "type_defs.ListCompositionRelationshipsRequestTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCompositionRelationshipsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCompositionRelationshipsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputationModelResolveToResourcesRequest:
    boto3_raw_data: "type_defs.ListComputationModelResolveToResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    computationModelId = field("computationModelId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComputationModelResolveToResourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputationModelResolveToResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputationModelsRequest:
    boto3_raw_data: "type_defs.ListComputationModelsRequestTypeDef" = (
        dataclasses.field()
    )

    computationModelType = field("computationModelType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComputationModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputationModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDashboardsRequest:
    boto3_raw_data: "type_defs.ListDashboardsRequestTypeDef" = dataclasses.field()

    projectId = field("projectId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDashboardsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDashboardsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsRequest:
    boto3_raw_data: "type_defs.ListDatasetsRequestTypeDef" = dataclasses.field()

    sourceType = field("sourceType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExecutionsRequest:
    boto3_raw_data: "type_defs.ListExecutionsRequestTypeDef" = dataclasses.field()

    targetResourceType = field("targetResourceType")
    targetResourceId = field("targetResourceId")
    resolveToResourceType = field("resolveToResourceType")
    resolveToResourceId = field("resolveToResourceId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    actionType = field("actionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExecutionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysRequest:
    boto3_raw_data: "type_defs.ListGatewaysRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInterfaceRelationshipsRequest:
    boto3_raw_data: "type_defs.ListInterfaceRelationshipsRequestTypeDef" = (
        dataclasses.field()
    )

    interfaceAssetModelId = field("interfaceAssetModelId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInterfaceRelationshipsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInterfaceRelationshipsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortalsRequest:
    boto3_raw_data: "type_defs.ListPortalsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPortalsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortalsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectAssetsRequest:
    boto3_raw_data: "type_defs.ListProjectAssetsRequestTypeDef" = dataclasses.field()

    projectId = field("projectId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectAssetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectAssetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsRequest:
    boto3_raw_data: "type_defs.ListProjectsRequestTypeDef" = dataclasses.field()

    portalId = field("portalId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectSummary:
    boto3_raw_data: "type_defs.ProjectSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectSummaryTypeDef"]],
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
class ListTimeSeriesRequest:
    boto3_raw_data: "type_defs.ListTimeSeriesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    assetId = field("assetId")
    aliasPrefix = field("aliasPrefix")
    timeSeriesType = field("timeSeriesType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTimeSeriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTimeSeriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesSummary:
    boto3_raw_data: "type_defs.TimeSeriesSummaryTypeDef" = dataclasses.field()

    timeSeriesId = field("timeSeriesId")
    dataType = field("dataType")
    timeSeriesCreationDate = field("timeSeriesCreationDate")
    timeSeriesLastUpdateDate = field("timeSeriesLastUpdateDate")
    timeSeriesArn = field("timeSeriesArn")
    assetId = field("assetId")
    propertyId = field("propertyId")
    alias = field("alias")
    dataTypeSpec = field("dataTypeSpec")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Location:
    boto3_raw_data: "type_defs.LocationTypeDef" = dataclasses.field()

    uri = field("uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricProcessingConfig:
    boto3_raw_data: "type_defs.MetricProcessingConfigTypeDef" = dataclasses.field()

    computeLocation = field("computeLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricProcessingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricProcessingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TumblingWindow:
    boto3_raw_data: "type_defs.TumblingWindowTypeDef" = dataclasses.field()

    interval = field("interval")
    offset = field("offset")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TumblingWindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TumblingWindowTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorErrorDetails:
    boto3_raw_data: "type_defs.MonitorErrorDetailsTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitorErrorDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitorErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortalResource:
    boto3_raw_data: "type_defs.PortalResourceTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortalResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortalResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortalTypeEntry:
    boto3_raw_data: "type_defs.PortalTypeEntryTypeDef" = dataclasses.field()

    portalTools = field("portalTools")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortalTypeEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortalTypeEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectResource:
    boto3_raw_data: "type_defs.ProjectResourceTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyValueNullValue:
    boto3_raw_data: "type_defs.PropertyValueNullValueTypeDef" = dataclasses.field()

    valueType = field("valueType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyValueNullValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyValueNullValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDefaultEncryptionConfigurationRequest:
    boto3_raw_data: "type_defs.PutDefaultEncryptionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    encryptionType = field("encryptionType")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutDefaultEncryptionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDefaultEncryptionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceNotFoundException:
    boto3_raw_data: "type_defs.ResourceNotFoundExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceNotFoundExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceNotFoundExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThrottlingException:
    boto3_raw_data: "type_defs.ThrottlingExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThrottlingExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThrottlingExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Trace:
    boto3_raw_data: "type_defs.TraceTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TraceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TraceTypeDef"]]
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
class UpdateAssetPropertyRequest:
    boto3_raw_data: "type_defs.UpdateAssetPropertyRequestTypeDef" = dataclasses.field()

    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")
    propertyNotificationState = field("propertyNotificationState")
    clientToken = field("clientToken")
    propertyUnit = field("propertyUnit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssetPropertyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetPropertyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssetRequest:
    boto3_raw_data: "type_defs.UpdateAssetRequestTypeDef" = dataclasses.field()

    assetId = field("assetId")
    assetName = field("assetName")
    assetExternalId = field("assetExternalId")
    clientToken = field("clientToken")
    assetDescription = field("assetDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDashboardRequest:
    boto3_raw_data: "type_defs.UpdateDashboardRequestTypeDef" = dataclasses.field()

    dashboardId = field("dashboardId")
    dashboardName = field("dashboardName")
    dashboardDefinition = field("dashboardDefinition")
    dashboardDescription = field("dashboardDescription")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDashboardRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDashboardRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayCapabilityConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateGatewayCapabilityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    gatewayId = field("gatewayId")
    capabilityNamespace = field("capabilityNamespace")
    capabilityConfiguration = field("capabilityConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateGatewayCapabilityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayCapabilityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayRequest:
    boto3_raw_data: "type_defs.UpdateGatewayRequestTypeDef" = dataclasses.field()

    gatewayId = field("gatewayId")
    gatewayName = field("gatewayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectRequest:
    boto3_raw_data: "type_defs.UpdateProjectRequestTypeDef" = dataclasses.field()

    projectId = field("projectId")
    projectName = field("projectName")
    projectDescription = field("projectDescription")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputationModelResolveToResourceSummary:
    boto3_raw_data: "type_defs.ComputationModelResolveToResourceSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resolveTo(self):  # pragma: no cover
        return ResolveTo.make_one(self.boto3_raw_data["resolveTo"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComputationModelResolveToResourceSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputationModelResolveToResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionSummary:
    boto3_raw_data: "type_defs.ActionSummaryTypeDef" = dataclasses.field()

    actionId = field("actionId")
    actionDefinitionId = field("actionDefinitionId")

    @cached_property
    def targetResource(self):  # pragma: no cover
        return TargetResource.make_one(self.boto3_raw_data["targetResource"])

    @cached_property
    def resolveTo(self):  # pragma: no cover
        return ResolveTo.make_one(self.boto3_raw_data["resolveTo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteActionRequest:
    boto3_raw_data: "type_defs.ExecuteActionRequestTypeDef" = dataclasses.field()

    @cached_property
    def targetResource(self):  # pragma: no cover
        return TargetResource.make_one(self.boto3_raw_data["targetResource"])

    actionDefinitionId = field("actionDefinitionId")

    @cached_property
    def actionPayload(self):  # pragma: no cover
        return ActionPayload.make_one(self.boto3_raw_data["actionPayload"])

    clientToken = field("clientToken")

    @cached_property
    def resolveTo(self):  # pragma: no cover
        return ResolveTo.make_one(self.boto3_raw_data["resolveTo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatedValue:
    boto3_raw_data: "type_defs.AggregatedValueTypeDef" = dataclasses.field()

    timestamp = field("timestamp")

    @cached_property
    def value(self):  # pragma: no cover
        return Aggregates.make_one(self.boto3_raw_data["value"])

    quality = field("quality")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AggregatedValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AggregatedValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetCompositeModelSummary:
    boto3_raw_data: "type_defs.AssetCompositeModelSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    type = field("type")
    description = field("description")

    @cached_property
    def path(self):  # pragma: no cover
        return AssetCompositeModelPathSegment.make_many(self.boto3_raw_data["path"])

    externalId = field("externalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetCompositeModelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetCompositeModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetRelationshipSummary:
    boto3_raw_data: "type_defs.AssetRelationshipSummaryTypeDef" = dataclasses.field()

    relationshipType = field("relationshipType")

    @cached_property
    def hierarchyInfo(self):  # pragma: no cover
        return AssetHierarchyInfo.make_one(self.boto3_raw_data["hierarchyInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetRelationshipSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetRelationshipSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelCompositeModelSummary:
    boto3_raw_data: "type_defs.AssetModelCompositeModelSummaryTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    type = field("type")
    externalId = field("externalId")
    description = field("description")

    @cached_property
    def path(self):  # pragma: no cover
        return AssetModelCompositeModelPathSegment.make_many(
            self.boto3_raw_data["path"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssetModelCompositeModelSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelCompositeModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariableValueOutput:
    boto3_raw_data: "type_defs.VariableValueOutputTypeDef" = dataclasses.field()

    propertyId = field("propertyId")
    hierarchyId = field("hierarchyId")

    @cached_property
    def propertyPath(self):  # pragma: no cover
        return AssetModelPropertyPathSegment.make_many(
            self.boto3_raw_data["propertyPath"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VariableValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VariableValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariableValue:
    boto3_raw_data: "type_defs.VariableValueTypeDef" = dataclasses.field()

    propertyId = field("propertyId")
    hierarchyId = field("hierarchyId")

    @cached_property
    def propertyPath(self):  # pragma: no cover
        return AssetModelPropertyPathSegment.make_many(
            self.boto3_raw_data["propertyPath"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VariableValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VariableValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataBindingValueFilter:
    boto3_raw_data: "type_defs.DataBindingValueFilterTypeDef" = dataclasses.field()

    @cached_property
    def asset(self):  # pragma: no cover
        return AssetBindingValueFilter.make_one(self.boto3_raw_data["asset"])

    @cached_property
    def assetModel(self):  # pragma: no cover
        return AssetModelBindingValueFilter.make_one(self.boto3_raw_data["assetModel"])

    @cached_property
    def assetProperty(self):  # pragma: no cover
        return AssetPropertyBindingValueFilter.make_one(
            self.boto3_raw_data["assetProperty"]
        )

    @cached_property
    def assetModelProperty(self):  # pragma: no cover
        return AssetModelPropertyBindingValueFilter.make_one(
            self.boto3_raw_data["assetModelProperty"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataBindingValueFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataBindingValueFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputationModelDataBindingValueOutput:
    boto3_raw_data: "type_defs.ComputationModelDataBindingValueOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assetModelProperty(self):  # pragma: no cover
        return AssetModelPropertyBindingValue.make_one(
            self.boto3_raw_data["assetModelProperty"]
        )

    @cached_property
    def assetProperty(self):  # pragma: no cover
        return AssetPropertyBindingValue.make_one(self.boto3_raw_data["assetProperty"])

    list = field("list")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComputationModelDataBindingValueOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputationModelDataBindingValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputationModelDataBindingValue:
    boto3_raw_data: "type_defs.ComputationModelDataBindingValueTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assetModelProperty(self):  # pragma: no cover
        return AssetModelPropertyBindingValue.make_one(
            self.boto3_raw_data["assetModelProperty"]
        )

    @cached_property
    def assetProperty(self):  # pragma: no cover
        return AssetPropertyBindingValue.make_one(self.boto3_raw_data["assetProperty"])

    list = field("list")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComputationModelDataBindingValueTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputationModelDataBindingValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataBindingValue:
    boto3_raw_data: "type_defs.DataBindingValueTypeDef" = dataclasses.field()

    @cached_property
    def assetModelProperty(self):  # pragma: no cover
        return AssetModelPropertyBindingValue.make_one(
            self.boto3_raw_data["assetModelProperty"]
        )

    @cached_property
    def assetProperty(self):  # pragma: no cover
        return AssetPropertyBindingValue.make_one(self.boto3_raw_data["assetProperty"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataBindingValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataBindingValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertySummary:
    boto3_raw_data: "type_defs.AssetPropertySummaryTypeDef" = dataclasses.field()

    id = field("id")
    externalId = field("externalId")
    alias = field("alias")
    unit = field("unit")

    @cached_property
    def notification(self):  # pragma: no cover
        return PropertyNotification.make_one(self.boto3_raw_data["notification"])

    assetCompositeModelId = field("assetCompositeModelId")

    @cached_property
    def path(self):  # pragma: no cover
        return AssetPropertyPathSegment.make_many(self.boto3_raw_data["path"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetPropertySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetProperty:
    boto3_raw_data: "type_defs.AssetPropertyTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    dataType = field("dataType")
    externalId = field("externalId")
    alias = field("alias")

    @cached_property
    def notification(self):  # pragma: no cover
        return PropertyNotification.make_one(self.boto3_raw_data["notification"])

    dataTypeSpec = field("dataTypeSpec")
    unit = field("unit")

    @cached_property
    def path(self):  # pragma: no cover
        return AssetPropertyPathSegment.make_many(self.boto3_raw_data["path"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetPropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetPropertyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutAssetPropertyError:
    boto3_raw_data: "type_defs.BatchPutAssetPropertyErrorTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @cached_property
    def timestamps(self):  # pragma: no cover
        return TimeInNanos.make_many(self.boto3_raw_data["timestamps"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutAssetPropertyErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutAssetPropertyErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateProjectAssetsResponse:
    boto3_raw_data: "type_defs.BatchAssociateProjectAssetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return AssetErrorDetails.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateProjectAssetsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateProjectAssetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateProjectAssetsResponse:
    boto3_raw_data: "type_defs.BatchDisassociateProjectAssetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return AssetErrorDetails.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateProjectAssetsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisassociateProjectAssetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPolicyResponse:
    boto3_raw_data: "type_defs.CreateAccessPolicyResponseTypeDef" = dataclasses.field()

    accessPolicyId = field("accessPolicyId")
    accessPolicyArn = field("accessPolicyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBulkImportJobResponse:
    boto3_raw_data: "type_defs.CreateBulkImportJobResponseTypeDef" = dataclasses.field()

    jobId = field("jobId")
    jobName = field("jobName")
    jobStatus = field("jobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBulkImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBulkImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDashboardResponse:
    boto3_raw_data: "type_defs.CreateDashboardResponseTypeDef" = dataclasses.field()

    dashboardId = field("dashboardId")
    dashboardArn = field("dashboardArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDashboardResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDashboardResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGatewayResponse:
    boto3_raw_data: "type_defs.CreateGatewayResponseTypeDef" = dataclasses.field()

    gatewayId = field("gatewayId")
    gatewayArn = field("gatewayArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectResponse:
    boto3_raw_data: "type_defs.CreateProjectResponseTypeDef" = dataclasses.field()

    projectId = field("projectId")
    projectArn = field("projectArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActionResponse:
    boto3_raw_data: "type_defs.DescribeActionResponseTypeDef" = dataclasses.field()

    actionId = field("actionId")

    @cached_property
    def targetResource(self):  # pragma: no cover
        return TargetResource.make_one(self.boto3_raw_data["targetResource"])

    actionDefinitionId = field("actionDefinitionId")

    @cached_property
    def actionPayload(self):  # pragma: no cover
        return ActionPayload.make_one(self.boto3_raw_data["actionPayload"])

    executionTime = field("executionTime")

    @cached_property
    def resolveTo(self):  # pragma: no cover
        return ResolveTo.make_one(self.boto3_raw_data["resolveTo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComputationModelExecutionSummaryResponse:
    boto3_raw_data: (
        "type_defs.DescribeComputationModelExecutionSummaryResponseTypeDef"
    ) = dataclasses.field()

    computationModelId = field("computationModelId")

    @cached_property
    def resolveTo(self):  # pragma: no cover
        return ResolveTo.make_one(self.boto3_raw_data["resolveTo"])

    computationModelExecutionSummary = field("computationModelExecutionSummary")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComputationModelExecutionSummaryResponseTypeDef"
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
                "type_defs.DescribeComputationModelExecutionSummaryResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDashboardResponse:
    boto3_raw_data: "type_defs.DescribeDashboardResponseTypeDef" = dataclasses.field()

    dashboardId = field("dashboardId")
    dashboardArn = field("dashboardArn")
    dashboardName = field("dashboardName")
    projectId = field("projectId")
    dashboardDescription = field("dashboardDescription")
    dashboardDefinition = field("dashboardDefinition")
    dashboardCreationDate = field("dashboardCreationDate")
    dashboardLastUpdateDate = field("dashboardLastUpdateDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDashboardResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDashboardResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayCapabilityConfigurationResponse:
    boto3_raw_data: (
        "type_defs.DescribeGatewayCapabilityConfigurationResponseTypeDef"
    ) = dataclasses.field()

    gatewayId = field("gatewayId")
    capabilityNamespace = field("capabilityNamespace")
    capabilityConfiguration = field("capabilityConfiguration")
    capabilitySyncStatus = field("capabilitySyncStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGatewayCapabilityConfigurationResponseTypeDef"
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
                "type_defs.DescribeGatewayCapabilityConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProjectResponse:
    boto3_raw_data: "type_defs.DescribeProjectResponseTypeDef" = dataclasses.field()

    projectId = field("projectId")
    projectArn = field("projectArn")
    projectName = field("projectName")
    portalId = field("portalId")
    projectDescription = field("projectDescription")
    projectCreationDate = field("projectCreationDate")
    projectLastUpdateDate = field("projectLastUpdateDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTimeSeriesResponse:
    boto3_raw_data: "type_defs.DescribeTimeSeriesResponseTypeDef" = dataclasses.field()

    assetId = field("assetId")
    propertyId = field("propertyId")
    alias = field("alias")
    timeSeriesId = field("timeSeriesId")
    dataType = field("dataType")
    dataTypeSpec = field("dataTypeSpec")
    timeSeriesCreationDate = field("timeSeriesCreationDate")
    timeSeriesLastUpdateDate = field("timeSeriesLastUpdateDate")
    timeSeriesArn = field("timeSeriesArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTimeSeriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTimeSeriesResponseTypeDef"]
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
class ExecuteActionResponse:
    boto3_raw_data: "type_defs.ExecuteActionResponseTypeDef" = dataclasses.field()

    actionId = field("actionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectAssetsResponse:
    boto3_raw_data: "type_defs.ListProjectAssetsResponseTypeDef" = dataclasses.field()

    assetIds = field("assetIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectAssetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectAssetsResponseTypeDef"]
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
class UpdateGatewayCapabilityConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateGatewayCapabilityConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    capabilityNamespace = field("capabilityNamespace")
    capabilitySyncStatus = field("capabilitySyncStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateGatewayCapabilityConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayCapabilityConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyAggregatesEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyAggregatesEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")
    aggregateTypes = field("aggregateTypes")
    resolution = field("resolution")
    startDate = field("startDate")
    endDate = field("endDate")
    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")
    qualities = field("qualities")
    timeOrdering = field("timeOrdering")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyAggregatesEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyAggregatesEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueHistoryEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueHistoryEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")
    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")
    startDate = field("startDate")
    endDate = field("endDate")
    qualities = field("qualities")
    timeOrdering = field("timeOrdering")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueHistoryEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueHistoryEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetPropertyAggregatesRequest:
    boto3_raw_data: "type_defs.GetAssetPropertyAggregatesRequestTypeDef" = (
        dataclasses.field()
    )

    aggregateTypes = field("aggregateTypes")
    resolution = field("resolution")
    startDate = field("startDate")
    endDate = field("endDate")
    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")
    qualities = field("qualities")
    timeOrdering = field("timeOrdering")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAssetPropertyAggregatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetPropertyAggregatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetPropertyValueHistoryRequest:
    boto3_raw_data: "type_defs.GetAssetPropertyValueHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")
    startDate = field("startDate")
    endDate = field("endDate")
    qualities = field("qualities")
    timeOrdering = field("timeOrdering")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAssetPropertyValueHistoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetPropertyValueHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyAggregatesSkippedEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyAggregatesSkippedEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")
    completionStatus = field("completionStatus")

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return BatchGetAssetPropertyAggregatesErrorInfo.make_one(
            self.boto3_raw_data["errorInfo"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyAggregatesSkippedEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyAggregatesSkippedEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueRequest:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entries(self):  # pragma: no cover
        return BatchGetAssetPropertyValueEntry.make_many(self.boto3_raw_data["entries"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueSkippedEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueSkippedEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")
    completionStatus = field("completionStatus")

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return BatchGetAssetPropertyValueErrorInfo.make_one(
            self.boto3_raw_data["errorInfo"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueSkippedEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueSkippedEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueHistorySkippedEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueHistorySkippedEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")
    completionStatus = field("completionStatus")

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return BatchGetAssetPropertyValueHistoryErrorInfo.make_one(
            self.boto3_raw_data["errorInfo"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueHistorySkippedEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueHistorySkippedEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageFile:
    boto3_raw_data: "type_defs.ImageFileTypeDef" = dataclasses.field()

    data = field("data")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageFileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnInfo:
    boto3_raw_data: "type_defs.ColumnInfoTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def type(self):  # pragma: no cover
        return ColumnType.make_one(self.boto3_raw_data["type"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositionDetails:
    boto3_raw_data: "type_defs.CompositionDetailsTypeDef" = dataclasses.field()

    @cached_property
    def compositionRelationship(self):  # pragma: no cover
        return CompositionRelationshipItem.make_many(
            self.boto3_raw_data["compositionRelationship"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompositionDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCompositionRelationshipsResponse:
    boto3_raw_data: "type_defs.ListCompositionRelationshipsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def compositionRelationshipSummaries(self):  # pragma: no cover
        return CompositionRelationshipSummary.make_many(
            self.boto3_raw_data["compositionRelationshipSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCompositionRelationshipsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCompositionRelationshipsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputationModelConfiguration:
    boto3_raw_data: "type_defs.ComputationModelConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def anomalyDetection(self):  # pragma: no cover
        return ComputationModelAnomalyDetectionConfiguration.make_one(
            self.boto3_raw_data["anomalyDetection"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComputationModelConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputationModelConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationStatus:
    boto3_raw_data: "type_defs.ConfigurationStatusTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def error(self):  # pragma: no cover
        return ConfigurationErrorDetails.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileFormatOutput:
    boto3_raw_data: "type_defs.FileFormatOutputTypeDef" = dataclasses.field()

    @cached_property
    def csv(self):  # pragma: no cover
        return CsvOutput.make_one(self.boto3_raw_data["csv"])

    parquet = field("parquet")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileFormatOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileFormatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileFormat:
    boto3_raw_data: "type_defs.FileFormatTypeDef" = dataclasses.field()

    @cached_property
    def csv(self):  # pragma: no cover
        return Csv.make_one(self.boto3_raw_data["csv"])

    parquet = field("parquet")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileFormatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileFormatTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiLayerStorage:
    boto3_raw_data: "type_defs.MultiLayerStorageTypeDef" = dataclasses.field()

    @cached_property
    def customerManagedS3Storage(self):  # pragma: no cover
        return CustomerManagedS3Storage.make_one(
            self.boto3_raw_data["customerManagedS3Storage"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MultiLayerStorageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiLayerStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDashboardsResponse:
    boto3_raw_data: "type_defs.ListDashboardsResponseTypeDef" = dataclasses.field()

    @cached_property
    def dashboardSummaries(self):  # pragma: no cover
        return DashboardSummary.make_many(self.boto3_raw_data["dashboardSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDashboardsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDashboardsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RowPaginator:
    boto3_raw_data: "type_defs.RowPaginatorTypeDef" = dataclasses.field()

    @cached_property
    def data(self):  # pragma: no cover
        return DatumPaginator.make_many(self.boto3_raw_data["data"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowPaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowPaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Row:
    boto3_raw_data: "type_defs.RowTypeDef" = dataclasses.field()

    @cached_property
    def data(self):  # pragma: no cover
        return Datum.make_many(self.boto3_raw_data["data"])

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
class RowWaiter:
    boto3_raw_data: "type_defs.RowWaiterTypeDef" = dataclasses.field()

    @cached_property
    def data(self):  # pragma: no cover
        return DatumWaiter.make_many(self.boto3_raw_data["data"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowWaiterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowWaiterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetModelInterfaceRelationshipResponse:
    boto3_raw_data: (
        "type_defs.DescribeAssetModelInterfaceRelationshipResponseTypeDef"
    ) = dataclasses.field()

    assetModelId = field("assetModelId")
    interfaceAssetModelId = field("interfaceAssetModelId")

    @cached_property
    def propertyMappings(self):  # pragma: no cover
        return PropertyMapping.make_many(self.boto3_raw_data["propertyMappings"])

    @cached_property
    def hierarchyMappings(self):  # pragma: no cover
        return HierarchyMapping.make_many(self.boto3_raw_data["hierarchyMappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssetModelInterfaceRelationshipResponseTypeDef"
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
                "type_defs.DescribeAssetModelInterfaceRelationshipResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyMappingConfiguration:
    boto3_raw_data: "type_defs.PropertyMappingConfigurationTypeDef" = (
        dataclasses.field()
    )

    matchByPropertyName = field("matchByPropertyName")
    createMissingProperty = field("createMissingProperty")

    @cached_property
    def overrides(self):  # pragma: no cover
        return PropertyMapping.make_many(self.boto3_raw_data["overrides"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyMappingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyMappingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetModelRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeAssetModelRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    excludeProperties = field("excludeProperties")
    assetModelVersion = field("assetModelVersion")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssetModelRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetModelRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetModelRequestWait:
    boto3_raw_data: "type_defs.DescribeAssetModelRequestWaitTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    excludeProperties = field("excludeProperties")
    assetModelVersion = field("assetModelVersion")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAssetModelRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetModelRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeAssetRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    excludeProperties = field("excludeProperties")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAssetRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetRequestWait:
    boto3_raw_data: "type_defs.DescribeAssetRequestWaitTypeDef" = dataclasses.field()

    assetId = field("assetId")
    excludeProperties = field("excludeProperties")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAssetRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePortalRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribePortalRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    portalId = field("portalId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePortalRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePortalRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePortalRequestWait:
    boto3_raw_data: "type_defs.DescribePortalRequestWaitTypeDef" = dataclasses.field()

    portalId = field("portalId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePortalRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePortalRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExecutionResponse:
    boto3_raw_data: "type_defs.DescribeExecutionResponseTypeDef" = dataclasses.field()

    executionId = field("executionId")
    actionType = field("actionType")

    @cached_property
    def targetResource(self):  # pragma: no cover
        return TargetResource.make_one(self.boto3_raw_data["targetResource"])

    targetResourceVersion = field("targetResourceVersion")

    @cached_property
    def resolveTo(self):  # pragma: no cover
        return ResolveTo.make_one(self.boto3_raw_data["resolveTo"])

    executionStartTime = field("executionStartTime")
    executionEndTime = field("executionEndTime")

    @cached_property
    def executionStatus(self):  # pragma: no cover
        return ExecutionStatus.make_one(self.boto3_raw_data["executionStatus"])

    executionResult = field("executionResult")
    executionDetails = field("executionDetails")
    executionEntityVersion = field("executionEntityVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionSummary:
    boto3_raw_data: "type_defs.ExecutionSummaryTypeDef" = dataclasses.field()

    executionId = field("executionId")

    @cached_property
    def targetResource(self):  # pragma: no cover
        return TargetResource.make_one(self.boto3_raw_data["targetResource"])

    targetResourceVersion = field("targetResourceVersion")
    executionStartTime = field("executionStartTime")

    @cached_property
    def executionStatus(self):  # pragma: no cover
        return ExecutionStatus.make_one(self.boto3_raw_data["executionStatus"])

    actionType = field("actionType")

    @cached_property
    def resolveTo(self):  # pragma: no cover
        return ResolveTo.make_one(self.boto3_raw_data["resolveTo"])

    executionEndTime = field("executionEndTime")
    executionEntityVersion = field("executionEntityVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoggingOptionsResponse:
    boto3_raw_data: "type_defs.DescribeLoggingOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def loggingOptions(self):  # pragma: no cover
        return LoggingOptions.make_one(self.boto3_raw_data["loggingOptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLoggingOptionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoggingOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLoggingOptionsRequest:
    boto3_raw_data: "type_defs.PutLoggingOptionsRequestTypeDef" = dataclasses.field()

    @cached_property
    def loggingOptions(self):  # pragma: no cover
        return LoggingOptions.make_one(self.boto3_raw_data["loggingOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLoggingOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLoggingOptionsRequestTypeDef"]
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

    @cached_property
    def details(self):  # pragma: no cover
        return DetailedError.make_many(self.boto3_raw_data["details"])

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
class ExecuteQueryRequestPaginate:
    boto3_raw_data: "type_defs.ExecuteQueryRequestPaginateTypeDef" = dataclasses.field()

    queryStatement = field("queryStatement")
    clientToken = field("clientToken")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteQueryRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteQueryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetPropertyAggregatesRequestPaginate:
    boto3_raw_data: "type_defs.GetAssetPropertyAggregatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    aggregateTypes = field("aggregateTypes")
    resolution = field("resolution")
    startDate = field("startDate")
    endDate = field("endDate")
    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")
    qualities = field("qualities")
    timeOrdering = field("timeOrdering")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAssetPropertyAggregatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetPropertyAggregatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetPropertyValueHistoryRequestPaginate:
    boto3_raw_data: "type_defs.GetAssetPropertyValueHistoryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")
    startDate = field("startDate")
    endDate = field("endDate")
    qualities = field("qualities")
    timeOrdering = field("timeOrdering")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAssetPropertyValueHistoryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetPropertyValueHistoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInterpolatedAssetPropertyValuesRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetInterpolatedAssetPropertyValuesRequestPaginateTypeDef"
    ) = dataclasses.field()

    startTimeInSeconds = field("startTimeInSeconds")
    endTimeInSeconds = field("endTimeInSeconds")
    quality = field("quality")
    intervalInSeconds = field("intervalInSeconds")
    type = field("type")
    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")
    startTimeOffsetInNanos = field("startTimeOffsetInNanos")
    endTimeOffsetInNanos = field("endTimeOffsetInNanos")
    intervalWindowInSeconds = field("intervalWindowInSeconds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInterpolatedAssetPropertyValuesRequestPaginateTypeDef"
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
                "type_defs.GetInterpolatedAssetPropertyValuesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListAccessPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    identityType = field("identityType")
    identityId = field("identityId")
    resourceType = field("resourceType")
    resourceId = field("resourceId")
    iamArn = field("iamArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListActionsRequestPaginateTypeDef" = dataclasses.field()

    targetResourceType = field("targetResourceType")
    targetResourceId = field("targetResourceId")
    resolveToResourceType = field("resolveToResourceType")
    resolveToResourceId = field("resolveToResourceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetModelCompositeModelsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssetModelCompositeModelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    assetModelVersion = field("assetModelVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssetModelCompositeModelsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetModelCompositeModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetModelPropertiesRequestPaginate:
    boto3_raw_data: "type_defs.ListAssetModelPropertiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    filter = field("filter")
    assetModelVersion = field("assetModelVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssetModelPropertiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetModelPropertiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetModelsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssetModelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assetModelTypes = field("assetModelTypes")
    assetModelVersion = field("assetModelVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssetModelsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetPropertiesRequestPaginate:
    boto3_raw_data: "type_defs.ListAssetPropertiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    filter = field("filter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssetPropertiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetPropertiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetRelationshipsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssetRelationshipsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    traversalType = field("traversalType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssetRelationshipsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetRelationshipsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssetsRequestPaginateTypeDef" = dataclasses.field()

    assetModelId = field("assetModelId")
    filter = field("filter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedAssetsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssociatedAssetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    hierarchyId = field("hierarchyId")
    traversalDirection = field("traversalDirection")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociatedAssetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedAssetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBulkImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListBulkImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    filter = field("filter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBulkImportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBulkImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCompositionRelationshipsRequestPaginate:
    boto3_raw_data: "type_defs.ListCompositionRelationshipsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCompositionRelationshipsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCompositionRelationshipsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputationModelResolveToResourcesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListComputationModelResolveToResourcesRequestPaginateTypeDef"
    ) = dataclasses.field()

    computationModelId = field("computationModelId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComputationModelResolveToResourcesRequestPaginateTypeDef"
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
                "type_defs.ListComputationModelResolveToResourcesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputationModelsRequestPaginate:
    boto3_raw_data: "type_defs.ListComputationModelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    computationModelType = field("computationModelType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComputationModelsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputationModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDashboardsRequestPaginate:
    boto3_raw_data: "type_defs.ListDashboardsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    projectId = field("projectId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDashboardsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDashboardsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetsRequestPaginateTypeDef" = dataclasses.field()

    sourceType = field("sourceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    targetResourceType = field("targetResourceType")
    targetResourceId = field("targetResourceId")
    resolveToResourceType = field("resolveToResourceType")
    resolveToResourceId = field("resolveToResourceId")
    actionType = field("actionType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExecutionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysRequestPaginate:
    boto3_raw_data: "type_defs.ListGatewaysRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInterfaceRelationshipsRequestPaginate:
    boto3_raw_data: "type_defs.ListInterfaceRelationshipsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    interfaceAssetModelId = field("interfaceAssetModelId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInterfaceRelationshipsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInterfaceRelationshipsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortalsRequestPaginate:
    boto3_raw_data: "type_defs.ListPortalsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPortalsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortalsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectAssetsRequestPaginate:
    boto3_raw_data: "type_defs.ListProjectAssetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    projectId = field("projectId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProjectAssetsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectAssetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsRequestPaginate:
    boto3_raw_data: "type_defs.ListProjectsRequestPaginateTypeDef" = dataclasses.field()

    portalId = field("portalId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTimeSeriesRequestPaginate:
    boto3_raw_data: "type_defs.ListTimeSeriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    aliasPrefix = field("aliasPrefix")
    timeSeriesType = field("timeSeriesType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTimeSeriesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTimeSeriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeasurementProcessingConfig:
    boto3_raw_data: "type_defs.MeasurementProcessingConfigTypeDef" = dataclasses.field()

    @cached_property
    def forwardingConfig(self):  # pragma: no cover
        return ForwardingConfig.make_one(self.boto3_raw_data["forwardingConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MeasurementProcessingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MeasurementProcessingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransformProcessingConfig:
    boto3_raw_data: "type_defs.TransformProcessingConfigTypeDef" = dataclasses.field()

    computeLocation = field("computeLocation")

    @cached_property
    def forwardingConfig(self):  # pragma: no cover
        return ForwardingConfig.make_one(self.boto3_raw_data["forwardingConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransformProcessingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransformProcessingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayPlatform:
    boto3_raw_data: "type_defs.GatewayPlatformTypeDef" = dataclasses.field()

    @cached_property
    def greengrass(self):  # pragma: no cover
        return Greengrass.make_one(self.boto3_raw_data["greengrass"])

    @cached_property
    def greengrassV2(self):  # pragma: no cover
        return GreengrassV2.make_one(self.boto3_raw_data["greengrassV2"])

    @cached_property
    def siemensIE(self):  # pragma: no cover
        return SiemensIE.make_one(self.boto3_raw_data["siemensIE"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayPlatformTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GatewayPlatformTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Identity:
    boto3_raw_data: "type_defs.IdentityTypeDef" = dataclasses.field()

    @cached_property
    def user(self):  # pragma: no cover
        return UserIdentity.make_one(self.boto3_raw_data["user"])

    @cached_property
    def group(self):  # pragma: no cover
        return GroupIdentity.make_one(self.boto3_raw_data["group"])

    @cached_property
    def iamUser(self):  # pragma: no cover
        return IAMUserIdentity.make_one(self.boto3_raw_data["iamUser"])

    @cached_property
    def iamRole(self):  # pragma: no cover
        return IAMRoleIdentity.make_one(self.boto3_raw_data["iamRole"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdentityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInterfaceRelationshipsResponse:
    boto3_raw_data: "type_defs.ListInterfaceRelationshipsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def interfaceRelationshipSummaries(self):  # pragma: no cover
        return InterfaceRelationshipSummary.make_many(
            self.boto3_raw_data["interfaceRelationshipSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInterfaceRelationshipsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInterfaceRelationshipsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBulkImportJobsResponse:
    boto3_raw_data: "type_defs.ListBulkImportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobSummaries(self):  # pragma: no cover
        return JobSummary.make_many(self.boto3_raw_data["jobSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBulkImportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBulkImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceDetail:
    boto3_raw_data: "type_defs.SourceDetailTypeDef" = dataclasses.field()

    @cached_property
    def kendra(self):  # pragma: no cover
        return KendraSourceDetail.make_one(self.boto3_raw_data["kendra"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsResponse:
    boto3_raw_data: "type_defs.ListProjectsResponseTypeDef" = dataclasses.field()

    @cached_property
    def projectSummaries(self):  # pragma: no cover
        return ProjectSummary.make_many(self.boto3_raw_data["projectSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTimeSeriesResponse:
    boto3_raw_data: "type_defs.ListTimeSeriesResponseTypeDef" = dataclasses.field()

    @cached_property
    def TimeSeriesSummaries(self):  # pragma: no cover
        return TimeSeriesSummary.make_many(self.boto3_raw_data["TimeSeriesSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTimeSeriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTimeSeriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Source:
    boto3_raw_data: "type_defs.SourceTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricWindow:
    boto3_raw_data: "type_defs.MetricWindowTypeDef" = dataclasses.field()

    @cached_property
    def tumbling(self):  # pragma: no cover
        return TumblingWindow.make_one(self.boto3_raw_data["tumbling"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricWindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricWindowTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortalStatus:
    boto3_raw_data: "type_defs.PortalStatusTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def error(self):  # pragma: no cover
        return MonitorErrorDetails.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortalStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortalStatusTypeDef"]],
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
    def portal(self):  # pragma: no cover
        return PortalResource.make_one(self.boto3_raw_data["portal"])

    @cached_property
    def project(self):  # pragma: no cover
        return ProjectResource.make_one(self.boto3_raw_data["project"])

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
class Variant:
    boto3_raw_data: "type_defs.VariantTypeDef" = dataclasses.field()

    stringValue = field("stringValue")
    integerValue = field("integerValue")
    doubleValue = field("doubleValue")
    booleanValue = field("booleanValue")

    @cached_property
    def nullValue(self):  # pragma: no cover
        return PropertyValueNullValue.make_one(self.boto3_raw_data["nullValue"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VariantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VariantTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputationModelResolveToResourcesResponse:
    boto3_raw_data: (
        "type_defs.ListComputationModelResolveToResourcesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def computationModelResolveToResourceSummaries(self):  # pragma: no cover
        return ComputationModelResolveToResourceSummary.make_many(
            self.boto3_raw_data["computationModelResolveToResourceSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComputationModelResolveToResourcesResponseTypeDef"
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
                "type_defs.ListComputationModelResolveToResourcesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActionsResponse:
    boto3_raw_data: "type_defs.ListActionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def actionSummaries(self):  # pragma: no cover
        return ActionSummary.make_many(self.boto3_raw_data["actionSummaries"])

    nextToken = field("nextToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyAggregatesSuccessEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyAggregatesSuccessEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")

    @cached_property
    def aggregatedValues(self):  # pragma: no cover
        return AggregatedValue.make_many(self.boto3_raw_data["aggregatedValues"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyAggregatesSuccessEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyAggregatesSuccessEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetPropertyAggregatesResponse:
    boto3_raw_data: "type_defs.GetAssetPropertyAggregatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def aggregatedValues(self):  # pragma: no cover
        return AggregatedValue.make_many(self.boto3_raw_data["aggregatedValues"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAssetPropertyAggregatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetPropertyAggregatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetRelationshipsResponse:
    boto3_raw_data: "type_defs.ListAssetRelationshipsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assetRelationshipSummaries(self):  # pragma: no cover
        return AssetRelationshipSummary.make_many(
            self.boto3_raw_data["assetRelationshipSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssetRelationshipsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetRelationshipsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetModelCompositeModelsResponse:
    boto3_raw_data: "type_defs.ListAssetModelCompositeModelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assetModelCompositeModelSummaries(self):  # pragma: no cover
        return AssetModelCompositeModelSummary.make_many(
            self.boto3_raw_data["assetModelCompositeModelSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssetModelCompositeModelsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetModelCompositeModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionVariableOutput:
    boto3_raw_data: "type_defs.ExpressionVariableOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def value(self):  # pragma: no cover
        return VariableValueOutput.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpressionVariableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionVariableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputationModelDataBindingUsagesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListComputationModelDataBindingUsagesRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def dataBindingValueFilter(self):  # pragma: no cover
        return DataBindingValueFilter.make_one(
            self.boto3_raw_data["dataBindingValueFilter"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComputationModelDataBindingUsagesRequestPaginateTypeDef"
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
                "type_defs.ListComputationModelDataBindingUsagesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputationModelDataBindingUsagesRequest:
    boto3_raw_data: "type_defs.ListComputationModelDataBindingUsagesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataBindingValueFilter(self):  # pragma: no cover
        return DataBindingValueFilter.make_one(
            self.boto3_raw_data["dataBindingValueFilter"]
        )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComputationModelDataBindingUsagesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputationModelDataBindingUsagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchedDataBinding:
    boto3_raw_data: "type_defs.MatchedDataBindingTypeDef" = dataclasses.field()

    @cached_property
    def value(self):  # pragma: no cover
        return DataBindingValue.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MatchedDataBindingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchedDataBindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetPropertiesResponse:
    boto3_raw_data: "type_defs.ListAssetPropertiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def assetPropertySummaries(self):  # pragma: no cover
        return AssetPropertySummary.make_many(
            self.boto3_raw_data["assetPropertySummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetPropertiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetPropertiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetCompositeModel:
    boto3_raw_data: "type_defs.AssetCompositeModelTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @cached_property
    def properties(self):  # pragma: no cover
        return AssetProperty.make_many(self.boto3_raw_data["properties"])

    description = field("description")
    id = field("id")
    externalId = field("externalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetCompositeModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetCompositeModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetCompositeModelResponse:
    boto3_raw_data: "type_defs.DescribeAssetCompositeModelResponseTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    assetCompositeModelId = field("assetCompositeModelId")
    assetCompositeModelExternalId = field("assetCompositeModelExternalId")

    @cached_property
    def assetCompositeModelPath(self):  # pragma: no cover
        return AssetCompositeModelPathSegment.make_many(
            self.boto3_raw_data["assetCompositeModelPath"]
        )

    assetCompositeModelName = field("assetCompositeModelName")
    assetCompositeModelDescription = field("assetCompositeModelDescription")
    assetCompositeModelType = field("assetCompositeModelType")

    @cached_property
    def assetCompositeModelProperties(self):  # pragma: no cover
        return AssetProperty.make_many(
            self.boto3_raw_data["assetCompositeModelProperties"]
        )

    @cached_property
    def assetCompositeModelSummaries(self):  # pragma: no cover
        return AssetCompositeModelSummary.make_many(
            self.boto3_raw_data["assetCompositeModelSummaries"]
        )

    @cached_property
    def actionDefinitions(self):  # pragma: no cover
        return ActionDefinition.make_many(self.boto3_raw_data["actionDefinitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssetCompositeModelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetCompositeModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutAssetPropertyErrorEntry:
    boto3_raw_data: "type_defs.BatchPutAssetPropertyErrorEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchPutAssetPropertyError.make_many(self.boto3_raw_data["errors"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchPutAssetPropertyErrorEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutAssetPropertyErrorEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyAggregatesRequest:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyAggregatesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entries(self):  # pragma: no cover
        return BatchGetAssetPropertyAggregatesEntry.make_many(
            self.boto3_raw_data["entries"]
        )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyAggregatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyAggregatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueHistoryRequest:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entries(self):  # pragma: no cover
        return BatchGetAssetPropertyValueHistoryEntry.make_many(
            self.boto3_raw_data["entries"]
        )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueHistoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Image:
    boto3_raw_data: "type_defs.ImageTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def file(self):  # pragma: no cover
        return ImageFile.make_one(self.boto3_raw_data["file"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDefaultEncryptionConfigurationResponse:
    boto3_raw_data: (
        "type_defs.DescribeDefaultEncryptionConfigurationResponseTypeDef"
    ) = dataclasses.field()

    encryptionType = field("encryptionType")
    kmsKeyArn = field("kmsKeyArn")

    @cached_property
    def configurationStatus(self):  # pragma: no cover
        return ConfigurationStatus.make_one(self.boto3_raw_data["configurationStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDefaultEncryptionConfigurationResponseTypeDef"
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
                "type_defs.DescribeDefaultEncryptionConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDefaultEncryptionConfigurationResponse:
    boto3_raw_data: "type_defs.PutDefaultEncryptionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    encryptionType = field("encryptionType")
    kmsKeyArn = field("kmsKeyArn")

    @cached_property
    def configurationStatus(self):  # pragma: no cover
        return ConfigurationStatus.make_one(self.boto3_raw_data["configurationStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutDefaultEncryptionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDefaultEncryptionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobConfigurationOutput:
    boto3_raw_data: "type_defs.JobConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def fileFormat(self):  # pragma: no cover
        return FileFormatOutput.make_one(self.boto3_raw_data["fileFormat"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobConfiguration:
    boto3_raw_data: "type_defs.JobConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def fileFormat(self):  # pragma: no cover
        return FileFormat.make_one(self.boto3_raw_data["fileFormat"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStorageConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeStorageConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    storageType = field("storageType")

    @cached_property
    def multiLayerStorage(self):  # pragma: no cover
        return MultiLayerStorage.make_one(self.boto3_raw_data["multiLayerStorage"])

    disassociatedDataStorage = field("disassociatedDataStorage")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @cached_property
    def configurationStatus(self):  # pragma: no cover
        return ConfigurationStatus.make_one(self.boto3_raw_data["configurationStatus"])

    lastUpdateDate = field("lastUpdateDate")
    warmTier = field("warmTier")

    @cached_property
    def warmTierRetentionPeriod(self):  # pragma: no cover
        return WarmTierRetentionPeriod.make_one(
            self.boto3_raw_data["warmTierRetentionPeriod"]
        )

    disallowIngestNullNaN = field("disallowIngestNullNaN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStorageConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStorageConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutStorageConfigurationRequest:
    boto3_raw_data: "type_defs.PutStorageConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    storageType = field("storageType")

    @cached_property
    def multiLayerStorage(self):  # pragma: no cover
        return MultiLayerStorage.make_one(self.boto3_raw_data["multiLayerStorage"])

    disassociatedDataStorage = field("disassociatedDataStorage")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    warmTier = field("warmTier")

    @cached_property
    def warmTierRetentionPeriod(self):  # pragma: no cover
        return WarmTierRetentionPeriod.make_one(
            self.boto3_raw_data["warmTierRetentionPeriod"]
        )

    disallowIngestNullNaN = field("disallowIngestNullNaN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutStorageConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutStorageConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutStorageConfigurationResponse:
    boto3_raw_data: "type_defs.PutStorageConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    storageType = field("storageType")

    @cached_property
    def multiLayerStorage(self):  # pragma: no cover
        return MultiLayerStorage.make_one(self.boto3_raw_data["multiLayerStorage"])

    disassociatedDataStorage = field("disassociatedDataStorage")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @cached_property
    def configurationStatus(self):  # pragma: no cover
        return ConfigurationStatus.make_one(self.boto3_raw_data["configurationStatus"])

    warmTier = field("warmTier")

    @cached_property
    def warmTierRetentionPeriod(self):  # pragma: no cover
        return WarmTierRetentionPeriod.make_one(
            self.boto3_raw_data["warmTierRetentionPeriod"]
        )

    disallowIngestNullNaN = field("disallowIngestNullNaN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutStorageConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutStorageConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteQueryResponsePaginator:
    boto3_raw_data: "type_defs.ExecuteQueryResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def columns(self):  # pragma: no cover
        return ColumnInfo.make_many(self.boto3_raw_data["columns"])

    @cached_property
    def rows(self):  # pragma: no cover
        return RowPaginator.make_many(self.boto3_raw_data["rows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExecuteQueryResponsePaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteQueryResponsePaginatorTypeDef"]
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
    def columns(self):  # pragma: no cover
        return ColumnInfo.make_many(self.boto3_raw_data["columns"])

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
class ExecuteQueryResponseWaiter:
    boto3_raw_data: "type_defs.ExecuteQueryResponseWaiterTypeDef" = dataclasses.field()

    @cached_property
    def columns(self):  # pragma: no cover
        return ColumnInfo.make_many(self.boto3_raw_data["columns"])

    @cached_property
    def rows(self):  # pragma: no cover
        return RowWaiter.make_many(self.boto3_raw_data["rows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteQueryResponseWaiterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteQueryResponseWaiterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAssetModelInterfaceRelationshipRequest:
    boto3_raw_data: "type_defs.PutAssetModelInterfaceRelationshipRequestTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    interfaceAssetModelId = field("interfaceAssetModelId")

    @cached_property
    def propertyMappingConfiguration(self):  # pragma: no cover
        return PropertyMappingConfiguration.make_one(
            self.boto3_raw_data["propertyMappingConfiguration"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAssetModelInterfaceRelationshipRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAssetModelInterfaceRelationshipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExecutionsResponse:
    boto3_raw_data: "type_defs.ListExecutionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def executionSummaries(self):  # pragma: no cover
        return ExecutionSummary.make_many(self.boto3_raw_data["executionSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExecutionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelStatus:
    boto3_raw_data: "type_defs.AssetModelStatusTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetModelStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetStatus:
    boto3_raw_data: "type_defs.AssetStatusTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputationModelStatus:
    boto3_raw_data: "type_defs.ComputationModelStatusTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputationModelStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputationModelStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetStatus:
    boto3_raw_data: "type_defs.DatasetStatusTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Measurement:
    boto3_raw_data: "type_defs.MeasurementTypeDef" = dataclasses.field()

    @cached_property
    def processingConfig(self):  # pragma: no cover
        return MeasurementProcessingConfig.make_one(
            self.boto3_raw_data["processingConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MeasurementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MeasurementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGatewayRequest:
    boto3_raw_data: "type_defs.CreateGatewayRequestTypeDef" = dataclasses.field()

    gatewayName = field("gatewayName")

    @cached_property
    def gatewayPlatform(self):  # pragma: no cover
        return GatewayPlatform.make_one(self.boto3_raw_data["gatewayPlatform"])

    gatewayVersion = field("gatewayVersion")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayResponse:
    boto3_raw_data: "type_defs.DescribeGatewayResponseTypeDef" = dataclasses.field()

    gatewayId = field("gatewayId")
    gatewayName = field("gatewayName")
    gatewayArn = field("gatewayArn")

    @cached_property
    def gatewayPlatform(self):  # pragma: no cover
        return GatewayPlatform.make_one(self.boto3_raw_data["gatewayPlatform"])

    gatewayVersion = field("gatewayVersion")

    @cached_property
    def gatewayCapabilitySummaries(self):  # pragma: no cover
        return GatewayCapabilitySummary.make_many(
            self.boto3_raw_data["gatewayCapabilitySummaries"]
        )

    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewaySummary:
    boto3_raw_data: "type_defs.GatewaySummaryTypeDef" = dataclasses.field()

    gatewayId = field("gatewayId")
    gatewayName = field("gatewayName")
    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")

    @cached_property
    def gatewayPlatform(self):  # pragma: no cover
        return GatewayPlatform.make_one(self.boto3_raw_data["gatewayPlatform"])

    gatewayVersion = field("gatewayVersion")

    @cached_property
    def gatewayCapabilitySummaries(self):  # pragma: no cover
        return GatewayCapabilitySummary.make_many(
            self.boto3_raw_data["gatewayCapabilitySummaries"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewaySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GatewaySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetSource:
    boto3_raw_data: "type_defs.DatasetSourceTypeDef" = dataclasses.field()

    sourceType = field("sourceType")
    sourceFormat = field("sourceFormat")

    @cached_property
    def sourceDetail(self):  # pragma: no cover
        return SourceDetail.make_one(self.boto3_raw_data["sourceDetail"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetReference:
    boto3_raw_data: "type_defs.DataSetReferenceTypeDef" = dataclasses.field()

    datasetArn = field("datasetArn")

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSetReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSetReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePortalResponse:
    boto3_raw_data: "type_defs.CreatePortalResponseTypeDef" = dataclasses.field()

    portalId = field("portalId")
    portalArn = field("portalArn")
    portalStartUrl = field("portalStartUrl")

    @cached_property
    def portalStatus(self):  # pragma: no cover
        return PortalStatus.make_one(self.boto3_raw_data["portalStatus"])

    ssoApplicationId = field("ssoApplicationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePortalResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePortalResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePortalResponse:
    boto3_raw_data: "type_defs.DeletePortalResponseTypeDef" = dataclasses.field()

    @cached_property
    def portalStatus(self):  # pragma: no cover
        return PortalStatus.make_one(self.boto3_raw_data["portalStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePortalResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePortalResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePortalResponse:
    boto3_raw_data: "type_defs.DescribePortalResponseTypeDef" = dataclasses.field()

    portalId = field("portalId")
    portalArn = field("portalArn")
    portalName = field("portalName")
    portalDescription = field("portalDescription")
    portalClientId = field("portalClientId")
    portalStartUrl = field("portalStartUrl")
    portalContactEmail = field("portalContactEmail")

    @cached_property
    def portalStatus(self):  # pragma: no cover
        return PortalStatus.make_one(self.boto3_raw_data["portalStatus"])

    portalCreationDate = field("portalCreationDate")
    portalLastUpdateDate = field("portalLastUpdateDate")

    @cached_property
    def portalLogoImageLocation(self):  # pragma: no cover
        return ImageLocation.make_one(self.boto3_raw_data["portalLogoImageLocation"])

    roleArn = field("roleArn")
    portalAuthMode = field("portalAuthMode")
    notificationSenderEmail = field("notificationSenderEmail")

    @cached_property
    def alarms(self):  # pragma: no cover
        return Alarms.make_one(self.boto3_raw_data["alarms"])

    portalType = field("portalType")
    portalTypeConfiguration = field("portalTypeConfiguration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePortalResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePortalResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortalSummary:
    boto3_raw_data: "type_defs.PortalSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    startUrl = field("startUrl")

    @cached_property
    def status(self):  # pragma: no cover
        return PortalStatus.make_one(self.boto3_raw_data["status"])

    description = field("description")
    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")
    roleArn = field("roleArn")
    portalType = field("portalType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortalSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortalSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePortalResponse:
    boto3_raw_data: "type_defs.UpdatePortalResponseTypeDef" = dataclasses.field()

    @cached_property
    def portalStatus(self):  # pragma: no cover
        return PortalStatus.make_one(self.boto3_raw_data["portalStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePortalResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePortalResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePortalRequest:
    boto3_raw_data: "type_defs.CreatePortalRequestTypeDef" = dataclasses.field()

    portalName = field("portalName")
    portalContactEmail = field("portalContactEmail")
    roleArn = field("roleArn")
    portalDescription = field("portalDescription")
    clientToken = field("clientToken")

    @cached_property
    def portalLogoImageFile(self):  # pragma: no cover
        return ImageFile.make_one(self.boto3_raw_data["portalLogoImageFile"])

    tags = field("tags")
    portalAuthMode = field("portalAuthMode")
    notificationSenderEmail = field("notificationSenderEmail")

    @cached_property
    def alarms(self):  # pragma: no cover
        return Alarms.make_one(self.boto3_raw_data["alarms"])

    portalType = field("portalType")
    portalTypeConfiguration = field("portalTypeConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePortalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePortalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPolicySummary:
    boto3_raw_data: "type_defs.AccessPolicySummaryTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def identity(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["identity"])

    @cached_property
    def resource(self):  # pragma: no cover
        return Resource.make_one(self.boto3_raw_data["resource"])

    permission = field("permission")
    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessPolicySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPolicySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPolicyRequest:
    boto3_raw_data: "type_defs.CreateAccessPolicyRequestTypeDef" = dataclasses.field()

    @cached_property
    def accessPolicyIdentity(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["accessPolicyIdentity"])

    @cached_property
    def accessPolicyResource(self):  # pragma: no cover
        return Resource.make_one(self.boto3_raw_data["accessPolicyResource"])

    accessPolicyPermission = field("accessPolicyPermission")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessPolicyResponse:
    boto3_raw_data: "type_defs.DescribeAccessPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    accessPolicyId = field("accessPolicyId")
    accessPolicyArn = field("accessPolicyArn")

    @cached_property
    def accessPolicyIdentity(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["accessPolicyIdentity"])

    @cached_property
    def accessPolicyResource(self):  # pragma: no cover
        return Resource.make_one(self.boto3_raw_data["accessPolicyResource"])

    accessPolicyPermission = field("accessPolicyPermission")
    accessPolicyCreationDate = field("accessPolicyCreationDate")
    accessPolicyLastUpdateDate = field("accessPolicyLastUpdateDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccessPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessPolicyRequest:
    boto3_raw_data: "type_defs.UpdateAccessPolicyRequestTypeDef" = dataclasses.field()

    accessPolicyId = field("accessPolicyId")

    @cached_property
    def accessPolicyIdentity(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["accessPolicyIdentity"])

    @cached_property
    def accessPolicyResource(self):  # pragma: no cover
        return Resource.make_one(self.boto3_raw_data["accessPolicyResource"])

    accessPolicyPermission = field("accessPolicyPermission")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertyValue:
    boto3_raw_data: "type_defs.AssetPropertyValueTypeDef" = dataclasses.field()

    @cached_property
    def value(self):  # pragma: no cover
        return Variant.make_one(self.boto3_raw_data["value"])

    @cached_property
    def timestamp(self):  # pragma: no cover
        return TimeInNanos.make_one(self.boto3_raw_data["timestamp"])

    quality = field("quality")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetPropertyValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertyValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterpolatedAssetPropertyValue:
    boto3_raw_data: "type_defs.InterpolatedAssetPropertyValueTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def timestamp(self):  # pragma: no cover
        return TimeInNanos.make_one(self.boto3_raw_data["timestamp"])

    @cached_property
    def value(self):  # pragma: no cover
        return Variant.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InterpolatedAssetPropertyValueTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterpolatedAssetPropertyValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyAggregatesResponse:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyAggregatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return BatchGetAssetPropertyAggregatesErrorEntry.make_many(
            self.boto3_raw_data["errorEntries"]
        )

    @cached_property
    def successEntries(self):  # pragma: no cover
        return BatchGetAssetPropertyAggregatesSuccessEntry.make_many(
            self.boto3_raw_data["successEntries"]
        )

    @cached_property
    def skippedEntries(self):  # pragma: no cover
        return BatchGetAssetPropertyAggregatesSkippedEntry.make_many(
            self.boto3_raw_data["skippedEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyAggregatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyAggregatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricOutput:
    boto3_raw_data: "type_defs.MetricOutputTypeDef" = dataclasses.field()

    @cached_property
    def window(self):  # pragma: no cover
        return MetricWindow.make_one(self.boto3_raw_data["window"])

    expression = field("expression")

    @cached_property
    def variables(self):  # pragma: no cover
        return ExpressionVariableOutput.make_many(self.boto3_raw_data["variables"])

    @cached_property
    def processingConfig(self):  # pragma: no cover
        return MetricProcessingConfig.make_one(self.boto3_raw_data["processingConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransformOutput:
    boto3_raw_data: "type_defs.TransformOutputTypeDef" = dataclasses.field()

    expression = field("expression")

    @cached_property
    def variables(self):  # pragma: no cover
        return ExpressionVariableOutput.make_many(self.boto3_raw_data["variables"])

    @cached_property
    def processingConfig(self):  # pragma: no cover
        return TransformProcessingConfig.make_one(
            self.boto3_raw_data["processingConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransformOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransformOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionVariable:
    boto3_raw_data: "type_defs.ExpressionVariableTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpressionVariableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComputationModelRequest:
    boto3_raw_data: "type_defs.CreateComputationModelRequestTypeDef" = (
        dataclasses.field()
    )

    computationModelName = field("computationModelName")

    @cached_property
    def computationModelConfiguration(self):  # pragma: no cover
        return ComputationModelConfiguration.make_one(
            self.boto3_raw_data["computationModelConfiguration"]
        )

    computationModelDataBinding = field("computationModelDataBinding")
    computationModelDescription = field("computationModelDescription")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateComputationModelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComputationModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComputationModelRequest:
    boto3_raw_data: "type_defs.UpdateComputationModelRequestTypeDef" = (
        dataclasses.field()
    )

    computationModelId = field("computationModelId")
    computationModelName = field("computationModelName")

    @cached_property
    def computationModelConfiguration(self):  # pragma: no cover
        return ComputationModelConfiguration.make_one(
            self.boto3_raw_data["computationModelConfiguration"]
        )

    computationModelDataBinding = field("computationModelDataBinding")
    computationModelDescription = field("computationModelDescription")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateComputationModelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComputationModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputationModelDataBindingUsageSummary:
    boto3_raw_data: "type_defs.ComputationModelDataBindingUsageSummaryTypeDef" = (
        dataclasses.field()
    )

    computationModelIds = field("computationModelIds")

    @cached_property
    def matchedDataBinding(self):  # pragma: no cover
        return MatchedDataBinding.make_one(self.boto3_raw_data["matchedDataBinding"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComputationModelDataBindingUsageSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputationModelDataBindingUsageSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutAssetPropertyValueResponse:
    boto3_raw_data: "type_defs.BatchPutAssetPropertyValueResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return BatchPutAssetPropertyErrorEntry.make_many(
            self.boto3_raw_data["errorEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchPutAssetPropertyValueResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutAssetPropertyValueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePortalRequest:
    boto3_raw_data: "type_defs.UpdatePortalRequestTypeDef" = dataclasses.field()

    portalId = field("portalId")
    portalName = field("portalName")
    portalContactEmail = field("portalContactEmail")
    roleArn = field("roleArn")
    portalDescription = field("portalDescription")

    @cached_property
    def portalLogoImage(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["portalLogoImage"])

    clientToken = field("clientToken")
    notificationSenderEmail = field("notificationSenderEmail")

    @cached_property
    def alarms(self):  # pragma: no cover
        return Alarms.make_one(self.boto3_raw_data["alarms"])

    portalType = field("portalType")
    portalTypeConfiguration = field("portalTypeConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePortalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePortalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBulkImportJobResponse:
    boto3_raw_data: "type_defs.DescribeBulkImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    jobName = field("jobName")
    jobStatus = field("jobStatus")
    jobRoleArn = field("jobRoleArn")

    @cached_property
    def files(self):  # pragma: no cover
        return File.make_many(self.boto3_raw_data["files"])

    @cached_property
    def errorReportLocation(self):  # pragma: no cover
        return ErrorReportLocation.make_one(self.boto3_raw_data["errorReportLocation"])

    @cached_property
    def jobConfiguration(self):  # pragma: no cover
        return JobConfigurationOutput.make_one(self.boto3_raw_data["jobConfiguration"])

    jobCreationDate = field("jobCreationDate")
    jobLastUpdateDate = field("jobLastUpdateDate")
    adaptiveIngestion = field("adaptiveIngestion")
    deleteFilesAfterImport = field("deleteFilesAfterImport")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBulkImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBulkImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelSummary:
    boto3_raw_data: "type_defs.AssetModelSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    description = field("description")
    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")

    @cached_property
    def status(self):  # pragma: no cover
        return AssetModelStatus.make_one(self.boto3_raw_data["status"])

    externalId = field("externalId")
    assetModelType = field("assetModelType")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetModelSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetModelCompositeModelResponse:
    boto3_raw_data: "type_defs.CreateAssetModelCompositeModelResponseTypeDef" = (
        dataclasses.field()
    )

    assetModelCompositeModelId = field("assetModelCompositeModelId")

    @cached_property
    def assetModelCompositeModelPath(self):  # pragma: no cover
        return AssetModelCompositeModelPathSegment.make_many(
            self.boto3_raw_data["assetModelCompositeModelPath"]
        )

    @cached_property
    def assetModelStatus(self):  # pragma: no cover
        return AssetModelStatus.make_one(self.boto3_raw_data["assetModelStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAssetModelCompositeModelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetModelCompositeModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetModelResponse:
    boto3_raw_data: "type_defs.CreateAssetModelResponseTypeDef" = dataclasses.field()

    assetModelId = field("assetModelId")
    assetModelArn = field("assetModelArn")

    @cached_property
    def assetModelStatus(self):  # pragma: no cover
        return AssetModelStatus.make_one(self.boto3_raw_data["assetModelStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetModelCompositeModelResponse:
    boto3_raw_data: "type_defs.DeleteAssetModelCompositeModelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assetModelStatus(self):  # pragma: no cover
        return AssetModelStatus.make_one(self.boto3_raw_data["assetModelStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAssetModelCompositeModelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetModelCompositeModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetModelInterfaceRelationshipResponse:
    boto3_raw_data: "type_defs.DeleteAssetModelInterfaceRelationshipResponseTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    interfaceAssetModelId = field("interfaceAssetModelId")
    assetModelArn = field("assetModelArn")

    @cached_property
    def assetModelStatus(self):  # pragma: no cover
        return AssetModelStatus.make_one(self.boto3_raw_data["assetModelStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAssetModelInterfaceRelationshipResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetModelInterfaceRelationshipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetModelResponse:
    boto3_raw_data: "type_defs.DeleteAssetModelResponseTypeDef" = dataclasses.field()

    @cached_property
    def assetModelStatus(self):  # pragma: no cover
        return AssetModelStatus.make_one(self.boto3_raw_data["assetModelStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssetModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAssetModelInterfaceRelationshipResponse:
    boto3_raw_data: "type_defs.PutAssetModelInterfaceRelationshipResponseTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    interfaceAssetModelId = field("interfaceAssetModelId")
    assetModelArn = field("assetModelArn")

    @cached_property
    def assetModelStatus(self):  # pragma: no cover
        return AssetModelStatus.make_one(self.boto3_raw_data["assetModelStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAssetModelInterfaceRelationshipResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAssetModelInterfaceRelationshipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssetModelCompositeModelResponse:
    boto3_raw_data: "type_defs.UpdateAssetModelCompositeModelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assetModelCompositeModelPath(self):  # pragma: no cover
        return AssetModelCompositeModelPathSegment.make_many(
            self.boto3_raw_data["assetModelCompositeModelPath"]
        )

    @cached_property
    def assetModelStatus(self):  # pragma: no cover
        return AssetModelStatus.make_one(self.boto3_raw_data["assetModelStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAssetModelCompositeModelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetModelCompositeModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssetModelResponse:
    boto3_raw_data: "type_defs.UpdateAssetModelResponseTypeDef" = dataclasses.field()

    @cached_property
    def assetModelStatus(self):  # pragma: no cover
        return AssetModelStatus.make_one(self.boto3_raw_data["assetModelStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssetModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetSummary:
    boto3_raw_data: "type_defs.AssetSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    assetModelId = field("assetModelId")
    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")

    @cached_property
    def status(self):  # pragma: no cover
        return AssetStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def hierarchies(self):  # pragma: no cover
        return AssetHierarchy.make_many(self.boto3_raw_data["hierarchies"])

    externalId = field("externalId")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedAssetsSummary:
    boto3_raw_data: "type_defs.AssociatedAssetsSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    assetModelId = field("assetModelId")
    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")

    @cached_property
    def status(self):  # pragma: no cover
        return AssetStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def hierarchies(self):  # pragma: no cover
        return AssetHierarchy.make_many(self.boto3_raw_data["hierarchies"])

    externalId = field("externalId")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatedAssetsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedAssetsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetResponse:
    boto3_raw_data: "type_defs.CreateAssetResponseTypeDef" = dataclasses.field()

    assetId = field("assetId")
    assetArn = field("assetArn")

    @cached_property
    def assetStatus(self):  # pragma: no cover
        return AssetStatus.make_one(self.boto3_raw_data["assetStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetResponse:
    boto3_raw_data: "type_defs.DeleteAssetResponseTypeDef" = dataclasses.field()

    @cached_property
    def assetStatus(self):  # pragma: no cover
        return AssetStatus.make_one(self.boto3_raw_data["assetStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetResponse:
    boto3_raw_data: "type_defs.DescribeAssetResponseTypeDef" = dataclasses.field()

    assetId = field("assetId")
    assetExternalId = field("assetExternalId")
    assetArn = field("assetArn")
    assetName = field("assetName")
    assetModelId = field("assetModelId")

    @cached_property
    def assetProperties(self):  # pragma: no cover
        return AssetProperty.make_many(self.boto3_raw_data["assetProperties"])

    @cached_property
    def assetHierarchies(self):  # pragma: no cover
        return AssetHierarchy.make_many(self.boto3_raw_data["assetHierarchies"])

    @cached_property
    def assetCompositeModels(self):  # pragma: no cover
        return AssetCompositeModel.make_many(
            self.boto3_raw_data["assetCompositeModels"]
        )

    assetCreationDate = field("assetCreationDate")
    assetLastUpdateDate = field("assetLastUpdateDate")

    @cached_property
    def assetStatus(self):  # pragma: no cover
        return AssetStatus.make_one(self.boto3_raw_data["assetStatus"])

    assetDescription = field("assetDescription")

    @cached_property
    def assetCompositeModelSummaries(self):  # pragma: no cover
        return AssetCompositeModelSummary.make_many(
            self.boto3_raw_data["assetCompositeModelSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAssetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssetResponse:
    boto3_raw_data: "type_defs.UpdateAssetResponseTypeDef" = dataclasses.field()

    @cached_property
    def assetStatus(self):  # pragma: no cover
        return AssetStatus.make_one(self.boto3_raw_data["assetStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputationModelSummary:
    boto3_raw_data: "type_defs.ComputationModelSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    type = field("type")
    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")

    @cached_property
    def status(self):  # pragma: no cover
        return ComputationModelStatus.make_one(self.boto3_raw_data["status"])

    version = field("version")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputationModelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputationModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComputationModelResponse:
    boto3_raw_data: "type_defs.CreateComputationModelResponseTypeDef" = (
        dataclasses.field()
    )

    computationModelId = field("computationModelId")
    computationModelArn = field("computationModelArn")

    @cached_property
    def computationModelStatus(self):  # pragma: no cover
        return ComputationModelStatus.make_one(
            self.boto3_raw_data["computationModelStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateComputationModelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComputationModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComputationModelResponse:
    boto3_raw_data: "type_defs.DeleteComputationModelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def computationModelStatus(self):  # pragma: no cover
        return ComputationModelStatus.make_one(
            self.boto3_raw_data["computationModelStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteComputationModelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComputationModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComputationModelResponse:
    boto3_raw_data: "type_defs.DescribeComputationModelResponseTypeDef" = (
        dataclasses.field()
    )

    computationModelId = field("computationModelId")
    computationModelArn = field("computationModelArn")
    computationModelName = field("computationModelName")
    computationModelDescription = field("computationModelDescription")

    @cached_property
    def computationModelConfiguration(self):  # pragma: no cover
        return ComputationModelConfiguration.make_one(
            self.boto3_raw_data["computationModelConfiguration"]
        )

    computationModelDataBinding = field("computationModelDataBinding")
    computationModelCreationDate = field("computationModelCreationDate")
    computationModelLastUpdateDate = field("computationModelLastUpdateDate")

    @cached_property
    def computationModelStatus(self):  # pragma: no cover
        return ComputationModelStatus.make_one(
            self.boto3_raw_data["computationModelStatus"]
        )

    computationModelVersion = field("computationModelVersion")

    @cached_property
    def actionDefinitions(self):  # pragma: no cover
        return ActionDefinition.make_many(self.boto3_raw_data["actionDefinitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeComputationModelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComputationModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComputationModelResponse:
    boto3_raw_data: "type_defs.UpdateComputationModelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def computationModelStatus(self):  # pragma: no cover
        return ComputationModelStatus.make_one(
            self.boto3_raw_data["computationModelStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateComputationModelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComputationModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetResponse:
    boto3_raw_data: "type_defs.CreateDatasetResponseTypeDef" = dataclasses.field()

    datasetId = field("datasetId")
    datasetArn = field("datasetArn")

    @cached_property
    def datasetStatus(self):  # pragma: no cover
        return DatasetStatus.make_one(self.boto3_raw_data["datasetStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetSummary:
    boto3_raw_data: "type_defs.DatasetSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    description = field("description")
    creationDate = field("creationDate")
    lastUpdateDate = field("lastUpdateDate")

    @cached_property
    def status(self):  # pragma: no cover
        return DatasetStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetResponse:
    boto3_raw_data: "type_defs.DeleteDatasetResponseTypeDef" = dataclasses.field()

    @cached_property
    def datasetStatus(self):  # pragma: no cover
        return DatasetStatus.make_one(self.boto3_raw_data["datasetStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDatasetResponse:
    boto3_raw_data: "type_defs.UpdateDatasetResponseTypeDef" = dataclasses.field()

    datasetId = field("datasetId")
    datasetArn = field("datasetArn")

    @cached_property
    def datasetStatus(self):  # pragma: no cover
        return DatasetStatus.make_one(self.boto3_raw_data["datasetStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysResponse:
    boto3_raw_data: "type_defs.ListGatewaysResponseTypeDef" = dataclasses.field()

    @cached_property
    def gatewaySummaries(self):  # pragma: no cover
        return GatewaySummary.make_many(self.boto3_raw_data["gatewaySummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetRequest:
    boto3_raw_data: "type_defs.CreateDatasetRequestTypeDef" = dataclasses.field()

    datasetName = field("datasetName")

    @cached_property
    def datasetSource(self):  # pragma: no cover
        return DatasetSource.make_one(self.boto3_raw_data["datasetSource"])

    datasetId = field("datasetId")
    datasetDescription = field("datasetDescription")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetResponse:
    boto3_raw_data: "type_defs.DescribeDatasetResponseTypeDef" = dataclasses.field()

    datasetId = field("datasetId")
    datasetArn = field("datasetArn")
    datasetName = field("datasetName")
    datasetDescription = field("datasetDescription")

    @cached_property
    def datasetSource(self):  # pragma: no cover
        return DatasetSource.make_one(self.boto3_raw_data["datasetSource"])

    @cached_property
    def datasetStatus(self):  # pragma: no cover
        return DatasetStatus.make_one(self.boto3_raw_data["datasetStatus"])

    datasetCreationDate = field("datasetCreationDate")
    datasetLastUpdateDate = field("datasetLastUpdateDate")
    datasetVersion = field("datasetVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDatasetRequest:
    boto3_raw_data: "type_defs.UpdateDatasetRequestTypeDef" = dataclasses.field()

    datasetId = field("datasetId")
    datasetName = field("datasetName")

    @cached_property
    def datasetSource(self):  # pragma: no cover
        return DatasetSource.make_one(self.boto3_raw_data["datasetSource"])

    datasetDescription = field("datasetDescription")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Reference:
    boto3_raw_data: "type_defs.ReferenceTypeDef" = dataclasses.field()

    @cached_property
    def dataset(self):  # pragma: no cover
        return DataSetReference.make_one(self.boto3_raw_data["dataset"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReferenceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortalsResponse:
    boto3_raw_data: "type_defs.ListPortalsResponseTypeDef" = dataclasses.field()

    @cached_property
    def portalSummaries(self):  # pragma: no cover
        return PortalSummary.make_many(self.boto3_raw_data["portalSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPortalsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortalsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPoliciesResponse:
    boto3_raw_data: "type_defs.ListAccessPoliciesResponseTypeDef" = dataclasses.field()

    @cached_property
    def accessPolicySummaries(self):  # pragma: no cover
        return AccessPolicySummary.make_many(
            self.boto3_raw_data["accessPolicySummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueHistorySuccessEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueHistorySuccessEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")

    @cached_property
    def assetPropertyValueHistory(self):  # pragma: no cover
        return AssetPropertyValue.make_many(
            self.boto3_raw_data["assetPropertyValueHistory"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueHistorySuccessEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueHistorySuccessEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueSuccessEntry:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueSuccessEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")

    @cached_property
    def assetPropertyValue(self):  # pragma: no cover
        return AssetPropertyValue.make_one(self.boto3_raw_data["assetPropertyValue"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueSuccessEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueSuccessEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetPropertyValueHistoryResponse:
    boto3_raw_data: "type_defs.GetAssetPropertyValueHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assetPropertyValueHistory(self):  # pragma: no cover
        return AssetPropertyValue.make_many(
            self.boto3_raw_data["assetPropertyValueHistory"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAssetPropertyValueHistoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetPropertyValueHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetPropertyValueResponse:
    boto3_raw_data: "type_defs.GetAssetPropertyValueResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def propertyValue(self):  # pragma: no cover
        return AssetPropertyValue.make_one(self.boto3_raw_data["propertyValue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAssetPropertyValueResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetPropertyValueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAssetPropertyValueEntry:
    boto3_raw_data: "type_defs.PutAssetPropertyValueEntryTypeDef" = dataclasses.field()

    entryId = field("entryId")

    @cached_property
    def propertyValues(self):  # pragma: no cover
        return AssetPropertyValue.make_many(self.boto3_raw_data["propertyValues"])

    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAssetPropertyValueEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAssetPropertyValueEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInterpolatedAssetPropertyValuesResponse:
    boto3_raw_data: "type_defs.GetInterpolatedAssetPropertyValuesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def interpolatedAssetPropertyValues(self):  # pragma: no cover
        return InterpolatedAssetPropertyValue.make_many(
            self.boto3_raw_data["interpolatedAssetPropertyValues"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInterpolatedAssetPropertyValuesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInterpolatedAssetPropertyValuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyTypeOutput:
    boto3_raw_data: "type_defs.PropertyTypeOutputTypeDef" = dataclasses.field()

    @cached_property
    def attribute(self):  # pragma: no cover
        return Attribute.make_one(self.boto3_raw_data["attribute"])

    @cached_property
    def measurement(self):  # pragma: no cover
        return Measurement.make_one(self.boto3_raw_data["measurement"])

    @cached_property
    def transform(self):  # pragma: no cover
        return TransformOutput.make_one(self.boto3_raw_data["transform"])

    @cached_property
    def metric(self):  # pragma: no cover
        return MetricOutput.make_one(self.boto3_raw_data["metric"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputationModelDataBindingUsagesResponse:
    boto3_raw_data: "type_defs.ListComputationModelDataBindingUsagesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataBindingUsageSummaries(self):  # pragma: no cover
        return ComputationModelDataBindingUsageSummary.make_many(
            self.boto3_raw_data["dataBindingUsageSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComputationModelDataBindingUsagesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputationModelDataBindingUsagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBulkImportJobRequest:
    boto3_raw_data: "type_defs.CreateBulkImportJobRequestTypeDef" = dataclasses.field()

    jobName = field("jobName")
    jobRoleArn = field("jobRoleArn")

    @cached_property
    def files(self):  # pragma: no cover
        return File.make_many(self.boto3_raw_data["files"])

    @cached_property
    def errorReportLocation(self):  # pragma: no cover
        return ErrorReportLocation.make_one(self.boto3_raw_data["errorReportLocation"])

    jobConfiguration = field("jobConfiguration")
    adaptiveIngestion = field("adaptiveIngestion")
    deleteFilesAfterImport = field("deleteFilesAfterImport")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBulkImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBulkImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetModelsResponse:
    boto3_raw_data: "type_defs.ListAssetModelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def assetModelSummaries(self):  # pragma: no cover
        return AssetModelSummary.make_many(self.boto3_raw_data["assetModelSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetsResponse:
    boto3_raw_data: "type_defs.ListAssetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def assetSummaries(self):  # pragma: no cover
        return AssetSummary.make_many(self.boto3_raw_data["assetSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedAssetsResponse:
    boto3_raw_data: "type_defs.ListAssociatedAssetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assetSummaries(self):  # pragma: no cover
        return AssociatedAssetsSummary.make_many(self.boto3_raw_data["assetSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociatedAssetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedAssetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComputationModelsResponse:
    boto3_raw_data: "type_defs.ListComputationModelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def computationModelSummaries(self):  # pragma: no cover
        return ComputationModelSummary.make_many(
            self.boto3_raw_data["computationModelSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListComputationModelsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComputationModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsResponse:
    boto3_raw_data: "type_defs.ListDatasetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def datasetSummaries(self):  # pragma: no cover
        return DatasetSummary.make_many(self.boto3_raw_data["datasetSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Citation:
    boto3_raw_data: "type_defs.CitationTypeDef" = dataclasses.field()

    @cached_property
    def reference(self):  # pragma: no cover
        return Reference.make_one(self.boto3_raw_data["reference"])

    @cached_property
    def content(self):  # pragma: no cover
        return Content.make_one(self.boto3_raw_data["content"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CitationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CitationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueHistoryResponse:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return BatchGetAssetPropertyValueHistoryErrorEntry.make_many(
            self.boto3_raw_data["errorEntries"]
        )

    @cached_property
    def successEntries(self):  # pragma: no cover
        return BatchGetAssetPropertyValueHistorySuccessEntry.make_many(
            self.boto3_raw_data["successEntries"]
        )

    @cached_property
    def skippedEntries(self):  # pragma: no cover
        return BatchGetAssetPropertyValueHistorySkippedEntry.make_many(
            self.boto3_raw_data["skippedEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueHistoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAssetPropertyValueResponse:
    boto3_raw_data: "type_defs.BatchGetAssetPropertyValueResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return BatchGetAssetPropertyValueErrorEntry.make_many(
            self.boto3_raw_data["errorEntries"]
        )

    @cached_property
    def successEntries(self):  # pragma: no cover
        return BatchGetAssetPropertyValueSuccessEntry.make_many(
            self.boto3_raw_data["successEntries"]
        )

    @cached_property
    def skippedEntries(self):  # pragma: no cover
        return BatchGetAssetPropertyValueSkippedEntry.make_many(
            self.boto3_raw_data["skippedEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAssetPropertyValueResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAssetPropertyValueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutAssetPropertyValueRequest:
    boto3_raw_data: "type_defs.BatchPutAssetPropertyValueRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entries(self):  # pragma: no cover
        return PutAssetPropertyValueEntry.make_many(self.boto3_raw_data["entries"])

    enablePartialEntryProcessing = field("enablePartialEntryProcessing")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchPutAssetPropertyValueRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutAssetPropertyValueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelPropertyOutput:
    boto3_raw_data: "type_defs.AssetModelPropertyOutputTypeDef" = dataclasses.field()

    name = field("name")
    dataType = field("dataType")

    @cached_property
    def type(self):  # pragma: no cover
        return PropertyTypeOutput.make_one(self.boto3_raw_data["type"])

    id = field("id")
    externalId = field("externalId")
    dataTypeSpec = field("dataTypeSpec")
    unit = field("unit")

    @cached_property
    def path(self):  # pragma: no cover
        return AssetModelPropertyPathSegment.make_many(self.boto3_raw_data["path"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetModelPropertyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelPropertyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelPropertySummary:
    boto3_raw_data: "type_defs.AssetModelPropertySummaryTypeDef" = dataclasses.field()

    name = field("name")
    dataType = field("dataType")

    @cached_property
    def type(self):  # pragma: no cover
        return PropertyTypeOutput.make_one(self.boto3_raw_data["type"])

    id = field("id")
    externalId = field("externalId")
    dataTypeSpec = field("dataTypeSpec")
    unit = field("unit")
    assetModelCompositeModelId = field("assetModelCompositeModelId")

    @cached_property
    def path(self):  # pragma: no cover
        return AssetModelPropertyPathSegment.make_many(self.boto3_raw_data["path"])

    @cached_property
    def interfaceSummaries(self):  # pragma: no cover
        return InterfaceSummary.make_many(self.boto3_raw_data["interfaceSummaries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetModelPropertySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelPropertySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Property:
    boto3_raw_data: "type_defs.PropertyTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    dataType = field("dataType")
    externalId = field("externalId")
    alias = field("alias")

    @cached_property
    def notification(self):  # pragma: no cover
        return PropertyNotification.make_one(self.boto3_raw_data["notification"])

    unit = field("unit")

    @cached_property
    def type(self):  # pragma: no cover
        return PropertyTypeOutput.make_one(self.boto3_raw_data["type"])

    @cached_property
    def path(self):  # pragma: no cover
        return AssetPropertyPathSegment.make_many(self.boto3_raw_data["path"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metric:
    boto3_raw_data: "type_defs.MetricTypeDef" = dataclasses.field()

    @cached_property
    def window(self):  # pragma: no cover
        return MetricWindow.make_one(self.boto3_raw_data["window"])

    expression = field("expression")
    variables = field("variables")

    @cached_property
    def processingConfig(self):  # pragma: no cover
        return MetricProcessingConfig.make_one(self.boto3_raw_data["processingConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Transform:
    boto3_raw_data: "type_defs.TransformTypeDef" = dataclasses.field()

    expression = field("expression")
    variables = field("variables")

    @cached_property
    def processingConfig(self):  # pragma: no cover
        return TransformProcessingConfig.make_one(
            self.boto3_raw_data["processingConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransformTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransformTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationOutput:
    boto3_raw_data: "type_defs.InvocationOutputTypeDef" = dataclasses.field()

    message = field("message")

    @cached_property
    def citations(self):  # pragma: no cover
        return Citation.make_many(self.boto3_raw_data["citations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvocationOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelCompositeModelOutput:
    boto3_raw_data: "type_defs.AssetModelCompositeModelOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    type = field("type")
    description = field("description")

    @cached_property
    def properties(self):  # pragma: no cover
        return AssetModelPropertyOutput.make_many(self.boto3_raw_data["properties"])

    id = field("id")
    externalId = field("externalId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssetModelCompositeModelOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelCompositeModelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetModelCompositeModelResponse:
    boto3_raw_data: "type_defs.DescribeAssetModelCompositeModelResponseTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    assetModelCompositeModelId = field("assetModelCompositeModelId")
    assetModelCompositeModelExternalId = field("assetModelCompositeModelExternalId")

    @cached_property
    def assetModelCompositeModelPath(self):  # pragma: no cover
        return AssetModelCompositeModelPathSegment.make_many(
            self.boto3_raw_data["assetModelCompositeModelPath"]
        )

    assetModelCompositeModelName = field("assetModelCompositeModelName")
    assetModelCompositeModelDescription = field("assetModelCompositeModelDescription")
    assetModelCompositeModelType = field("assetModelCompositeModelType")

    @cached_property
    def assetModelCompositeModelProperties(self):  # pragma: no cover
        return AssetModelPropertyOutput.make_many(
            self.boto3_raw_data["assetModelCompositeModelProperties"]
        )

    @cached_property
    def compositionDetails(self):  # pragma: no cover
        return CompositionDetails.make_one(self.boto3_raw_data["compositionDetails"])

    @cached_property
    def assetModelCompositeModelSummaries(self):  # pragma: no cover
        return AssetModelCompositeModelSummary.make_many(
            self.boto3_raw_data["assetModelCompositeModelSummaries"]
        )

    @cached_property
    def actionDefinitions(self):  # pragma: no cover
        return ActionDefinition.make_many(self.boto3_raw_data["actionDefinitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssetModelCompositeModelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetModelCompositeModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetModelPropertiesResponse:
    boto3_raw_data: "type_defs.ListAssetModelPropertiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assetModelPropertySummaries(self):  # pragma: no cover
        return AssetModelPropertySummary.make_many(
            self.boto3_raw_data["assetModelPropertySummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssetModelPropertiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetModelPropertiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositeModelProperty:
    boto3_raw_data: "type_defs.CompositeModelPropertyTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @cached_property
    def assetProperty(self):  # pragma: no cover
        return Property.make_one(self.boto3_raw_data["assetProperty"])

    id = field("id")
    externalId = field("externalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompositeModelPropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositeModelPropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseStream:
    boto3_raw_data: "type_defs.ResponseStreamTypeDef" = dataclasses.field()

    @cached_property
    def trace(self):  # pragma: no cover
        return Trace.make_one(self.boto3_raw_data["trace"])

    @cached_property
    def output(self):  # pragma: no cover
        return InvocationOutput.make_one(self.boto3_raw_data["output"])

    @cached_property
    def accessDeniedException(self):  # pragma: no cover
        return AccessDeniedException.make_one(
            self.boto3_raw_data["accessDeniedException"]
        )

    @cached_property
    def conflictingOperationException(self):  # pragma: no cover
        return ConflictingOperationException.make_one(
            self.boto3_raw_data["conflictingOperationException"]
        )

    @cached_property
    def internalFailureException(self):  # pragma: no cover
        return InternalFailureException.make_one(
            self.boto3_raw_data["internalFailureException"]
        )

    @cached_property
    def invalidRequestException(self):  # pragma: no cover
        return InvalidRequestException.make_one(
            self.boto3_raw_data["invalidRequestException"]
        )

    @cached_property
    def limitExceededException(self):  # pragma: no cover
        return LimitExceededException.make_one(
            self.boto3_raw_data["limitExceededException"]
        )

    @cached_property
    def resourceNotFoundException(self):  # pragma: no cover
        return ResourceNotFoundException.make_one(
            self.boto3_raw_data["resourceNotFoundException"]
        )

    @cached_property
    def throttlingException(self):  # pragma: no cover
        return ThrottlingException.make_one(self.boto3_raw_data["throttlingException"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResponseStreamTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetModelResponse:
    boto3_raw_data: "type_defs.DescribeAssetModelResponseTypeDef" = dataclasses.field()

    assetModelId = field("assetModelId")
    assetModelExternalId = field("assetModelExternalId")
    assetModelArn = field("assetModelArn")
    assetModelName = field("assetModelName")
    assetModelType = field("assetModelType")
    assetModelDescription = field("assetModelDescription")

    @cached_property
    def assetModelProperties(self):  # pragma: no cover
        return AssetModelPropertyOutput.make_many(
            self.boto3_raw_data["assetModelProperties"]
        )

    @cached_property
    def assetModelHierarchies(self):  # pragma: no cover
        return AssetModelHierarchy.make_many(
            self.boto3_raw_data["assetModelHierarchies"]
        )

    @cached_property
    def assetModelCompositeModels(self):  # pragma: no cover
        return AssetModelCompositeModelOutput.make_many(
            self.boto3_raw_data["assetModelCompositeModels"]
        )

    @cached_property
    def assetModelCompositeModelSummaries(self):  # pragma: no cover
        return AssetModelCompositeModelSummary.make_many(
            self.boto3_raw_data["assetModelCompositeModelSummaries"]
        )

    assetModelCreationDate = field("assetModelCreationDate")
    assetModelLastUpdateDate = field("assetModelLastUpdateDate")

    @cached_property
    def assetModelStatus(self):  # pragma: no cover
        return AssetModelStatus.make_one(self.boto3_raw_data["assetModelStatus"])

    assetModelVersion = field("assetModelVersion")

    @cached_property
    def interfaceDetails(self):  # pragma: no cover
        return InterfaceRelationship.make_many(self.boto3_raw_data["interfaceDetails"])

    eTag = field("eTag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAssetModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetPropertyResponse:
    boto3_raw_data: "type_defs.DescribeAssetPropertyResponseTypeDef" = (
        dataclasses.field()
    )

    assetId = field("assetId")
    assetExternalId = field("assetExternalId")
    assetName = field("assetName")
    assetModelId = field("assetModelId")

    @cached_property
    def assetProperty(self):  # pragma: no cover
        return Property.make_one(self.boto3_raw_data["assetProperty"])

    @cached_property
    def compositeModel(self):  # pragma: no cover
        return CompositeModelProperty.make_one(self.boto3_raw_data["compositeModel"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAssetPropertyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetPropertyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyType:
    boto3_raw_data: "type_defs.PropertyTypeTypeDef" = dataclasses.field()

    @cached_property
    def attribute(self):  # pragma: no cover
        return Attribute.make_one(self.boto3_raw_data["attribute"])

    @cached_property
    def measurement(self):  # pragma: no cover
        return Measurement.make_one(self.boto3_raw_data["measurement"])

    transform = field("transform")
    metric = field("metric")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertyTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeAssistantResponse:
    boto3_raw_data: "type_defs.InvokeAssistantResponseTypeDef" = dataclasses.field()

    body = field("body")
    conversationId = field("conversationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeAssistantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeAssistantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelPropertyDefinition:
    boto3_raw_data: "type_defs.AssetModelPropertyDefinitionTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    dataType = field("dataType")
    type = field("type")
    id = field("id")
    externalId = field("externalId")
    dataTypeSpec = field("dataTypeSpec")
    unit = field("unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetModelPropertyDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelPropertyDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelProperty:
    boto3_raw_data: "type_defs.AssetModelPropertyTypeDef" = dataclasses.field()

    name = field("name")
    dataType = field("dataType")
    type = field("type")
    id = field("id")
    externalId = field("externalId")
    dataTypeSpec = field("dataTypeSpec")
    unit = field("unit")

    @cached_property
    def path(self):  # pragma: no cover
        return AssetModelPropertyPathSegment.make_many(self.boto3_raw_data["path"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetModelPropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelPropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelCompositeModelDefinition:
    boto3_raw_data: "type_defs.AssetModelCompositeModelDefinitionTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    type = field("type")
    id = field("id")
    externalId = field("externalId")
    description = field("description")

    @cached_property
    def properties(self):  # pragma: no cover
        return AssetModelPropertyDefinition.make_many(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssetModelCompositeModelDefinitionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelCompositeModelDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetModelCompositeModelRequest:
    boto3_raw_data: "type_defs.CreateAssetModelCompositeModelRequestTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    assetModelCompositeModelName = field("assetModelCompositeModelName")
    assetModelCompositeModelType = field("assetModelCompositeModelType")
    assetModelCompositeModelExternalId = field("assetModelCompositeModelExternalId")
    parentAssetModelCompositeModelId = field("parentAssetModelCompositeModelId")
    assetModelCompositeModelId = field("assetModelCompositeModelId")
    assetModelCompositeModelDescription = field("assetModelCompositeModelDescription")
    clientToken = field("clientToken")
    composedAssetModelId = field("composedAssetModelId")

    @cached_property
    def assetModelCompositeModelProperties(self):  # pragma: no cover
        return AssetModelPropertyDefinition.make_many(
            self.boto3_raw_data["assetModelCompositeModelProperties"]
        )

    ifMatch = field("ifMatch")
    ifNoneMatch = field("ifNoneMatch")
    matchForVersionType = field("matchForVersionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAssetModelCompositeModelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetModelCompositeModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetModelRequest:
    boto3_raw_data: "type_defs.CreateAssetModelRequestTypeDef" = dataclasses.field()

    assetModelName = field("assetModelName")
    assetModelType = field("assetModelType")
    assetModelId = field("assetModelId")
    assetModelExternalId = field("assetModelExternalId")
    assetModelDescription = field("assetModelDescription")

    @cached_property
    def assetModelProperties(self):  # pragma: no cover
        return AssetModelPropertyDefinition.make_many(
            self.boto3_raw_data["assetModelProperties"]
        )

    @cached_property
    def assetModelHierarchies(self):  # pragma: no cover
        return AssetModelHierarchyDefinition.make_many(
            self.boto3_raw_data["assetModelHierarchies"]
        )

    @cached_property
    def assetModelCompositeModels(self):  # pragma: no cover
        return AssetModelCompositeModelDefinition.make_many(
            self.boto3_raw_data["assetModelCompositeModels"]
        )

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetModelCompositeModel:
    boto3_raw_data: "type_defs.AssetModelCompositeModelTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    description = field("description")
    properties = field("properties")
    id = field("id")
    externalId = field("externalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetModelCompositeModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetModelCompositeModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssetModelCompositeModelRequest:
    boto3_raw_data: "type_defs.UpdateAssetModelCompositeModelRequestTypeDef" = (
        dataclasses.field()
    )

    assetModelId = field("assetModelId")
    assetModelCompositeModelId = field("assetModelCompositeModelId")
    assetModelCompositeModelName = field("assetModelCompositeModelName")
    assetModelCompositeModelExternalId = field("assetModelCompositeModelExternalId")
    assetModelCompositeModelDescription = field("assetModelCompositeModelDescription")
    clientToken = field("clientToken")
    assetModelCompositeModelProperties = field("assetModelCompositeModelProperties")
    ifMatch = field("ifMatch")
    ifNoneMatch = field("ifNoneMatch")
    matchForVersionType = field("matchForVersionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAssetModelCompositeModelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetModelCompositeModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssetModelRequest:
    boto3_raw_data: "type_defs.UpdateAssetModelRequestTypeDef" = dataclasses.field()

    assetModelId = field("assetModelId")
    assetModelName = field("assetModelName")
    assetModelExternalId = field("assetModelExternalId")
    assetModelDescription = field("assetModelDescription")
    assetModelProperties = field("assetModelProperties")

    @cached_property
    def assetModelHierarchies(self):  # pragma: no cover
        return AssetModelHierarchy.make_many(
            self.boto3_raw_data["assetModelHierarchies"]
        )

    assetModelCompositeModels = field("assetModelCompositeModels")
    clientToken = field("clientToken")
    ifMatch = field("ifMatch")
    ifNoneMatch = field("ifNoneMatch")
    matchForVersionType = field("matchForVersionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssetModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
